from django.db import models

class SEN0322(models.Model):
    id = models.AutoField(primary_key=True)
    o2 = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.o2} {self.time}'

    class Meta:
        verbose_name = 'SEN0322'
        verbose_name_plural = 'SEN0322'
        ordering = ['-time']