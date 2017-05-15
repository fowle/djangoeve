from django.db import models

class InvGroup(models.Model):
	group_id = models.IntegerField()
	name_ru = models.CharField(max_length=200)
	name_en = models.CharField(max_length=200)
	
	def __str__(self):
		return str(self.group_id)+":"+self.name_ru