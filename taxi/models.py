from django.db import models


class TaxiGroup(models.Model):
    leave_time = models.DateTimeField('leave time')
    from_place = models.CharField(max_length=30)
    to_place = models.CharField(max_length=30)
    def __str__(self):
        return self.taxiplaceholder_set.all().__str__() + self.leave_time + self.from_place + self.to_place

class TaxiPlaceholder(models.Model):
    sitting_places_amount = models.PositiveSmallIntegerField(default=1)
    vk_id = models.CharField(max_length=10, primary_key=True)
    group = models.ForeignKey(TaxiGroup, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return str(self.sitting_places_amount) + ' place ' + self.vk_id + ' in group'
