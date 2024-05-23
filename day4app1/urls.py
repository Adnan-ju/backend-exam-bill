from django.contrib import admin
from django.urls import path
from .import views


# from django.urls import path,include


urlpatterns = [
      path("",views.home,name='index'),
      path("del/<int:id>",views.remove,name='remove'),
      path("edit/<int:id>",views.edit,name='edit'),
      path("addnew/",views.add,name='add'),
      path("save/",views.save,name='save'),
      # path('api/courses/', views.get_course_data, name='get_course_data'),
    # path('day3app/',include('day3app.urls')),
    # path('day4app/',include('day4app.urls')),
]
