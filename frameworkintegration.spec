%define major 5
%define libname %mklibname KF5Style %{major}
%define devname %mklibname KF5Style -d
%define debug_package %{nil}

Name: frameworkintegration
Version: 5.1.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: Workspace and cross-framework integration plugins
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(XCB)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(OxygenFont)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
Workspace and cross-framework integration plugins

%package -n %{libname}
Summary: Workspace and cross-framework integration plugins
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Workspace and cross-framework integration plugins

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Style library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Style library

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_datadir}/kf5/infopage
%{_libdir}/plugins/kf5/FrameworkIntegrationPlugin.so
%{_libdir}/plugins/platformthemes/KDEPlatformTheme.so

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
