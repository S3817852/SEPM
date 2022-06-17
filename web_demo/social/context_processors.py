from .models import Notification


def notifications(request):
    if request.user.is_authenticated:
        return {'notifications': request.user.notifications_reciver.filter(is_read=False)}
    else:
        return {'notifications': []}
