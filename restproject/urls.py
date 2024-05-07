
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from restapp.views import TaskViewset, CreateuserView
from restapp import views
from django.conf.urls.static import static
from django.conf import settings

#router=routers.DefaultRouter()
router=routers.SimpleRouter()
router.register('task',TaskViewset)
router.register('completed_task',views.CompletedTaskViewset,basename='completed_task')
router.register('due_task',views.DueTaskViewset,basename='due_task')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.CreateuserView.as_view(),name='user'),
    path('api_auth/',include('rest_framework.urls')),
    path('',include(router.urls)) 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)