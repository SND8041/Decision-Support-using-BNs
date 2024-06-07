from django import forms
from .models import Scenario

#I have updated the following class based on the work on model reported in Paper 2.
class ScenarioForm_Admin(forms.ModelForm):
    class Meta:
        model = Scenario
        fields = ('name','season','temperature', 'sea_state', 'days_at_sea', 'voyage_geography', 'recovery_method',
                  'quantity_of_oil','oil_type', 'hydrocarbonType',
                  'population_size', 'rise_in_food_cost','rise_in_health_expenses',
                  'compensation_amount', 'recovery_time', 'rate_of_biodegradation', 'social_discount_rate',
                  'soil_damage', 'response','crew_experience', 'vessel_size', 'hull',
                  'hole_size', 'material_strength', 'vessel_age', 'norgreg_zone', 'hunt_distrupt', 'cult_distrupt',
                  'association_distrupt','trust','water_effectOn','socio_distrupt','recovery_method',
                  )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'season': forms.Select(attrs={'class': 'form-control'}),
            'temperature': forms.Select(attrs={'class': 'form-control'}),
            'sea_state': forms.Select(attrs={'class': 'form-control'}),
            'recovery_method': forms.Select(attrs={'class': 'form-control'}),
            'quantity_of_oil': forms.TextInput(attrs={'class': 'form-control'}),
            'population_size': forms.TextInput(attrs={'class': 'form-control'}),
            'compensation_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'recovery_time': forms.TextInput(attrs={'class': 'form-control'}),
            'soil_damage': forms.Select(attrs={'class': 'form-control'}),
            'response': forms.Select(attrs={'class': 'form-control'}),
            'crew_experience': forms.Select(attrs={'class': 'form-control'}),
            'vessel_size': forms.Select(attrs={'class': 'form-control'}),
            'material_strength': forms.Select(attrs={'class': 'form-control'}),
            'hydrocarbonType': forms.Select(attrs={'class': 'form-control'}),
            'rate_of_biodegradation': forms.TextInput(attrs={'class': 'form-control'}),
            'social_discount_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'rise_in_food_cost': forms.Select(attrs={'class': 'form-control'}),
            'rise_in_health_expenses': forms.Select(attrs={'class': 'form-control'}),
            'hull': forms.Select(attrs={'class': 'form-control'}),
            'hole_size': forms.Select(attrs={'class': 'form-control'}),
            'norgreg_zone': forms.Select(attrs={'class': 'form-control'}),
            'oil_type': forms.Select(attrs={'class': 'form-control'}),
            #'flora_fauna_destruc': forms.Select(attrs={'class': 'form-control'}),
            'hunt_distrupt': forms.Select(attrs={'class': 'form-control'}),
            'crew_experience': forms.Select(attrs={'class': 'form-control'}),
            'vessel_age': forms.Select(attrs={'class': 'form-control'}),
            'cult_distrupt': forms.Select(attrs={'class': 'form-control'}),
            'days_at_sea': forms.Select(attrs={'class': 'form-control'}),
            'association_distrupt': forms.Select(attrs={'class': 'form-control'}),
            'trust': forms.Select(attrs={'class': 'form-control'}),
            'water_effectOn': forms.Select(attrs={'class': 'form-control'}),
            'socio_distrupt': forms.Select(attrs={'class': 'form-control'}),
            'voyage_geography': forms.Select(attrs={'class': 'form-control'}),

        }

#this form will be used when an inuit users logs in
class ScenarioForm_CommunityUsers(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       # self.fields['season'].initial = 3 #Season.SUMMER, set here more initial values

    class Meta:
        model = Scenario
        fields = (
            'name',
            'season',
            'temperature',
            'sea_state',
           # 'recovery_method',
            'quantity_of_oil',
            'population_size',
           # 'compensation_amount',
            'recovery_time',
            #'rate_of_biodegradation', 'social_discount_rate',
            'hunt_distrupt',
            'cult_distrupt',
            'socio_distrupt',
            'trust',
          #  'association_distrupt',
            'psycholical_effect',
          #  'water_effectOn',
            'rise_in_food_cost',
            'rise_in_health_expenses',
                  )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'season': forms.Select(attrs={'class': 'form-control'}),
            'temperature': forms.Select(attrs={'class': 'form-control'}),
            'sea_state': forms.Select(attrs={'class': 'form-control'}),
           # 'recovery_method': forms.Select(attrs={'class': 'form-control'}),
            'quantity_of_oil': forms.TextInput(attrs={'class': 'form-control'}),
            'population_size': forms.TextInput(attrs={'class': 'form-control'}),
           # 'compensation_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'recovery_time': forms.TextInput(attrs={'class': 'form-control'}),
           # 'rate_of_biodegradation': forms.TextInput(attrs={'class': 'form-control'}),
           # 'social_discount_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'hunt_distrupt': forms.Select(attrs={'class': 'form-control'}),
            'cult_distrupt': forms.Select(attrs={'class': 'form-control'}),
            'socio_distrupt': forms.Select(attrs={'class': 'form-control'}),
            'trust': forms.Select(attrs={'class': 'form-control'}),
          #  'association_distrupt': forms.Select(attrs={'class': 'form-control'}),
            'psycholical_effect': forms.Select(attrs={'class': 'form-control'}),
         #   'water_effectOn': forms.Select(attrs={'class': 'form-control'}),
            'rise_in_food_cost': forms.Select(attrs={'class': 'form-control'}),
            'rise_in_health_expenses': forms.Select(attrs={'class': 'form-control'}),

        }


#this form will be used when an inuit users logs in
class ScenarioForm_EnvAgencyUsers(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       # self.fields['season'].initial = 3 #Season.SUMMER, set here more initial values

    class Meta:
        model = Scenario
        fields = ('name','season','temperature', 'sea_state', 'recovery_method',
                  'quantity_of_oil', 'population_size', 'compensation_amount',
                  'recovery_time', 'rate_of_biodegradation', 'social_discount_rate',

                  'oil_type','flora_fauna_destruc','release','days_at_sea','water_effectOn',
                  )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'season': forms.Select(attrs={'class': 'form-control'}),
            'temperature': forms.Select(attrs={'class': 'form-control'}),
            'sea_state': forms.Select(attrs={'class': 'form-control'}),
            'recovery_method': forms.Select(attrs={'class': 'form-control'}),
            'quantity_of_oil': forms.TextInput(attrs={'class': 'form-control'}),
            'population_size': forms.TextInput(attrs={'class': 'form-control'}),
            'compensation_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'recovery_time': forms.TextInput(attrs={'class': 'form-control'}),
            'rate_of_biodegradation': forms.TextInput(attrs={'class': 'form-control'}),
            'social_discount_rate': forms.TextInput(attrs={'class': 'form-control'}),

            'oil_type': forms.Select(attrs={'class': 'form-control'}),
            'flora_fauna_destruc': forms.Select(attrs={'class': 'form-control'}),
            'release': forms.Select(attrs={'class': 'form-control'}),
            'days_at_sea': forms.Select(attrs={'class': 'form-control'}),
            'water_effectOn': forms.Select(attrs={'class': 'form-control'}),
        }

