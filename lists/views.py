from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_safe
from django.shortcuts import get_object_or_404, redirect, render
from .models import List, Item
from django.contrib import messages
from .forms import AddItemForm, AddListForm


@login_required
@require_safe
def shopping_list(request):
    lists = (
        List.objects
        .filter(owner=request.user)
        .order_by("name")
    )
    add_list_form = AddListForm()
    return render(request, "lists/lists_list.html", {
        "lists": lists,
        "add_list_form": add_list_form,
    })

@login_required
@require_safe
def detail_list(request, pk):
    shopping_list = get_object_or_404(List, pk=pk)
    items = Item.objects.filter(shopping_list=shopping_list).order_by("name","-quantity")

    add_form = AddItemForm()
    
    return render(request, "lists/detail_list.html", {
        "list": shopping_list,
        "items": items,
        "add_form": add_form,
    })

@login_required
@require_POST
def delete_list(request, pk):
    shopping_list = get_object_or_404(List,pk=pk)
    shopping_list.delete()
    messages.success(request, "List removed.")
    return redirect("lists:lists_list")

@login_required
@require_POST
def toggle_item(request, pk, item_id):
    item = get_object_or_404(Item, pk=item_id, shopping_list_id=pk)
    item.done = not item.done
    item.save()
    return redirect("lists:detail_list", pk=pk)

@login_required
@require_POST
def delete_item(request, pk, item_id):
    item = get_object_or_404(Item, pk=item_id, shopping_list_id=pk)
    item.delete()
    messages.success(request, "Product removed from list.")
    return redirect("lists:detail_list", pk=pk)

@login_required
@require_POST
def add_item(request, pk):
    shopping_list = get_object_or_404(List, pk=pk)
    form = AddItemForm(request.POST)
    if form.is_valid():
        item = form.save(commit=False)
        item.shopping_list = shopping_list  
        item.save()
        messages.success(request, "Item added.")
        return redirect("lists:detail_list", pk=pk)

    items = Item.objects.filter(shopping_list=shopping_list).order_by("-id")
    return render(request, "lists/detail_list.html", {
        "list": shopping_list,
        "items": items,
        "add_form": form,  
    })

@login_required
@require_POST
def add_list(request):
    form = AddListForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.owner = request.user   
        obj.save()
        messages.success(request, "List created.")
        return redirect("lists:lists_list")

    lists = (
        List.objects
        .filter(owner=request.user)
        .order_by("-created_at")
    )
    return render(request, "lists/lists_list.html", {
        "lists": lists,
        "add_list_form": form,
    })