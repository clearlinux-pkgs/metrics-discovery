#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : metrics-discovery
Version  : 1.5.108
Release  : 4
URL      : https://github.com/intel/metrics-discovery/archive/metrics-discovery-1.5.108/metrics-discovery-1.5.108.tar.gz
Source0  : https://github.com/intel/metrics-discovery/archive/metrics-discovery-1.5.108/metrics-discovery-1.5.108.tar.gz
Summary  : This software is a user mode library that provides access to GPU performance data.
Group    : Development/Tools
License  : MIT
Requires: metrics-discovery-lib = %{version}-%{release}
Requires: metrics-discovery-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev

%description
# Intel(R) Metrics Discovery Application Programming Interface
## Introduction
This software is a user mode library that provides access to GPU performance data.

%package dev
Summary: dev components for the metrics-discovery package.
Group: Development
Requires: metrics-discovery-lib = %{version}-%{release}
Provides: metrics-discovery-devel = %{version}-%{release}
Requires: metrics-discovery = %{version}-%{release}

%description dev
dev components for the metrics-discovery package.


%package lib
Summary: lib components for the metrics-discovery package.
Group: Libraries
Requires: metrics-discovery-license = %{version}-%{release}

%description lib
lib components for the metrics-discovery package.


%package license
Summary: license components for the metrics-discovery package.
Group: Default

%description license
license components for the metrics-discovery package.


%prep
%setup -q -n metrics-discovery-metrics-discovery-1.5.108
cd %{_builddir}/metrics-discovery-metrics-discovery-1.5.108

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579208201
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DMD_PLATFORM=linux -DMD_BUILD_TYPE=release
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1579208201
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/metrics-discovery
cp %{_builddir}/metrics-discovery-metrics-discovery-1.5.108/LICENSE.md %{buildroot}/usr/share/package-licenses/metrics-discovery/24ebc22b6e51adf8b01ec0340b69fc7dd2178c1d
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/mdapi/metrics_discovery_api.h
/usr/lib64/libmd.so
/usr/lib64/pkgconfig/libmd.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmd.so.1
/usr/lib64/libmd.so.1.5.108

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/metrics-discovery/24ebc22b6e51adf8b01ec0340b69fc7dd2178c1d
