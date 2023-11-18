from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from .models import MQ9
from .serializers import MQ9Serializer

@csrf_exempt
@api_view(['GET', 'POST'])
def real_time(request):
    if request.method == 'GET':
        #return last record from database
        ser = MQ9Serializer(MQ9.objects.last())
        return JsonResponse(ser.data, safe=False)
    
    elif request.method == 'POST':
        #create new record
        ser = MQ9Serializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)
    
    return JsonResponse({'message': 'Bad request'}, status=400)

@csrf_exempt
@api_view(['GET'])
def history(request, last_of=0):
    if request.method == 'GET':
        #if last_of is not specified, return all records
        if last_of == 0:
            mq9 = MQ9.objects.all()
        else:
            mq9 = MQ9.objects.all()[:last_of]

        ser = MQ9Serializer(mq9, many=True)
        return JsonResponse(ser.data, safe=False)
    
    return JsonResponse({'message': 'Bad request'}, status=400)
