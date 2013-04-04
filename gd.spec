%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticdevelname %mklibname %{name} -d -s

Summary:	A library used to create PNG, JPEG, or WBMP images
Name:		gd
Version:	2.0.35
Release:	21
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
Provides:	%{libname} = %{version}-%{release}

%description -n	%{libname}
This package contains the library needed to run programs dynamically linked
with libgd.

%package -n	%{develname}
Summary:	The development libraries and header files for gd
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

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

chmod a+r *.c *.h

%build
sed -i -e 's,AM_PROG_CC_STDC,AC_PROG_CC,g' configure.*
libtoolize --force --copy
autoreconf -fi
%configure2_5x \
	--disable-static

%make 

%install
%makeinstall

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


%changelog
* Sat Nov 26 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.0.35-20
+ Revision: 733641
- fixed file list
- rebuild
- cleaned up spec
- removed .la files
- removed defattr
- disabled static build & pkg
- removed clean section
- removed old ldconfig scriptlets
- shortened descriptsion for lib & devel pkgs
- converted BRs to pkgconfig provides
- removed mkrel & BuildRoot

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0.35-19
+ Revision: 720154
- Rebuild with newer libpng

* Mon Sep 12 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.35-18
+ Revision: 699510
- rebuild for new libpng-1.5

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.35-17
+ Revision: 661899
- stupid macros
- multiarch fixes

* Fri Mar 04 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0.35-16
+ Revision: 641570
- Rebuild with jpeg turbo

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.35-15mdv2011.0
+ Revision: 605442
- rebuild

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.35-14mdv2010.1
+ Revision: 488755
- rebuilt against libjpeg v8

* Tue Oct 20 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.35-13mdv2010.0
+ Revision: 458378
- P3: security fix for CVE-2009-3546

* Wed Oct 07 2009 Thierry Vignaud <tv@mandriva.org> 2.0.35-12mdv2010.0
+ Revision: 455478
- move huge unreadable doc in devel package and make it readable

* Tue Oct 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.35-11mdv2010.0
+ Revision: 455256
- add two patches from Debian, backported from upstream CVS (should fix #34829)

* Thu Sep 24 2009 Olivier Blin <blino@mandriva.org> 2.0.35-10mdv2010.0
+ Revision: 448379
- use smaller build deps (from Arnaud Patard, change taken in fedora cvs)

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.35-9mdv2010.0
+ Revision: 416514
- rebuilt against libjpeg v7

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.35-8mdv2009.1
+ Revision: 316589
- fix build with -Werror=format-security (P0)

* Fri Nov 07 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.35-7mdv2009.1
+ Revision: 300707
- rebuilt against new libxcb

* Mon Sep 01 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.35-6mdv2009.0
+ Revision: 278488
- add missing header (needed by php-5.3.x)

* Wed Jul 02 2008 Pixel <pixel@mandriva.com> 2.0.35-5mdv2009.0
+ Revision: 230660
- remove --no-undefined and --as-needed from "gdlib-config --ldflags"

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.0.35-4mdv2009.0
+ Revision: 221042
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Feb 28 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.35-3mdv2008.1
+ Revision: 176225
- remove white noise (very funny!)
- fix devel package naming
- fix descriptions

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.0.35-2mdv2008.1
+ Revision: 150096
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jun 22 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0.35-1mdv2008.0
+ Revision: 42898
- 2.0.35


* Mon Feb 12 2007 Stew Benedict <sbenedict@mandriva.com> 2.0.34-1mdv2007.0
+ Revision: 120041
- 2.0.34
  drop P0-P2, merged upstream
  new URL

* Wed Feb 07 2007 Stew Benedict <sbenedict@mandriva.com> 2.0.33-7mdv2007.1
+ Revision: 116953
- yeah, add the patch too, love this build system
- P2: security fix for CVE-2007-0455

* Tue Oct 31 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.33-6mdv2007.1
+ Revision: 74670
- bunzip patches
- Import gd

* Tue Jun 27 2006 Stew Benedict <sbenedict@mandriva.com> 2.0.33-5mdv2006.0
- P1: security fix for CVE-2006-2096

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.0.33-4mdk
- Rebuild

* Mon Jan 31 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.0.33-3mdk
- some more multiarch support

* Mon Jan 31 2005 Stew Benedict <sbenedict@mandrakesoft.com> 2.0.33-2mdk
- multiarch support, remove "dot" from summaries

* Thu Nov 11 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.0.33-1mdk
- 2.0.33, still missing an overflow check - patched (patch0)

* Mon Nov 08 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.0.32-1mdk
- 2.0.32, conditional gif options go away

* Sat Oct 23 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.0.28-1mdk
- 2.0.28

* Mon Jul 26 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.0.27-3mdk
- add BuildRequires: gettext-devel

* Wed Jul 21 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.27-2mdk
- add conditional gif support (not enabled per default)
- spec file cleanups

* Tue Jul 06 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.27-1mdk
- 2.0.27

* Thu Jun 10 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.0.26-1mdk
- 2.0.26

* Sun Apr 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0.22-1mdk
- 2.0.22
- fix buildrequires
- spec cosmetics

