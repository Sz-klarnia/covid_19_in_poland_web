from django.db import models


# Models autogenerated using inspectdb function from manage.py django file. Primary keys set to index or date fields
class Cases(models.Model):
    index = models.BigIntegerField(blank=True,primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    new_cases = models.FloatField(blank=True, null=True)
    misreported_cases = models.FloatField(blank=True, null=True)
    cases_rise_pct = models.FloatField(blank=True, null=True)
    cases_rise_week_to_week = models.FloatField(blank=True, null=True)
    new_cases_pct_from_active = models.FloatField(blank=True, null=True)
    active_cases_rise_in_pct = models.FloatField(blank=True, null=True)
    new_deaths = models.FloatField(blank=True, null=True)
    new_recoveries = models.FloatField(blank=True, null=True)
    inactive_cases_rise = models.FloatField(blank=True, null=True)
    active_cases_rise = models.FloatField(blank=True, null=True)
    sum_cases = models.FloatField(blank=True, null=True)
    sum_deaths = models.FloatField(blank=True, null=True)
    sum_recoveries = models.FloatField(blank=True, null=True)
    inactive_cases = models.FloatField(blank=True, null=True)
    active_cases = models.FloatField(blank=True, null=True)
    pct_of_deaths_inactive_cases = models.FloatField(blank=True, null=True)
    pct_of_recoveries_inactive_cases = models.FloatField(blank=True, null=True)
    pct_of_deaths = models.FloatField(blank=True, null=True)
    pct_of_recoveries = models.FloatField(blank=True, null=True)
    pct_of_inactive_cases = models.FloatField(blank=True, null=True)
    pct_of_active_cases = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cases'

class Hospitalizations(models.Model):
    index = models.BigIntegerField(blank=True,primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pct_hospitalized_in_active = models.FloatField(blank=True, null=True)
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    pct_icu_in_hospitalized = models.FloatField(blank=True, null=True)
    icu_beds = models.FloatField(blank=True, null=True)
    quarantined_locally = models.FloatField(blank=True, null=True)
    from_abroad = models.FloatField(blank=True, null=True)
    quarantined = models.FloatField(blank=True, null=True)
    monitored_til_25_01 = models.FloatField(db_column='monitored_til_25.01', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'hospitalizations'

class Testing(models.Model):
    index = models.BigIntegerField(blank=True,primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    sum_tested_people = models.FloatField(blank=True, null=True)
    new_tested_people = models.FloatField(blank=True, null=True)
    sum_tests = models.FloatField(blank=True, null=True)
    tests_in_24h = models.FloatField(blank=True, null=True)
    antibody_tests = models.FloatField(blank=True, null=True)
    pct_of_antibody_tests = models.FloatField(db_column='pct of antibody tests', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sum_poz_orders = models.FloatField(db_column='sum_POZ_orders', blank=True, null=True)  # Field name made lowercase.
    poz_orders_24h = models.FloatField(db_column='POZ_orders_24h', blank=True, null=True)  # Field name made lowercase.
    poz_orders_week_to_week_pct = models.FloatField(db_column='POZ_orders_week_to_week_pct', blank=True, null=True)  # Field name made lowercase.
    sum_positive_tests = models.FloatField(blank=True, null=True)
    positive_tests_24h = models.FloatField(blank=True, null=True)
    pct_positive_in_samples = models.FloatField(blank=True, null=True)
    pct_positive_in_people = models.FloatField(blank=True, null=True)
    pct_24h_positivity_rate = models.FloatField(blank=True, null=True)
    pct_24h_positivity_rate_people = models.FloatField(blank=True, null=True)
    sum_negatives_and_second_positives = models.FloatField(blank=True, null=True)
    negatives_and_second_positives = models.FloatField(blank=True, null=True)
    number_7_day_mean_test_nr = models.FloatField(db_column='7_day_mean_test_nr', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_7_day_mean_positivity_rate = models.FloatField(db_column='7_day_mean_positivity_rate', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    class Meta:
        managed = False
        db_table = 'testing'

class Vaccinations(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    sum_vacc = models.TextField(blank=True, null=True)
    daily_vacc = models.FloatField(blank=True, null=True)
    people_vacc = models.FloatField(blank=True, null=True)
    pct_vacc = models.FloatField(blank=True, null=True)
    number_1_dose = models.FloatField(db_column='1_dose', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2_doses = models.FloatField(db_column='2_doses', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    nop_light = models.FloatField(blank=True, null=True)
    nop_serious = models.FloatField(blank=True, null=True)
    nop_severe = models.FloatField(blank=True, null=True)
    nop_death = models.FloatField(blank=True, null=True)
    f = models.FloatField(blank=True, null=True)
    m = models.FloatField(blank=True, null=True)
    doses_delivered = models.FloatField(blank=True, null=True)
    doses_to_points = models.FloatField(blank=True, null=True)
    utilized = models.FloatField(blank=True, null=True)
    used = models.FloatField(blank=True, null=True)
    number_18_30 = models.FloatField(db_column='18-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_31_40 = models.FloatField(db_column='31-40', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_41_50 = models.FloatField(db_column='41-50', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_51_60 = models.FloatField(db_column='51-60', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_61_70 = models.FloatField(db_column='61-70', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_71_75 = models.FloatField(db_column='71-75', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_75_field = models.FloatField(db_column='75+', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    dolnoslaskie = models.FloatField(blank=True, null=True)
    kujawsko_pomorskie = models.FloatField(db_column='kujawsko-pomorskie', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lubelskie = models.FloatField(blank=True, null=True)
    lubuskie = models.FloatField(blank=True, null=True)
    lodzkie = models.FloatField(blank=True, null=True)
    malopolskie = models.FloatField(blank=True, null=True)
    mazowieckie = models.FloatField(blank=True, null=True)
    opolskie = models.FloatField(blank=True, null=True)
    podkarpackie = models.FloatField(blank=True, null=True)
    podlaskie = models.FloatField(blank=True, null=True)
    pomorskie = models.FloatField(blank=True, null=True)
    slaskie = models.FloatField(blank=True, null=True)
    swietokrzyskie = models.FloatField(blank=True, null=True)
    war_maz = models.FloatField(db_column='war-maz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wielkopolskie = models.FloatField(blank=True, null=True)
    zachodniopomorskie = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vaccinations'
 