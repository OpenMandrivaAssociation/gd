# gd is used by libgphoto, libgphoto is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 3
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define lib32name %mklib32name %{name} %{major}
%define dev32name %mklib32name %{name} -d

Summary:	A library used to create PNG, JPEG, or WBMP images
Name:		gd
Version:	2.3.3
Release:	1
License:	BSD-style
Group:		System/Libraries
Url:		http://libgd.org/
Source0:	https://github.com/libgd/libgd/releases/download/gd-%{version}/libgd-%{version}.tar.xz
Patch0:		https://src.fedoraproject.org/rpms/gd/raw/rawhide/f/libgd-flip.patch
Patch1:		https://src.fedoraproject.org/rpms/gd/raw/rawhide/f/libgd-iostream.patch

BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libwebp)
%if %{with compat32}
BuildRequires:	devel(libintl)
BuildRequires:	devel(libjpeg)
BuildRequires:	devel(libfontconfig)
BuildRequires:	devel(libfreetype)
BuildRequires:	devel(libpng16)
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXpm)
BuildRequires:	devel(libz)
BuildRequires:	devel(libtiff)
BuildRequires:	devel(libwebp)
%endif

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

%package -n %{libname}
Summary:	A library used to create PNG, JPEG, or WBMP images
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically linked
with libgd.

%package -n %{devname}
Summary:	The development libraries and header files for gd
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig(libjpeg)
Requires:	pkgconfig(fontconfig)
Requires:	pkgconfig(freetype2)
Requires:	pkgconfig(libpng)
Requires:	pkgconfig(x11)
Requires:	pkgconfig(xpm)
Requires:	pkgconfig(zlib)
Requires:	pkgconfig(libtiff-4)
Requires:	pkgconfig(libwebp)
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
These are the development libraries and header files for gd, the .png and .jpeg
graphics library. If you're installing the gd graphics library, you'll probably
want to install gd-devel.

%package utils
Requires:	%{libname} = %{version}
Summary:	The Utils files for gd
Group:		System/Libraries

%description utils
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

%if %{with compat32}
%package -n %{lib32name}
Summary:	A library used to create PNG, JPEG, or WBMP images (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
This package contains the library needed to run programs dynamically linked
with libgd.

%package -n %{dev32name}
Summary:	The development libraries and header files for gd (32-bit)
Group:		Development/C
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}

%description -n %{dev32name}
These are the development libraries and header files for gd, the .png and .jpeg
graphics library. If you're installing the gd graphics library, you'll probably
want to install gd-devel.
%endif

%prep
%autosetup -n libgd-%{version} -p1

sed -i -e 's,AM_PROG_CC_STDC,AC_PROG_CC,g' configure.*
libtoolize --force --copy
autoreconf -fi

export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
#ln -s ../config .
%configure32 --disable-static
cd ..
%endif

mkdir build
cd build
#ln -s ../config .
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

install -m0644 src/gdhelpers.h %{buildroot}%{_includedir}/

%files -n %{libname}
%{_libdir}/libgd.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h

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

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libgd.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/*.pc
%endif
