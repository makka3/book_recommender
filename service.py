class ToDoService:
	def __init__(self):
		self.model = model

	def create(self, params):
		self.model.create(params["text"], params["Description"])

	def update(self, params):
		self.model.update(params["id"],params["text"],params["description"])

	def delete(self, params):
		self.model.delete(params["id"])

	def select_by_id(self, params):
		self.model.select_by_id(params["id"])

	def select_all_by_user(self, params):
		self.model.select_all_by_user(params["userid"])