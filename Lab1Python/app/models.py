class Date(object):
	num = 0

	def __init__(self, date, description, is_done=False, id=-1):
		if id == -1:
			self.id = Date.num
		else:
			self.id = id
		Date.num = Date.num + 1
		self.date = date
		self.description = description
		self.is_done = is_done
	def as_json(self):
		return {
			"id": self.id,
			"date": self.date,
			"description": self.description,
			"is_done": self.is_done
		}
