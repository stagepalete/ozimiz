from django.core.paginator import Paginator
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from urllib.parse import unquote
from .models import *
from django.core.paginator import Paginator, EmptyPage
from django.template.context import RequestContext
from django.utils import timezone
# Create your views here.


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


def filter_courses(request):
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
    print('pagenumber:' + page_number)
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

    return render(request, 'templates/components/home/course-cards.html', context)


def course(request, pk):
    course = Course.objects.get(pk=pk)
    current_date = timezone.now().date()
    nearest_stream = course.course_stream_set.filter(start_date__gte=current_date).order_by('start_date').first()
    other_streams = course.course_stream_set.filter(start_date__gte=current_date).order_by('-start_date')
    course = course.serialize_course()
    print(other_streams)
    context = {"Course": course, "nearest_stream": nearest_stream, "other_streams": other_streams}
    return render(request, "templates/base.html", context)



