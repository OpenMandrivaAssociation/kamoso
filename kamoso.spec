%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		kamoso
Summary:	Application to take pictures and videos out of your webcam
Version:	21.08.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://userbase.kde.org/Kamoso
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/kamoso-%{version}.tar.xz
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
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	qt5-qtgraphicaleffects
BuildRequires:	qt5-qtquickcontrols
Requires:	purpose
Requires:	kirigami
Requires:	qt5-gstreamer
Requires:	qt5-qtgraphicaleffects
Requires:	qt5-qtquickcontrols
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
%ifnarch %{arm}
# No gstreamer-plugins-bad on ARM32 so far...
Requires:	gstreamer1.0-plugins-bad
%endif

%description
Kamoso is an application to take pictures and videos out of your webcam.

%files -f %{name}.lang
%doc %{_docdir}/HTML/*/kamoso
%{_kde5_bindir}/*
%{_datadir}/applications/org.kde.kamoso.desktop
%{_datadir}/metainfo/org.kde.kamoso.appdata.xml
%{_libdir}/gstreamer-1.0/gstkamosoqt5videosink.so
%{_kde5_iconsdir}/*/*/*/*
%{_datadir}/knotifications5/kamoso.notifyrc
%{_datadir}/sounds/kamoso-shutter.wav

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C  build

%install
%ninja_install -C build

%find_lang %{name}
