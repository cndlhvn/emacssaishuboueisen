# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")


@task
def package_manager_update():
  """[1]パッケージマネージャーをアップデート"""
  os_name=check_os()
  
  if(os_name =='centos'):
    sudo("yum -y update")
  elif(os_name == 'ubuntu'):
    sudo("apt-get update")
  elif(os_name == 'mac'):
    run("brew update")

@task
def install_basic_package():
  """[2]!emacsをインストールするのに必要なパッケージ"""
  os_name=check_os()

  if(os_name == 'centos'):
    if not command_check("wget"):
      sudo("yum install -y wget ncurses-devel")

@task
def install_emacs24():
  """[3]!emacs24のインストール"""
  os_name=check_os()
  
  if(os_name == 'centos'):
    if not command_check("emacs"):
      run("wget http://ftp.jaist.ac.jp/pub/GNU/emacs/emacs-24.3.tar.gz")
      run("tar zxvfp emacs-24.3.tar.gz")
      with cd("emacs-24.3"):
        run("./configure -without-x -without-selinux")
        run("make")
        sudo("make install")
        run("rm -rf ~/emacs-24.3")
        run("rm -f ~/emacs-24.3.tar.gz")
  elif(os_name == 'ubuntu'):
    if not command_check("emacs"):
      sudo("apt-get -y install emacs24")
