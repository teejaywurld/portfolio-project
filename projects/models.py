
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.TextField(default="https://thumbs.dreamstime.com/b/project-management-concept-27391266.jpg")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
