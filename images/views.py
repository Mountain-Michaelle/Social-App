from django.shortcuts import render, redirect
from .forms import ImageCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def image_create(request):
    if request.method == 'POST':
        #send the form
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')
            
            return redirect(new_image.get_absolute_url())
    else:
        #build the form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET) 
        
    context = {'section': 'images', 'form': form}
    return render(request, 'images/image/create.html', context)