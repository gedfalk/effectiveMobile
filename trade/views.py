from django.shortcuts import render

def trade(request):
    context = {}
    return render(request, 'trade/trade.html', context)
