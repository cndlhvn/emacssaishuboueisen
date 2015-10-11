# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def dmacro_install():
  """[1]dmacroのインストール"""
  if not contains(EMACS_FILE,";;;dmacro_setting"):
    dmacro_setting ="""
;;;dmacro_setting
;;繰り返したい処理をemacs上で2回以上繰り返す
;;C-tで繰り返せる
(el-get-bundle dmacro
	:type http
	:url "http://www.pitecan.com/papers/JSSSTDmacro/dmacro.el")
(defconst *dmacro-key* "\C-t" "繰返し指定キー")
(global-set-key *dmacro-key* 'dmacro-exec)
(autoload 'dmacro-exec "dmacro" nil t)"""
    file_appendln(EMACS_FILE,dmacro_setting)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")

