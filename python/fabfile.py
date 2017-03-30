# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def python_setting():
  """[1]pythonのタブと文字エンコードの設定"""
  if not contains(EMACS_FILE,";;;python_setting"):
    python_setting="""
;;;python_setting
;;utf-8で記述する事を宣言    
(custom-set-variables '(safe-local-variable-values (quote ((encoding . utf-8)))))
;;インデントモードをオフにする
(add-hook 'python-mode-hook
          (lambda ()
            (setq python-indent 2)
            (setq indent-tabs-mode nil)))"""
    file_appendln(EMACS_FILE,python_setting)
  if gitcheckdiff():
    gitcommit("python-modeでutf-8を宣言、インデントではなくスペース2")
    print("python-modeでutf-8を宣言、インデントではなくスペース2")
