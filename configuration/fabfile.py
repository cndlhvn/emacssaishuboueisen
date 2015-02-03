# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def create_emacs_file_dir():
  """[1]emacsで使うフォルダと設定ファイルを作成"""
  
  if not dir_exists(EMACS_DIR):
    run('mkdir ' + EMACS_DIR)
  if not dir_exists(EMACS_DIR  + "backups"):
    run('mkdir ' + EMACS_DIR + "backups")
  if not dir_exists(EMACS_DIR  + "elpa"):
    run('mkdir ' + EMACS_DIR + "elpa")
  if not dir_exists(EMACS_DIR  + "conf"):
    run('mkdir ' + EMACS_DIR + "conf")
  if not file_exists(EMACS_FILE):
    run('touch '+EMACS_FILE)

@task
def elpa_management_file_upload():
  """[2]elpaを管理するファイルをconfフォルダにアップロード"""
  if not file_exists(EMACS_CONF+"elpa-component.el"):
    put("elpa-component.el",EMACS_CONF)
			  
@task
def set_emacs_user_setting():
  """[3]emacsのログインユーザーのデフォルトセッティング"""

  if not contains(EMACS_FILE,";;;user-language"):
    file_appendln(EMACS_FILE,';;;user-language')
    file_appendln(EMACS_FILE,';;;ユーザーの自然言語と文字エンコーディングを設定')
    file_appendln(EMACS_FILE,'(set-language-environment "Japanese")')
    file_appendln(EMACS_FILE,"(prefer-coding-system 'utf-8)")
    file_appendln(EMACS_FILE,"")
			  
  if not contains(EMACS_FILE,";;;elpa-setting"):
    file_appendln(EMACS_FILE,';;;elpa-setting')
    file_appendln(EMACS_FILE,';;;elpaを使う為に必要な設定')
    file_appendln(EMACS_FILE,"(require 'package)")
    file_appendln(EMACS_FILE,'(add-to-list \'package-archives \'("melpa" . "http://melpa.milkbox.net/packages/"))')
    file_appendln(EMACS_FILE,'(add-to-list \'package-archives \'("marmalade" . "http://marmalade-repo.org/packages/"))')
    file_appendln(EMACS_FILE,'(package-initialize)')
    file_appendln(EMACS_FILE,'')

  if not contains(EMACS_FILE,";;;emacs-color-theme"):
    file_appendln(EMACS_FILE,';;;emacs-color-theme')
    file_appendln(EMACS_FILE,';;emacsのカラーテーマをmanoj-darkに設定')
    file_appendln(EMACS_FILE,"(load-theme 'manoj-dark t)")
    file_appendln(EMACS_FILE,"")
	  
  if not contains(EMACS_FILE,";;;change-line-mode"):
    file_appendln(EMACS_FILE,';;;change-line-mode')
    file_appendln(EMACS_FILE,';;;行の画面外の折り返しを変更するショートカット')
    file_appendln(EMACS_FILE,'(define-key global-map (kbd "M-l") \'toggle-truncate-lines)')
    file_appendln(EMACS_FILE,"")

  if not contains(EMACS_FILE,";;;comment_out"):
    file_appendln(EMACS_FILE,';;;comment_out')
    file_appendln(EMACS_FILE,';;;複数行のコメントアウトの設定ctrlと/で選択範囲を全てコメントアウト')
    file_appendln(EMACS_FILE,"(define-key global-map (kbd \"C-c /\") 'comment-or-uncomment-region)")
    file_append(EMACS_FILE,'')

  if not contains(EMACS_FILE,";;;page_up"):
    file_appendln(EMACS_FILE,';;;page_up')
    file_appendln(EMACS_FILE,';;; ページアップのキーにctrl+]を追加')
    file_appendln(EMACS_FILE,"(define-key global-map (kbd \"C-]\") 'scroll-down)")
    file_appendln(EMACS_FILE,'')

  if not contains(EMACS_FILE,";;;buffer_reload"):
    file_appendln(EMACS_FILE,";;;buffer_reload")
    file_appendln(EMACS_FILE,";;;バッファの再読み込みをM+rで実行する")
    file_appendln(EMACS_FILE,"(defun revert-buffer-no-confirm (&optional force-reverting)")
    file_appendln(EMACS_FILE,'(interactive "P")',1)
    file_appendln(EMACS_FILE,';;(message "force-reverting value is %s" force-reverting)',1)
    file_appendln(EMACS_FILE,"(if (or force-reverting (not (buffer-modified-p)))",1)
    file_appendln(EMACS_FILE,"(revert-buffer :ignore-auto :noconfirm)",3)
    file_appendln(EMACS_FILE,'(error "The buffer has been modified")))',2)
    file_appendln(EMACS_FILE,'(global-set-key \"\M-r\" \'revert-buffer-no-confirm)')
    file_appendln(EMACS_FILE,"")

  if not contains(EMACS_FILE,";;;show-column-number"):
    file_appendln(EMACS_FILE,";;;show-column-number")
    file_appendln(EMACS_FILE,";;;行番号を表示")
    file_appendln(EMACS_FILE,"(column-number-mode t)")
    file_appendln(EMACS_FILE,"")

  if not contains(EMACS_FILE,";;;show-file-size"):
    file_appendln(EMACS_FILE,";;;show-file-size")
    file_appendln(EMACS_FILE,";;;ファイルサイズを表示")
    file_appendln(EMACS_FILE,"(size-indication-mode t)")
    file_appendln(EMACS_FILE,"")

  if not contains(EMACS_FILE,";;;paren-mode"):
    file_appendln(EMACS_FILE,";;;paren-mode")
    file_appendln(EMACS_FILE,";;;カーソルを括弧に合わせると範囲を表示する")
    file_appendln(EMACS_FILE,"(show-paren-mode t)")
    file_appendln(EMACS_FILE,";;範囲表示の遅延を０秒にする")
    file_appendln(EMACS_FILE,"(setq show-paren-delay 0)")
    file_appendln(EMACS_FILE,";;範囲内全てをカラーリングする")
    file_appendln(EMACS_FILE,"(setq show-paren-style 'expression)")
    file_appendln(EMACS_FILE,";;括弧内の背景色反転をオフに設定")
    file_appendln(EMACS_FILE,"(set-face-background 'show-paren-match-face nil)")
    file_appendln(EMACS_FILE,";;括弧内をアンダーラインで表示する")
    file_appendln(EMACS_FILE,'(set-face-underline-p \'show-paren-match-face "color-123")')
    file_appendln(EMACS_FILE,"")

  if not contains(EMACS_FILE,";;;auto-close-parentheses"):
    file_appendln(EMACS_FILE,";;;auto-close-parentheses")
    file_appendln(EMACS_FILE,";;;括弧を自動的に閉じる設定")
    file_appendln(EMACS_FILE,"(electric-pair-mode 1)")
    file_appendln(EMACS_FILE,"")

