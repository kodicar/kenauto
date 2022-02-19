from django.shortcuts import render
from django.http import HttpResponse

from cars.models import Cars
from dealers.models import Dealers
from cars.choices import makes_choices, price_choices, counties

def index(request):
    listings = Cars.objects.order_by('date_added').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'county_choices': counties,
        'makes_choices': makes_choices,
        'price_choices': price_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    dealers = Dealers.objects.order_by('-deal_date')

    # Get MVP
    mvp_dealers = Dealers.objects.all().filter(is_mvp=True)

    context = {
        'dealers': dealers,
        'mvp_dealers': mvp_dealers
    }

    return render(request, 'pages/about.html', context)