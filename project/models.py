from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    def __str__(self):
        return f' {self.project_name} '


class Stage(models.Model):
    stage_name = models.CharField(max_length=255)
    stage_details = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.stage_name} {self.stage_details} '
