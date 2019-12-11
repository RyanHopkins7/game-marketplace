from accounts.views import Signup
from django.urls import path, include
from django.urls import reverse_lazy

urlpatterns = [
    path('signup/', Signup.as_view(), name='wiki-signup'),
    path('', include('django.contrib.auth.urls')),
]
