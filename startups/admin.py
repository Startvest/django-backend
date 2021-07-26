from django.contrib import admin
from .models import Startup, JobOpening, StartupGallery

# Register your models here.
admin.site.register(Startup)
admin.site.register(JobOpening)
admin.site.register(StartupGallery)