from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.

class ListPost(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    
class DetailPost(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    
    
    
def main(request):
    message = request.GET.get('title')
    return HttpResponse("안녕?")

def PostWrite(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    post = Test(title=title, content=content)
    post.save()
    
    return HttpResponse("PostWrite")

def test(request, pk):
    post = Test.objects.get(pk=pk)
    post.views = post.views + 0.5
    post.save()
    serializer_class = TestSerializer(post)
    return JsonResponse(serializer_class.data, safe=False)