from django.db import models


class SilverManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(metal_name='silver')


class GoldManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(metal_name='gold')


class Metal(models.Model):

    metal_name = models.CharField(max_length=10)
    datetime = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    gold = GoldManager()
    silver = SilverManager()

    def __str__(self):
        return "{}: {}".format(
            self.metal_name, self.datetime.strftime("%Y-%m-%d")
        )


class Rate(models.Model):

    metal_rate = models.DecimalField(max_digits=10, decimal_places=4)
    currency = models.CharField(max_length=3)
    metal_code = models.CharField(max_length=3, blank=True)
    unit = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now=True)
    metal = models.ForeignKey(Metal, on_delete=models.CASCADE,
                              related_name='rates')
    source = models.CharField(max_length=25, blank=True, null=True)

    def total_silver_rates(self):
        return Rate.objects.filter(metal_code="AG").count()

    def total_gold_rates(self):
        return Rate.objects.filter(metal_code="AU").count()

    def __str__(self):
        return "{}: {}".format(
            "rate", self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        )
