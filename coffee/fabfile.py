# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def coffee_install():
  """[1]coffee-modeのインストール"""
  if not contains(EMACS_FILE,";;;coffee-mode"):
    coffee_mode="""
;;;coffee-mode
(el-get-bundle coffee-mode :depends (dash))
(when (require 'coffee-mode nil t)
  (defun coffee-custom ()
    ;;インデントモードをオフ
    (setq-default indent-tabs-mode nil)
    ;;タブの幅をスペース２つに設定
    (setq tab-width 2))
  (add-hook 'coffee-mode-hook 'coffee-custom))"""
    file_appendln(EMACS_FILE,coffee_mode)
    with cd(EMACS_DIR):
      run("emacs --batch --script  init.el")

  if gitcheckdiff():
    gitcommit("coffee-modeのインストールと設定")
    print("coffee-modeののインストールと設定")
