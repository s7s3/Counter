from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
        print('key exists!')
    else:
        print("key 'key_name' does NOT exist")
        request.session['count'] = 0
    
    return render(request, 'index.html')

def destroy(request):
    del request.session['count']
    return redirect ('/')

def add_2(request):
    request.session['count'] += 1
    return redirect ('/')