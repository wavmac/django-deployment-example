from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'text': 'Hello World',
        'number': 100    
    }
    return render(request,'basic_app/index.html',context)

def other(request):
    context = {}
    return render(request, 'basic_app/other.html', context)

def relative(request):
    context = {}
    return render(request,'basic_app/relative_templates.html',context)
