from accounts.views import Signup
from django.urls import path, include

urlpatterns = [
    path('signup/', Signup.as_view(), name='marketplace-signup'),
    path('', include('django.contrib.auth.urls')),
]
