from django.shortcuts import render, redirect
from .models import Library
from .forms import LibraryForm

def Libarary_list(request):
    library=Library.objects.all()
    form=LibraryForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'library_list.html',
                  {'library':library,'form':form})   
