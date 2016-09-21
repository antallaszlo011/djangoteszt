from django.db import models

class Szemely(models.Model):
	szemely_nev = models.CharField(max_length=50)
	tel_szam = models.CharField(max_length=12)
	reg_dat = models.DateTimeField('date registered')
	def __str__(self):
		return self.szemely_nev