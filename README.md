# slack-todo
ToDo 管理とその他さまざまな反応をする slackbot

## 機能
* plugins/hello.py
  - `@bot hello`: bot 宛の 'hello を含む文字列' に対して「こんにちは」と返す

* plugins/fizzbuzz.py
  - `@bot fizzbuzz {数字}`: bot 宛の 'fizzbuzz {数字}' に対して Fizz Buzz ゲームの反応

* plugins/listen.py
  - チャンネル内で 'what' を含む文字列の発言に対して「??」と返す

* plugins/todo.py
  - `@bot todo add 'タイトル' [締切]`: ToDo 内容を登録する
  - `@bot todo list`: ToDo の一覧を表示する
  - `@bot todo reset`: ToDo の DB をリセットする

## ToDo DBのスキーマ
| id | title |     limit_at     |    update_at     | status |
|----|-------|------------------|------------------|--------|
|  1 | test1 | 2020/04/30 23:59 | 2020/04/01 13:10 |   済   |
|  2 | test2 | 2020/07/30 7:05  | 2020/06/01 17:00 |   未   |

## ToDo DBの操作関数
* `add(title, limit_at)`: title と limit_at (有効期限) を登録
* `add(title)`: title を無期限の有効期限として登録
* `list()`: ToDo DB のデータを一覧した文字列を返す
* `reset()`: ToDo DB の内容を削除し，空のデータベースを作成
* `add_dict()`:列名をkey、データの値をvalueとするdictのデータをToDo DBに登録　#6　に詳細あり
* `dict_list()`ToDo DB の各データをそれぞれdictにして、dictのリストを返す #6　に詳細あり
* `select_id()`指定したidのデータをdictにして返す #6　に詳細あり

## テスト用プログラム
* test_regex.py
  - 正規表現の確認プログラム
  - 正規表現のパターンを入力し，その後，文字列を入力するとパターンにマッチしているかどうかを判定
  - `python test_regex.py`

* test_tododb.py
  - tododb.py のテストプログラム
  - tododb.py で定義した関数をテストするためのプログラム
