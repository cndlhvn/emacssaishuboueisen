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
    emmet_mode="""
;;;emmet-mode
;;emmetの記法の文末でC-jで展開
(when (require 'emmet-mode nil t)
  ;; マークアップ言語全部で使う
  (add-hook 'sgml-mode-hook 'emmet-mode)
  ;; CSSにも使う
  (add-hook 'css-mode-hook  'emmet-mode)
  ;; web-modeに付け加える
  (add-hook 'web-mode-hook  'emmet-mode)
  ;; php-modeに付け加える
  (add-hook 'php-mode-hook 'emmet-mode)
  ;; indent はスペース2個
  (add-hook 'emmet-mode-hook (lambda () (setq emmet-indentation 2))))"""
    file_appendln(EMACS_FILE,emmet_mode)
