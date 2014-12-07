%define major	3
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	A library used to create PNG, JPEG, or WBMP images
Name:		gd
Version:	2.1.0
Release:	4
License:	BSD-style
Group:		System/Libraries
Url:		http://libgd.bitbucket.org/
Source0:	http://cdn.bitbucket.org/libgd/gd-libgd/downloads/libgd-%{version}.tar.xz
Patch0:		gd-2.1.0-automake.patch
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(zlib)

%description
gd is a graphics library. It allows your code to quickly draw images complete
with lines, arcs, text, multiple colors, cut and paste from other images, and
flood fills, and write out the result as a PNG or JPEG file. This is
particularly useful in World Wide Webapplications, where PNG and JPEG are two
of the formats accepted for inlineimages by most browsers.

gd is not a paint program. If you are looking for a paint program, you are
looking in the wrong place. If you are not a programmer, you are looking in the
wrong place. 

gd does not provide for every possible desirable graphics operation. It is not
necessary or desirable for gd to become a kitchen-sink graphics package, but
version 1.7.3 incorporates most of the commonly requested features for an 8-bit
2D package.

%package -n	%{libname}
Summary:	A library used to create PNG, JPEG, or WBMP images
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
This package contains the library needed to run programs dynamically linked
with libgd.

%package -n	%{devname}
Summary:	The development libraries and header files for gd
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
These are the development libraries and header files for gd, the .png and .jpeg
graphics library. If you're installing the gd graphics library, you'll probably
want to install gd-devel.

%package	utils
Requires:	%{libname} = %{version}
Summary:	The Utils files for gd
Group:		System/Libraries

%description	utils
gd is a graphics library. It allows your code to quickly draw images complete
with lines, arcs, text, multiple colors, cut and paste from other images, and
flood fills, and write out the result as a PNG or JPEG file. This is
particularly useful in World Wide Webapplications, where PNG and JPEG are two
of the formats accepted for inlineimages by most browsers.

gd is not a paint program. If you are looking for a paint program, you are
looking in the wrong place. If you are not a programmer, you are looking in the
wrong place. 

gd does not provide for every possible desirable graphics operation. It is not
necessary or desirable for gd to become a kitchen-sink graphics package, but
version 1.7.3 incorporates most of the commonly requested features for an 8-bit
2D package.

This package contains various utilities utilizing the gd library.

%prep
%setup -q -n libgd-%{version}
%apply_patches

sed -i -e 's,AM_PROG_CC_STDC,AC_PROG_CC,g' configure.*
libtoolize --force --copy
autoreconf -fi

%build
%configure2_5x \
	--disable-static

%make 

%install
%makeinstall_std

sed -i -e 's!-Wl,--as-needed!!' -e 's!-Wl,--no-undefined!!' %{buildroot}%{_bindir}/gdlib-config

%multiarch_binaries %{buildroot}%{_bindir}/gdlib-config

%multiarch_includes %{buildroot}%{_includedir}/gd.h

install -m0644 src/gdhelpers.h %{buildroot}%{_includedir}/

%files -n %{libname}
%{_libdir}/libgd.so.%{major}*

%files -n %{devname}
%{_bindir}/gdlib-config
%{multiarch_bindir}/gdlib-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h
%{multiarch_includedir}/*.h

%files utils
%{_bindir}/annotate
%{_bindir}/bdftogd
%{_bindir}/gd2copypal
%{_bindir}/gd2topng
%{_bindir}/gdparttopng
%{_bindir}/gdtopng
%{_bindir}/pngtogd
%{_bindir}/pngtogd2
%{_bindir}/webpng
%{_bindir}/gd2togif
%{_bindir}/gdcmpgif
%{_bindir}/giftogd2

