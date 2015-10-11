# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def haml_install():
  """[1]hamlのインストール"""
  if not contains(EMACS_FILE,";;;haml-mode"):
    haml_mode="""
;;;haml-mode
(el-get-bundle haml-mode)
(when (require 'haml-mode nil t)
(add-hook 'haml-mode-hook
          (lambda ()
            (setq tab-width 2)
            (indent-tabs-mode nil)
            (setq c-basic-offset 8)
            (setq haml-indent-offset 2))))"""
    file_appendln(EMACS_FILE,haml_mode)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")
    
