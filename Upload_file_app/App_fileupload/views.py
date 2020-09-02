from django.shortcuts import render
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
        file.objects.create(title=title, uploadedfile=uploadedfile)
        return HttpResponse({'message:File uploaded'}, status=200)

