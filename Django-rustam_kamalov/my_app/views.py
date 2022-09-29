from django.shortcuts import render
from .models import *
from cms.models import *
from price.models import PriceTable, PriceCard
from .forms import OrderForm
from telebot.send_message import sendTelegram

def indexView(request):
    slider = Cms_app.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    pc_table = PriceTable.objects.all()
    form = OrderForm
    ctx = {
        'slider':slider,
        'pc_1':pc_1,
        'pc_2':pc_2,
        'pc_3':pc_3,
        'pc_table':pc_table,
        'form':form
    }
    return render(request, 'index.html', ctx)

def thanks_view(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name = name, order_phone = phone)
        element.save()
        sendTelegram(tele_name = name, tele_number = phone)
        ctx = {
            'name':name,
            'phone':phone,
        }
        return render(request, 'thanks.html', ctx)
    else:
        return render(request, 'thanks.html')
        


