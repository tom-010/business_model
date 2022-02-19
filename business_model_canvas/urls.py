from django.urls import path
from business_model_canvas import views

app_name = 'business_model_canvas'

urlpatterns = [
     path('', views.BusinessModelCanvasesView.as_view(), name='all'),
     path('business_model_canvas/create', views.CreateBusinessModelCanvasView.as_view(), name='create'),
     path('business_model_canvas/<pk>/edit', views.EditBusinessModelCanvas.as_view(), name='edit'),
     path('business_model_canvas/<pk>/new_version', views.CreateNewVersionView.as_view(), name='new_version')
     
]
