# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def auto_complete_installing():
  """[1]auto-completeのインストール"""
  if not contains(EMACS_FILE,";;;auto-complete"):
    auto_complete="""
;;;auto-complete
(el-get-bundle auto-complete)
(when (require 'auto-complete-config nil t)
  (ac-config-default)
  ;;M-tabで補完候補を表示
  (define-key ac-mode-map (kbd "M-TAB") 'auto-complete))"""
    file_appendln(EMACS_FILE,auto_complete)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")
