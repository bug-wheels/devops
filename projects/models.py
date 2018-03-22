from django.db import models

# Create your models here.
from member.models import Member


class Project(models.Model):
    company_id = models.IntegerField()
    name = models.CharField(max_length=30)
    leader = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'
