




from datetime import datetime
from django.db.models import Q
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from products.models import Users, Product, ProductCategory
from .models import Comments, Posts, Interaction
from django.db.models import Prefetch
import json

def test(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())


def landing(request):
  # request.session.flush()
  return render(request, 'landing.html', { 'current_year': datetime.now().year})


def home(request, param):

  if request.method == "POST":
    user = Users.objects.get(id=request.session['user_id'])
    description = request.POST['description']
    uploadImageInput = request.FILES.get('uploadImageInput', None)

    post = Posts(post_user = user, post_picture = uploadImageInput, post_description = description)
    post.save()

    return redirect('/home')

  
  # FOR RENDER FUNCTION
  user = Users.objects.get(id=request.session['user_id'])
  product_list = Product.objects.all().select_related('product_category').values(
  'id', 'product_picture', 'product_name', 'product_description', 'total_likes','total_favorites', 'total_reviews',
  'product_category__category_name', 'product_category__category_icon'
  )

  # removed filter(Q(is_shown=True))
  post_list = Posts.objects.order_by('-datetime_published').select_related('post_user').prefetch_related( Prefetch('comments', queryset=Comments.objects.prefetch_related('replies')))

  # for post in post_list:
  #   for comments in post.comments_set.all():
  #     print(post, post.id, "com:", comments, 'tis', comments.comments_set.all())


  dt = datetime.now()

  user_list = list(Users.objects.filter(Q(id = user.id)).values_list())
  interaction_list = list(Interaction.objects.filter(Q(user_id = user.id)).values_list())
  
  return render(request, 'home.html', {"user_list": user_list, "user": user, "current_year": datetime.now().year, 'product_list': product_list, 'post_list' : post_list, "interaction_list" : interaction_list })
  

def favorites(request):
  user = Users.objects.get(id=request.session['user_id'])

  # user.posts_set.all() --- the objects in a list
  post_list = user.posts_set.all().values()  # the objects with values

  interactions = user.interaction_set.all().select_related('post').filter(is_post_favorite = True) #.all()
  
  post_list = Posts.objects.order_by('-datetime_published').select_related('post_user').prefetch_related( Prefetch('comments', queryset=Comments.objects.prefetch_related('replies')))

  user_list = json.dumps((Users.objects.filter(Q(id = user.id)).values().first()))
  interaction_toList = list(interactions.values_list())
  print('lop', user_list, interaction_toList)
  return render(request, 'favorites.html', {"current_year": datetime.now().year, "user_list": user_list, "post_list": post_list, 'interaction_toList' : interaction_toList, 'interactions' : interactions})


def notifications(request):

  return render(request, 'notification.html')

def about(request):

  return render(request, 'about.html', {"current_year": datetime.now().year,})

def team(request):

  return render(request, 'team.html', {"current_year": datetime.now().year,})



def profile(request):
  user = Users.objects.get(id=request.session['user_id'])

  if request.method == "POST":
    user.username = request.POST['username']
    user.bio = request.POST['bio']
    user.save()
  
  # user.posts_set.all() --- the objects in a list
  user_post_list = user.posts_set.all().values()  # the objects with values

  return render(request, 'profile.html', {"current_year": datetime.now().year,"user": user, "user_post_list": user_post_list})



def search_body(request, search):

  posts_list = Posts.objects.filter(Q(post_description__contains =search) | Q(post_description__startswith =search[0])).select_related('post_user').values(
    'id', 'post_user__id', 'post_user__username', 'post_picture', 'post_description', 'total_likes','total_dislikes','total_favorites', 'datetime_published'
  )
  
  # | Q(product_description__contains=search) | Q(product_description__startswith =search[0]
  products_list = Product.objects.filter(Q(product_name__contains =search) | Q(product_name__startswith =search[0])).select_related('product_category').values(
    'id', 'product_picture', 'product_name', 'product_description', 'total_likes', 'total_favorites', 'total_reviews',
    'product_category__category_name', 'product_category__category_icon'
  )
  
  print(search[0], posts_list, products_list)

  return render(request, 'search_body.html', {'posts_list' : posts_list, 'current_year': datetime.now().year, 'products_list' : products_list})


def add_comment(request, user_id, post_id):

  user = Users.objects.get(id=user_id)
  post = Posts.objects.get(id=post_id)


  if request.method == "POST":

    # Get the JSON payload from the request bod
    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON payload'}, status=400)
    
    # Access the 'comment' field from the JSON payload
    comment = payload.get('comment_text', '')

    # Add comment object to database
    new_comment = Comments.objects.create(comment_user = user, post = post, comment_description = comment)
    new_comment_dict = model_to_dict(new_comment)
    
    formatted_time = datetime.now().strftime("%b %d %Y, %I:%M %p").replace('AM', 'a.m.').replace('PM', 'p.m.')

    # print("this is he", new_comment, user_id, post_id, post.comments_set.all())

    return JsonResponse({"new_comment" : new_comment_dict, "comment_username" : user.username, "datetime_now" : formatted_time})
  return JsonResponse({'error': 'Invalid request'}, status=400)


