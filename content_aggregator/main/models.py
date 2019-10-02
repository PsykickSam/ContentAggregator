from django.db import models
from django.utils import timezone

# Create your models here
class Website(models.Model):
    id = models.AutoField(primary_key=True)
    web_data_title = models.TextField()
    web_identifier = models.TextField(unique=True, max_length=5)
    created_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.web_data_title + " Identifier: " + self.web_identifier
    
    class Meta:
        db_table = "tb_website"

class Link(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.TextField(unique=True)
    title = models.TextField(default=None)
    web_identifier = models.TextField(max_length=5)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    updated_at = models.DateTimeField(null=True)
    
    class Meta:
        db_table = "tb_link"


