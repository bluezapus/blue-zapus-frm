from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'title': 'BlueZapus',
    }
    return render(request, 'index.html', context)