from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('day2app/',include('day2app.urls')),
    path('day3app/',include('day3app.urls')),
    path('day4app/',include('day4app.urls')),
    path('day5app/',include('day5app.urls')),
]
