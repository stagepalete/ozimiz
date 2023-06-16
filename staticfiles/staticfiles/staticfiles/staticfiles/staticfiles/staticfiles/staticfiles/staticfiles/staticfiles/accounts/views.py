from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from .models import User
def login_view(request):
    if request.method == 'POST':
        # Retrieve the form data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Perform form validation
        if username and password:
            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                # Log in the user
                login(request, user)
                # Redirect to a success page
                print(user)
                return redirect('home')
                
            else:
                # Invalid credentials
                messages.error(request, 'Invalid username or password.')
        else:
            # Required fields not provided
            messages.error(request, 'Please fill in all the required fields.')

    # Render the login template
    return render(request, 'templates/components/auth/login.html')




def registration_view(request):
    if request.method == 'POST':
        # Retrieve form data
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        birth_date = request.POST.get('birth_date')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Validate form data
        # Add your validation logic here
        if not fname or not lname or not email or not password:
            # Handle validation error, e.g., display error message to the user
            error_message = "Please fill in all required fields."
            return render(request, 'templates/components/auth/register.html', {'error_message': error_message})
        
        # Create a new user account
        # Add your user creation logic here
        try:
            # Create a new user object
            user = User.objects.create_user(username=email, email=email, password=password)
            
            # Set additional user attributes
            user.first_name = fname
            user.last_name = lname
            # ...set other user attributes...
            
            # Save the user to the database
            user.save()
            
            # Perform additional registration tasks, such as sending confirmation email
            
            # Redirect to the success page or any other desired page
            return redirect('home')  # Replace 'home' with your desired success page URL or view name
        
        except Exception as e:
            # Handle any exceptions that occur during user creation
            error_message = "Registration failed. Please try again later."
            return render(request, 'templates/components/auth/register.html', {'error_message': error_message})
    
    else:
        return render(request, 'register.html')

# def registration_view(request):
#     if request.method == 'POST':
#         if request.method == 'POST':
#             fname = request.POST.get('fname')
#             lname = request.POST.get('lname')
#             birth_date = request.POST.get('birth_date')
#             phone_number = request.POST.get('phone_number')
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             return redirect('home')  # Replace with the actual success page URL
#     else:
#         form = RegistrationForm()
#     return render(request, 'templates/components/auth/register.html', {'form': form})
