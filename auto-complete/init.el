;;;auto-complete
(when (require 'auto-complete-config nil t)
  ;;auto-completeの候補データを収めるフォルダを指定
  (add-to-list 'ac-dictionary-directories "~/.emacs.d/ac-dict")
  ;;M-tabで補完候補を表示
  (define-key ac-mode-map (kbd "M-TAB") 'auto-complete)
  (ac-config-default))
