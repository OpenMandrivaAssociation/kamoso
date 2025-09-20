%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Name:		kamoso
Summary:	Application to take pictures and videos out of your webcam
Version:	25.08.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://userbase.kde.org/Kamoso
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/kamoso-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Purpose)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-video-1.0)
BuildRequires:	clang-tools
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Kamoso is an application to take pictures and videos out of your webcam.

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/applications/org.kde.kamoso.desktop
%{_datadir}/metainfo/org.kde.kamoso.appdata.xml
%{_datadir}/icons/*/*/*/*
%{_datadir}/knotifications6/kamoso.notifyrc
