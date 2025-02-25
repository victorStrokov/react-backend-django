from customers.models import Customer
from django.http import JsonResponse
from customers.serialaizers import CustomerSerializer

def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers': serializer.data})