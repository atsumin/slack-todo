from slackbot.bot import respond_to
from tododb import DB
from . import tools
import os
import datetime

@respond_to(r'\s+todo\s+add\s+(\S+)\s+(\S+)$')
def todo_add(message, title, limit_at):
    database = DB(os.environ['TODO_DB'])
    now = datetime.datetime.now()
    limit_at_fin = tools.datetrans(limit_at, now)
    status = '未'
    if limit_at_fin == None:
        database.add_dict(
            {"title": title, "limit_at": limit_at, "status": status, "noticetime":3})
        msg = "以下の内容で追加しました。\ntitle:" + title + \
            "\nlimit:" + limit_at + "\nstatus:" + status
    else:
        limit_at_format = datetime.datetime.strptime(limit_at_fin, '%Y/%m/%d %H:%M')
        if now > limit_at_format:
            status = '期限切れ'
        noticetime = tools.noticetimeSet(limit_at_format, now)
        database.add_dict(
            {"title": title, "limit_at": limit_at_fin, "status": status, "noticetime":noticetime})
        msg = "以下の内容で、期限を正しく設定して追加しました。\ntitle:" + title + \
            "\nlimit:" + limit_at_fin + "\nstatus:" + status
    message.reply(msg)

@respond_to(r'\s+todo\s+add\s+(\S+)$')
def todo_add_unlimit(message, title):
    database = DB(os.environ['TODO_DB'])
    database.add(title, None)

@respond_to(r'\s+todo\s+list$')
def todo_list(message):
    database = DB(os.environ['TODO_DB'])
    message.reply(database.list())

@respond_to(r'\s+todo\s+reset$')
def todo_reset(message):
    database = DB(os.environ['TODO_DB'])
    database.reset()
    message.reply('データベースを初期化しました')

@respond_to(r'\s+todo\s+search\s+(\S+)$')
def todo_search(message, text):
    database = DB(os.environ['TODO_DB'])
    ids = tools.search('title', text, database.dict_list())
    str_list = database.list_design(ids)
    if str_list == '一致したassignment:\n':
        message.reply('そのようなassignmentは存在しません')
    else:
        message.reply(str_list)

@respond_to(r'\s+todo\s+searchnew\s+(\S+)$')
def todo_search_new(message, text):
    msg = ''
    num = 0
    database = DB(os.environ['TODO_DB'])    
    dict_list = database.dict_list()
    matched = tools.search_new('title', text, dict_list)
    if matched == []:
        msg = '一致するassigmentは存在しません'
    else:
        for data in matched:
            num += 1
            msg += f'\n{data["title"]}, 期限:{data["limit_at"]}, status:{data["status"]}, id:{data["id"]}'
        msg = f'一致するassignmentは以下の{num}件です。' + msg
    message.reply(msg)
