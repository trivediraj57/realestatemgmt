from django.shortcuts import get_object_or_404, render
from .models import Listing
from .choices import *
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing' : listing
    }
    return render(request,'listings/listing.html', context)

def search(request):
    querysearch_list = Listing.objects.order_by('-list_date')

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            querysearch_list = querysearch_list.filter(description__icontains=keywords)

    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            querysearch_list = querysearch_list.filter(city__icontains=city)

    
    #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            querysearch_list = querysearch_list.filter(state__icontains=state)

    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            querysearch_list = querysearch_list.filter(bedrooms__lte=bedrooms)

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            querysearch_list = querysearch_list.filter(price__lte=price)

    context = {
        'price_choices' : price_choices,
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'listings' : querysearch_list,
        'values' : request.GET
    }
    return render(request,'listings/search.html', context)