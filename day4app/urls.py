from django.urls import path
from . import views
from .views import get_courses,YourView,SaveResult,display_data,save_results

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.main,name='main'),
    path('home', views.home, name='student_list'),
    path('chome/',views.Chome,name="Courses"),
    path('registration/', views.search_student, name='search_student'),
    path('registration/<int:student_id>/', views.register, name='register'),
    path('del/<int:id>', views.remove, name='remove_course'),
    path('edit/<int:id>', views.edit, name='edit_course'),
    path('addNew/', views.add, name='add'),
    path('save/', views.save, name='save'),
    path('del_stu/<int:id>', views.remove_stu, name='remove_stu'),
    path('edit_stu/<int:id>', views.edit_stu, name='edit_stu'),
    path('addNewStu/', views.add_stu, name='add_stu'),
    path('saveStu/', views.save_stu, name='save_stu'),
    path('remove_course/<int:student_id>/<int:course_id>/', views.remove_course, name='remove_course'),
    path('api/courses/', views.get_course_data, name='get_course_data'),
    path('api/get-courses/', views.get_courses, name='get_courses'),
    
    path('api/rates/', views.get_rates_data, name='get_rates_data'),
    path('rates/', views.rate_list, name='rate_list'),
    path('rates/add/', views.add_rate, name='add_rate'),
    path('rates/edit/<int:id>/', views.edit_rate, name='edit_rate'),
    path('rates/delete/<int:id>/', views.delete_rate, name='delete_rate'),
    
    path('api/committees/', views.get_committee_data, name='get_committee_data'),
    path('committee/', views.committee_list, name='committee_list'),
    path('committee/add/', views.add_committee, name='add_committee'),
    path('committee/edit/<int:id>/', views.edit_committee, name='edit_committee'),
    path('committee/delete/<int:id>/', views.delete_committee, name='delete_committee'),
    

    path('your-endpoint/', YourView.as_view(), name='your-view'),
    path('display_data/', views.display_data, name='display_data'),
    path('teacher_profile/', views.teacher_profile, name='teacher_profile'),

    path('save-result/', SaveResult.as_view(),name='save_result'),

    path('api/save-results/', views.save_results, name='save_results'),

     ##CHANGE##
    path("api/faculty/",views.faculty_list,name="faculty_list"),
    path("faculties/",views.faculty_members,name="faculty_members"),
    path('edit_faculty/<int:id>/', views.edit_faculty, name='edit_faculty'),
    path('remove_faculty/<int:faculty_id>/', views.remove_faculty, name='remove_faculty'),
    path('add_faculty/', views.add_faculty, name='add_faculty'),

]