def edit_comment(request, comment_id):

  if request.method == "POST":

    # Get the JSON payload from the request bod
    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON payload'}, status=400)
    
    # Access the 'comment' field from the JSON payload
    newCommentDescription = payload.get('newCommentDescription', '')

    # Add comment object to database
    comment = Comments.objects.get(id = comment_id)
    comment.comment_description = newCommentDescription
    comment.save()

    return JsonResponse({"yey" : 12})
  return JsonResponse({'error': 'Invalid request'}, status=400)


def delete_comment(request, comment_id):

  if request.method == "DELETE":
    comment = Comments.objects.get(id = comment_id)
    comment.delete()

    return JsonResponse({"yey" : 12})
  return JsonResponse({'error': 'Invalid request'}, status=400)


def add_reply(request, user_id, comment_id):

  user = Users.objects.get(id=user_id)

  if request.method == "POST":
    comment = Comments.objects.get(id=comment_id);

    # Get the JSON payload from the request bod
    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON payload'}, status=400)
    
    # Access the 'comment' field from the JSON payload
    reply_content = payload.get('reply_content', '')

    Comments.objects.create(comment_user = user, comment_description = reply_content, comment_replies=comment)

    print(comment, reply_content, 'klore')

    return JsonResponse({"yey" : 12})
  return JsonResponse({"yey" : 112})


def view_post(request):
  if request.method == "POST":

    comment_list = 1
    return render(request, "view_post.html", { 'comment_list' : comment_list})



def add_post(request, param):
  if request.method == "POST":

    user = Users.objects.get(id=request.session['user_id'])
    description = request.POST['description']
    uploadImageInput = request.FILES.get('uploadImageInput', None)

    post = Posts(post_user = user, post_picture = uploadImageInput, post_description = description)
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


def delete_post(request, id):
  post = Posts.objects.get(id=id)
  post.delete()
  
  return redirect('/home')

def visibility_post(request, id):
  post = Posts.objects.get(id=id)
  post.is_shown = not post.is_shown
  post.save()
  
  return JsonResponse({'post_visibility' : post.is_shown })



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


def like_interaction(request, user_id, post_id):
  if request.method == 'POST':
    user = Users.objects.get(id=user_id)
    post = Posts.objects.get(id=post_id)

    try:
      interaction = Interaction.objects.get(Q(user__id=user_id) & Q(post__id=post_id))
      interaction.is_post_liked = not interaction.is_post_liked
      interaction.save()

    except Interaction.DoesNotExist:
      interaction = Interaction.objects.create(user = user, post = post, is_post_liked = True)

    post.total_likes = post.interaction_set.filter(is_post_liked = True).count()
    post.save()

    return JsonResponse({'isLiked': interaction.is_post_liked, "total_likes" : post.total_likes})
  return JsonResponse({'error': 'Invalid request'}, status=400)

def dislike_interaction(request, user_id, post_id):
  if request.method == 'POST':
    user = Users.objects.get(id=user_id)
    post = Posts.objects.get(id=post_id)

    try:
      interaction = Interaction.objects.get(Q(user__id=user_id) & Q(post__id=post_id))
      interaction.is_post_disliked = not interaction.is_post_disliked
      interaction.save()

    except Interaction.DoesNotExist:
      interaction = Interaction.objects.create(user = user, post = post, is_post_disliked = True)

    post.total_dislikes = post.interaction_set.filter(is_post_disliked = True).count()
    post.save()

    return JsonResponse({'isDisliked': interaction.is_post_disliked, "total_dislikes" : post.total_dislikes})
  return JsonResponse({'error': 'Invalid request'}, status=400)


def heart_interaction(request, user_id, post_id):
  if request.method == 'POST':
    user = Users.objects.get(id=user_id)
    post = Posts.objects.get(id=post_id)

    try:
      interaction = Interaction.objects.get(Q(user__id=user_id) & Q(post__id=post_id))
      interaction.is_post_favorite = not interaction.is_post_favorite
      interaction.save()

    except Interaction.DoesNotExist:
      interaction = Interaction.objects.create(user = user, post = post, is_post_favorite = True)

    post.total_favorites = post.interaction_set.filter(is_post_favorite = True).count()
    post.save()

    return JsonResponse({'isFavorite': interaction.is_post_favorite, "total_favorites" : post.total_favorites})
  return JsonResponse({'error': 'Invalid request'}, status=400)



