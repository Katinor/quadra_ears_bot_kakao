#!flask/bin/python
# -*- coding: utf-8 -*-

import random, json, re
from functools import wraps
from kakaobot import *


from quadra_version import version, tou
from quadra_neko import neko_search
from quadra_trans_module import quadra_trans

app = Client(port = 7600)

@app.add_command()
def 안녕(user_key):
	return Message(text = "반가워!")

@app.add_command(["사잽아 네코"])
def neko_comm(user_key):
	return neko_search(user_key)

@app.add_command(["통상모드로 전환"])
def default_command(user_key):
	return Message(text = "처음으로 돌아왔어!")

@app.add_prefix_command(["도움말"], True)
def help_depth(user_key, content):
	return version(flag = content)

@app.add_prefix_command(["이용약관"], True)
def check_tou_depth(user_key, content):
	return tou(flag = content)

@app.add_regex_command("^사잽아 (?:((?:(?!로).)*)로 )?((?:(?! 번역해줘).)*) 번역해줘")
def trans_comm(user_key, target_group):
	return Message(text = quadra_trans(target_group, user_key))

app.run()