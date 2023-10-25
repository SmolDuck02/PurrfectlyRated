




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

  

  user = Users.objects.get(id=request.session['user_id'])
  product_list = Product.objects.all().select_related('product_category').values(
  'id', 'product_picture', 'product_name', 'product_description', 'total_likes','total_favorites', 'total_reviews',
  'product_category__category_name', 'product_category__category_icon'
  )

  post_list = Posts.objects.filter(Q(is_shown=True)).order_by('-datetimePublished').select_related('postUser').values(
    'id', 'postUser__id', 'postUser__username', 'post_picture', 'post_description', 'total_likes','total_dislikes', 'total_favorites', 'datetimePublished'
    )

  dt = datetime.now()

  return render(request, 'home.html', {"user": user, "datetime": dt, 'product_list': product_list, 'post_list' : post_list})
  



def landing(request):
  request.session.flush()
  template = loader.get_template('landing.html')
  return HttpResponse(template.render())



def test(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())



def profile(request):
  user = Users.objects.get(id=request.session['user_id'])

  post_list = Posts.objects.filter(Q(postUser__id = request.session['user_id'])).select_related('postUser').values(
    'id', 'postUser__id', 'postUser__username', 'post_picture', 'post_description', 'total_likes','total_dislikes','total_favorites', 'datetimePublished'
  )

  return render(request, 'profile.html', {"user": user, "post_list": post_list})



def search_body(request, search):

  post_list = Posts.objects.filter(Q(post_description__contains =search) | Q(post_description__startswith =search[0])).select_related('postUser').values(
    'id', 'postUser__id', 'postUser__username', 'post_picture', 'post_description', 'total_likes','total_dislikes','total_favorites', 'datetimePublished'
  )
  
  # | Q(product_description__contains=search) | Q(product_description__startswith =search[0]
  products_list = Product.objects.filter(Q(product_name__contains =search) | Q(product_name__startswith =search[0])).select_related('product_category').values(
    'id', 'product_picture', 'product_name', 'product_description', 'total_likes', 'total_favorites', 'total_reviews',
    'product_category__category_name', 'product_category__category_icon'
  )
  
  print(search[0], post_list, products_list)

  return render(request, 'search_body.html', {'post_list' : post_list, 'products_list' : products_list})


def view_post(request):
  if request.method == "POST":

    comment_list = 1
    return render(request, "view_post.html", { 'comment_list' : comment_list})



def add_post(request, param):
  if request.method == "POST":

    user = Users.objects.get(id=request.session['user_id'])
    description = request.POST['description']
    uploadImageInput = request.FILES.get('uploadImageInput', None)

    post = Posts(postUser = user, post_picture = uploadImageInput, post_description = description)
    post.save()

    if param == 'profile':
      return redirect('/profile')
    return redirect('/home')


    
def update_post(request, id):
  
  description = request.POST['description']
  changeImageInput = request.FILES.get('changeImageInput', None)


  post = Posts.objects.get(id=id)

  post.post_description = description
  
  if(changeImageInput):
    post.post_picture = changeImageInput
  post.save()

  return redirect('/home')



def visibility_post(request, id):

  post = Posts.objects.get(id=id)
  post.is_shown = not post.is_shown
  post.save()
  
  return redirect('/home')


def update_like(request, post_id):
    if request.method == 'POST':
    
        post = Posts.objects.get(id=post_id)
        post.total_likes += 1
        post.save()

        return JsonResponse({'likes': post.total_likes})

   
    return JsonResponse({'error': 'Invalid request'}, status=400)




def update_dislike(request, post_id):
    if request.method == 'POST':
        post = Posts.objects.get(id=post_id)

        post.total_dislikes += 1
        post.save()

        return JsonResponse({'dislikes': post.total_dislikes})

    return JsonResponse({'error': 'Invalid request'}, status=400)