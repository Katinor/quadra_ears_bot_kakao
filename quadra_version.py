from quadra_json import kakao_msg

def version(flag):
	target = kakao_msg()

	if flag == "도움말":
		target.set_text("반가워! 난 사잽이라구 해!\n밑의 리스트들을 누르면 원하는 도움말을 찾을 수 있어!")
		target.add_keyboard("도움말 : 약관")
		target.add_keyboard("도움말 : 일상")
		target.add_keyboard("도움말 : 사용자")
		target.add_keyboard("도움말 : 게임")
		target.add_keyboard("통상모드로 전환")
	elif "약관" in flag:
		target.set_text("사잽이봇을 이용하기위해 지켜야할 것들이 담겨져있어!")
		target.add_keyboard("이용약관")
		target.add_keyboard("통상모드로 전환")
	else:
		target.set_text("아직은 도움말이 준비되지 않았어!")
	return target.make_dict()

def tou(flag):
	target = kakao_msg()
	if flag == "이용약관":
		target.set_text("사잽이봇을 이용하기위해 지켜야할 것들이 담겨져있어!\n꼭 전부 읽어줘~!")
		target.add_keyboard("이용약관 : 개인정보 관리방침")
		target.add_keyboard("이용약관 : 저작권")
		target.add_keyboard("이용약관 : 사용 API")
		target.add_keyboard("이용약관 : 프로그램 라이센스")
		target.add_keyboard("이용약관 : 연락처")
		target.add_keyboard("통상모드로 전환")
	elif flag == "이용약관 : 개인정보 관리방침":
		temp_text = "사잽이봇은 서비스 제공을 위해 작성자의 고유정보와 그 내용을 수집합니다. "
		temp_text+= "단, 작성자의 고유정보는 본 \"사잽이봇 서비스\"를 제공할 수 있도록 (주)카카오 (이하 '카카오톡 측')가 제공하는 무작위의 'key'값이며, "
		temp_text+= "사잽이봇 측에서는 작성자를 특정할 방법이 없으며, 이 정보로 타 서비스를 이용할 수 없습니다.\n\n"
		temp_text+="사잽이봇은 수집되는 정보를 본 용도로만 사용하며, 아래 명시된 용도 외에는 보관 및 사용되지 않습니다.\n"
		temp_text+=" - 반응했을 경우의 디버깅을 위한 로그\n"
		temp_text+=" - 서비스 제공 등을 위한 데이터베이스 구축\n"
		temp_text+="본 봇과 대화를 함으로서 본 약관에 동의한 것으로 간주됩니다. 여기에 반대할 경우 언제든지 서비스 받기를 중단할 수 있으며, "
		temp_text+="이를 위해서는 그저 사용자가 본 봇과의 대화를 그만두는 것으로 충분합니다.\n"
		temp_text+="사잽이봇은 국가의 명령이 있을 경우 그 기록을 수사기관에 제공할 수 있습니다. 그러니 애한테 위법적인것좀 시키지 마세요."
		target.set_text(temp_text)
		target.add_keyboard("이용약관")
		target.add_keyboard("통상모드로 전환")
	elif flag == "이용약관 : 저작권":
		temp_text = "4ears_bot\n - ⓒ2017-2018, Katinor, All Right Reserved.\n"
		temp_text+= "profile portrait\n - ⓒ2017, Muku, All Right Reserved.\n"
		temp_text+= "Katinor who make this bot received the Public Transmission Right of this illustration (that is protected under the Copyright law of Korea)."
		target.set_text(temp_text)
		target.add_keyboard("이용약관")
		target.add_keyboard("통상모드로 전환")
	elif flag == "이용약관 : 사용 API":
		temp_text ="This bot use Flask.\n"
		temp_text+=" - http://flask.pocoo.org/docs/1.0/license/\n"
		temp_text+= "This bot use nekos.life API.\n"
		temp_text+=" - https://discord.services/api/"
		target.set_text(temp_text)
		target.add_keyboard("이용약관")
		target.add_keyboard("통상모드로 전환")
	elif flag == "이용약관 : 프로그램 라이센스" :
		temp_text ="This bot is licensed, not sold. This bot's TOU only gives you some rights to use it.\n"
		temp_text+="Katinor reserves all other rights. This means you cannot reverse engineer, decompile or disassemble this bot, or otherwise attempt to derive the source code for the software except, and solely to extent: permitted by applicable law, despite this limitation\n"
		temp_text+="Despite above, you can use this bot's \"Clean Build\" code repository under the AGPLv3.0\n"
		temp_text+=" - https://github.com/Katinor/quadra_ears_bot_kakao"
		target.set_text(temp_text)
		target.add_keyboard("이용약관")
		target.add_keyboard("통상모드로 전환")
	elif flag == "이용약관 : 연락처" :
		target.add_button(label = "카티노르의 마도서",url="https://blog.4ears.net/")
		target.add_keyboard("이용약관")
		target.add_keyboard("통상모드로 전환")
	else:
		temp_text ="그런 약관은 없어! 되도록 리스트 내에서 골라줘!"
		target.set_text(temp_text)
		target.add_keyboard("이용약관")
		target.add_keyboard("통상모드로 전환")
	return target.make_dict()