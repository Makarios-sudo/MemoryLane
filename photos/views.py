import profile
from unicodedata import category, name
from django import forms
from django.shortcuts import redirect, render
from .models import Category, Memory
from .forms import CategoryForm, MemoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    return render(request, "index.html")


#View all memories
@login_required(login_url='index')
def memoryGallery(request):
  
    category = request.GET.get('searchCategory')
    if category == None:
        memories = Memory.objects.filter(category__user__id__contains =request.user.profile.id) 
    else:
        memories = Memory.objects.filter(category__name__contains =category,  )
    
    categories = Category.objects.filter(user__id = request.user.profile.id)


    context = {"categories":categories, "memories":memories}
    return render(request, 'photos/memoryGallery.html', context)



#view individual memory
@login_required(login_url='index')
def viewMemory(request, pk):
    memory = Memory.objects.get(id=pk)

    context = {"memory": memory}
    return render(request, 'photos/viewMemory.html', context)


#add a category
@login_required(login_url='index')
def addCategory(request):

    page = 'Category'
    form = CategoryForm()
    
    if request.method == 'POST':
        form = form = CategoryForm(request.POST)
        if form.is_valid():
            categoryform =form.save(commit=False)
            categoryform.user = request.user.profile
            categoryform.save()
            messages.success(request, "Your Category was Successfully Added")
            return redirect('memoryGallery')

    context = {"form": form, "page":page}
    return render(request, 'photos/addMemory_Category.html', context)

#add a new memory
@login_required(login_url='index')
def addMemory(request, pk):
    category = Category.objects.get(id=pk)

    form = MemoryForm()
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.category =category
            memory.save()
            messages.success(request, "Your Memory was Successfully Added")
            return redirect('memoryGallery')

    context = {"form": form}
    return render(request, 'photos/addMemory_Category.html', context)


#delete Category
@login_required(login_url='index')
def deleteCategory(request, pk):
    page = 'deleteCategory'
    category = Category.objects.get(id=pk)

    if request.method=='POST':
        category.delete()
        messages.success(request, "Your Delete was Successful")
        return redirect('memoryGallery')
   
    context = {"obj":category, 'page': page}
    return render(request, 'photos/Update-Delete.html', context )



@login_required(login_url='index')
def updateMemory(request,pk):
    page ="update"
    memory = Memory.objects.get(id=pk)
    form = MemoryForm(instance=memory)

    if request.method == "POST":
        form = MemoryForm(request.POST, request.FILES, instance=memory,)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Update was Successful")
            return redirect("memoryGallery")
    context = {"form":form, "page":page}
    return render(request, "photos/Update-Delete.html", context)
    


#delete a Memory
@login_required(login_url='index')
def deleteMemory(request, pk):
    page = "delete"
    memory = Memory.objects.get(id=pk)

    if request.method=='POST':
        memory.delete()
        messages.success(request, "Your Delete was Successful")
        return redirect('memoryGallery')
   
    context = {"obj":memory,  "page":page }
    return render(request, 'photos/Update-Delete.html', context )
    
