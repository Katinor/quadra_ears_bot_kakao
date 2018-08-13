#!flask/bin/python
# -*- coding: utf-8 -*-

import random
from functools import wraps
import json
from flask import Flask, jsonify, render_template, request, abort, redirect, url_for
from quadra_version import version, tou
from quadra_json import kakao_msg
from quadra_neko import neko_search

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

@app.route("/message", methods = ['POST'])
def return_func():
	target_json = {}
	msg_content = request.get_json() # user_key, type, content
	if msg_content["content"].startswith("도움말"):
		target_json = version(msg_content["content"])
	elif msg_content["content"].startswith("이용약관"):
		target_json = tou(msg_content["content"])
	elif msg_content["content"].startswith("사잽아"):
		if msg_content["content"] == "사잽아 네코":
			target_json = neko_search()
		else : target_json["message"] = {
			"text" : "무슨 말인지 모르겟어! 도움이 필요하면 \"도움말\"이라고 해줘!"
		}
	elif msg_content["content"] == "통상모드로 전환":
		target_json = kakao_msg(text = "돌아왔어! 이제 평상시처럼 말하면 돼!").make_dict()
	else :
		target_json["message"] = {
			"text" : "무슨 말인지 모르겠어! 도움이 필요하면 \"도움말\"이라고 해줘!"
		}

	return jsonify(target_json)


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=7600,debug=True)