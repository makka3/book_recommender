import sqlite3

class Schema:
	def __init__(self):
		self.conn = sqlite3.connect('todo.db')
		self.create_user_table()
		self.create_to_do_table()

	def create_user_table(self):
		query = """
		CREATE TABLE IF NOT EXISTS "USERS" (
			_id INTEGER PRIMARY KEY AUTOINCREMENT,
			Name TEXT NOT NULL,
			Email TEXT,
			CreatedOn Date default CURRENT_DATE
		);
		"""

		self.conn.execute(query)

	def create_to_do_table(self):
		query = """
		CREATE TABLE IF NOT EXISTS "TODO" (
			id INTEGER PRIMARY KEY,
			userid INTEGER FOREIGN KEY,
			Title TEXT,
			Description TEXT,
			CreatedON DATE,
			DueDate DATE,
			_is_done boolean,
			_is_deleted boolean)
		"""

		self.conn.execute(query)

class ToDoModel:
	TABLENAME = "TODO"

	def __init__(self):
		self.conn = sqlite3.connect('todo.db')
		self.conn.row_factory = sqlite3.Row

	def create(self, text, description):
		query = f'INSERT INTO {self.TABLENAME} ' \
				f'(Title, Description) ' \
				f'values ("{text}","{description}")'

		result = self.conn.execute(query)
		return result

	def list_items(self,where_clause=""):
		query = f'SELECT Title, Description, _is_done, '

	def update(self, id, text, description):
		query = f'UPDATE {TABLENAME} ' \
				f'SET Title = {text}, Description = {description}' \
				f'WHERE id = {id} '

		result = self.conn.execute(query)
		return result

	def select_by_id(self, id):
		query = f'SELECT * ' \
				f'FROM {TABLENAME} ' \
				f'WHERE id = {id} '

		result = self.conn.execute(query)
		return result

	def select_all_by_user(self, userid):
		query = f'SELECT * ' \
				f'FROM {TABLENAME} ' \
				f'WHERE userid = {userid} '

		result = self.conn.execute(query)
		return result

	def delete(self, id):
		query = f'UPDATE {self.TABLENAME} ' \
				f'SET _is_deleted = {1}'
				f'WHERE id = {id} '

		result = self.conn.execute(query)
		return result


class User:
	TABLENAME = "User"

	def create(self, name, email):
		query = f'INSERT INTO {self.TABLENAME} ' \
				f'(Name, Email) ' \
				f'values ({name},{email})'

		result = self.conn.execute(query)
		return result