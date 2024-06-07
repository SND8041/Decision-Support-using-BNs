from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# License issued by BayesFusion Licensing Server
# The code below must be executed before any PySMILE object is created.
# You can use "import pysmile_license" or copy the pysmile.License
# call into your Python source code.
import pysmile
pysmile.License((
	b"SMILE LICENSE 2c7480a9 6d5b67f2 eb9f9a45 "
	b"Serial #: c5lkz636onmgxiv6svyercdc8 "
	b"Valid until: 2025-01-18 "
	b"Support ends on: 2025-01-18 "
	b"Issued for: Dr. Syed Danial "
	b"Organization: University of Manitoba "
	b""
	),[
	0x60,0xe1,0xbf,0xaf,0xac,0x5f,0x34,0x76,0x32,0xc9,0xce,0xa6,0xcf,0xd1,0x85,0x45,
	0xfd,0xbb,0xc2,0xac,0x6f,0x89,0xd6,0xf4,0x64,0x1f,0xd0,0xa5,0xca,0xaf,0x0f,0x17,
	0x22,0xb8,0x3c,0xdd,0x11,0x53,0x9c,0xfb,0xed,0x64,0x29,0xfb,0x3a,0x4d,0xa8,0xe4,
	0x9d,0x5c,0x67,0x66,0x6c,0x6e,0x06,0x52,0xa6,0xa3,0xe0,0xb7,0xb6,0xde,0xe3,0xf4])


