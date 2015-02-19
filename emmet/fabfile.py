# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def emmet_install():
  """[1]emmetを導入"""
  with cd(EMACS_CONF):
    if not contains("elpa-component.el",";;;emmet-mode"):
      register_library_to_elpa("emmet-mode")
      run("emacs --batch --script elpa-component.el")

  if not contains(EMACS_FILE,";;;emmet-mode"):
    file_appendln(EMACS_FILE,";;;emmet-mode")
    file_appendln(EMACS_FILE,";;;emmetの設定")
    file_appendln(EMACS_FILE,";;emmetの記法の文末でC-jで展開")
    file_appendln(EMACS_FILE,"(when (require 'emmet-mode nil t)")
    file_appendln(EMACS_FILE,";; マークアップ言語全部で使う",1)
    file_appendln(EMACS_FILE,"(add-hook 'sgml-mode-hook 'emmet-mode)",1)
    file_appendln(EMACS_FILE,";; CSSにも使う",1)
    file_appendln(EMACS_FILE,"(add-hook 'css-mode-hook  'emmet-mode)",1)
    file_appendln(EMACS_FILE,";; web-modeに付け加える",1)
    file_appendln(EMACS_FILE,"(add-hook 'web-mode-hook  'emmet-mode)",1)
    file_appendln(EMACS_FILE,";; php-modeに付け加える",1)
    file_appendln(EMACS_FILE,"(add-hook 'php-mode-hook 'emmet-mode)",1)
    file_appendln(EMACS_FILE,";; indent はスペース2個",1)
    file_appendln(EMACS_FILE,"(add-hook 'emmet-mode-hook (lambda () (setq emmet-indentation 2))))",1)
    file_appendln(EMACS_FILE,"")
    

