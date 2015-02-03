;;;user-language
;;;ユーザーの自然言語と文字エンコーディングを設定
(set-language-environment "Japanese")
(prefer-coding-system 'utf-8)

;;;elpa-setting
;;;elpaを使う為に必要な設定
(require 'package)
(add-to-list 'package-archives '("melpa" . "http://melpa.milkbox.net/packages/"))
(add-to-list 'package-archives '("marmalade" . "http://marmalade-repo.org/packages/"))
(package-initialize)

;;;emacs-color-theme
;;emacsのカラーテーマをmanoj-darkに設定
(load-theme 'manoj-dark t)

;;;change-line-mode
;;;行の画面外の折り返しを変更するショートカット
(define-key global-map (kbd "M-l") 'toggle-truncate-lines)

;;;comment_out
;;;複数行のコメントアウトの設定ctrlと/で選択範囲を全てコメントアウト
(define-key global-map (kbd "C-c /") 'comment-or-uncomment-region)
;;;page_up
;;; ページアップのキーにctrl+]を追加
(define-key global-map (kbd "C-]") 'scroll-down)

;;;buffer_reload
;;;バッファの再読み込みをM+rで実行する
(defun revert-buffer-no-confirm (&optional force-reverting)
	(interactive "P")
	;;(message "force-reverting value is %s" force-reverting)
	(if (or force-reverting (not (buffer-modified-p)))
			(revert-buffer :ignore-auto :noconfirm)
		(error "The buffer has been modified")))
(global-set-key "\M-r" 'revert-buffer-no-confirm)

;;;show-column-number
;;;行番号を表示
(column-number-mode t)

;;;show-file-size
;;;ファイルサイズを表示
(size-indication-mode t)

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
(set-face-underline-p 'show-paren-match-face "color-123")

;;;auto-close-parentheses
;;;括弧を自動的に閉じる設定
(electric-pair-mode 1)

;;;backup-setting
;; バックアップとオートセーブファイルを~/.emacs.d/backups/へ集める
(add-to-list 'backup-directory-alist
	(cons "." "~/.emacs.d/backups/"))
(setq auto-save-file-name-transforms
	`((".*" ,(expand-file-name "~/.emacs.d/backups/") t)))

