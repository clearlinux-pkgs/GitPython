#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : GitPython
Version  : 2.1.3
Release  : 11
URL      : http://pypi.debian.net/GitPython/GitPython-2.1.3.tar.gz
Source0  : http://pypi.debian.net/GitPython/GitPython-2.1.3.tar.gz
Summary  : Python Git Library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: GitPython-python
Requires: ddt
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the GitPython package.
Group: Default
Provides: gitpython-python

%description python
python components for the GitPython package.


%prep
%setup -q -n GitPython-2.1.3

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488983047
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1488983047
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
