# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def emmet_install():
  """[1]emmetを導入"""
  if not contains(EMACS_FILE,";;;emmet-mode"):
    emmet_mode="""
;;;emmet-mode
;;emmetの記法の文末でC-jで展開
(el-get-bundle emmet-mode)
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
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")
  if gitcheckdiff():
    gitcommit("emmet-modeのインストールと設定")
    print("emmet-modeのインストールと設定")
