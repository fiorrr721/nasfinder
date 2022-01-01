# nasfinder

## Features

サーバ内のファイルを名前で検索し、検索結果のファイルフルパスを UNC パスに変換して表示するWebアプリケーション。
Samba などで公開している共有フォルダのファイル検索を行う用途を想定。

検索範囲を設定ファイルで指定できる。
検索結果に表示するパスを変換することができる。（例： `/export/` を `\\172.0.0.1\` に変換）

# How to Use

## とりあえず動かす

### Docker Desktop (Flask)
1. VS Code このフォルダをコンテナ内で開く。
2. ターミナルで `python3 main.py` を実行する。
3. 127.0.0.1:5000 にアクセスする。

### Docker Desktop (uWSGI)
1. VS Code でこのフォルダをコンテナ内で開く。
2. ターミナルで、`uwsgi --wsgi-file=main.py --callable=app --http=0.0.0.0:8080` を実行する。
3. 127.0.0.1:8080 にアクセスする。

### Linux Machine
このフォルダを適当な場所に配置し、

## config.ini の編集
サンプルに従って、localpath と smbpath を列記する。列記したら再起動する。


## ローカルの準備

ブラウザ(Chrome/Edge)に、Enable Local File Open プラグインをインストールする。
https://chrome.google.com/webstore/detail/enable-local-file-links/nikfmfgobenbhmocjaaboihbeocackld

プラグインインストール・node.jsランタイムインストール・レジストリ登録が必要。


# 参考文献
Flask + uwsgi
https://serip39.hatenablog.com/entry/2020/07/06/070000

https://www.python.ambitious-engineer.com/archives/1959
