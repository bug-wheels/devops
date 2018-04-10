from django.db import models

# Create your models here.
from member.models import Member


class TaskHistory(models.Model):
    host_name = models.CharField(max_length=100)
    ip = models.CharField(max_length=20)
    shell = models.CharField(max_length=200)
    operation_name = models.CharField(max_length=20)
    operation = models.ForeignKey(Member, models.DO_NOTHING)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'task_history'
