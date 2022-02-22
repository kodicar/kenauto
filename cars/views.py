from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . models import Cars
from .choices import counties, price_choices, makes_choices

# Create your views here.
def index(request):
  listings = Cars.objects.order_by('-date_added').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'cars/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Cars, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'cars/listing.html', context)

def search(request):
  queryset_list = Cars.objects.order_by('-date_added')

  # Keywords
  # if 'keywords' in request.GET:
  #   keywords = request.GET['keywords']
  #   if keywords:
  #     queryset_list = queryset_list.filter(description__icontains=keywords)

  # County
  if 'county' in request.GET:
    county = request.GET['county']
    if county:
      queryset_list = queryset_list.filter(county__iexact=county)

  # Town
  if 'town' in request.GET:
    town = request.GET['town']
    if town:
      queryset_list = queryset_list.filter(town__iexact=town)

  # Makes
  if 'make' in request.GET:
    make = request.GET['make']
    if make:
      queryset_list = queryset_list.filter(make__lte=make)

  if 'model' in request.GET:
    model = request.GET['model']
    if model:
      queryset_list = queryset_list.filter(model__lte=model)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'county_choices': counties,
    'makes_choices': makes_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'cars/search.html', context)