class Scenario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # instead of project_id = IntegerField..., user will get the user info in the templetes
   # project_id = models.ForeignKey(ProjectDesc, on_delete=models.CASCADE)
    #scenario_id= models.IntegerField(primary_key=True)
    class YESNO(models.Model):
        Yes=1
        No=2
        OPTION=(
            (Yes,'Yes'),
            (No,'No')
        )
    class Season(models.Model):
        WINTER = 1
        SPRING = 2
        SUMMER = 3
        FALL = 4
        SEASON_CHOICES = (
            (WINTER, 'Winter'),
            (SPRING, 'Spring'),
            (SUMMER, 'Summer'),
            (FALL, 'Fall')
        )
    class TwoOptions(models.Model):
        LOW = 0
        HIGH = 1
        BINARY_CHOICES = (
            (LOW, 'Low'),
            (HIGH, 'High'),
        )
    class OilType(models.Model):
        LIGHT = 0
        MEDIUM = 1
        HEAVY = 2
        EXTRA_HEAVY = 3
        OIL_TYPE_CHOICES = (
            (LIGHT, 'Light'),
            (MEDIUM, 'Medium'),
            (HEAVY, 'Heavy'),
            (EXTRA_HEAVY, 'Extra Heavy'),
        )

    class Temperature(models.Model):
        HIGH_TEMPERATURE = 1
        MODERATE_TEMPERATURE = 2
        LOW_TEMPERATURE = 3
        TEMPERATURE_CHOICES = (
            (HIGH_TEMPERATURE, 'High'),
            (MODERATE_TEMPERATURE, 'Moderate'),
            (LOW_TEMPERATURE, 'Low')
        )

    class SeaState(models.Model):
        ROUGH_STATE = 1
        CALM_STATE = 2
        SEASTATE_CHOICES = ((ROUGH_STATE, 'Rough'), (CALM_STATE, 'Calm'))

    class RecoveryMethod(models.Model):
        NATURAL_ATTENUATION = 1
        DISPERSANT_USE = 2
        MECHANICAL_RECOVERY = 3
        IN_SITU_BURNING = 4
        RECOVERY_CHOICES = (
            (NATURAL_ATTENUATION, 'MNA'),
            (DISPERSANT_USE, 'dispersant use'),
            (MECHANICAL_RECOVERY, 'mechanical recovery'),
            (IN_SITU_BURNING, 'insitu burning')
        )
    class DaysSpentAtSea(models.Model):
        T5_15 = 1
        T15_25 = 2
        NUMBER_OF_DAYS = (
            (T5_15, '5-15 days'),
            (T15_25, '15-25 days'),
        )
    class Response(models.Model):
        Slow = 1
        Prompt = 2
        RESPONSE = (
            (Slow, 'Slow'),
            (Prompt, 'Prompt'),
        )
    class VESSEL_SIZE(models.Model):
        Small=1
        Big=2
        SIZE=(
            (Small,'Small'),
            (Big,'Big'),
        )
    class MATERIAL_STRENGTH(models.Model):
        Thin=1
        Thick=2
        STRENGTH=(
            (Thin,'Thin'),
            (Thick,'Thick'),
        )

    class HYDROCARBTYPE(models.Model):
        Toxic = 1
        Nontoxic = 2
        TYPE = (
            (Toxic, 'Toxic'),
            (Nontoxic, 'NonToxic'),
        )
    class SINGLEDOUBLE(models.Model):
        Single=1
        Double=2
        BINARY_CHOICES = (
            (Single, 'Single Hull'),
            (Double, 'Double Hull'),
        )
    class VOYAGE(models.Model):
        HeavyIce=1
        MediumIce=2
        LowIce=3
        ICED=(
            (HeavyIce, 'Heavily iced'),
            (MediumIce, 'Medium iced'),
            (LowIce, 'Low iced'),

        )
    class AGE(models.Model):
        Years15_20 = 1
        Years10_15 = 2
        Years5_10 = 3
        Years1_5 = 4
        OPTIONS = (
            (Years15_20, '15 to 20 years old'),
            (Years10_15, '10 to 15 years old'),
            (Years5_10, '5 to 10 years old'),
            (Years1_5, '1 to 5 years old'),
        )

    name = models.CharField(max_length=50)
    season = models.IntegerField(choices=Season.SEASON_CHOICES, default=Season.SUMMER)
    temperature= models.IntegerField(verbose_name="Temperature",choices=Temperature.TEMPERATURE_CHOICES, default=Temperature.MODERATE_TEMPERATURE)
    sea_state=models.IntegerField(choices=SeaState.SEASTATE_CHOICES, default=SeaState.ROUGH_STATE)
    recovery_method = models.IntegerField(choices=RecoveryMethod.RECOVERY_CHOICES, default=RecoveryMethod.NATURAL_ATTENUATION)
    quantity_of_oil=models.IntegerField(verbose_name="Quantity of oil spilled (in US gallons)")
    population_size=models.IntegerField(verbose_name="Population size of the affected community")
    compensation_amount=models.FloatField(verbose_name="An estimate of the compensation the government has announced")
    recovery_time=models.IntegerField(verbose_name="For how many years do you want to see the impact?")
    rate_of_biodegradation=0.02133 #(mg/Lhr)
    rate_of_biodegradation=models.FloatField(default=0.02133,help_text='Rate of biodegradation of spilled oil, a default value is set to 0.02133 mg/Lhr')
    social_discount_rate=0.035
    social_discount_rate=models.FloatField(default=0.035,help_text='The social discount rate, a default value is set to 0.035')
    socioeconomic_impact=models.FloatField(default=0.0)
    psycholical_effect = models.IntegerField(choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)
    soil_damage = models.IntegerField(verbose_name="The damage to soil in the seas", choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)
    response = models.IntegerField(verbose_name="Was response fast or slow?", choices=Response.RESPONSE, default=Response.Prompt)
    vessel_size = models.IntegerField(verbose_name="What was the size of the ship or vessel causing the spill?", choices=VESSEL_SIZE.SIZE, default=VESSEL_SIZE.Small)
    material_strength = models.IntegerField(verbose_name="Was the material of manufacture of the vessel thin or thick?",choices=MATERIAL_STRENGTH.STRENGTH, default=MATERIAL_STRENGTH.Thick)
    hydrocarbonType=models.IntegerField(verbose_name="The toxity of the hydrocarbon release, light oil is usually toxic?",choices=HYDROCARBTYPE.TYPE, default=HYDROCARBTYPE.Toxic)
    hull = models.IntegerField(choices=SINGLEDOUBLE.BINARY_CHOICES, default=SINGLEDOUBLE.Single)
    hole_size = models.IntegerField(choices=VESSEL_SIZE.SIZE, default=VESSEL_SIZE.Small)
    voyage_geography = models.IntegerField(choices=VOYAGE.ICED, default=VOYAGE.HeavyIce)
    norgreg_zone = models.IntegerField(choices=YESNO.OPTION, default=YESNO.Yes)
    crew_experience = models.IntegerField(choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)
    vessel_age = models.IntegerField(choices=AGE.OPTIONS, default=AGE.Years10_15)




    # model values for Only Inuit users
    hunt_distrupt = models.IntegerField(verbose_name="How do you grade the impact of this spill scenario on hunting activities, such as fishing?",choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)
    cult_distrupt = models.IntegerField(verbose_name="How do you grade the impact of this spill on disruption of cultural activities, such as cultural events like certain practices of worship?",choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)
    socio_distrupt = models.IntegerField(verbose_name="How do you grade the impact of this spill on social harmony among the community members?",choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)
    trust = models.IntegerField(verbose_name="How do you grade a likely distrust between community and the federal government if the recovery is slow?",choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)
    association_distrupt = models.IntegerField(choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)
    water_effectOn = models.IntegerField(choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)
    rise_in_food_cost       = models.IntegerField(verbose_name="How do you grade the rise in food cost by the impact of this spill?", choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)
    rise_in_health_expenses = models.IntegerField(verbose_name="How do you grade the rise in health expenses by the impact of this spill?", choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)

