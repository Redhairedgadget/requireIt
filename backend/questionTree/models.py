from django.db import models

class Requirement(models.Model):
    requirement = models.CharField(max_length=255, unique=True)
    obligatory = models.BooleanField(default=True)
    answer = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.requirement

class Industry(models.Model):
    industry = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.industry

class WebApp(models.Model):
    title = models.CharField(max_length=255, unique=True)
    requirements = models.ManyToManyField(Requirement)
    industries = models.ManyToManyField(Industry)

    def __str__(self):
        return self.title

