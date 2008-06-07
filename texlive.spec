# This spec file is based on texjive project created by Michael A. Peters.
# Adopted and modified for Fedora by Jindrich Novy.

%define texlive_ver	2007
%define ptex_src_ver	3.1.10
%define pdvipsk_ver	p1.7a
%define mendexk_ver	2.6e

%define desktop_file_utils_version 0.9
%define default_letter_paper 0
# lcdf typetools can be easily built as a separate tool, so it should be
%define disable_lcdf_typetools 1

# These need to match what is in the texlive-texmf package.
#  since texlive-texmf is a BuildRequires, it installs an rpm macro
#  file that defines them. Change the definitions in the texlive-texmf.spec
#  file and rebuild it if you do not like where things get put.
%{!?_texmf_main:%define _texmf_main %{_datadir}/texmf}
%{!?_texmf_conf:%define _texmf_conf %{_sysconfdir}/texmf}
%{!?_texmf_var:%define _texmf_var %{_var}/lib/texmf}

Summary:	Binaries for the TeX formatting system
Name:		texlive
Version:	%{texlive_ver}
Release:	31%{?dist}

License:	GPLv2 and BSD and Public Domain and LGPLv2+ and GPLv2+ and LPPL
Group:		Applications/Publishing
URL:		http://tug.org/texlive/

#####
# Source0-99: main sources
#####
#Source0:	http://tug.org/svn/texlive/branches/branch2007/Master/source/source.tar.bz2
# non free source files removed with texlive-generate-tarball.sh
Source0:	source-free.tar.bz2

Source10:	%{name}.cron
# Filter out bad requirements (RH bug #59819).
Source99:	%{name}-filter-requires.sh
Source100:	%{name}-generate-tarball.sh
%define __perl_requires %{SOURCE99}
# 1000-: Japanese pTeX
Source1000:	ftp://ftp.ascii.co.jp/pub/TeX/ascii-ptex/tetex/ptex-src-%{ptex_src_ver}.tar.gz
Source1001:	ftp://ftp.ascii.co.jp/pub/TeX/ascii-ptex/dvips/dvipsk-jpatch-%{pdvipsk_ver}.tar.bz2
Source1002:	ftp://ftp.ascii.co.jp/pub/TeX/ascii-ptex/mendex/mendexk%{mendexk_ver}.tar.gz

# Don't run brp-python-bytecompile
%define __os_install_post  /usr/lib/rpm/redhat/brp-compress /usr/lib/rpm/redhat/brp-strip %{__strip} /usr/lib/rpm/redhat/brp-strip-static-archive %{__strip} /usr/lib/rpm/redhat/brp-strip-comment-note %{__strip} %{__objdump} %{nil}

######
# Red Hat-specific TeX configuration patches
######

# and sane defaults to build against can be inserted via sed
Patch5:		%{name}-2007-browser.patch
Patch9:		%{name}-teckit.patch

Patch21:	%{name}-more_paths.patch
Patch22:	%{name}-fedora_paths.patch

######
# TeX patches
######

Patch11:	%{name}-2007-makej.patch
Patch12:	%{name}-2007-badscript.patch
Patch17:	%{name}-2007-tmpcleanup.patch
Patch18:	%{name}-fmtutil-infloop.patch
Patch19:	%{name}-2007-kpse-extensions.patch
Patch20:	%{name}-CVE-2007-4033.patch
Patch25:	%{name}-dvipsoverflow.patch
Patch26:	%{name}-dviljktemp.patch
Patch27:	%{name}-poppler.patch
Patch28:	%{name}-man-notetex.patch
Patch29:	%{name}-man-context.patch

######
# mpeters contributed patches
######
# fixes man pages to utf-8
Patch42:	%{name}-2007-copyright-utf8-man.patch
# use proper shellbang
Patch43:	%{name}-2007-epstopdf-shellbang.patch

######
# Debian patches
######
Patch100:	%{name}-Build_script.patch
Patch101:	%{name}-mktexlsr_fixes.patch
Patch102:	%{name}-fix_pkfix_invocation.patch
Patch104:	%{name}-12a_fix_thumbpdf_invocation.patch
Patch105:	%{name}-12b_fix_a2ping_invocation.patch
Patch106:	%{name}-12c_fix_pdfcrop_invocation.patch
Patch107:	%{name}-12d_fix_ebong_invocation.patch
Patch108:	%{name}-12e_fix_vpe_invocation.patch
Patch109:	%{name}-texdoc.patch
Patch114:	%{name}-dvips_fontbug_fix_upstream.patch
Patch115:	%{name}-maketexmf.patch
Patch117:	%{name}-fmtutil_keep_failedlog.patch
Patch119:	%{name}-checklib_fixes.patch
Patch123:	%{name}-fix_makempx_installation.patch

######
# Mandriva patches
######
Patch202:	%{name}-pdftex.patch

######
# Suse patches
######
Patch300:	%{name}-source-icu.patch
Patch301:	%{name}-source-t1lib.patch
Patch302:	%{name}-source-warns.patch
Patch303:	%{name}-source-x11r7.patch
Patch306:	%{name}-source-CVE-2007-0650.patch

# 1000-: Japanese pTeX
Patch1000:	dvipsk-jpatch-pdvips.patch
Patch1004:	%{name}-2007-jp-platex209.patch
Patch1005:	%{name}-2007-pdvips.patch
Patch1006:	%{name}-2007-ptex-3.1.10.patch
Patch1007:	%{name}-2007-fmtutil-ptex.patch

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

