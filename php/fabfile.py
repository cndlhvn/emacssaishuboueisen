# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def php_install():
  """[1]php-modeのインストール"""
  if not contains(EMACS_FILE,";;;php-mode"):
    php_mode="""
;;;php-mode
(el-get-bundle php-mode)"""
    file_appendln(EMACS_FILE,php_mode)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")
    
