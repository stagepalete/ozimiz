from django.db import models

class Category(models.Model):
    category_title = models.CharField(max_length=50)

    def __str__(self):
        return self.category_title

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    program = models.TextField()
    result = models.TextField()
    duration_months = models.IntegerField()
    duration_lesson_minutes = models.IntegerField()
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    course_logo_16 = models.CharField(max_length=255)
    course_logo_32 = models.CharField(max_length=255)
    course_logo_48 = models.CharField(max_length=255)
    course_logo_100 = models.CharField(max_length=255)
    course_banner = models.CharField(max_length=255)
    additional_info = models.TextField()

    def serialize_course(course):
        serialized_course = {
            'name': course.name,
            'description': course.description,
            'category_id': course.category_id.id,
            'program': course.program.split(';'),
            'result': course.result.split(';'),
            'duration_months': course.duration_months,
            'duration_lesson_minutes': course.duration_lesson_minutes,
            'price': str(course.price - course.price * (course.discount/100)),
            'course_logo_16': course.course_logo_16,
            'course_logo_32': course.course_logo_32,
            'course_logo_48': course.course_logo_48,
            'course_logo_100': course.course_logo_100,
            'course_banner': course.course_banner,
            'additional_info': course.additional_info,
        }
        return serialized_course

    def __str__(self):
        return self.name

class Course_stream(models.Model):
    stream_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    max_capacity = models.IntegerField()
    stream_description = models.TextField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    additional_info = models.TextField()

    def __str__(self):
        return self.stream_name

class schedult(models.Model):
    student_id = models.IntegerField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(unique=True)
    enrollment_duration = models.DurationField(unique_for_date=True, unique_for_month=True, unique_for_year=True) # Хуй знает, надо посмотреть
    enrollment_description = models.TextField()
    additional_info = models.TextField()
    