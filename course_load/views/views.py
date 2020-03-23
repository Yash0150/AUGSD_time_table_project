import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
 
from course_load.utils import get_department_cdc_list, get_department_elective_list, get_department_instructor_list, get_instructor_list, get_department_phd_student_list
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from course_load.models import Course, Instructor, CourseInstructor

from django.shortcuts import get_object_or_404

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
    # dept = request.user.userprofile.department
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