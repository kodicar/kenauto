from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from cars.models import Cars
from dealers.models import Dealer

def index(request):
    listings = Cars.objects.order_by('date_added').filter(is_published=True)[:3]
    context = {
        'listings': listings,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    dealers = Dealer.objects.order_by('-hire_date')

    # Get MVP
    mvp_dealers = Dealer.objects.all().filter(is_mvp=True)

    context = {
        'dealers': dealers,
        'mvp_dealers': mvp_dealers
    }

    return render(request, 'pages/about.html', context)