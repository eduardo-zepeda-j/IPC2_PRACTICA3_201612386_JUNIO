from django.shortcuts import render,redirect
import requests

# Create your views here.
backend = 'http://localhost:5000/texto'

def post(request):
    global backend
    text = request.POST.get('text')
    requests.post(backend,text)
    return redirect('Home')

def put(request):
    global backend
    text = request.POST.get('text')
    requests.put(backend,text)
    return redirect('Home')

def delete(request):
    global backend
    requests.delete(backend)
    return redirect('Home')
    
def home(request):
    global backend
    context = ''
    textReq = request.GET.get('texto',None)
    texto = requests.get(backend,{
            'texto':textReq
        }).text
    context = {'texto':texto}
    
    return render(request,'index.html',context)