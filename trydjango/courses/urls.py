from django.urls import path

from .views import (
    CourseView,
    MyListView,
    # my_fbv,
)

app_name = 'courses'
urlpatterns = [
    path('', MyListView.as_view(), name='courses_list'),
    path('<int:id>/', CourseView.as_view(), name='courses_detail'),

]
