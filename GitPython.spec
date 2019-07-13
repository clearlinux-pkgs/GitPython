#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : GitPython
Version  : 2.1.11
Release  : 21
URL      : https://files.pythonhosted.org/packages/4d/e8/98e06d3bc954e3c5b34e2a579ddf26255e762d21eb24fede458eff654c51/GitPython-2.1.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/4d/e8/98e06d3bc954e3c5b34e2a579ddf26255e762d21eb24fede458eff654c51/GitPython-2.1.11.tar.gz
Summary  : Python Git Library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: GitPython-python3
Requires: GitPython-license
Requires: GitPython-python
Requires: ddt
Requires: gitdb2
BuildRequires : buildreq-distutils3

%description
## GitPython
GitPython is a python library used to interact with git repositories, high-level like git-porcelain,
or low-level like git-plumbing.

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
%setup -q -n GitPython-2.1.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533789848
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
