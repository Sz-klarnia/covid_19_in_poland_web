from django.db import models

# Create your models here.
class ModellingData(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    date_x = models.TextField(blank=True, null=True)
    total_cases_per_million = models.FloatField(blank=True, null=True)
    new_cases_per_million = models.FloatField(blank=True, null=True)
    stringency_index = models.FloatField(blank=True, null=True)
    total_deaths_per_million = models.FloatField(blank=True, null=True)
    new_deaths_per_million = models.FloatField(blank=True, null=True)
    reproduction_rate = models.FloatField(blank=True, null=True)
    hosp_patients_per_million = models.FloatField(blank=True, null=True)
    new_tests_per_thousand = models.FloatField(blank=True, null=True)
    positive_rate = models.FloatField(blank=True, null=True)
    tests_per_case = models.FloatField(blank=True, null=True)
    total_vaccinations_per_hundred = models.FloatField(blank=True, null=True)
    people_vaccinated_per_hundred = models.FloatField(blank=True, null=True)
    people_fully_vaccinated_per_hundred = models.FloatField(blank=True, null=True)
    c1_school_closing = models.FloatField(db_column='C1_School closing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    c2_workplace_closing = models.FloatField(db_column='C2_Workplace closing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    c3_cancel_public_events = models.FloatField(db_column='C3_Cancel public events', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    c4_restrictions_on_gatherings = models.FloatField(db_column='C4_Restrictions on gatherings', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    c5_close_public_transport = models.FloatField(db_column='C5_Close public transport', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    c6_stay_at_home_requirements = models.FloatField(db_column='C6_Stay at home requirements', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    c7_restrictions_on_internal_movement = models.FloatField(db_column='C7_Restrictions on internal movement', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    c8_international_travel_controls = models.FloatField(db_column='C8_International travel controls', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    h1_public_information_campaigns = models.FloatField(db_column='H1_Public information campaigns', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    h2_testing_policy = models.FloatField(db_column='H2_Testing policy', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    h3_contact_tracing = models.FloatField(db_column='H3_Contact tracing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    h6_facial_coverings = models.FloatField(db_column='H6_Facial Coverings', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    h7_vaccination_policy = models.FloatField(db_column='H7_Vaccination policy', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    h8_protection_of_elderly_people = models.FloatField(db_column='H8_Protection of elderly people', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    containmenthealthindex = models.FloatField(db_column='ContainmentHealthIndex', blank=True, null=True)  # Field name made lowercase.
    mobility_recreation = models.FloatField(blank=True, null=True)
    mobility_grocery = models.FloatField(blank=True, null=True)
    mobility_parks = models.FloatField(blank=True, null=True)
    mobility_transit = models.FloatField(blank=True, null=True)
    mobility_work = models.FloatField(blank=True, null=True)
    mobility_residential = models.FloatField(blank=True, null=True)
    british_strain = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modelling_data'


class Scenario1(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    new_cases = models.FloatField(blank=True, null=True)
    hospitalizations = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario 1'


class Scenario10(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    new_cases = models.FloatField(blank=True, null=True)
    hospitalizations = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario 10'


class Scenario11(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    new_cases = models.FloatField(blank=True, null=True)
    hospitalizations = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario 11'


class Scenario12(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    new_cases = models.FloatField(blank=True, null=True)
    hospitalizations = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario 12'


class Scenario2(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    new_cases = models.FloatField(blank=True, null=True)
    hospitalizations = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario 2'


class Scenario3(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    new_cases = models.FloatField(blank=True, null=True)
    hospitalizations = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario 3'


class Scenario4(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    new_cases = models.FloatField(blank=True, null=True)
    hospitalizations = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario 4'


class Scenario5(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    new_cases = models.FloatField(blank=True, null=True)
    hospitalizations = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario 5'


class Scenario6(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    new_cases = models.FloatField(blank=True, null=True)
    hospitalizations = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario 6'


class Scenario7(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    new_cases = models.FloatField(blank=True, null=True)
    hospitalizations = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario 7'


class Scenario8(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    new_cases = models.FloatField(blank=True, null=True)
    hospitalizations = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario 8'


class Scenario9(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    new_cases = models.FloatField(blank=True, null=True)
    hospitalizations = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)