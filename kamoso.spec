%define snapshot 20150331

Name:		kamoso
Summary:	Application to take pictures and videos out of your webcam
Version:	2.0.2
Release:	8.%{snapshot}.3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://launchpad.net/kamoso
#git archive --format=tar --prefix=kamoso-2.0.2-$(date +%Y%m%d)/ HEAD | xz -vf > kamoso-2.0.2-$(date +%Y%m%d).tar.x
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}-%{snapshot}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(QtGStreamer-1.0)
BuildRequires:	pkgconfig(libkipi)
Requires:	qt-gstreamer
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-bad

%description
Kamoso is an application to take pictures and videos out of your webcam.

%files
%doc %{_docdir}/HTML/*/kamoso
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*.so
%{_kde_applicationsdir}/kamoso.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop

#--------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}-%{snapshot}


%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

