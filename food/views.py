from django.shortcuts import render,redirect
from .models import *
from random import *
import datetime
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect

def index(request):
    settings = Setting.objects.latest('id')
    menus = Menu.objects.all()
    products = Product.objects.all()
    sale = Discount.objects.all()
    recall = Coment.objects.all()
    qury_object = request.GET.get('key')
    comments = Coment.objects.all()
    if request.method == 'POST':
        if 'comment' in request.POST:
            text = request.POST.get('message')
            Coment.objects.create(message=text)
            return redirect('index')
    if qury_object:
        products = Product.objects.filter(Q(name__icontains = qury_object))
    if len(menus)>0:
    
        sliders = Product.objects.filter(menuObject=choice(menus)).order_by('?')
    else:
        sliders=[]

    context = {
        'settings': settings,
        'menus': menus,
        'products': products,
        'sales': sale,
        'sliders': sliders,
        'comments' : comments,
        'recalls': recall,
        'numbers': range(1,len(sliders)),
    }
    return render(request, 'index.html', context)

def about(request):
    settings = Setting.objects.latest('id')
    aboutfoot = Recipe.objects.all()
    context = {
        'about':aboutfoot,
        'settings': settings,
    }
    return render(request,'about.html',context)


def menu(request):
    rows = Menu.objects.all()
    settings = Setting.objects.latest('id')
    products = Product.objects.all()
    context = {
        'menus': rows,
        'products': products,
        'settings': settings,

    }
    return render(request, 'menu.html',context)


def book(request):
    settings = Setting.objects.latest('id')
    stol =  Stol.objects.all()
    
    context = {
        'settings': settings,
        'rows': stol,
    }
    return render(request, 'book.html',context)





def food_order(request,id):
    ip = getIp(request)
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    try:
        currentChek = Cheks.objects.get(humanIp=ip, date__range=(today_min, today_max), isPay=False)
    except:
        currentChek = Cheks.objects.create(humanIp=ip)
        currentChek.save()
    settings = Setting.objects.latest('id')
    product = Product.objects.get(id=id)
    menus = Menu.objects.all()
    sliders = Product.objects.filter(menuObject=choice(menus)).order_by('?')
    try:
        pass
        # products = CheksDetail.objects.filter(productObject=product, cheksObject=currentChek).first()
        # products.productCount = products.productCount + 0.5
        # products.totalSum += product.prise
        # products.save()
    except Exception as e:
        print(e)
        products = CheksDetail.objects.create(productObject=product, cheksObject=currentChek, totalSum=product.prise, productCount=1.0)
        products.save()
    productList = CheksDetail.objects.filter(cheksObject=currentChek) 
    context = {
        'settings' : settings,
        'product' : productList,
        'numbers': range(1,len(sliders)),
    }
    return render(request,'major.html',context)

def getIp(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def search(request):
    setting = Setting.objects.latest('id')
    # products = Product.objects.all()
    qury_object = request.GET.get('key')
    if qury_object:
        products = Product.objects.filter(Q(name__icontains = qury_object))
        print(products)
        context = {
            'setting' : setting,
            'products' : products,
        }
        return render(request,"search.html", context)    
    context={
        'setting':setting
    }
    return render(request,"search.html", context)

def cardpay(request):
    return render(request,'cardpay.html')
@csrf_protect
def bron(request):
    if request.method == "POST":
        name = request.POST.get('name')
        nomer = request.POST.get('nomer')
        count = request.POST.get('count')
        stol = request.POST.get('stol')
        date = request.POST.get('date')
        newRow = Bron.objects.create(name = name, phone = nomer, haumany = count, dait = date, stolObject_id=stol)
        newRow.save()
    return index(request)