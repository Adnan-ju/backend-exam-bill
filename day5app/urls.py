# from django.contrib import admin
# from django.urls import path
# from .import views
# # from django.urls import path,include


# urlpatterns = [
#       path("",views.home,name='index'),
#       path("del/<int:id>",views.remove,name='remove'),
#       path("edit/<int:id>",views.edit,name='edit'),
#       path("addnew/",views.add,name='add'),
#       path("save/",views.save,name='save'),
 
# ]

# urls.py

from django.urls import path
from .views import YourView

urlpatterns = [
    path('your-endpoint/', YourView.as_view(), name='your-view'),
]
