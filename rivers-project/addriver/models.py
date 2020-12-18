from django.db import models

class River(models.Model):
    RiverName = models.CharField(max_length=25, unique=False, null=False)
    RiverLengthKm = models.FloatField(unique=False, null=False)
    RiverLengthMiles = models.FloatField(unique=False, null=False)
    RiverRating = models.CharField(max_length=25, unique=False, null=False)

    def __str__(self):
        obj_str = f'ID: {self.id},' \
                   f'River Name: {self.RiverName},' \
                   f'Length (Km): {self.RiverLengthKm},' \
                   f'Length (M): {self.RiverLengthMiles},' \
                   f'Rating: {self.RiverRating}' \

        return obj_str
