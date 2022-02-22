from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('/', RedirectView.as_view(url='/project/', permanent=False), name='index'),
    path('business_model_canvas/', include('business_model_canvas.urls', namespace='business_model_canvas')),
    path('story/', include('story.urls', namespace='story')),
    path('project/', include('story.urls', namespace='story')),
    path('admin/', admin.site.urls),
]
