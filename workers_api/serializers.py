from rest_framework import serializers
from workers_api.models import Team, Developer


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = "__all__"
