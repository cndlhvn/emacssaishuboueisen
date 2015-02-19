;;;emmet-mode
;;;emmetの設定
;;emmetの記法の文末でC-jで展開
(when (require 'emmet-mode nil t)
  ;; マークアップ言語全部で使う
  (add-hook 'sgml-mode-hook 'emmet-mode)
  ;; CSSにも使う
  (add-hook 'css-mode-hook  'emmet-mode)
  ;; web-modeに付け加える
  (add-hook 'web-mode-hook  'emmet-mode)
  ;; php-modeに付け加える
  (add-hook 'php-mode-hook 'emmet-mode)
  ;; indent はスペース2個
  (add-hook 'emmet-mode-hook (lambda () (setq emmet-indentation 2))))
