Name: x11-driver-video-r128
Version: 6.8.0
Release: %mkrel 1
Epoch: 1
Summary: X.org driver for ATI Rage 128
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-r128-%{version}.tar.bz2

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-r128 is the X.org driver for ATI Rage 128.


%prep
%setup -q -n xf86-video-r128-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/r128_drv.la
%{_libdir}/xorg/modules/drivers/r128_drv.so
%{_mandir}/man4/r128.*
