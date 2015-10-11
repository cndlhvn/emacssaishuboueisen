# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def multi_term_install():
  """[1]multi-termのインストール"""
  if not contains(EMACS_FILE,";;;multi-term"):
    multi_term="""
;;;multi-term
(el-get-bundle multi-term)
(when (require 'multi-term nil t)
  (setq multi-term-program "/bin/bash"))"""
    file_appendln(EMACS_FILE,multi_term)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")