@task
def back_up_setting():
  """[4]ファイルのバックアップを一カ所に集める設定（便利）"""
  if not dir_exists(EMACS_DIR  + "backups"):
    run('mkdir ' + EMACS_DIR + "backups")
  if not contains(EMACS_FILE,";;;backup-setting"):
    file_appendln(EMACS_FILE,";;;backup-setting")
    file_appendln(EMACS_FILE,";; バックアップとオートセーブファイルを~/.emacs.d/backups/へ集める")
    file_appendln(EMACS_FILE,"(add-to-list 'backup-directory-alist")
    file_appendln(EMACS_FILE,'(cons "." "~/.emacs.d/backups/"))',1)
    file_appendln(EMACS_FILE,"(setq auto-save-file-name-transforms")
    file_appendln(EMACS_FILE,'`((".*" ,(expand-file-name "~/.emacs.d/backups/") t)))',1)
    file_appendln(EMACS_FILE,"")
	

@task
def share_config_with_root_user():
  """[4]ログインユーザーのemacs設定をlnでsudoユーザーと共有する"""
  
  login_user_name=get_login_user_name()
  os_name=check_os()
  
  if(os_name == 'centos' or os_name == 'ubuntu'):
    with mode_sudo():
      if file_exists("/root/.emacs.d") or dir_exists("/root/.emacs.d"):
        sudo("mv /root/.emacs.d /root/.emacs.d_old")
    sudo("ln -s /home/"+login_user_name+"/.emacs.d /root/")