BuildRequires:	desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	ed
BuildRequires:	xdg-utils
BuildRequires:	libSM-devel
BuildRequires:	libICE-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	gd-devel
BuildRequires:	t1lib-devel
# for non-modular xorg - use xorg-devel instead of above
BuildRequires:	Xaw3d-devel
BuildRequires:	poppler-devel >= 0.6.2-2
BuildRequires:	teckit-devel
Requires:	texlive-texmf = %{version}
Requires:	texlive-texmf-errata = %{version}
Requires:	texlive-texmf-fonts = %{version}
# make sure fonts package installed before running post - since
# fmtutil-sys is symlink to fmtutil
Requires(post):	%{_bindir}/fmtutil /sbin/restorecon
Requires(preun,postun):	/sbin/restorecon
Provides:	tetex = 3.0-99
Provides:	tetex-fonts = 3.0-99
Provides:	tex(tex)
Provides:	texlive-fonts = %{version}-%{release}
Obsoletes:	tetex < 3.0-99
Obsoletes:	tetex-fonts < 3.0-99
Obsoletes:	texlive-fonts < 2007-6

%description
TeXLive is an implementation of TeX for Linux or UNIX systems. TeX
takes a text file and a set of formatting commands as input and
creates a printable file as output. Usually, TeX is used in
conjunction with a higher level formatting package like LaTeX or
PlainTeX, since TeX by itself is not very user-friendly.

Install texlive if you want to use the TeX text formatting system.
Consider to install texlive-latex (a higher level formatting package
which provides an easier-to-use interface for TeX).

The TeX documentation is located in the texlive-doc package.

%package afm
Summary:	A converter for PostScript(TM) font metric files, for use with TeX
Group:		Applications/Publishing
Requires(post,postun):	/sbin/restorecon
Requires:	texlive-texmf-afm = %{version}
Requires:	texlive-texmf-errata = %{version}
Provides:	tetex-afm = 3.0-99
Obsoletes:	tetex-afm < 3.0-99

%description afm
texlive-afm provides afm2tfm, a converter for PostScript(TM) font
metric files. PostScript fonts are accompanied by .afm font metric
files which describe the characteristics of each font. To use
PostScript fonts with TeX, TeX needs .tfm files that contain similar
information. Afm2tfm will convert .afm files to .tfm files.

If you are installing texlive in order to use the TeX text formatting
system and PostScript files, you will need to install texlive-afm. You
will also need to install texlive-dvips (for converting .dvi files to
PostScript format for printing on PostScript printers), texlive-latex
(a higher level formatting package which provides an easier-to-use
interface for TeX), and xdvi (for previewing .dvi files in X).

The TeX documentation is located in the texlive-doc package.

%package doc
Summary:	Applications to browse documentation for TeXLive
Group:		Applications/Publishing
Requires:	texlive = %{version}-%{release}
Requires:	texlive-texmf-doc = %{version}
Requires:	texlive-texmf-errata-doc = %{version}
Requires:	xdg-utils
Provides:	tetex-doc = 3.0-99
Provides:	texlive-doc = %{version}-%{release}
Obsoletes:	tetex-doc < 3.0-99
Obsoletes:	texlive-doc < 2007-7

%description doc
If you are installing texlive and need a documentation to describe
styles or you are a TeX beginner and need tutorials, you may install
this package to obtain applications allowing you to user-friendly
browse documentation of the TeX formatting system.

%package utils
Summary:	TeXLive utilities using ghostscript and metafont with X support
Group:		Applications/Publishing
Requires:	ghostscript
Requires:	texlive = %{version}-%{release}
Requires:	texlive-dvips = %{version}-%{release}

%description utils
This package contains TeXLive utilities using ghostscript and metafont
with X support.

%package xetex
Summary:	TeX typesetting engine using Unicode with OpenType or AAT support
Group:		Applications/Publishing
Requires(post,postun):	/sbin/restorecon
Requires:	dvipdfmx
Requires:	xdvipdfmx
Requires:	texlive = %{version}-%{release}
Requires:	texlive-texmf-xetex = %{version}

%description xetex
XeTeX is a TeX typesetting engine using Unicode and supporting modern
font technologies such as OpenType or AAT. Initially developed for Mac
OS X only, it is now available for all major platforms. It natively
supports Unicode and the input file is assumed to be in UTF-8 encoding
by default.

%package dvips
Summary:	A DVI to PostScript converter for the TeX text formatting system
Group:		Applications/Publishing
Requires(post,postun):	/sbin/restorecon
Requires:	psutils
Requires:	texlive = %{version}-%{release}
Requires:	texlive-texmf-dvips = %{version}
Requires:	texlive-texmf-errata = %{version}
Provides:	tetex-dvips = 3.0-99
Provides:	tex(dvips)
Obsoletes:	tetex < 3.0-99
Obsoletes:	tetex-dvips < 3.0-99

%description dvips
Dvips converts .dvi files, for example those produced by the TeX text
formatting system, to PostScript(TM) format.

If you are installing texlive, so that you can use the TeX text
formatting system without direct PDF compilation, consider to install
texlive-dvips. In addition, you will need to install texlive-latex (a
higher level formatting package which provides an easier-to-use
interface for TeX), and xdvi (for previewing .dvi files in X).

%package dviutils
Summary:	A collection of utilities for working with dvi files
Group:		Applications/Publishing
# not positive about this requires, pretty sure though
Requires(post,postun):	/sbin/restorecon
Requires:	texlive = %{version}-%{release}
# used to be in tetex, but has a separate upstream
Requires:	dvipng
Requires:	dvipdfm
# some dvi utilities used to be in tetex
Obsoletes:	tetex < 3.0-99

%description dviutils
The texlive-dviutils package includes a set of tools for working with
dvi files. You only need this package if you plan to manipulate
existing dvi files.

%package latex
Summary:	The LaTeX front end for the TeX text formatting system
Group:		Applications/Publishing
Requires:	netpbm-progs
Requires:	texlive = %{version}-%{release}
Requires:	texlive-dvips = %{version}-%{release}
# make sure main and fonts package installed before running post
BuildRequires:	ghostscript
BuildRequires:	netpbm-progs
Requires(post):	%{_bindir}/fmtutil %{_bindir}/fmtutil-sys
Requires(post):	%{_bindir}/texconfig-sys /sbin/install-info
Requires(post,preun,postun):	/sbin/restorecon
Requires:	texlive-texmf-errata = %{version}
Requires:	texlive-texmf-latex = %{version}
Requires:	texlive-utils = %{version}-%{release}
Provides:	tetex-latex = 3.0-99
Provides:	tex(latex)
Obsoletes:	tetex < 3.0-99
Obsoletes:	tetex-latex < 3.0-99

