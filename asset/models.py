from django.db import models

# Create your models here.
from member.models import Member


class SystemUser(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    remark = models.CharField(max_length=100)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_user'


class Asset(models.Model):
    hostname = models.CharField(max_length=30)
    network_ip = models.CharField(max_length=30)
    inner_ip = models.CharField(max_length=30)
    remark = models.CharField(max_length=100)
    port = models.IntegerField(blank=True, null=True)
    member = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)
    system_user = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset'
