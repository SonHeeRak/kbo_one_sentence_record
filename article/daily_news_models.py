# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BaseTemplate(models.Model):
    index = models.IntegerField(primary_key=True)
    group = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    rank = models.IntegerField()
    use = models.CharField(max_length=50, blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    eval = models.CharField(max_length=50, blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)
    template_tab = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'daily_news'
        managed = False
        db_table = 'base_template'


class CommonDynamicVariable(models.Model):
    index = models.IntegerField(primary_key=True)
    group = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    rank = models.IntegerField()
    use = models.CharField(max_length=50, blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    eval = models.CharField(max_length=50, blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'daily_news'
        managed = False
        db_table = 'common_dynamic_variable'


class HitterRecordSentence(models.Model):
    index = models.IntegerField(primary_key=True)
    group = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    rank = models.IntegerField()
    use = models.CharField(max_length=50, blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    eval = models.CharField(max_length=50, blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'daily_news'
        managed = False
        db_table = 'hitter_record_sentence'


class MethodInfo(models.Model):
    index = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    kor = models.CharField(max_length=50, blank=True, null=True)
    method = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'daily_news'
        managed = False
        db_table = 'method_info'


class PitcherRecordSentence(models.Model):
    index = models.IntegerField(primary_key=True)
    group = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    rank = models.IntegerField()
    use = models.CharField(max_length=50, blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    eval = models.CharField(max_length=50, blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'daily_news'
        managed = False
        db_table = 'pitcher_record_sentence'


class PitcherSeasonRecordSentence(models.Model):
    index = models.IntegerField(primary_key=True)
    group = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    rank = models.IntegerField()
    use = models.CharField(max_length=50, blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    eval = models.CharField(max_length=50, blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'daily_news'
        managed = False
        db_table = 'pitcher_season_record_sentence'


class HitterSeasonRecordSentence(models.Model):
    index = models.IntegerField(primary_key=True)
    group = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    rank = models.IntegerField()
    use = models.CharField(max_length=50, blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    eval = models.CharField(max_length=50, blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'daily_news'
        managed = False
        db_table = 'hitter_season_record_sentence'


class TeamRecordSentence(models.Model):
    index = models.IntegerField(primary_key=True)
    group = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    rank = models.IntegerField()
    use = models.CharField(max_length=50, blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    eval = models.CharField(max_length=50, blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'daily_news'
        managed = False
        db_table = 'team_record_sentence'
