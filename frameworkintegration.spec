%define major 5
%define libname %mklibname KF5Style %{major}
%define devname %mklibname KF5Style -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: frameworkintegration
Version:	5.110.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Workspace and cross-framework integration plugins
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xext)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5Package)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(packagekitqt5)
BuildRequires: (cmake(AppStreamQt) >= 0.10.4 with cmake(AppStreamQt) < 0.90.0)
Requires: %{libname} = %{EVRD}

%description
Workspace and cross-framework integration plugins.

%package -n %{libname}
Summary: Workspace and cross-framework integration plugins
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Workspace and cross-framework integration plugins.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Style library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Style library.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_libdir}/libexec/kf5/kpackagehandlers/knshandler
%{_datadir}/kf5/infopage
%{_datadir}/knotifications5/plasma_workspace.notifyrc
%{_libdir}/qt5/plugins/kf5/FrameworkIntegrationPlugin.so
%{_libdir}/libexec/kf5/kpackagehandlers/appstreamhandler

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
