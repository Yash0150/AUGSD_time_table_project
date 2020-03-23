import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
 
from course_load.utils import get_department_cdc_list, get_department_elective_list, get_department_instructor_list, get_instructor_list, get_department_phd_student_list
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from course_load.models import Course, Instructor, CourseInstructor

from django.shortcuts import get_object_or_404

import csv
from django.http import HttpResponse

# Only for testing
from django.views.decorators.csrf import csrf_exempt

@method_decorator(login_required, name='dispatch')
class DashboardView(generic.TemplateView):
    template_name = 'course_load/dashboard.html'
    context = {}

    def get(self, request, *args, **kwargs):
        # Get required data from utils function and pass it in context
        self.context = {}
        return render(request, self.template_name, self.context)

@login_required
def get_data(request, *args, **kwargs):
    response = {}
    dept = request.user.userprofile.department
    try:
        department_cdc_list = Course.objects.filter(department = dept, course_type = 'C')
        department_elective_list = Course.objects.filter(department = dept, course_type = 'E')
        department_faculty_list = Instructor.objects.filter(department = dept, instructor_type = 'F') | Instructor.objects.filter(department = dept, instructor_type = 'S')
        faculty_list = Instructor.objects.filter()
        response['data'] = {
            'department_cdc_list': list(department_cdc_list.values('name', 'code')),
            'department_elective_list': list(department_elective_list.values('name', 'code')),
            'department_faculty_list': list(department_faculty_list.values('name', 'psrn_or_id')),
            'faculty_list': list(faculty_list.values('name', 'psrn_or_id')),
        }
        response['error'] = False
        response['message'] = 'success'
    except Exception as e:
        response['data'] = {}
        response['error'] = True
        response['message'] = str(e)
    return JsonResponse(response, safe=False)

# @login_required
@csrf_exempt
def submit_data(request, *args, **kwargs):
    response = {}
    try:
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        course = Course.objects.filter(code = data['course_code'], course_type = data['course_type'])
        course.update(
            l_count = data['l_count'],
            t_count = data['t_count'],
            p_count = data['p_count'],
            student_count = data['student_count'],
            max_strength = data['max_strength'],
            ic = Instructor.objects.get(psrn_or_id = data['ic']),
        )


        CourseInstructor.objects.filter(course = course.first(), course_type = data['course_type']).delete()
        l = data['l']
        t = data['t']
        p = data['p']
        for psrn_or_id in l:
            instructor = Instructor.objects.get(psrn_or_id = psrn_or_id)
            CourseInstructor.objects.create(
                section_type = 'L',
                course_type = data['course_type'],
                course = course.first(),
                instructor = instructor
            )
        for psrn_or_id in t:
            instructor = Instructor.objects.get(psrn_or_id = psrn_or_id)
            CourseInstructor.objects.create(
                section_type = 'T',
                course_type = data['course_type'],
                course = course.first(),
                instructor = instructor
            )
        for psrn_or_id in p:
            instructor = Instructor.objects.get(psrn_or_id = psrn_or_id)
            CourseInstructor.objects.create(
                section_type = 'P',
                course_type = data['course_type'],
                course = course.first(),
                instructor = instructor
            )

        response['error'] = False
        response['message'] = 'success'
    except Exception as e:
        response['error'] = True
        response['message'] = str(e)
    return JsonResponse(response, safe=False)

@login_required
def download_course_wise(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Course Load course-wise.csv"'
    writer = csv.writer(response)

    writer.writerow(['Course Code', 'Course Name', 'IC'])
    writer.writerow(['Instructor Name', 'L', 'T', 'P'])
    course_list = CourseInstructor.objects.filter().values('course').distinct()
    for course in course_list:
        writer.writerow([])
        writer.writerow([])
        course = Course.objects.get(code = course['course'])
        writer.writerow([course.code, course.name, course.ic])
        writer.writerow([])
        instructor_list = CourseInstructor.objects.filter(course = course).values('instructor').distinct()
        for instructor in instructor_list:
            instructor = Instructor.objects.get(psrn_or_id = instructor['instructor'])
            l_count = CourseInstructor.objects.filter(course = course, instructor = instructor, section_type = 'L').count()
            t_count = CourseInstructor.objects.filter(course = course, instructor = instructor, section_type = 'T').count()
            p_count = CourseInstructor.objects.filter(course = course, instructor = instructor, section_type = 'P').count()
            writer.writerow([instructor.name, l_count, t_count, p_count])    
    return response

@login_required
def download_instructor_wise(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Course Load instructor-wise.csv"'
    writer = csv.writer(response)

    writer.writerow(['Instructor Name', 'Deptartment'])
    writer.writerow(['Course Code', 'Course Name', 'L', 'T', 'P', 'Role'])
    instructor_list = CourseInstructor.objects.filter().values('instructor').distinct()
    for instructor in instructor_list:
        writer.writerow([])
        writer.writerow([])
        instructor = Instructor.objects.get(psrn_or_id = instructor['instructor'])
        writer.writerow([instructor.name, instructor.department])
        writer.writerow([])
        course_list = CourseInstructor.objects.filter(instructor = instructor).values('course').distinct()
        for course in course_list:
            course = Course.objects.get(code = course['course'])
            l_count = CourseInstructor.objects.filter(course = course, instructor = instructor, section_type = 'L').count()
            t_count = CourseInstructor.objects.filter(course = course, instructor = instructor, section_type = 'T').count()
            p_count = CourseInstructor.objects.filter(course = course, instructor = instructor, section_type = 'P').count()
            role = 'I'
            if course.ic == instructor:
                role = 'IC'
            writer.writerow([course.code, course.name, l_count, t_count, p_count, role])
    return response