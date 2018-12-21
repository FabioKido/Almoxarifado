from django.shortcuts import render
from .forms import materialForm

# Create your views here.

def newMateriais(request):
    form = materialForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    return render(request,'materiais.html', {'form': form})
