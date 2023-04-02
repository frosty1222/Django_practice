from django.shortcuts import get_object_or_404, render,redirect
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for product
from .serializers import ProductSerializer
# product model
from .models import Product
# Create your views here.
from django.core.paginator import Paginator
def index(request):
    context = {
        'title':'VueDj'
    }
    return render(request,'vuedj/index.html',context)
# get all product
@csrf_exempt
def products(request):
    '''
    List all product snippets
    '''
    if(request.method == 'GET'):
        # get all the products
        products = Product.objects.all()
        count = Product.objects.all().count()
        # serialize the product data
        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = ProductSerializer(page_obj, many=True)
        # return a Json response
        return JsonResponse({"data":serializer.data,"count":count},safe=False)
    elif(request.method == 'POST'):
        data = {
            'name': request.POST.get('name'),
            'description': request.POST.get('description'),
            'price': request.POST.get('price'),
            'product_image': request.FILES.get('product_image'),
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success':'Product saved'}, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
# delete product 
@csrf_exempt
def product_detail(request, id):
    try:
        # obtain the product with the passed id.
        product = Product.objects.get(id=id)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = ProductSerializer(product, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the product
        product.delete() 
        # return a no content response.
        return HttpResponse(status=204)
