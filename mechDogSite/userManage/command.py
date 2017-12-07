
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import cookie
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django import forms

from models import User

from views import *

def operate(request):
    if(not TokenCheck()):
        return HttpResponseRedirect('/user/')
    sparseOperation(request.POST)
def sparseOperation(POST):
    pass