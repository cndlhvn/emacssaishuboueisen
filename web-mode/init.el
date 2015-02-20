;;;web_mode
(when (require 'web-mode nil t)
  ;;web-modeを適応させる拡張子
  (add-to-list 'auto-mode-alist '("\.php" . web-mode))
  (add-to-list 'auto-mode-alist '("\.html". web-mode))
  (add-to-list 'auto-mode-alist '("\.html.erb". web-mode))
  (add-to-list 'auto-mode-alist '("\.ctp" . web-mode))
  (defun my-web-mode-hook ()
    ;;マークアップのタブ幅をスペース２個
    (setq web-mode-markup-indent-offset 2)
    ;;スタイシートでタブ幅をスペース２個
    (setq web-mode-css-indent-offset 2)
    ;;プログラムでタブ幅をスペース２個
    (setq web-mode-code-indent-offset 2))
  (add-hook 'web-mode-hook  'my-web-mode-hook))

;;;web_mode_color
;;端末の背景が黒系の時に見やすい色に設定
(set-face-attribute 'web-mode-doctype-face nil :foreground "Blue")
(set-face-attribute 'web-mode-html-tag-face nil :foreground "White")
(set-face-attribute 'web-mode-html-tag-bracket-face nil :foreground "White3")
(set-face-attribute 'web-mode-html-attr-name-face nil :foreground "Red")
(set-face-attribute 'web-mode-html-attr-value-face nil :foreground "Yellow")


