from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime
from datetime import datetime
def index(request):
        context = {
            "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        }
        if 'total_gold' not in request.session:
            request.session['total_gold'] = 0
            request.session['temp_gold'] = 0
            request.session['building'] = 'nowhere'
            request.session['made'] = 'made'
            request.session['message'] = []
        return render(request, 'index.html', context)


def process_gold_farm(request):
        context = {
            "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        }
        request.session['temp_gold'] =random.randint(10, 20)
        request.session['total_gold'] +=request.session['temp_gold']
        request.session['building'] = 'the farm'
        request.session['made'] = 'made'
        request.session['message'].append(f" You {request.session['made']} {request.session['temp_gold']} gold at {request.session['building']} ")
        return redirect('/')

def process_gold_cave(request):
        request.session['temp_gold'] =random.randint(5, 10)
        request.session['total_gold'] +=request.session['temp_gold']
        request.session['building'] = 'the cave'
        request.session['made'] = 'made'
        request.session['message'].append(f" You {request.session['made']} {request.session['temp_gold']} gold at {request.session['building']} ")
        return redirect('/')

def process_gold_house(request):
        request.session['temp_gold'] =random.randint(2, 5)
        request.session['total_gold'] +=request.session['temp_gold']
        request.session['building'] = 'the house'
        request.session['made'] = 'made'
        request.session['message'].append(f" You {request.session['made']} {request.session['temp_gold']} gold at {request.session['building']} ")
        return redirect('/')

def process_gold_casino(request):
        request.session['temp_gold'] =random.randint(-50, 50)
        request.session['total_gold'] +=request.session['temp_gold']
        request.session['building'] = 'casino'
        request.session['made'] = 'made'
        if request.session['temp_gold'] < 0:
            request.session['made']= 'lost'
            request.session['temp_gold'] = request.session['temp_gold'] * -1
        request.session['message'].append(f" You {request.session['made']} {request.session['temp_gold']} gold at {request.session['building']} ")
        return redirect('/')

def reset(request):
        request.session.flush()
        return redirect ('/')


