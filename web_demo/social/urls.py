from django.urls import include, path

from .views import notifications

urlpatterns = [
    path('', notifications, name='notifications'),
#     path('announcement/add/',add_announcement, name='add_announcement'),
#     path('announcement/<int:id>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
#     path('ew/', ew, name='ew'),
#     path('ew/add/', ew_add, name='ew_add'),
#     path('ew/monthly/<int:year>/<str:month>/', ew_month, name='ew_month'),
]
