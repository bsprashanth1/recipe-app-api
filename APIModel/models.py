# from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class UIModel(models.Model):
    request_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    inputText = models.TextField(max_length=2000, blank=True, default='')
    inputType = models.CharField(max_length=10, blank=True,default="text")# or file
    keywords = models.TextField(max_length=200, blank=True)
    totalScenarios = models.IntegerField(blank=True, default=0)
    # testCases = ArrayField(models.CharField(max_length=200, blank=True))

    class Meta:
        ordering = ('request_id',)

    def __str__(self):
        return self.title


# class AIModel(models.Model):
#     # response_id = models.IntegerField(primary_key=True)
#     uiModel = models.ForeignKey(UIModel, models.CASCADE,null=True, blank=True)
#     # Add more fields based on the API response from the AI models
#     keywords = models.CharField(max_length=200, blank=False)
#     # testCases = ArrayField(models.CharField(max_length=200, blank=True))

