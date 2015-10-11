# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def scss_install():
  """[1]scssのインストール"""
  if not contains(EMACS_FILE,";;;scss-mode"):
    scss_mode="""
;;;scss-mode
(el-get-bundle scss-mode)
(when (require 'scss-mode nil t)
(add-to-list 'auto-mode-alist '("\.scss$" . scss-mode))
;; インデント幅を2にする
;; コンパイルは compass watchで行うので自動コンパイルをオフ
(defun scss-custom ()
  ;;インデントモードをオフ
  (setq-default indent-tabs-mode nil)
  ;;タブの幅をスペース２つに設定
  (set (make-local-variable 'css-indent-offset) 2)
  (setq tab-width 2)
  ;; コンパイルは compass watchで行うので自動コンパイルをオフ
  (set (make-local-variable 'scss-compile-at-save) nil))
(add-hook 'scss-mode-hook 'scss-custom))"""
    file_appendln(EMACS_FILE,scss_mode)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")
