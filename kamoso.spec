%define snapshot 20150331

Name:		kamoso
Summary:	Application to take pictures and videos out of your webcam
Version:	2.0.2
Release:	9.%{snapshot}.1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://launchpad.net/kamoso
#git archive --format=tar --prefix=kamoso-2.0.2-$(date +%Y%m%d)/ HEAD | xz -vf > kamoso-2.0.2-$(date +%Y%m%d).tar.x
Source:		ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}-%{snapshot}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(QtGStreamer-1.0)
BuildRequires:	pkgconfig(libkipi)
Requires:	qt-gstreamer

%description
Kamoso is an application to take pictures and videos out of your webcam.

%files -f %{name}.lang
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*.so
%{_kde_applicationsdir}/kamoso.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop

#--------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}-%{snapshot}

# rename some icons that conflict with kdeplasma-addons
# upstreamed,
# http://commits.kde.org/kamoso/b8b03322d58a920deac198c2360d65deddccd610
pushd src/plugins/youtube
sed -i.bak -e 's|^Icon=youtube|Icon=kipiplugin_youtube|' *.desktop
for icon in icons/*-action-youtube.* ; do
  new_name=$(echo ${icon} | sed -e's|-youtube|-kipiplugin_youtube|')
  mv ${icon} ${new_name}
done

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

