from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, update_course

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('courses/update/<int:course_id>/', update_course, name='update_course')
]
