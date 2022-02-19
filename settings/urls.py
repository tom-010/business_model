from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('business_model_canvas.urls', namespace='business_model_canvas')),
    path('admin/', admin.site.urls),
]
