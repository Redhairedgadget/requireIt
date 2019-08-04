from rest_framework import viewsets
from rest_framework.response import Response

from .models import WebApp, Requirement, Industry
from .serializers import WebAppSerializer, RequirementSerializer, IndustrySerializer
import ast

class WebAppViewSet(viewsets.ModelViewSet):


    # def list(self, request):
    #     if request.method == 'GET':
    #         received = ast.literal_eval(request.GET['data'])['data']
    #         queryset = WebApp.objects.all()
    #         serializer = WebAppSerializer(queryset, many=True)
    #         print(type(received), received)
    #         print('lalalalalalalalalalalal')
    #         print(queryset, type(queryset))
    #         return Response(serializer.data)
    def list(self, request):
        queryset = WebApp.objects.all()
        data = ast.literal_eval(request.query_params.get('data', None))['data']
        industry = data[0]
        if data[3] == 'Children, teenagers' or data[3] == 'Families':
            webapps = queryset.filter(industries__industry=industry).exclude(title='Gambling website')
        else:
            webapps = queryset.filter(industries__industry=industry)

        reqs=Requirement.objects.none()

        for answer in data[1:]:
            reqs |= Requirement.objects.all().filter(answer=answer)

        general_reqs = Requirement.objects.none()
        general_reqs |= Requirement.objects.all().filter(answer='general')

        return Response({'webapps': WebAppSerializer(webapps, many=True).data, 'reqs': RequirementSerializer(reqs, many=True).data,
                         'general': RequirementSerializer(general_reqs, many=True).data})

class RequirementViewSet(viewsets.ModelViewSet):

    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer

class IndustryViewSet(viewsets.ModelViewSet):

    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

