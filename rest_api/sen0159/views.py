from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

import logging
from django.utils import timezone
logger = logging.getLogger(__name__)

from .models import SEN0159
from .serializers import SEN0159Serializer


@csrf_exempt
@api_view(['GET', 'POST'])
def real_time(request):
    #log timestamp: got method from who to url
    logger.info(f'GOT {request.method} TO {request.path} FROM {request.META["REMOTE_ADDR"]}')
    if request.method == 'GET':
        #return last record from database
        ser = SEN0159Serializer(SEN0159.objects.last())
        return JsonResponse(ser.data, safe=False)
    
    elif request.method == 'POST':
        #create new record
        #log timestamp: got data 
        logger.info(f'GOT DATA {request.data}')
        ser = SEN0159Serializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)
    
    return JsonResponse({'message': 'Bad request'}, status=400)

@csrf_exempt
@api_view(['GET'])
def history(request, last_of=0):
    #log timestamp: got method from who to url
    logger.info(f'GOT {request.method} TO {request.path} FROM {request.META["REMOTE_ADDR"]}')
    if request.method == 'GET':
        #if last_of is not specified, return all records
        if last_of == 0:
            sen0159 = SEN0159.objects.all()
        else:
            sen0159 = SEN0159.objects.all()[:last_of]

        ser = SEN0159Serializer(sen0159, many=True)
        return JsonResponse(ser.data, safe=False)
    
    return JsonResponse({'message': 'Bad request'}, status=400)
