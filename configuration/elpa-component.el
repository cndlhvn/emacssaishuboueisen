(require 'cl)

;;;elpa-setting
;;;elpaの初期化
(require 'package)
(add-to-list 'package-archives '("melpa" . "http://melpa.milkbox.net/packages/"))
(add-to-list 'package-archives '("marmalade" . "http://marmalade-repo.org/packages/"))
(package-initialize)

(defvar installing-package-list
  '(
    ;; ここに自動的にインストールしたいelpaのパッケージを追加
		;;add-elpa-package
		
    ))

(let ((not-installed (loop for x in installing-package-list
													 when (not (package-installed-p x))
													 collect x)))
  (when not-installed
    (package-refresh-contents)
    (dolist (pkg not-installed)
			(package-install pkg))))


(defvar installing-package-urls-list
  '(
    ;; 1ファイルのelispしか管理できません
		;; ここに自動的にダウンロードしたい.elのURLを追加
    ;; パッケージ名はファイル名の.elより前の部分になります
		;;add-elisp-url
		
    )
	)

;; ネットワーク経由で取得したelispをpackage.el管理する
(defun package-install-from-url (url)
  "URLを指定してパッケージをインストールする"
  (interactive "sURL: ")
  (let ((file (and (string-match "\\([a-z0-9-]+\\)\\.el" url) (match-string-no-properties 1 url))))
    (with-current-buffer (url-retrieve-synchronously url)
      (goto-char (point-min))
      (delete-region (point-min) (search-forward "\n\n"))
      (goto-char (point-min))
      (setq info (cond ((condition-case nil (package-buffer-info) (error nil)))
                       ((re-search-forward "[$]Id: .+,v \\([0-9.]+\\) .*[$]" nil t)
                        (vector file nil (concat "[my:package-install-from-url]") (match-string-no-properties 1) ""))
                       (t (vector file nil (concat file "[my:package-install-from-url]") (format-time-string "%Y%m%d") ""))))
      (package-install-from-buffer info 'single)
      (kill-buffer)
      )))

(defun package-url-installed-p (url)
  "指定されたURLに対応するパッケージがインストールされているか調べる"
  (interactive "sURL: ")
  (let ((pkg-name (and (string-match "\\([a-z0-9-]+\\)\\.el" url) (match-string-no-properties 1 url))))
    (package-installed-p (intern pkg-name))))

(let ((urls (loop for url in installing-package-urls-list
									unless (package-url-installed-p url)
									collect url)))
	(dolist (url urls)
		(package-install-from-url url)))
