from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import render
from urllib.parse import unquote
from .models import *
from django.core.paginator import Paginator, EmptyPage
# Create your views here.
def home(request):
    option = request.GET.get('option')
    currentPage = request.GET.get('currentPage')
    print(option)
    print(currentPage)
    
    if option:
        courses = Course.objects.filter(category_id__category_title=option)
    else:
        courses = Course.objects.all()

    # Create a paginator object with a page size of 2
    paginator = Paginator(courses, 2)

    # Get the current page from the request, default to 1 if not provided
    page_number = currentPage or 1

    try:
        # Get the courses for the requested page number
        current_page = paginator.page(page_number)
    except EmptyPage:
        # If the requested page is out of range, return an empty list of courses
        current_page = []

    serialized_courses = [course.serialize_course() for course in current_page]
    for course in serialized_courses:
        if 'program' in course:
            course['program'] = course['program'][0:3]
    categories = Category.objects.all()
    context = {"Courses": serialized_courses, "Categories": categories}

    return render(request, "templates/base.html", context)

from django.core.paginator import Paginator

def filter_courses(request):
    option = request.GET.get('option')
    currentPage = request.GET.get('currentPage')
    print(option)
    print(currentPage)
    if option:
        courses = Course.objects.filter(category_id__category_title=option)
    else:
        courses = Course.objects.all()

    # Apply ordering to the queryset
    courses = courses.order_by('id')

    # Create a paginator object with a page size of 2
    paginator = Paginator(courses, 2)

    # Get the current page from the request, default to 1 if not provided
    page_number = currentPage or 1

    try:
        # Get the courses for the requested page number
        current_page = paginator.page(page_number)
    except EmptyPage:
        # If the requested page is out of range, return an empty list of courses
        current_page = []

    serialized_courses = [course.serialize_course() for course in current_page]
    for course in serialized_courses:
        if 'program' in course:
            course['program'] = course['program'][0:3]
    categories = Category.objects.all()
    context = {
    "Courses": serialized_courses,
    "Categories": categories,
    "current_page": current_page,
    "totalPages": paginator.num_pages
}

    return render(request, 'templates/components/home/course-cards.html', context)