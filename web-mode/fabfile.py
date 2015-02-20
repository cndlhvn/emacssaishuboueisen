# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def web_mode_install():
  """[1]web-modeをインストール"""
  with cd(EMACS_CONF):
    if not contains("elpa-component.el",";;;web-mode"):
      register_library_to_elpa("web-mode")
      run("emacs --batch --script elpa-component.el")

  if not contains(EMACS_FILE,";;;web_mode"):
    file_appendln(EMACS_FILE,";;;web_mode")
    file_appendln(EMACS_FILE,"(when (require 'web-mode nil t)")
    file_appendln(EMACS_FILE,";;web-modeを適応させる拡張子",1)
    file_appendln(EMACS_FILE,"(add-to-list 'auto-mode-alist '(\"\.php\" . web-mode))",1)
    file_appendln(EMACS_FILE,"(add-to-list 'auto-mode-alist '(\"\.html\". web-mode))",1)
    file_appendln(EMACS_FILE,"(add-to-list 'auto-mode-alist '(\"\.html.erb\". web-mode))",1)
    file_appendln(EMACS_FILE,"(add-to-list 'auto-mode-alist '(\"\.ctp\" . web-mode))",1)
    file_appendln(EMACS_FILE,"(defun my-web-mode-hook ()",1)
    file_appendln(EMACS_FILE,";;マークアップのタブ幅をスペース２個",1)
    file_appendln(EMACS_FILE,"(setq web-mode-markup-indent-offset 2)",2)
    file_appendln(EMACS_FILE,";;スタイシートでタブ幅をスペース２個",1)
    file_appendln(EMACS_FILE,"(setq web-mode-css-indent-offset 2)",2)
    file_appendln(EMACS_FILE,";;プログラムでタブ幅をスペース２個",1)
    file_appendln(EMACS_FILE,"(setq web-mode-code-indent-offset 2))",2)
    file_appendln(EMACS_FILE,"(add-hook 'web-mode-hook  'my-web-mode-hook))",1)
    file_appendln(EMACS_FILE,"")

@task
def web_mode_color():
  """[2]web-modeでのhtmlの色を設定"""
  if not contains(EMACS_FILE,";;;web_mode_color"):
    file_appendln(EMACS_FILE,";;;web_mode_color")
    file_appendln(EMACS_FILE,";;端末の背景が黒系の時に見やすい色に設定")
    file_appendln(EMACS_FILE,"(set-face-attribute 'web-mode-doctype-face nil :foreground \"Blue\")",1)
    file_appendln(EMACS_FILE,"(set-face-attribute 'web-mode-html-tag-face nil :foreground \"White\")",1)
    file_appendln(EMACS_FILE,"(set-face-attribute 'web-mode-html-tag-bracket-face nil :foreground \"White3\")",1)
    file_appendln(EMACS_FILE,"(set-face-attribute 'web-mode-html-attr-name-face nil :foreground \"Red\")",1)
    file_appendln(EMACS_FILE,"(set-face-attribute 'web-mode-html-attr-value-face nil :foreground \"Yellow\")",1)
    file_appendln(EMACS_FILE,"")


