from django.db import models

# Create your models here.




class Drug(models.Model):
    sample_text = models.CharField(max_length=1024, blank=True, null=True, verbose_name="Nazwa leku")
    sample_bool = models.BooleanField(blank=True, null=True, default=False, verbose_name="Czy lek jest ważny?")

