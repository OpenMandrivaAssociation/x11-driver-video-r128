%define _disable_ld_no_undefined 1

Summary:	X.org driver for ATI Rage 128
Name:		x11-driver-video-r128
Epoch:		1
Version:	6.13.0
Release:	1
Group:		System/X11
License:	MIT
URL:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-r128-%{version}.tar.xz
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-r128 is the X.org driver for ATI Rage 128.

%prep
%autosetup -n xf86-video-r128-%{version} -p1

%build
export CC=gcc
export CXX=g++

%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/drivers/r128_drv.so
%doc %{_mandir}/man4/r128.*

