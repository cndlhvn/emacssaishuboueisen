# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def haml_install():
  """[1]hamlのインストール"""
  with cd(EMACS_CONF):
    if not contains("elpa-component.el",";;;haml-mode"):
      register_library_to_elpa("haml-mode")
      run("emacs --batch --script elpa-component.el")

  if not contains(EMACS_FILE,";;;haml-mode"):
    haml_mode="""
;;;haml-mode
(when (require 'haml-mode nil t)
(add-hook 'haml-mode-hook
          (lambda ()
            (setq tab-width 2)
            (indent-tabs-mode nil)
            (setq c-basic-offset 8)
            (setq haml-indent-offset 2))))"""
    file_appendln(EMACS_FILE,haml_mode)
    