%description latex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX. LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users. It also allows to
compile LaTeX files directly to PDF format.

The TeX documentation is located in the texlive-doc package.

%package east-asian
Summary:	Support for East Asian languages in TeXLive
Group:		Applications/Publishing
Requires(post,postun):	/sbin/restorecon
Requires:	mendexk
Requires:	texlive = %{version}-%{release}
Requires:	texlive-latex = %{version}-%{release}
Requires:	texlive-texmf-dvips = %{version}
Requires:	texlive-texmf-errata-east-asian = %{version}
Provides:	tex(east-asian)
Provides:	tex(japanese)
Provides:	texlive-japanese = %{version}-%{release}
Obsoletes:	texlive-japanese < 2007-20

%description east-asian
East Asian support for TeXLive.

%package context
Summary:	ConTeXt is a document preparation system based on TeX
Group:		Applications/Publishing
Requires(post,postun):	/sbin/restorecon
Requires:	ruby
Requires:	texlive = %{version}-%{release}
Requires:	texlive-texmf-errata-context = %{version}
Provides:	tex(context)

%description context
ConTeXt is a document preparation system based on TeX.

%package -n kpathsea
Summary:	Shared library needed by kpathsea and info files
Group:		Development/Libraries
Requires(post,preun,postun):	/sbin/restorecon
Requires:	texlive = %{version}-%{release}
Obsoletes:	tetex-fonts < 3.0-99

%description -n kpathsea
Shared library needed by kpathsea and info files.

%package -n kpathsea-devel
Summary:	Files needed to build software against kpathsea
Group:		Development/Libraries
Requires:	kpathsea = %{version}-%{release}

%description -n kpathsea-devel
This package includes the kpathsea header files and the libkpathsea.so
symbolic link.

You only need to install this package if you will be compiling
software that wants to link against the kpathsea library.

%package -n mendexk
Summary:	Replacement for makeindex with many enhancements
Version:	%{mendexk_ver}
Group:		Applications/Publishing
#Url: ftp://ftp.ascii.co.jp/pub/TeX/ascii-ptex/mendex/
#Source0: ftp://ftp.ascii.co.jp/pub/TeX/ascii-ptex/mendex/mendexk%{version}.tar.bz2

%description -n mendexk
Replacement for makeindex with many enhancements.

%define version %{texlive_ver}
# without this define, the version is overriden by separated
subpackages # versions

%prep
%setup -q -T -c -a0

# fix for debuginfo rpmlint happiness
chmod -x texk/dvipdfm/macglyphs.h
chmod -x texk/dvipdfm/ttf.c
chmod -x texk/dvipdfm/encodings.c

######
# Red Hat-specific TeX configuration patches
######
# Use htmlview first
%patch5 -p1 -b .browser
%patch9 -p1 -b .teckit
%patch22 -p1 -b .fedora_paths

######
# TeX patches
######

# Fix parallel builds.
%patch11 -p1 -b .makej
# Don't use PID for temporary file names in scripts (RH bug #41269)
%patch12 -p1 -b .badscript
# Always cleanup temporary directories for texconfig, updmap, fmtutil
#  (RH #172534)
%patch17 -p1 -b .tmpcleanup
# fmtutil won't hang in infinite loop (#437008)
%patch18 -p1 -b .infloop
%patch19 -p0 -b .kpse-extensions
%patch20 -p1 -b .CVE-2007-4033
%patch21 -p1 -b .more_paths
%patch25 -p1 -b .dvipsoverflow
%patch26 -p1 -b .dviljktemp
%patch27 -p1 -b .poppler
%patch28 -p1 -b .notetex
%patch29 -p1 -b .man-context

# fix non utf man pages
%patch42 -p1 -b .notutf8-2
# user a proper shellbang
%patch43 -p1 -b .perl

%patch100 -p3
%patch101 -p1 -b .mktexlsr_fixes
%patch102 -p3
%patch104 -p3
%patch105 -p3
%patch106 -p3
%patch107 -p3
%patch108 -p3
%patch109 -p1
%patch114 -p3
%patch115 -p3
%patch117 -p3
%patch119 -p3
%patch123 -p3

%patch202 -p1 -b .pdftex

%patch300 -p0
%patch301 -p0
%patch302 -p0
%patch303 -p0
%patch306 -p0

%patch1007 -p1 -b .ptex

%if %{disable_lcdf_typetools}
pushd utils
rm -rf lcdf-typetools
popd
%endif

## Japanese pTeX
# set platex to Japanese pLaTeX. original one is moved to platex-pl
sed -e s/^platex/platex-pl/g \
    -e s/^pdfplatex/pdfplatex-pl/g \
    -e s/platex\.ini/platex\-pl\.ini/g \
     -i texk/web2c/fmtutil.in

# Prepare pTeX
tar xfz %{SOURCE1000} -C texk/web2c/
cd texk/web2c/ptex-src-%{ptex_src_ver}
sed -i -e  's|/{ptex/{platex,generic,},tex/{latex,generic,}}|/{ptex/platex,{p,}tex/latex,{p,}tex/generic,{p,}tex}|g' -e 's/| uniq//g' mkconf
%patch1004 -p1 -b .fmts
%patch1006 -p1
cd -

# Prepare Japanese dvips
mkdir pdvipsk
tar xfj %{SOURCE1001} -C pdvipsk
cp -lR texk/dvipsk texk/pdvipsk
cd pdvipsk
%patch1005 -p0
cd -
patch -d texk/pdvipsk -p1 < pdvipsk/dvipsk-%{pdvipsk_ver}.patch
%patch1000 -p1 -b .pdvips
ln -s dvips.1 texk/pdvipsk/pdvips.1

