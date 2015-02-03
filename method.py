# -*- encoding:utf-8 -*-
import base64
SHELL_ESCAPE= " '\";`|"

def check_os():
	if command_check("apt-get"):
		return 'ubuntu'
	elif command_check("yum"):
		return 'centos'
	elif command_check("brew"):
		return 'mac'
def get_login_user_name():
  return run("whoami")

def shell_safe(path):
	return "".join([("\\" + _) if _ in SHELL_ESCAPE else _ for _ in path])

def file_appendln(location, content,tab=0):
	tabstring=""
	for i in range(tab):
		tabstring +="\t"
	run('echo "%s" | openssl base64 -A -d >> %s' % (base64.b64encode(tabstring+content+"\n"), shell_safe(location)))

