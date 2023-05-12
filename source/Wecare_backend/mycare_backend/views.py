from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serializer import HeartSerializer, BodyStatusSerializer, TempSerializer
from .controller import get_heart_rate, get_latest_body_info, get_temp_info,get_body_status_info
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi

@swagger_auto_schema(
    method='get',  # HTTP method for which to generate the schema
    responses={
        200: openapi.Response(
            description='OK'
        ),
        404: 'Not Found',
    },
    operation_summary='Heart rate list',
    operation_description='Get the latest 60 heartbeat data',
)
@swagger_auto_schema(
    method='post',  # HTTP method for which to generate the schema
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['heart_rate', 'update_time'],
        properties={
            'heart_rate': openapi.Schema(type=openapi.FORMAT_DECIMAL),
            'update_time': openapi.Schema(type=openapi.FORMAT_DATETIME),
        },
    ),
    responses={
        201: 'Created',
        400: 'Bad Request',
    },
    operation_summary='Upload data',
    operation_description='Store heart rate data to the database.',
)
@api_view(['GET', 'POST'])
def heart_rate(request):
    if request.method == 'GET':
        result = get_heart_rate()
        return JsonResponse(result, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HeartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@swagger_auto_schema(
    method='get',  # HTTP method for which to generate the schema
    responses={
        200: openapi.Response(
            description='OK'
        ),
        404: 'Not Found',
    },
    operation_summary='temperature information list',
    operation_description='Get the latest 60 temperature data',
)
@swagger_auto_schema(
    method='post',  # HTTP method for which to generate the schema
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['temperature', 'update_time'],
        properties={
            'temperature': openapi.Schema(type=openapi.FORMAT_DECIMAL),
            'update_time': openapi.Schema(type=openapi.FORMAT_DATETIME),
        },
    ),
    responses={
        201: 'Created',
        400: 'Bad Request',
    },
    operation_summary='Upload data',
    operation_description='Store sensor data to the database.',
)
@api_view(['GET', 'POST'])
def environment_info(request):
    if request.method == 'GET':
        result = get_temp_info()
        return JsonResponse(result, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TempSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@swagger_auto_schema(
    method='get',  # HTTP method for which to generate the schema
    responses={
        200: openapi.Response(
            description='OK'
        ),
        404: 'Not Found',
    },
    operation_summary='latest body status',
)
@swagger_auto_schema(
    method='post',  # HTTP method for which to generate the schema
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['body_status', 'update_time'],
        properties={
            'body_status': openapi.Schema(type=openapi.TYPE_STRING),
            'update_time': openapi.Schema(type=openapi.FORMAT_DATETIME),
        },
    ),
    responses={
        201: 'Created',
        400: 'Bad Request',
    },
    operation_summary='Upload data',
    operation_description='Store sensor data to the database.',
)
@api_view(['GET', 'POST'])
def latest_body(request):
    if request.method == 'GET':
        result = get_body_status_info()
        return JsonResponse(result, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BodyStatusSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



