# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def apache_install():
  """[1]apache-modeのインストール"""
  if not contains(EMACS_FILE,";;;apache-mode"):
    apache_mode="""
;;;apache-mode
(el-get-bundle apache-mode)
(add-to-list 'auto-mode-alist '("\.htaccess\'"   . apache-mode))
(add-to-list 'auto-mode-alist '("httpd\.conf\'"  . apache-mode))
(add-hook 'apache-mode-hook
          (lambda ()
            (setq apache-indent-level 2)
            (setq indent-tabs-mode nil)))"""
    file_appendln(EMACS_FILE,apache_mode)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")
  if gitcheckdiff():
    gitcommit("apache-modeのインストールとタブの設定")
    print("apache-modeのインストールとタブの設定")