# model values for Only environment users (env001)
    oil_type = models.IntegerField(choices=OilType.OIL_TYPE_CHOICES, default=OilType.MEDIUM)
    flora_fauna_destruc = models.IntegerField(choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)
    release = models.IntegerField(choices=TwoOptions.BINARY_CHOICES, default=TwoOptions.LOW)
    days_at_sea = models.IntegerField(choices=DaysSpentAtSea.NUMBER_OF_DAYS, default=DaysSpentAtSea.T5_15)



    def save(self, *args, **kwargs):
        self.updatesei()
        super().save(*args, **kwargs)

    def updatesei(self):
        #sei=0.0
        net=pysmile.Network()
        net.read_file("Latest_Canadain_Arctic_Model v2_18-Final-for-paper.xdsl")
        self.updateNetwork(net)
        if net.is_value_valid("SocImp"):
            sei=net.get_node_value("SocImp")
            self.socioeconomic_impact = sei[0]    #here you should use the Network object to


    def updateNetwork(self, net):
        # Model items for All types of Users
        #clears all previous evidence
        net.clear_all_evidence()
        if self.season == self.Season.WINTER:
            node_id="Season"
            new_evidence="Winter"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.season == self.Season.SUMMER:
            node_id="Season"
            new_evidence="Summer"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.season == self.Season.SPRING:
            node_id="Season"
            new_evidence="Spring"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.season == self.Season.FALL:
            node_id="Season"
            new_evidence="Fall"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id ="Season"
        # Updating the node Temperature
        if self.temperature == self.Temperature.LOW_TEMPERATURE:
            node_id="Temperature"
            new_evidence="Low"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.temperature == self.Temperature.MODERATE_TEMPERATURE:
            node_id="Temperature"
            new_evidence="Moderate"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.temperature == self.Temperature.HIGH_TEMPERATURE:
            node_id="Temperature"
            new_evidence="High"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id ="Temperature"
        # Updating the node Sea State
        if self.sea_state == self.SeaState.CALM_STATE:
            node_id="Sea_State"
            new_evidence="Calm"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.sea_state == self.SeaState.ROUGH_STATE:
            node_id="Sea_State"
            new_evidence="Rough"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id ="Sea_State"
        # Updating the node Recovery Method
        if self.recovery_method == self.RecoveryMethod.NATURAL_ATTENUATION:
            node_id="Recovery_method"
            new_evidence="Natural_Attenuation"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.recovery_method == self.RecoveryMethod.MECHANICAL_RECOVERY:
            node_id="Recovery_method"
            new_evidence="Mechanical"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.recovery_method == self.RecoveryMethod.DISPERSANT_USE:
            node_id="Recovery_method"
            new_evidence="Dispersant"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.recovery_method == self.RecoveryMethod.IN_SITU_BURNING:
            node_id="Recovery_method"
            new_evidence="Insitu"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Recovery_method"


        # Updating the node Quantity of oil

        node_id = "Quantityofoil"   #the amount is in US gallons
        qtyTons=self.quantity_of_oil*0.00372487
        if  qtyTons> 7.0 and qtyTons< 700.0: #(in galons)
            new_evidence="T_7_700"
        elif qtyTons >= 700.0:
            new_evidence="T_greatherthan_700"
        else:
            new_evidence="T_lessthan_7"
        self.set_evidence_and_update(net, node_id, new_evidence)

        # Model items for Users in the Inuit Group
        if self.hunt_distrupt == self.TwoOptions.LOW:
            node_id="Hunting_disruption"
            new_evidence="Low"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.hunt_distrupt == self.TwoOptions.HIGH:
            node_id="Hunting_disruption"
            new_evidence="High"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id="Hunting_disruption"


        if self.cult_distrupt == self.TwoOptions.LOW:
            node_id="Cultureinteference"
            new_evidence="Low_impact"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.hunt_distrupt == self.TwoOptions.HIGH:
            node_id="Cultureinteference"
            new_evidence="High_impact"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id="Cultureinteference"


        if self.socio_distrupt == self.TwoOptions.LOW:
            node_id="Social_disruption"
            new_evidence="Low"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.socio_distrupt == self.TwoOptions.HIGH:
            node_id="Social_disruption"
            new_evidence="High"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id="Social_disruption"
            #new_evidence=None
            #self.set_evidence_and_update(net, node_id, new_evidence)

        if self.trust == self.TwoOptions.LOW:
            node_id="Leveloftrust"
            new_evidence="Low"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.trust == self.TwoOptions.HIGH:
            node_id="Leveloftrust"
            new_evidence="High"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id="Leveloftrust"
            #new_evidence=None
            #self.set_evidence_and_update(net, node_id, new_evidence)

        if self.water_effectOn == self.TwoOptions.LOW:
            node_id="Decreaseinwatersupply"
            new_evidence="Low"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.water_effectOn == self.TwoOptions.HIGH:
            node_id="Decreaseinwatersupply"
            new_evidence="High"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id="Decreaseinwatersupply"
            #new_evidence=None
            #self.set_evidence_and_update(net, node_id, new_evidence)

