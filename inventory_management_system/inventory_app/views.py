from django.http import JsonResponse

def home(request):
    return JsonResponse({'message': 'Inventory Management System API'})
