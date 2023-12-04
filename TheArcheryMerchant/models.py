import django.db.models as models

class Bow(models.Model):
    types = (("LongBow", "LongBow"), ("CompoundBow", "CompoundBow"), ("RecurveBow", "RecurveBow"))
    sellers = (("Amazon", "Amazon"), ("Ebay", "Ebay"))
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    bowtype = models.CharField(max_length=100, choices=types)
    drawLength = models.IntegerField(default=0)
    drawStrength = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sellers = models.CharField(max_length=100, choices=sellers)
    
    def __str__(self):
        return self.name

class Arrows(models.Model):
    sellers = (("Amazon", "Amazon"), ("Ebay", "Ebay"))
    name = models.CharField(max_length=100)
    arrowLength = models.IntegerField(default=0)
    spinage = models.IntegerField(default=0)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sellers = models.CharField(max_length=100, choices=sellers)
    
    def __str__(self):
        return self.name