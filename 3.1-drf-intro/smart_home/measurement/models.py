from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)


class Measurement(models.Model):

    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', null=True)
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

