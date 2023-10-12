from django.http import HttpResponse
from django.template import loader

def post(request):
  template = loader.get_template('post.html')
  return HttpResponse(template.render())