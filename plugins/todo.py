from slackbot.bot import respond_to
from tododb import DB
from . import tools
import os
import datetime

@respond_to(r'\s*todo\s+delete_secret\s+(\d+)$')
def todo_delete_secret(message, id):
    db = DB(os.environ['TODO_DB'])
    userid = tools.getmsginfo(message)["user_id"]
    result = db.delete_id(id, userid,secret=True)
    if result==200:
        msg = f"id{id}番を削除しました。また、id{id}番データ内容は初期化されました。"
    elif result==401:
        msg = f"idが不正です。"
    elif result==402:
        msg = f"sql文が上手く実行できませんでした。"
    elif result==-1:
        msg = f"他のユーザーのものは変更できません。"
    else:
        msg = "うまくいきませんでした。"
    message.reply(msg)


@respond_to(r'\s*todo\s+delete\s+(\d+)$')
def todo_delete(message, id):
    db = DB(os.environ['TODO_DB'])
    userid = tools.getmsginfo(message)["user_id"]
    result = db.delete_id(id, userid)
    if result==200:
        msg = f"id{id}番を削除しました。"
    elif result==401:
        msg = f"idが不正です。"
    elif result==402:
        msg = f"sql文が上手く実行できませんでした。"
    elif result==-1:
        msg = f"他のユーザーのものは変更できません。"
    else:
        msg = "うまくいきませんでした。"
    message.reply(msg)


@respond_to(r'\s*todo\s+cancel\s+announcement\s+(\d+)$')
def todo_cancel_announcement(message, id):
    db = DB(os.environ['TODO_DB'])
    result = db.delete_id(id, "all")
    if result==200:
        msg = f"id{id}番のannouncementを削除しました。"
    elif result==401:
        msg = f"idが不正です。"
    elif result==402:
        msg = f"sql文が上手く実行できませんでした。"
    elif result==-1:
        msg = f"指定されたidのデータはannouncementではありません。"
    else:
        msg = "うまくいきませんでした。"
    message.reply(msg)



@respond_to(r'\s+todo\s+add\s+(\S+)\s+(\S+)$')
def todo_add(message, title, limit_at):
    data={"title": title,"limit_at": limit_at}
    msg=todo_add_sub(message,data)
    message.reply(msg)

@respond_to(r'\s+todo\s+add\s+(\S+)$')
def todo_add_unlimit(message, title):
    data={"title": title}
    msg=todo_add_sub(message,data)
    message.reply(msg)


@respond_to(r'todo\s+announce\s+(\S+)\s+(\S+)\s+(\S+)$')
def todo_announce(message, title, limit_at, note):
    data= {"title": title, "limit_at": limit_at, "note": note}
    msg=todo_add_sub(message,data,announce=True)
    message.reply(msg)


#titleとlimitに加えてstatusも登録できるようにする
@respond_to(r'\s+todo\s+add\s+(\S+)\s+(\S+)\s+(\S+)$')
def todo_add_status(message, title, limit_at, status):
    data={"title": title,"limit_at": limit_at, "status": status}
    msg=todo_add_sub(message,data)
    message.reply(msg)

#status未のものを済にする
@respond_to(r'\s+todo\s+finish\s+(\S+)$')
def todo_finish(message, id):
    database = DB(os.environ['TODO_DB'])
    database.change_id(id, 'status', '済')
    message.reply("お疲れさまでした")

#exampleを表示する
@respond_to(r'\s+todo\s+example$')
def todo_example(message):
    message.reply("\n<タスクの登録> todo add タスク名\n<タスクの一覧表示(userのみ)> todo list\n<タスクの一覧表示> todo list all\n<タスクの消去> todo delete id\n<登録したタスクのリセット> todo reset\n<タスクの検索> todo research タスク名に含まれる文字\n<status未→済> todo finish id")

@respond_to(r'\s+todo\s+list$')
def todo_list(message):
    database = DB(os.environ['TODO_DB'])
    userId = tools.getmsginfo(message)['user_id']
    data = database.search('user', userId, mode=1)
    str_list = 'TODO list:\n'
    for r in data:
        str_list += ', '.join(map(str, r.values()))
        str_list += '\n'
    message.reply(str_list)

@respond_to(r'\s+todo\s+list\s+all$')
def todo_list_all(message):
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
    if status_code == 400:
        msg = 'カラムが不正です'
    elif status_code == 401:
        msg = 'idが不正です'
    elif status_code == 402:
        msg = 'sqlite文が実行できません'
    elif status_code == 403:
        msg = 'limit_atを正しく入力してください'
    elif status_code == 404:
        msg = 'idまたはupdate_atを変更することはできません'
    elif status_code == 200:
        msg = '値を変更しました'
    message.reply(msg)

def todo_add_sub(message,data:dict,announce=False) -> str:
    """データ登録の際はこのtodo_add_subにmessageとデータのディクショナリを与えてください。

    戻り値は、登録内容をお知らせする文字列となっています。
    """
    # ユーザー情報取得
    if announce:
        data["user"]="all"
    else:
        info=tools.getmsginfo(message)
        data["user"]=info["user_id"]
    database = DB(os.environ['TODO_DB'])
    now = datetime.datetime.now()
    if "limit_at" in data.keys() or not "status" in data.keys():
        if not "limit_at" in data.keys() and not "status" in data.keys():
            data["limit_at"]=None
        limit_at_fin = tools.datetrans(data["limit_at"], now)
        msg="以下の内容で"
        if limit_at_fin != None or data["limit_at"] == None:
            if data["limit_at"] != None:
                limit_at_format = datetime.datetime.strptime(limit_at_fin, '%Y/%m/%d %H:%M')
                if now > limit_at_format:
                    data["status"] = '期限切れ'
                noticetime = tools.noticetimeSet(limit_at_format, now)
                data["noticetime"]=noticetime
                data["limit_at"]=limit_at_fin
            msg += "、期限を正しく設定して"
        else:
            return "limit_atの形が不正です。以下の入力例を参考にしてください。\n202008161918: 2020年8月16日19時18分となります。\n0816: 現在以降で最も早い8月16日23時59分となります。"
        data = database.add_dict(data)
        msg += "追加しました。"
        for item in data.items():
            if item[0]=="user":
                continue
            msg+=f"\n{item[0]}: {item[1]}"
        return msg
    if "status" in data.keys():
        data["noticetime"]=3
        data = database.add_dict(data)
        msg="以下の内容で追加しました。\n"
        for item in data.items():
            if item[0]=="user":
                continue
            msg+=f"\n{item[0]}: {item[1]}"
        return msg
    return "何らかの不具合により追加できません。"
        