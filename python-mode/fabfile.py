# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def python_setting():
  """[1]pythonのタブと文字エンコードの設定"""
  if not contains(EMACS_FILE,";;;pyhthon_setting"):
    file_appendln(EMACS_FILE,";;;python_setting")
    file_appendln(EMACS_FILE,";;utf-8で記述する事を宣言")
    file_appendln(EMACS_FILE,"(custom-set-variables '(safe-local-variable-values (quote ((encoding . utf-8)))))")
    file_appendln(EMACS_FILE,";;タブをスペース2つに設定")
    file_appendln(EMACS_FILE,"(add-hook 'python-mode-hook")
    file_appendln(EMACS_FILE,"'(lambda ()",1)
    file_appendln(EMACS_FILE,"(setq python-indent 2)",1)
    file_appendln(EMACS_FILE,";;indent-tabsをオフにしないとemacsに表示されるスペース間隔と実際の間隔に齟齬が生じる",1)
    file_appendln(EMACS_FILE,"(setq indent-tabs-mode nil)))",1)
    file_appendln(EMACS_FILE,"")





    
        
        
    
