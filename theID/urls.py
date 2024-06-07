from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import ListScenarios, EstSEIImpact

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('add_scenario', views.add_scenario, name='add-scenario'),
    path('list_scenarios', ListScenarios.as_view(), name='list-scenario'),
    path('sei_curr_scenario/<int:pk>', EstSEIImpact.as_view(), name="sei-curr-scenario"),#a DetailView
    path('delete_scenario/<scenario_id>', views.delete_scenario,name='delete-scenario'),
    path('delete_scenario_v2/<scenario_id>', views.delete_scenario_v2,name='delete-scenario-v2'),
    path('update_scenario/<scenario_id>', views.update_scenario,name='update-scenario'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
