from django.contrib import admin
from .models import Userauth
from django.contrib.auth.admin import UserAdmin

admin.site.register(Userauth, UserAdmin)