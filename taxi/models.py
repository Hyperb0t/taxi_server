from django.db import models


class TaxiGroup(models.Model):
    leave_time = models.DateTimeField('leave time')
    from_place = models.CharField(max_length=30)
    to_place = models.CharField(max_length=30)
    def __str__(self):
        return self.taxiplaceholder_set

class TaxiPlaceholder(models.Model):
    sitting_places_amount = models.PositiveSmallIntegerField
    vk_id = models.CharField(max_length=10)
    group = models.ForeignKey(TaxiGroup, on_delete=models.CASCADE)
    def __str__(self):
        return self.sitting_places_amount + ' place ' + self.vk_id + ' in group'
