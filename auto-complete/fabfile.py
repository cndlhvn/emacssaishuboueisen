# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def auto_complete_installing():
  """[1]auto-completeのインストール"""
  with cd(EMACS_CONF):
    if not contains("elpa-component.el",";;;auto-complete"):
      register_library_to_elpa("auto-complete")
      run("emacs --batch --script elpa-component.el")

    if not dir_exists(EMACS_DIR+"ac-dict"):
      run("mkdir "+EMACS_DIR+"ac-dict")
      
    if not contains(EMACS_FILE,";;;auto-complete"):
      auto_complete="""
;;;auto-complete
(when (require 'auto-complete-config nil t)
  (ac-config-default)
  ;;auto-completeの候補データを収めるフォルダを指定
  (add-to-list 'ac-dictionary-directories "~/.emacs.d/ac-dict")
  ;;M-tabで補完候補を表示
  (define-key ac-mode-map (kbd "M-TAB") 'auto-complete))"""
      file_appendln(EMACS_FILE,auto_complete)

