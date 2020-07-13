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
            {"title": title, "limit_at": limit_at, "status": status})
        msg = "以下の内容で追加しました。\ntitle:" + title + \
            "\nlimit:" + limit_at + "\nstatus:" + status
    else:
        if now > datetime.datetime.strftime(limit_at_fin, '%Y/%m/%d %H:%M'):
            status = '期限切れ'
            database.add_dict(
                {"title": title, "limit_at": limit_at_fin, "status": status})
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
