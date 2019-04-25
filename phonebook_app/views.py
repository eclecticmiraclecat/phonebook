from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

def home(request):
    names = Contact.objects.order_by('name')
    context = { 'names': names }
    return render(request, 'phonebook_app/home.html', context)

def delete(request, name_id):
    name = Contact.objects.get(pk=name_id)
    name.delete()
    return redirect('home')

def create(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = { 'form': form }
    return render(request, "phonebook_app/create.html", context)

def update(request, name_id):
    name = get_object_or_404(Contact, pk=name_id)
    form = ContactForm(request.POST or None, instance=name)
    if form.is_valid():
        form.save()
        return redirect('read', name_id)
    context = { 'form': form }
    return render(request, "phonebook_app/create.html", context)

def read(request, name_id):
    name = get_object_or_404(Contact, pk=name_id)
    context = { "name": name }
    return render(request, "phonebook_app/detail.html", context)
