from django.db import models
from django.contrib.auth.models import User


class Routine(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    today_date = models.DateField(max_length=20)
    check_in_time = models.TimeField(max_length=20)
    check_out_time = models.TimeField(max_length=20)
    current_project = models.CharField(max_length=30)
    billable_task = models.TextField()
    lunch_break = models.TimeField(max_length=20)
    tea_break = models.TimeField(max_length=20)
    meeting = models.TimeField(max_length=20)
    other_break = models.TimeField(max_length=20)
    task_owner = models.CharField(max_length=30)
