from django.contrib import admin

# Register your models here.
from members.models import Profile

admin.site.register(Profile)