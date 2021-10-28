#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9CB5EE7895E8268B (sebastian.thiel@icloud.com)
#
Name     : GitPython
Version  : 3.1.24
Release  : 74
URL      : https://files.pythonhosted.org/packages/34/cc/aaa7a0d066ac9e94fbffa5fcf0738f5742dd7095bdde950bd582fca01f5a/GitPython-3.1.24.tar.gz
Source0  : https://files.pythonhosted.org/packages/34/cc/aaa7a0d066ac9e94fbffa5fcf0738f5742dd7095bdde950bd582fca01f5a/GitPython-3.1.24.tar.gz
Source1  : https://files.pythonhosted.org/packages/34/cc/aaa7a0d066ac9e94fbffa5fcf0738f5742dd7095bdde950bd582fca01f5a/GitPython-3.1.24.tar.gz.asc
Summary  : GitPython is a python library used to interact with Git repositories
Group    : Development/Tools
License  : BSD-3-Clause
Requires: GitPython-license = %{version}-%{release}
Requires: GitPython-python = %{version}-%{release}
Requires: GitPython-python3 = %{version}-%{release}
Requires: gitdb
BuildRequires : buildreq-distutils3
BuildRequires : gitdb

%description
![Python package](https://github.com/gitpython-developers/GitPython/workflows/Python%20package/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/gitpython/badge/?version=stable)](https://readthedocs.org/projects/gitpython/?badge=stable)
[![Packaging status](https://repology.org/badge/tiny-repos/python:gitpython.svg)](https://repology.org/metapackage/python:gitpython/versions)

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
%setup -q -n GitPython-3.1.24
cd %{_builddir}/GitPython-3.1.24

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632179088
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
cp %{_builddir}/GitPython-3.1.24/LICENSE %{buildroot}/usr/share/package-licenses/GitPython/98a91252d682790e518df3df5c68339d17ab7e47
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
