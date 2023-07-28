from django.shortcuts import render
from courses.forms import UserForm,UserProfileInfoForm, MainCoursesForm
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Udemy, Level, Subjects, Price
from django.shortcuts import redirect

# Create your views here.
def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(
            Q(course_title__icontains=q) |
            Q(course_id__icontains=q) |
            Q(subject__subject__icontains=q) |
            Q(level__level__icontains=q) |
            Q(url__icontains=q)
        )
        courses = Udemy.objects.filter(multiple_q)
    elif 'min_price' in request.GET and 'max_price' in request.GET:
        max_price = request.GET['max_price']
        min_price = request.GET['min_price']
        courses = Udemy.objects.filter(price__price__lte= max_price, price__price__gte=min_price)
        courses = courses.order_by('price')
    elif 'min_subs' in request.GET and 'max_subs' in request.GET:
        min_subs = request.GET['min_subs']
        max_subs = request.GET['max_subs']
        courses = Udemy.objects.filter(num_subscribers__lte=max_subs, num_subscribers__gte=min_subs)
        courses = courses.order_by('num_subscribers')
    elif 'min_cont' in request.GET and 'max_cont' in request.GET:
        min_cont = request.GET['min_cont']
        max_cont = request.GET['max_cont']
        courses = Udemy.objects.filter(content_duration__lte=max_cont, content_duration__gte=min_cont)
        courses = courses.order_by('content_duration')
    elif 'min_rev' in request.GET and 'max_rev' in request.GET:
        min_rev = request.GET['min_rev']
        max_rev = request.GET['max_rev']
        courses = Udemy.objects.filter(num_reviews__lte=max_rev, num_reviews__gte=min_rev)
        courses = courses.order_by('num_reviews')
    elif 'min_lec' in request.GET and 'max_lec' in request.GET:
        min_lec = request.GET['min_lec']
        max_lec = request.GET['max_lec']
        courses = Udemy.objects.filter(num_lectures__lte=max_lec, num_lectures__gte=min_lec)
        courses = courses.order_by('num_lectures')
    else:
        courses = Udemy.objects.all()

    context = {
        'courses': courses,
    }
    return render(request,'basic_apps/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MainCoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:index')  # Redirect to a page where you list all courses after creating one
    else:
        form = MainCoursesForm()
    return render(request, 'full/create_course.html', {'form': form})


    return render(request, 'basic_apps/index.html', context)





def delete(request, course_id):
    course = Udemy.objects.get(pk=course_id)
    if request.method == 'POST':
        #course.price.delete()
        #course.level.delete()
        course.delete()
        return redirect('courses:index')
    return render(request, 'basic_apps/index.html')




def update(request, course_id):
    course = Udemy.objects.get(pk=course_id)
    form = MainCoursesForm(instance=course)
    if request.method == 'POST':
        form = MainCoursesForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('udemy_courses:udemy_courses')  # Redirect to a page where you list all courses after creating one
    else:
        form = MainCoursesForm(instance=course)
    return render(request, 'basic_apps/update.html', {'form': form})



@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/courses/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user
            # save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'basic_apps/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_apps/login.html', {})
