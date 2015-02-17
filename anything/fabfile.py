# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def anything_install():
  """[1]anythingのインストール"""
  with cd(EMACS_CONF):
    if not contains("elpa-component.el",";;;anything"):
      register_library_to_elpa("anything")
      run("emacs --batch --script elpa-component.el")
      
  if not contains(EMACS_FILE,";;;anything"):
    file_appendln(EMACS_FILE,";;;anything")
    file_appendln(EMACS_FILE,"(when (require 'anything nil t)")
    file_appendln(EMACS_FILE,"(when (require 'anything-startup nil t))",1)
    file_appendln(EMACS_FILE,"(setq",1)
    file_appendln(EMACS_FILE,";; 候補を表示するまでの時間。デフォは0.5",2)
    file_appendln(EMACS_FILE,"anything-idle-delay 0.3",2)
    file_appendln(EMACS_FILE,";; タイプして再描写するまでの時間。デフォルトは0.1",2)
    file_appendln(EMACS_FILE,"anything-input-idle-delay 0.2",2)
    file_appendln(EMACS_FILE,";; 候補の最大表示数。デフォルトは50",2)
    file_appendln(EMACS_FILE,"anything-candidate-number-limit 100",2)
    file_appendln(EMACS_FILE,";; 候補が多いときに体感速度を早くする",2)
    file_appendln(EMACS_FILE,"anything-quick-update t",2)
    file_appendln(EMACS_FILE,";; 候補選択ショートカットをアルファベットに",2)
    file_appendln(EMACS_FILE,"anything-enable-shortcuts 'alphabet)",2)
    file_appendln(EMACS_FILE,";; C-x C-aでanythingを起動",2)
    file_appendln(EMACS_FILE,'(define-key global-map (kbd "C-x C-a") \'anything)',1)
    file_appendln(EMACS_FILE,'')
    file_appendln(EMACS_FILE,"(when (require 'anything-config nil t)",1)
    file_appendln(EMACS_FILE,";;root権限でアクションを実行するときのコマンド",2)
    file_appendln(EMACS_FILE,';; デフォルトは"su"',2)
    file_appendln(EMACS_FILE,';;anythingで表示されたファイルリストにカーソルを当てたまま',2)
    file_appendln(EMACS_FILE,';;タブを押すとファイルに対してのアクションが選択できる',2)
    file_appendln(EMACS_FILE,';;そこでFind file as rootを選んでファイルを開く時、sudoでファイルを開く',2)
    file_appendln(EMACS_FILE,'(setq anything-su-or-sudo "sudo"))',2)
    file_appendln(EMACS_FILE,'')
    file_appendln(EMACS_FILE,';;今のところこの下の設定は使い方が分からない',1)
    file_appendln(EMACS_FILE,"(require 'anything-show-completion nil t)",1)
    file_appendln(EMACS_FILE,"(when (require 'anything-complete nil t)",1)
    file_appendln(EMACS_FILE,";; lispシンボルの補完候補の再検索時間",2)
    file_appendln(EMACS_FILE,"(anything-lisp-complete-symbol-set-timer 150)))",2)
    file_appendln(EMACS_FILE,'')
    

