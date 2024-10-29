    
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .product import Product
from .category import Category
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import Customer

# Create your views here.

def index(request):
    categories = Category.objects.all()
    
    categoryId = request.GET.get('category')
    if categoryId:
        products = Product.get_category_id(categoryId)
    else:
        products = Product.objects.all()
        
    data = {'products': products, 'categories': categories}
    return render(request, 'index.html', data)

# Signup Page

def signup(request):
    error_msg = None
    success_msg = None
    
        
    if request.method == 'GET':
        return render(request, "signup.html")
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        # password = make_password(password)
        
        
        # Validation
        if not first_name:
            error_msg = "First Name should not be empty."
        elif not last_name:
            error_msg = "Last Name should not be empty."
        elif not email:
            error_msg = "Email should not be empty."
        elif not mobile:
            error_msg = "Mobile should not be empty."
        elif not password:
            error_msg = "Password should not be empty."
            
        elif Customer.email_exists(email):  
            error_msg = "Email Already Exists"
            
            
        uservalues = {
            'first_name' : first_name ,
            'last_name' : last_name,
            'email'  :email,
            'mobile' : mobile 
        }
        
        
    if not error_msg:
            hashed_password = make_password(password)  # Hash the password
            customerData = Customer(
                first_name=first_name, 
                last_name=last_name, 
                email=email, 
                mobile=mobile, 
                password=hashed_password
            )
            customerData.save()
            success_msg = "Account created successfully"
            return render(request, 'signup.html', {'success': success_msg})
    else:
            return render(request, 'signup.html', {'error': error_msg, 'value': uservalues})
         
       
       
# login Page

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST['email']
        password = request.POST['password']
        
        error_msg = None

        user = Customer.get_email(email=email)  

        if user:
            # If email is found, check the password
            if check_password(password, user.password):  
                return redirect('/')
            else:
                error_msg = "Password is incorrect"
        else:
            error_msg = "Email is incorrect"
        
    return render(request, 'login.html', {'error': error_msg})
