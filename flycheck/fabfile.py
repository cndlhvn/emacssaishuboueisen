# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def flycheck_installing():
  """[1]flycheckのインストール"""
  if not contains(EMACS_FILE,";;;flycheck"):
    flycheck="""
;;;flycheck
(el-get-bundle flycheck)
(add-hook 'after-init-hook #'global-flycheck-mode)"""
    file_appendln(EMACS_FILE,flycheck)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")
  if gitcheckdiff():
    gitcommit("flycheckのインストール")
    print("flycheckのインストール")
