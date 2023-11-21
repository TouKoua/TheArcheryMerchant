import django.db.models as models

class Bow(models.Model):
    types = {"LongBow", "CompoundBow"}
    name = models.CharField(max_length=100)
    bowtype = models.TextChoices(object=types)
    drawLength = models.IntegerField(default=0)
    drawStrength = models.IntegerField(default=0)

class Arrows(models.Model):
    arrowLength = models.IntegerField(default=0)
    spinage = models.IntegerField(default=0)