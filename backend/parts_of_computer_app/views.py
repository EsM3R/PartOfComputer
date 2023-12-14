from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category , Product , MotherboardFeature ,ComputerCaseFeature ,GraphicsCardFeature ,ProcessorFeature ,CaseFanFeature ,KeyboardFeature ,MonitorFeature , MouseFeature ,RamFeature ,CoolerFeature
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer , ProductSerializer , KeyboardFeatureSerializer, CoolerFeatureSerializer , RamFeatureSerializer , MonitorFeatureSerializer ,MotherBoardFeatureSerializer , CaseFanFeatureSerializer , MouseFeatureSerializer , ComputerCaseFeatureSerializer , GraphicsCardFeatureSerializer ,ProcessorFeatureSerializer
# Create your views here.

@api_view(['GET'])
def category(request):
    if request.method == 'GET':
        data = Category.objects.all()
        serializer = CategorySerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def product(request):
    if request.method == "GET":
        data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return  Response(serializer.data)


@api_view(["GET"])
def product_details(request , id):
    if request.method == "GET":
        data = Product.objects.filter(id = id )
        serializer = ProductSerializer(data, many=True)
        return  Response(serializer.data)



@api_view(["GET"])
def category_details(request, id):
    if request.method == "GET":
        data = Product.objects.filter(category = id)
        serializer = ProductSerializer(data, many=True)
        return  Response(serializer.data)



@api_view(["GET"])
def motherboard(request , product):
    if request.method == 'GET':
        data = MotherboardFeature.objects.filter(product = product)
        serializer = MotherBoardFeatureSerializer(data, many=True)
        return  Response(serializer.data)
    
    
@api_view(["GET"])
def computer_case(request ,product):
    if request.method == 'GET':
        data = ComputerCaseFeature.objects.filter(product = product)
        serializer = GraphicsCardFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def  graphics_card(request,product):
    if request.method == 'GET':
        data = GraphicsCardFeature.objects.filter(product = product)
        serializer = ComputerCaseFeatureSerializer(data, many=True)
        return  Response(serializer.data)
@api_view(["GET"])  
def  processor(request,product):
    if request.method == 'GET':
        data = ProcessorFeature.objects.filter(product = product)
        serializer = ProcessorFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def case_fan(request,product):
    if request.method == 'GET':
        data = CaseFanFeature.objects.filter(product = product)
        serializer = CaseFanFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def keyboard(request,product):
    if request.method == 'GET':
        data = KeyboardFeature.objects.filter(product = product)
        serializer = KeyboardFeatureSerializer(data, many=True)
        return  Response(serializer.data)
@api_view(["GET"])
def monitor(request,product):
    if request.method == 'GET':
        data = MonitorFeature.objects.filter(product = product)
        serializer = MonitorFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def mouse(request,product):
    if request.method == 'GET':
        data = MouseFeature.objects.filter(product = product)
        serializer = MouseFeatureSerializer(data, many=True)
        return  Response(serializer.data)
@api_view(["GET"])
def ram(request,product):
    if request.method == 'GET':
        data = RamFeature.objects.filter(product = product)
        serializer = RamFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def cooler(request,product):
    if request.method == 'GET':
        data = CoolerFeature.objects.filter(product = product)
        serializer = CoolerFeatureSerializer(data, many=True)
        return  Response(serializer.data)
