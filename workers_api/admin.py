from django.contrib import admin
from .models import TypeOfTeam, Team, Developer

admin.site.register(Team)
admin.site.register(TypeOfTeam)
admin.site.register(Developer)

