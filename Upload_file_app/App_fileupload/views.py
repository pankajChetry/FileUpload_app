from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import FileSerializer
from .models import file

# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    queryset = file.objects.all()
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        uploadedfile = request.data['uploadedfile']
        title = request.data['title']
        try:
            file.objects.create(title=title, uploadedfile=uploadedfile)
            return HttpResponse({'message:File uploaded'}, status=200)
        except Exception as e:
            return HttpResponse({'status': 500, 'error': str(e)}, status=500)


