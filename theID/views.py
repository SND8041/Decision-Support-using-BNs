import base64
import io
import urllib.parse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView
from matplotlib.ticker import FuncFormatter

from theID.forms import ScenarioForm_Admin, ScenarioForm_CommunityUsers, ScenarioForm_EnvAgencyUsers
import matplotlib

matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np

import pysmile
from theID.models import Scenario
from theID.utils import getSEI
from theID.utils import millions

def about(request):
    return render(request, 'theID/about.html')


def home(request):
    return render(request, "theID/home.html")

#this function deletes a given scenario upon button click
def delete_scenario(request, scenario_id):
    scenario = Scenario.objects.get(pk=scenario_id)
    scenario.delete()
    return redirect('list-scenario')    #redirect back to the same page

#this function deletes a given scenario upon button click from a detail view page therefore it redirects to home
def delete_scenario_v2(request, scenario_id):
    scenario = Scenario.objects.get(pk=scenario_id)
    scenario.delete()
    return redirect('home')    #redirect back to the same page


def update_scenario(request, scenario_id):
    scenario = Scenario.objects.get(pk=scenario_id)
    if request.user.is_superuser:
        form = ScenarioForm_Admin(request.POST or None, instance=scenario)
    elif request.user.groups.filter(name="Inuit"):
        form = ScenarioForm_CommunityUsers(request.POST or None, instance=scenario)
    elif request.user.groups.filter(name="environment"):
        form = ScenarioForm_EnvAgencyUsers(request.POST or None, instance=scenario)
    else:
        return HttpResponseNotFound("No group user found")
    if form.is_valid(): #save the valid changes
        form.save()
        return redirect('list-scenario')#redirect to the list-view again
    return render(request, 'theID/update_scenario.html',{"scenario": scenario,
                                                         "form": form})    #redirect back to the same page

###############$$$ Class based views
def add_scenario(request):
    #submitFlag = False      #initially the form is not submitted
    if request.method == "POST":
        if request.user.is_superuser:
            form = ScenarioForm_Admin(request.POST)
        elif request.user.groups.filter(name="Inuit"):
            form = ScenarioForm_CommunityUsers(request.POST)
        elif request.user.groups.filter(name="environment"):
            form = ScenarioForm_EnvAgencyUsers(request.POST)
        else:
            return HttpResponseNotFound("No group user found")
        if form.is_valid():
            print("form is saving")
            newform = form.save(commit=False)   #
            newform.user = request.user     #this information will be saved in the model's user now
            newform.save()
            if hasattr(form, 'save_m2m'):
                form.save_m2m()
            print("The new record ", newform, " is added")
            return redirect("sei-curr-scenario", newform.pk)
    else:
        if request.user.is_superuser:
            form = ScenarioForm_Admin
        elif request.user.groups.filter(name="Inuit"):
            form = ScenarioForm_CommunityUsers(request.POST)
        elif request.user.groups.filter(name="environment"):
            form = ScenarioForm_EnvAgencyUsers(request.POST)
        else:
            return HttpResponseNotFound("No group user found")
     #   if 'submitFlag' in request.GET:  #is submitted is true, means a form has already been submitted
     #       submitFlag = True
    return render(request, 'theID/add_scenario.html', {'form': form})


'''
class AddScenarioView(CreateView):
    model = Scenario
    form_class = ScenarioForm
    template_name = "theID/add_scenario.html"

    def get_success_url(self):
        return reverse("sei-curr-scenario", kwargs={"pk": self.object.pk})

    # to add currently logged in user with every new scenario
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Inuit').exists():
            template_name = "theID/add_scenario.html"

'''
# The following class's object will be invoked when the submit button of the scenario
# entering form is clicked. It will fetch the details about the scenario added and
# calculate the net present value for sei estimation and finally plot the data with
# the required projection

# @login_required(login_url="login/")
class EstSEIImpact(DetailView):
    model = Scenario
    template_name = 'theID/sei_curr_scenario.html'

    def generate_plot2(self, year, seis):
        ######### Setting up canvas starts

        #---- create figure ----
        plt.close('all')
        plt.clf()
        fwidth = 7.  # total width of the figure in inches
        fheight = 5. # total height of the figure in inches
        fig = plt.figure(figsize=(fwidth, fheight))
        plt.style.use('ggplot')

        #---- define margins -> size in inches / figure dimension ----

        left_margin  = 1.25 / fwidth
        right_margin = 0.5 / fwidth
        bottom_margin = 0.5 / fheight
        top_margin = 0.35 / fheight

        #---- create axes ----

        # dimensions are calculated relative to the figure size

        x = left_margin    # horiz. position of bottom-left corner
        y = bottom_margin  # vert. position of bottom-left corner
        w = 1 - (left_margin + right_margin) # width of axes
        h = 1 - (bottom_margin + top_margin) # height of axes

        ax = fig.add_axes([x, y, w, h])
        formatter = FuncFormatter(millions)
        ax.yaxis.set_major_formatter(formatter)
        #---- Define the Ylabel position ----

        # Location are defined in dimension relative to the figure size

        xloc =  0.25 / fwidth
        yloc =  y + h / 2.
        ax.set_ylabel('yLabel', fontsize=14, verticalalignment='top',
              horizontalalignment='center')
        ax.yaxis.set_label_coords(xloc, yloc, transform = fig.transFigure)
        ######## Ending canvas

        x = []
        for i in range(year):
            x.append(i + 1)
        y_pos = np.arange(len(x))
        plt.bar(y_pos, seis, align='center', alpha=0.9)
        plt.xticks(y_pos, x)
        plt.ylabel('SEI impact in US dollars')
        plt.xlabel('Future projection (years)')
        plt.title('Siberian oil spill')
        print("Value of sei from views.py")
        print(y_pos, seis)


        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        buf.close()
        uri = urllib.parse.quote(string)
        print("The length of seis is: ", len(seis))
        print("The years is: ", len(x))

        return uri

    def get(self, request, *args, **kwargs):
        # kwargs contains the primary key of the recent scenario model's object
        recent_entry = None
        seis = []  # for one scenario there may be impacts for each years, that' why seis, not sei
        if 'pk' in kwargs:  # using this pk, retrieve record from DB and make a context with the_plot
            print("Value in kwargs is: ")
            print(kwargs.get("pk"))
            # a_scenario = Scenario.objects.all().filter(is_active=True, author__is_active=True).order_by('author')
            recent_entry = Scenario.objects.get(pk=kwargs.get("pk"))
            seis = getSEI(recent_entry)  # get the sei over the years

        # now generate the plot
        uri = self.generate_plot2(recent_entry.recovery_time, seis)

        return render(request, 'theID/sei_curr_scenario.html', {'object': recent_entry, 'data': uri})


class ListScenarios(ListView):
    model = Scenario
    template_name = 'theID/list_scenarios.html'

    def get(self, request, *args, **kwargs):
        scenario_list = Scenario.objects.filter(user=request.user)
        return render(request, 'theID/list_scenarios.html', {'scenario_list': scenario_list})
