# emacssaishubouseisen

このプロジェクトは主にmac ubuntu centOS向けて、fabricコマンドを打つだけで、自動的にemacsの環境を作ります。
自動的に構築するemacsの項目は以下のものです。

- インストール
- emacs設定ファイルの初期設定
- ライブラリのインストール
- ライブラリの設定の書き込み

## 実行環境条件

1. python2.7以上
	 私は2.7で動かしているのでそれ以上のバージョンでどう動くかは検証していない。


2. fabricとcuisineを使用しする
	 easy_installかpipでfabricとcuisineをインストールしておく。	 


##使い方


ダウンロードしたzipファイルを解凍します。

example-config.pyをconfig.pyに名前を変更します。

ssh接続を設定する。

sshの認証がパスワードの場合はパスワードの項目をコメントインしてパスワードを記入します。
sshの認証が公開鍵の場合は鍵の項目をコメントインして、秘密鍵のパスを記入します。



