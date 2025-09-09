from django.db import models
from .validators import validate_cv_file, cv_upload_path

# Create your models here.


class Candidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    skills = models.JSONField(default=list)
    cv_url = models.FileField(upload_to=cv_upload_path, validators=[validate_cv_file])

    class Meta:
        ordering = ["name"]
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"

    def __str__(self):
        return f"{self.name} ({self.email})"
