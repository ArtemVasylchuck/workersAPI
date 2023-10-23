from django.urls import path
from workers_api.views import Developers, DeveloperDetail, Teams, TeamDetail

urlpatterns = [
    path('developers/', Developers.as_view()),
    path('developers/<str:pk>', DeveloperDetail.as_view()),

    path('teams/', Teams.as_view()),
    path('teams/<str:pk>', TeamDetail.as_view()),
]
