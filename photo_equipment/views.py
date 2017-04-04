from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Instrument, Basket


@login_required(login_url='/login/')
def products_list(request):
    products = Instrument.objects.all().order_by('created_date')
    return render(request, 'products_list.html', {'products': products})


@login_required(login_url='/login/')
def basket(request):
    basket_item = Basket.objects.filter(user=request.user)
    products = basket_item[0].products.all() if basket_item else []
    return render(request, 'basket.html', {'products': products})


@login_required(login_url='/login/')
def product_by_id(request, pk):
    product = get_object_or_404(Instrument, pk=pk)
    try:
        basket_item = Basket.objects.get(user=request.user)
        in_basket = product in basket_item.products.all()
    except Basket.DoesNotExist:
        in_basket = False
    return render(request, 'product.html', {'product': product, 'in_basket': in_basket})


@login_required(login_url='/login/')
def add_product_to_basket(request, pk):
    product = get_object_or_404(Instrument, pk=pk)
    try:
        basket_item = Basket.objects.get(user=request.user)
    except Basket.DoesNotExist:
        basket_item = Basket.objects.create(user=request.user)
    basket_item.products.add(product)
    return HttpResponse(status=200)

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request, 'login_page.html', {'status': 0})
