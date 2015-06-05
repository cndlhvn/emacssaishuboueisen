# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def yaml_install():
  """[1]yamlのインストール"""
  with cd(EMACS_CONF):
    if not contains("elpa-component.el",";;;yaml-mode"):
      register_library_to_elpa("yaml-mode")
      run("emacs --batch --script elpa-component.el")

  if not contains(EMACS_FILE,";;;yaml-mode"):
    yaml_mode="""
;;;yaml-mode
(when (require 'yaml-mode nil t)
(add-to-list 'auto-mode-alist '("\\.yml$" . yaml-mode)))"""
    file_appendln(EMACS_FILE,yaml_mode)
    
