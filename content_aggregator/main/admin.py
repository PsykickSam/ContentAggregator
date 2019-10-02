from django.contrib import admin
from .models import Website
from .models import Link

admin.site.register(Link)
admin.site.register(Website)

# Register your models here.
