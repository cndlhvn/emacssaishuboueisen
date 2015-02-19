# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def dmacro_install():
  """[1]dmacroのインストール"""
  with cd(EMACS_CONF):
    if not contains("elpa-component.el",";;;dmacro"):
      register_elisp_to_elpa("dmacro",'http://www.pitecan.com/papers/JSSSTDmacro/dmacro.el')
      run("emacs --batch --script elpa-component.el")
      
  if not contains(EMACS_FILE,";;;dmacro_setting"):
    file_appendln(EMACS_FILE,";;;dmacro_setting")
    file_appendln(EMACS_FILE,";;;繰り返しコマンドdmacroの設定")
    file_appendln(EMACS_FILE,"(defconst *dmacro-key* \"\C-t\" \"繰返し指定キー\")")
    file_appendln(EMACS_FILE,"(global-set-key *dmacro-key* 'dmacro-exec)")
    file_appendln(EMACS_FILE,"(autoload 'dmacro-exec \"dmacro\" nil t)")
    file_appendln(EMACS_FILE,"")

