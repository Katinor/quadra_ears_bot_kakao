import requests, json
from quadra_json import kakao_msg

def neko_search(flag="kemonomimi"):
	r = requests.get("https://nekos.life/api/v2/img/"+flag)
	r = r.text
	data = json.loads(r)
	file = data["url"]
	target_msg = kakao_msg(text="원본보기 : "+file)
	target_msg.set_photo(file)
	return target_msg.make_dict()