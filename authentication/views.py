from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from products.models import Users

def myfirst(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())



def login(request):

  print("Sesion User Id:", request.session.get('user_id', 'User ID not found'))
  if 'user_id' in request.session:
     return redirect("/home")
  


  if request.method == "POST":
    
    usernameinput = request.POST['usernamefield']
    passwordinput = request.POST['passwordfield']

    try:
        user = Users.objects.get(username=usernameinput, password=passwordinput)
        request.session['user_id'] = user.id
        request.session['username'] = user.username
        request.session['password'] = user.password

        print("Session Username", request.session['username'] )

        return redirect("/home")
    
    except Users.DoesNotExist:
        return render(request, 'login.html', {'Error' : "User does not Exist!"})

  return render(request, 'login.html')




def admin(request):

  if 'user_id' in request.session:
     return redirect("/home")
  
  if request.method == "POST":
    
    usernameinput = request.POST['usernamefield']
    passwordinput = request.POST['passwordfield']

    try:
        user = Users.objects.get(username=usernameinput, password=passwordinput)
        request.session['user_id'] = user.id
        request.session['username'] = user.username
        request.session['password'] = user.password

        return redirect("/home")
   
    except Users.DoesNotExist:
        return render(request, 'admin.html', {'Error' : "User does not Exist!"})

  return render(request, 'admin.html')




def signup(request):

  if request.method == "POST":
    
    usernameinput = request.POST['usernameinput']
    passwordinput = request.POST['passwordinput']

    user = Users(username=usernameinput, password=passwordinput)
    user.save()
    
    return redirect("/authentication/login")
  

  return render(request, 'signup.html')



def logout(request):
    # Check if 'username' key exists in the session
    if 'user_id' in request.session:
        # Print the username before flushing
        print("Before flush:", request.session['user_id'])
    
    # Flush the session
    request.session.flush()
    
    # Print the username after flushing (it should not exist)
    print("After flush:", request.session.get('user_id', 'User _D not found'))
    
    # Redirect to the login page
    return redirect("/authentication/login")


def delete_account(request, id):
   
   user = Users.objects.get(id=id)
   user.delete()

   request.session.flush()
   
   return redirect('/')


 