# set up mendexk
tar xfz %{SOURCE1002} -C texk


%build
set -x
# define CCACHE_DIR to let the build pass with ccache enabled.
export CCACHE_DIR=$HOME/.ccache
unset TEXINPUTS ||:
unset HOME ||:

%{__rm} -r libs/{teckit,obsdcompat}

# Japanese pTeX
pushd texk
$RPM_BUILD_DIR/%{name}-%{version}/texk/autoconf2.13 -m $RPM_BUILD_DIR/%{name}-%{version}/texk%{_sysconfdir}/autoconf
popd

%configure \
%if %{default_letter_paper}
		--disable-a4 \
%endif
	--enable-shared=yes \
	--with-system-ncurses \
	--with-system-zlib \
	--with-system-pnglib \
	--with-system-gd \
	--without-system-icu \
	--with-icu-include=%{_includedir}/unicode \
	--with-system-freetype \
	--with-freetype-include=/usr/include/freetype \
	--with-system-freetype2 \
	--with-freetype2-include=/usr/include/freetype2 \
	--with-system-t1lib \
	--without-texlive \
	--without-t1utils \
	--without-psutils \
	--without-ps2eps \
	--without-pdfopen \
	--without-ttf2pk \
	--disable-multiplatform \
	--without-dialog --without-texinfo --without-texi2html \
	--without-tex4htk \
	--without-detex --without-dvi2tty \
%if %{disable_lcdf_typetools}
	--with-lcdf-typetools=no \
%endif
	--without-xdvik \
	--with-mf-x-toolkit=yes \
	--without-cxx-runtime-hack \
	--without-dvipng \
	--without-dvipdfm \
	--without-dvipdfmx \
	--without-xdvipdfmx

# Remove everything except:
# icu: includes some changes
# md5: the aladdin md5 code (not a library)
%{__rm} -r libs/{curl,expat,freetype,freetype2,gd,howto,jpeg,libgnuw32,libgsw32,libpng,libttf,ncurses,regex,unzip,zlib,type1,t1lib,xpdf}/

# parallel build fails in libs/icu-xetex/common, build this one sequentially
cd libs/icu-xetex
%{__make}
cd -

# compile the rest parallelly
%{__make} %{?_smp_mflags}

cd texk/web2c/ptex-src-%{ptex_src_ver}
./configure EUC
%{__make}
cd -

# mendexk build
cd texk/mendexk%{mendexk_ver}
./configure EUC
%{__make}
cd -


%install
rm -rf $RPM_BUILD_ROOT
export CCACHE_DIR=$HOME/.ccache
unset TEXINPUTS || :
unset HOME || :

install -d $RPM_BUILD_ROOT%{_texmf_main}
install -d $RPM_BUILD_ROOT%{_texmf_var}/web2c
install -d $RPM_BUILD_ROOT%{_texmf_conf}

export LD_LIBRARY_PATH=`pwd`/texk/kpathsea/.libs

# a temporary placeholder for texmf.cnf
install -d $RPM_BUILD_ROOT%{_datadir}/texmf-local/web2c
cp -a texk/kpathsea/texmf.cnf $RPM_BUILD_ROOT%{_datadir}/texmf-local/web2c

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
        texmf=$RPM_BUILD_ROOT%{_texmf_main} \
        texmfmain=$RPM_BUILD_ROOT%{_texmf_main}

rm -rf $RPM_BUILD_ROOT%{_datadir}/texmf-local/

# remove all .la files
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT | grep -e "\\.la$" | xargs rm -f

# set executable bit for the library for debuginfo creation
chmod a+x $RPM_BUILD_ROOT%{_libdir}/libkpathsea.so.*.*

## remove what is packages in other Fedora packages
# jadetex
rm -f $RPM_BUILD_ROOT%{_bindir}/jadetex
rm -f $RPM_BUILD_ROOT%{_bindir}/pdfjadetex
# xmltex
rm -f $RPM_BUILD_ROOT%{_bindir}/xmltex
rm -f $RPM_BUILD_ROOT%{_bindir}/pdfxmltex
# octave-forge
### looks to me like a name clash ?? Octave mex looks like it has nada to
### to with TeX
rm -f $RPM_BUILD_ROOT%{_bindir}/mex
### not in octave-forge, nuking anyway
rm -f $RPM_BUILD_ROOT%{_bindir}/pdfmex
rm -f $RPM_BUILD_ROOT%{_bindir}/utf8mex

# these are owned by texmf-fonts package
rm -f $RPM_BUILD_ROOT%{_texmf_main}/ls-R

# keep fmtutil.cnf used for the initial configuration in doc
rm -rf __fedora_kpathsea
install -d __fedora_kpathsea/
mv $RPM_BUILD_ROOT%{_texmf_main}/web2c/fmtutil.cnf __fedora_kpathsea/fmtutil.cnf-init

# this file is different from the one in texmf-fonts, since it is
# the one from kpathsea which isn't specific of texlive. It is only
# used during build and to set the kpathsea default paths, however.
# Kept as documentation together with paths.h since they describe
# what the kpathsea default paths are
install -d __fedora_kpathsea/kpathsea_defaults
mv $RPM_BUILD_ROOT%{_texmf_main}/web2c/texmf.cnf __fedora_kpathsea/kpathsea_defaults/texmf-kpathsea-defaults.cnf
cp texk/kpathsea/paths.h __fedora_kpathsea/kpathsea_defaults

# these are owned by texmf-doc package
rm -rf $RPM_BUILD_ROOT%{_texmf_main}/doc/tetex

# install cron file
install -p -D %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/texlive.cron

