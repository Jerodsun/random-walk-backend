from django.db import models
# from django.db.models import Q

# Create your models here.

# Models are database mappings
# https://docs.djangoproject.com/en/2.2/topics/db/models/

class SampleData(models.Model):
    """This is a sample model for the random walk implementation.
    Fields: timestamp, direction, useragent."""
    created = models.DateTimeField(auto_now_add=True)
    direction = models.IntegerField()
    ip_address = models.CharField(max_length = 15)

    # Think about how to expand this concept to per user.

    class Meta:
        ordering = ['created']
        db_table = 'Sample_Data'
        indexes = [
            models.Index(fields=['created'], name='created_idx')
        ]
        verbose_name_plural = "Sample Data Model" # This shows up in django admin


# sample POST
# curl -d '{"direction":"-1"}'  -X POST 127.0.0.1:8000/api/randomwalk/

class BlackScholes(models.Model):
    """This is a sample model to store the POST request for a Black Scholes Merton
    calculation. """
    # Use FE for validation.
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    strike = models.FloatField() # DecimalField returns string repr for serializer
    interest_rate = models.FloatField() # This needs to be divided by 100 from FE
    volatility = models.FloatField()
    time_to_exp = models.IntegerField()

    class Meta:
        verbose_name_plural = "Black Scholes Model"


class BrownianMotion(models.Model):
    """ This is a model to warehouse when a random implementation is requested to be generated.
    Demonstrated with Brownian Motion and Random Walk. """

    GENERATOR_CHOICES = (
        ('BM', 'Brownian Motion'),
        ('RW', 'Random Walk'),
    )
    created = models.FloatField() # Datetime should come from inside Python function
    # type = models.CharField(max_length=1, choices=GENERATOR_CHOICES)
    # volatility = sigma, variance = mu, start = x0
    volatility = models.FloatField()
    variance = models.FloatField()
    start = models.FloatField()
    count = models.IntegerField()
    

    # As Brownian Motion is going into one class, there is no need for constraints
    # class Meta:
    #     # enforce model constraints
    #     constraints = [
    #         models.CheckConstraint(
    #             check=(
    #                 Q(volatility__isnull=False) &
    #                 Q(variance__isnull=False) &
    #                 Q(start__isnull=False) &
    #                 Q(count__isnull=False)                
    #             ) | (
    #                 Q(volatility__isnull=True) &
    #                 Q(variance__isnull=True) &
    #                 Q(start__isnull=True) &
    #                 Q(count__isnull=True) 
    #             ),
    #             name="all_or_none_parameters"
    #         )
    #     ]