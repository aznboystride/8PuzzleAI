import copy, sys

class queue:

	def __init__(self, items=[]):
		self.items = items

	def empty(self):
		while not self.isEmpty():
			self.pop()

	def isEmpty(self):
		if len(self.items) == 0:
			return True
		else:
			return False

	def push(self, item):
		self.items.append(item)

	def top(self):
		if not self.isEmpty():
			return self.items[0]
		else:
			print('Queue is Empty!')

	def display(self):
		self.temp = copy.copy(self.items)
		if self.isEmpty():
			print('Queue is empty!')
		else:
			while not self.isEmpty():
				print(self.top())
				self.pop()
			print()
		self.items = copy.copy(self.temp)

	def pop(self):
		if self.isEmpty():
			print('Queue is empty!')
		else:
			del self.items[0]

	def size(self):
		if self.isEmpty():
			print('Queue is empty!')
		else:
			return len(self.items)

	def value(self):
		return self.items



class stack:

	def __init__(self, items=[]):
		self.items = items

	def isEmpty(self):
		if len(self.items) == 0:
			return True
		else:
			return False

	def push(self, item):
		self.items.append(item)

	def top(self):
		if self.size() == 0:
			print('Stack is empty')
		else:
			return self.items[-1]

	def display(self):
		self.temp = copy.copy(self.items)
		if self.isEmpty():
			print('Stack is empty!')
		else:
			while not self.isEmpty():
				print(self.top())
				self.pop()
			print()
		self.items = copy.copy(self.temp)

	def pop(self):
		if self.isEmpty():
			print('Stack is empty!')
		else:
			deleted = self.items[-1]
			del self.items[-1]
			return deleted

	def size(self):
		return len(self.items)

	def fringe(self):
		return self.items

queues = queue()
stacks = stack()
