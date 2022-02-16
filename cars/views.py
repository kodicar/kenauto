from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . models import Cars
from .choices import counties, price_choices

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