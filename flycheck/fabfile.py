# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def flycheck_installing():
  """[1]flycheckのインストール"""
  with cd(EMACS_CONF):
    if not contains("elpa-component.el",";;;flycheck"):
      register_library_to_elpa("flycheck")
      run("emacs --batch --script elpa-component.el")

  if not contains(EMACS_FILE,";;;flycheck"):
    flycheck="""
;;;flycheck
(add-hook 'after-init-hook #'global-flycheck-mode)"""
    file_appendln(EMACS_FILE,flycheck)
