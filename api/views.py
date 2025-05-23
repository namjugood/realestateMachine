from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RealEstateData
import json

# Create your views here.

@csrf_exempt
def real_estate_data(request):
    if request.method == 'GET':
        data = RealEstateData.objects.all()
        return JsonResponse({
            'data': list(data.values())
        })
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_data = RealEstateData.objects.create(**data)
            return JsonResponse({
                'status': 'success',
                'data': {
                    'id': new_data.id,
                    'date': new_data.date,
                    'price': new_data.price,
                    'area': new_data.area,
                    'location': new_data.location,
                    'type': new_data.type
                }
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
