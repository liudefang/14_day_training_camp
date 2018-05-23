import os
import sys

from django.shortcuts import render

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

sys.path.append(BASE_DIR)
from my_proj import settings


def sayhi():
    print('hello world!')

print(settings.DATABASES)
