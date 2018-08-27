import re
from kakaobot import log_append
from googletrans import Translator

lang_list = {
	'한글' : 'ko',
	'한국어' : 'ko',
	'영어' : 'en',
	'일어' : 'ja',
	'일본어' : 'ja',
	'중국어' : 'zh-CN',
	'대만어' : 'zh-TW'
}

def quadra_trans(target, user):
	translator = Translator()

	lang_dest = "ko"

	if target[0] in lang_list.keys():
		lang_dest = lang_list[target[0]]
	elif target[0]:
		lang_dest = target[0]
	try:
		asw = translator.translate(target[1],dest = lang_dest)
		text = asw.src+" -> "+asw.dest+"\n"+asw.text
		if len(text) > 900 :
			log_append(user, "Too long to send : "+asw.text, "trans",0)
			return "너무 긴 말은 번역하기 힘들어!"
		log_append(user, "Success! : "+asw.text, "trans",0)
		return text
	except Exception as ex:
		if ex == ValueError:
			log_append(user, "Cannot understand dest language.", "trans",0)
			return "어느 언어로 번역할지 제대로 이해못했어!"
		else:
			log_append(user, "Unknown Error : "+str(ex), "trans",0)
			return "미안해! 번역이 잘 안돼.."