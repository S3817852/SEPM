from django.urls import path, include
from .views import index, add_announcement, AnnouncementDetailView

urlpatterns = [
    path('', index, name='index'),
    path('add/',add_announcement, name='add_announcement'),
    path('<int:id>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
]