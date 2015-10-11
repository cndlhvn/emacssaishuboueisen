# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def create_emacs_file_dir():
  """[1]!emacsで使うフォルダと設定ファイルを作成"""
  
  if not dir_exists(EMACS_DIR):
    run('mkdir ' + EMACS_DIR)
  if not dir_exists(EMACS_DIR  + "backups"):
    run('mkdir ' + EMACS_DIR + "backups")
  if not file_exists(EMACS_FILE):
    run('touch '+EMACS_FILE)
			  
@task
def set_emacs_user_setting():
  """[2]!emacsのログインユーザーのデフォルトセッティング"""

  if not contains(EMACS_FILE,";;;user-language"):
    user_language="""
;;;user-language
;;;ユーザーの自然言語と文字エンコーディングを設定
(set-language-environment "Japanese")
(prefer-coding-system 'utf-8)"""
    file_appendln(EMACS_FILE, user_language)
			  
  if not contains(EMACS_FILE, ";;;el-get-setting"):
    el_get="""
;;;el-get-setting
(when load-file-name
  (setq user-emacs-directory (file-name-directory load-file-name)))

(add-to-list 'load-path (locate-user-emacs-file "el-get/el-get"))

(unless (require 'el-get nil 'noerror)
  (with-current-buffer
      (url-retrieve-synchronously
       "https://raw.githubusercontent.com/dimitri/el-get/master/el-get-install.el")
    (goto-char (point-max))
    (eval-print-last-sexp)))
"""
    file_appendln(EMACS_FILE, el_get)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")

  if not contains(EMACS_FILE,";;;emacs-color-theme"):
    emacs_color_theme="""
;;;emacs-color-theme
;;emacsのカラーテーマをmanoj-darkに設定
(load-theme 'manoj-dark t)"""
    file_appendln(EMACS_FILE,emacs_color_theme)
	  
  if not contains(EMACS_FILE,";;;change-line-mode"):
    change_line_mode="""
;;;change-line-mode
;;;行の画面外の折り返しを変更するショートカット
(define-key global-map (kbd "M-l") \'toggle-truncate-lines)"""
    file_appendln(EMACS_FILE,change_line_mode)

  if not contains(EMACS_FILE,";;;comment_out"):
    comment_out="""
;;;comment_out
;;;複数行のコメントアウトの設定ctrlと/で選択範囲を全てコメントアウト
(define-key global-map (kbd \"C-c /\") 'comment-or-uncomment-region)"""
    file_appendln(EMACS_FILE,comment_out)

  if not contains(EMACS_FILE,";;;page_up"):
    page_up="""
;;;page_up
;;; ページアップのキーにctrl+]を追加
(define-key global-map (kbd \"C-]\") 'scroll-down)"""
    file_appendln(EMACS_FILE,page_up)

  if not contains(EMACS_FILE,";;;buffer_reload"):
    buffer_reload="""
;;;buffer_reload
;;;バッファの再読み込みをM+rで実行する
(defun revert-buffer-no-confirm (&optional force-reverting)
  (interactive "P")
  (if (or force-reverting (not (buffer-modified-p)))
      (revert-buffer :ignore-auto :noconfirm)
    (error "The buffer has been modified")))
(global-set-key \"\M-r\" \'revert-buffer-no-confirm)"""
    file_appendln(EMACS_FILE,buffer_reload)

  if not contains(EMACS_FILE,";;;show-column-number"):
    show_column_number="""
;;;show-column-number
;;;行番号を表示
(column-number-mode t)"""
    file_appendln(EMACS_FILE,show_column_number)

  if not contains(EMACS_FILE,";;;show-file-size"):
    show_file_size="""
;;;show-file-size
;;;ファイルサイズを表示
(size-indication-mode t)"""
    file_appendln(EMACS_FILE,show_file_size)

  if not contains(EMACS_FILE,";;;paren-mode"):
    paren_mode = """
;;;paren-mode
;;;カーソルを括弧に合わせると範囲を表示する
(show-paren-mode t)
;;範囲表示の遅延を０秒にする
(setq show-paren-delay 0)
;;範囲内全てをカラーリングする
(setq show-paren-style 'expression)
;;括弧内の背景色反転をオフに設定
(set-face-background 'show-paren-match-face nil)
;;括弧内をアンダーラインで表示する
(set-face-underline-p \'show-paren-match-face "color-123")"""
    file_appendln(EMACS_FILE,paren_mode)

  if not contains(EMACS_FILE,";;;auto-close-parentheses"):
    auto_close_parentheses="""
;;;auto-close-parentheses
;;;括弧を自動的に閉じる設定
(electric-pair-mode 1)"""
    file_appendln(EMACS_FILE,auto_close_parentheses)

  if not contains(EMACS_FILE,";;;show-file-name"):
    show_file_name="""
;;;show-file-name
(defun show-file-name ()
  "Show the full path file name in the minibuffer."
  (interactive)
  (message (buffer-file-name)))"""
    file_appendln(EMACS_FILE,show_file_name)

  if not contains(EMACS_FILE,";;;default_tab_width"):
    default_tab_width="""
;;;default_tab_width
;;;デフォルトタブ幅の設定
(setq default-tab-width 2)
(setq tab-width 2)"""
    file_appendln(EMACS_FILE,default_tab_width)


@task
def back_up_setting():
  """[3]ファイルのバックアップを一カ所に集める設定（便利）"""
  if not dir_exists(EMACS_DIR  + "backups"):
    run('mkdir ' + EMACS_DIR + "backups")
  if not contains(EMACS_FILE,";;;backup-setting"):
    backup_setting = """
;;;backup-setting
;; バックアップとオートセーブファイルを~/.emacs.d/backups/へ集める
(add-to-list 'backup-directory-alist(cons "." "~/.emacs.d/backups/"))
(setq auto-save-file-name-transforms
      `((".*" ,(expand-file-name "~/.emacs.d/backups/") t)))"""
    file_appendln(EMACS_FILE,backup_setting)
	

@task
def share_config_with_root_user():
  """[3]ログインユーザーのemacs設定をlnでsudoユーザーと共有する"""
  
  login_user_name=get_login_user_name()
  os_name=check_os()

  if(os_name == 'centos'):
    sudo("chmod 740 /etc/sudoers")
    sed("/etc/sudoers","secure_path = /sbin:/bin:/usr/sbin:/usr/bin","secure_path = /usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin",limit="" ,use_sudo=True)
    sudo("chmod 440 /etc/sudoers")
  if(os_name == 'centos' or os_name == 'ubuntu'):
    with mode_sudo():
      if file_exists("/root/.emacs.d") or dir_exists("/root/.emacs.d"):
        sudo("mv /root/.emacs.d /root/.emacs.d_old")
    sudo("ln -s /home/"+login_user_name+"/.emacs.d /root/")
  elif(os_name == 'mac'):
    with mode_sudo():
      if file_exists("/var/root/.emacs.d") or dir_exists("/var/root/.emacs.d"):
        sudo("mv /var/root/.emacs.d /var/root/.emacs.d_old")
    sudo("ln -s /Users/"+login_user_name+"/.emacs.d /var/root/")
