# from django.shortcuts import render
# from django.http import HttpResponse

# def members(request):
#     return HttpResponse("Yes!")


from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import ProductCategory
from authentication.models import Users
from .serializers import  ProductCategorySerializer


x = ''

@api_view(['GET', 'POST'])
def routes(request):
  allRoutes = [
    {
      'Endpoint': '/login/',
      'method': 'GET',
      'body': None,
      'description': "Returns a user"
    }
  ]
  return Response(allRoutes)


@api_view(['GET', 'POST'])
def users(request):

  user_list = Users.objects.all()
  # serializer = UsersSerializer(user_list, many=True) 
  #many=TRUE meaning serialize mny objects 
  # return Response(serializer.data)



@api_view(['GET', 'POST'])
def user(request, pk):

  user = Users.objects.get(id=pk)
  # serializer = UsersSerializer(user, many=False)
   #many=TRUE meaning serialize mny objects 
  # return Response(serializer.data)



@api_view(['PUT'])
def updateUser(request, pk):
  data = request.data
  user = Users.objects.get(id=pk)
  # serializer = UsersSerializer(instance=user, data=data)
  
  # if serializer.is_valid():
  #   serializer.save()

  # return Response(serializer.data)


@api_view(['DELETE'])
def deleteUser(request, pk):

  user = Users.objects.get(id=pk)
  user.delete()
  return Response("User Deleted :<")


@api_view(['POST'])
def createUser(request):

  data = request.data
  user = Users.objects.create(
        username=data.get('username', ''),
        password=data.get('password', '')
    )
    
  # serializer = UsersSerializer(user, many=False)
  # return Response(serializer.data)



@api_view(['GET'])
def products(request):

  products_category_list = ProductCategory.objects.all()

  serializer = ProductCategorySerializer(products_category_list, many=True) #many=TRUE meaning serialize mny objects 

  return Response(serializer.data)



@api_view(['GET'])
def home(request):

  return Response()




   # REACT


# --------------------------


  # NON REACT



def products(request):

  products_category_list = ProductCategory.objects.all()

  template = loader.get_template('products.html')
  context = {
    'product_category_list' : products_category_list
  }
  return HttpResponse(template.render(context, request))




def signup(request):
  
  if request.method == "POST":
    
    usernameinput = request.POST['usernamefield']
    passwordinput = request.POST['passwordfield']

    user = Users(username=usernameinput, password=passwordinput)
    user.save()
    
    return redirect('prod/')

  return render(request, 'signup.html')



def login(request):
  
  if request.method == "POST":
    
    usernameinput = request.POST['usernamefield']
    passwordinput = request.POST['passwordfield']

    user = Users.objects.filter(username=usernameinput, password=passwordinput).values()


    if user.count() > 0:
      global x 
      x = user
      return redirect('/profile')
    else:
      print("Wop")

  return render(request, 'login.html')


def profile(request):
 
    context = {
      'current_user' : x
    }

    return render(request, 'profile.html', context)


def jameel(request):
  return render(request, 'jameel.html')