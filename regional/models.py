from django.db import models
from django.contrib.gis.db import models as mdls


# All models automatically created by inspectdb, primary keys assigned to index or date fields
class RegCases(models.Model):
    index = models.BigIntegerField(blank=True,primary_key=True)
    region = models.TextField(blank=True, null=True)
    sum_cases = models.FloatField(blank=True, null=True)
    sum_deaths = models.FloatField(blank=True, null=True)
    sum_recoveries = models.FloatField(blank=True, null=True)
    inactive_cases = models.FloatField(blank=True, null=True)
    active_cases = models.FloatField(blank=True, null=True)
    rise_today = models.FloatField(blank=True, null=True)
    rise_yesterday = models.FloatField(blank=True, null=True)
    number_7_day_mean_per_100k = models.FloatField(db_column='7_day_mean_per_100k', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    population = models.FloatField(blank=True, null=True)
    cases_per_1000 = models.FloatField(blank=True, null=True)
    deaths_per_1000 = models.FloatField(blank=True, null=True)
    active_per_1000 = models.FloatField(blank=True, null=True)
    cases_per_death = models.FloatField(blank=True, null=True)
    pct_of_deaths = models.FloatField(blank=True, null=True)
    pct_healthy = models.FloatField(blank=True, null=True)
    pct_active = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reg_cases'

class PlMap(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    region = models.TextField(blank=True, null=True)
    geometry = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_map'


class NewCasesRegional(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)  # Field renamed because it wasn't a valid Python identifier.
    dolnoslaskie = models.TextField(blank=True, null=True)
    kujawsko_pomorskie = models.TextField(db_column='kujawsko-pomorskie', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lubelskie = models.TextField(blank=True, null=True)
    lubuskie = models.TextField(blank=True, null=True)
    lodzkie = models.TextField(blank=True, null=True)
    malopolskie = models.TextField(blank=True, null=True)
    mazowieckie = models.TextField(blank=True, null=True)
    opolskie = models.TextField(blank=True, null=True)
    podkarpackie = models.TextField(blank=True, null=True)
    podlaskie = models.TextField(blank=True, null=True)
    pomorskie = models.TextField(blank=True, null=True)
    slaskie = models.TextField(blank=True, null=True)
    swietokrzyskie = models.TextField(blank=True, null=True)
    war_maz = models.TextField(db_column='war-maz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wielkopolskie = models.TextField(blank=True, null=True)
    zachodniopomorskie = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_cases_regional'
    
class NewDeathsRegional(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)  # Field renamed because it wasn't a valid Python identifier.
    dolnoslaskie = models.TextField(blank=True, null=True)
    kujawsko_pomorskie = models.TextField(db_column='kujawsko-pomorskie', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lubelskie = models.TextField(blank=True, null=True)
    lubuskie = models.TextField(blank=True, null=True)
    lodzkie = models.TextField(blank=True, null=True)
    malopolskie = models.TextField(blank=True, null=True)
    mazowieckie = models.TextField(blank=True, null=True)
    opolskie = models.TextField(blank=True, null=True)
    podkarpackie = models.TextField(blank=True, null=True)
    podlaskie = models.TextField(blank=True, null=True)
    pomorskie = models.TextField(blank=True, null=True)
    slaskie = models.TextField(blank=True, null=True)
    swietokrzyskie = models.TextField(blank=True, null=True)
    war_maz = models.TextField(db_column='war-maz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wielkopolskie = models.TextField(blank=True, null=True)
    zachodniopomorskie = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_deaths_regional'

class HospInDolnoslaskie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_dolnoslaskie'


class HospInKujawskoPomorskie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_kujawsko_pomorskie'


class HospInLodzkie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_lodzkie'


class HospInLubelskie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_lubelskie'


class HospInLubuskie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_lubuskie'


class HospInMalopolskie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_malopolskie'


class HospInMazowieckie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_mazowieckie'


class HospInOpolskie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_opolskie'


class HospInPodkarpackie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_podkarpackie'


class HospInPodlaskie(models.Model):
    date = models.DateTimeField(blank=True,primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_podlaskie'


class HospInPomorskie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_pomorskie'


class HospInSlaskie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_slaskie'


class HospInSwietokrzyskie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_swietokrzyskie'


class HospInWarminskoMazurskie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_warminsko_mazurskie'


class HospInWielkopolskie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_wielkopolskie'


class HospInZachodniopomorskie(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    hospitalized = models.FloatField(blank=True, null=True)
    change_d_d = models.FloatField(db_column='change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beds = models.FloatField(blank=True, null=True)
    pct_taken_beds = models.FloatField(blank=True, null=True)
    icu = models.FloatField(blank=True, null=True)
    icu_change_d_d = models.FloatField(db_column='icu_change_d/d', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    icu_beds = models.FloatField(blank=True, null=True)
    pct_taken_icu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp_in_zachodniopomorskie'


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

class RollingMean(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
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
        db_table = 'rolling_mean'


class RollingMeanPer100K(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
    dolnoslaskie = models.TextField(blank=True, null=True)
    kujawsko_pomorskie = models.TextField(db_column='kujawsko-pomorskie', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lubelskie = models.TextField(blank=True, null=True)
    lubuskie = models.TextField(blank=True, null=True)
    lodzkie = models.TextField(blank=True, null=True)
    malopolskie = models.TextField(blank=True, null=True)
    mazowieckie = models.TextField(blank=True, null=True)
    opolskie = models.TextField(blank=True, null=True)
    podkarpackie = models.TextField(blank=True, null=True)
    podlaskie = models.TextField(blank=True, null=True)
    pomorskie = models.TextField(blank=True, null=True)
    slaskie = models.TextField(blank=True, null=True)
    swietokrzyskie = models.TextField(blank=True, null=True)
    war_maz = models.TextField(db_column='war-maz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wielkopolskie = models.TextField(blank=True, null=True)
    zachodniopomorskie = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling_mean_per_100k'

class DailyPositivePct(models.Model):
    date = models.DateTimeField(blank=True, primary_key=True)
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
        db_table = 'daily_positive_pct'