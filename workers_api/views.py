from rest_framework.response import Response
from rest_framework import status, generics

from workers_api.models import Team, Developer
from workers_api.serializers import TeamSerializer, DeveloperSerializer


class Developers(generics.GenericAPIView):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()

    def get(self, request):
        developers = Developer.objects.all()
        serializer = self.serializer_class(developers, many=True)
        return Response({
            "status": "success",
            "developers": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success",
                             "data": {"developer": serializer.data}},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DeveloperDetail(generics.GenericAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

    def get_developer(self, pk):
        try:
            return Developer.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        developer = self.get_developer(pk=pk)
        if developer is None:
            return Response({"status": "fail", "message": f"Developer with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(developer)
        return Response({"status": "success", "data": {"note": serializer.data}})

    def patch(self, request, pk):
        developer = self.get_developer(pk)
        if developer is None:
            return Response({"status": "fail", "message": f"Developer with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            developer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        developer = self.get_developer(pk)
        if developer is None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        developer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Teams(generics.GenericAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get(self, request):
        teams = Team.objects.all()
        serializer = self.serializer_class(teams, many=True)
        return Response({
            "status": "success",
            "teams": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success",
                             "data": {"team": serializer.data}},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TeamDetail(generics.GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_team(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        team = self.get_team(pk=pk)
        if team is None:
            return Response({"status": "fail", "message": f"Team with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(team)
        return Response({"status": "success", "data": {"team": serializer.data}})

    def patch(self, request, pk):
        team = self.get_team(pk)
        if team is None:
            return Response({"status": "fail", "message": f"Team with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            team, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"team": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        team = self.get_team(pk)
        if team is None:
            return Response({"status": "fail", "message": f"Team with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




