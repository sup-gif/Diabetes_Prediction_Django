from django.http import JsonResponse
from .apps import DiabetAppConfig
from rest_framework.views import APIView
from .apps import *
import numpy as np
import pandas as pd

from rest_framework.response import Response


class DjangoAPIView(APIView):
    def post(self, request):
        """Handle HTML POST request"""
        #data = request.data
        glucouse = request.GET.get["Glucose"]
        insulin = request.GET.get["insulin"]
        bmi = request.GET.get["BMI"]
        age = request.GET.get["age"]

        prediction = DiabetAppConfig.model.predict([[glucouse, insulin, bmi , age]]
                                                   )
        response_dict = {"Predicted diabet": prediction}
        print(response_dict)
        return Response(response_dict, status=200)
