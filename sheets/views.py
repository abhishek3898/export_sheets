from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

import pandas as pd
from .models import *
# from django .import settings
# from sheets.serializers import OrderSerializer
# from rest_framework.authentication.models import Token



# Create your views here.

def Exportsheets(request):
    return render(request,'index.html')

class ExportImportCsv(APIView):
    def get(self,request):
        orders = Orders.objects.all()
        print(orders)
