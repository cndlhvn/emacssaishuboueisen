#サーバのIPアドレス。
#ローカルでやる場合はプライベートIPアドレス
env.hosts = ['xxx.xxx.xxx.xxx']
env.user = "your_pc_name"

#パスワード認証の場合はそのPCのパスワードを
env.password ="your_pc_password"
#公開鍵認証の場合は秘密鍵のパス
#env.key_filename = '/path/to/secretkeyfile.pem'

#サーバのIPアドレス。
#グローバルでやる場合はグローバルIPアドレス
#ローカルでやる場合はプライベートIPアドレス
env.hosts = ['192.168.1.1']
env.user = "candle"

#パスワード認証の場合はそのPCのパスワードを
env.password ="hogehoge"

#公開鍵認証の場合は秘密鍵のパス
#env.key_filename = '~/.ssh/hoge.pem'

#vagrant環境でやる場合は下をコメントイン
#env.key_filename = '~/.vagrant.d/insecure_private_key'
#env.port=2222
#env.hosts = ['127.0.0.1']
#env.user = "vagrant"


#myqlのアクセス
env.mysql_user = "root"
env.mysql_password = ""
env.mysql_host = "localhost"



