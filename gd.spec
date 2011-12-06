%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	A library used to create PNG, JPEG, or WBMP images
Name:		gd
Version:	2.0.35
Release:	20
License:	BSD-style
Group:		System/Libraries
URL:		http://www.libgd.org/
Source0:	http://www.libgd.org/releases/%{name}-%{version}.tar.bz2
Patch0:		gd-2.0.35-format_not_a_string_literal_and_no_format_arguments.diff
Patch1:		0001_cvs20070904.patch
Patch2:		0002_cvs20070916.patch
Patch3:		gd-2.0.35-CVE-2009-3546.diff
#It uses freetype2-devel, but uses the old library for gdttf
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:  pkgconfig(fontconfig)
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
Provides:	%{libname} = %{version}-%{release}
Obsoletes:	%name

%description -n	%{libname}
This package contains the library needed to run programs dynamically linked
with libgd.

%package -n	%{develname}
Summary:	The development libraries and header files for gd
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel
Provides:	%{mklibname %{name} 2 -d} = %{version}-%{release}
Obsoletes:	%{mklibname %{name} 2 -d}

%description -n	%{develname}
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

%setup -q
%patch0 -p0 -b .format_not_a_string_literal_and_no_format_arguments
%patch1 -p1 -b .cvs20070904
%patch2 -p1 -b .cvs20070916
%patch3 -p0 -b .CVE-2009-3546

%build
autoreconf -fi
%configure2_5x \
	--disable-static

%make 

%install
rm -rf %{buildroot} 
%makeinstall
find %{buildroot} -name "*.la" -exec rm -rf {} \;

sed -i -e 's!-Wl,--as-needed!!' -e 's!-Wl,--no-undefined!!' %{buildroot}%{_bindir}/gdlib-config

%multiarch_binaries %{buildroot}%{_bindir}/gdlib-config

%multiarch_includes %{buildroot}%{_includedir}/gd.h

install -m0644 gdhelpers.h %{buildroot}%{_includedir}/

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%attr(644,root,root) %doc index.html
%{_bindir}/gdlib-config
%{multiarch_bindir}/gdlib-config
%{_libdir}/*.so
%{_includedir}/*.h
%{multiarch_includedir}/*.h

%files utils
%doc README.TXT
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
