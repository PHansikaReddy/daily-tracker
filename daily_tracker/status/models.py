
from django.db import models

class DailyStatus(models.Model):
    day = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    question_name = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return f"Day {self.day}: {self.question_name}"
