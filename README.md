# slack-todo
ToDo 管理とその他さまざまな反応をする slackbot

## 機能
* plugins/hello.py
  - `@bot hello`: bot 宛の 'hello を含む文字列' に対して「こんにちは」と返す

* plugins/fizzbuzz.py
  - `@bot fizzbuzz {数字}`: bot 宛の 'fizzbuzz {数字}' に対して Fizz Buzz ゲームの反応

* plugins/listen.py
  - チャンネル内で 'what' を含む文字列の発言に対して「??」と返す

