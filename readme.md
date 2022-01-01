# nasfinder

## What's this

所定のディレクトリでファイル名による検索を行い、UNCパスに変換して表示するアプリケーション。
Samba などで公開している共有フォルダのファイル検索を行う用途を想定。

## Features

サーバ内の検索対象ディレクトリを設定ファイルで指定できる。
検索対象ディレクトリごとに対となるUNCパスを指定できる。その通りに変換して出力する。（例： `/export/` を `\\172.0.0.1\` に変換）

# How to Use

## とりあえず動かす

### Docker Desktop (Flask) - For Testing
1. VS Code このフォルダをコンテナ内で開く。
2. ターミナルで `python3 main.py` を実行する。
3. 127.0.0.1:5000 にアクセスする。

### Docker Desktop (uWSGI) - For Testing
1. VS Code でこのフォルダをコンテナ内で開く。
2. ターミナルで、`uwsgi --wsgi-file=main.py --callable=app --http=0.0.0.0:8080` を実行する。
3. 127.0.0.1:8080 にアクセスする。

### uWSGI - For Production
1. このフォルダを適当な場所に配置する。
2. requirements.txt の内容をインストールする。必要に応じてvirtualenvを作成する。
3. `uwsgi.ini` を確認し、`chdir`, `virtualenv` の値を実態に即して修正する。
4. その他必要に応じて追記などを行う

## config.ini の編集
サンプルに従って、localpath と smbpath を列記する。列記したら再起動する。


## ローカルの準備

ブラウザ(Chrome/Edge)に、Enable Local File Open プラグインをインストールする。
https://chrome.google.com/webstore/detail/enable-local-file-links/nikfmfgobenbhmocjaaboihbeocackld

プラグインインストール・node.jsランタイムインストール・レジストリ登録が必要。


# 参考文献
Flask + uwsgi
* [uWSGI入門 | Python学習講座](https://www.python.ambitious-engineer.com/archives/1959)
* [【Python】Flaskの本番環境構築（Flask + uWSGI + Nginx） - 7839](https://serip39.hatenablog.com/entry/2020/07/06/070000)
