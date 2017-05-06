yum install wget -y
wget  http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
rpm -ivh nginx-release-centos-7-0.el7.ngx.noarch.rpm
yum install nginx -y
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
run.sh