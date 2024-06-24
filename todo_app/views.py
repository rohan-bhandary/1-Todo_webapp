from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.

# ============================================================================================================


def index(request):

    item_list = Todo.objects.order_by("-date")

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect (index)
    
    form = TodoForm()

    context = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }

    return render(request, 'index.html', context)


# ============================================================================================================


def remove(request,item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('index')


