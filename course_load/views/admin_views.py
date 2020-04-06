import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from course_load.forms import *
from course_load.models import Course, Instructor, CourseInstructor

@method_decorator(login_required, name='dispatch')
class AddCourse(View):
    form_class = AddCourseForm
    initial = {'key': 'value'}
    template_name = 'admin/add-course.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            return HttpResponseRedirect('/course-load/dashboard')

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            try:
                form = self.form_class(request.POST)
                if form.is_valid():
                    course, created = Course.objects.get_or_create(
                        code = form.cleaned_data['code'], 
                        name = form.cleaned_data['name'], 
                        department = form.cleaned_data['department'], 
                        course_type = form.cleaned_data['course_type'], 
                    )
                    return HttpResponseRedirect('/course-load/dashboard')
                return render(request, self.template_name, {'form': form})
            except Exception as e:
                print(e)
                return render(request, self.template_name, {'form': form})
        else:
            return HttpResponseRedirect('/course-load/dashboard')

@method_decorator(login_required, name='dispatch')
class AddInstructor(View):
    form_class = AddInstructorForm
    initial = {'key': 'value'}
    template_name = 'admin/add-instructor.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            return HttpResponseRedirect('/course-load/dashboard')

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            try:
                form = self.form_class(request.POST)
                if form.is_valid():
                    instructor, created = Instructor.objects.get_or_create(
                        psrn_or_id = form.cleaned_data['psrn_or_id'], 
                        name = form.cleaned_data['name'], 
                        department = form.cleaned_data['department'], 
                        instructor_type = form.cleaned_data['instructor_type'], 
                    )
                    return HttpResponseRedirect('/course-load/dashboard')
                return render(request, self.template_name, {'form': form})
            except Exception as e:
                print(e)
                return render(request, self.template_name, {'form': form})
        else:
            return HttpResponseRedirect('/course-load/dashboard')

@method_decorator(login_required, name='dispatch')
class UpdateCourse(View):
    form_class = UpdateCourseForm
    initial = {'key': 'value'}
    template_name = 'admin/update-course.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            return HttpResponseRedirect('/course-load/dashboard')

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            try:
                course = Course.objects.get(code = request.POST['old_code'])
                course_original = Course.objects.get(code = request.POST['old_code'])
                form = self.form_class(request.POST, instance = course)
            except Course.DoesNotExist:
                form = self.form_class(initial=self.initial)
                return render(request, self.template_name, {'form': form})
            course.delete()
            try:
                if form.is_valid():
                    form.code = form.cleaned_data['code'], 
                    form.name = form.cleaned_data['name'], 
                    form.department = Department.objects.get(code = form.cleaned_data['department']), 
                    form.course_type = form.cleaned_data['course_type'], 
                    form.save()
                    return HttpResponseRedirect('/course-load/dashboard')
            except Exception as e:
                course_original.save()
                print(e)
                return render(request, self.template_name, {'form': form})
        else:
            return HttpResponseRedirect('/course-load/dashboard')

@method_decorator(login_required, name='dispatch')
class UpdateInstructor(View):
    form_class = UpdateInstructorForm
    initial = {'key': 'value'}
    template_name = 'admin/update-instructor.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            return HttpResponseRedirect('/course-load/dashboard')

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            try:
                instructor = Instructor.objects.get(psrn_or_id = request.POST['old_psrn_or_id'])
                instructor_original = Instructor.objects.get(psrn_or_id = request.POST['old_psrn_or_id'])
                form = self.form_class(request.POST, instance = instructor)
            except Instructor.DoesNotExist:
                form = self.form_class(initial=self.initial)
                return render(request, self.template_name, {'form': form})
            instructor.delete()
            try:
                if form.is_valid():
                    form.psrn_or_id = form.cleaned_data['psrn_or_id'], 
                    form.name = form.cleaned_data['name'], 
                    form.department = Department.objects.get(code = form.cleaned_data['department']), 
                    form.instructor_type = form.cleaned_data['instructor_type'], 
                    form.save()
                    return HttpResponseRedirect('/course-load/dashboard')
            except Exception as e:
                instructor_original.save()
                print(e)
                return render(request, self.template_name, {'form': form})
        else:
            return HttpResponseRedirect('/course-load/dashboard')

