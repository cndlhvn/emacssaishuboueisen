# -*- encoding:utf-8 -*-
import base64
SHELL_ESCAPE= " '\";`|"

def get_install_command():
	if command_check("apt-get"):
		tmp_command='apt-get install '
	elif command_check("yum"):
		tmp_command='yum install '
	elif command_check("brew"):
		tmp_command='brew install '
	return tmp_command

def shell_safe(path):
	return "".join([("\\" + _) if _ in SHELL_ESCAPE else _ for _ in path])

def file_appendln(location, content,tab=0):
	tabstring=""
	for i in range(tab):
		tabstring +="\t"
	run('echo "%s" | openssl base64 -A -d >> %s' % (base64.b64encode(tabstring+content+"\n"), shell_safe(location)))

