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
    msg = ''
    num = 0
    database = DB(os.environ['TODO_DB'])
    matched = database.search('title', text)
    if matched == []:
        msg = '一致するassigmentは存在しません'
    else:
        for data in matched:
            num += 1
            msg += f'\n{data["title"]}, 期限:{data["limit_at"]}, status:{data["status"]}, id:{data["id"]}'
        msg = f'一致するassignmentは以下の{num}件です。' + msg
    message.reply(msg)

@respond_to(r'\s*todo\s+change\s+(\S+)\s+(\S+)\s+(\S+)$')
def todo_change_id(message, id, column, value):
    database = DB(os.environ['TODO_DB'])
    status_code = database.change_id(id, column, value)
    msg = ''
    if status_code == 0:
        msg = 'カラムが不正です'
    elif status_code == 1:
        msg = 'idが不正です'
    elif status_code == 2:
        msg = 'sqlite文が実行できません'
    elif status_code == 3:
        msg = '値を変更しました'
    message.reply(msg)