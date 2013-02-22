# Create your models here.
from django.db import models

class ClickData(models.Model):
	click_time = models.TextField()
	click_date = models.TextField()
	click_url = models.TextField()
	
	# def save(self, *args, **kwargs):
	# 	super(ClickData, self).save(*args, **kwargs)
	# 	record = ClickData()
	# 	record.id = click_id
	# 	record.time = click_time
	# 	record.date = click_date
	# 	record.url = click_url
	# 	record.save()