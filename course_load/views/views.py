from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
 
from course_load.utils import get_department_cdc_list, get_department_elective_list, get_department_faculty_list, get_faculty_list, get_phd_scholar_list
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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
    dept = request.user.userprofile.department.code
    try:
        department_cdc_list = get_department_cdc_list(dept)
        department_elective_list = get_department_elective_list(dept)
        department_faculty_list = get_department_faculty_list(dept)
        faculty_list = get_faculty_list()
        response['data'] = {
            'department_cdc_list': department_cdc_list,
            'department_elective_list': department_elective_list,
            'department_faculty_list': department_faculty_list,
            'faculty_list': faculty_list,
        }
        response['error'] = False
        response['message'] = 'success'
    except Exception as e:
        response['data'] = {}
        response['error'] = True
        response['message'] = str(e)
    return JsonResponse(response, safe=False)

