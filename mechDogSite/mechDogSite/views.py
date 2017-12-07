# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import cookie
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect

def main(request):
    return render(request,"home.html")
