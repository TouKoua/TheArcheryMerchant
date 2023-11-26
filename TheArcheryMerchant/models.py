import django.db.models as models

class Bow(models.Model):
    types = (("LongBow", "LongBow"), ("CompoundBow", "CompoundBow"), ("RecurveBow", "RecurveBow"))
    name = models.CharField(max_length=100)
    bowtype = models.CharField(max_length=100, choices=types)
    drawLength = models.IntegerField(default=0)
    drawStrength = models.IntegerField(default=0)

class Arrows(models.Model):
    arrowLength = models.IntegerField(default=0)
    spinage = models.IntegerField(default=0)