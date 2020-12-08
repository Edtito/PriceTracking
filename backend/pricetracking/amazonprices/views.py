from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from amazonprices.models import Items
from amazonprices.serializers import UserSerializer, ItemsSerializer
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hell0oofddsfj asdofadsf adsf asdf</h1>")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serialize_class = UserSerializer

#API
# /items/

@csrf_exempt
def items_list(request):
    #List all
    if request.method == 'GET':
        items = Items.objects.all()
        items_serializer = ItemsSerializer(items,many=True)
        return JsonResponse(items_serializer.data, safe=False)
    #Add one   
    if request.method == 'POST':
        item_data = JSONParser().parser(request)
        item_serializer = ItemsSerializer(data=item_data)
        if item_serializer.is_valid():
           item_serializer.save()
           return JsonResponse(item_data.data, status=status.HTTP_201_created)
        return JsonResponse(item_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #Delete all
    if request.method == 'DELETE':
        Items.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def item_detail(request,pk):
    try:
        item = Items.objects.get(pk=pk)
    except Items.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    #Retrieve one
    if request.method == 'GET':
        item_serializer = ItemsSerializer(item)
        return JsonResponse(item_serializer.data)
    
    #Update one
    if request.method == 'PUT':
        item_data = JSONParser().parser(request)
        item_serializer = ItemsSerializer(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse(item_serializer.data)
        return JsonResponse(item_serializer.errors,status=HTTP_404_BAD_REQUEST)

    #Delete one 
    if request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=HTTP_204_NO_CONTENT)