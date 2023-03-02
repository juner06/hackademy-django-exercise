"""hackademy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from activity1.views import profile_view, edit_view, home_view
from django.conf import settings
from django.conf.urls.static import static
from api.views import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView



urlpatterns = [
    path('', home_view, name='home'),
    path('', include('activity1.urls')),
    path('', include('django.contrib.auth.urls')),
    path('profile', profile_view, name="profilepage"),
    path('profile/edit', edit_view, name="edit_user"),
    path('api/', include('api.urls')),
    path('api/users', UserListView.as_view()),
    path('api/users/<int:user_id>[GET]', UserDetailView.as_view()),
    path('api/users', UserCreateView.as_view()),
    path('api/users/<int:user_id>[PUT]', UserUpdateView.as_view()),
    path('api/users/<int:user_id>[DELETE]', UserDeleteView.as_view()),
    path('admin/', admin.site.urls),
    path('__debug__', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)