# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def yaml_install():
  """[1]yamlのインストール"""
  if not contains(EMACS_FILE,";;;yaml-mode"):
    yaml_mode="""
;;;yaml-mode
(el-get-bundle yaml-mode)
(when (require 'yaml-mode nil t)
(add-to-list 'auto-mode-alist '("\\.yml$" . yaml-mode)))"""
    file_appendln(EMACS_FILE,yaml_mode)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")
