from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Customerdetails

def customer_list_view(request):

    username_query = request.GET.get('username', '')
    mobile_number_query = request.GET.get('mobile_number', '')
    place_query = request.GET.get('place', '')


    sort_by = request.GET.get('sort', 'username')


    customers = Customerdetails.objects.all()

    if username_query:
        customers = customers.filter(username__icontains=username_query)
    if mobile_number_query:
        customers = customers.filter(mobile_number__icontains=mobile_number_query)
    if place_query:
        customers = customers.filter(place__icontains=place_query)


    usernames = Customerdetails.objects.values_list('username', flat=True).distinct()
    mobile_numbers = Customerdetails.objects.values_list('mobile_number', flat=True).distinct()
    places = Customerdetails.objects.values_list('place', flat=True).distinct()


    customers = customers.order_by(sort_by)


    paginator = Paginator(customers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    no_results = not customers.exists()

    return render(request, 'customer_list.html', {
        'customers': page_obj,
        'page_obj': page_obj,
        'username_query': username_query,
        'mobile_number_query': mobile_number_query,
        'place_query': place_query,
        'sort_by': sort_by,
        'usernames': usernames,
        'mobile_numbers': mobile_numbers,
        'places': places,
        'no_results': no_results,
    })

def home_view(request):
    return redirect('customer_list')
