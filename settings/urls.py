from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('business_model_canvas.urls', namespace='business_model_canvas')),
    path('story', include('story.urls', namespace='story')),
    path('admin/', admin.site.urls),
]
