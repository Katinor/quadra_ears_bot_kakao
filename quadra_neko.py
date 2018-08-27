import requests, json
from kakaobot import log_append, Message, Photo

def neko_search(user, flag="kemonomimi"):
	log_append(user, "flag name : "+flag, "neko",0)
	r = requests.get("https://nekos.life/api/v2/img/"+flag)
	r = r.text
	data = json.loads(r)
	file = data["url"]
	return Message(text = "원본보기 : "+file, photo = Photo(file))