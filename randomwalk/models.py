from django.db import models

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


# sample POST
# curl -d '{"direction":"-1"}'  -X POST 127.0.0.1:8000/api/randomwalk/
