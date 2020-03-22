import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AUGSD_time_table_project.settings')

import django

django.setup()
from course_load.models import UserProfile, Department, Course
from course_load.utils import get_department_list, get_department_cdc_list, get_department_elective_list

from django.contrib.auth.models import User

def create_super_user():
    try:
        (super_user, created) = User.objects.get_or_create(username="admin", is_superuser=True)
        super_user.set_password('password')
        super_user.is_staff = True
        super_user.is_admin = True
        super_user.is_superuser = True
        super_user.save()
    except:
        print("Error occurred while creating super user")

def create_user_profile():
    try:
        dept_list = get_department_list()
        for i in dept_list:
            (mUser, created) = User.objects.get_or_create(username = 'hod_'+i)
            mUser.set_password('password')
            mUser.save()
            (dept, created) = Department.objects.get_or_create(code = i, name = i)
            dept.save()
            UserProfile.objects.create(user = mUser, department = dept)
            
    except Exception as e:
        print(str(e))
        print("Error creating user profiles")

def create_course():
    try:
        dept_list = get_department_list()
        for i in dept_list:
            dept = Department.objects.get(code = i)
            department_cdc_list = get_department_cdc_list(i)
            for cdc in department_cdc_list:
                print(cdc[0], ' ', cdc[1])
                Course.objects.create(code = cdc[0], name = cdc[1], course_type = 'C', department = dept)
            # department_elective_list = get_department_elective_list(i)
            # for elective in department_elective_list:
            #     Course.objects.create(code = elective[0], name = elective[1], course_type = 'E', department = dept)

    except Exception as e:
        print(str(e))
        print("Error creating courses")

if __name__ == '__main__':

    print("Clearing database")
    User.objects.all().delete()
    UserProfile.objects.all().delete()
    Course.objects.all().delete()

    print("Creating superuser")
    create_super_user()

    print("Creating users")
    create_user_profile()

    print("Creating courses")
    create_course()

    print("Done!")