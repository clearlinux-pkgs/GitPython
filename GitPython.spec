#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9FEE1C6A3B07188F (byronimo@gmail.com)
#
Name     : GitPython
Version  : 2.1.5
Release  : 15
URL      : http://pypi.debian.net/GitPython/GitPython-2.1.5.tar.gz
Source0  : http://pypi.debian.net/GitPython/GitPython-2.1.5.tar.gz
Source99 : http://pypi.debian.net/GitPython/GitPython-2.1.5.tar.gz.asc
Summary  : Python Git Library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: GitPython-python3
Requires: GitPython-license
Requires: GitPython-python
Requires: ddt
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package license
Summary: license components for the GitPython package.
Group: Default

%description license
license components for the GitPython package.


%package python
Summary: python components for the GitPython package.
Group: Default
Requires: GitPython-python3
Provides: gitpython-python

%description python
python components for the GitPython package.


%package python3
Summary: python3 components for the GitPython package.
Group: Default
Requires: python3-core

%description python3
python3 components for the GitPython package.


%prep
%setup -q -n GitPython-2.1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532207633
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/GitPython
cp LICENSE %{buildroot}/usr/share/doc/GitPython/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/GitPython/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
