%bcond_with check
Name:          deepin-turbo
Version:       0.0.3
Release:       2
Summary:       deepin-trubo is a deepin project that derives from Applauncherd.

License:       GPLv3
URL:           https://uos-packages.deepin.com/uos/pool/main/d/deepin-turbo/
Source0:       %{name}-%{version}.orig.tar.xz

Patch0:	       0001-Modify-program-path.patch 

BuildRequires: cmake
BuildRequires: qt5-qtbase-devel
BuildRequires: dbus-devel
BuildRequires: systemd-devel

%description
deepin-trubo is a deepin project that derives from Applauncherd.

%package devel
Summary:    %{summary}
%description devel

%prep
%autosetup -p1

%build
cmake .
make

%install
%make_install
mkdir -p %{?buildroot}%{_libdir}
mkdir -p %{?buildroot}%{_bindir}
mkdir -p %{?buildroot}%{_includedir}
mv %{?buildroot}/usr/local/lib/* %{?buildroot}%{_libdir}/
mv %{?buildroot}/usr/local/bin/* %{?buildroot}%{_bindir}/
mv %{?buildroot}/usr/local/include/%{name}/ %{?buildroot}%{_includedir}/

%files
%{_libdir}/*.so
%{_bindir}/*
/usr/lib/systemd/user/deepin-turbo-booster-dtkwidget.service
%{_libdir}/deepin-turbo/booster-dtkwidget
%doc README.md

%files devel
%{_libdir}/*.so
%{_bindir}/*
%{_includedir}/*
%doc README.md


%changelog
* Mon Jun 07 2021 weidong <weidong@uniontech.com> - 0.0.3-2
- Modify program path

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 0.0.3-1
- Package init
