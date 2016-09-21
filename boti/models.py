from django.db import models

class Pizza(models.Model):
	nev = models.CharField(max_length=30)
	kep = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/pizza.jpg')
	def __str__(self):
		return self.nev