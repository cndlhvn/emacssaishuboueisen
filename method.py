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

def get_tab_char():
  os_name=check_os()
  if(os_name =='mac'):
    return "\\\t"
  else:
    return "\\t"

def get_newline_char():
  os_name=check_os()
  if(os_name =='mac'):
    return "\\\n"
  else:
    return "\\n"
  
def register_library_to_elpa(library_name):
  library_symbol=";;;"+library_name
  newline_char=get_newline_char()
  tab=get_tab_char()
  sed("elpa-component.el",';;add-elpa-package',';;add-elpa-package'+newline_char+tab+tab+library_name+library_symbol, limit='')

def register_elisp_to_elpa(library_name,url):
  library_symbol=";;;"+library_name
  url='"'+url+'"'
  newline_char=get_newline_char()
  tab=get_tab_char()
  sed("elpa-component.el",';;add-elisp-url',';;add-elisp-url'+newline_char+tab+tab+url+library_symbol, limit='')

def shell_safe(path):
  return "".join([("\\" + _) if _ in SHELL_ESCAPE else _ for _ in path])

def file_appendln(location, content,tab=0):
  tabstring=""
  for i in range(tab):
    tabstring +="\t"
  run('echo "%s" | openssl base64 -A -d >> %s' % (base64.b64encode(tabstring+content+"\n"), shell_safe(location)))

def gitcheckdiff():
  repo.git.add(".")
  diff_content = repo.head.commit.diff(None)
  if len(diff_content) > 0:
    repo.git.reset(".")
    return True
  else:
    return False

def gitcommit(message):
  repo.git.add(".")
  repo.git.commit( m=message)

def gitcommitcheck():
  t = repo.head.commit.tree
  print(repo.git.diff(t))
  msg = 'gitのコミット行ってよろしいでしょうか'
  if not confirm(msg):
    abort('中止しました。')
  else:
    return True
