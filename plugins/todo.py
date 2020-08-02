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



@respond_to(r'\s*todo\s+add\s+(\S+)\s+(\S+)$')
def todo_add(message, title, limit_at):
    data={"title": title,"limit_at": limit_at}
    msg=todo_add_sub(message,data)
    message.reply(msg)

@respond_to(r'\s*todo\s+add\s+(\S+)$')
def todo_add_unlimit(message, title):
    data={"title": title}
    msg=todo_add_sub(message,data)
    message.reply(msg)


@respond_to(r'\s*todo\s+announce\s+(\S+)\s+(\S+)\s+(\S+)$')
def todo_announce(message, title, limit_at, note):
    data= {"title": title, "limit_at": limit_at, "note": note}
    msg=todo_add_sub(message,data,announce=True)
    message.reply(msg)


#titleとlimitに加えてstatusも登録できるようにする
@respond_to(r'\s*todo\s+add\s+(\S+)\s+(\S+)\s+(\S+)$')
def todo_add_status(message, title, limit_at, status):
    database = DB(os.environ['TODO_DB'])
    database.add_dict({"title": title, "limit_at": limit_at, "status": status})

@respond_to(r'\s*todo\s+finish\s+(.*)')
def todo_finish(message, ids):
    msg = ''
    msg1 = '\nid： '
    msg2 = '\nid： '
    msg3 = '\nid： '
    success = False
    failed = False
    others = False
    id = ids.split()
    database = DB(os.environ['TODO_DB'])
    for i in id:
        strip = i.find('|')
        if strip > 0:
            i = i[strip+1:]
        i = i.replace('>','')
        data = database.select_id(i)
        if data["user"] == None:
            msg2 += '`' + i + '` ' 
            failed = True
            continue
        elif tools.getmsginfo(message)['user_id'] != data["user"]:
            msg3 += '`' + i + '` '
            others = True
            continue
        status_code = database.change_id(i, 'status', '済')
        if status_code == 200:
            msg1 += '`' + i + '` '
            success = True
    if success and failed and others:
        msg = msg1 + 'を完了しました。お疲れ様でした。' + msg2 + 'は存在しません。' + msg3 + 'は他人のタスクです。'
    elif success and failed:
        msg = msg1 + 'を完了しました。お疲れ様でした。' + msg2 + 'は存在しません。'
    elif failed and others:
        msg = msg2 + 'は存在しません。' + msg3 + 'は他人のタスクです。'
    elif success:
        msg = msg1 + 'を完了しました。お疲れ様でした。'
    elif failed:
        msg = msg2 + 'は存在しません。'
    elif others:
        msg = msg3 + 'は他人のタスクです。'
    else:
        msg = 'このコマンドは実行できません。'
    message.reply(msg)

# 実用性の観点からから未のものだけ表示する
@respond_to(r'\s*todo\s+list$')
def todo_list(message):
    database = DB(os.environ['TODO_DB'])
    userId = tools.getmsginfo(message)['user_id']
    data = database.dict_list_sorted(show_over_deadline=3, user_id=userId)
    num = 0
    str_list = ''
    for r in data:
        num += 1
        if r["importance"] == '大':
            #もう少しわかりやすく区別したい
            if r["subject"] == 'None':
                str_list += f' _`{r["id"]}`_ _*{r["title"]}*_   期限：{r["limit_at"][5:]}   status：{r["status"]} \n'
            else:
                str_list += f' _`{r["id"]}`_ _{r["subject"]}_ _*{r["title"]}*_   期限：{r["limit_at"][5:]}   status：{r["status"]} \n'
        else:
            if r["subject"] == 'None':
                str_list += f' `{r["id"]}` *{r["title"]}*   期限：{r["limit_at"][5:]}   status：{r["status"]} \n'
            else:
                str_list += f' `{r["id"]}` {r["subject"]} *{r["title"]}*   期限：{r["limit_at"][5:]}   status：{r["status"]} \n'
    if str_list == '':
        str_list = '現在のリストにはタスクが存在しません。'
    else:
        str_list = f'現在のタスクは以下の{num}件です。\n' + str_list
    message.reply(str_list)

@respond_to(r'\s*todo\s+list\s+all$')
def todo_list_all(message):
    database = DB(os.environ['TODO_DB'])
    message.reply(database.list())

@respond_to(r'\s*todo\s+reset$')
def todo_reset(message):
    database = DB(os.environ['TODO_DB'])
    database.reset()
    message.reply('データベースを初期化しました')

@respond_to(r'\s*todo\s+search\s+(\S+)$')
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
        