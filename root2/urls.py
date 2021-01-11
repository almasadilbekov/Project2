from django.contrib import admin
from django.urls import path
from qwerty import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.first_page),

    path('second',views.second_page),

    path('second2', views.second2_page),

    path('third_page', views.third_page),

    path('fourth_page', views.fourth_page)
]
