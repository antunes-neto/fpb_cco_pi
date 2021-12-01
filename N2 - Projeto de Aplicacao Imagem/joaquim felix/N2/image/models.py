from django.db import models

class Photo(models.Model):
    file = models.ImageField(upload_to='media',null = True, blank = True)
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'

    def __str__(self):
        return str(self.pk)