@method_decorator(login_required, name='dispatch')
class DeleteCourse(View):
    form_class = DeleteCourseForm
    initial = {'key': 'value'}
    template_name = 'admin/delete-course.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            return HttpResponseRedirect('/course-load/dashboard')

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            try:
                course = Course.objects.get(code = request.POST['code'])
            except Course.DoesNotExist:
                form = self.form_class(initial=self.initial)
                return render(request, self.template_name, {'form': form})
            course.delete()
            return HttpResponseRedirect('/course-load/dashboard')
        else:
            return HttpResponseRedirect('/course-load/dashboard')

@method_decorator(login_required, name='dispatch')
class DeleteInstructor(View):
    form_class = DeleteInstructorForm
    initial = {'key': 'value'}
    template_name = 'admin/delete-instructor.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            return HttpResponseRedirect('/course-load/dashboard')

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            try:
                instructor = Instructor.objects.get(psrn_or_id = request.POST['psrn_or_id'])
            except Instructor.DoesNotExist:
                form = self.form_class(initial=self.initial)
                return render(request, self.template_name, {'form': form})
            instructor.delete()
            return HttpResponseRedirect('/course-load/dashboard')
        else:
            return HttpResponseRedirect('/course-load/dashboard')

@login_required
def get_course_preview(request):
    code = request.GET.get('course_code', None)
    try:
        course = Course.objects.get(code = code)
        data = {
            'name': course.name,
            'comcode': course.comcode,
            'department': course.department.name,
            'course_type': course.course_type,
        }
    except Exception as e:
        print(e)
        data = {
            'name': '',
            'comcode': '',
            'departemnt': '',
            'course_type': '',
        }
    return JsonResponse(data)

@login_required
def get_instructor_preview(request):
    psrn_or_id = request.GET.get('psrn_or_id', None)
    try:
        instructor = Instructor.objects.get(psrn_or_id = psrn_or_id)
        data = {
            'name': instructor.name,
            'department': instructor.department.name,
            'instructor_type': instructor.instructor_type,
        }
    except Exception as e:
        print(e)
        data = {
            'name': '',
            'departemnt': '',
            'instructor_type': '',
        }
    return JsonResponse(data)


@login_required
def download_erp(request):
    if request.user.is_superuser:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Course Load ERP.csv"'
        writer = csv.writer(response)
        writer.writerow(['Comcode', 'Course number', 'Course title', 'Section type', 'Section number', 'Instructor name', 'PSRN/ID', 'Role'])
        course_list = Course.objects.filter(ic__isnull = False).values('code').distinct()
        for course in course_list:
            course = Course.objects.get(code = course['code'])

            ic = course.ic
            l_entry_list = CourseInstructor.objects.filter(course = course, instructor = ic, section_type = 'L')
            for entry in l_entry_list:
                writer.writerow([course.comcode, course.code, course.name, entry.section_type, entry.section_number, ic.name, ic.psrn_or_id, 'IC'])
            t_entry_list = CourseInstructor.objects.filter(course = course, instructor = ic, section_type = 'T')
            for entry in t_entry_list:
                writer.writerow([course.comcode, course.code, course.name, entry.section_type, entry.section_number, ic.name, ic.psrn_or_id, 'IC'])
            p_entry_list = CourseInstructor.objects.filter(course = course, instructor = ic, section_type = 'P')
            for entry in p_entry_list:
                writer.writerow([course.comcode, course.code, course.name, entry.section_type, entry.section_number, ic.name, ic.psrn_or_id, 'IC'])
                
            instructor_list = CourseInstructor.objects.filter(course = course).values('instructor').distinct()
            for instructor in instructor_list:
                if instructor['instructor'] == ic.psrn_or_id:
                    continue
                instructor = Instructor.objects.get(psrn_or_id = instructor['instructor'])
                l_entry_list = CourseInstructor.objects.filter(course = course, instructor = instructor, section_type = 'L')
                for entry in l_entry_list:
                    writer.writerow([course.comcode, course.code, course.name, entry.section_type, entry.section_number, instructor.name, instructor.psrn_or_id, 'I'])
                t_entry_list = CourseInstructor.objects.filter(course = course, instructor = instructor, section_type = 'T')
                for entry in t_entry_list:
                    writer.writerow([course.comcode, course.code, course.name, entry.section_type, entry.section_number, instructor.name, instructor.psrn_or_id, 'I'])
                p_entry_list = CourseInstructor.objects.filter(course = course, instructor = instructor, section_type = 'P')
                for entry in p_entry_list:
                    writer.writerow([course.comcode, course.code, course.name, entry.section_type, entry.section_number, instructor.name, instructor.psrn_or_id, 'I'])
        return response
    else:
        return HttpResponseRedirect('/course-load/dashboard')