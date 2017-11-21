%define _disable_ld_no_undefined 1

Summary:	X.org driver for ATI Rage 128
Name:		x11-driver-video-r128
Epoch:		1
Version:	6.10.2
Release:	1
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-r128-%{version}.tar.bz2
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-r128 is the X.org driver for ATI Rage 128.

%prep
%setup -qn xf86-video-r128-%{version}
[ -e autogen.sh ] && ./autogen.sh

%build
export CC=gcc
export CXX=g++

%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/r128_drv.so
%{_mandir}/man4/r128.*

