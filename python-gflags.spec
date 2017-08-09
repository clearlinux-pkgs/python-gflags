#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-gflags
Version  : 3.1.1
Release  : 1
URL      : http://pypi.debian.net/python-gflags/python-gflags-3.1.1.tar.gz
Source0  : https://pypi.python.org/packages/ea/30/b8469c0d1837ce58fe3706e1f7169cbf6ca1fb87d1f84cece5182b67cb0b/python-gflags-3.1.1.tar.gz
Summary  : Google Commandline Flags Module
Group    : Development/Tools
License  : BSD-3-Clause
Requires: python-gflags-bin
Requires: python-gflags-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
This repository contains a python implementation of the Google commandline
flags module.

%package bin
Summary: bin components for the python-gflags package.
Group: Binaries

%description bin
bin components for the python-gflags package.


%package python
Summary: python components for the python-gflags package.
Group: Default

%description python
python components for the python-gflags package.


%prep
%setup -q -n python-gflags-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502288242
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1502288242
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gflags2man.py

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
