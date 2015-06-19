# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def multi_term_install():
  """[1]multi-termのインストール"""
  with cd(EMACS_CONF):
    if not contains("elpa-component.el",";;;multi-term"):
      register_library_to_elpa("multi-term")
      run("emacs --batch --script elpa-component.el")

  if not contains(EMACS_FILE,";;;multi-term"):
    multi_term="""
;;;multi-term
(when (require 'multi-term nil t)
  (setq multi-term-program "/bin/bash"))"""
    file_appendln(EMACS_FILE,multi_term)
