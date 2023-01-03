from django.db import models

# Create your models here.
# Create your models here.
class Posting(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images')
    date = models.DateTimeField()

    def _str_(self):
        return self.judul