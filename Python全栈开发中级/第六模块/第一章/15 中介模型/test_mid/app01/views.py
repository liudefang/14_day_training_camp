from datetime import date

from django.shortcuts import render

# Create your views here.
from app01.models import Membership


def index(request):
    m1 = Membership(person=ringo, group=beatles, date_joined=date(1962, 8, 16), invite_reason="Needed a new drummer.")