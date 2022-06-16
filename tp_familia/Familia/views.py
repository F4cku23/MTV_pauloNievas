from django.shortcuts import render
from .models import Familiar

# Create your views here.

def home(request):
    familiaList=Familiar.objects.all()
    return render(request, "index.html", {"familiar": familiaList})

