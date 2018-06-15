#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-gflags
Version  : 3.1.2
Release  : 12
URL      : http://pypi.debian.net/python-gflags/python-gflags-3.1.2.tar.gz
Source0  : http://pypi.debian.net/python-gflags/python-gflags-3.1.2.tar.gz
Summary  : Google Commandline Flags Module
Group    : Development/Tools
License  : BSD-3-Clause
Requires: python-gflags-bin
Requires: python-gflags-python3
Requires: python-gflags-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
The list of files here isn't complete.  For a step-by-step guide on
how to set this package up correctly, check out
http://www.debian.org/doc/maint-guide/

%package bin
Summary: bin components for the python-gflags package.
Group: Binaries

%description bin
bin components for the python-gflags package.


%package python
Summary: python components for the python-gflags package.
Group: Default
Requires: python-gflags-python3

%description python
python components for the python-gflags package.


%package python3
Summary: python3 components for the python-gflags package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-gflags package.


%prep
%setup -q -n python-gflags-3.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523299287
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
