Name:		kamoso
Summary:	Application to take pictures and videos out of your webcam
Version:	3.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://launchpad.net/kamoso
Source:		http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(Qt5GStreamer-1.0)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5OpenGL)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KDEExperimentalPurpose)

Requires:	qt-gstreamer
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-bad

%description
Kamoso is an application to take pictures and videos out of your webcam.

%files -f %{name}.lang
%doc %{_docdir}/HTML/*/kamoso
%{_kde5_bindir}/*
%{_datadir}/applications/org.kde.kamoso.desktop
%{_kde5_iconsdir}/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q


%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name}

