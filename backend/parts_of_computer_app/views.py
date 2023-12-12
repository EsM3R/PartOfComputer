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
def motherboard(request):
    if request.method == 'GET':
        data = MotherboardFeature.objects.all()
        serializer = MotherBoardFeatureSerializer(data, many=True)
        return  Response(serializer.data)
    
    
@api_view(["GET"])
def computer_case(request):
    if request.method == 'GET':
        data = ComputerCaseFeature.objects.all()
        serializer = GraphicsCardFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def  graphics_card(request):
    if request.method == 'GET':
        data = GraphicsCardFeature.objects.all()
        serializer = ComputerCaseFeatureSerializer(data, many=True)
        return  Response(serializer.data)
@api_view(["GET"])  
def  processor(request):
    if request.method == 'GET':
        data = ProcessorFeature.objects.all()
        serializer = ProcessorFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def case_fan(request):
    if request.method == 'GET':
        data = CaseFanFeature.objects.all()
        serializer = CaseFanFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def keyboard(request):
    if request.method == 'GET':
        data = KeyboardFeature.objects.all()
        serializer = KeyboardFeatureSerializer(data, many=True)
        return  Response(serializer.data)
@api_view(["GET"])
def monitor(request):
    if request.method == 'GET':
        data = MonitorFeature.objects.all()
        serializer = MonitorFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def mouse(request):
    if request.method == 'GET':
        data = MouseFeature.objects.all()
        serializer = MouseFeatureSerializer(data, many=True)
        return  Response(serializer.data)
@api_view(["GET"])
def ram(request):
    if request.method == 'GET':
        data = RamFeature.objects.all()
        serializer = RamFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def cooler(request):
    if request.method == 'GET':
        data = CoolerFeature.objects.all()
        serializer = CoolerFeatureSerializer(data, many=True)
        return  Response(serializer.data)
