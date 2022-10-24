#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pylint
Version  : 2.15.5
Release  : 145
URL      : https://files.pythonhosted.org/packages/4e/9d/fa68dd17140373786c5a379f6b313ceeb324dfe47ff13f717710c2e63c1d/pylint-2.15.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/4e/9d/fa68dd17140373786c5a379f6b313ceeb324dfe47ff13f717710c2e63c1d/pylint-2.15.5.tar.gz
Summary  : python code static checker
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: pypi-pylint-bin = %{version}-%{release}
Requires: pypi-pylint-license = %{version}-%{release}
Requires: pypi-pylint-python = %{version}-%{release}
Requires: pypi-pylint-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(astroid)
BuildRequires : pypi(dill)
BuildRequires : pypi(isort)
BuildRequires : pypi(mccabe)
BuildRequires : pypi(platformdirs)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(tomlkit)
BuildRequires : pypi(wheel)

%description
`Pylint`_
=========
.. _`Pylint`: https://pylint.pycqa.org/
.. This is used inside the doc to recover the start of the introduction

%package bin
Summary: bin components for the pypi-pylint package.
Group: Binaries
Requires: pypi-pylint-license = %{version}-%{release}

%description bin
bin components for the pypi-pylint package.


%package license
Summary: license components for the pypi-pylint package.
Group: Default

%description license
license components for the pypi-pylint package.


%package python
Summary: python components for the pypi-pylint package.
Group: Default
Requires: pypi-pylint-python3 = %{version}-%{release}

%description python
python components for the pypi-pylint package.


%package python3
Summary: python3 components for the pypi-pylint package.
Group: Default
Requires: python3-core
Provides: pypi(pylint)
Requires: pypi(astroid)
Requires: pypi(dill)
Requires: pypi(isort)
Requires: pypi(mccabe)
Requires: pypi(platformdirs)
Requires: pypi(tomli)
Requires: pypi(tomlkit)

%description python3
python3 components for the pypi-pylint package.


%prep
%setup -q -n pylint-2.15.5
cd %{_builddir}/pylint-2.15.5
pushd ..
cp -a pylint-2.15.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666631031
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . astroid
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . astroid
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pylint
cp %{_builddir}/pylint-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pylint/909b58c9b803acb8d063ac6b2147e56afc8055f6 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} astroid
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/epylint
/usr/bin/pylint
/usr/bin/pylint-config
/usr/bin/pyreverse
/usr/bin/symilar

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pylint/909b58c9b803acb8d063ac6b2147e56afc8055f6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
