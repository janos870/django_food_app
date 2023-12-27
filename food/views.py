from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

########  class views  ##########

class IndexClassView(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "item_list"


class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item_form.html'
    success_url = reverse_lazy('food:index')
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        print(f"Current user: {self.request.user}")
        return super().form_valid(form)


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'food/item_form.html'
    success_url = reverse_lazy('food:index')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'food/item_delete.html'
    success_url = reverse_lazy('food:index')
    



########  function view   #########

def index(request):
    item_list = Item.objects.all()
    context = {
        "item_list": item_list,
    }
    return render( request, "food/index.html", context)
    

def item(request):
    return HttpResponse('Items')

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        "item": item,
    }
    return render(request, 'food/detail.html', context)
    

def create_item(requvest):
    form = ItemForm(requvest.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(requvest, 'food/item_form.html', {'form':form})


def update_item(requvest, id):
    item = Item.objects.get(id=id)
    form = ItemForm(requvest.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(requvest, 'food/item_form.html', {'form':form, 'item':item})


def delete_item(requvest, id):
    item = Item.objects.get(id=id)
    if requvest.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(requvest, 'food/item_delete.html', {'item':item})