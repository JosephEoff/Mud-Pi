from django.contrib.gis.db import models

class Sensor(models.Model):
    sensorID = models.CharField(max_length = 100)
    controlnode = models.ForeignKey('controlnode.ControlNode',  on_delete=models.CASCADE)
    location = models.PointField()
    
    def __str__(self):
        return self.sensorID

class SensorDataUnit(models.Model):
    name = models.CharField(max_length = 50)
    abbreviatedName = models.CharField(max_length = 5)
    
    def __str__(self):
        return self.name
        
class SensorDataType(models.Model):
    typeName = models.CharField(max_length = 50)
    unit = models.ForeignKey(SensorDataUnit,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.typeName
    
class SensorData(models.Model):
    sensor =  models.ForeignKey(Sensor,  on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    datatype = models.ForeignKey(SensorDataType,  on_delete=models.CASCADE)
    value = models.FloatField()
    
    def __str__(self):
        return "Timestamp: " +str(self.timestamp) + " Type:" + str(self.datatype.typeName) + " Value:" + str(self.value) +  str(self.datatype.unit.abbreviatedName)