# remove pool files, they belong to texlive-texmf
rm -rf $RPM_BUILD_ROOT%{_texmf_main}/web2c/*.pool
# ptex pool file is added later, and therefore kept

# Japanese pTeX
rm -f $RPM_BUILD_ROOT%{_bindir}/platex
# Convert documents to UTF-8
install -d $RPM_BUILD_ROOT%{_texmf_main}/doc/ptex/ptex-src-%{name} \
         $RPM_BUILD_ROOT%{_texmf_main}/doc/pdvipsk
cd texk/web2c/ptex-src-%{ptex_src_ver}
iconv -f ISO-2022-JP -t UTF-8 \
      COPYRIGHT.jis \
      -o $RPM_BUILD_ROOT%{_texmf_main}/doc/ptex/ptex-src-%{name}/COPYRIGHT-ja
for i in README.txt Changes.txt ; do
  iconv -f EUC-JP -t UTF-8 ${i} \
        -o $RPM_BUILD_ROOT%{_texmf_main}/doc/ptex/ptex-src-%{name}/${i}
done
cd -
cd pdvipsk
for i in ChangeLog.jpatch README.jpatch ; do
  iconv -f EUC-JP -t UTF-8 ${i} -o $RPM_BUILD_ROOT%{_texmf_main}/doc/pdvipsk/${i}
done
cd -

cd texk/web2c/ptex-src-%{ptex_src_ver}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" prefix=$RPM_BUILD_ROOT%{_prefix} \
        texmf=$RPM_BUILD_ROOT%{_texmf_main} \
        texmfmain=$RPM_BUILD_ROOT%{_texmf_main}
# texmf.cnf is prepared by texlive-texmf package.
rm $RPM_BUILD_ROOT%{_texmf_main}/web2c/texmf.cnf
cd -

# mendexk install
cd texk/mendexk%{mendexk_ver}

sh ../libtool --mode=install install mendex $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_mandir}/ja/man1
iconv -f EUC-JP -t UTF-8 mendex.1 -o $RPM_BUILD_ROOT%{_mandir}/ja/man1/mendex.1
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/doc/mendexk-%{name}
install -p COPYRIGHT ChangeLog $RPM_BUILD_ROOT%{_datadir}/texmf/doc/mendexk-%{name}
iconv -f EUC-JP -t UTF-8 README -o $RPM_BUILD_ROOT%{_datadir}/texmf/doc/mendexk-%{name}/README
iconv -f ISO-2022-JP -t UTF-8 COPYRIGHT.jis -o $RPM_BUILD_ROOT%{_datadir}/texmf/doc/mendexk-%{name}/COPYRIGHT.jis
cd -

# remove useless files in texconfig
rm -rf $RPM_BUILD_ROOT%{_texmf_main}/texconfig/{g,v,x,README,generic}

# move the configuration files that should be under user control
install -d $RPM_BUILD_ROOT%{_texmf_conf}/{web2c/,dvipdfm/}
mv $RPM_BUILD_ROOT%{_texmf_main}/web2c/mktexdir.opt $RPM_BUILD_ROOT%{_texmf_conf}/web2c/

# separated projects
rm $RPM_BUILD_ROOT%{_bindir}/devnag
rm $RPM_BUILD_ROOT%{_bindir}/afm2pl $RPM_BUILD_ROOT%{_mandir}/man1/afm2pl.1*

# remove unused ConTeXt stuff
rm $RPM_BUILD_ROOT%{_mandir}/man1/texfind.1* $RPM_BUILD_ROOT%{_mandir}/man1/fdf2tex.1*

# remove (x)dvipdfmx related stuff
rm -f $RPM_BUILD_ROOT%{_bindir}/dvipdfmx
rm -f $RPM_BUILD_ROOT%{_bindir}/xdvipdfmx
rm -rf $RPM_BUILD_ROOT%{_texmf_main}/dvipdfm

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/install-info ] && /sbin/install-info %{_infodir}/web2c.info.gz %{_infodir}/dir
%{_bindir}/fmtutil-sys --all &> /dev/null
%{_bindir}/updmap-sys --syncwithtrees &> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%post afm
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%post context
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%post dvips
[ -x /sbin/install-info ] && /sbin/install-info %{_infodir}/dvips.info.gz %{_infodir}/dir
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%post dviutils
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%post east-asian
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%post latex
[ -x /sbin/install-info ] && /sbin/install-info %{_infodir}/latex.info.gz %{_infodir}/dir
%{_bindir}/texconfig-sys init &> /dev/null
%{_bindir}/texconfig-sys rehash 2> /dev/null
%{_bindir}/fmtutil-sys --all &> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%post xetex
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%post -n kpathsea
/sbin/ldconfig
[ -x /sbin/install-info ] && /sbin/install-info %{_infodir}/kpathsea.info.gz %{_infodir}/dir
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:


%preun
if [ "$1" = 0 ]; then
  [ -x /sbin/install-info ] && /sbin/install-info --delete %{_infodir}/web2c.info.gz %{_infodir}/dir
fi
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%preun dvips
if [ "$1" = 0 ]; then
  [ -x /sbin/install-info ] && /sbin/install-info --delete %{_infodir}/dvips.info.gz %{_infodir}/dir
fi
:

%preun latex
if [ "$1" = 0 ]; then
  [ -x /sbin/install-info ] && /sbin/install-info --delete %{_infodir}/latex.info.gz %{_infodir}/dir
fi
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%preun -n kpathsea
/sbin/ldconfig
if [ "$1" = 0 ]; then
  [ -x /sbin/install-info ] && /sbin/install-info --delete %{_infodir}/kpathsea.info.gz %{_infodir}/dir
fi
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%postun
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%postun afm
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%postun context
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%postun east-asian
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%postun dviutils
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%postun dvips
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%postun latex
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%postun xetex
%{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%postun -n kpathsea
/sbin/ldconfig
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
:

%files
%defattr(644,root,root,755)
# config files
%dir %{_texmf_conf}
%dir %{_texmf_conf}/web2c/
%dir %{_texmf_var}/web2c/
%dir %{_texmf_main}/web2c/
%dir %{_texmf_main}/doc/
%doc %{_texmf_main}/doc/bibtex8/
%doc __fedora_kpathsea/fmtutil.cnf-init
%config(noreplace) %{_texmf_conf}/web2c/mktexdir.opt
# binaries
%attr(755,root,root) %{_bindir}/aleph
%attr(755,root,root) %{_bindir}/amstex
%attr(755,root,root) %{_bindir}/bibtex
%attr(755,root,root) %{_bindir}/ctangle
%attr(755,root,root) %{_bindir}/ctie
%attr(755,root,root) %{_bindir}/cweave
%attr(755,root,root) %{_bindir}/dmp
%attr(755,root,root) %{_bindir}/dvitomp
%attr(755,root,root) %{_bindir}/etex
%attr(755,root,root) %{_bindir}/fmtutil
%attr(755,root,root) %{_bindir}/fmtutil-sys
%attr(755,root,root) %{_bindir}/fontinst
%attr(755,root,root) %{_bindir}/gftodvi
%attr(755,root,root) %{_bindir}/gftopk
%attr(755,root,root) %{_bindir}/gftype
%attr(755,root,root) %{_bindir}/kpseaccess
%attr(755,root,root) %{_bindir}/kpsepath
%attr(755,root,root) %{_bindir}/kpsereadlink
%attr(755,root,root) %{_bindir}/kpsestat
%attr(755,root,root) %{_bindir}/kpsetool
%attr(755,root,root) %{_bindir}/kpsewhich
%attr(755,root,root) %{_bindir}/kpsexpand
%attr(755,root,root) %{_bindir}/kpsewhere
%attr(755,root,root) %{_bindir}/lambda
%attr(755,root,root) %{_bindir}/lamed
%attr(755,root,root) %{_bindir}/mag
%attr(755,root,root) %{_bindir}/makeindex
%attr(755,root,root) %{_bindir}/makempx
%attr(755,root,root) %{_bindir}/mf-nowin
%attr(755,root,root) %{_bindir}/mft
%attr(755,root,root) %{_bindir}/mkindex
%attr(755,root,root) %{_bindir}/mkocp
%attr(755,root,root) %{_bindir}/mkofm
%attr(755,root,root) %{_bindir}/mktexfmt
%attr(755,root,root) %{_bindir}/mktexlsr
%attr(755,root,root) %{_bindir}/mktexmf
%attr(755,root,root) %{_bindir}/mktextfm
%attr(755,root,root) %{_bindir}/mpost
%attr(755,root,root) %{_bindir}/mpto
%attr(755,root,root) %{_bindir}/newer
%attr(755,root,root) %{_bindir}/ofm2opl
%attr(755,root,root) %{_bindir}/omega
%attr(755,root,root) %{_bindir}/omfonts
%attr(755,root,root) %{_bindir}/opl2ofm
%attr(755,root,root) %{_bindir}/otangle
%attr(755,root,root) %{_bindir}/otp2ocp
%attr(755,root,root) %{_bindir}/outocp
%attr(755,root,root) %{_bindir}/ovf2ovp
%attr(755,root,root) %{_bindir}/ovp2ovf
%attr(755,root,root) %{_bindir}/patgen
%attr(755,root,root) %{_bindir}/pdfetex
%attr(755,root,root) %{_bindir}/pdftex
%attr(755,root,root) %{_bindir}/pfb2pfa
%attr(755,root,root) %{_bindir}/pk2bm
%attr(755,root,root) %{_bindir}/pktogf
%attr(755,root,root) %{_bindir}/pktype
%attr(755,root,root) %{_bindir}/pltotf
%attr(755,root,root) %{_bindir}/pooltype
%attr(755,root,root) %{_bindir}/ps2frag
%attr(755,root,root) %{_bindir}/ps2pk
%attr(755,root,root) %{_bindir}/rubibtex
%attr(755,root,root) %{_bindir}/rumakeindex
%attr(755,root,root) %{_bindir}/tangle
%attr(755,root,root) %{_bindir}/tex
%attr(755,root,root) %{_bindir}/texconfig
%attr(755,root,root) %{_bindir}/texconfig-dialog
%attr(755,root,root) %{_bindir}/texconfig-sys
%attr(755,root,root) %{_bindir}/texhash
%attr(755,root,root) %{_bindir}/texlinks
%attr(755,root,root) %{_bindir}/tftopl
%attr(755,root,root) %{_bindir}/tie
%attr(755,root,root) %{_bindir}/updmap
%attr(755,root,root) %{_bindir}/updmap-sys
%attr(755,root,root) %{_bindir}/vftovp
%attr(755,root,root) %{_bindir}/vptovf
%attr(755,root,root) %{_bindir}/weave
# new files not in Fedora tetex
%attr(755,root,root) %{_bindir}/bibtex8
%attr(755,root,root) %{_bindir}/csplain
# separated project
%attr(755,root,root) %{_bindir}/mltex
%attr(755,root,root) %{_bindir}/pdfcsplain
# separated project
%attr(755,root,root) %{_bindir}/eplain
%attr(755,root,root) %{_bindir}/extconv
%attr(755,root,root) %{_bindir}/musixflx
%attr(755,root,root) %{_bindir}/physe
%attr(755,root,root) %{_bindir}/phyzzx
%attr(755,root,root) %{_bindir}/texsis
# other utilities
%attr(755,root,root) %{_bindir}/pdftosrc
# man pages
%{_mandir}/man1/amstex.1*
%{_mandir}/man1/bibtex.1*
%{_mandir}/man1/ctangle.1*
%{_mandir}/man1/ctie.1*
%{_mandir}/man1/cweave.1*
%{_mandir}/man1/cweb.1*
%{_mandir}/man1/dmp.1*
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/eplain.1*
%{_mandir}/man1/etex.1*
%{_mandir}/man1/fmtutil.1*
%{_mandir}/man1/fmtutil-sys.1*
%{_mandir}/man1/fontinst.1*
%{_mandir}/man1/gftodvi.1*
%{_mandir}/man1/gftopk.1*
%{_mandir}/man1/gftype.1*
%{_mandir}/man1/kpseaccess.1*
%{_mandir}/man1/kpsepath.1*
%{_mandir}/man1/kpsereadlink.1*
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsetool.1*
%{_mandir}/man1/kpsewhich.1*
%{_mandir}/man1/kpsewhere.1*
%{_mandir}/man1/kpsexpand.1*
%{_mandir}/man1/lambda.1*
%{_mandir}/man1/mag.1*
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/makempx.1*
%{_mandir}/man1/mf-nowin.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/mkindex.1*
%{_mandir}/man1/mkocp.1*
%{_mandir}/man1/mkofm.1*
%{_mandir}/man1/mktexfmt.1*
%{_mandir}/man1/mktexlsr.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktextfm.1*
%{_mandir}/man1/mpost.1*
%{_mandir}/man1/mpto.1*
%{_mandir}/man1/newer.1*
%{_mandir}/man1/ofm2opl.1*
%{_mandir}/man1/omega.1*
%{_mandir}/man1/opl2ofm.1*
%{_mandir}/man1/otp2ocp.1*
%{_mandir}/man1/outocp.1*
%{_mandir}/man1/ovf2ovp.1*
%{_mandir}/man1/ovp2ovf.1*
%{_mandir}/man1/patgen.1*
%{_mandir}/man1/pdfetex.1*
%{_mandir}/man1/pdftex.1*
%{_mandir}/man1/pfb2pfa.1*
%{_mandir}/man1/pk2bm.1*
%{_mandir}/man1/pktogf.1*
%{_mandir}/man1/pktype.1*
%{_mandir}/man1/pltotf.1*
%{_mandir}/man1/pooltype.1*
%{_mandir}/man1/ps2frag.1*
%{_mandir}/man1/ps2pk.1*
%{_mandir}/man1/rubibtex.1*
%{_mandir}/man1/rumakeindex.1*
%{_mandir}/man1/tangle.1*
%{_mandir}/man1/tex.1*
%{_mandir}/man1/texconfig.1*
%{_mandir}/man1/texconfig-sys.1*
%{_mandir}/man1/texhash.1*
%{_mandir}/man1/texlinks.1*
%{_mandir}/man1/tftopl.1*
%{_mandir}/man1/tie.1*
%{_mandir}/man1/updmap.1*
%{_mandir}/man1/updmap-sys.1*
%{_mandir}/man1/vftovp.1*
%{_mandir}/man1/vptovf.1*
%{_mandir}/man1/weave.1*
%{_mandir}/man5/fmtutil.cnf.5*
# new files not in Fedora tetex
%{_mandir}/man5/updmap.cfg.*
# man pages for other utilities
%{_mandir}/man1/pdftosrc.1*
# other stuff
/etc/cron.daily/texlive.cron
%{_infodir}/web2c.info.*
%{_texmf_main}/web2c/*.opt
%{_texmf_main}/web2c/mktexdir
%{_texmf_main}/web2c/mktexnam
%{_texmf_main}/web2c/mktexupd
%{_texmf_main}/bibtex/
%{_texmf_main}/texconfig/tcfmgr*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/a2ping
%attr(755,root,root) %{_bindir}/e2pall
%attr(755,root,root) %{_bindir}/epstopdf
%attr(755,root,root) %{_bindir}/gsftopk
%attr(755,root,root) %{_bindir}/mf
%attr(755,root,root) %{_bindir}/mktexpk
%attr(755,root,root) %{_bindir}/pdfcrop
%attr(755,root,root) %{_bindir}/ps4pdf
%attr(755,root,root) %{_bindir}/thumbpdf
%{_mandir}/man1/e2pall.1*
%{_mandir}/man1/epstopdf.1*
%{_mandir}/man1/gsftopk.1*
%{_mandir}/man1/mf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/thumbpdf.1*

%files xetex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xetex
%attr(755,root,root) %{_bindir}/xelatex

%files afm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afm2tfm
%attr(755,root,root) %{_bindir}/ttf2afm
%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/ttf2afm.1*

%files dvips
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/allcm
%attr(755,root,root) %{_bindir}/allec
%attr(755,root,root) %{_bindir}/allneeded
%attr(755,root,root) %{_bindir}/dvi2fax
%attr(755,root,root) %{_bindir}/dvips
%attr(755,root,root) %{_bindir}/dvired
%attr(755,root,root) %{_bindir}/odvips
%{_texmf_main}/dvips/
%{_mandir}/man1/allcm.1*
%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvips.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/odvips.1*
%{_infodir}/dvips.info.*

%files doc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/texdoc
%attr(755,root,root) %{_bindir}/texdoctk
# man pages
%{_mandir}/man1/texdoc.1*
%{_mandir}/man1/texdoctk.1*

%files dviutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dt2dv
%attr(755,root,root) %{_bindir}/dv2dt
%attr(755,root,root) %{_bindir}/dvicopy
%attr(755,root,root) %{_bindir}/dvihp
%attr(755,root,root) %{_bindir}/dvitype
%attr(755,root,root) %{_bindir}/dvibook
%attr(755,root,root) %{_bindir}/dviconcat
%attr(755,root,root) %{_bindir}/dvidvi
%attr(755,root,root) %{_bindir}/dvilj
%attr(755,root,root) %{_bindir}/dvilj2p
%attr(755,root,root) %{_bindir}/dvilj4
%attr(755,root,root) %{_bindir}/dvilj4l
%attr(755,root,root) %{_bindir}/dvilj6
%attr(755,root,root) %{_bindir}/dvipos
%attr(755,root,root) %{_bindir}/dviselect
%attr(755,root,root) %{_bindir}/dvitodvi
%attr(755,root,root) %{_bindir}/odvicopy
%attr(755,root,root) %{_bindir}/odvitype
%{_mandir}/man1/dvicopy.1*
%{_mandir}/man1/dvihp.1*
%{_mandir}/man1/dvitype.1*
%{_mandir}/man1/dt2dv.1*
%{_mandir}/man1/dv2dt.1*
%{_mandir}/man1/dvibook.1*
%{_mandir}/man1/dviconcat.1*
%{_mandir}/man1/dvidvi.1*
%{_mandir}/man1/dvilj.1*
%{_mandir}/man1/dvilj2p.1*
%{_mandir}/man1/dvilj4.1*
%{_mandir}/man1/dvilj4l.1*
%{_mandir}/man1/dvilj6.1*
%{_mandir}/man1/dvipos.1*
%{_mandir}/man1/dviselect.1*
%{_mandir}/man1/dvitodvi.1*
%{_mandir}/man1/odvicopy.1*
%{_mandir}/man1/odvitype.1*

%files latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/latex
%attr(755,root,root) %{_bindir}/pdflatex
%attr(755,root,root) %{_bindir}/platex
%attr(755,root,root) %{_bindir}/pslatex
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pdflatex.1*
%{_mandir}/man1/pslatex.1*
%{_infodir}/latex.info.*
# not in fedora tetex
%attr(755,root,root) %{_bindir}/cslatex
%attr(755,root,root) %{_bindir}/lacheck
%attr(755,root,root) %{_bindir}/mllatex
%attr(755,root,root) %{_bindir}/pdfcslatex
%{_mandir}/man1/lacheck.1*

%files -n kpathsea
%defattr(644,root,root,755)
%doc __fedora_kpathsea/kpathsea_defaults/
%attr(755,root,root) %{_libdir}/libkpathsea.so.*
%{_infodir}/kpathsea.info.*

%files -n kpathsea-devel
%defattr(644,root,root,755)
%{_includedir}/kpathsea/
%{_libdir}/libkpathsea.so
# yes - packaging the static too. Some programs apparently can't link
#  against the shared. I can't name any, but so i hear.
%{_libdir}/libkpathsea.a

%files -n mendexk
%defattr(644,root,root,755)
%doc %{_texmf_main}/doc/mendexk-%{name}/
%attr(755,root,root) %{_bindir}/mendex
%{_mandir}/ja/man1/mendex.1*

%files east-asian
%defattr(644,root,root,755)
%doc %{_texmf_main}/doc/pdvipsk/
%doc %{_texmf_main}/doc/ptex/
%{_texmf_main}/fonts/map/pdvips/
%{_texmf_main}/pdvips/
%{_texmf_main}/web2c/ptex.pool
%attr(755,root,root) %{_bindir}/bg5+latex
%attr(755,root,root) %{_bindir}/bg5+pdflatex
%attr(755,root,root) %{_bindir}/bg5latex
%attr(755,root,root) %{_bindir}/bg5pdflatex
%attr(755,root,root) %{_bindir}/cef5latex
%attr(755,root,root) %{_bindir}/cef5pdflatex
%attr(755,root,root) %{_bindir}/ceflatex
%attr(755,root,root) %{_bindir}/cefpdflatex
%attr(755,root,root) %{_bindir}/cefslatex
%attr(755,root,root) %{_bindir}/cefspdflatex
%attr(755,root,root) %{_bindir}/bg5conv
%attr(755,root,root) %{_bindir}/cef5conv
%attr(755,root,root) %{_bindir}/cefconv
%attr(755,root,root) %{_bindir}/cefsconv
%attr(755,root,root) %{_bindir}/gbklatex
%attr(755,root,root) %{_bindir}/gbkpdflatex
%attr(755,root,root) %{_bindir}/hbf2gf
%attr(755,root,root) %{_bindir}/jbibtex
%attr(755,root,root) %{_bindir}/pdfplatex-pl
%attr(755,root,root) %{_bindir}/pdvips
%attr(755,root,root) %{_bindir}/pdvitype
%attr(755,root,root) %{_bindir}/platex-pl
%attr(755,root,root) %{_bindir}/platex209
%attr(755,root,root) %{_bindir}/ptex
%attr(755,root,root) %{_bindir}/sjisconv
%attr(755,root,root) %{_bindir}/sjislatex
%attr(755,root,root) %{_bindir}/sjispdflatex
%attr(755,root,root) %{_bindir}/opdvips
%{_mandir}/man1/hbf2gf.1*
%{_mandir}/man1/pdvips.1*
%{_mandir}/man1/opdvips.1*

%files context
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ctxtools
%attr(755,root,root) %{_bindir}/exatools
%attr(755,root,root) %{_bindir}/luatools
%attr(755,root,root) %{_bindir}/makempy
%attr(755,root,root) %{_bindir}/mpstools
%attr(755,root,root) %{_bindir}/mptopdf
%attr(755,root,root) %{_bindir}/mtxtools
%attr(755,root,root) %{_bindir}/pdftools
%attr(755,root,root) %{_bindir}/pstopdf
%attr(755,root,root) %{_bindir}/rlxtools
%attr(755,root,root) %{_bindir}/runtools
%attr(755,root,root) %{_bindir}/texexec
%attr(755,root,root) %{_bindir}/texfont
%attr(755,root,root) %{_bindir}/texmfstart
%attr(755,root,root) %{_bindir}/textools
%attr(755,root,root) %{_bindir}/texutil
%attr(755,root,root) %{_bindir}/tmftools
%attr(755,root,root) %{_bindir}/xmltools
%{_mandir}/man1/ctxtools.1*
%{_mandir}/man1/makempy.1*
%{_mandir}/man1/mptopdf.1*
%{_mandir}/man1/pdftools.1*
%{_mandir}/man1/pstopdf.1*
%{_mandir}/man1/texexec.1*
%{_mandir}/man1/texfont.1*
%{_mandir}/man1/texmfstart.1*
%{_mandir}/man1/textools.1*
%{_mandir}/man1/texutil.1*
