# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActiveCasesChange(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'active_cases_change'


class ActiveCasesRegional(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'active_cases_regional'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cases(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
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


class DailyPositive(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'daily_positive'


class DailyPositivePct(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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




class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HospInDolnoslaskie(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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


class HospIndol(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_indol'


class HospInkujPom(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inkuj-pom'


class HospInlubel(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inlubel'


class HospInlubu(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inlubu'


class HospInmaz(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inmaz'


class HospInmp(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inmłp'


class HospInopo(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inopo'


class HospInpdk(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inpdk'


class HospInpod(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inpod'


class HospInpom(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inpom'


class HospInsl(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_insl'


class HospInwM(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inw-m'


class HospInwlkp(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inwlkp'


class HospInzach(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inzach'


class HospIndz(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inłdz'


class HospInw(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'hosp_inśw'


class Hospitalizations(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
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


class Layer(models.Model):
    topology = models.OneToOneField('Topology', models.DO_NOTHING, primary_key=True)
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=-1)
    table_name = models.CharField(max_length=-1)
    feature_column = models.CharField(max_length=-1)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'
        unique_together = (('topology', 'layer_id'), ('schema_name', 'table_name', 'feature_column'),)


class NewCasesRegional(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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


class PctActiveDailyRise(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'pct_active_daily_rise'


class PctDailyRiseRegional(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'pct_daily_rise_regional'


class PlMap(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    geometry = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_map'


class Polska(models.Model):
    gid = models.AutoField(primary_key=True)
    region = models.CharField(max_length=80, blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polska'


class RecoveriesRegional(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'recoveries_regional'


class RegCases(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
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


class RollingMean(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
    date = models.DateTimeField(blank=True, null=True)
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


class RollingMeanRegional(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'rolling_mean_regional'


class SumCasesRegional(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'sum_cases_regional'


class SumDeathsRegional(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'sum_deaths_regional'


class SumRecoveriesRegional(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'sum_recoveries_regional'


class Testing(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
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


class TestsPer100K(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
        db_table = 'tests_per_100k'


class Topology(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topology'


class Vaccinations(models.Model):
    date = models.DateTimeField(blank=True, null=True)
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
