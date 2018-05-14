import os
import sys

from django.shortcuts import render

# Create your views here.

from my_proj import settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

sys.path.append(BASE_DIR)

def sayhi():
    print('hello world!')

print(settings.DATABASES)
