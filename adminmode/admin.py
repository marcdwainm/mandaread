from django.contrib import admin
from .models import UserLog, AchievementLog

admin.site.register(UserLog)
admin.site.register(AchievementLog)
