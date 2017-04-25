from django.db import models
from django.urls import reverse

from users.models import Member

class Table(models.Model):
	name = models.CharField(max_length=64)
	#owner = models.ForeignKey(Member)
	# let's do all this in JSON because fuck it
	""" STRUCTURE OF A FIELD:
	{'from': number/string, 'to': number/string, 'name': string}
	"""
	fields = models.CharField(max_length=2048, default="[]")
	def get_absolute_url(self):
		return reverse('table_detail', kwargs={'pk': self.id})
