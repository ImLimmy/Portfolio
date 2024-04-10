from django.urls import path, include

urlpatterns = [
    # users app
    path('users/', include('users.urls')),
    
]
