from django.urls import path
from business_model_canvas import views

app_name = 'business_model_canvas'

urlpatterns = [
     path('all', views.BusinessModelCanvasesView.as_view(), name='all'),
     path('create', views.CreateBusinessModelCanvasView.as_view(), name='create'),
     path('<pk>/edit', views.EditBusinessModelCanvas.as_view(), name='edit'),
     path('<pk>/new_version', views.CreateNewVersionView.as_view(), name='new_version')
     
]
