from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer

class FileView(APIView):
    parser_classes = (MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        fileserializer = FileSerializer(data=request.data)
        if fileserializer.is_valid():
            print("File Uploaded")
            fileserializer.save()
            return Response(fileserializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(fileserializer.errors,status=status.HTTP_400_BAD_REQUEST)



