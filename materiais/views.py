from django.shortcuts import render
from .forms import materialForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def newMateriais(request):
    form = materialForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    return render(request,'materiais.html', {'form': form})
