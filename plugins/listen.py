from slackbot.bot import listen_to
from . import todo
import time, re

# 初めの文字が!ならコマンドと判断
@listen_to(r'^!.*')
def com_set(message):
    text = message.body['text'][1:]

    todo_add_unlimit = re.search(r'^add\s+(\S+)$', text)
    todo_add = re.search(r'^add\s+(\S+)\s+(\S+)$', text)
    todo_delete_secret = re.search(r'^delete_secret\s+(\d+)$', text)
    todo_delete = re.search(r'^delete\s+(\d+)$', text)
    todo_cancel_announcement = re.search(r'^cancel_announcement\s+(\d+)$', text)
    todo_list = re.search(r'^list$', text)
    todo_list_all = re.search(r'^list\s+all$', text)
    todo_list_notdone = re.search(r'^list\s+\-1', text)
    todo_reset = re.search(r'^reset$', text)
    todo_finish = re.search(r'^finish\s+(.*)', text)
    todo_search = re.search(r'^search\s+(\S+)$', text)
    todo_change_id = re.search(r'^change\s+(\S+)\s+(\S+)\s+(\S+)$', text)
    todo_announce = re.search(r'^announce\s+(\S+)\s+(\S+)\s+(\S+)$', text)
    todo_help = re.search(r'^help', text)

    if todo_add_unlimit:
        todo.todo_add_unlimit(message, todo_add_unlimit.group(1))
    elif todo_add:
        todo.todo_add(message, todo_add.group(1), todo_add.group(2))
    elif todo_delete_secret:
        todo.todo_delete_secret(message,todo_delete_secret.group(1))
    elif todo_delete:
        todo.todo_delete(message,todo_delete.group(1))
    elif todo_cancel_announcement:
        todo.todo_cancel_announcement(message,todo_cancel_announcement.group(1))
    elif todo_list:
        todo.todo_list(message)
    elif todo_list_all:
        todo.todo_list_all(message)
    elif todo_list_notdone:
        todo.todo_list_notdone(message)
    elif todo_reset:
        todo.todo_reset(message)
    elif todo_finish:
        todo.todo_finish(message, todo_finish.group(1))
    elif todo_search:
        todo.todo_search(message, todo_search.group(1))
    elif todo_change_id: 
        todo.todo_change_id(message, todo_change_id.group(1), \
            todo_change_id.group(2), todo_change_id.group(3))
    elif todo_announce:
        todo.todo_announce(message, todo_announce.group(1), todo_announce.group(2), todo_announce.group(3))
    elif todo_help:
        todo.todo_help(message)
    else:
        message.reply('このコマンドは無効です')

@listen_to('what')
def listen_what(message):
    message.reply('??')

@listen_to('app')
def listen_help(message):
    message.reply('このアプリはtodo管理アプリです')