Name:           kamoso
Summary:        Application to take pictures and videos out of your webcam
Version:        2.0.2
Release:        2
License:        GPLv2+
Url:            http://www.kde-apps.org/content/show.php/Kamoso?content=111750
Group:          Graphical desktop/KDE
BuildRequires:  kdelibs4-devel
BuildRequires:  qt-gstreamer-devel
BuildRequires:	kdegraphics4-devel
BuildRequires:	boost-devel
Requires:	qt-gstreamer
Source:         http://fr2.rpmfind.net/linux/KDE/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		kamoso-2.0.2-l10n-ru.patch

%description
Kamoso is an application to take pictures and videos out of your webcam.

%files -f %name.lang
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*.so
%{_kde_applicationsdir}/kamoso.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p 1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %name
