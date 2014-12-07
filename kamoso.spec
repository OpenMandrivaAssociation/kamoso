Name:		kamoso
Summary:	Application to take pictures and videos out of your webcam
Version:	2.0.2
Release:	8
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://launchpad.net/kamoso
Source:		ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
## upstream patches
Patch105:	0005-Make-the-About-dialog-work.patch
Patch121:	0021-add-include.patch
Patch131:	0031-Store-and-install-kamoso.desktop-with-755-permission.patch
Patch132:	0032-use-camera-web-icon-instead-of-webcamreceive.patch
Patch133:	0033-initial-port-to-libkipi-2.x.patch
Patch134:	0034-add-license-header.patch
Patch135:	0035-fix-build-for-libkipi-2.patch
Patch136:	kamoso-2.0.2-gstreamer1.patch
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
%setup -q
%patch105 -p1 -b .0005
%patch121 -p1 -b .0021
%patch131 -p1 -b .0031
%patch132 -p1 -b .0032
%patch133 -p1 -b .0033
%patch134 -p1 -b .0034
%patch135 -p1 -b .0035
%patch136 -p1 -b .gst1

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

