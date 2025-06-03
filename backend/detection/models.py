from django.db import models

class DetectionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add = True)
    people_detected = models.IntegerField()
    frame_processed = models.BooleanField(default = True)




