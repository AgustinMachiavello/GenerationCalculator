from django.db import models

# Create your models here.


class Generations(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    from_year = models.IntegerField()
    to_year = models.IntegerField()

    def __str__(self):
        return "{0} {1} from {2} to {3}".format(self.name, self.description, self.from_year, self.to_year)
