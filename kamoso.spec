Name:           kamoso
Summary:        Application to take pictures and videos out of your webcam
Version:        2.0
Release:        %mkrel 1
License:        GPL v2 or later
Url:            http://www.kde-apps.org/content/show.php/Kamoso?content=111750
Group:          Graphical desktop/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  kdelibs4-devel
BuildRequires:  qt-gstreamer-devel
BuildRequires:	kdegraphics4-devel
BuildRequires:	boost-devel
Requires:	qt-gstreamer
Source:         http://fr2.rpmfind.net/linux/KDE/stable/%{name}/%{version}/src/%{name}-%{version}-final.tar.bz2

%description
Kamoso is an application to take pictures and videos out of your webcam.

%files -f %name.lang
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*.so
%{_kde_applicationsdir}/kamoso.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version-final

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
