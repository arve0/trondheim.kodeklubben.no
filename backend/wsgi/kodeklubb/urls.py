from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from class_based_auth_views.views import LoginView

from rest_framework import viewsets, routers

from newsfeed.views import NewsView
#from usermanagement.views import UserView, login, logout, LoginView
from courses.views import CourseView, FullCourseView

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'news',NewsView, base_name='news')
router.register(r'courses',CourseView, base_name='courses')
router.register(r'courses_full', FullCourseView, base_name='courses_full')
#router.register(r'users', UserView, base_name='users')
#router.register(r'users', LoginView, base_name='login')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'tinymce/', include('tinymce.urls')),
    url(r'login/',LoginView.as_view(form_class=EmailAsUsernameAuthenticationForm), name="login"),
    url(r'^register/', CreateView.as_view(
        template_name='register.html',
        form_class=UserCreationForm,
        success_url='/')),
    url(r'accounts/', include('registration.backends.default.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
