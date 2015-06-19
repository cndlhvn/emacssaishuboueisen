# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def coffee_install():
  """[1]coffee-modeのインストール"""
  with cd(EMACS_CONF):
    if not contains("elpa-component.el",";;;coffee-mode"):
      register_library_to_elpa("coffee-mode")
      run("emacs --batch --script elpa-component.el")

  if not contains(EMACS_FILE,";;;coffee-mode"):
    coffee_mode="""
;;;coffee-mode
(when (require 'coffee-mode nil t)
  (defun coffee-custom ()
    ;;インデントモードをオフ
    (setq-default indent-tabs-mode nil)
    ;;タブの幅をスペース２つに設定
    (setq tab-width 2))
  (add-hook 'coffee-mode-hook 'coffee-custom))
"""
    file_appendln(EMACS_FILE,coffee_mode)
    
