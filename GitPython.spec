#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : GitPython
Version  : 3.0.7
Release  : 35
URL      : https://files.pythonhosted.org/packages/c7/6b/ba961c8a9d1dfdadcb2f860fe33ee17a2d16c6f77732a6105b718630dfdf/GitPython-3.0.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/c7/6b/ba961c8a9d1dfdadcb2f860fe33ee17a2d16c6f77732a6105b718630dfdf/GitPython-3.0.7.tar.gz
Summary  : Python Git Library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: GitPython-license = %{version}-%{release}
Requires: GitPython-python = %{version}-%{release}
Requires: GitPython-python3 = %{version}-%{release}
Requires: gitdb2
BuildRequires : buildreq-distutils3
BuildRequires : gitdb2

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
Requires: GitPython-python3 = %{version}-%{release}
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
%setup -q -n GitPython-3.0.7
cd %{_builddir}/GitPython-3.0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581185652
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/GitPython
cp %{_builddir}/GitPython-3.0.7/LICENSE %{buildroot}/usr/share/package-licenses/GitPython/98a91252d682790e518df3df5c68339d17ab7e47
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/GitPython/98a91252d682790e518df3df5c68339d17ab7e47

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
