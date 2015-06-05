;;;python_setting
;;utf-8で記述する事を宣言
(custom-set-variables '(safe-local-variable-values (quote ((encoding . utf-8)))))
;;;タブをスペース2つに設定
(add-hook 'python-mode-hook
					'(lambda ()
						 (setq python-indent 2)
						 ;;indent-tabsをオフにしないとemacsに表示されるスペース間隔と実際の間隔に齟齬が生じる
						 (setq indent-tabs-mode nil)))
