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
	"""[2]emacsをインストールするのに必要なパッケージ"""
	os_name=check_os()

	if(os_name == 'centos'):
		if not command_check("wget"):
			sudo("yum install -y wget")

@task
def install_emacs24():
	"""[3]emacs24のインストール"""
	os_name=check_os()
	
	if(os_name == 'centos'):
		if not command_check("emacs"):
			with cd("/etc/yum.repos.d"):        
				sudo("wget http://pj.freefaculty.org/EL/pjku.repo")
				sudo("rpm --import http://pj.freefaculty.org/EL/PaulJohnson-BinaryPackageSigningKey")
				sudo("yum install -y emacs-24.2-4.el6.x86_64")
	elif(os_name == 'ubuntu'):
		if not command_check("emacs"):
			sudo("apt-get -y install emacs24")
