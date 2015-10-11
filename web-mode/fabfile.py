# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def web_mode_install():
  """[1]web-modeをインストール"""
  if not contains(EMACS_FILE,";;;web_mode"):
    web_mode="""
;;;web_mode
(el-get-bundle web-mode)
(when (require 'web-mode nil t)
  ;;web-modeを適応させる拡張子
  (add-to-list 'auto-mode-alist '(\"\.php$\" . web-mode))
  (add-to-list 'auto-mode-alist '(\"\.html$\". web-mode))
  (add-to-list 'auto-mode-alist '(\"\.html.erb$\". web-mode))
  (add-to-list 'auto-mode-alist '(\"\.ctp$\" . web-mode))
  (defun my-web-mode-hook ()
    ;;インデントモードをオフ
    (setq-default indent-tabs-mode nil)
    ;;タブ幅をスペース２つ
    (setq tab-width 2)
    ;;マークアップのタブ幅をスペース２個
    (setq web-mode-markup-indent-offset 2)
    ;;スタイシートでタブ幅をスペース２個
    (setq web-mode-css-indent-offset 2)
    (setq css-indent-offset 2)
    ;;プログラムでタブ幅をスペース２個
    (setq web-mode-code-indent-offset 2))
  (add-hook 'web-mode-hook  'my-web-mode-hook))"""
    file_appendln(EMACS_FILE,web_mode)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")

@task
def web_mode_color():
  """[2]web-modeでのhtmlの色を設定"""
  if not contains(EMACS_FILE,";;;web_mode_color"):
    web_mode_color="""
;;;web_mode_color
;;端末の背景が黒系の時に見やすい色に設定
(set-face-attribute 'web-mode-doctype-face nil :foreground \"Blue\")
(set-face-attribute 'web-mode-html-tag-face nil :foreground \"White\")
(set-face-attribute 'web-mode-html-tag-bracket-face nil :foreground \"White3\")
(set-face-attribute 'web-mode-html-attr-name-face nil :foreground \"Red\")
(set-face-attribute 'web-mode-html-attr-value-face nil :foreground \"Yellow\")
"""
    file_appendln(EMACS_FILE,web_mode_color)
