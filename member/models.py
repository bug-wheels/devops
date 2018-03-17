from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=30)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class Member(models.Model):
    name = models.CharField(max_length=30)
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    position = models.ForeignKey('Position', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'


class Position(models.Model):
    name = models.CharField(max_length=30)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position'
