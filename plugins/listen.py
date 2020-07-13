from slackbot.bot import listen_to
from . import todo
import time, re

# 初めの文字が!ならコマンドと判断
@listen_to(r'^!.*')
def com_set(message):
    text = message.body['text'][1:]

    todo_add = re.search(r'^add\s+(\S+)\s+(\S+)$', text)
    todo_list = re.search(r'^list$', text)
    todo_reset = re.search(r'^reset$', text)

    if todo_add:
        todo.todo_add(message, todo_add.group(1), todo_add.group(2))
    elif todo_list:
        todo.todo_list(message)
    elif todo_reset:
        todo.todo_reset(message)
    else:
        message.reply('このコマンドは無効です')

@listen_to('what')
def listen_what(message):
    message.reply('??')