from pathlib import Path

from django.apps import AppConfig
from django.conf import settings
import joblib
import numpy as np


class DiabetAppConfig(AppConfig):
    name = 'DjangoAPI'
    diabet_model_path = settings.MODELS / "model.joblib"
    model = joblib.load(diabet_model_path)