#        if self.psycholical_effect == self.TwoOptions.LOW:
#            node_id = "Psychologicaleffect"
#            new_evidence = "Low"
#            self.set_evidence_and_update(net, node_id, new_evidence)
#        elif self.psycholical_effect == self.TwoOptions.HIGH:
#            node_id = "Psychologicaleffect"
#            new_evidence = "High"
#            self.set_evidence_and_update(net, node_id, new_evidence)
#        else:
#            node_id = "Psychologicaleffect"
#            print("No psychological node set")
            #new_evidence = None
            #self.set_evidence_and_update(net, node_id, new_evidence)

        if self.association_distrupt == self.TwoOptions.LOW:
            node_id = "Disruptioninassociation"
            new_evidence = "Low"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.association_distrupt == self.TwoOptions.HIGH:
            node_id = "Disruptioninassociation"
            new_evidence = "High"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Disruptioninassociation"

            # Model items for Users in the environment Group
        if self.oil_type == self.OilType.LIGHT:
            print("Test 3 in oil type 1")
            node_id = "Typeofoil"
            new_evidence = "Light"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.oil_type == self.OilType.MEDIUM:
            print("Test 3 in oil type 2")
            node_id = "Typeofoil"
            new_evidence = "Medium"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.oil_type == self.OilType.HEAVY:
            print("Test 3 in oil type 3")
            node_id = "Typeofoil"
            new_evidence = "Heavy"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.oil_type == self.OilType.EXTRA_HEAVY:
            print("Test 3 in oil type 4")
            node_id = "Typeofoil"
            new_evidence = "Extra_Heavy"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Typeofoil"
                # do nothing
###
#        if self.flora_fauna_destruc == self.TwoOptions.LOW:
#            node_id = "Destruction_of_flora_and_fauna"
#            new_evidence = "Low"
#            self.set_evidence_and_update(net, node_id, new_evidence)
#        elif self.flora_fauna_destruc == self.TwoOptions.HIGH:
#            node_id = "Destruction_of_flora_and_fauna"
#            new_evidence = "High"
#            self.set_evidence_and_update(net, node_id, new_evidence)
#        else:
#            node_id = "Destruction_of_flora_and_fauna"
#            print("Floar fauna not touched")
            # do nothing

#        if self.release == self.TwoOptions.LOW:
#            node_id = "Release"
#            new_evidence = "Low"
#            self.set_evidence_and_update(net, node_id, new_evidence)
#        elif self.release== self.TwoOptions.HIGH:
#            node_id = "Release"
#            new_evidence = "High"
#            self.set_evidence_and_update(net, node_id, new_evidence)
#        else:
#            node_id = "Release"
#                # do nothing

        if self.response == self.Response.Slow:
            node_id = "Response"
            new_evidence = "Slow"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.response== self.Response.Prompt:
            node_id = "Response"
            new_evidence = "Prompt"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Response"
                # do nothing

        if self.soil_damage == self.TwoOptions.LOW:
            node_id = "Soil_damage"
            new_evidence = "Low"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.soil_damage== self.TwoOptions.HIGH:
            node_id = "Soil_damage"
            new_evidence = "High"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Soil_damage"
                # do nothing


