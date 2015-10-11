# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def anything_install():
  """[1]anythingのインストール"""
  if not contains(EMACS_FILE,";;;anything"):
    anything="""
;;;anything    
(el-get-bundle anything)
(when (require 'anything nil t)
  (when (require 'anything-startup nil t))
  (setq
   ;; 候補を表示するまでの時間。デフォは0.5
   anything-idle-delay 0.3
   ;; タイプして再描写するまでの時間。デフォルトは0.1
   anything-input-idle-delay 0.2
   ;; 最近使ったファイル候補の最大表示数。デフォルトは50
   anything-candidate-number-limit 10
   ;; 候補が多いときに体感速度を早くする
   anything-quick-update t
   ;; 候補選択ショートカットをアルファベットに
   anything-enable-shortcuts 'alphabet)
  ;; C-x C-aでanythingを起動
  (define-key global-map (kbd "C-x C-a") \'anything)

  (when (require 'anything-config nil t)
    ;;root権限でアクションを実行するときのコマンド
    ;; デフォルトは"su "
    ;;anythingで表示されたファイルリストにカーソルを当てたまま
    ;;タブを押すとファイルに対してのアクションが選択できる
    ;;そこでFind file as rootを選んでファイルを開く時、sudoでファイルを開く
    (setq anything-su-or-sudo "sudo")))
  ;;今のところこの下の設定は使い方が分からない
  ;;(require 'anything-show-completion nil t)
  ;;(when (require 'anything-complete nil t)
  ;; lispシンボルの補完候補の再検索時間
  ;;(anything-lisp-complete-symbol-set-timer 150)))"""
    file_appendln(EMACS_FILE,anything)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")
    
@task
def anything_killring_list():
  """[2]anythingのkill-ring-listの設定"""
  if not contains(EMACS_FILE,";;;anything_killring"):
    anything_killring="""
;;;anything_killring
;;コピーやカットの履歴から貼り付けが可能
(setq anything-kill-ring-threshold 5)
(global-set-key "\M-y" 'anything-show-kill-ring)"""
    file_appendln(EMACS_FILE,anything_killring)
