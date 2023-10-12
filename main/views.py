from datetime import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from products.models import Users, Product, ProductCategory
from .models import Posts

def home(request):

  if request.method == "POST":
    
    user = Users.objects.get(id=request.session['user_id'])

    description = request.POST['description']

    uploadImageInput = request.FILES.get('uploadImageInput', None)

    post = Posts(postUser = user, post_picture = uploadImageInput, post_description = description)
    post.save()

    return redirect('/home')

    
 
  if 'user_id' in request.session:
    user = Users.objects.get(id=request.session['user_id'])
    product_list = Product.objects.all().select_related('product_category').values(
    'id', 'product_picture', 'product_name', 'product_description', 'total_likes', 'total_favorites', 'total_reviews',
    'product_category__category_name', 'product_category__category_icon'
    )

    post_list = Posts.objects.filter(Q(is_shown=True)).order_by('-datetimePublished').select_related('postUser').values(
      'id', 'postUser__id', 'postUser__username', 'post_picture', 'post_description', 'total_likes', 'total_favorites', 'datetimePublished'
      )
    
    dt = datetime.now()

    print(user, request)
    
    return render(request, 'home.html', {"user": user, "datetime": dt, 'product_list': product_list, 'post_list' : post_list})
  
  else:
    return redirect('/authentication/login')



def landing(request):
  request.session.flush()
  template = loader.get_template('landing.html')
  return HttpResponse(template.render())



def test(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())



def profile(request):
  if 'user_id' in request.session:
    
    user = Users.objects.get(id=request.session['user_id'])

    post_list = Posts.objects.filter(Q(postUser__id = request.session['user_id'])).select_related('postUser').values(
      'id', 'postUser__id', 'postUser__username', 'post_picture', 'post_description', 'total_likes', 'total_favorites', 'datetimePublished'
    )

    print(post_list)

    return render(request, 'profile.html', {"user": user, "post_list": post_list})


def search_body(request, search):

  post_list = Posts.objects.filter(Q(post_description__contains =search) | Q(post_description__startswith =search[0])).select_related('postUser').values(
    'id', 'postUser__id', 'postUser__username', 'post_picture', 'post_description', 'total_likes', 'total_favorites', 'datetimePublished'
  )
  
  products_list = Product.objects.filter(Q(product_name__contains =search) | Q(product_name__startswith =search[0]) | Q(product_description__contains=search) | Q(product_description__startswith =search[0])).select_related('product_category').values(
    'id', 'product_picture', 'product_name', 'product_description', 'total_likes', 'total_favorites', 'total_reviews',
    'product_category__category_name', 'product_category__category_icon'
  )
  
  print(search[0], post_list, products_list)

  return render(request, 'search_body.html', {'post_list' : post_list, 'products_list' : products_list})

def add_post(request):

  return render(request, 'home.html')



def update_post(request, id):
  
  description = request.POST['description']
  changeImageInput = request.FILES.get('changeImageInput', None)

  post = Posts.objects.get(id=id)
  post.post_description = description
  post.post_picture = changeImageInput

  post.save()

  return redirect('/home')



def delete_post(request, id):

  post = Posts.objects.get(id=id)
  post.is_shown = False

  post.save()
  
  return redirect('/home')


def undelete_post(request, id):

  post = Posts.objects.get(id=id)
  post.is_shown = True

  post.save()

  return redirect('/home')
