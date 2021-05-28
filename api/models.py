from django.db import models


class Pelanggan(models.Model):
    nama = models.CharField(max_length=300)
    usia = models.CharField(max_length=150, blank=True)
    profesi = models.CharField(max_length=200)
    alamat = models.TextField()

    def __str__(self):
        return self.nama
