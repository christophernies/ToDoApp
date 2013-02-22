from piston.handler import BaseHandler
from todo_app.models import ClickData

class DataHandler(BaseHandler):
	allowed_methods = ('GET',)
	model = ClickData   

	def read(self, request, click_id=None):
		"""
		Returns a single post if `blogpost_id` is given,
		otherwise a subset.
		"""
		base = ClickData.objects
		if click_id:
			return base.get(pk=click_id)
		else:
			return base.all() # Or base.filter(...)