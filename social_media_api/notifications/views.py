from rest_framework.decorators import api_view  # Ensure this is imported
from rest_framework.response import Response  # Ensure this is imported
from .models import Notification  # Import the Notification model
from django.contrib.contenttypes.models import ContentType  # Needed for content type usage

# Fetch unread notifications for the authenticated user
@api_view(['GET'])
def user_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user, read=False).order_by('-timestamp')
    
    # Create a list of notifications with relevant details
    data = [
        {
            'actor': n.actor.username,
            'verb': n.verb,
            'target': str(n.target),  # Ensure that target is handled as a string
            'timestamp': n.timestamp
        } for n in notifications
    ]
    
    return Response(data)

# Mark a specific notification as read
@api_view(['POST'])
def mark_as_read(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id, recipient=request.user)
        notification.read = True
        notification.save()
        return Response({'status': 'Notification marked as read'})
    except Notification.DoesNotExist:
        return Response({'error': 'Notification not found'}, status=404)

