%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticdevelname %mklibname %{name} -d -s

Summary:	A library used to create PNG, JPEG, or WBMP images
Name:		gd
Version:	2.0.35
Release:	%mkrel 3
License:	BSD-style
Source0:	http://www.libgd.org/releases/%{name}-%{version}.tar.bz2
Group:		System/Libraries
URL:		http://www.libgd.org/
#It uses freetype2-devel, but uses the old library for gdttf
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	freetype2-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	X11-devel
BuildRequires:	xpm-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

This package contains the library needed to run programs dynamically linked
with libgd.

%package -n	%{develname}
Summary:	The development libraries and header files for gd
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel
Provides:	%{mklibname %{name} 2 -d} = %{version}-%{release}
Obsoletes:	%{mklibname %{name} 2 -d}

%description -n	%{develname}
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

These are the development libraries and header files for gd, the .png and .jpeg
graphics library. If you're installing the gd graphics library, you'll probably
want to install gd-devel.

%package -n	%{staticdevelname}
Summary:	Static GD library
Group:		Development/C
Requires:	%{develname} = %{version}
Provides:	lib%{name}-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Provides:	%{mklibname %{name} 2 -d -s} = %{version}-%{release}
Obsoletes:	%{mklibname %{name} 2 -d -s}

%description -n	%{staticdevelname}
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

This package contains static gd library.

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

%setup -q -n gd-%{version}

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal-1.7; automake-1.7 --copy --add-missing; autoconf

%configure2_5x

%make 

%install
rm -rf %{buildroot} 

%makeinstall

%multiarch_binaries %{buildroot} %{_bindir}/gdlib-config
%multiarch_includes %{buildroot} %{_includedir}/gd.h

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot} 

%files -n %{libname}
%defattr(-,root,root)
%doc README.TXT index.html
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/gdlib-config
%multiarch %{multiarch_bindir}/gdlib-config
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*.h
%multiarch %{multiarch_includedir}/*.h

%files -n %{staticdevelname}
%defattr(-,root,root)
%{_libdir}/lib*.a

%files utils
%defattr(-,root,root)
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
