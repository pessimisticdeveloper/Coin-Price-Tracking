from django.shortcuts import render
import requests
from .models import Coin
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    api_data = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=try&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=tr').json()

    for item in api_data:
        coin = Coin(
            name=item['name'],
            symbol=item['symbol'],
            image=item['image'],
            current_price=item['current_price'],
            market_cap=item['market_cap'], )
        coin.save()

    # Sayfalama için Paginator kullanımı
    paginator = Paginator(api_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})
