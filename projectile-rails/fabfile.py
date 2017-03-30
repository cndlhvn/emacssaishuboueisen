# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def projectile_rails_install():
  """[1]projectile-railsのインストール"""
  if not contains(EMACS_FILE,";;;projectile_rails"):
    projectile_rails="""
;;;projectile_rails
(el-get-bundle projectile-rails)
(require 'projectile)
(projectile-global-mode)

(require 'projectile-rails)
(projectile-rails-global-mode)"""
    file_appendln(EMACS_FILE,projectile_rails)
    with cd(EMACS_DIR):
      run("emacs --batch --script init.el")
  if gitcheckdiff():
    gitcommit("projectile_railsのインストール")
    print("projectile_railsのインストール")
