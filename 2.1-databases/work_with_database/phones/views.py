from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort', '')
    all_phones = Phone.objects.all()

    if sort_pages == 'max_price':
        phones = all_phones.order_by('-price')
        context = {'phones': phones}
        return render(request, template, context)

    elif sort_pages == 'min_price':
        phones = all_phones.order_by('price')
        context = {'phones': phones}
        return render(request, template, context)

    elif sort_pages == 'name':
        phones = all_phones.order_by('name')
        context = {'phones': phones}
        return render(request, template, context)

    context = {'phones': all_phones}
    return render(request, template, context)


def show_product(request, slug):

    template = 'product.html'
    phones = Phone.objects.get(slug=slug)
    context = {'phones': phones}
    return render(request, template, context)


def show_phone(request):
    phones = Phone.objects.all()
    for phone in phones:
        phone_list = [f'{p.id} - {p.name}, {p.image}' for p in Phone]
        return HttpResponse('<br>'.join(phone_list))
