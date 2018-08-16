#!flask/bin/python
# -*- coding: utf-8 -*-

import random, json, re
from functools import wraps
from flask import Flask, jsonify, render_template, request, abort, redirect, url_for
from quadra_version import version, tou
from quadra_json import kakao_msg
from quadra_neko import neko_search
from quadra_log_module import log_append
from quadra_trans_module import quadra_trans

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello():
	return render_template('index.html')

@app.route("/keyboard")
def main_key():
	target_json = {
		"type" : "text"
	}
	return jsonify(target_json)

def general_command(msg_content, source_json):
	target_json = source_json
	if msg_content["content"] == "사잽아 네코":
		log_append(msg_content["user_key"], msg_content["content"], "neko",0)
		target_json = neko_search(user = msg_content["user_key"])
		return target_json
	re_target = re.search('^사잽아 (?:((?:(?!로).)*)로 )?((?:(?! 번역해줘).)*) 번역해줘',msg_content["content"])
	if re_target:
		log_append(msg_content["user_key"], msg_content["content"], "trans",0)
		target_json = kakao_msg(text = quadra_trans(msg_content["content"],msg_content["user_key"])).make_dict()
		return target_json 
	log_append(msg_content["user_key"], msg_content["content"], "ERR","None")
	target_json["message"] = {
		"text" : "무슨 말인지 모르겟어! 도움이 필요하면 \"도움말\"이라고 해줘!"
	}
	return target_json


@app.route("/message", methods = ['POST'])
def return_func():
	target_json = {}
	msg_content = request.get_json() # user_key, type, content
	if msg_content["content"].startswith("도움말"):
		log_append(msg_content["user_key"], msg_content["content"], "help",0)
		target_json = version(msg_content["content"])
	elif msg_content["content"].startswith("이용약관"):
		log_append(msg_content["user_key"], msg_content["content"], "tou",0)
		target_json = tou(msg_content["content"])
	elif msg_content["content"].startswith("사잽아"):
		target_json = general_command(msg_content, target_json)
	elif msg_content["content"] == "통상모드로 전환":
		log_append(msg_content["user_key"], msg_content["content"], "SYS","trans")
		target_json = kakao_msg(text = "돌아왔어! 이제 평상시처럼 말하면 돼!").make_dict()
	else :
		log_append(msg_content["user_key"], msg_content["content"], "ERR","None")
		target_json["message"] = {
			"text" : "무슨 말인지 모르겠어! 도움이 필요하면 \"도움말\"이라고 해줘!"
		}
	return jsonify(target_json)


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=7600,debug=True)