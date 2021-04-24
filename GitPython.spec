#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : GitPython
Version  : 3.1.15
Release  : 61
URL      : https://files.pythonhosted.org/packages/4a/8a/1519359949ce416eb059966c483fe340547a6fb5efb9f1dbcc0b33483146/GitPython-3.1.15.tar.gz
Source0  : https://files.pythonhosted.org/packages/4a/8a/1519359949ce416eb059966c483fe340547a6fb5efb9f1dbcc0b33483146/GitPython-3.1.15.tar.gz
Summary  : Python Git Library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: GitPython-license = %{version}-%{release}
Requires: GitPython-python = %{version}-%{release}
Requires: GitPython-python3 = %{version}-%{release}
Requires: gitdb
BuildRequires : buildreq-distutils3
BuildRequires : gitdb

%description
## [Gitoxide](https://github.com/Byron/gitoxide): A peek into the future…
I started working on GitPython in 2009, back in the days when Python was 'my thing' and I had great plans with it.
Of course, back in the days, I didn't really know what I was doing and this shows in many places. Somewhat similar to
Python this happens to be 'good enough', but at the same time is deeply flawed and broken beyond repair.

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
Provides: pypi(gitpython)
Requires: pypi(gitdb)
Requires: pypi(typing_extensions)

%description python3
python3 components for the GitPython package.


%prep
%setup -q -n GitPython-3.1.15
cd %{_builddir}/GitPython-3.1.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619023092
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/GitPython
cp %{_builddir}/GitPython-3.1.15/LICENSE %{buildroot}/usr/share/package-licenses/GitPython/98a91252d682790e518df3df5c68339d17ab7e47
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
