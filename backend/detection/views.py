from django.db.models import Sum, Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DetectionLog
from django.forms.models import model_to_dict
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.views.generic import TemplateView

current_total_people = 0
current_total_frames = 0
current_average_people = 0


@api_view(['POST'])
def log_detection(request):
    global current_total_people, current_total_frames
    data = request.data 
    stat = DetectionLog.objects.create(
        people_detected=data['people_detected'],
        frame_processed=data['frame_processed']  
    )

    if data['frame_processed']:
        current_total_frames += 1
        current_total_people += data['people_detected']
        
    current_average_people = round(current_total_people / current_total_frames, 2) if current_total_frames else 0
    

    total_people = DetectionLog.objects.aggregate(Sum('people_detected'))['people_detected__sum'] or 0
    total_frames = DetectionLog.objects.filter(frame_processed=True).count()
    average_people = round(total_people / total_frames, 2) if total_frames else 0



    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "stats", {
            "type": "send_update",
            "stat": {
                "total_people": total_people,
                "total_frames": total_frames,
                "average_people": average_people,
                "current_people": current_total_people,
                "current_total_frames": current_total_frames,
                "current_average": current_average_people

            }
        }
    )

    return Response({"status": "ok"})


class FrontendAppView(TemplateView):
    template_name = 'index.html'

