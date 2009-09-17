Name:           kamoso
Summary:        Application to take pictures and videos out of your webcam
Version:        1.0
Release:        %mkrel 1
License:        GPL v2 or later
Url:            http://www.kde-apps.org/content/show.php/Kamoso?content=111750
Group:          Graphical desktop/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  kdelibs4-devel
BuildRequires:  vlc-devel
BuildRequires:  kdebase4-workspace-devel
Source:         111750-kamoso-dali.tar.bz2
Patch0:         kamoso-fix-build.patch

%description
Kamoso is an application to take pictures and videos out of your webcam.

%files
%defattr(-,root,root)
%_kde_bindir/kamoso
%_kde_libdir/kde4/*
%_kde_libdir/libkamosoplugin.so
%_kde_datadir/applications/kde4/kamoso.desktop
%_kde_appsdir/kamoso_facebook
%_kde_appsdir/kamoso_youtube
%_kde_iconsdir/hicolor/*/apps/kamoso.*
%_kde_datadir/kde4/services/execute.desktop
%_kde_datadir/kde4/services/facebooksender.desktop
%_kde_datadir/kde4/services/trash.desktop
%_kde_datadir/kde4/services/youtube.desktop
%_kde_datadir/kde4/servicetypes/kamosoplugin.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %name
%patch0 -p1

%build
%cmake_kde4

%install
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT
