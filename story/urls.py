from django.urls import path
from story import views

app_name = 'story'

urlpatterns = [
     path('', views.StoriesView.as_view(), name='all'),
     path('create', views.CreateStoryView.as_view(), name='create'),
     path('<pk>/edit', views.EditStory.as_view(), name='edit'),
     path('<pk>/new_version', views.CreateNewVersionView.as_view(), name='new_version')
     
]
