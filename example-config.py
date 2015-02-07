# -*- encoding:utf-8 -*-
from fabric.api import env, settings,local,run,sudo,cd
from fabric.colors import *
from fabric.decorators import task,roles
from fabric.contrib.files import *
from cuisine import mode_sudo, select_package,package_ensure, dir_exists,file_append,file_exists,command_check

#使用するグローバル変数
EMACS_FILE = '~/.emacs.d/init.el'
EMACS_DIR = '~/.emacs.d/'
EMACS_CONF = '~/.emacs.d/conf/'
EMACS_ELISP_DIR='~/.emacs.d/elisp/'

#サーバのIPアドレス。
#グローバルでやる場合はグローバルIPアドレス
#ローカルでやる場合はプライベートIPアドレス
env.hosts = ['xxx.xxx.xxx.xxx']
env.user = "your_pc_name"

#パスワード認証の場合はそのPCのパスワードを
env.password ="your_pc_password"

#公開鍵認証の場合は秘密鍵のパス
#env.key_filename = '/path/to/secretkeyfile.pem'

#vagrant環境でやる場合は下をコメントイン
#env.key_filename = '~/.vagrant.d/insecure_private_key'
#env.port=2222
#env.hosts = ['127.0.0.1']
#env.user = "vagrant"


#myqlのアクセス
env.mysql_user = "root"
env.mysql_password = ""
env.mysql_host = "localhost"



