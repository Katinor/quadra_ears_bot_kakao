class kakao_msg():
	text = None
	photo = {}
	message_button = {}
	keyboard = {}
	buttons = []

	def __init__(self, text = None):
		if text: self.text = text
		else: self.text = None
		self.photo = {}
		self.message_button = {}
		self.keyboard = {"type" : "text"}
		self.buttons = []

	def set_text(self, text):
		self.text = text

	def set_photo(self, url, width = 720, height = 630):
		self.photo["url"] = url
		self.photo["width"] = width
		self.photo["height"] = height

	def add_button(self, label, url):
		self.message_button["label"] = label
		self.message_button["url"] = url
	
	def add_keyboard(self, buttons):
		self.keyboard["type"] = "buttons"
		self.buttons.append(buttons)

	def make_dict(self):
		target = {
			"message":{
			}
		}
		if self.text: target["message"]["text"] = self.text
		if self.photo: target["message"]["photo"] = self.photo
		if self.message_button: target["message"]["message_button"] = self.message_button
		if self.keyboard["type"] == "text" : target["keyboard"] = { "type" : "text" }
		else:
			target["keyboard"] = { "type" : "buttons", "buttons" : self.buttons }
		return target