#        if self.days_at_sea == self.DaysSpentAtSea.T5_15:
#            node_id = "Daysexpectedtospendatsea"
#            new_evidence = "T5_15"
#            self.set_evidence_and_update(net, node_id, new_evidence)
#        elif self.days_at_sea == self.DaysSpentAtSea.T15_25:
#            node_id = "Daysexpectedtospendatsea"
#            new_evidence = "T15_25"
#            self.set_evidence_and_update(net, node_id, new_evidence)
#        else:
#            node_id = "Daysexpectedtospendatsea"
            # do nothing

        if self.vessel_size == self.VESSEL_SIZE.Small:
            node_id = "Size_of_ship"
            new_evidence = "Small"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.vessel_size == self.VESSEL_SIZE.Big:
            node_id = "Size_of_ship"
            new_evidence = "Big"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Size_of_ship"
            # do nothing

        if self.vessel_age == self.AGE.Years1_5:
            node_id = "Age_of_vessel"
            new_evidence = "T1_5"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.vessel_age == self.AGE.Years5_10:
            node_id = "Age_of_vessel"
            new_evidence = "T5_10"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.vessel_age == self.AGE.Years10_15:
            node_id = "Age_of_vessel"
            new_evidence = "T10_15"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.vessel_age == self.AGE.Years15_20:
            node_id = "Age_of_vessel"
            new_evidence = "T15_20"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Age_of_vessel"
            # do nothing

        if self.material_strength == self.MATERIAL_STRENGTH.Thin:
            node_id = "Material_ship_is_made_of"
            new_evidence = "Thin"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.material_strength == self.VESSEL_SIZE.Big:
            node_id = "Material_ship_is_made_of"
            new_evidence = "Thick"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "material_strength"
            # do nothing

        if self.hydrocarbonType == self.HYDROCARBTYPE.Toxic:
            node_id = "Type_of_hydrocarbon_released"
            new_evidence = "Toxic"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.hydrocarbonType == self.HYDROCARBTYPE.Nontoxic:
            node_id = "Type_of_hydrocarbon_released"
            new_evidence = "Non_toxic"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Type_of_hydrocarbon_released"
            # do nothing

        if self.hull == self.SINGLEDOUBLE.Single:
            node_id = "Hull"
            new_evidence = "Single_Hull"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.hull == self.SINGLEDOUBLE.Double:
            node_id = "Hull"
            new_evidence = "Double_Hull"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Hull"

        if self.hole_size == self.VESSEL_SIZE.Small:
            node_id = "Holesize"
            new_evidence = "Small"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.hole_size == self.VESSEL_SIZE.Big:
            node_id = "Holesize"
            new_evidence = "Big"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Holesize"

        if self.voyage_geography == self.VOYAGE.LowIce:
            node_id = "Geography_of_voyage"
            new_evidence = "Low_ice"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.voyage_geography == self.VOYAGE.MediumIce:
            node_id = "Geography_of_voyage"
            new_evidence = "Medium_ice"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.voyage_geography == self.VOYAGE.HeavyIce:
            node_id = "Geography_of_voyage"
            new_evidence = "Heavily_ice"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Geography_of_voyage"

        if self.crew_experience == self.TwoOptions.LOW:
            node_id = "Experienceofcrew"
            new_evidence = "Low_level_of_experience"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.crew_experience == self.TwoOptions.HIGH:
            node_id = "Experienceofcrew"
            new_evidence = "Experienced"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Experienceofcrew"

        if self.rise_in_food_cost == self.TwoOptions.LOW:
            node_id = "RiseInFoodCost"
            new_evidence = "Low"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.rise_in_food_cost == self.TwoOptions.HIGH:
            node_id = "RiseInFoodCost"
            new_evidence = "High"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "RiseInFoodCost"

        if self.rise_in_health_expenses == self.TwoOptions.LOW:
            node_id = "Rise_in_health_expenses"
            new_evidence = "Low"
            self.set_evidence_and_update(net, node_id, new_evidence)
        elif self.rise_in_health_expenses == self.TwoOptions.HIGH:
            node_id = "Rise_in_health_expenses"
            new_evidence = "High"
            self.set_evidence_and_update(net, node_id, new_evidence)
        else:
            node_id = "Rise_in_health_expenses"




#    New network functions
    def set_evidence_and_update(self, net, node_id, new_evidence):
        if new_evidence is not None:
            net.set_evidence(node_id, new_evidence)
        else:
            net.clear_evidence(node_id)
        net.update_beliefs()

    def __str__(self):
        return self.name


# Create your models here.
class ProjectDesc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None) #incstead of project_id = IntegerField..., this user will get the user info in the templetes

    project_id = models.IntegerField(primary_key=True)
    project_name=models.CharField(max_length=50,
                                   help_text="The name of the project for which data collection is being done.")
    location=models.CharField(max_length=50,
                                   help_text="The location where the data is mostly collected")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name

# The following Users' model is not to be confused with Django's authentication
# The two are different
# We will tie the below class with django's authentication later because in
# our OSDSS the two sets should be same.

class UsersOfOSDSS(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

