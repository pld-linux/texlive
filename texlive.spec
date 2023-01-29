# TODO:
# - get rid of /etc/cron.daily depencency from base pkg, use /etc/tmpwatch.d instead
# - cache in /var/lib? (move to /var/cache)
# - clean fonts packaging mess (-tex-*/-latex-*, -fonts-*, -fonts-type1-* packages:
#   which should exist, how dirs/files should be propagated in them)

# Conditional build:
%bcond_with	bootstrap	# bootstrap build
%bcond_without	xindy		# xindy packages

%if %{with bootstrap}
%undefine	with_xindy
%endif

Summary:	TeX typesetting system and MetaFont font formatter
Summary(de.UTF-8):	TeX-Satzherstellungssystem und MetaFont-Formatierung
Summary(es.UTF-8):	Sistema de typesetting TeX y formateador de fuentes MetaFont
Summary(fr.UTF-8):	Systéme de compostion TeX et formatteur de MetaFontes
Summary(hu.UTF-8):	TeX szövegszedő rendszer és MetaFont font formázó
Summary(pl.UTF-8):	System składu publikacji TeX oraz formater fontów MetaFont
Summary(pt_BR.UTF-8):	Sistema de typesetting TeX e formatador de fontes MetaFont
Summary(tr.UTF-8):	TeX dizgi sistemi ve MetaFont yazıtipi biçimlendiricisi
Name:		texlive
Version:	20080816
Release:	40
Epoch:		1
License:	distributable
Group:		Applications/Publishing/TeX
Source0:	https://tug.org/svn/texlive/branches/branch2008/Master/source/%{name}-%{version}-source.tar.lzma
# Source0-md5:	554287c3e458da776edd684506048d45
Source1:	ftp://tug.org/texlive/historic/2008/%{name}-20080822-texmf.tar.lzma
# Source1-md5:	fa74072e1344e8390eb156bcda61a8b2
Source4:	%{name}.cron
Source5:	xdvi.desktop
Source6:	xdvi.png
# current (until 20230128) version is 2012-02-29, here is some older (2008-03-30)
#Source10:	http://tug.ctan.org/macros/latex/contrib/floatflt.zip
Source10:	floatflt.zip
# Source10-md5:	5d9fe14d289aa81ebb6b4761169dd5f2
Source11:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-fonts-larm.tar.bz2
# Source11-md5:	df2fcc66f0c2e90785ca6c9b27dacd34
# dated 2008-01-29
Source12:	http://www.ctan.org/macros/latex/contrib/foiltex.zip
# Source12-md5:	0a6b4e64fb883a68d9b288bf3421db25
Source50:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/Splashscreen.pm
# Source50-md5:	5cc49f49010f27fdb02dd7053797ba19
Source51:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLConfig.pm
# Source51-md5:	947ee29c38c2c2cfd9a25c597a89598a
Source52:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLMedia.pm
# Source52-md5:	9f1e76f3528125691edd4fbcdd69c5cb
Source53:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPDB.pm
# Source53-md5:	47cae437999e98a7bd24f27db7b0fa34
Source54:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPOBJ.pm
# Source54-md5:	c573c407ae3d98f710d65d593a7d1745
Source55:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPSRC.pm
# Source55-md5:	834ae0ac5c59fd00ab6000ba6367a987
Source56:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPaper.pm
# Source56-md5:	326314fc034a5d9ef9d4a60033f7186f
Source57:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPostActions.pm
# Source57-md5:	17c1968725ccf4aaafb7162b7b3609fc
Source58:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLTREE.pm
# Source58-md5:	039cc8878f380cab3b0beffe75870c6c
Source59:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLUtils.pm
# Source59-md5:	4e611075975c0dd62a9170d319258b8f
Source60:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLWinGoo.pm
# Source60-md5:	825121187994692ecda0f48a5b17421a
Source61:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TeXCatalogue.pm
# Source61-md5:	6289d93a12aa246fc2019b0109d2167f
Source62:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/waitVariableX.pm
# Source62-md5:	f0fa0f2fc7aacb1e9b40eb65891a24c8
Patch0:		%{name}-am.patch
Patch1:		%{name}-20080816-kpathsea-ar.patch
Patch2:		%{name}-gcc44.patch
Patch3:		%{name}-getline.patch
Patch4:		%{name}-no-common.patch
Patch5:		%{name}-aclocal.patch
Patch6:		%{name}-libpng.patch
Patch7:		%{name}-libpng15.patch
Patch8:		%{name}-extramembot.patch
Patch9:		%{name}-5yr-old.patch
Patch10:	format-security.patch
Patch11:	%{name}-clisp.patch
Patch12:	%{name}-system-libpng.patch
Patch13:	%{name}-system-zzip.patch
Patch14:	%{name}-system-zlib.patch
Patch15:	%{name}-xetex-zlib.patch
Patch16:	cxx11.patch
Patch17:	perl-syntax.patch
Patch18:	%{name}-open.patch
Patch19:	%{name}-info.patch
Patch20:	%{name}-throw.patch
URL:		https://tug.org/texlive/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
%if %{with xindy}
BuildRequires:	clisp
%endif
BuildRequires:	ed
BuildRequires:	expat-devel
BuildRequires:	ffcall-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	freetype1-devel
BuildRequires:	gd-devel >= 2.0.33
BuildRequires:	libpng-devel >= 2:1.2.8
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRequires:	lzma
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	sed >= 4.0
BuildRequires:	t1lib-devel >= 5.0.2
BuildRequires:	texinfo
%if %{with bootstrap}
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-format-plain
BuildRequires:	tetex-latex-cyrillic
BuildRequires:	tetex-tex-babel
%else
BuildRequires:	%{name}-context
BuildRequires:	%{name}-cslatex
BuildRequires:	%{name}-csplain
BuildRequires:	%{name}-fonts-cmsuper
#BuildRequires:	%{name}-format-amstex
#BuildRequires:	%{name}-format-cslatex
BuildRequires:	%{name}-format-eplain
BuildRequires:	%{name}-format-mex
BuildRequires:	%{name}-format-pdflatex
BuildRequires:	%{name}-latex
BuildRequires:	%{name}-latex-cyrillic
BuildRequires:	%{name}-metapost
BuildRequires:	%{name}-mex
BuildRequires:	%{name}-omega
BuildRequires:	%{name}-other-utils
BuildRequires:	%{name}-pdftex
BuildRequires:	%{name}-phyzzx
BuildRequires:	%{name}-plain
BuildRequires:	%{name}-tex-babel
BuildRequires:	%{name}-tex-physe
BuildRequires:	%{name}-xetex
BuildRequires:	%{name}-xmltex
# fill with future texlive BR. guesses ones for now
%endif
BuildRequires:	/usr/bin/latex
BuildRequires:	texconfig
BuildRequires:	unzip
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel >= 1.2.1
BuildRequires:	zziplib-devel
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-cm = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-misc = %{epoch}:%{version}-%{release}
Requires:	awk
Requires:	dialog
Requires:	kpathsea = %{epoch}:%{version}-%{release}
Requires:	sed
Requires:	sh-utils
Requires:	textutils
Suggests:	texconfig = %{epoch}:%{version}-%{release}
Suggests:	tmpwatch
Provides:	tetex = %{epoch}:%{version}-%{release}
Provides:	tetex-format-pdfetex = %{epoch}:%{version}-%{release}
Provides:	tetex-metafont
Obsoletes:	tetex < 1:3.1
Obsoletes:	tetex-afm < 1:2.0
Obsoletes:	tetex-doc < 1:3.1
Obsoletes:	tetex-doc-latex2e-html < 1:3.0-1
Obsoletes:	tetex-fontinst < 1:3.1
Obsoletes:	tetex-fontname < 1:3.1
Obsoletes:	tetex-fonts < 1:2.0
Obsoletes:	tetex-fonts-pandora < 1:3.0
Obsoletes:	tetex-fonts-vcm < 1:3.0
Obsoletes:	tetex-format-elatex < 1:3.0
Obsoletes:	tetex-format-pdfelatex < 1:3.0
Obsoletes:	tetex-format-pdfemex < 1:3.0
Obsoletes:	tetex-latex-vnps < 1:3.0
Obsoletes:	tetex-latex-vnr < 1:3.0
Obsoletes:	tetex-metafont < 1:3.1
Obsoletes:	tetex-oxdvi < 1:3.0
Obsoletes:	tetex-plain-dvips < 1:3.0
Obsoletes:	tetex-plain-mathtime < 1:3.0
Obsoletes:	tetex-plain-misc < 1:3.0
Obsoletes:	tetex-plain-plnfss < 1:3.0
Obsoletes:	tetex-tex-hyphen < 1:3.1
Obsoletes:	tetex-tex-vietnam < 1:3.0
Obsoletes:	texlive-metafont < 1:20080816-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texmf		%{_datadir}/texmf
%define		texmfdist	%{texmf}-dist
%define		texmfdoc	%{texmf}-doc
%define		fmtdir		/var/lib/texmf/web2c
%define		_localstatedir	/var/lib/texmf
%define		fixinfodir [ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 ;
%define		fmtutil(f:) [ ! \\\( -f %{_localstatedir}/web2c/%{-f*}.fmt.rpmnew -o -f %{_localstatedir}/web2c/%{-f*}.efmt.rpmnew \\\) ] || %{_bindir}/fmtutil-sys --byfmt %{-f*} >/dev/null 2>/dev/null || echo "Regenerating %{-f*} failed. See %{_localstatedir}/web2c/%{-f*}.log for details" 1>&2 && exit 0 ;

%define		_noautoreq 'perl(path_tre)'

%description
TeXLive is an implementation of TeX for Linux or UNIX systems. TeX
takes a text file and a set of formatting commands as input and
creates a typesetter independent .dvi (DeVice Independent) file as
output. Usually, TeX is used in conjunction with a higher level
formatting package like LaTeX or PlainTeX, since TeX by itself is not
very user-friendly.

%description -l es.UTF-8
Tex formata archivos de texto y órdenes para una salida independiente
de dispositivo (que se llama DVI - DeVice Independent). En The TeXbook
de Knut se describen las capacidades y el lenguaje TeX.

%description -l de.UTF-8
TeX formatiert eine Datei, die abwechselnd Text und Befehle enthält
und gibt eine geräteunabhängige Datei aus (DVI genannt, Abk. für
DeVice Independent). Die Funktionen und Sprache von TeX werden in The
TeXbook von Knuth beschrieben.

%description -l fr.UTF-8
TeX formate un fichier de commandes et de texte mélandés, et produit
un fichier de indépendant de toute plate-forme (appelé DVI, qui est un
raccourci pour Device Independant). Les possibilités de TeX et son
langage sont décrites dans l'ouvrage TeXbook, de Knuth.

%description -l hu.UTF-8
TeXLive a TeX egy implementációja Linux és UNIX rendszerekre. TeX egy
egyszerű szövegfájlt fogad bemenetként, és formázó parancsok
segítségével a szövegszedő egy független .dvi (DeVice Independent)
fájlt készít. A TeX-et leginkább magasabb szintű formázó parancsokkal
kiegészítve használják, mint pl. LaTeX-hel vagy PlainTeX-hel, mivel a
TeX önmaga nem túlzottan "felhasználóbarát".

%description -l pl.UTF-8
TeX formatuje przygotowany tekst oraz komendy i produkuje niezależny
od urządzenia plik wynikowy (tzw. DVI -- skrót od DeVice Independent).
Możliwości TeXa, oraz jego język zostały opisane w ,,The TeXbook''
Donalda E. Knutha.

%description -l pt_BR.UTF-8
Tex formata arquivos de texto e comandos para uma saída independente
de dispositivo (chamado DVI - DeVice Independent). As capacidades e a
linguagem TeX são descritas no The TeXbook, de Knuth.

%description -l tr.UTF-8
TeX, içinde metin ve komutların yer aldığı bir dosyayı okur ve dizgi
aygıtından bağımsız bir çıktı (DeVice Independent - DVI) oluşturur.
TeX'in becerileri ve dizgi dili, dili geliştiren Knuth'un 'The
TeXbook' başlıklı kitabında anlatılmaktadır.

%package other-utils
Summary:	Other utilities
Summary(pl.UTF-8):	Inne narzędzia
Group:		Applications/Publishing/TeX
# contains texlua scripts
Requires:	%{name}-luatex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-cyrtexinfo < 1:3.1

%description other-utils
Other utilities.

%description other-utils -l pl.UTF-8
Narzędzia inne.

%package jadetex
Summary:	LaTeX macros for converting Jade TeX output into DVI/PS/PDF
Summary(pl.UTF-8):	Makra LaTeXa do konwersji Jade TeXa do DVI/PS/PDF
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Provides:	jadetex = %{epoch}:%{version}-%{release}
Obsoletes:	jadetex < 3.14
BuildArch:	noarch

%description jadetex
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as LaTeX files.

%description jadetex -l pl.UTF-8
JadeTeX zawiera dodatkowe makra LaTeXa potrzebne do konwersji plików
otrzymanych z Jade TeXa i przetworzenia ich jako plików LaTeXa.

%package other-utils-doc
Summary:	Other utilities documentation
Summary(pl.UTF-8):	Dokumentacja do narzędzi innych
Group:		Applications/Publishing/TeX
BuildArch:	noarch

%description other-utils-doc
Other utilities documentation.

%description other-utils-doc -l pl.UTF-8
Dokumentacja do narzędzi innych.

%package doc
Summary:	Documentation for TeX Live
Summary(pl.UTF-8):	Dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc
Assorted useful documentation for TeX Live.

%description doc -l pl.UTF-8
Zbiór przydatnej dokumentacji do TeX Live'a.

%package doc-bg
Summary:	Bulgarian documentation for TeX Live
Summary(pl.UTF-8):	Bułgarska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-bg
Assorted useful Bulgarian documentation for TeX Live.

%description doc-bg -l pl.UTF-8
Zbiór przydatnej bułgarskiej dokumentacji do TeX Live'a.

%package doc-cs
Summary:	Czech documentation for TeX Live
Summary(pl.UTF-8):	Czeska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-cs
Assorted useful Czech documentation for TeX Live.

%description doc-cs -l pl.UTF-8
Zbiór przydatnej czeskiej dokumentacji do TeX Live'a.

%package doc-de
Summary:	German documentation for TeX Live
Summary(pl.UTF-8):	Niemiecka dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-de
Assorted useful German documentation for TeX Live.

%description doc-de -l pl.UTF-8
Zbiór przydatnej niemieckiej dokumentacji do TeX Live'a.

%package doc-el
Summary:	Greek documentation for TeX Live
Summary(pl.UTF-8):	Grecka dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-el
Assorted useful Greek documentation for TeX Live.

%description doc-el -l pl.UTF-8
Zbiór przydatnej greckiej dokumentacji do TeX Live'a.

%package doc-es
Summary:	Spanish documentation for TeX Live
Summary(pl.UTF-8):	Hiszpańska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-es
Assorted useful Spanish documentation for TeX Live.

%description doc-es -l pl.UTF-8
Zbiór przydatnej hiszpańskiej dokumentacji do TeX Live'a.

%package doc-fi
Summary:	Finnish documentation for TeX Live
Summary(pl.UTF-8):	Fińska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-fi
Assorted useful Finnish documentation for TeX Live.

%description doc-fi -l pl.UTF-8
Zbiór przydatnej fińskiej dokumentacji do TeX Live'a.

%package doc-fr
Summary:	French documentation for TeX Live
Summary(pl.UTF-8):	Francuska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-fr
Assorted useful French documentation for TeX Live.

%description doc-fr -l pl.UTF-8
Zbiór przydatnej francuskiej dokumentacji do TeX Live'a.

%package doc-it
Summary:	Italian documentation for TeX Live
Summary(pl.UTF-8):	Włoska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-it
Assorted useful Italian documentation for TeX Live.

%description doc-it -l pl.UTF-8
Zbiór przydatnej włoskiej dokumentacji do TeX Live'a.

%package doc-ja
Summary:	Japanese documentation for TeX Live
Summary(pl.UTF-8):	Japońska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-ja
Assorted useful Japanese documentation for TeX Live.

%description doc-ja -l pl.UTF-8
Zbiór przydatnej japońskiej dokumentacji do TeX Live'a.

%package doc-ko
Summary:	Korean documentation for TeX Live
Summary(pl.UTF-8):	Koreańska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-ko
Assorted useful Korean documentation for TeX Live.

%description doc-ko -l pl.UTF-8
Zbiór przydatnej koreańskiej dokumentacji do TeX Live'a.

%package doc-mn
Summary:	Mongolian documentation for TeX Live
Summary(pl.UTF-8):	Mongolska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-mn
Assorted useful Mongolian documentation for TeX Live.

%description doc-mn -l pl.UTF-8
Zbiór przydatnej mongolskiej dokumentacji do TeX Live'a.

%package doc-nl
Summary:	Dutch documentation for TeX Live
Summary(pl.UTF-8):	Holenderska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-nl
Assorted useful Dutch documentation for TeX Live.

%description doc-nl -l pl.UTF-8
Zbiór przydatnej holenderskiej dokumentacji do TeX Live'a.

%package doc-pl
Summary:	Polish documentation for TeX Live
Summary(pl.UTF-8):	Polska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-pl
Assorted useful Polish documentation for TeX Live.

%description doc-pl -l pl.UTF-8
Zbiór przydatnej polskiej dokumentacji do TeX Live'a.

%package doc-pt
Summary:	Portuguese documentation for TeX Live
Summary(pl.UTF-8):	Portugalska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-pt
Assorted useful Portuguese documentation for TeX Live.

%description doc-pt -l pl.UTF-8
Zbiór przydatnej portugalskiej dokumentacji do TeX Live'a.

%package doc-ru
Summary:	Russian documentation for TeX Live
Summary(pl.UTF-8):	Rosyjska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-ru
Assorted useful Russian documentation for TeX Live.

%description doc-ru -l pl.UTF-8
Zbiór przydatnej rosyjskiej dokumentacji do TeX Live'a.

%package doc-sk
Summary:	Slovak documentation for TeX Live
Summary(pl.UTF-8):	Słowacka dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-sk
Assorted useful Slovak documentation for TeX Live.

%description doc-sk -l pl.UTF-8
Zbiór przydatnej słowackiej dokumentacji do TeX Live'a.

%package doc-sl
Summary:	Slovenian documentation for TeX Live
Summary(pl.UTF-8):	Słoweńska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-sl
Assorted useful Slovenian documentation for TeX Live.

%description doc-sl -l pl.UTF-8
Zbiór przydatnej słoweńskiej dokumentacji do TeX Live'a.

%package doc-th
Summary:	Thai documentation for TeX Live
Summary(pl.UTF-8):	Tajska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-th
Assorted useful Thai documentation for TeX Live.

%description doc-th -l pl.UTF-8
Zbiór przydatnej tajskiej dokumentacji do TeX Live'a.

%package doc-tr
Summary:	Turkish documentation for TeX Live
Summary(pl.UTF-8):	Turecka dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-tr
Assorted useful Turkish documentation for TeX Live.

%description doc-tr -l pl.UTF-8
Zbiór przydatnej tureckiej dokumentacji do TeX Live'a.

%package doc-uk
Summary:	Ukrainian documentation for TeX Live
Summary(pl.UTF-8):	Ukraińska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-uk
Assorted useful Ukrainian documentation for TeX Live.

%description doc-uk -l pl.UTF-8
Zbiór przydatnej ukraińskiej dokumentacji do TeX Live'a.

%package doc-vi
Summary:	Vietnamese documentation for TeX Live
Summary(pl.UTF-8):	Wietnamska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-vi
Assorted useful Vietnamese documentation for TeX Live.

%description doc-vi -l pl.UTF-8
Zbiór przydatnej wietnamskiej dokumentacji do TeX Live'a.

%package doc-zh_CN
Summary:	Chinese documentation for TeX Live
Summary(pl.UTF-8):	Chińska dokumentacja do TeX Live'a
Group:		Documentation
BuildArch:	noarch

%description doc-zh_CN
Assorted useful Chinese documentation for TeX Live.

%description doc-zh_CN -l pl.UTF-8
Zbiór przydatnej chińskiej dokumentacji do TeX Live'a.

%package doc-latex
Summary:	Basic LaTeX packages documentation
Summary(hu.UTF-8):	Az alap LaTeX csomagok dokumentációja
Summary(pl.UTF-8):	Podstawowa dokumentacja do pakietów LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-doc-latex < 1:3.1
BuildArch:	noarch

%description doc-latex
Basic LaTeX packages documentation.

%description doc-latex -l hu.UTF-8
Az alap LaTeX csomagok dokumentációja

%description doc-latex -l pl.UTF-8
Podstawowa dokumentacja do pakietów LaTeXa.

# # libraries #
%package -n kpathsea
Summary:	File name lookup library
Summary(hu.UTF-8):	Fájlnév-kereső könyvtár
Summary(pl.UTF-8):	Biblioteka szukająca nazw plików
Group:		Libraries

%description -n kpathsea
File name lookup library.

%description -n kpathsea -l hu.UTF-8
Fájlnév-kereső könyvtár.

%description -n kpathsea -l pl.UTF-8
Biblioteka szukająca nazw plików.

%package -n kpathsea-devel
Summary:	Kpathsea library filename lookup header files and documentation
Summary(es.UTF-8):	Bibliotecas y archivos de inclusión para desarrollo TeX
Summary(hu.UTF-8):	Kpathsea fájlnév-kereső könyvtár header fájljai és dokumentációja
Summary(pl.UTF-8):	Pliki nagłówkowe oraz dokumetacja kpathsea
Summary(pt_BR.UTF-8):	Bibliotecas e headers para desenvolvimento TeX
Group:		Development/Libraries
Requires:	kpathsea = %{epoch}:%{version}-%{release}

%description -n kpathsea-devel
Kpathsea library filename lookup header files and documentation.

%description -n kpathsea-devel -l es.UTF-8
Bibliotecas, archivos de inclusión, etc, para que puedas desarrollar
aplicaciones TeX.

%description -n kpathsea-devel -l hu.UTF-8
Kpathsea fájlnév-kereső könyvtár header fájljai és dokumentációja.

%description -n kpathsea-devel -l pl.UTF-8
Pliki nagłówkowe oraz dokumentacja biblioteki kpathsea.

%description -n kpathsea-devel -l pt_BR.UTF-8
Bibliotecas, headers e outros componentes que podem ser utilizados
para desenvolver aplicações TeX.

# # programs #
%package dvips
Summary:	DVI to PostScript converter
Summary(de.UTF-8):	dvi-Postscript-Konvertierungsprogramm
Summary(es.UTF-8):	Convertidor dvi para postscript
Summary(fr.UTF-8):	Convertisseur dvi vers PostScript
Summary(hu.UTF-8):	DVI-ből PosctScript-be konvertáló
Summary(pl.UTF-8):	Konwerter plików DVI do PostScriptu
Summary(pt_BR.UTF-8):	Conversor dvi para postscript
Summary(tr.UTF-8):	dvi'dan postscript'e dönüştürücü
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-dvips = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-dvips < 1:3.1

%description dvips
The program dvips takes a DVI file file[.dvi] produced by TeX (or by
some other processor such as GFtoDVI) and converts it to PostScript,
normally sending the result directly to the laserprinter.

%description dvips -l de.UTF-8
Das dvips-Programm nimmt eine dvi-Datei ([.dvi]), die von TeX bzw.
durch einen anderen Prozessor wie GFtoDVI) erzeugt wurde, und
konvertiert diese in PostScript, wobei das Ergebnis in der Regel
direkt an einen Laserdrucker gesandt wird.

%description dvips -l es.UTF-8
El programa dvips coge un archivo DVI (.dvi) producido por TeX (o por
otro procesador como GFtoDVI) y lo convierte a PostScript, normalmente
enviando el resultado directamente a la impresora láser.

%description dvips -l fr.UTF-8
Le programme dvips convertit les fichiers DVI en PostScript, en
envoyant normalement le résultat directement sur une imprimante Laser.

%description dvips -l hu.UTF-8
A dvips program egy TeX által készített DVI-fájlból PostScript
állományt készít, amelyet a legtöbb esetben közvetlenül a
lézernyomtatóra küldhetsz.

%description dvips -l pl.UTF-8
Program dvips bierze plik DVI wygenerowany przez TeXa (lub jakiś inny
program, jak na przykład GFtoDVI) i konwertuje go do PostScriptu.
Domyślnie wynik jest wysyłany bezpośrednio do drukarki.

%description dvips -l pt_BR.UTF-8
O programa dvips toma um arquivo DVI (.dvi) produzido pelo TeX (ou por
outro processador como o GFtoDVI) e o converte para PostScript,
normalmente enviando o resultado diretamente para a impressora laser.

%description dvips -l tr.UTF-8
dvips programı, dvi biçiminde bir girdi dosyası alır ve onu
PostScript'e dönüştürür. Kaynak dosya TeX tarafından oluşturulmuş
olabileceği gibi başka işleyiciler tarafından da (GFtoDVI gibi)
üretilmiş olabilir.

%package dvilj
Summary:	DVI to PCL converter
Summary(de.UTF-8):	Ein dvi-->Laserjet-Konvertierer
Summary(es.UTF-8):	Convertidor dvi para laserjet
Summary(fr.UTF-8):	convertisseur dvi vers laserjet
Summary(hu.UTF-8):	DVI-ből PCL-be konvertáló
Summary(pl.UTF-8):	Konwerter plików DVI do języka PCL
Summary(pt_BR.UTF-8):	Conversor dvi para laserjet
Summary(tr.UTF-8):	dvi'dan laserjet'e dönüştürücü
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-dvilj < 1:3.1

%description dvilj
Dvilj and dvilj's siblings (included in this package) will convert TeX
text formatting system output .dvi files to HP PCL (HP Printer Control
Language) commands. Using dvilj, you can print TeX files to HP
LaserJet+ and fully compatible printers. With dvilj2p, you can print
to HP LaserJet IIP and fully compatible printers. And with dvilj4, you
can print to HP LaserJet4 and fully compatible printers.

%description dvilj -l de.UTF-8
Dvilj und Gebrüder konvertieren TeX-Ausgabe-.dvi-Dateien in HP PCL (HP
Printer Control Language) Befehle zum Drucken auf HP LaserJet+, HP
LaserJet IIP (mit dvilj2p), HP LaserJet 4 (mit dvilj4) und vollständig
kompatiblen Druckern.

%description dvilj -l es.UTF-8
Dvilj y semejantes convierten archivos de salida TeX.dvi en comandos
HP PCL (i.e. Lenguaje de Control de Impresoras HP) adecuados a
impresión de impresoras HP LaserJEt+, HP LaserJet IIP (usando
dvilj2p), HP LaserJet 4 (usando dvilj4) y compatibles.

%description dvilj -l fr.UTF-8
dvilj et ses cousins convertissent les fichiers dvi en commandes HPPCL
(le langage des imprimantes HP) pour les imprimer sur HP LaserJet+, HP
LaserJet IIP (avec dvilj2p), HP LaserJet 4 (avec dvilj4), et autres
imprimantes totalement compatibles.

%description dvilj -l hu.UTF-8
Dvilj a TeX által előállított .dvi fájlokat konvertálja HP PCL (HP
Printer Control Language) parancsokká. A dvilj használatával TeX
fájlokat tudsz nyomtatni HP LaserJet+ és a vele kompatibilis
nyomtatókon. A dvilj2p-vel HP LaserJet IIP és kompatibilis
nyomtatókra. És végül a dvilj4-gyel HP LaserJet4 és kompatibilisekre.

%description dvilj -l pl.UTF-8
dvilj oraz pokrewne narzędzia (załączone w tym pakiecie) konwertują
pliki wyjściowe .dvi systemu formatującego tekst TeX na polecenia HP
PCL (HP Printer Control Language). Przy użyciu dvilj można drukować
pliki TeXa na drukarkach HP LaserJet+ i w pełni kompatybilnych. Przy
użyciu dvilj2p można drukować na drukarkach HP LaserJet IIP i w pełni
kompatybilnych. Przy użyciu dvilj4 można drukować na drukarkach HP
LaserJet4 i w pełni kompatybilnych.

%description dvilj -l pt_BR.UTF-8
Dvilj e semelhantes convertem arquivos de saída TeX .dvi em comandos
HP PCL (i.e. Linguagem de Controle de Impressoras HP) adequados para
impressão em impressoras HP LaserJet+, HP LaserJet IIP (usando
dvilj2p), HP LaserJet 4 (usando dvilj4) e compatíveis.

%description dvilj -l tr.UTF-8
TeX çıktısı dvi dosyalarını HP PCL (HP'nin geliştirdiği bir yazıcı
denetim dili) komutlarına çevirir ve böylece bir LaserJet+, HP
LaserJet IIP (dvilj2p ile), HP LaserJet4 (dvilj4 ile) ve tam
uyumlularından yazıcı çıktısı alınabilir.

%package makeindex
Summary:	A general purpose hierarchical index generator
Summary(hu.UTF-8):	Egy általános célú hierarchikus index generáló
Summary(pl.UTF-8):	Generator hierarchicznych indeksów ogólnego przeznaczenia
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-makeindex
Obsoletes:	tetex-makeindex < 1:3.1
Obsoletes:	tetex-rumakeindex < 1:3.1

%description makeindex
A general purpose hierarchical index generator; it accepts one or more
input files (often produced by a text formatter such as TeX or troff),
sorts the entries, and produces an output file which can be formatted.
The formats of the input and output files are specified in a style
file; by default, input is assumed to be an idx file, as generated by
LaTeX.

%description makeindex -l hu.UTF-8
Egy általános célű hierarchikus index generáló; elfogad egy vagy több
bemeneti fájlt (gyakran szövegformázótól, mint a TeX vagy a troff),
rendezi a bejegyzéseket, és egy kimeneti, megfelelő formátumú fájlt
készit. A be- és kimeneti fájlok formátumai stílus fájlokban van
definiálva; alapértelmezetten a bemeneti fájl egy idx fájl, amit a
LaTeX generál.

%description makeindex -l pl.UTF-8
Generator hierarchicznych indeksów ogólnego przeznaczenia; przyjmuje
jeden lub więcej plików wejściowych (zazwyczaj zrobionych przez
narzędzie formatujące tekst, takie jak TeX lub troff), sortuje
elementy i tworzy plik wyjściowy, który może być sformatowany. Formaty
plików wejściowych i wyjściowych podaje się w pliku stylu; domyślnie
przyjmowany jest plik wejściowy w formacie idx, wygenerowany przez
LaTeX.

%package tex-arrayjob
Summary:	Array data structures for (La)TeX
Summary(hu.UTF-8):	Tömb adatstruktúra (La)TeX-hez
Summary(pl.UTF-8):	Tablicowe struktury danych dla (La)TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description tex-arrayjob
Array data structures for (La)TeX.

%description tex-arrayjob -l hu.UTF-8
Tömb adatstruktúra (La)TeX-hez.

%description tex-arrayjob -l pl.UTF-8
Tablicowe struktury danych dla (La)TeXa.

%package tex-mathdots
Summary:	Commands to produce dots in math that respect font size
Summary(hu.UTF-8):	Pontok előállítása matematikai módban a font méret figyelmbevételével
Summary(pl.UTF-8):	Polecenia do wstawiania we wzorach kropek respektujących rozmiar fontu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description tex-mathdots
Commands to produce dots in math that respect font size.

%description tex-mathdots -l hu.UTF-8
Pontok előállítása matematikai módban a font méret figyelmbevételével.

%description tex-mathdots -l pl.UTF-8
Polecenia do wstawiania we wzorach kropek respektujących rozmiar
fontu.

%package tex-midnight
Summary:	A set of useful macro tools
Summary(hu.UTF-8):	Hasznos makrók gyűjteménye
Summary(pl.UTF-8):	Zbiór przydatnych narzędzi do makr
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description tex-midnight
A set of useful macro tools.

%description tex-midnight -l hu.UTF-8
Hasznos makrók gyűjteménye.

%description tex-midnight -l pl.UTF-8
Zbiór przydatnych narzędzi do makr.

%package tex-kastrup
Summary:	Convert numbers into binary, octal and hexadecimal
Summary(pl.UTF-8):	Konwersja liczb na binarne, ósemkowe i szesnastkowe
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description tex-kastrup
Convert numbers into binary, octal and hexadecimal.

%description tex-kastrup -l pl.UTF-8
Konwersja liczb na binarne, ósemkowe i szesnastkowe.

%package tex-ofs
Summary:	Olsak's Font System
Summary(pl.UTF-8):	System fontów Olsaka
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description tex-ofs
Olsak's Font System.

%description tex-ofs -l pl.UTF-8
System fontów Olsaka.

%package tex-physe
Summary:	The PHYSE format
Summary(hu.UTF-8):	PHYSE formátum
Summary(pl.UTF-8):	Format PHYSE
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description tex-physe
The PHYSE format.

%description tex-physe -l hu.UTF-8
PHYSE formátum.

%description tex-physe -l pl.UTF-8
Format PHYSE.

%package tex-velthuis
Summary:	Support for typesetting texts in Devanagari script (Sanskrit and Hindi)
Summary(hu.UTF-8):	Ezzel a csomaggal lehetőséged nyílik Devanagari szövegek szedésére (Sanskrit és Hindi)
Summary(pl.UTF-8):	Obsługa składu tekstu w piśmie dewanagari (sakskryt i hindi)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description tex-velthuis
This package provides support for typesetting texts in Devanagari
script (Sanskrit and Hindi).

%description tex-velthuis -l hu.UTF-8
Ezzel a csomaggal lehetőséged nyílik Devanagari szövegek szedésére
(Sanskrit és Hindi).

%description tex-velthuis -l pl.UTF-8
Ten pakiet zapewnia obsługę składu tekstu w piśmie dewanagari
(sanskryt i hindi).

%package tex-ytex
Summary:	Macro package developed at MIT
Summary(hu.UTF-8):	MIT-en fejlesztett makrócsomag
Summary(pl.UTF-8):	Pakiet makr stworzonych w MIT
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description tex-ytex
Macro package developed at MIT.

%description tex-ytex -l hu.UTF-8
MIT-en fejlesztett makrócsomag.

%description tex-ytex -l pl.UTF-8
Pakiet makr stworzonych w MIT.

%package metapost
Summary:	MetaPost
Summary(hu.UTF-8):	MetaPost
Summary(pl.UTF-8):	Zestaw narzędzi MetaPost
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-metapost < 1:3.1

%description metapost
MetaPost.

%description metapost -l hu.UTF-8
MetaPost.

%description metapost -l pl.UTF-8
Zestaw narzędzi MetaPost.

%package metapost-other
Summary:	Various MetaPost utils
Summary(hu.UTF-8):	Különböző MetaPost eszközök
Summary(pl.UTF-8):	Różne narzędzia MetaPost
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description metapost-other
Various MetaPost utils.

%description metapost-other -l hu.UTF-8
Különböző MetaPost eszközök.

%description metapost-other -l pl.UTF-8
Różne narzędzia MetaPost.

%package mptopdf
Summary:	MetaPost to PDF converter
Summary(hu.UTF-8):	MetaPost-ból PDF-be konvertáló
Summary(pl.UTF-8):	Konwerter MetaPost do PDF
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-metapost = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-mptopdf < 1:3.1
BuildArch:	noarch

%description mptopdf
MetaPost to PDF converter.

%description mptopdf -l hu.UTF-8
MetaPost-ból PDF-be konvertáló.

%description mptopdf -l pl.UTF-8
Konwerter MetaPost do PDF.

%package texdoctk
Summary:	Easy access to TeX documentation
Summary(pl.UTF-8):	Łatwy dostęp do dokumentacji TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-texdoctk < 1:3.1
BuildArch:	noarch

%description texdoctk
A Perl/Tk-based GUI for easy access to package documentation for TeX
on Unix platforms; the databases it uses are based on the texmf/doc
subtrees of teTeX v.1.0.x, but database files for local configurations
with modified/extended directories can be derived from them. Note that
texdoctk is not a viewer itself, but an interface for finding
documentation files and opening them with the appropriate viewer; so
it relies on appropriate programs to be installed on the system.
However, the choice of these programs can be configured by the
sysadmin or user.

%description texdoctk -l pl.UTF-8
Oparty na Perlu i Tk graficzny interfejs dający łatwy dostęp do
dokumentacji pakietów TeXowych na platformach uniksowych; używa baz
danych opartych na poddrzewach texmf/doc z teTeXa 1.0.x, ale może
używać konfiguracji ze zmodyfikowanymi lub rozszerzonymi katalogami.
Należy zauważyć, że texdoctk sam w sobie nie jest przeglądarką, ale
interfejsem do wyszukiwania plików dokumentacji i otwierania ich we
właściwej przeglądarce; tak więc wymaga on odpowiednich programów
zainstalowanych w systemie. Wybór tych programów może być dokonany
przez administratora lub użytkownika.

%package -n texconfig
Summary:	TeX typesetting system configurator
Summary(pl.UTF-8):	Konfigurator systemu składu TeX
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-dvips = %{epoch}:%{version}-%{release}
Requires:	xdvi = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-texconfig < 1:3.1
BuildArch:	noarch

%description -n texconfig
TeX typesetting system configurator.

%description -n texconfig -l pl.UTF-8
Konfigurator systemu składu TeX.

%package -n xdvi
Summary:	X11 previewer
Summary(de.UTF-8):	X11-Previewer
Summary(es.UTF-8):	Visualizador TeX X11
Summary(fr.UTF-8):	Prévisualisateur X11
Summary(pl.UTF-8):	Przeglądarka DVI dla X11
Summary(pt_BR.UTF-8):	Visualizador TeX X11
Summary(tr.UTF-8):	X11 öngörüntüleyici
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Suggests:	%{name}-dvips
Obsoletes:	tetex-xdvi < 1.0-2

%description -n xdvi
xdvi is a program which runs under the X window system. It is used to
preview dvi files, such as are produced by tex and latex.

%description -n xdvi -l de.UTF-8
xdvi ist ein Programm, das unter dem X-Window-System läuft und gewohnt
ist, dvi-Dateien als Vorschau anzuzeigen, etwa solche, die von tex und
latex erzeugt wurden.

%description -n xdvi -l es.UTF-8
xdvi es un programa que se ejecuta en el sistema X Window. Se usa para
visualizar archivos dvi, como los producidos por tex y latex.

%description -n xdvi -l fr.UTF-8
xdvi est un programme s'exécutant sous le système X Window. Il sert à
visualiser les fichiers dvi tels que ceux produits par tex et latex.

%description -n xdvi -l pl.UTF-8
Xdvi jest programem (działającym w X Window System) do przeglądania
plików DVI, produkowanych przez TeXa i LaTeXa.

%description -n xdvi -l pt_BR.UTF-8
xdvi é um programa que roda no sistema X Window. É usado para
visualizar arquivos dvi, como os produzidos por tex e latex.

%package -n xindy
Summary:	Creating sorted and tagged index from raw index
Summary(hu.UTF-8):	Xindy rendezett és cimkézett indexet készít nyers indexekből
Summary(pl.UTF-8):	Tworzenie posortowanego i pooznaczanego indeksu z surowego
Group:		Applications/Publishing/TeX

%description -n xindy
Xindy creates sorted and tagged index from raw index.

%description -n xindy -l hu.UTF-8
Xindy rendezett és cimkézett indexet készít nyers indexekből.

%description -n xindy -l pl.UTF-8
Xindy tworzy posortowany i pooznaczany indeks z surowego.

%package -n xindy-albanian
Summary:	Xindy Albanian language
Summary(hu.UTF-8):	Xindy albán nyelv
Summary(pl.UTF-8):	Obsługa języka albańskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-albanian
Xindy Albanian language.

%description -n xindy-albanian -l hu.UTF-8
Xindy albán nyelv

%description -n xindy-albanian -l pl.UTF-8
Obsługa języka albańskiego do Xindy.

%package -n xindy-belarusian
Summary:	Xindy Belarusian language
Summary(hu.UTF-8):	Xindy belorusz nyelv
Summary(pl.UTF-8):	Obsługa języka białoruskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-belarusian
Xindy Belarusian language.

%description -n xindy-belarusian -l hu.UTF-8
Xindy belorusz nyelv.

%description -n xindy-belarusian -l pl.UTF-8
Obsługa języka białoruskiego do Xindy.

%package -n xindy-bulgarian
Summary:	Xindy Bulgarian language
Summary(hu.UTF-8):	Xindy bolgár nyelv
Summary(pl.UTF-8):	Obsługa języka bułgarskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-bulgarian
Xindy Bulgarian language.

%description -n xindy-bulgarian -l hu.UTF-8
Xindy bolgár nyelv.

%description -n xindy-bulgarian -l pl.UTF-8
Obsługa języka bułgarskiego do Xindy.

%package -n xindy-croatian
Summary:	Xindy Croatian language
Summary(hu.UTF-8):	Xindy horvát nyelv
Summary(pl.UTF-8):	Obsługa języka chrowackiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-croatian
Xindy Croatian language.

%description -n xindy-croatian -l hu.UTF-8
Xindy horvát nyelv.

%description -n xindy-croatian -l pl.UTF-8
Obsługa języka chrowackiego do Xindy.

%package -n xindy-czech
Summary:	Xindy Czech language
Summary(hu.UTF-8):	Xindy cseh nyelv
Summary(pl.UTF-8):	Obsługa języka czeskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-czech
Xindy Czech language.

%description -n xindy-czech -l hu.UTF-8
Xindy cseh nyelv.

%description -n xindy-czech -l pl.UTF-8
Obsługa języka czeskiego do Xindy.

%package -n xindy-danish
Summary:	Xindy Danish language
Summary(hu.UTF-8):	Xindy dán nyelv
Summary(pl.UTF-8):	Obsługa języka duńskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-danish
Xindy Danish language.

%description -n xindy-danish -l hu.UTF-8
Xindy dán nyelv.

%description -n xindy-danish -l pl.UTF-8
Obsługa języka duńskiego do Xindy.

%package -n xindy-dutch
Summary:	Xindy Dutch language
Summary(hu.UTF-8):	Xindy holland nyelv
Summary(pl.UTF-8):	Obsługa języka holenderskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-dutch
Xindy Dutch language.

%description -n xindy-dutch -l hu.UTF-8
Xindy holland nyelv.

%description -n xindy-dutch -l pl.UTF-8
Obsługa języka holenderskiego do Xindy.

%package -n xindy-english
Summary:	Xindy English language
Summary(hu.UTF-8):	Xindy angol nyelv
Summary(pl.UTF-8):	Obsługa języka angielskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-english
Xindy English language.

%description -n xindy-english -l hu.UTF-8
Xindy angol nyelv.

%description -n xindy-english -l pl.UTF-8
Obsługa języka angielskiego do Xindy.

%package -n xindy-esperanto
Summary:	Xindy Esperanto language
Summary(hu.UTF-8):	Xindy eszperantó nyelv
Summary(pl.UTF-8):	Obsługa języka esperanto do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-esperanto
Xindy Esperanto language.

%description -n xindy-esperanto -l hu.UTF-8
Xindy eszperantó nyelv.

%description -n xindy-esperanto -l pl.UTF-8
Obsługa języka esperanto do Xindy.

%package -n xindy-estonian
Summary:	Xindy Estonian language
Summary(hu.UTF-8):	Xindy észt nyelv
Summary(pl.UTF-8):	Obsługa języka estońskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-estonian
Xindy Estonian language.

%description -n xindy-estonian -l hu.UTF-8
Xindy észt nyelv.

%description -n xindy-estonian -l pl.UTF-8
Obsługa języka estońskiego do Xindy.

%package -n xindy-finnish
Summary:	Xindy Finnish language
Summary(hu.UTF-8):	Xindy finn nyelv
Summary(pl.UTF-8):	Obsługa języka fińskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-finnish
Xindy Finnish language.

%description -n xindy-finnish -l hu.UTF-8
Xindy finn nyelv.

%description -n xindy-finnish -l pl.UTF-8
Obsługa języka fińskiego do Xindy.

%package -n xindy-french
Summary:	Xindy French language
Summary(hu.UTF-8):	Xindy francia nyelv
Summary(pl.UTF-8):	Obsługa języka francuskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-french
Xindy French language.

%description -n xindy-french -l hu.UTF-8
Xindy francia nyelv.

%description -n xindy-french -l pl.UTF-8
Obsługa języka francuskiego do Xindy.

%package -n xindy-general
Summary:	Xindy general language
Summary(hu.UTF-8):	Xindy általános nyelv
Summary(pl.UTF-8):	Obsługa języka ogólnego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-general
Xindy general language.

%description -n xindy-general -l hu.UTF-8
Xindy általános nyelv.

%description -n xindy-general -l pl.UTF-8
Obsługa języka ogólnego do Xindy.

%package -n xindy-georgian
Summary:	Xindy Georgian language
Summary(hu.UTF-8):	Xindy georgian nyelv
Summary(pl.UTF-8):	Obsługa języka gruzińskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-georgian
Xindy Georgian language.

%description -n xindy-georgian -l hu.UTF-8
Xindy georgian nyelv.

%description -n xindy-georgian -l pl.UTF-8
Obsługa języka gruzińskiego do Xindy.

%package -n xindy-german
Summary:	Xindy german language
Summary(hu.UTF-8):	Xindy német nyelv
Summary(pl.UTF-8):	Obsługa języka niemieckiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-german
Xindy German language.

%description -n xindy-german -l hu.UTF-8
Xindy német nyelv.

%description -n xindy-german -l pl.UTF-8
Obsługa języka niemieckiego do Xindy.

%package -n xindy-greek
Summary:	Xindy Greek language
Summary(hu.UTF-8):	Xindy görög nyelv
Summary(pl.UTF-8):	Obsługa języka greckiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-greek
Xindy Greek language.

%description -n xindy-greek -l hu.UTF-8
Xindy görög nyelv.

%description -n xindy-greek -l pl.UTF-8
Obsługa języka greckiego do Xindy.

%package -n xindy-gypsy
Summary:	Xindy Gypsy language
Summary(hu.UTF-8):	Xindy cigány nyelv
Summary(pl.UTF-8):	Obsługa języka cygańskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-gypsy
Xindy Gypsy language.

%description -n xindy-gypsy -l hu.UTF-8
Xindy cigány nyelv.

%description -n xindy-gypsy -l pl.UTF-8
Obsługa języka cygańskiego do Xindy.

%package -n xindy-hausa
Summary:	Xindy Hausa language
Summary(hu.UTF-8):	Xindy hausa nyelv
Summary(pl.UTF-8):	Obsługa języka hausa do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-hausa
Xindy Hausa language.

%description -n xindy-hausa -l hu.UTF-8
Xindy hausa nyelv.

%description -n xindy-hausa -l pl.UTF-8
Obsługa języka hausa do Xindy.

%package -n xindy-hebrew
Summary:	Xindy Hebrew language
Summary(hu.UTF-8):	Xindy héber nyelv
Summary(pl.UTF-8):	Obsługa języka hebrajskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-hebrew
Xindy Hebrew language.

%description -n xindy-hebrew -l hu.UTF-8
Xindy héber nyelv.

%description -n xindy-hebrew -l pl.UTF-8
Obsługa języka hebrajskiego do Xindy.

%package -n xindy-hungarian
Summary:	Xindy Hungarian language
Summary(hu.UTF-8):	Xindy magyar nyelv
Summary(pl.UTF-8):	Obsługa języka węgierskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-hungarian
Xindy Hungarian language.

%description -n xindy-hungarian -l hu.UTF-8
Xindy magyar nyelv.

%description -n xindy-hungarian -l pl.UTF-8
Obsługa języka węgierskiego do Xindy.

%package -n xindy-icelandic
Summary:	Xindy Icelandic language
Summary(hu.UTF-8):	Xindy izlandi nyelv
Summary(pl.UTF-8):	Obsługa języka islandzkiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-icelandic
Xindy Icelandic language.

%description -n xindy-icelandic -l hu.UTF-8
Xindy izlandi nyelv.

%description -n xindy-icelandic -l pl.UTF-8
Obsługa języka islandzkiego do Xindy.

%package -n xindy-italian
Summary:	Xindy Italian language
Summary(hu.UTF-8):	Xindy olasz nyelv
Summary(pl.UTF-8):	Obsługa języka włoskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-italian
Xindy Italian language.

%description -n xindy-italian -l hu.UTF-8
Xindy olasz nyelv.

%description -n xindy-italian -l pl.UTF-8
Obsługa języka włoskiego do Xindy.

%package -n xindy-klingon
Summary:	Xindy Klingon language
Summary(hu.UTF-8):	Xindy klingon nyelv
Summary(pl.UTF-8):	Obsługa języka klingońskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-klingon
Xindy Klingon language.

%description -n xindy-klingon -l hu.UTF-8
Xindy klingon nyelv.

%description -n xindy-klingon -l pl.UTF-8
Obsługa języka klingońskiego do Xindy.

%package -n xindy-kurdish
Summary:	Xindy Kurdish language
Summary(hu.UTF-8):	Xindy kurd nyelv
Summary(pl.UTF-8):	Obsługa języka kurdyjskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-kurdish
Xindy Kurdish language.

%description -n xindy-kurdish -l hu.UTF-8
Xindy kurd nyelv.

%description -n xindy-kurdish -l pl.UTF-8
Obsługa języka kurdyjskiego do Xindy.

%package -n xindy-latin
Summary:	Xindy Latin language
Summary(hu.UTF-8):	Xindy latin nyelv
Summary(pl.UTF-8):	Obsługa języka łacińskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-latin
Xindy Latin language.

%description -n xindy-latin -l hu.UTF-8
Xindy latin nyelv.

%description -n xindy-latin -l pl.UTF-8
Obsługa języka łacińskiego do Xindy.

%package -n xindy-latvian
Summary:	Xindy Latvian language
Summary(hu.UTF-8):	Xindy lett nyelv
Summary(pl.UTF-8):	Obsługa języka łotewskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-latvian
Xindy Latvian language.

%description -n xindy-latvian -l hu.UTF-8
Xindy lett nyelv.

%description -n xindy-latvian -l pl.UTF-8
Obsługa języka łotewskiego do Xindy.

%package -n xindy-lithuanian
Summary:	Xindy Lithuanian language
Summary(hu.UTF-8):	Xindy litván nyelv
Summary(pl.UTF-8):	Obsługa języka litewskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-lithuanian
Xindy Lithuanian language.

%description -n xindy-lithuanian -l hu.UTF-8
Xindy litván nyelv.

%description -n xindy-lithuanian -l pl.UTF-8
Obsługa języka litewskiego do Xindy.

%package -n xindy-lower-sorbian
Summary:	Xindy Lower-Sorbian language
Summary(hu.UTF-8):	Xindy lower-sorbian nyelv
Summary(pl.UTF-8):	Obsługa języka dolnołużyckiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-lower-sorbian
Xindy Lower-Sorbian language.

%description -n xindy-lower-sorbian -l hu.UTF-8
Xindy lower-sorbian nyelv.

%description -n xindy-lower-sorbian -l pl.UTF-8
Obsługa języka dolnołużyckiego do Xindy.

%package -n xindy-macedonian
Summary:	Xindy Macedonian language
Summary(hu.UTF-8):	Xindy macedón nyelv
Summary(pl.UTF-8):	Obsługa języka macedońskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-macedonian
Xindy Macedonian language.

%description -n xindy-macedonian -l hu.UTF-8
Xindy macedón nyelv.

%description -n xindy-macedonian -l pl.UTF-8
Obsługa języka macedońskiego do Xindy.

%package -n xindy-mongolian
Summary:	Xindy Mongolian language
Summary(hu.UTF-8):	Xindy mongol nyelv
Summary(pl.UTF-8):	Obsługa języka mongolskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-mongolian
Xindy Mongolian language.

%description -n xindy-mongolian -l hu.UTF-8
Xindy mongol nyelv.

%description -n xindy-mongolian -l pl.UTF-8
Obsługa języka mongolskiego do Xindy.

%package -n xindy-norwegian
Summary:	Xindy Norwegian language
Summary(hu.UTF-8):	Xindy norvég nyelv
Summary(pl.UTF-8):	Obsługa języka norweskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-norwegian
Xindy Norwegian language.

%description -n xindy-norwegian -l hu.UTF-8
Xindy norvég nyelv.

%description -n xindy-norwegian -l pl.UTF-8
Obsługa języka norweskiego do Xindy.

%package -n xindy-polish
Summary:	Xindy Polish language
Summary(hu.UTF-8):	Xindy lengyel nyelv
Summary(pl.UTF-8):	Obsługa języka polskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-polish
Xindy Polish language.

%description -n xindy-polish -l hu.UTF-8
Xindy lengyel nyelv.

%description -n xindy-polish -l pl.UTF-8
Obsługa języka polskiego do Xindy.

%package -n xindy-portuguese
Summary:	Xindy Portuguese language
Summary(hu.UTF-8):	Xindy portugál nyelv
Summary(pl.UTF-8):	Obsługa języka portugalskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-portuguese
Xindy Portuguese language.

%description -n xindy-portuguese -l hu.UTF-8
Xindy portugál nyelv.

%description -n xindy-portuguese -l pl.UTF-8
Obsługa języka portugalskiego do Xindy.

%package -n xindy-romanian
Summary:	Xindy Romanian language
Summary(hu.UTF-8):	Xindy román nyelv
Summary(pl.UTF-8):	Obsługa języka rumuńskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-romanian
Xindy Romanian language.

%description -n xindy-romanian -l hu.UTF-8
Xindy román nyelv.

%description -n xindy-romanian -l pl.UTF-8
Obsługa języka rumuńskiego do Xindy.

%package -n xindy-russian
Summary:	Xindy Russian language
Summary(hu.UTF-8):	Xindy orosz nyelv
Summary(pl.UTF-8):	Obsługa języka rosyjskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-russian
Xindy Russian language.

%description -n xindy-russian -l hu.UTF-8
Xindy orosz nyelv.

%description -n xindy-russian -l pl.UTF-8
Obsługa języka rosyjskiego do Xindy.

%package -n xindy-serbian
Summary:	Xindy Serbian language
Summary(hu.UTF-8):	Xindy szerb nyelv
Summary(pl.UTF-8):	Obsługa języka serbskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-serbian
Xindy Serbian language.

%description -n xindy-serbian -l hu.UTF-8
Xindy szerb nyelv.

%description -n xindy-serbian -l pl.UTF-8
Obsługa języka serbskiego do Xindy.

%package -n xindy-slovak
Summary:	Xindy Slovak language
Summary(hu.UTF-8):	Xindy szlovák nyelv
Summary(pl.UTF-8):	Obsługa języka słowackiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-slovak
Xindy Slovak language.

%description -n xindy-slovak -l hu.UTF-8
Xindy szlovák nyelv.

%description -n xindy-slovak -l pl.UTF-8
Obsługa języka słowackiego do Xindy.

%package -n xindy-slovenian
Summary:	Xindy Slovenian language
Summary(hu.UTF-8):	Xindy szlovén nyelv
Summary(pl.UTF-8):	Obsługa języka słoweńskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-slovenian
Xindy Slovenian language.

%description -n xindy-slovenian -l hu.UTF-8
Xindy szlovén nyelv.

%description -n xindy-slovenian -l pl.UTF-8
Obsługa języka słoweńskiego do Xindy.

%package -n xindy-spanish
Summary:	Xindy Spanish language
Summary(hu.UTF-8):	Xindy spanyol nyelv
Summary(pl.UTF-8):	Obsługa języka hiszpańskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-spanish
Xindy Spanish language.

%description -n xindy-spanish -l hu.UTF-8
Xindy spanyol nyelv.

%description -n xindy-spanish -l pl.UTF-8
Obsługa języka hiszpańskiego do Xindy.

%package -n xindy-swedish
Summary:	Xindy Swedish language
Summary(hu.UTF-8):	Xindy svéd nyelv
Summary(pl.UTF-8):	Obsługa języka szwedzkiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-swedish
Xindy Swedish language.

%description -n xindy-swedish -l hu.UTF-8
Xindy svéd nyelv.

%description -n xindy-swedish -l pl.UTF-8
Obsługa języka szwedzkiego do Xindy.

%package -n xindy-turkish
Summary:	Xindy Turkish language
Summary(hu.UTF-8):	Xindy török nyelv
Summary(pl.UTF-8):	Obsługa języka tureckiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-turkish
Xindy Turkish language.

%description -n xindy-turkish -l hu.UTF-8
Xindy török nyelv.

%description -n xindy-turkish -l pl.UTF-8
Obsługa języka tureckiego do Xindy.

%package -n xindy-ukrainian
Summary:	Xindy Ukrainian language
Summary(hu.UTF-8):	Xindy ukrán nyelv
Summary(pl.UTF-8):	Obsługa języka ukraińskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-ukrainian
Xindy Ukrainian language.

%description -n xindy-ukrainian -l hu.UTF-8
Xindy ukrán nyelv.

%description -n xindy-ukrainian -l pl.UTF-8
Obsługa języka ukraińskiego do Xindy.

%package -n xindy-upper-sorbian
Summary:	Xindy Upper-Sorbian language
Summary(hu.UTF-8):	Xindy upper-sorbian nyelv
Summary(pl.UTF-8):	Obsługa języka górnołużyckiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-upper-sorbian
Xindy Upper-Sorbian language.

%description -n xindy-upper-sorbian -l hu.UTF-8
Xindy upper-sorbian nyelv.

%description -n xindy-upper-sorbian -l pl.UTF-8
Obsługa języka górnołużyckiego do Xindy.

%package -n xindy-vietnamese
Summary:	Xindy Vietnamese language
Summary(hu.UTF-8):	Xindy vietnámi nyelv
Summary(pl.UTF-8):	Obsługa języka wietnamskiego do Xindy
Group:		Applications/Publishing/TeX
Requires:	xindy = %{epoch}:%{version}-%{release}

%description -n xindy-vietnamese
Xindy Vietnamese language.

%description -n xindy-vietnamese -l hu.UTF-8
Xindy vietnám nyelv.

%description -n xindy-vietnamese -l pl.UTF-8
Obsługa języka wietnamskiego do Xindy.

%package pdftex
Summary:	TeX generating PDF files instead DVI
Summary(hu.UTF-8):	PDF fájlok készítése DVI helyett TeX-ből
Summary(pl.UTF-8):	TeX generujący pliki PDF zamiast DVI
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-type1-bluesky = %{epoch}:%{version}-%{release}
Requires:	ghostscript
Provides:	tetex-format-pdftex = %{epoch}:%{version}-%{release}
Provides:	tetex-pdftex
Obsoletes:	tetex-format-pdftex < 1:3.1
Obsoletes:	tetex-pdftex < 1:3.1

%description pdftex
TeX generating PDF files instead DVI.

%description pdftex -l pl.UTF-8
TeX generujący pliki PDF zamiast DVI.

%package psutils
Summary:	PostScript Utilities
Summary(hu.UTF-8):	PostScript eszközök
Summary(pl.UTF-8):	Narzędzia do PostScriptu
Group:		Applications/Printing
Provides:	psutils
Obsoletes:	psutils < 1.18
Obsoletes:	texlive-epsutils < 1:20080816-5
Obsoletes:	texlive-filters < 1:20080816-5

%description psutils
This archive contains some utilities for manipulating PostScript
documents. Page selection and rearrangement are supported, including
arrangement into signatures for booklet printing, and page merging for
n-up printing.

%description psutils -l hu.UTF-8
Ez a csomag jónéhány eszközt tartalmaz, amellyel a PostScript
dokumentumok manipulálhatók. Oldal kijelölés és átrendezés támogatott,
beleértve a booklet nyomtatáshoz való átrendezést is.

%description psutils -l pl.UTF-8
PSutils zawiera programy pomagające manipulować plikami PostScript,
wybierać strony przeznaczone do wydruku, ich kolejność, układ. Pozwala
także na łączenie różnych plików PostScript w całość.

%package phyzzx
Summary:	A TeX format for physicists
Summary(hu.UTF-8):	TeX formátum fizikusoknak
Summary(pl.UTF-8):	Format TeXa dla fizyków
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description phyzzx
A TeX format for physicists.

%description phyzzx -l hu.UTF-8
TeX formátum fizikusoknak.

%description phyzzx -l pl.UTF-8
Format TeXa dla fizyków.

%package omega
Summary:	Extended unicode TeX
Summary(pl.UTF-8):	Omega - TeX ze wsparciem dla unikodu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-omega = %{epoch}:%{version}-%{release}
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-omega < 1:3.1

%description omega
Omega is a version of the TeX program modified for multilingual
typesetting. It uses unicode, and has additional primitives for (among
other things) bidirectional typesetting.

%description omega -l pl.UTF-8
Omega to wersja TeXa zmodyfikowana dla potrzeb składu wielojęzycznego.
Używa unikodu i ma dodatkowe prymitywy do (między innymi) składania
tekstu pisanego w obu kierunkach.

# # formats #

# Plain format.

%package plain
Summary:	Plain TeX format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla formatu Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-format-plain
Provides:	tetex-plain
Obsoletes:	tetex-cyrplain < 1:3.1
Obsoletes:	tetex-format-cyrplain < 1:3.1
Obsoletes:	tetex-format-plain < 1:3.1
Obsoletes:	tetex-plain < 1:3.1
BuildArch:	noarch

%description plain
Plain TeX format basic files.

%description plain -l pl.UTF-8
Podstawowe pliki dla formatu Plain TeX.

# MeX Plain format

%package mex
Summary:	MeX Plain Format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla format MeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	texlive-fonts-pl = %{epoch}:%{version}-%{release}
Requires:	texlive-plain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-mex < 1:3.1
BuildArch:	noarch

%description mex
MeX Plain Format basic files.

%description mex -l pl.UTF-8
Podstawowe pliki dla formatu MeX Plain.

%package format-mex
Summary:	MeX Plain Format
Summary(pl.UTF-8):	Format MeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	texlive-mex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-mex < 1:3.1
BuildArch:	noarch

%description format-mex
MeX Plain Format.

%description format-mex -l pl.UTF-8
Format MeX Plain.

%package format-pdfmex
Summary:	PDFMeX Plain Format
Summary(pl.UTF-8):	Format PDFMeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-mex = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-pdfmex < 1:3.1
BuildArch:	noarch

%description format-pdfmex
PDFMeX Plain Format.

%description format-pdfmex -l pl.UTF-8
Format PDFMeX Plain.

%package format-utf8mex
Summary:	MeX Plain Format with UTF-8 encoded source files
Summary(pl.UTF-8):	Format MeX Plain z plikami źródłowymi kodowanymi UTF-8
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-mex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-utf8mex < 1:3.1
BuildArch:	noarch

%description format-utf8mex
MeX Plain Format with UTF-8 encoded source files.

%description format-utf8mex -l pl.UTF-8
Format MeX Plain z plikami źródłowymi kodowanymi UTF-8.

# AMS TeX format

%package amstex
Summary:	AMS macros for Plain TeX basic files
Summary(pl.UTF-8):	Podstawowe pliki makr AMS dla formatu Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-ams = %{epoch}:%{version}-%{release}
Requires:	%{name}-format-amstex = %{epoch}:%{version}-%{release}
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Provides:	tetex-ams
Obsoletes:	tetex-ams < 1:2.0
Obsoletes:	tetex-amstex < 1:3.1
Obsoletes:	tetex-plain-amsfonts < 1:3.1
BuildArch:	noarch

%description amstex
American Mathematical Society macros for Plain TeX basic files.

%description amstex -l pl.UTF-8
Podstawowe pliki makr AMS (American Mathematical Society) dla formatu
Plain TeX.

%package format-amstex
Summary:	AMS macros for Plain TeX
Summary(pl.UTF-8):	Makra AMS dla formatu Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-amstex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-amstex < 1:3.1
Obsoletes:	tetex-format-cyramstex < 1:3.1
BuildArch:	noarch

%description format-amstex
American Mathematical Society macros for Plain TeX.

%description format-amstex -l pl.UTF-8
Makra AMS (American Mathematical Society) dla formatu Plain TeX.

# CSPlain format

%package csplain
Summary:	TeX CSPlain format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla formatu TeX CSPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-cs = %{epoch}:%{version}-%{release}
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Provides:	tetex-csplain
Obsoletes:	tetex-csplain < 1:3.1
BuildArch:	noarch

%description csplain
TeX CSPlain format basic files.

%description csplain -l pl.UTF-8
Podstawowe pliki dla formatu TeX CSPlain.

%package format-csplain
Summary:	TeX CSPlain format
Summary(pl.UTF-8):	Format TeX CSPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-csplain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-csplain < 1:3.1
BuildArch:	noarch

%description format-csplain
TeX CSPlain format.

%description format-csplain -l pl.UTF-8
Format TeX CSPlain.

%package format-pdfcsplain
Summary:	PDFTeX CSPlain format
Summary(pl.UTF-8):	Format PDFTeX CSPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-csplain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-pdfcsplain < 1:3.1
BuildArch:	noarch

%description format-pdfcsplain
PDFTeX CSPlain format.

%description format-pdfcsplain -l pl.UTF-8
Format PDFTeX CSPlain.

# CSLaTeX format

%package cslatex
Summary:	CSLaTeX format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla formatu CSLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-cs = %{epoch}:%{version}-%{release}
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Provides:	tetex-cslatex
Obsoletes:	tetex-cslatex < 1:3.1
BuildArch:	noarch

%description cslatex
CSLaTeX format basic files.

%description cslatex -l pl.UTF-8
Podstawowe pliki dla formatu CSLaTeX.

%package format-cslatex
Summary:	CSLaTeX format
Summary(pl.UTF-8):	Format CSLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-cslatex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-cslatex < 1:3.1
BuildArch:	noarch

%description format-cslatex
CSLaTeX format.

%description format-cslatex -l pl.UTF-8
Format CSLaTeX.

%package format-pdfcslatex
Summary:	PDF CSLaTeX format
Summary(pl.UTF-8):	Format PDF CSLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-cslatex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-pdfcslatex < 1:3.1
BuildArch:	noarch

%description format-pdfcslatex
PDF CSLaTeX format.

%description format-pdfcslatex -l pl.UTF-8
Format PDF CSLaTeX.

# EPlain format

%package eplain
Summary:	EPlain format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla formatu EPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-eplain < 1:3.1
Obsoletes:	tetex-etex < 1:2.0
BuildArch:	noarch

%description eplain
EPlain format basic files.

%description eplain -l pl.UTF-8
Podstawowe pliki dla formatu EPlain.

%package format-eplain
Summary:	EPlain format
Summary(pl.UTF-8):	Format EPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-eplain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-eplain < 1:3.1
BuildArch:	noarch

%description format-eplain
EPlain format.

%description format-eplain -l pl.UTF-8
Format EPlain.

# ConTeXt format.

%package context
Summary:	ConTeXt macro package basic files
Summary(pl.UTF-8):	Podstawowe pliki pakietu makr ConTeXt
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
# contains texlua scripts
Requires:	%{name}-luatex = %{epoch}:%{version}-%{release}
Provides:	tetex-context
Obsoletes:	tetex-context < 1:3.1
BuildArch:	noarch

%description context
A full featured, parameter driven macro package, which fully supports
advanced interactive documents.

This package contains basic files.

%description context -l pl.UTF-8
Pakiet makr sterowanych przez parametry o pełnych możliwościach,
całkowicie obsługujący zaawansowane dokumenty interaktywne.

Ten pakiet zawiera podstawowe pliki.

%package format-context-de
Summary:	German ConTeXt format
Summary(pl.UTF-8):	Niemiecka wersja formatu ConTeXt
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-context = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-context-de < 1:3.1
BuildArch:	noarch

%description format-context-de
German ConTeXt format.

%description format-context-de -l pl.UTF-8
Niemiecka wersja formatu ConTeXt.

%package format-context-en
Summary:	English ConTeXt format
Summary(pl.UTF-8):	Angielska wersja formatu ConTeXt
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-context = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-context-en < 1:3.1
BuildArch:	noarch

%description format-context-en
English ConTeXt format.

%description format-context-en -l pl.UTF-8
Angielska wersja formatu ConTeXt.

%package format-context-nl
Summary:	Dutch ConTeXt format
Summary(pl.UTF-8):	Holenderska wersja formatu ConTeXt
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-context = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-context-nl < 1:3.1
BuildArch:	noarch

%description format-context-nl
Dutch ConTeXt format.

%description format-context-nl -l pl.UTF-8
Holenderska wersja formatu ConTeXt.

# LaTeX format.

%package latex
Summary:	LaTeX macro package basic files
Summary(pl.UTF-8):	Podstawowe pliki pakietu makr LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-ruhyphen = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-ukrhyph = %{epoch}:%{version}-%{release}
# for misc/eurosym:
Requires:	%{name}-fonts-eurosym = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-babel = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
Suggests:	%{name}-fonts-jknappen
Suggests:	%{name}-latex-ucs = %{epoch}:%{version}-%{release}
Provides:	tetex-format-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-koma-script < 1:3.1
Obsoletes:	tetex-format-latex < 1:3.1
Obsoletes:	tetex-latex < 1:3.1
Obsoletes:	tetex-latex-SIunits < 1:3.1
Obsoletes:	tetex-latex-caption < 1:3.1
Obsoletes:	tetex-latex-curves < 1:3.1
Obsoletes:	tetex-latex-dinbrief < 1:3.1
Obsoletes:	tetex-latex-draftcopy < 1:3.1
Obsoletes:	tetex-latex-dstroke < 1:3.1
Obsoletes:	tetex-latex-dvilj < 1:3.1
Obsoletes:	tetex-latex-eepic < 1:3.1
Obsoletes:	tetex-latex-endfloat < 1:3.1
Obsoletes:	tetex-latex-fancyhdr < 1:3.1
Obsoletes:	tetex-latex-fancyheadings < 1:3.1
Obsoletes:	tetex-latex-fancyvrb < 1:3.1
Obsoletes:	tetex-latex-fp < 1:3.1
Obsoletes:	tetex-latex-graphics < 1:3.1
Obsoletes:	tetex-latex-hyperref < 1:3.1
Obsoletes:	tetex-latex-koma-script < 1:3.1
Obsoletes:	tetex-latex-labels < 1:3.1
Obsoletes:	tetex-latex-listings < 1:3.1
Obsoletes:	tetex-latex-misc < 1:3.1
Obsoletes:	tetex-latex-ms < 1:3.1
Obsoletes:	tetex-latex-multirow < 1:3.1
Obsoletes:	tetex-latex-mwcls < 1:3.1
Obsoletes:	tetex-latex-mwdtools < 1:3.1
Obsoletes:	tetex-latex-ntgclass < 1:3.1
Obsoletes:	tetex-latex-oberdiek < 1:3.1
Obsoletes:	tetex-latex-pb-diagram < 1:3.1
Obsoletes:	tetex-latex-pstricks < 1:3.1
Obsoletes:	tetex-latex-qfonts < 1:3.1
Obsoletes:	tetex-latex-revtex4 < 1:3.1
Obsoletes:	tetex-latex-seminar < 1:3.1
Obsoletes:	tetex-latex-t2 < 1:3.1
Obsoletes:	tetex-latex-titlesec < 1:3.1
Obsoletes:	tetex-latex-tools < 1:3.1
Obsoletes:	tetex-latex-units < 1:3.1
Obsoletes:	tetex-mwcls < 20030510
Obsoletes:	tetex-revtex4 < rc4-3

%description latex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains basic files.

%description latex -l pl.UTF-8
LaTeX jest frontendem do systemu formatującego tekst TeX. Jest
łatwiejszy w użyciu niż TeX. Jest właściwie zestawem makr TeXowych,
dających użytkownikom wygodne, predefiniowane formaty dokumentów.

Ten pakiet zawiera podstawowe pliki.

%package latex-colortab
Summary:	Shade cells of tables and halign
Summary(pl.UTF-8):	Wyszarzanie komórek tabel i halign
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-colortab
Shade cells of tables and halign.

%description latex-colortab -l pl.UTF-8
Wyszarzanie komórek tabel i halign

%package latex-12many
Summary:	Generalising mathematical index sets
Summary(hu.UTF-8):	A matematikai halmazok indexelésének általánosítása
Summary(pl.UTF-8):	Uogólnienie zbiorów indeksów matematycznych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-12many
Generalising mathematical index sets.

%description latex-12many -l hu.UTF-8
A matematikai halmazok indexelésének általánosítása.

%description latex-12many -l pl.UTF-8
Uogólnienie zbiorów indeksów matematycznych.

%package latex-abstract
Summary:	Control the typesetting of the abstract environment
Summary(hu.UTF-8):	Az "abstract" környezet szedésének irányítása
Summary(pl.UTF-8):	Sterowanie składem środowiska abstract
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-abstract
Control the typesetting of the abstract environment.

%description latex-abstract -l hu.UTF-8
Az "abstract" környezet szedésének irányítása.

%description latex-abstract -l pl.UTF-8
Sterowanie składem środowiska abstract.

%package latex-accfonts
Summary:	Utilities to derive new fonts from existing ones
Summary(hu.UTF-8):	Eszközök új betűtípusok származtatására már létezőkből
Summary(pl.UTF-8):	Narzędzia do tworzenia nowych fontów w oparciu o istniejące
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
BuildArch:	noarch

%description latex-accfonts
Utilities to derive new fonts from existing ones.

%description latex-accfonts -l hu.UTF-8
Eszközök új betűtípusok származtatására már létezőkből.

%description latex-accfonts -l pl.UTF-8
Narzędzia do tworzenia nowych fontów w oparciu o istniejące.

%package latex-adrconv
Summary:	BibTeX styles to implement an address database
Summary(hu.UTF-8):	BibTeX stílusok cím-adatbázis megvalósításához
Summary(pl.UTF-8):	Style BibTeXa do implementowania bazy danych adresów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-adrconv
BibTeX styles to implement an address database.

%description latex-adrconv -l hu.UTF-8
BibTeX stílusok cím-adatbázis megvalósításához.

%description latex-adrconv -l pl.UTF-8
Style BibTeXa do implementowania bazy danych adresów.

%package latex-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Summary(pl.UTF-8):	Wirtualne fonty dla plików PDF z fontami CMR o kodowaniu T1
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-ae = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-ae
Obsoletes:	tetex-latex-ae < 1:3.1
BuildArch:	noarch

%description latex-ae
A set of virtual fonts which emulates T1 coded fonts using the
standard CM fonts. The package is called AE fonts (for Almost
European). The main use of the package is to produce PDF files using
versions of the CM fonts instead of the bitmapped EC fonts.

%description latex-ae -l pl.UTF-8
Zestaw wirtualnych fontów emulujących fonty o kodowaniu T1 przy użyciu
standardowych fontów CM. Ten pakiet został nazwany AE (Almost European
- prawie europejskie). Głównym przeznaczeniem tego pakietu jest
  produkowanie plików PDF przy użyciu wersji fontów CM zamiast
  bitmapowych fontów EC.

%package latex-algorithms
Summary:	Floating algorithm environment
Summary(pl.UTF-8):	Pływające środowisko dla algorytmów
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-algorith < 1:3.1
Obsoletes:	tetex-latex-algorithms < 1:3.1
BuildArch:	noarch

%description latex-algorithms
Defines a floating algorithm environment designed to work with the
algorithmic package.

%description latex-algorithms -l pl.UTF-8
Pakiet definiujący pływające środowisko dla algorytmów zaprojektowane
do pracy z pakietem algorithmic.

%package latex-ams
Summary:	AMS math facilities for LaTeX
Summary(pl.UTF-8):	Udogodnienia matematyczne AMS dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-ams = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-ams
Obsoletes:	tetex-latex-ams < 1:3.1
Obsoletes:	tetex-latex-amscls < 1:3.1
Obsoletes:	tetex-latex-amsfonts < 1:3.1
Obsoletes:	tetex-latex-amsmath < 1:3.1
BuildArch:	noarch

%description latex-ams
This package is the principal package in the AMS-LaTeX distribution.
It adapts for use in LaTeX most of the mathematical features found in
AMS-TeX.

%description latex-ams -l pl.UTF-8
To jest główny pakiet dystrybucji AMS-LaTeX. Jest adaptacją większości
możliwości matematycznych AMS-TeXa do używania w LaTeXu.

%package latex-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl.UTF-8):	Antykwa Półtawskiego - rodzina tradycyjnych czcionek polskich jako Type 1
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-antp = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-antp < 1:3.1
BuildArch:	noarch

%description latex-antp
A replica of Antykwa Poltawskiego font in PostScript Type 1 format
- -- preliminary version. This font was designed in the 'twenties and
  the 'thirties of XX century by a Polish graphic artist and a
  typographer Adam Poltawski. It was widely used by Polish printing
  houses as long as metal types were in use (until ca the 'sixties).
  Perhaps the first complete font family programmed and parametrized in
  METAPOST.

%description latex-antp -l pl.UTF-8
Wstępna wersja repliki kroju Antykwa Półtawskiego w formacie
PostScript Type 1. Ten krój został opracowany w latach 30-tych i
40-tych XX wieku przez polskiego grafika i typografa Adama
Półtawskiego. Była szeroko używana przez polskie drukarnie dopóki
używano metalowych czcionek (do lat 60-tych). Prawdopodobnie pierwsza
kompletna rodzina fontów zaprogramowana i zparametryzowana w
METAPOSCIE.

%package latex-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Summary(pl.UTF-8):	Antykwa Turuńska - rodzina tradycyjnych czcionek polskich jako Type 1
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-antt = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-antt < 1:3.1
BuildArch:	noarch

%description latex-antt
Antykwa Torunska is a serif font designed by the late Polish
typographer Zygfryd Gardzielewski, reconstructed and digitized as Type
1.

%description latex-antt -l pl.UTF-8
Antykwa Toruńska to krój szeryfowy opracowany niedawno przez polskiego
typografa Zygfryda Gardzielewskiego, zrekonstruowany i przerobiony na
postać cyfrową jako Type 1.

%package latex-appendix
Summary:	Extra control of appendices
Summary(hu.UTF-8):	Az appendixek nagyobb irányítása
Summary(pl.UTF-8):	Dodatkowe sterowanie załącznikami
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-appendix
Extra control of appendices.

%description latex-appendix -l hu.UTF-8
Az appendixek nagyobb irányítása.

%description latex-appendix -l pl.UTF-8
Dodatkowe sterowanie załącznikami.

%package latex-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Summary(pl.UTF-8):	Tablicowy wariant fontów Computer Modern z obsługą LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-bbm = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-bbm < 1:3.1
BuildArch:	noarch

%description latex-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%description latex-bbm -l pl.UTF-8
Tablicowy wariant fontów Computer Modern z obsługą LaTeXa.

%package latex-bardiag
Summary:	LateX package for drawing bar diagrams
Summary(hu.UTF-8):	LaTeX csomag oszlopdiagramok rajzolására
Summary(pl.UTF-8):	Pakiet LaTeXa do wykresów słupkowych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
BuildArch:	noarch

%description latex-bardiag
LateX package for drawing bar diagrams.

%description latex-bardiag -l hu.UTF-8
LaTeX csomag oszlopdiagramok rajzolására.

%description latex-bardiag -l pl.UTF-8
Pakiet LaTeXa do wykresów słupkowych.

%package latex-bbold
Summary:	Sans serif blackboard bold for LaTeX
Summary(pl.UTF-8):	Tablicowy tłusty font sans serif dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-bbold = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-bbold < 1:3.1
BuildArch:	noarch

%description latex-bbold
A geometric sans serif blackboard bold font, for use in mathematics.

%description latex-bbold -l pl.UTF-8
Geometryczny tablicowy tłusty font sans serif, do używania w
matematyce.

%package latex-bibtex
Summary:	Bibliography management for LaTeX
Summary(pl.UTF-8):	Zarządzenie bibliografią dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-bibtex
Obsoletes:	tetex-bibtex < 1:3.1
Obsoletes:	tetex-latex-bibtex < 1:3.1
Obsoletes:	tetex-natbib < 1:3.1
Obsoletes:	tetex-latex-natbib < 1:3.1
Obsoletes:	tetex-rubibtex < 1:3.1

%description latex-bibtex
Bibliography management for LaTeX.

%description latex-bibtex -l pl.UTF-8
Zarządzanie bibliografią dla LaTeXa.

%package latex-beamer
Summary:	A LaTeX class for producing presentations and slides
Summary(hu.UTF-8):	LaTeX dokumentumosztály prezentációk és fóliák készítéséhez
Summary(pl.UTF-8):	Klasa LaTeXa do tworzenia prezentacji i slajdów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-beamer < 3.08
BuildArch:	noarch

%description latex-beamer
A LaTeX class for producing presentations and slides.

%description latex-beamer -l hu.UTF-8
LaTeX dokumentumosztály prezentációk és fóliák készítéséhez.

%description latex-beamer -l pl.UTF-8
Klasa LaTeXa do tworzenia prezentacji i slajdów.

%package latex-bezos
Summary:	Packages by Javier Bezos (additional math tools)
Summary(hu.UTF-8):	Javier Bezos csomagjai (további matematikai eszközök)
Summary(pl.UTF-8):	Pakiety Javiera Bezosa (dodatkowe narzędzia matematyczne)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-bezos
Packages by Javier Bezos (additional math tools).

%description latex-bezos -l hu.UTF-8
Javier Bezos csomagjai (további matematikai eszközök).

%description latex-bezos -l pl.UTF-8
Pakiety Javiera Bezosa (dodatkowe narzędzia matematyczne).

%package latex-bibtex-ams
Summary:	BibTeX style files for American Mathematical Society publications
Summary(pl.UTF-8):	Pliki stylów BibTeXa do publikacji American Mathematical Society
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-ams = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-ams < 1:3.1
Obsoletes:	tetex-latex-bibtex-ams < 1:3.1
BuildArch:	noarch

%description latex-bibtex-ams
BibTeX style files for American Mathematical Society publications.

%description latex-bibtex-ams -l pl.UTF-8
Pliki stylów BibTeXa do publikacji American Mathematical Society.

%package latex-bibtex-dk
Summary:	Danish variants of the standard BibTeX styles
Summary(pl.UTF-8):	Duńskie warianty standardowych stylów BibTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-bibtex-dk < 1:3.1
BuildArch:	noarch

%description latex-bibtex-dk
Dk-bib is a translation of the four standard BibTeX style files
(abbrv, alpha, plain and unsrt) into Danish. The files have been
extended with ISBN, ISSN and URL fields which can be enabled through a
LaTeX style file.

%description latex-bibtex-dk -l pl.UTF-8
Dk-bib to tłumaczenie czterech standardowych plików stylów BibTeXa
(abbrv, alpha, plain i unsrt) na język duński. Pliki zostały
rozszerzone o pola ISBN, ISSN i URL, które można włączyć poprzez plik
stylu LaTeXa.

%package latex-bibtex-pl
Summary:	Polish bibliography management for LaTeX
Summary(pl.UTF-8):	Polska wersja zarządzania bibliografią dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-plbib < 1:3.1
Obsoletes:	tetex-latex-bibtex-pl < 1:3.1
BuildArch:	noarch

%description latex-bibtex-pl
Polish bibliography management for LaTeX.

%description latex-bibtex-pl -l pl.UTF-8
Polska wersja zarządzania bibliografią dla LaTeXa.

%package latex-bibtex-german
Summary:	German variants of standard BibTeX styles
Summary(pl.UTF-8):	Niemieckie wersje standardowych stylów BibTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-germbib < 1:3.1
Obsoletes:	tetex-latex-bibtex-german < 1:3.1
BuildArch:	noarch

%description latex-bibtex-german
German variants of standard BibTeX styles.

%description latex-bibtex-german -l pl.UTF-8
Niemieckie wersje standardowych stylów BibTeXa.

%package latex-bibtex-revtex4
Summary:	BibTeX styles for REVTeX4
Summary(pl.UTF-8):	Style BibTeXa dla REVTeX4
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-revtex4 < 1:3.1
Obsoletes:	tetex-latex-bibtex-revtex4 < 1:3.1
BuildArch:	noarch

%description latex-bibtex-revtex4
BibTeX styles for REVTeX4.

%description latex-bibtex-revtex4 -l pl.UTF-8
Style BibTeXa dla REVTeX4.

%package latex-bibtex-jurabib
Summary:	Extended BibTeX citation support for the humanities and legal texts
Summary(pl.UTF-8):	Rozszerzona obsługa cytowania BibTeXa do tekstów humanistycznych i prawniczych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-jurabib < 1:3.1
Obsoletes:	tetex-latex-bibtex-jurabib < 1:3.1
BuildArch:	noarch

%description latex-bibtex-jurabib
Extended BibTeX citation support for the humanities and legal texts.

%description latex-bibtex-jurabib -l pl.UTF-8
Rozszerzona obsługa cytowania BibTeXa do tekstów humanistycznych i
prawniczych.

%package latex-bibtex-styles
Summary:	Various BibTeX styles
Summary(hu.UTF-8):	Vegyes BibTeX stílusok
Summary(pl.UTF-8):	Różne style BibTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-bibtex-styles
Various BibTeX styles.

%description latex-bibtex-styles -l hu.UTF-8
Vegyes BibTeX stílusok.

%description latex-bibtex-styles -l pl.UTF-8
Różne style BibTeXa.

%package latex-bibtex-vancouver
Summary:	Bibliographic style file for Biomedical Journals
Summary(hu.UTF-8):	Irodalomjegyzék-stílus a Biomedical Journal-hoz
Summary(pl.UTF-8):	Plik stylu bibliografii dla Biomedical Journals
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-bibtex-vancouver
Bibliographic style file for Biomedical Journals.

%description latex-bibtex-vancouver -l hu.UTF-8
Irodalomjegyzék-stílus a Biomedical Journal-hoz.

%description latex-bibtex-vancouver -l pl.UTF-8
Plik stylu bibliografii dla Biomedical Journals.

%package latex-booktabs
Summary:	Publication quality tables in LaTeX
Summary(hu.UTF-8):	Nyomdai minőségű táblázatok LaTeX-ben
Summary(pl.UTF-8):	Tabele o jakości publikacji w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-booktabs
Publication quality tables in LaTeX.

%description latex-booktabs -l hu.UTF-8
Nyomdai minőségű táblázatok LaTeX-ben.

%description latex-booktabs -l pl.UTF-8
Tabele o jakości publikacji w LaTeXu.

%package latex-caption
Summary:	Customising captions in floating environments
Summary(hu.UTF-8):	Feliratok testreszabása úszó környezetekben
Summary(pl.UTF-8):	Dostosowywanie podpisów w środowiskach pływających
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-caption
Customising captions in floating environments.

%description latex-caption -l hu.UTF-8
Feliratok testreszabása úszó környezetekben.

%description latex-caption -l pl.UTF-8
Dostosowywanie podpisów w środowiskach pływających.

%package latex-carlisle
Summary:	Miscellaneous small packages by David Carlisle
Summary(pl.UTF-8):	Różne małe pakiety autorstwa Davida Carlisle
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-carlisle
Obsoletes:	tetex-latex-carlisle < 1:3.1
BuildArch:	noarch

%description latex-carlisle
Miscellaneous small packages by David Carlisle.

%description latex-carlisle -l pl.UTF-8
Różne małe pakiety autorstwa Davida Carlisle.

%package latex-ccfonts
Summary:	Support for Concrete text and math fonts in LaTeX
Summary(pl.UTF-8):	Obsługa fontów tekstowych i matematycznych Concrete w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-ccfonts < 1:3.1
BuildArch:	noarch

%description latex-ccfonts
LaTeX font definition files for the Concrete fonts and a LaTeX package
for typesetting documents using Concrete as the default font family.
The files support OT1, T1, TS1, and Concrete math including AMS fonts
(Ulrik Vieth's concmath).

%description latex-ccfonts -l pl.UTF-8
Pliki definicji fontów LaTeXowych dla fontów Concrete oraz pakiet
LaTeXa do składania dokumentów przy użyciu Concrete jako domyślnej
rodziny fontów. Pliki obsługują fonty OT1, T1, TS1 oraz matematyczny
Concrete wraz z AMS (concmath Ulrika Vietha).

%package latex-cite
Summary:	Supports compressed, sorted lists of numerical citations
Summary(pl.UTF-8):	Obsługa kompresowanych, sortowanych list numerowanych cytatów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-cite < 1:3.1
BuildArch:	noarch

%description latex-cite
Supports compressed, sorted lists of numerical citations.

%description latex-cite -l pl.UTF-8
Obsługa kompresowanych, sortowanych list numerowanych cytatów.

%package latex-cmbright
Summary:	Support for CM Bright fonts in LaTeX
Summary(pl.UTF-8):	Obsługa fontów CM Bright w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-cmbright = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-cmbright < 1:3.1
BuildArch:	noarch

%description latex-cmbright
A family of sans serif fonts for TeX and LaTeX, based on Donald
Knuth's CM fonts. It comprises OT1, T1 and TS1 encoded text fonts of
various shapes as well as all the fonts necessary for mathematical
typesetting, incl. AMS symbols. This collection provides all the
necessary files for using the fonts with LaTeX.

%description latex-cmbright -l pl.UTF-8
Rodzina fontów sans serif dla TeXa i LaTeXa, oparta na fontach CM
Donalda Knutha. Obejmuje fonty dla kodowań OT1, T1 i TS1 różnych
kształtów oraz fonty niezbędne do składu matematycznego, włącznie z
symbolami AMS. Ten zestaw dostarcza wszystkie niezbędne pliki do
używania fontów w LaTeXu.

%package latex-comment
Summary:	Selectively include/excludes portions of text
Summary(hu.UTF-8):	A szöveg részeinek beillesztése/kihagyása
Summary(pl.UTF-8):	Wybiórcze włączanie/wyłączanie części tekstu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-comment
Selectively include/excludes portions of text.

%description latex-comment -l hu.UTF-8
A szöveg részeinek beillesztése/kihagyása.

%description latex-comment -l pl.UTF-8
Wybiórcze włączanie/wyłączanie części tekstu.

%package latex-concmath
Summary:	LaTeX package and font definition files to access the Concrete math fonts
Summary(pl.UTF-8):	Pakiet LaTeXa i pliki definicji fontów udostępniające fonty matematyczne Concrete
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-concmath = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-concmath < 1:3.1
BuildArch:	noarch

%description latex-concmath
LaTeX package and font definition files to access the Concrete math
fonts, which were derived from Computer Modern math fonts using
parameters from Concrete Roman text fonts.

%description latex-concmath -l pl.UTF-8
Pakiet LaTeXa i pliki definicji fontów udostępniające fonty
matematyczne Concrete wywodzące się z fontów matematycznych Computer
Modern poprzez zastosowanie parametrów fontów tekstowych Concrete
Roman.

%package latex-currvita
Summary:	Typeset a curriculum vitae
Summary(hu.UTF-8):	Önéletrajzok írása
Summary(pl.UTF-8):	Skład życiorysu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-currvita
Typeset a curriculum vitae.

%description latex-currvita -l hu.UTF-8
Önéletrajzok írása.

%description latex-currvita -l pl.UTF-8
Skład życiorysu.

%package latex-curves
Summary:	Curves for LaTeX picture environment
Summary(hu.UTF-8):	Görbék LaTeX picture környezetébe
Summary(pl.UTF-8):	Krzywe do środowiska LaTeXa picture
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-curves
Curves for LaTeX picture environment.

%description latex-curves -l hu.UTF-8
Görbék LaTeX picture környezetébe.

%description latex-curves -l pl.UTF-8
Krzywe do środowiska LaTeXa picture.

%package latex-custom-bib
Summary:	Customized BibTeX styles for LaTeX
Summary(pl.UTF-8):	Dostosowywanie stylów BibTeXa dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-custom-bib < 1:3.1
BuildArch:	noarch

%description latex-custom-bib
Package generating customized BibTeX bibliography styles from a
generic file using docstrip. Includes support for the Harvard style.

%description latex-custom-bib -l pl.UTF-8
Pakiet generujący dostosowane style bibliografii BibTeXa z ogólnego
pliki przy użyciu docstrip. Zawiera obsługę stylu Harvard.

%package latex-cyrillic
Summary:	LaTeX Cyrillic support
Summary(pl.UTF-8):	Obsługa cyrylicy dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-cyrillic
Obsoletes:	tetex-latex-cyrillic < 1:3.1
BuildArch:	noarch

%description latex-cyrillic
LaTeX Cyrillic support.

%description latex-cyrillic -l pl.UTF-8
Obsługa cyrylicy dla LaTeXa.

%package latex-enumitem
Summary:	A package to customize the three basic lists
Summary(hu.UTF-8):	Egy csomag, amivel testreszabhatod a három alapvető listát
Summary(pl.UTF-8):	Pakiet do dostosowywania trzech podstawowych list
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-enumitem
A package to customize the three basic lists (enumerate, itemize and
description).

%description latex-enumitem -l hu.UTF-8
Egy csomag, amivel testreszabhatod a három alapvető listakörnyezetet
(enumerate, itemize, description).

%description latex-enumitem -l pl.UTF-8
Pakiet do dostosowywania trzech podstawowych list (enumerate, itemize
oraz description).

%package latex-exams
Summary:	Various document classes to typeset exams
Summary(hu.UTF-8):	Különböző dokumentumosztályok vizsgák, feladatsorok szedésére
Summary(pl.UTF-8):	Różne klasy dokumentów do składu egzaminów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-exams
Various document classes to typeset exams.

%description latex-exams -l hu.UTF-8
Különböző dokumentumosztályok vizsgák, feladatsorok szedésére.

%description latex-exams -l pl.UTF-8
Różne klasy dokumentów do składu egzaminów.

%package latex-float
Summary:	Tools to manipulate float objects
Summary(hu.UTF-8):	Eszközök úszó objektuomok kezeléséhez
Summary(pl.UTF-8):	Narzędzia do operowania obiektami pływającymi
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-float
Tools to manipulate float objects.

%description latex-float -l hu.UTF-8
Eszközök úszó objektuomok kezeléséhez.

%description latex-float -l pl.UTF-8
Narzędzia do operowania obiektami pływającymi.

%package latex-foiltex
Summary:	FoilTeX - a collection of LaTeX files for making foils
Summary(hu.UTF-8):	A FoilTeX a LaTeX fájlok gyűjteménye fóliák készítéséhez
Summary(pl.UTF-8):	FoilTeX - zbiór plików LaTeXa do tworzenia folii
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-foiltex
The FoilTeX is a collection of LaTeX files for making foils.

%description latex-foiltex -l hu.UTF-8
A FoilTeX a LaTeX fájlok gyűjteménye fóliák készítéséhez.

%description latex-foiltex -l pl.UTF-8
FoilTeX to zbiór plików LaTeXa do tworzenia folii.

%package latex-formlett
Summary:	Letters to multiple recipients
Summary(hu.UTF-8):	Levél több címzettnek ("körlevél")
Summary(pl.UTF-8):	Listy do wielu adresatów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-formlett
Letters to multiple recipients.

%description latex-formlett -l hu.UTF-8
Levél több címzettnek ("körlevél").

%description latex-formlett -l pl.UTF-8
Listy do wielu adresatów.

%package latex-formular
Summary:	Create forms containing field for manual entry
Summary(hu.UTF-8):	Kézzel kitöltendő űrlapok készítése
Summary(pl.UTF-8):	Tworzenie formularzy z polami do ręcznego wypełnienia
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-formular
Create forms containing field for manual entry.

%description latex-formular -l hu.UTF-8
Kézzel kitöltendő űrlapok készítése.

%description latex-formular -l pl.UTF-8
Tworzenie formularzy z polami do ręcznego wypełnienia.

%package latex-gbrief
Summary:	Letter document class
Summary(hu.UTF-8):	Levél dokumentumosztály
Summary(pl.UTF-8):	Klasa dokumentu listowego
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-gbrief
Letter document class.

%description latex-gbrief -l hu.UTF-8
Levél dokumentumosztály.

%description latex-gbrief -l pl.UTF-8
Klasa dokumentu listowego.

%package latex-keystroke
Summary:	Graphical representation of keys on keyboard
Summary(hu.UTF-8):	A billentyűk grafikus megjelenítése
Summary(pl.UTF-8):	Graficzna reprezentacja klawiszy na klawiaturze
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-keystroke
Graphical representation of keys on keyboard.

%description latex-keystroke -l hu.UTF-8
A billentyűk grafikus megjelenítése.

%description latex-keystroke -l pl.UTF-8
Graficzna reprezentacja klawiszy na klawiaturze.

%package latex-labbook
Summary:	Typeset laboratory journals
Summary(hu.UTF-8):	Laborjegyzőkönyvek szedése
Summary(pl.UTF-8):	Składanie dzienników laboratoryjnych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-labbook
Typeset laboratory journals.

%description latex-labbook -l hu.UTF-8
Laborjegyzőkönyvek szedése.

%description latex-labbook -l pl.UTF-8
Składanie dzienników laboratoryjnych.

%package latex-lcd
Summary:	Alphanumerical LCD-style displays
Summary(hu.UTF-8):	Alfanumerikus LCD-szerű kijelzés
Summary(pl.UTF-8):	Alfanumeryczne wyświetlacze w stylu LCD
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-lcd
Alphanumerical LCD-style displays.

%description latex-lcd -l hu.UTF-8
Alfanumerikus LCD-szerű kijelzés.

%description latex-lcd -l pl.UTF-8
Alfanumeryczne wyświetlacze w stylu LCD.

%package latex-leaflet
Summary:	Create small handouts (flyers)
Summary(hu.UTF-8):	Kis "kézikönyvek" készítése (brossúrák)
Summary(pl.UTF-8):	Tworzenie małych ulotek
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-leaflet
Create small handouts (flyers).

%description latex-leaflet -l hu.UTF-8
Kis "kézikönyvek" készítése (brossúrák).

%description latex-leaflet -l pl.UTF-8
Tworzenie małych ulotek.

%package latex-leftidx
Summary:	Left and right subscripts and superscripts in math mode
Summary(hu.UTF-8):	Bal és jobboldali alsó és felső indexek matematikai módban
Summary(pl.UTF-8):	Lewe i prawe indeksy dolne i górne w trybie matematycznym
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-leftidx
Left and right subscripts and superscripts in math mode.

%description latex-leftidx -l hu.UTF-8
Bal és jobboldali alsó és felső indexek matematikai módban.

%description latex-leftidx -l pl.UTF-8
Lewe i prawe indeksy dolne i górne w trybie matematycznym.

%package latex-lewis
Summary:	Draw Lewis structures (chemistry)
Summary(hu.UTF-8):	Lewis struktúrák készítése (kémia)
Summary(pl.UTF-8):	Rysowanie struktur Lewisa (chemicznych)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-lewis
Draw Lewis structures (chemistry).

%description latex-lewis -l hu.UTF-8
Lewis struktúrák készítése (kémia).

%description latex-lewis -l pl.UTF-8
Rysowanie struktur Lewisa (chemicznych).

%package latex-lm
Summary:	LaTeX styles for Latin Modern family fonts
Summary(pl.UTF-8):	Style LaTeXa dla fontów z rodziny Latin Modern
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-lm = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-lm < 1:3.1
BuildArch:	noarch

%description latex-lm
Latin Modern family of fonts, based on the Computer Modern fonts
released into public domain by AMS (copyright (C) 1997 AMS). Contain a
lot of additional characters, mainly accented ones, but not only.
There is a one set of PostScript fonts and four sets of TeX Font
Metric files, corresponding to: Cork encoding (cork-*.tfm); QX
encoding (qx-*.tfm); TeX'n'ANSI aka LY1 encoding (texnansi-*.tfm); and
Text Companion for EC fonts aka TS1 (ts1-*.tfm). It is presumed that a
potential user knows what to do with all these files. The author is
Boguslaw Jackowski.

%description latex-lm -l pl.UTF-8
Rodzina fontów Latin Modern, oparta na fontach Computer Modern
przekazanych do domeny publicznej przez AMS (copyright (C) 1997 AMS).
Zawiera wiele dodatkowych znaków, głównie z akcentami, ale nie tylko.
Jest jeden zbiór fontów postscriptowych oraz cztery zbiory plików TeX
Font Metric, odpowiadających: kodowaniu Cork (cork-*.tfm); kodowaniu
QX (qx-*.tfm); kodowaniu TeX'n'ANSI zwanemu także LY1
(texnansi-*.tfm); oraz Text Companion dla fontów EC zwanemu także TS1
(ts1-*.tfm). Zakłada się, że potencjalny użytkownik wie, co zrobić z
tymi wszystkimi plikami. Autorem jest Bogusław Jackowski.

%package latex-lastpage
Summary:	Reference last page for "Page N of M" type footers
Summary(hu.UTF-8):	Az utolsó oldalra hivatkozás "N/M. oldal" típusú lábfejekhez
Summary(pl.UTF-8):	Odnośnik do ostatniej strony na potrzeby stopek typu "Strona N z M"
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
BuildArch:	noarch

%description latex-lastpage
Reference last page for Page N of M type footers.

%description latex-lastpage -l hu.UTF-8
Az utolsó oldalra hivatkozás "N/M. oldal" típusú lábfejekhez.

%description latex-lastpage -l pl.UTF-8
Odnośnik do ostatniej strony na potrzeby stopek typu "Strona N z M".

%package latex-lineno
Summary:	Line numbers on paragraphs
Summary(pl.UTF-8):	Numery linii dla paragrafów
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-lineno < 1:3.1
BuildArch:	noarch

%description latex-lineno
The LaTeX package lineno.sty provides line numbers on paragraphs.
After TeX has broken a paragraph into lines there will be line numbers
attached to them, with the possibility to make references through the
LaTeX \ref, \pageref cross reference mechanism.

%description latex-lineno -l pl.UTF-8
Pakiet LaTeXa lineno.sty daje numery linii dla paragrafów. Po podziale
paragrafu na linie przez TeXa do linii dołączane są ich numery z
możliwością tworzenia odnośników poprzez mechanizm odnośników LaTeXa
\ref i \pageref.

%package latex-metre
Summary:	Support for the work of classicists
Summary(pl.UTF-8):	Wsparcie pracy dla filologów klasycznych
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-metre
Support for the work of classicists.

%description latex-metre -l pl.UTF-8
Wsparcie pracy dla filologów klasycznych.

%package latex-games
Summary:	Packages for typesetting games
Summary(hu.UTF-8):	Játékok szedése
Summary(pl.UTF-8):	Pakiety do składu gier
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-games
Chess, chinese chess, crosswords, go, backgammon and more.

%description latex-games -l hu.UTF-8
Sakk, kínai sakk, keresztrejtvények, go, backgammon és még sok más.

%description latex-games -l pl.UTF-8
Szachy, szachy chińskie, krzyżówki, go, tryktrak i inne.

%package latex-extend
Summary:	Extensions, patches, improvements of main LaTeX styles, environments
Summary(hu.UTF-8):	Az alap LaTeX stílusok, környezetek, stb. bővítései, foltjai
Summary(pl.UTF-8):	Rozszerzenia, łaty i usprawnienia głównych stylów i środowisk LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-ltablex
Obsoletes:	tetex-latex-ltablex < 1:3.1
BuildArch:	noarch

%description latex-extend
This package contains:
- addlines: a user-friendly wrapper around \enlargethispage.
- alnumsec: alphanumeric section numbering.
- arydshln: horizontal and vertical dashed lines in arrays and
  tabulars
- babelbib: multilingual bibliographies.
- bibtopicprefix: prefix references to bibliographies produced by
  bibtopic.
- boites: boxes that may break across pages
- booklet: aids for printing simple booklets.
- bullcntr: display list item counter as regular pattern of bullets.
- chappg: page numbering by chapter.
- cjw: a bundle of packages and classes.
- clefval: key/value support with a hash.
- colortbl: add colour to LaTeX tables.
- combine: bundle individual documents into a single document.
- contour: print a coloured contour around text.
- ctable: easily typeset centered tables.
- curve2e: extensions for package pict2e.
- dashbox: draw dashed boxes.
- dashline: draw dashed rules.
- etaremune: reverse-counting enumerate environment.
- expdlist: expanded description environments.
- HA-prosper: patches and improvements for prosper.
- leading: define leading with a length.
- listliketab: typeset lists as tables.
- ltablex: table package extensions.
- makebox: defines a \makebox* command.
- makecell: tabular column heads and multilined cells.
- marginnote: notes in the margin, even where \marginpar fails
- mcaption: put captions in the margin.
- mcite: multiple items in a single citation.
- mciteplus: enhanced multiple citations.
- minipage-marginpar: minipages with marginal notes.
- miniplot: a package for easy figure arrangement.
- multicap: format captions inside multicols
- newvbtm: define your own verbatim-like environment.
- notes2bib: integrating notes into the bibliography.
- ntabbing: simple tabbing extension for automatic line numbering.
- numline: LaTeX macros for numbering lines.
- pbox: a variable-width \parbox command.
- pinlabel: a TeX labelling package.
- polytable: tabular-like environments with named columns.
- rccol: decimal-centered optionally rounded numbers in tabular.
- romannum: generate roman numerals instead of arabic digits.
- schedule: weekly schedules.
- subfloat: sub-numbering for figures and tables.
- umoline: underline text allowing line breaking.
- umrand: package for fancy box frames.
- underlin: underlined running heads.
- ushort: shorter (and longer) underlines and underbars.

%description latex-extend -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- addlines: felhasználóbarát wrapper \enlargethispage-hez
- alnumsec: alfanumerikus section számozás
- arydshln: vízszintes és függőleges pontozott vonalak array és
  tabular környezetkben
- babelbib: többnyelvű bibliográfiák
- bibtopicprefix: prefix hivatkozás bibtopic által készített
  bibliográfiára
- boites: dobozok, amelyek törhetők oldalak között
- booklet: booklet formátumban történő nyomtatás
- bullcntr: lista elemek számlálójának megjelenítése mint...
- chappg: oldalszámozás chapter alapján
- cjw: csomagok és osztályok tömkelege
- clefval: kulcs/érték párok hash-sel
- colortbl: színek LaTeX táblázatokban
- combine: külön dokumentumok eggyé fűzése
- contour: színes kontúr nyomtatása szöveg körül
- ctable: középre igazított táblázatok szedése
- curve2e: pict2e csomaghoz kiegészítések
- dashbox: pontozott dobozok
- dashline: pontozott vonalak
- etaremune: visszafele sorszámazó enumerate környezet
- expdlist: kibővített description környezetek
- HA-prosper: foltok és bővítések a prosper-hez
- leading: sorközök definiálása hosszal
- listliketab: listák táblázatként szedése
- ltablex: table csomag kiegészítése
- makebox: egy \makebox* parancs definiálása
- makecell: táblázat címsorral és többsoros cellákkal
- marginnote: széljegyzetek, ott is, ahol a \marginpar hibázik
- mcaption: címkék a margóra
- mcite: több elem egy hivatkozásban
- mciteplus: kibővített többszörös hivatkozás
- minipage-marginpar: minipage-ek széljegyzetekkel
- miniplot: egy csomag ábrák könnyű elhelyezéséhez
- multicap: formázott cimkék multicols környezetben
- newvbtm: saját verbatim-szerű környezetek
- notes2bib: megjegyzések elhelyezése bibliográfiába
- ntabbing: tabbing környezet automatikus sorszámozással
- numline: LaTeX makrók sorok számozására
- pbox: változtatható szélességű \parbox
- pinlabel: a TeX labelling package.
- polytable: tabular-like environments with named columns.
- rccol: decimal-centered optionally rounded numbers in tabular.
- romannum: generate roman numerals instead of arabic digits.
- schedule: heti időbeosztás (órarend)
- subfloat: sub-numbering for figures and tables.
- umoline: aláhúzott szövegben sortörés engedélyezése
- umrand: package for fancy box frames.
- underlin: aláhúzott élőfej
- ushort: shorter (and longer) underlines and underbars.

%description latex-extend -l pl.UTF-8
Ten pakiet zawiera:
- addlines: przyjazne dla użytkownika obudowanie \enlargethispage.
- alnumsec: alfanumeryczne numerowanie sekcji.
- arydshln: poziome i pionowe linie kreskowane w tabelach.
- babelbib: bibliografie wielojęzyczne.
- bibtopicprefix: prefiksy dla odnośników do bibliografii z bibtopica.
- boites: pola, które można łamać na wiele stron.
- booklet: pomoce przy drukowaniu prostych broszur.
- bullcntr: licznik elementów jako zwykły wzorzec wypunktowań.
- chappg: numerowanie stron po rozdziale.
- cjw: zestaw pakietów i klas.
- clefval: obsługa klucza/wartości z haszem.
- colortbl: dodanie kolorów do tabel LaTeXowych.
- combine: włączanie osobnych dokumentów w pojedynczy dokument.
- contour: drukowanie kolorowych konturów wokół tekstu.
- ctable: łatwy skład wyśrodkowanych tabel.
- curve2e: rozszerzenia pakietu pict2e.
- dashbox: rysowanie kreskowanych pól.
- dashline: rysowanie kreskowanych linii.
- etaremune: środowisko enumerate liczące wtecz.
- expdlist: środowiska z rozwijanym opisem.
- HA-prosper: łaty i usprawnienia pakietu prosper.
- leading: definiowanie odstępu międzywierszowego o zadanej długości.
- listliketab: skład listy tabel.
- ltablex: rozszerzenia pakietu table.
- makebox: polecenie \makebox*.
- makecell: nagłówki kolumn w tabeli i komórki wielowierszowe.
- marginnote: notatki na marginesie skuteczniejsze niż \marginpar.
- mcaption: podpisy na marginesie.
- mcite: wiele elementów w jednym cytacie.
- mciteplus: rozszerzone wielokrotne cytaty.
- minipage-marginpar: miniaturowe strony z notatkami na marginesie.
- miniplot: pakiet do łatwego układania rysunków.
- multicap: formatowanie podpisów w środowisku multicol.
- newvbtm: definiowanie własnego środowiska w stylu maszynopisu.
- notes2bib: osadzanie notatek w bibliografii.
- ntabbing: proste rozszerzenie tabel o automatyczne numery wierszy.
- numline: makra LaTeXa do numerowania wierszy.
- pbox: polecenie \parbox o różnej szerokości.
- pinlabel: pakiet TeXa do etykietowania.
- polytable: środowiska typu tabular o nazwanych kolumnach.
- rccol: centrowane dziesiętnie, ew. zaokrąglane liczby w tabeli.
- romannum: generowanie liczb rzymskich zamiast arabskich.
- schedule: plany tygodniowe.
- subfloat: numeracja podrzędna rysunków i tabel.
- umoline: podkreślanie tekstu z możliwością łamania wierszy.
- umrand: pakiet do fantazyjnych obramowań.
- underlin: podkreślone tytuły skrócone.
- ushort: krótsze (i dłuższe) podkreślenia.

%package latex-effects
Summary:	Additional effects to fonts, texts
Summary(hu.UTF-8):	További effektek betűkhöz, szövegekhez,...
Summary(pl.UTF-8):	Dodatkowe efekty do fontów, tekstów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-effects
This package contains:
- arcs: draw arcs over and under text
- blowup: upscale or downscale all pages of a document.
- changebar: generate changebars in LaTeX documents.
- draftwatermark: put a grey textual watermark on document pages.
- flippdf: horizontal flipping of pages with pdfLaTeX.
- flowfram: create text frames for posters, brochures or magazines.
- isorot: rotation of document elements.
- lettrine: typeset dropped capitals.
- niceframe: support for fancy frames.
- notes: mark sections of a document.
- objectz: macros for typesetting Object Z.
- parallel: typeset parallel texts.
- quotchap: decorative chapter headings.
- rotpages: typeset sets of pages upside-down and backwards.
- sectionbox: create fancy boxed ((sub)sub)sections.
- shadethm: theorem environments that are shaded

%description latex-effects -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- arcs: ívek rajzolása szöveg fölé és alá
- blowup: a dokumentum összes oldalának nagyítása vagy kicsinyítése
- changebar: oldalsávok készítése LaTeX dokumentumokban
- draftwatermark: szürke szöveges vízjel a dokumentum oldalaira
- flippdf: oldalak vízszintes tükrözése pdfLaTeX-hel
- flowfram: szövegkeretek poszterekhez, brossúrákhoz vagy magazinokhoz
- isorot: dokumentum-elemek forgatása
- lettrine: ejtett kapitálisok szedése
- niceframe: különféle keretek
- notes: dokumentum részeinek kiemelése, megjelölése
- objectz: Object Z objektumok szedése
- parallel: párhuzamos szövegek szedése
- quotchap: decorative chapter headings.
- rotpages: typeset sets of pages upside-down and backwards.
- sectionbox: create fancy boxed ((sub)sub)sections.
- shadethm: theorem environments that are shaded

%description latex-effects -l pl.UTF-8
Ten pakiet zawiera:
- arcs: rysowanie łuków nad i pod tekstem.
- blowup: powiększanie lub zmniejszanie wszystkich stron dokumentu.
- changebar: generowanie pasków na marginesie w dokumentach LaTeXa.
- draftwatermark: umieszczanie szarych znaków wodnych na stronach.
- flippdf: pozioma zmiana stron przy użyciu pdfLaTeXa.
- flowfram: ramki tekstu na plakatach, bruszurach i magazynach.
- isorot: obracanie elementów dokumentu.
- lettrine: skład wysuniętych inicjałów.
- niceframe: obsługa fantazyjnych ramek.
- notes: oznaczanie sekcji dokumentu.
- objectz: makra do składu notacji Object-Z.
- parallel: skład tekstów równoległych.
- quotchap: dekorowane nagłówki rozdziałów.
- rotpages: skład zbiorów stron do góry nogami i wstecz.
- sectionbox: tworzenie fantazyjnych pól ((pod)pod)sekcji.
- shadethm: środowiska theorem z cieniowaniem.

%package latex-math-sources
Summary:	Sources of latex-math
Summary(hu.UTF-8):	A latex-math forrása
Summary(pl.UTF-8):	Źródła latex-math
Group:		Applications/Publishing/TeX
BuildArch:	noarch

%description latex-math-sources
Sources of latex-math.

%description latex-math-sources -l hu.UTF-8
A latex-math forrása.

%description latex-math-sources -l pl.UTF-8
Źródła latex-math.

%package latex-math
Summary:	Mathematical packages
Summary(hu.UTF-8):	Matematikai csomagok
Summary(pl.UTF-8):	Pakiety matematyczne
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-bbm = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-stmaryrd = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-ams = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-carlisle = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-psnfss = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-pst-3dplot = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-wasysym = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-xkeyval = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-xypic = %{epoch}:%{version}-%{release}
# gnuplottex needs gnuplot
Requires:	gnuplot
BuildArch:	noarch

%description latex-math
This package contains:
- bez123: Support for Bezier curves.
- binomexp: Calculate Pascal's triangle
- cmll: symbols for linear logic.
- constants: automatic numbering of constants.
- coordsys: draw cartesian coordinate systems.
- dotseqn: flush left equations with dotted leaders to the numbers.
- egplot: encapsulate Gnuplot sources in LaTeX documents.
- eqlist: description lists with equal indentation.
- eqnarray: more generalised equation arrays with numbering.
- esdiff: simplify typesetting of derivatives.
- esvect: vector arrows.
- extpfeil: extensible arrows in mathematics
- faktor: typeset quotient structures with LaTeX.
- fouridx: left sub- and superscripts in maths mode.
- functan: macros for functional analysis and PDE theory
- galois: typeset Galois connections.
- gnuplottex: embed Gnuplot commands in LaTeX documents.
- hhtensor: print vectors, matrices, and tensors.
- logpap: generate logarithmic graph paper with LaTeX.
- makeplot: easy plots from Matlab in LaTeX.
- maybemath: make math bold or italic according to context.
- mfpic4ode: macros to draw direction fields and solutions of ODEs.
- mhequ: multicolumn equations, tags, labels, sub-numbering.
- mhs: historical mathematics.
- mlist: logical markup for lists.
- nath: natural mathematics notation.
- noitcrul: improved underlines in mathematics.
- numprint: print numbers with separators and exponent if necessary.
- permute: support for symmetric groups.
- petri-nets: A set TeX/LaTeX packages for drawing Petri nets.
- qsymbols: maths symbol abbreviations.
- qtree: draw tree structures.
- sdrt: macros for Segmented Discourse Representation Theory.
- semantic: help for writing programming language semantics.
- simplewick: simple Wick contractions.
- sseq: spectral sequence diagrams.
- subdepth: unify maths subscript height.
- subeqn: package for subequation numbering.
- subeqnarray: equation array with sub numbering.
- tree-dvips: trees and other linguists' macros.
- trfsigns: typeset transform signs.
- trsym: symbols for transformations.
- ulsy: extra mathematical characters.

%description latex-math -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- bez123: Bezier-görbék
- binomexp: Pascal-háromszög számítása
- cmll: szimbólumok lineáris logikához
- constants: változók automatikus sorszámozása
- coordsys: Descartes-féle koordinátarendszerek rajzolása
- dotseqn: TODO
- egplot: Gnuplot források LaTeX dokumentumokba ágyazása
- eqlist: leíró lista egyenlő behúzással
- eqnarray: általánosabb egyenlet-rendszer sorszámozással
- esdiff: deriváltak bevitele
- esvect: vektornyilak
- extpfeil: bővíthető nyilak matematikában
- faktor: hányados struktúrák LaTeX-hel
- fouridx: alsó és felső indexek bal oldalon matematikai módban
- functan: funkcionálanalízés és PDE elmélethez makrók
- galois: Galois kapcsolatok szedése
- gnuplottex: Gnuplot parancsok beágyazása LaTeX dokumentumokba
- hhtensor: vetkorok, mátrixok és tenzorok nyomtatása
- logpap: logaritmikus grafikonok
- makeplot: könnyű ábrázolások Matlab-ból LaTeX-be
- maybemath: matematikai félkövér ill. dőlt szöveg környezettől
  függően
- mfpic4ode: differenciálegyenletek megoldásainak ábrázolása
- mhequ: többoszlopos egyenletek, cimkék, al-sorszámozás
- mhs: történelmi matematika
- mlist: listák logikus jelölése
- nath: természetes matematikai jelölés
- noitcrul: kibővített aláhúzások matematikában
- numprint: számok írása elválasztókkal és kitevőkkel, ha szükséges
- permute: szimmetriacsoportok
- petri-nets: A set TeX/LaTeX packages for drawing Petri nets.
- qsymbols: matematikai szimbólumok rövidítése
- qtree: fastruktúrák rajzolása
- sdrt: macros for Segmented Discourse Representation Theory.
- semantic: help for writing programming language semantics.
- simplewick: simple Wick contractions.
- sseq: spectral sequence diagrams.
- subdepth: matematikai indexek méretének egységesítése
- subeqn: alegyenletek sorszámozása
- subeqnarray: egyenletek al-sorszámozása
- tree-dvips: trees and other linguists' macros
- trfsigns: transzformációs jelek szedése
- trsym: szimbólumok transzformációkhoz
- ulsy: extra matematikai karakterek

%description latex-math -l pl.UTF-8
Ten pakiet zawiera:
- bez123: obsługa krzywych Beziera.
- binomexp: obliczanie trójkąta Pascala.
- cmll: symbole logiki liniowej.
- constants: automatyczne numerowanie stałych.
- coordsys: rysowanie kartezjańskich układów współrzędnych.
- dotseqn: równania z kropkowanymi liniami odniesienia do numerów.
- egplot: osadzanie źródeł Gnuplota w dokumentach w LaTeXu.
- eqlist: listy opisów z równymi wcięciami.
- eqnarray: uogólnione tablice równań z numerowaniem.
- esdiff: uproszczenie składu pochodnych.
- esvect: strzałki wektorów.
- extpfeil: rozszerzalne strzałki w matematyce.
- faktor: skład struktur wykładników w LaTeXu.
- fouridx: lewe indeksy dolne i górne w trybie matematycznym.
- functan: makra do analizy funkcjonalnej i teorii PDE.
- galois: skład połączeń Galois.
- gnuplottex: osadzanie poleceń Gnuplota w dokumentach w LaTeXu.
- hhtensor: drukowanie wektorów, macierzy i tensorów.
- logpap: generowanie siatek logarytmicznych w LaTeXu.
- makeplot: łatwe wykresy z Matlaba w LaTeXu.
- maybemath: wytłuszczanie i kursywa dla wzorów zgodnie z kontekstem.
- mfpic4ode: makra do rysowania pól skierowanych i rozwiązań ODE.
- mhequ: wielokolumnowe równania, znaczniki, etykiety i podindeksy.
- mhs: matematyka historyczna.
- mlist: znaczniki logiczne dla list.
- nath: naturalna notacja matematyczna.
- noitcrul: ulepszone podkreślenia w matematyce.
- numprint: liczby z separatorami i wykładnikami w razie potrzeby.
- permute: obsługa grup symetrycznych.
- petri-nets: zbiór pakietów TeXa/LaTeXa do rysowania sieci Petriego.
- qsymbols: skróty symboli matematycznych.
- qtree: rysowanie struktur drzewiastych.
- sdrt: makra do teorii reprezentacji dyskursu segmentowanego.
- semantic: pomoc przy opisie semantyki języków programowania.
- simplewick: proste zwężenia Wicka.
- sseq: diagramy sekwencji widmowych.
- subdepth: ujednolicenie wysokości indeksów matematycznych.
- subeqn: pakiet do numerowania podrównań.
- subeqnarray: tablica równań z numerowaniem podrzędnym.
- tree-dvips: drzewa i inne makra lingwistyczne.
- trfsigns: skład znaków przekształceń.
- trsym: symbole przekształceń.
- ulsy: dodatkowe znaki matematyczne.

%package latex-misc
Summary:	Misc packages
Summary(hu.UTF-8):	Vegyes csomagok
Summary(pl.UTF-8):	Różne pakiety
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-misc
This packages contains:
- cooking: typeset recipes.
- cuisine: typeset recipes.
- fixme: insert "fixme" notes into draft documents.
- recipecard: typeset recipes in note-card-sized boxes.
- todo: make a to-do list for a document.

%description latex-misc -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- cooking: receptek szedése
- cuisine: receptek szedése
- fixme: "fixme" megjegyzések elhelyezése
- recipecard: receptek szedése jegyzet-méretű dobozokba
- todo: dokumentumok teendőinek listája

%description latex-misc -l pl.UTF-8
Ten pakiet zawiera:
- cooking: skład przepisów.
- cuisine: skład przepisów.
- fixme: wstawianie notatek "fixme" do szkiców dokumentów.
- recipecard: skład przepisów w polach rozmiaru notatek.
- todo: lista "todo" dla dokumentu.

%package latex-music
Summary:	Musical packages
Summary(hu.UTF-8):	Zenei csomagok
Summary(pl.UTF-8):	Pakiety muzyczne
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-music
This package contains:
- abc: support ABC music notation in LaTeX.
- guitar: guitar chords and song texts.
- songbook: package for typesetting song lyrics and chord books.

%description latex-music -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- abc: ABC hangjegyzések LaTeX-ben
- guitar: gitárkották és dalszövegek
- songbook: dalszövegek és akkordkönyvek szedése

%description latex-music -l pl.UTF-8
Ten pakiet zawiera:
- abc: skład notacji muzycznej ABC w LaTeXu.
- guitar: akordy gitarowe i teksty utworów.
- songbook: pakiet do składu książek z tekstami utworów i akordami.

%package latex-physics
Summary:	Physical packages
Summary(hu.UTF-8):	Fizikai csomagok
Summary(pl.UTF-8):	Pakiety fizyczne
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Suggests:	%{name}-latex-SIstyle
Suggests:	%{name}-latex-SIunits
Suggests:	%{name}-latex-siunitx
BuildArch:	noarch

%description latex-physics
This package contains:
- circ: macros for typesetting circuit diagrams.
- colorwav: colours by wavelength of visible light.
- dyntree: construct Dynkin tree diagrams.
- feynmf: macros and fonts for creating Feynman (and other) diagrams.
- formula: typesetting physical units.
- isotope: a package for type setting isotopes
- listofsymbols: create and manipulate lists of symbols
- miller: typeset Miller indices.
- susy: macros for SuperSymmetry-related work.

%description latex-physics -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- circ: áramkörök szedése
- colorwav: a látható fény színei hullámhossz szerint
- dyntree: Dynkin fadiagramok készítése
- feynmf: makrók és fontok Feynman (és más) diagramok készítésére
- formula: fizikai egységek szedése
- isotope: izotópok szedése
- listofsymbols: szimbólumok listájának létrehozása és kezelése
- miller: miller indexek szedése
- susy: Szuper-Szimmetria elmélettel kapcsolatos munkákhoz makrók

%description latex-physics -l pl.UTF-8
Ten pakiet zawiera:
- circ: makra do składu schematów elektrycznych.
- colorwav: kolory wg długości fali światła widzialnego.
- dyntree: konstruowanie diagramów drzewiastych Dynkina.
- feynmf: makra i fonty do tworzenia diagramów Feynmana (i innych).
- formula: skład jednostek fizycznych.
- isotope: pakiet do składu izotopów.
- listofsymbols: tworzenie i operowanie listami symboli.
- miller: skład wskaźników Millera.
- susy: makra do prac związanych z supersymetrią.

%package latex-biology
Summary:	Biological packages
Summary(hu.UTF-8):	Biológiai csomagok
Summary(pl.UTF-8):	Pakiety biologiczne
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-xetex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-biology
This package contains:
- biocon: typesetting biological species names
- dnaseq: format DNA base sequences.

%description latex-biology -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- biocon: biológiai fajnevek szedése
- dnaseq: DNS szekvenciák szedése

%description latex-biology -l pl.UTF-8
Ten pakiet zawiera:
- biocon: skład nazw gatunków.
- dnaseq: formatowanie sekwencji podstawowych DNA.

%package latex-presentation
Summary:	Presentations in LaTeX
Summary(hu.UTF-8):	Prezentációk LaTeX-ben
Summary(pl.UTF-8):	Prezentacje w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-foiltex = %{epoch}:%{version}-%{release}
Suggests:	%{name}-latex-prosper = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-presentation
This package contains:
- powerdot: a presentation class.
- ppower4: a postprocessor for PDF presentations.
- sciposter: make posters of ISO A3 size and larger.
- tpslifonts: a LaTeX package for configuring presentation fonts.

%description latex-presentation -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- powerdot: egy prezentáció osztály
- ppower4: egy postprocesszor PDF prezentációkhoz
- sciposter: poszterek készítése A3-as és nagyobb méretben
- tpslifonts: a LaTeX package for configuring presentation fonts.

%description latex-presentation -l pl.UTF-8
Ten pakiet zwiera:
- powerdot: klasa do prezentacji.
- ppower4: postprocesor do prezentacji PDF.
- sciposter: tworzenie plakatów w rozmiarze ISO A3 i większych.
- tpslifonts: pakiet LaTeXa do konfigurowania fontów prezentacyjnych.

%package latex-chem
Summary:	Chemical packages
Summary(hu.UTF-8):	Kémiai csomagok
Summary(pl.UTF-8):	Pakiety chemiczne
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Suggests:	%{name}-latex-lewis
BuildArch:	noarch

%description latex-chem
This package contains:
- achemso: support for American Chemical Society journal submissions.
- bpchem: typeset chemical names, formulae, etc.
- chemarrow: arrows for use in chemistry.
- chemcompounds: simple consecutive numbering of chemical compounds.
- chemcono: support for compound numbers in chemistry documents.
- chemstyle: writing chemistry with style.
- mhchem: typeset chemical formulae/equations and Risk and Safety
  phrases

%description latex-chem -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- achemso: American Chemical Society formátuma
- bpchem: kémiai nevek, formulák, stb. szedése
- chemarrow: kémiában használatos nyilak
- chemcompounds: kémiai vegyületek számozása
- chemcono: kémiai vegyületek kémiai dokumentumokbam
- chemstyle: kémiai dokumentum írása
- mhchem: kémiai formulák/egyenletek szedése

%description latex-chem -l pl.UTF-8
Ten pakiet zawiera:
- achemso: obsługa artykułów do wydawnictw American Chemical Society.
- bpchem: skład nazw i wzorów chemicznych.
- chemarrow: strzałki do zastosowań chemicznych.
- chemcompounds: proste numerowanie związków chemicznych.
- chemcono: obsługa numerów związków w dokumentach chemicznych.
- chemstyle: artykuły chemiczne ze stylem.
- mhchem: skład chemicznych wzorów/równań oraz symboli zagrożeń.

%package latex-informatic
Summary:	Informatical packages
Summary(hu.UTF-8):	Informatikai csomagok
Summary(pl.UTF-8):	Pakiety informatyczne
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-informatic
This package contains:
- alg: LaTeX environments for typesetting algorithms.
- bytefield: Create illustrations for network protocol specifications.
- lsc: typesetting Live Sequence Charts.
- method: typeset method and variable declarations.
- msc: draw MSC diagrams.
- nag: detecting and warning about obsolete LaTeX commands
- progkeys: typeset programs, recognising keywords.
- register: typeset programmable elements in digital hardware
  (registers).
- uml: UML diagrams in LaTeX.

%description latex-informatic -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- alg: LaTeX környezetek algoritmusok szedésére
- bytefield: hálózati protokoll specifikációk szemléltetése
- lsc: Live Sequence Charts
- method: eljárások és változók deklarációjának szedése
- msc: MSC diagramok
- nag: elavult LaTeX parancsok detektálása és figyelmeztetés
- progkeys: programok szedése, kulcsszavakkal
- register: programozható elemek (regiszterek) szedése
- uml: UML diagramok LaTeX-ben

%description latex-informatic -l pl.UTF-8
Ten pakiet zawiera:
- alg: środowiska LaTeXa do składu algorytmów.
- bytefield: tworzenie ilustracji specyfikacji protokołów sieciowych.
- lsc: skład wykresów Live Sequence Chart.
- method: skład deklaracji metod i zmiennych.
- msc: rysowanie diagramów MSC.
- nag: wykrywanie i ostrzeżenia o przestarzałych poleceniach LaTeXa.
- progkeys: skład programów z rozpoznawaniem słów kluczowych.
- register: skład elementów programowania w sprzęcie cyfrowym.
- uml: diagramy UML w LaTeXu.

%package latex-pdftools
Summary:	Various tools to PDF output
Summary(hu.UTF-8):	Különböző eszközök pdf output-hoz
Summary(pl.UTF-8):	Różne narzędzia do wyjścia PDF
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pdftools
This package contains:
- attachfile: attach arbitrary files to a PDF document
- cooltooltips: associate a pop-up window and tooltip with PDF
  hyperlinks
- movie15: multimedia inclusion package.
- pdfcprot: activating and setting of character protruding using
  pdflatex.
- pdfsync: provide links between source and PDF.
- pdftricks: support for pstricks in pdfTeX.
- pdfscreen: support screen-based document design.

%description latex-pdftools -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- attachfile: fájlok csatolása PDF dokumentumokba
- cooltooltips: felugró ablakok és súgók társítása PDF linkekhez
- movie15: multimédia beillesztése
- pdfcprot: activating and setting of character protruding using
  pdflatex.
- pdftricks: pstricks támogatás pdfTeX-ben
- pdfsync: provide links between source and PDF.
- pdfscreen: képernyő alapú dokumentumok

%description latex-pdftools -l pl.UTF-8
Ten pakiet zawiera:
- attachfile: dołączanie dowolnych plików do dokumentu PDF.
- cooltooltips: wiązanie okienek i podpowiedzi z hiperłączami PDF.
- movie15: pakiet do włączania multimediów.
- pdfcprot: aktywacja i ustawianie odstających znaków w pdflatexu.
- pdfsync: powiązania między źródłem a PDF-em.
- pdftricks: obsługa pstricks w pdfTeXu.
- pdfscreen: wsparcie projektowania dokumentów ekranowych.

%package latex-microtype
Summary:	An interface to the micro-typographic extensions of pdfTeX
Summary(pl.UTF-8):	Interfejs do rozszerzeń mikrotypograficznych pdfTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-microtype < 1:3.1
BuildArch:	noarch

%description latex-microtype
The `microtype' package provides a LaTeX interface to pdfTeX's
micro-typographic extensions: character protrusion and font expansion.
It allows to restrict character protrusion and/or font expansion to a
definable set of fonts, and to configure micro-typographic aspects of
the fonts in a straight-forward and flexible way. Settings for various
fonts are provided.

%description latex-microtype -l pl.UTF-8
Pakiet microtype dodaje do LaTeXa mechanizm do rozszerzeń
mikrotypograficznych pdfTeXa: wysuwania znaków i rozszerzania fontów.
Pozwala ograniczyć wysuwanie znaku i/lub rozszerzanie fontu do
określonego zbioru fontów oraz skonfigurować mikrotypograficzne
aspekty fontów w prosty i elastyczny sposób. Dostarczone są ustawienia
dla różnych fontów.

%package latex-musictex
Summary:	Typesetting music with TeX
Summary(hu.UTF-8):	Zenék szedése TeX-hel
Summary(pl.UTF-8):	Skład muzyki w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-musictex
Typesetting music with TeX.

%description latex-musictex -l hu.UTF-8
Zenék szedése TeX-hel.

%description latex-musictex -l pl.UTF-8
Skład muzyki w LaTeXu.

%package latex-lucidabr
Summary:	Package to make Lucida Bright fonts usable with LaTeX
Summary(pl.UTF-8):	Pakiet umożliwiający używanie fontów Lucida Bright w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-lucidabr < 1:3.1
BuildArch:	noarch

%description latex-lucidabr
Package to make Lucida Bright fonts usable with LaTeX.

%description latex-lucidabr -l pl.UTF-8
Pakiet umożliwiający używanie fontów Lucida Bright w LaTeXu.

%package latex-marvosym
Summary:	Styles for Martin Vogel's Symbol (marvosym) font
Summary(pl.UTF-8):	Style dla fontu Symbol Martina Vogela (marvosym)
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-marvosym = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-marvosym
Obsoletes:	tetex-latex-marvosym < 1:3.1
BuildArch:	noarch

%description latex-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols for
structural engineering; Symbols for steel cross-sections; Astronomy
signs (Sun, Moon, planets); The 12 signs of the zodiac; Scissor
symbols; CE sign and others.

%description latex-marvosym -l pl.UTF-8
Font Martin Vogel's Symbol (marvosym) to font zawierający: symbol
waluty Euro zdefiniowany przez Komisję Europejską; symbole Euro w
krojach Times, Helvetica i Courier; symbole do inżynierii
strukturalnej; symbole do przekrojów stalowych; znaki astronomiczne
(Słońce, Księżyc, planety); 12 znaków Zodiaku; symbole nożyczek; znak
CE i inne.

%package latex-mflogo
Summary:	LaTeX support for MetaFont and logo fonts
Summary(pl.UTF-8):	Obsługa LaTeXa dla MetaFonta i fontów logo
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-mflogo = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-mflogo < 1:3.1
BuildArch:	noarch

%description latex-mflogo
LaTeX package and font definition file to access the Knuthian `logo'
fonts described in `The MetaFontbook' and the MetaFont and logos in
LaTeX documents.

%description latex-mflogo -l pl.UTF-8
Pakiet LaTeXa i plik definicji fontów udostępniający fonty logo Knutha
opisane w "The MetaFontbook" oraz MetaFont i loga w dokumentach
LaTeXa.

%package latex-mfnfss
Summary:	Font description files to use extra fonts like yinit and ygoth
Summary(pl.UTF-8):	Pliki opisów fontów udostępniające dodatkowe fonty, jak yinit i ygoth
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-mfnfss < 1:3.1
BuildArch:	noarch

%description latex-mfnfss
Font description files to use extra fonts like yinit and ygoth.

%description latex-mfnfss -l pl.UTF-8
Pliki opisów fontów udostępniające dodatkowe fonty, jak yinit i ygoth.

%package latex-minitoc
Summary:	Produce a table of contents for each chapter
Summary(pl.UTF-8):	Tworzenie spisów treści dla każdego rozdziału
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-minitoc < 1:3.1
BuildArch:	noarch

%description latex-minitoc
Produce a table of contents for each chapter.

%description latex-minitoc -l pl.UTF-8
Tworzenie spisów treści dla każdego rozdziału.

%package latex-mltex
Summary:	Support for MLTeX
Summary(pl.UTF-8):	Wsparcie dla MLTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-mltex < 1:3.1
BuildArch:	noarch

%description latex-mltex
Support for MLTeX, the multilingual TeX extension from Michael J.
Ferguson.

%description latex-mltex -l pl.UTF-8
Wsparcie dla MLTeXa - rozszerzenia TeXa z obsługą wielu języków,
autorstwa Michaela J. Fergusona.

%package latex-multienum
Summary:	Multi-column enumerated lists
Summary(hu.UTF-8):	Többoszlopos számozott listák
Summary(pl.UTF-8):	Wielokolumnowe listy numerowane
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-multienum
Multi-column enumerated lists.

%description latex-multienum -l hu.UTF-8
Többoszlopos számozott listák.

%description latex-multienum -l pl.UTF-8
Wielokolumnowe listy numerowane.

%package latex-moreverb
Summary:	Extended verbatim
Summary(hu.UTF-8):	Kiterjesztett verbatim
Summary(pl.UTF-8):	Rozszerzony maszynopis
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-moreverb
Extended verbatim.

%description latex-moreverb -l hu.UTF-8
Kiterjesztett verbatim.

%description latex-moreverb -l pl.UTF-8
Rozszerzony maszynopis.

%package latex-ntheorem
Summary:	Enhanced theorem environment
Summary(hu.UTF-8):	Bővített tétel környezet
Summary(pl.UTF-8):	Rozszerzone środowisko theorem
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-ntheorem
Enhanced theorem environment.

%description latex-ntheorem -l hu.UTF-8
Bővített tétel környezet

%description latex-ntheorem -l pl.UTF-8
Rozszerzone środowisko theorem.

%package latex-other
Summary:	Other LaTeX packages
Summary(hu.UTF-8):	Néhány további LaTeX csomag
Summary(pl.UTF-8):	Inne pakiety LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-platex < 1:3.1
BuildArch:	noarch

%description latex-other
Other LaTeX packages.

%description latex-other -l hu.UTF-8
Néhány további LaTeX csomag.

%description latex-other -l pl.UTF-8
Inne pakiety LaTeXa.

%package latex-other-doc
Summary:	Other LaTeX packages documentation
Summary(hu.UTF-8):	Néhány további LaTeX csomag dokumentációja
Summary(pl.UTF-8):	Dokumentacja do innych pakietów LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-other-doc
Other LaTeX packages documentation.

%description latex-other-doc -l hu.UTF-8
Néhány további LaTeX csomag dokumentációja.

%description latex-other-doc -l pl.UTF-8
Dokumentacja do innych pakietów LaTeXa.

%package latex-pdfslide
Summary:	Presentation slides using pdftex
Summary(hu.UTF-8):	Prezentáció készítése pdftex-hel
Summary(pl.UTF-8):	Slajdy do prezentacji z użyciem pdftexa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pdfslide
Presentation slides using pdftex.

%description latex-pdfslide -l hu.UTF-8
Prezentáció készítése pdftex-hel.

%description latex-pdfslide -l pl.UTF-8
Slajdy do prezentacji z użyciem pdftexa.

%package latex-pgf
Summary:	The TeX Portable Graphic Format
Summary(hu.UTF-8):	TeX Portable Graphic Formátum
Summary(pl.UTF-8):	Przenośny format grafiki dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-xcolor = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-pgf < 2.01
BuildArch:	noarch

%description latex-pgf
A macro package for creating graphics directly in TeX and LaTeX.

%description latex-pgf -l hu.UTF-8
Makró csomag rajzok készítéséhez közvetlenül TeX-ben és LaTeX-ben.

%description latex-pgf -l pl.UTF-8
Pakiet makr do tworzenia grafiki bezpośrednio z TeXa i LaTeXa.

%package latex-polynom
Summary:	Macros for manipulating polynomials
Summary(hu.UTF-8):	Makrók polinomokkal való műveletekre
Summary(pl.UTF-8):	Makra do operacji na wielomianach
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-polynom
Macros for manipulating polynomials.

%description latex-polynom -l hu.UTF-8
Makrók polinomokkal való műveletekre.

%description latex-polynom -l pl.UTF-8
Makra do operacji na wielomianach.

%package latex-polynomial
Summary:	Typeset (univariate) polynomials
Summary(hu.UTF-8):	Egyváltozós polinomok szedése
Summary(pl.UTF-8):	Skład wielomianów (jednej zmiennej)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-polynomial
Typeset (univariate) polynomials.

%description latex-polynomial -l hu.UTF-8
Egyváltozós polinomok szedése.

%description latex-polynomial -l pl.UTF-8
Skład wielomianów (jednej zmiennej).

%package latex-programming
Summary:	Additional utilities to programming LaTeX
Summary(hu.UTF-8):	További eszközök LaTeX programozásához
Summary(pl.UTF-8):	Dodatkowe narzędzia do programowania LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-programming
This package contains:
- cmdtrack: check used commands.
- cool: COntent-Oriented LaTeX
- coollist: manipulate COntent Oriented LaTeX Lists.
- coolstr: string manipulation in LaTeX.
- csvtools: reading data from CSV files.
- datatool: tools to load and manipulate data.
- datenumber: convert a date into a number and vice versa.
- delimtxt: read and parse text tables.
- dialogl: macros for constructing interactive LaTeX scripts.
- dprogress: LaTeX-relevant log information for debugging.
- environ: a new interface for environments in LaTeX.
- export: import and export values of LaTeX registers.
- fmtcount: display the value of a LaTeX counter in a variety of
  formats.
- forarray: using array structures in LaTeX.
- forloop: iteration in LaTeX.
- inversepath: calculate inverse file paths.
- labelcas: check the existence of labels, and fork accordingly.
- lcg: generate random integers.
- makecmds: the new \makecommand command always (re)defines a command.
- multido: a loop facility for Generic TeX.
- namespc: rudimentary c++-like namespaces in LaTeX.
- patchcmd: change the definition of an existing command.
- progress: creates an overview of a document's state.
- randtext: randomise the order of characters in strings.
- regcount: display the allocation status of the TeX registers.
- robustcommand: declare robust command, with \newcommand checks.
- splitindex: unlimited number of indexes.
- stack: tools to define and use stacks.
- stringstrings: string manipulation for cosmetic and programming
  application
- substr: deal with substrings in strings.
- typedref: eliminate errors by enforcing the types of labels.

%description latex-programming -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- cmdtrack: használt parancsok ellenőrzése
- cool: tartalom-orientált (COntent-Oriented) LaTeX
- coollist: COntent Oriented LaTeX listák manipulációja
- coolstr: sztring manipuláció LaTeX-ben
- csvtools: adatok olvasása CSV fájlokból
- datatool: eszközök adatok beolvasására és manipulációjához
- datenumber: dátum számmá konvertálása és vissza
- delimtxt: szöveges táblázatok olvasása és feldolgozása
- dialogl: interaktív makrók LaTeX-ben
- dprogress: LaTeX-releváns log információ debuggoláshoz
- export: LaTeX regiszterek értékeinek importálása és exportálása
- environ: egy új felület környezetek létrehozására
- fmtcount: LaTeX számlálók megjelenítése különböző formátumokban
- forarray: tömb struktúrák LaTeX-ben
- forloop: iteráció LaTeX-ben
- inversepath: fájlútvonalak visszafele relatív meghatározása
- labelcas: cimkék létezésének ellenőrzése
- lcg: véletlen egész számok generálása
- makecmds: új \makecommand, amely mindig (újra)definiál parancsot
- multido: ciklusok szervezése LaTeX-ben
- namespc: c++-szerű névterek LaTeX-ben
- patchcmd: létező parancsok definíciójának megváltoztatása
- progress: egy áttekintést készít a dokumentum állapotáról
- randtext: sztring karaktereinek összekeverése
- regcount: display the allocation status of the TeX registers.
- robustcommand: declare robust command, with \newcommand checks.
- splitindex: unlimited number of indexes.
- stack: verem használata
- stringstrings: sztring manipuláció
- substr: részszövegek keresése
- typedref: eliminate errors by enforcing the types of labels.

%description latex-programming -l pl.UTF-8
Ten pakiet zawiera:
- cmdtrack: sprawdzanie użytych poleceń.
- cool: COntent-Oriented LaTeX (LaTeX zorientowany kontekstowo).
- coollist: operowanie na listach w COntent Oriented LaTeXu.
- coolstr: operacje na łańcuchach w LaTeXu.
- csvtools: odczyt danych z plików CSV.
- datatool: narzędzia do wczytywania i operacji na danych.
- datenumber: konwersja dat na liczby i na odwrót.
- delimtxt: odczyt i analiza tablic tekstowych.
- dialogl: makra do tworzenia interaktywnych skryptów w LaTeXu.
- dprogress: logi diagnostyczne dla LaTeXa.
- environ: nowy interfejs dla środowisk w LaTeXu.
- export: import i eksport wartości rejestrów LaTeXa.
- fmtcount: wyświetlanie wartości licznika LaTwXowego w różnych
  formatach.
- forarray: użycie struktur tablicowych w LaTeXu.
- forloop: iterowanie w LaTeXu.
- inversepath: obliczanie odwróconych ścieżek plików.
- labelcas: sprawdzanie istnienia etykiet i odgałęzianie.
- lcg: generowanie całkowitych liczb losowych.
- makecmds: nowe polecenie \makecommand zawsze definiujące polecenie.
- multido: usprawnienie pętli w Generic TeXu.
- namespc: podstawowe przestrzenie nazw w stylu C++ w LaTeXu.
- patchcmd: zmiana definicji istniejącego polecenia.
- progress: tworzenie przeglądu stanu dokumentu.
- randtext: losowa kolejność znaków w łańcuchu.
- regcount: wyświetlenie stanu przydziału rejestrów TeXa.
- robustcommand: deklaracja poleceń z kontrolą \newcommand.
- splitindex: nieograniczona liczba indeksów.
- stack: narzędzia do definiowania i używania stosów.
- stringstrings: operacje na łańcuchach do zastosowań kosmetycznych i
  w programowaniu
- substr: obsługa podciągów w łańcuchach.
- typedref: eliminacja błędów przez wymuszanie typów etykiet.

%package latex-prosper
Summary:	LaTeX class for high quality slides
Summary(hu.UTF-8):	LaTeX osztály jó minőségű fóliák készítéséhez
Summary(pl.UTF-8):	Klasy LaTeXa do slajdów wysokiej jakości
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-xetex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-prosper
LaTeX class for high quality slides.

%description latex-prosper -l hu.UTF-8
LaTeX osztály jó minőségű fóliák készítéséhez.

%description latex-prosper -l pl.UTF-8
Klasy LaTeXa do slajdów wysokiej jakości.

%package latex-pseudocode
Summary:	LaTeX enviroment for specifying algorithms in a natural way
Summary(hu.UTF-8):	LaTeX környezet algoritmusok bevitelére
Summary(pl.UTF-8):	Środowisko LaTeXa do opisu algorytmów w sposób naturalny
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pseudocode
LaTeX enviroment for specifying algorithms in a natural way.

%description latex-pseudocode -l hu.UTF-8
LaTeX környezet algoritmusok bevitelére.

%description latex-pseudocode -l pl.UTF-8
Środowisko LaTeXa do opisu algorytmów w sposób naturalny.

%package latex-psnfss
Summary:	LaTeX font support for common PostScript fonts
Summary(pl.UTF-8):	Obsługa popularnych fontów postscriptowych w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-adobe = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-psnfss
Obsoletes:	tetex-latex-mathptm < 1:3.1
Obsoletes:	tetex-latex-mathptmx < 1:3.1
Obsoletes:	tetex-latex-psnfss < 1:3.1
BuildArch:	noarch

%description latex-psnfss
LaTeX font definition files, macros and font metrics for common
PostScript fonts.

%description latex-psnfss -l pl.UTF-8
LaTeXowe pliki definicji fontów, makra i metryki fontów dla
popularnych fontów postscriptowych.

%package latex-pst-2dplot
Summary:	A PSTricks package for drawing 2D curves
Summary(hu.UTF-8):	PSTricks csomag kétdimenziós görbék rajzolásához
Summary(pl.UTF-8):	Pakiet PSTricks do rysowania krzywych 2D
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-2dplot
A PSTricks package for drawing 2D curves.

%description latex-pst-2dplot -l hu.UTF-8
PSTricks csomag kétdimenziós görbék rajzolásához.

%description latex-pst-2dplot -l pl.UTF-8
Pakiet PSTricks do rysowania krzywych 2D.

%package latex-pst-3dplot
Summary:	Draw 3d curves and graphs using PSTricks
Summary(hu.UTF-8):	3D-s görbék és grafikonok PSTricks-szel
Summary(pl.UTF-8):	Rysowanie krzywych i wykresów 3D przy użyciu PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-3dplot
Draw 3d curves and graphs using PSTricks.

%description latex-pst-3dplot -l hu.UTF-8
3D-s görbék és grafikonok PSTricks-szel.

%description latex-pst-3dplot -l pl.UTF-8
Rysowanie krzywych i wykresów 3D przy użyciu PSTricks.

%package latex-pst-bar
Summary:	Produces bar charts using PSTricks
Summary(hu.UTF-8):	Oszlopdiagramok PSTricks-szel
Summary(pl.UTF-8):	Tworzenie wykresów słupkowych przy użyciu PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-bar
Produces bar charts using PSTricks.

%description latex-pst-bar -l hu.UTF-8
Oszlopdiagramok PSTricks-szel.

%description latex-pst-bar -l pl.UTF-8
Tworzenie wykresów słupkowych przy użyciu PSTricks.

%package latex-pst-circ
Summary:	PSTricks package for drawing electric circuits
Summary(hu.UTF-8):	PSTricks csomag elektromos áramkörök rajzolásához
Summary(pl.UTF-8):	Pakiet PSTricks do rysowania schematów elektrycznych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-circ
PSTricks package for drawing electric circuits.

%description latex-pst-circ -l hu.UTF-8
PSTricks csomag elektromos áramkörök rajzolásához.

%description latex-pst-circ -l pl.UTF-8
Pakiet PSTricks do rysowania schematów elektrycznych.

%package latex-pst-diffraction
Summary:	Print diffraction patterns from various apertures
Summary(hu.UTF-8):	Diffrakciós képek különböző eszközökön
Summary(pl.UTF-8):	Drukowanie wzorów dyfrakcji z różnych szczelin
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-diffraction
Print diffraction patterns from various apertures.

%description latex-pst-diffraction -l hu.UTF-8
Diffrakciós képek különböző eszközökön.

%description latex-pst-diffraction -l pl.UTF-8
Drukowanie wzorów dyfrakcji z różnych szczelin.

%package latex-pst-eucl
Summary:	Euclidian geometry with PSTricks
Summary(hu.UTF-8):	Euklidészi geometria a PSTricks használatával
Summary(pl.UTF-8):	Geometria euklidesowa przy użyciu PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-eucl
Euclidian geometry with PSTricks.

%description latex-pst-eucl -l hu.UTF-8
Euklidészi geometria a PSTricks használatával.

%description latex-pst-eucl -l pl.UTF-8
Geometria euklidesowa przy użyciu PSTricks.

%package latex-pst-fun
Summary:	Draw "funny" objects with PSTricks
Summary(hu.UTF-8):	"Vicces" rajzok PSTricks-szel
Summary(pl.UTF-8):	Rysowanie "zabawnych" obiektów przy użyciu PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-fun
Draw "funny" objects with PSTricks.

%description latex-pst-fun -l hu.UTF-8
"Vicces" rajzok PSTricks-szel.

%description latex-pst-fun -l pl.UTF-8
Rysowanie "zabawnych" obiektów przy użyciu PSTricks.

%package latex-pst-func
Summary:	PSTricks package for plotting mathematical functions
Summary(hu.UTF-8):	PSTricks csomag matematikai függvények ábrázolásához
Summary(pl.UTF-8):	Pakiet PSTricks do rysowania funkcji matematycznych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-func
PSTricks package for plotting mathematical functions.

%description latex-pst-func -l hu.UTF-8
PSTricks csomag matematikai függvények ábrázolásához.

%description latex-pst-func -l pl.UTF-8
Pakiet PSTricks do rysowania funkcji matematycznych.

%package latex-pst-fr3d
Summary:	Draw 3-dimensional framed boxes using PSTricks
Summary(hu.UTF-8):	Háromdimenziós dobozok PSTricks segítségével
Summary(pl.UTF-8):	Rysowanie trójwymiarowych obramowań przy użyciu PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-fr3d
Draw 3-dimensional framed boxes using PSTricks.

%description latex-pst-fr3d -l hu.UTF-8
Háromdimenziós dobozok PSTricks segítségével.

%description latex-pst-fr3d -l pl.UTF-8
Rysowanie trójwymiarowych obramowań przy użyciu PSTricks.

%package latex-pst-fractal
Summary:	Draw fractal sets using PSTricks
Summary(hu.UTF-8):	Fraktálok rajzolása PSTricks segítségével
Summary(pl.UTF-8):	Rysowanie zbiorów fraktalnych przy użyciu PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-fractal
Draw fractal sets using PSTricks.

%description latex-pst-fractal -l hu.UTF-8
Fraktálok rajzolása PSTricks segítségével.

%description latex-pst-fractal -l pl.UTF-8
Rysowanie zbiorów fraktalnych przy użyciu PSTricks.

%package latex-pst-infixplot
Summary:	Using PSTricks plotting capacities with infix expressions rather than RPN
Summary(hu.UTF-8):	Infix kifejezések ábrázolása
Summary(pl.UTF-8):	Używanie PSTricks z wyrażeniami infiksowymi zamiast RPN
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-infixplot
Using PSTricks plotting capacities with infix expressions rather than
RPN.

%description latex-pst-infixplot -l hu.UTF-8
Infix kifejezések ábrázolása.

%description latex-pst-infixplot -l pl.UTF-8
Używanie PSTricks z wyrażeniami infiksowymi zamiast RPN.

%package latex-pst-math
Summary:	Enhancement of PostScript math operators to use with PSTricks
Summary(hu.UTF-8):	PostScript matematikai operátorok bővítése PSTricks-szel
Summary(pl.UTF-8):	Rozszerzenie operatorów matematycznych PostScriptu do użycia z PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-math
Enhancement of PostScript math operators to use with pstricks.

%description latex-pst-math -l hu.UTF-8
PostScript matematikai operátorok bővítése pstricks-szel.

%description latex-pst-math -l pl.UTF-8
Rozszerzenie operatorów matematycznych PostScriptu do użycia z
PSTricks.

%package latex-pst-ob3d
Summary:	Three dimensional objects using PSTricks
Summary(hu.UTF-8):	Háromdimenziós objektumok PSTricks-szel
Summary(pl.UTF-8):	Obiekty trójwymiarowe przy użyciu PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-ob3d
Three dimensional objects using PSTricks.

%description latex-pst-ob3d -l hu.UTF-8
Háromdimenziós objektumok PSTricks-szel.

%description latex-pst-ob3d -l pl.UTF-8
Obiekty trójwymiarowe przy użyciu PSTricks.

%package latex-pst-optexp
Summary:	Drawing optical experimental setups
Summary(hu.UTF-8):	Optikai összeállítások rajzolása
Summary(pl.UTF-8):	Rysowanie konfiguracji doświadczeń optycznych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-optexp
Drawing optical experimental setups.

%description latex-pst-optexp -l hu.UTF-8
Optikai összeállítások rajzolása.

%description latex-pst-optexp -l pl.UTF-8
Rysowanie konfiguracji doświadczeń optycznych.

%package latex-pst-optic
Summary:	Drawing optics diagrams
Summary(hu.UTF-8):	Optikai ábrák rajzolása
Summary(pl.UTF-8):	Rysowanie diagramów optycznych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-optic
Drawing optics diagrams.

%description latex-pst-optic -l hu.UTF-8
Optikai ábrák rajzolása.

%description latex-pst-optic -l pl.UTF-8
Rysowanie diagramów optycznych.

%package latex-pst-text
Summary:	Text and character manipulation in PSTricks
Summary(hu.UTF-8):	Szöveg és karakter manipulációk PSTricks-szel
Summary(pl.UTF-8):	Operacje na tekście i znakach przy użyciu PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-text
Text and character manipulation in PSTricks.

%description latex-pst-text -l hu.UTF-8
Szöveg és karakter manipulációk PSTricks-szel.

%description latex-pst-text -l pl.UTF-8
Operacje na tekście i znakach przy użyciu PSTricks.

%package latex-pst-uncategorized
Summary:	Other uncategorized PSTricks packages
Summary(hu.UTF-8):	Néhány kategorizálatlan PSTricks csomag
Summary(pl.UTF-8):	Inne nieskategoryzowane pakiety PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-pst-uncategorized
Other uncategorized PSTricks packages.

%description latex-pst-uncategorized -l hu.UTF-8
Néhány kategorizálatlan PSTricks csomag.

%description latex-pst-uncategorized -l pl.UTF-8
Inne nieskategoryzowane pakiety PSTricks.

%package latex-pxfonts
Summary:	PX fonts LaTeX support
Summary(pl.UTF-8):	Obsługa fontów PX w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-px = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-pxfonts < 1:3.1
BuildArch:	noarch

%description latex-pxfonts
PX fonts LaTeX support.

%description latex-pxfonts -l pl.UTF-8
Obsługa fontów PX w LaTeXu.

%package latex-SIstyle
Summary:	Package to typeset SI units, numbers and angles
Summary(hu.UTF-8):	Csomag SI egységek, számok és szögek szedésére
Summary(pl.UTF-8):	Pakiet do składu jednostek SI, liczb i kątów
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex-ams = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-SIstyle
Package to typeset SI units, numbers and angles.

%description latex-SIstyle -l hu.UTF-8
Csomag SI egységek, számok és szögek szedésére.

%description latex-SIstyle -l pl.UTF-8
Pakiet do składu jednostek SI, liczb i kątów.

%package latex-SIunits
Summary:	The SIunits package can be used to standardise the use of units in your writings
Summary(hu.UTF-8):	Az SIunits csomag a mennyiségek egységes írásában nyújt segítséget
Summary(pl.UTF-8):	Pakiet SIunits - standaryzacja użycia jednostek w artykułach
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex-ams = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-SIunits
The SIunits package can be used to standardise the use of units in
your writings.

%description latex-SIunits -l hu.UTF-8
Az SIunits csomag a mennyiségek egységes írásában nyújt segítséget.

%description latex-SIunits -l pl.UTF-8
Pakiet SIunits może być używany do ustandaryzowania użycia jednostek w
artykułach.

%package latex-siunitx
Summary:	A comprehensive (SI) units package
Summary(hu.UTF-8):	Egy minden részletre kiterjedő (SI) egységek kezelését végző csomag
Summary(pl.UTF-8):	Obszerny pakiet jednostek (SI)
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-siunitx
A comprehensive (SI) units package.

%description latex-siunitx -l hu.UTF-8
Egy minden részletre kiterjedő (SI) egységek kezelését végző csomag.

%description latex-siunitx -l pl.UTF-8
Obszerny pakiet jednostek (SI).

%package latex-sources
Summary:	LaTeX sources
Summary(hu.UTF-8):	LaTeX források
Summary(pl.UTF-8):	Źródła LaTeXa
Group:		Applications/Publishing/TeX
BuildArch:	noarch

%description latex-sources
LaTeX sources.

%description latex-sources -l hu.UTF-8
LaTeX források.

%description latex-sources -l pl.UTF-8
Źródła LaTeXa.

%package latex-styles
Summary:	Various LaTeX styles
Summary(hu.UTF-8):	Különböző LaTeX stílusok
Summary(pl.UTF-8):	Różne style LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-styles
Various LaTeX styles.

%description latex-styles -l hu.UTF-8
Különböző LaTeX stílusok.

%description latex-styles -l pl.UTF-8
Różne style LaTeXa.

%package latex-lang
Summary:	LaTeX support for non-english languages
Summary(hu.UTF-8):	LaTeX támogatás nem-angol nyelvekhez
Summary(pl.UTF-8):	Wsparcie LaTeXa dla języków nieangielskich
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-lang
LaTeX support for non-english languages.

%description latex-lang -l hu.UTF-8
LaTeX támogatás nem-angol nyelvekhez.

%description latex-lang -l pl.UTF-8
Wsparcie LaTeXa dla języków nieangielskich.

%package latex-Tabbing
Summary:	Tabbing with accented letters
Summary(hu.UTF-8):	Tabbing környezet ékezetes betűk használatával
Summary(pl.UTF-8):	Tabele z literami akcentowanymi
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
BuildArch:	noarch

%description latex-Tabbing
Tabbing with accented letters.

%description latex-Tabbing -l hu.UTF-8
Tabbing környezet ékezetes betűk használatával.

%description latex-Tabbing -l pl.UTF-8
Tabele z literami akcentowanymi.

%package latex-txfonts
Summary:	TX fonts LaTeX support
Summary(pl.UTF-8):	Obsługa fontów TX w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-tx = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-txfonts < 1:3.1
BuildArch:	noarch

%description latex-txfonts
TX fonts LaTeX support.

%description latex-txfonts -l pl.UTF-8
Obsługa fontów TX w LaTeXu.

%package latex-ucs
Summary:	Support for using UTF-8 as input encoding in LaTeX documents
Summary(hu.UTF-8):	Ez a csomag lehetővé teszi UTF-8 kódolást a LaTeX dokumentumokban
Summary(pl.UTF-8):	Obsługa UTF-8 jako kodowania wejściowego w dokumentach LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-ucs
This package contains support for using UTF-8 as input encoding in
LaTeX documents.

%description latex-ucs -l hu.UTF-8
Ez a csomag lehetővé teszi UTF-8 kódolást a LaTeX dokumentumokban.

%description latex-ucs -l pl.UTF-8
Ten pakiet zawiera obsługę używania UTF-8 jako kodowania wejściowego w
dokumentach LaTeXa.

%package latex-umlaute
Summary:	An interface to inputenc for using alternate input encodings
Summary(pl.UTF-8):	Interfejs inputenc do używania alternatywnych kodowań wejściowych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-umlaute < 1:3.1
BuildArch:	noarch

%description latex-umlaute
An interface to inputenc for using alternate input encodings.

%description latex-umlaute -l pl.UTF-8
Interfejs inputenc do używania alternatywnych kodowań wejściowych.

%package latex-wasysym
Summary:	Extra characters from the Waldis symbol fonts
Summary(pl.UTF-8):	Dodatkowe znaki z fontów Waldis symbol
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-wasy = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-wasysym
Obsoletes:	tetex-latex-wasysym < 1:3.1
BuildArch:	noarch

%description latex-wasysym
Makes some additional characters available that come from the wasy
fonts (Waldis symbol fonts). These fonts are not automatically
included in NFSS2/LaTeX2e since they take up important space and often
aren't necessary if one makes use of the packages amsfonts or amssymb.
Symbols include: join box, diamond, leadsto, sqsubset, lhd, rhd,
apple, ocircle invneg, logof, varint, male, female, phone, clock,
lightning, pointer, sun, bell, permil, smiley, various electrical
symbols, shapes, music notes, circles, signs, astronomy, etc.

%description latex-wasysym -l pl.UTF-8
Pakiet udostępniający dodatkowe symbole pochodzące z fontów wasy
(Waldis symbol). Te fonty nie są automatycznie dołączane w
NFSS2/LaTeX2e, ponieważ zajmują miejsce i zazwyczaj nie są potrzebne
jeśli używa się pakietów amsfonts lub amssymb. Zestaw symboli zawiera
m.in.: symbole join box, diamond, leadsto, sqsubset, lhd, rhd, apple,
ocircle invneg, logof, varint, male, female, phone, clock, lightning,
pointer, sun, bell, permil, smiley oraz różne symbole elektryczne,
kształty, nuty, okręgi, znaki, symbole astronomiczne itp.

%package latex-xcolor
Summary:	Allows for access to color tints, shades, tones etc
Summary(hu.UTF-8):	Hozzáférés színekhez, tónusokhoz, átmenetekhez, stb.
Summary(pl.UTF-8):	Pozwala na dostęp do odcieni, gradientów itp.
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-latex-xcolor < 2.01
BuildArch:	noarch

%description latex-xcolor
`xcolor' provides easy driver-independent access to several kinds of
color tints, shades, tones, and mixes of arbitrary colors. It allows
to select a document-wide target color model and offers tools for
automatic color schemes, conversion between eight color models, and
alternating table row colors.

%description latex-xcolor -l hu.UTF-8
`xcolor' egy egyszerű meghajtó-független hozzáférést biztosít
színekhez, átmenetekhez, tónusokhóz, és a színek korlátlan
keverékéhez. Lehetőséged van a teljes dokumentumra érvényes szín
modell kiválasztásához és a színmodellek közötti konverzióra.

%description latex-xcolor -l pl.UTF-8
`xcolor' dostarcza łatwego, niezależnego od urządzenia dostępu do
wielu rodzai cieniowania, tonów i połączeń dowolnych kolorów. Pozwala
na wybór modelu koloru dla całego dokumentu i oferuje narzędzia dla
schematów kolorów, konwersji między ośmioma modelami kolorów oraz
naprzemiennych kolorów w tabelach.

%package format-pdflatex
Summary:	PDF LaTeX macro package
Summary(pl.UTF-8):	Pakiet makr PDF LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-jknappen = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-type1-urw = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-psnfss = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Provides:	tetex-format-pdflatex
Obsoletes:	tetex-format-pdflatex < 1:3.1
BuildArch:	noarch

%description format-pdflatex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains PDF LaTeX format.

%description format-pdflatex -l pl.UTF-8
LaTeX jest frontendem do systemu formatującego tekst TeX. Jest
łatwiejszy w użyciu niż TeX. Jest właściwie zestawem makr TeXowych,
dających użytkownikom wygodne, predefiniowane formaty dokumentów.

Ten pakiet zawiera format PDF LaTeX.

%package scripts
Summary:	Various scripts
Summary(hu.UTF-8):	Néhány szkript
Summary(pl.UTF-8):	Różne pisma
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description scripts
Various scripts.

%description scripts -l hu.UTF-8
Néhány szkript.

%description scripts -l pl.UTF-8
Różne pisma.

%package tlmgr
Summary:	TeXLive manager
Summary(hu.UTF-8):	TeXLive manager
Summary(pl.UTF-8):	Zarządca TeXLive'a
Group:		Applications/Publishing/TeX
BuildArch:	noarch

%description tlmgr
tlmgr manages an existing TeX Live installation, both packages and
configuration options. It performs many of the same actions as
texconfig, and more besides.

%description tlmgr -l hu.UTF-8
tlmgr egy létező TeX Live telepítést tart karban, csomag és beállítás
tekintetében is. Hasonló műveleteket végez, mint a texconfig, sőt,
többet is.

%description tlmgr -l pl.UTF-8
tlmgr zarządza istniejącą instalacją TeX Live'a - zarówno pakietami,
jak i opcjami konfiguracyjnymi. Wykonuje podobne czynności, co m.in.
texconfig.

# # TeX generic macros #

%package tex-babel
Summary:	Multilingual support for TeX
Summary(pl.UTF-8):	Obsługa wielu języków dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-babel
Obsoletes:	tetex-tex-babel < 1:3.1
BuildArch:	noarch

%description tex-babel
Multilingual support for TeX.

%description tex-babel -l pl.UTF-8
Obsługa wielu języków dla TeXa.

%package tex-german
Summary:	Supports the new German orthography (neue deutsche Rechtschreibung)
Summary(pl.UTF-8):	Obsługa nowej ortografii niemieckiej (neue deutsche Rechtschreibung)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-german
Obsoletes:	tetex-tex-german < 1:3.1
BuildArch:	noarch

%description tex-german
Supports the new German orthography (neue deutsche Rechtschreibung).

%description tex-german -l pl.UTF-8
Obsługa nowej ortografii niemieckiej (neue deutsche Rechtschreibung).

%package tex-insbox
Summary:	A TeX macro for inserting pictures/boxes into paragraphs
Summary(hu.UTF-8):	TeX makró képek/dobozok beszúrására bekezdésekbe
Summary(pl.UTF-8):	Makro TeXa do wstawiania obrazów/pól wewnątrz ustępów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description tex-insbox
A TeX macro for inserting pictures/boxes into paragraphs.

%description tex-insbox -l hu.UTF-8
TeX makró képek/dobozok beszúrására bekezdésekbe.

%description tex-insbox -l pl.UTF-8
Makro TeXa do wstawiania obrazów/pól wewnątrz ustępów.

%package tex-mfpic
Summary:	Macros which generate Metafont or Metapost for drawing pictures
Summary(pl.UTF-8):	Makra generujące Metafont lub Metapost do rysowania obrazków
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-mfpic < 1:3.1
BuildArch:	noarch

%description tex-mfpic
Macros which generate Metafont or Metapost for drawing pictures.

%description tex-mfpic -l pl.UTF-8
Makra generujące Metafont lub Metapost do rysowania obrazków.

%package tex-misc
Summary:	Miscellaneous TeX macros
Summary(pl.UTF-8):	Różne makra TeXowe
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-misc
Obsoletes:	tetex-tex-eijkhout < 1:3.1
Obsoletes:	tetex-tex-misc < 1:3.1
BuildArch:	noarch

%description tex-misc
Miscellaneous TeX macros.

%description tex-misc -l pl.UTF-8
Różne makra TeXowe.

%package tex-pictex
Summary:	Picture drawing macros for TeX and LaTeX
Summary(pl.UTF-8):	Makra do rysowania obrazków dla TeXa i LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-pictex < 1:3.1
BuildArch:	noarch

%description tex-pictex
Picture drawing macros for TeX and LaTeX.

%description tex-pictex -l pl.UTF-8
Makra do rysowania obrazków dla TeXa i LaTeXa.

%package tex-psizzl
Summary:	A TeX format for physics papers
Summary(hu.UTF-8):	TeX formátum fizikai kiadványokhoz
Summary(pl.UTF-8):	Format TeXa do artykułów fizycznych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description tex-psizzl
A TeX format for physics papers.

%description tex-psizzl -l hu.UTF-8
TeX formátum fizikai kiadványokhoz.

%description tex-psizzl -l pl.UTF-8
Format TeXa do artykułów fizycznych.

%package tex-pstricks
Summary:	PostScript macros for TeX
Summary(pl.UTF-8):	Makra postscriptowe dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-dvips = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-misc = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-pstricks
Obsoletes:	tetex-tex-pstricks < 1:3.1
BuildArch:	noarch

%description tex-pstricks
An extensive collection of PostScript macros that is compatible with
most TeX macro packages, including Plain TeX, LaTeX, AMS-TeX, and
AMS-LaTeX. Included are macros for color, graphics, pie charts,
rotation, trees and overlays. It has many special features, including:
a wide variety of graphics (picture drawing) macros, with a flexible
interface and with color support. There are macros for coloring or
shading the cells of tables.

%description tex-pstricks -l pl.UTF-8
Duży zestaw makr postscriptowych kompatybilny z większością pakietów
makr TeXowych, w tym: Plain TeX, LaTeX, AMS-TeX i AMS-LaTeX. Załączono
makra obsługujące kolory, grafikę, wykresy kołowe, obroty, drzewa i
nakładanie. Mają wiele możliwości, w tym dużo makr graficznych (do
rysowania obrazków) z elastycznym interfejsem i obsługą koloru. Są też
makra do kolorowania lub cieniowania komórek tabel.

%package tex-qpxqtx
Summary:	QuasiTimes and TX fonts typesetting support
Summary(pl.UTF-8):	Wsparcie dla składu fontami QuasiTimes i TX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-qpxqtx = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-qpx < 1:3.1
Obsoletes:	tetex-tex-qtx < 1:3.1
BuildArch:	noarch

%description tex-qpxqtx
QuasiTimes and TX fonts typesetting support.

%description tex-qpxqtx -l pl.UTF-8
Wsparcie dla składu fontami QuasiTimes i TX.

%package tex-huhyphen
Summary:	Hungarian hyphenation
Summary(hu.UTF-8):	Magyar elválasztás
Summary(pl.UTF-8):	Węgierskie reguły przenoszenia wyrazów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description tex-huhyphen
Hungarian hyphenation.

%description tex-huhyphen -l hu.UTF-8
Magyar elválasztás.

%description tex-huhyphen -l pl.UTF-8
Węgierskie reguły przenoszenia wyrazów.

%package tex-ruhyphen
Summary:	Russian hyphenation
Summary(pl.UTF-8):	Rosyjskie reguły przenoszenia wyrazów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-ruhyphen
Obsoletes:	tetex-tex-ruhyphen < 1:3.1
BuildArch:	noarch

%description tex-ruhyphen
A collection of Russian hyphenation patterns supporting a number of
Cyrillic font encodings, including T2, UCY (Omega Unicode Cyrillic),
LCY, LWN (OT2), and koi8-r.

%description tex-ruhyphen -l pl.UTF-8
Zestaw rosyjskich wzorców przenoszenia wyrazów obsługujący wiele
kodowań fontów w cyrylicy, włącznie z T2, UCY (Omega Unicode
Cyrillic), LCY, LWN (OT2) i koi8-r.

%package tex-spanish
Summary:	Various TeX related files for typesetting documents written in Spanish
Summary(pl.UTF-8):	Różne pliki TeXowe służące do składu dokumentów w języku hiszpańskim
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-spanish < 1:3.1
Obsoletes:	tetex-tex-spanishb < 1:3.1
BuildArch:	noarch

%description tex-spanish
Various TeX related files for typesetting documents written in
Spanish, including hyphenation and dictionaries.

%description tex-spanish -l pl.UTF-8
Różne pliki TeXowe służące do składu dokumentów napisanych w języku
hiszpańskim - w tym reguły przenoszenia wyrazów i słowniki.

%package tex-texdraw
Summary:	Graphical macros, using embedded PostScript
Summary(pl.UTF-8):	Makra graficzne używające osadzanego PostScriptu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-texdraw < 1:3.1
BuildArch:	noarch

%description tex-texdraw
Graphical macros, using embedded PostScript.

%description tex-texdraw -l pl.UTF-8
Makra graficzne używające osadzanego PostScriptu.

%package tex-thumbpdf
Summary:	Thumbnails for PDFTeX and dvips/ps2pdf
Summary(pl.UTF-8):	Ikonki dla PDFTeXa i dvips/ps2pdf
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-thumbpdf < 1:3.1
BuildArch:	noarch

%description tex-thumbpdf
Provides support, using Perl, for thumbnails in pdfTeX and
dvips/ps2pdf, using ghostscript to generate the thumbnails which get
represented in a TeX readable file that is read by the package
thumbpdf.sty to automatically include the thumbnails. Works with both
plain TeX and LaTeX.

%description tex-thumbpdf -l pl.UTF-8
Pakiet przy pomocy Perla dodaje ikonki w pdfTeXu i dvips/ps2pdf przy
użyciu ghostscripta. Ikonki są reprezentowane w pliku czytanym przez
TeXa, który jest wywoływany z thumbpdf.sty, aby automatycznie dołączyć
ikonki. Działa z formatami plain TeX i LaTeX.

%package tex-ukrhyph
Summary:	Ukranian hyphenation
Summary(pl.UTF-8):	Ukraińskie zasady przenoszenia wyrazów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-ukrhyph
Obsoletes:	tetex-tex-ukrhyph < 1:3.1
BuildArch:	noarch

%description tex-ukrhyph
This package allows the use of different hyphenation patterns for the
Ukrainian language for various Cyrillic font encodings. Contains
packages implementing traditional rules, modern rules, and combined
English-Ukrainian hyphenation.

%description tex-ukrhyph -l pl.UTF-8
Ten pakiet pozwala na używanie różnych wzorców przenoszenia wyrazów
dla języka ukraińskiego z różnymi kodowaniami fontów z cyrylicą.
Zawiera pakiety z implementacją reguł tradycyjnych, współczesnych i
łączonych angielsko-ukraińskich.

%package latex-variations
Summary:	Typeset tables of variations of functions
Summary(pl.UTF-8):	Skład tabeli wahań funkcji
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description latex-variations
Typeset tables of variations of functions.

%description latex-variations -l pl.UTF-8
Skład tabeli wahań funkcji.

%package latex-vietnam
Summary:	Vietnamese language support
Summary(pl.UTF-8):	Wsparcie dla języka wietnamskiego
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-urwvn < 1:3.1
Obsoletes:	tetex-latex-vietnam < 1:3.1
Obsoletes:	tetex-tex-vietnam < 1:3.0
BuildArch:	noarch

%description latex-vietnam
Vietnamese language support.

%description latex-vietnam -l pl.UTF-8
Wsparcie dla języka wietnamskiego.

%package tex-xypic
Summary:	Package for typesetting a variety of graphs and diagrams with TeX
Summary(pl.UTF-8):	Pakiet do składania w TeXu różnych wykresów i diagramów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-xypic = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-xypic < 1:3.1
Obsoletes:	tetex-xypic < 1:3.1
BuildArch:	noarch

%description tex-xypic
A package for typesetting a variety of graphs and diagrams with TeX.
Xy-pic works with most formats (including LaTeX, AMS-LaTeX, AMS-TeX,
and plain TeX), in particular Xy-pic is provided as a LaTeX2e
`supported package'.

%description tex-xypic -l pl.UTF-8
Pakiet do składania w TeXu różnych wykresów i diagramów. Xy-pic działa
z większością formatów (w tym LaTeX, AMS-LaTeX, AMS-TeX i plain TeX),
w szczególności jest dołączany jako "wspierany pakiet" LaTeX2e.

%package tex-xkeyval
Summary:	Extension to keyval package
Summary(pl.UTF-8):	Rozszerzenie do pakietu keyval
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-xkeyval < 1:3.1
BuildArch:	noarch

%description tex-xkeyval
Extension to keyval package.

%description tex-xkeyval -l pl.UTF-8
Rozszerzenie do pakietu keyval.

%package dirs-fonts
Summary:	TeX font directories
Summary(pl.UTF-8):	Katalogi fontów TeXa
Group:		Fonts
Provides:	tetex-dirs-fonts
Obsoletes:	tetex-dirs-fonts < 1:3.1
BuildArch:	noarch

%description dirs-fonts
TeX font directories.

%description dirs-fonts -l pl.UTF-8
Katalogi fontów TeXa.

# # Fonts packages #

%package fonts-adobe
Summary:	Adobe fonts
Summary(pl.UTF-8):	Fonty Adobe
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-adobe
Obsoletes:	tetex-fonts-adobe < 1:3.1
BuildArch:	noarch

%description fonts-adobe
Adobe fonts.

%description fonts-adobe -l pl.UTF-8
Fonty Adobe.

%package fonts-larm
Summary:	Larm (cyrillic) fonts
Summary(pl.UTF-8):	Fonty Larm (cyrylickie)
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description fonts-larm
Larm (cyrillic) fonts.

%description fonts-larm -l pl.UTF-8
Fonty Larm (cyrylickie).

%package fonts-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Summary(pl.UTF-8):	Wirtualne fonty do plików PDF z fontami CMR o kodowaniu T1
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-ae < 1:3.1
BuildArch:	noarch

%description fonts-ae
Virtual fonts for PDF-files with T1 encoded CMR-fonts.

%description fonts-ae -l pl.UTF-8
Wirtualne fonty do plików PDF z fontami CMR o kodowaniu T1.

%package fonts-ams
Summary:	AMS fonts
Summary(pl.UTF-8):	Fonty AMS
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-ams
Obsoletes:	tetex-fonts-ams < 1:3.1
BuildArch:	noarch

%description fonts-ams
AMS fonts.

%description fonts-ams -l pl.UTF-8
Fonty AMS.

%package fonts-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl.UTF-8):	Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-antp < 1:3.1
BuildArch:	noarch

%description fonts-antp
Antykwa Poltawskiego, a Type 1 family of Polish traditional type.

%description fonts-antp -l pl.UTF-8
Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako
Type 1.

%package fonts-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Summary(pl.UTF-8):	Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-antt < 1:3.1
BuildArch:	noarch

%description fonts-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%description fonts-antt -l pl.UTF-8
Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1.

%package fonts-arphic
Summary:	Arphic fonts
Summary(pl.UTF-8):	Fonty Arphic
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description fonts-arphic
Arphic fonts.

%description fonts-arphic -l pl.UTF-8
Fonty Arphic.

%package fonts-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Summary(pl.UTF-8):	Tablicowy wariant fontów Computer Modern ze wsparciem dla LaTeXa
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-bbm < 1:3.1
BuildArch:	noarch

%description fonts-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%description fonts-bbm -l pl.UTF-8
Tablicowy wariant fontów Computer Modern ze wsparciem dla LaTeXa.

%package fonts-bbold
Summary:	Sans serif blackboard bold for LaTeX
Summary(pl.UTF-8):	Tablicowy tłusty font sans serif dla LaTeXa
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-bbold < 1:3.1
BuildArch:	noarch

%description fonts-bbold
Sans serif blackboard bold for LaTeX.

%description fonts-bbold -l pl.UTF-8
Tablicowy tłusty font sans serif dla LaTeXa.

%package fonts-bitstream
Summary:	Bitstream fonts
Summary(pl.UTF-8):	Fonty Bitstream
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-bitstrea < 1:3.0-11
Obsoletes:	tetex-fonts-bitstream < 1:3.1
BuildArch:	noarch

%description fonts-bitstream
Bitstream fonts.

%description fonts-bitstream -l pl.UTF-8
Fonty Bitstream.

%package fonts-cc-pl
Summary:	Polish version of Computer Concrete fonts
Summary(pl.UTF-8):	Polska wersja fontów Computer Concrete
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-cc-pl < 1:3.1
BuildArch:	noarch

%description fonts-cc-pl
Polish version of Computer Concrete fonts.

%description fonts-cc-pl -l pl.UTF-8
Polska wersja fontów Computer Concrete.

%package fonts-cg
Summary:	Compugraphic fonts
Summary(pl.UTF-8):	Fonty Compugraphic
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-cg < 1:3.1
BuildArch:	noarch

%description fonts-cg
Compugraphic fonts.

%description fonts-cg -l pl.UTF-8
Fonty Compugraphic.

%package fonts-cm
Summary:	Computer Modern fonts
Summary(pl.UTF-8):	Fonty Computer Modern
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-cm
Obsoletes:	tetex-fonts-cm < 1:3.1
BuildArch:	noarch

%description fonts-cm
Computer Modern fonts.

%description fonts-cm -l pl.UTF-8
Fonty Computer Modern.

%package fonts-cmbright
Summary:	CM Bright fonts
Summary(pl.UTF-8):	Fonty CM Bright
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-cmbright < 1:3.1
BuildArch:	noarch

%description fonts-cmbright
CM Bright fonts.

%description fonts-cmbright -l pl.UTF-8
Fonty CM Bright.

%package fonts-cmsuper
Summary:	CM Super fonts
Summary(hu.UTF-8):	CM Super betűtípus
Summary(pl.UTF-8):	Fonty CM Super
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description fonts-cmsuper
CM Super fonts.

%description fonts-cmsuper -l hu.UTF-8
CM Super betűtípus.

%description fonts-cmsuper -l pl.UTF-8
Fonty CM Super.

%package fonts-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Summary(pl.UTF-8):	Fonty Computer Modern rozszerzone o litery rosyjskie
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-cmcyr
Obsoletes:	tetex-fonts-cmcyr < 1:3.1
Obsoletes:	texlive-fonts-type1-cmcyr < 1:20080816-6
BuildArch:	noarch

%description fonts-cmcyr
Computer Modern fonts extended with Russian letters.

%description fonts-cmcyr -l pl.UTF-8
Fonty Computer Modern rozszerzone o litery rosyjskie.

%package fonts-cmextra
Summary:	Extra Computer Modern fonts, from the American Mathematical Society
Summary(pl.UTF-8):	Dodatkowe fonty Computer Modern z AMS
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-cmextra
Obsoletes:	tetex-fonts-cmextra < 1:3.1
BuildArch:	noarch

%description fonts-cmextra
Extra Computer Modern fonts, from the American Mathematical Society.

%description fonts-cmextra -l pl.UTF-8
Dodatkowe fonty Computer Modern z AMS (American Mathematical Society).

%package fonts-concmath
Summary:	Concrete Math fonts
Summary(pl.UTF-8):	Fonty matematyczne Concrete Math
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-concmath < 1:3.1
BuildArch:	noarch

%description fonts-concmath
Concrete Math fonts.

%description fonts-concmath -l pl.UTF-8
Fonty matematyczne Concrete Math.

%package fonts-concrete
Summary:	Concrete Roman fonts
Summary(pl.UTF-8):	Fonty Concrete Roman
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-concrete < 1:3.1
BuildArch:	noarch

%description fonts-concrete
Concrete Roman fonts, designed by Donald E. Knuth, originally for use
with Euler math fonts.

%description fonts-concrete -l pl.UTF-8
Fonty Concrete Roman, opracowane przez Donalda E. Knutha, oryginalnie
przeznaczone do używania z fontami matematycznymi Euler.

%package fonts-cs
Summary:	Czech/Slovak-tuned MetaFont Computer Modern fonts
Summary(pl.UTF-8):	Fonty MetaFont Computer Modern dla języków czeskiego i słowackiego
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-cs < 1:3.1
BuildArch:	noarch

%description fonts-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%description fonts-cs -l pl.UTF-8
Fonty MetaFont Computer Modern zmodyfikowane pod kątem języków
czeskiego i słowackiego.

%package fonts-ecc
Summary:	Sources for the European Concrete fonts
Summary(pl.UTF-8):	Źródła dla fontów European Concrete
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-ecc < 1:3.1
BuildArch:	noarch

%description fonts-ecc
The MetaFont sources and tfm files of the European Concrete Fonts.
This is the EC implementation of Knuth's Concrete fonts, including
also the corresponding text companion fonts.

%description fonts-ecc -l pl.UTF-8
Źródła MetaFonta i pliki tfm dla fontów European Concrete. Jest to
implementacja EC fontów Concrete Knutha, włącznie z odpowiadającymi
tekstowymi fontami towarzyszącymi.

%package fonts-eurosym
Summary:	The new European currency symbol for the Euro
Summary(pl.UTF-8):	Symbol nowej europejskiej waluty Euro
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-eurosym < 1:3.1
BuildArch:	noarch

%description fonts-eurosym
The new European currency symbol for the Euro implemented in Metafont,
using the official European Commission dimensions, and providing
several shapes (normal, slanted, bold, outline).

%description fonts-eurosym -l pl.UTF-8
Symbol nowej europejskiej waluty Euro, zaimplementowany w Metafoncie,
z użyciem oficjalnych wymiarów wg Komisji Europejskiej, dostarczający
różnych kształtów (normalnego, pochylonego, tłustego, szkicowanego).

%package fonts-eulervm
Summary:	The Virtual Euler Math fonts
Summary(pl.UTF-8):	Fonty Virtual Euler Math
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-eulervm < 1:3.1
BuildArch:	noarch

%description fonts-eulervm
Euler-VM is a set of _virtual_ math fonts based on Euler and CM. This
approach has several advantages over immediately using the _real_
Euler fonts: Most noticeably, less TeX resources are consumed, the
quality of various math symbols is improved, and a usable \hslash
symbol can be provided.

%description fonts-eulervm -l pl.UTF-8
Euler-VM to zbiór _wirtualnych_ fontów matematycznych opartych na
fontach Euler i CM. Podejście to ma różne zalety nad bezpośrednim
używaniem _prawdziwych_ fontów Euler: najbardziej zauważalnie, używane
jest mniej zasobów TeXa, poprawiona jest jakość różnych symboli
matematycznych i może być dostępny używalny symbol \hslash.

%package fonts-euxm
Summary:	Fonts similar to EUSM but with two more characters
Summary(pl.UTF-8):	Fonty podobne do EUSM, ale z dwoma dodatkowymi znakami
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-euxm < 1:3.1
BuildArch:	noarch

%description fonts-euxm
Fonts like EUSM but with two more characters needed for Concrete Math
included in TeXLive distribution in fonts3.

%description fonts-euxm -l pl.UTF-8
Fonty podobne do EUSM, ale z dwoma dodatkowymi znakami, potrzebnymi
dla Concrete Math dołączonego w fonts3 dystrybucji TeXLive.

%package fonts-gothic
Summary:	Gothic and ornamental initial fonts by Yannis Haralambous
Summary(pl.UTF-8):	Początkowe fonty gotyckie i ornamentowe Yannisa Haralambousa
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-gothic < 1:3.1
BuildArch:	noarch

%description fonts-gothic
Gothic and ornamental initial fonts by Yannis Haralambous.

%description fonts-gothic -l pl.UTF-8
Początkowe fonty gotyckie i ornamentowe Yannisa Haralambousa.

%package fonts-hoekwater
Summary:	Converted mflogo font
Summary(pl.UTF-8):	Przekonwertowany font mflogo
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-hoekwater < 1:3.1
BuildArch:	noarch

%description fonts-hoekwater
Fonts originally created in MetaFont, transformed to PostScript by
Taco Hoekwater; includes logo, manfnt, rsfs, stmaryrd, wasy, wasy2,
xipa.

%description fonts-hoekwater -l pl.UTF-8
Fonty oryginalnie stworzone w MetaFoncie, przekształcone do
PostScriptu przez Taco Hoekwatera; zawierają: logo, manfnt, rsfs,
stmaryrd, wasy, wasy2, xipa.

%package fonts-jknappen
Summary:	Miscellaneous packages by Joerg Knappen
Summary(pl.UTF-8):	Różne pakiety autorstwa Joerga Knappena
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-jknappen
Obsoletes:	tetex-fonts-jknappen < 1:3.1
Obsoletes:	tetex-latex-jknappen < 1:3.1
Obsoletes:	texlive-latex-jknappen < 1:20080816-6
BuildArch:	noarch

%description fonts-jknappen
Miscellaneous macros, mostly for making use of extra fonts, by Joerg
Knappen, including sgmlcmpt.

%description fonts-jknappen -l pl.UTF-8
Różne makra, głównie do używania dodatkowych fontów autorstwa Joerga
Knappena. Zawiera sgmlcmpt.

%package fonts-kpfonts
Summary:	A complete set of fonts for text and mathematics
Summary(hu.UTF-8):	Betűtípusok teljes készlete (matematikai) szövegekhez
Summary(pl.UTF-8):	Kompletny zbiór fontów do tekstu i matematyki
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description fonts-kpfonts
A complete set of fonts for text and mathematics.

%description fonts-kpfonts -l hu.UTF-8
Betűtípusok teljes készlete (matematikai) szövegekhez.

%description fonts-kpfonts -l pl.UTF-8
Kompletny zbiór fontów do tekstu i matematyki.

%package fonts-latex
Summary:	Basic LaTeX fonts
Summary(pl.UTF-8):	Podstawowe fonty dla LaTeXa
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-latex
Obsoletes:	tetex-fonts-latex < 1:3.1
BuildArch:	noarch

%description fonts-latex
Basic LaTeX fonts.

%description fonts-latex -l pl.UTF-8
Podstawowe fonty dla LaTeXa.

%package fonts-lh
Summary:	Olga Lapko's LH fonts
Summary(pl.UTF-8):	Fonty LH Olgi Lapko
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-lh < 1:3.1
BuildArch:	noarch

%description fonts-lh
The lh fonts for the `T2'/X2 encodings (for cyrillic languages).

%description fonts-lh -l pl.UTF-8
Fonty lh dla kodowań `T2'/X2 (dla języków zapisywanych cyrylicą).

%package fonts-lm
Summary:	Latin Modern family fonts
Summary(pl.UTF-8):	Fonty z rodziny Latin Modern
Group:		Applications/Publishing/TeX
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-lm < 1:3.1
Obsoletes:	texlive-fonts-type1-lm < 1:20080816-6
BuildArch:	noarch

%description fonts-lm
Latin Modern family of fonts, based on the Computer Modern fonts
released into public domain by AMS (copyright (C) 1997 AMS). Contain a
lot of additional characters, mainly accented ones, but not only.
There is a one set of PostScript fonts and four sets of TeX Font
Metric files, corresponding to: Cork encoding (cork-*.tfm); QX
encoding (qx-*.tfm); TeX'n'ANSI aka LY1 encoding (texnansi-*.tfm); and
Text Companion for EC fonts aka TS1 (ts1-*.tfm). It is presumed that a
potential user knows what to do with all these files. The author is
Boguslaw Jackowski.

%description fonts-lm -l pl.UTF-8
Rodzina fontów Latin Modern, oparta na fontach Computer Modern
przekazanych do domeny publicznej przez AMS (copyright (C) 1997 AMS).
Zawiera wiele dodatkowych znaków, głównie z akcentami, ale nie tylko.
Jest jeden zbiór fontów postscriptowych oraz cztery zbiory plików TeX
Font Metric, odpowiadających: kodowaniu Cork (cork-*.tfm); kodowaniu
QX (qx-*.tfm); kodowaniu TeX'n'ANSI zwanemu także LY1
(texnansi-*.tfm); oraz Text Companion dla fontów EC zwanemu także TS1
(ts1-*.tfm). Zakłada się, że potencjalny użytkownik wie, co zrobić z
tymi wszystkimi plikami. Autorem jest Bogusław Jackowski.

%package fonts-marvosym
Summary:	Martin Vogel's Symbol (marvosym) font
Summary(pl.UTF-8):	Font Symbol Martina Vogela (marvosym)
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-marvosym < 1:3.1
BuildArch:	noarch

%description fonts-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols for
structural engineering; Symbols for steel cross-sections; Astronomy
signs (Sun, Moon, planets); The 12 signs of the zodiac; Scissor
symbols; CE sign and others.

%description fonts-marvosym -l pl.UTF-8
Font Symbol Martina Vogela (marvosym) to font zawierający: symbol
waluty Euro zdefiniowany przez Komisję Europejską; symbole waluty Euro
dla krojów Times, Helvetica i Courier; symbole dla inżynierii
strukturalnej; symbole dla przekroi poprzecznych; symbole
astronomiczne (Słońce, Księżyc, planety); 12 znaków Zodiaku; symbole
krawieckie; znak CE i inne.

%package fonts-mflogo
Summary:	Logo fonts
Summary(pl.UTF-8):	Fonty logo
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-mflogo < 1:3.1
BuildArch:	noarch

%description fonts-mflogo
Logo fonts.

%description fonts-mflogo -l pl.UTF-8
Fonty logo.

%package fonts-misc
Summary:	Miscellaneous fonts
Summary(pl.UTF-8):	Różne fonty
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-misc < 1:3.1
BuildArch:	noarch

%description fonts-misc
Miscellaneous fonts.

%description fonts-misc -l pl.UTF-8
Fonty różne.

%package fonts-monotype
Summary:	Monotype fonts
Summary(pl.UTF-8):	Fonty Monotype
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-monotype < 1:3.1
BuildArch:	noarch

%description fonts-monotype
Monotype fonts.

%description fonts-monotype -l pl.UTF-8
Fonty Monotype.

%package fonts-omega
Summary:	Fonts for Omega - extended unicode TeX
Summary(pl.UTF-8):	Fonty dla Omegi - TeXa ze wsparciem dla unikodu
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-omega < 1:3.1
BuildArch:	noarch

%description fonts-omega
Fonts for Omega - extended unicode TeX.

%description fonts-omega -l pl.UTF-8
Fonty dla Omegi - TeXa ze wsparciem dla unikodu.

%package fonts-other
Summary:	Other fonts
Summary(hu.UTF-8):	További betűtípusok
Summary(pl.UTF-8):	Fonty inne
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-cbgreek < 1:3.1
Obsoletes:	tetex-fonts-dstroke < 1:3.1
Obsoletes:	tetex-fonts-pazo < 1:3.1
Obsoletes:	tetex-fonts-qfonts < 1:3.1
Obsoletes:	tetex-fonts-type1-dstroke < 1:3.1
Obsoletes:	tetex-fonts-type1-qfonts < 1:3.1
Obsoletes:	tetex-fonts-type1-tt2001 < 1:3.1
BuildArch:	noarch

%description fonts-other
Other fonts.

%description fonts-other -l hu.UTF-8
További betűtípusok.

%description fonts-other -l pl.UTF-8
Fonty inne.

%package fonts-pl
Summary:	Polish fonts
Summary(pl.UTF-8):	Polskie fonty
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-pl < 1:3.1
BuildArch:	noarch

%description fonts-pl
Polish fonts.

%description fonts-pl -l pl.UTF-8
Polskie fonty.

%package fonts-px
Summary:	PX fonts
Summary(pl.UTF-8):	Fonty PX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-px < 1:3.1
BuildArch:	noarch

%description fonts-px
PX fonts.

%description fonts-px -l pl.UTF-8
Fonty PX.

%package fonts-qpxqtx
Summary:	Additional fonts for QTX package
Summary(pl.UTF-8):	Dodatkowe fonty dla pakietu QTX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
# I hope qpxqtx doesn't need qfonts
# Requires:	%{name}-fonts-qfonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-tx = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-qpx < 1:3.1
Obsoletes:	tetex-fonts-qtx < 1:3.1
BuildArch:	noarch

%description fonts-qpxqtx
Additional fonts for QTX package.

%description fonts-qpxqtx -l pl.UTF-8
Dodatkowe fonty dla pakietu QTX.

%package fonts-rsfs
Summary:	Fonts of uppercase script letters for scientific and mathematical typesetting
Summary(pl.UTF-8):	Fonty wielkich liter pisanych do składania dokumentów naukowych i matematycznych
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-rsfs < 1:3.1
BuildArch:	noarch

%description fonts-rsfs
Fonts of uppercase script letters for use as symbols in scientific and
mathematical typesetting, in contrast to the informal script fonts
such as that used for the `calligraphic' symbols in the TeX math
symbol font.

%description fonts-rsfs -l pl.UTF-8
Fonty wielkich liter pisanych do używania jako symbole przy składaniu
dokumentów naukowych i matematycznych, w odróżnieniu od nieformalnych
fontów pisanych takich jak używane do symboli "kaligraficznych" w
matematycznym foncie TeXowym symbol.

%package fonts-stmaryrd
Summary:	St Mary Road symbols for functional programming
Summary(pl.UTF-8):	Symbole St Mary Road do programowania funkcyjnego
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-stmaryrd
Obsoletes:	tetex-fonts-stmaryrd < 1:3.1
BuildArch:	noarch

%description fonts-stmaryrd
St Mary Road symbols for functional programming.

%description fonts-stmaryrd -l pl.UTF-8
Symbole St Mary Road do programowania funkcyjnego.

%package fonts-tx
Summary:	TX fonts
Summary(pl.UTF-8):	Fonty TX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-tx < 1:3.1
BuildArch:	noarch

%description fonts-tx
TX fonts.

%description fonts-tx -l pl.UTF-8
Fonty TX.

%package fonts-uhc
Summary:	UHC fonts
Summary(pl.UTF-8):	Fonty UHC
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description fonts-uhc
UHC fonts.

%description fonts-uhc -l pl.UTF-8
Fonty UHC.

%package fonts-urw
Summary:	URW fonts
Summary(pl.UTF-8):	Fonty URW
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-urw < 1:3.1
BuildArch:	noarch

%description fonts-urw
URW fonts.

%description fonts-urw -l pl.UTF-8
Fonty URW.

%package fonts-urwvn
Summary:	URWVN fonts
Summary(pl.UTF-8):	Fonty URWVN
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-urwvn < 1:3.1
BuildArch:	noarch

%description fonts-urwvn
URWVN fonts.

%description fonts-urwvn -l pl.UTF-8
Fonty URWVN.

%package fonts-vnr
Summary:	VNR fonts
Summary(pl.UTF-8):	Fonty VNR
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-vnr < 1:3.1
BuildArch:	noarch

%description fonts-vnr
VNR fonts.

%description fonts-vnr -l pl.UTF-8
Fonty VNR.

%package fonts-urw35vf
Summary:	urw35vf fonts
Summary(hu.UTF-8):	urw35vf betűtípus
Summary(pl.UTF-8):	Fonty urw35vf
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description fonts-urw35vf
urw35vf fonts.

%description fonts-urw35vf -l hu.UTF-8
urw35vf betűtípus.

%description fonts-urw35vf -l pl.UTF-8
Fonty urw35vf.

%package fonts-wadalab
Summary:	Wadalab fonts
Summary(pl.UTF-8):	Fonty Wadalab
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description fonts-wadalab
Wadalab fonts.

%description fonts-wadalab -l pl.UTF-8
Fonty Wadalab.

%package fonts-wasy
Summary:	Waldis symbol fonts
Summary(pl.UTF-8):	Fonty Waldis symbol
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-wasy
Obsoletes:	tetex-fonts-wasy < 1:3.1
BuildArch:	noarch

%description fonts-wasy
Waldis symbol fonts.

%description fonts-wasy -l pl.UTF-8
Fonty Waldis symbol.

%package fonts-xypic
Summary:	Xy-pic fonts
Summary(pl.UTF-8):	Fonty Xy-pic
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-xypic < 1:3.1
BuildArch:	noarch

%description fonts-xypic
Xy-pic fonts.

%description fonts-xypic -l pl.UTF-8
Fonty Xy-pic.

%package fonts-yandy
Summary:	European Modern fonts from Y&Y
Summary(pl.UTF-8):	Fonty European Modern od Y&Y
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-yandy < 1:3.1
BuildArch:	noarch

%description fonts-yandy
European Modern fonts from Y&Y.

%description fonts-yandy -l pl.UTF-8
Fonty European Modern od Y&Y.

%package fonts-type1-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl.UTF-8):	Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-antp < 1:3.1
BuildArch:	noarch

%description fonts-type1-antp
Antykwa Poltawskiego, a Type 1 family of Polish traditional type.

%description fonts-type1-antp -l pl.UTF-8
Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako
Type 1.

%package fonts-type1-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Summary(pl.UTF-8):	Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-antt < 1:3.1
BuildArch:	noarch

%description fonts-type1-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%description fonts-type1-antt -l pl.UTF-8
Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1.

%package fonts-type1-arphic
Summary:	Type1 Arphic fonts
Summary(pl.UTF-8):	Fonty Type1 Arphic
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description fonts-type1-arphic
Type1 Arphic fonts.

%description fonts-type1-arphic -l pl.UTF-8
Fonty Type1 Arphic.

%package fonts-type1-belleek
Summary:	Free replacement for basic MathTime fonts
Summary(pl.UTF-8):	Wolnodostępny zamiennik podstawowych fontów MathTime
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-belleek < 1:3.1
BuildArch:	noarch

%description fonts-type1-belleek
Free replacement for basic MathTime fonts.

%description fonts-type1-belleek -l pl.UTF-8
Wolnodostępny zamiennik podstawowych fontów MathTime.

%package fonts-type1-bitstream
Summary:	Bitstream fonts
Summary(pl.UTF-8):	Fonty Bitstream
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-bitstrea < 1:3.0-11
Obsoletes:	tetex-fonts-type1-bitstream < 1:3.1
BuildArch:	noarch

%description fonts-type1-bitstream
Bitstream fonts.

%description fonts-type1-bitstream -l pl.UTF-8
Fonty Bitstream.

%package fonts-type1-bluesky
Summary:	Computer Modern family fonts
Summary(pl.UTF-8):	Fonty z rodziny Computer Modern
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-type1-bluesky
Obsoletes:	tetex-fonts-type1-bluesky < 1:3.1
BuildArch:	noarch

%description fonts-type1-bluesky
Computer Modern family fonts.

%description fonts-type1-bluesky -l pl.UTF-8
Fonty z rodzony Computer Modern.

%package fonts-type1-cc-pl
Summary:	Polish version of Computer Concrete fonts
Summary(pl.UTF-8):	Polska wersja fontów Computer Concrete
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-cc-pl < 1:3.1
BuildArch:	noarch

%description fonts-type1-cc-pl
Polish version of Computer Concrete fonts.

%description fonts-type1-cc-pl -l pl.UTF-8
Polska wersja fontów Computer Concrete.

%package fonts-type1-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Summary(pl.UTF-8):	Fonty Computer Modern rozszerzone o litery rosyjskie
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-cmcyr < 1:3.1

%description fonts-type1-cmcyr
Computer Modern fonts extended with Russian letters.

%description fonts-type1-cmcyr -l pl.UTF-8
Fonty Computer Modern rozszerzone o litery rosyjskie.

%package fonts-type1-cs
Summary:	Czech/Slovak-tuned MetaFont Computer Modern fonts
Summary(pl.UTF-8):	Fonty MetaFont Computer Modern dla języków czeskiego i słowackiego
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-cs < 1:3.1
BuildArch:	noarch

%description fonts-type1-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%description fonts-type1-cs -l pl.UTF-8
Fonty MetaFont Computer Modern zmodyfikowane pod kątem języków
czeskiego i słowackiego.

%package fonts-type1-eurosym
Summary:	The new European currency symbol for the Euro
Summary(pl.UTF-8):	Symbol nowej europejskiej waluty Euro
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-eurosym < 1:3.1
BuildArch:	noarch

%description fonts-type1-eurosym
The new European currency symbol for the Euro implemented in Metafont,
using the official European Commission dimensions, and providing
several shapes (normal, slanted, bold, outline).

%description fonts-type1-eurosym -l pl.UTF-8
Symbol nowej europejskiej waluty Euro, zaimplementowany w Metafoncie,
z użyciem oficjalnych wymiarów wg Komisji Europejskiej, dostarczający
różnych kształtów (normalnego, pochylonego, tłustego, szkicowanego).

%package fonts-type1-fpl
Summary:	SC/OsF fonts for URW Palladio L
Summary(pl.UTF-8):	Fonty SC/OsF dla URW Palladio L
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-fpl < 1:3.1
BuildArch:	noarch

%description fonts-type1-fpl
The FPL Fonts provide a set of SC/OsF fonts for URW Palladio L which
are compatible with respect to metrics with the Palatino SC/OsF fonts
from Adobe. Note that it is not the author's aim to exactly reproduce
the outlines of the original Adobe fonts. The SC and OsF in the FPL
Fonts were designed with the glyphs from URW Palladio L as starting
point. For some glyphs (eg 'o') the author got the best result by
scaling and boldening. For others (eg 'h') shifting selected portions
of the character gave more satisfying results. All this was done using
the free font editor FontForge <http://fontforge.sf.net/>. The kerning
data in these fonts comes from Walter Schmidt's improved Palatino
metrics.

%description fonts-type1-fpl -l pl.UTF-8
Fonty FPL dostarczają zbiór fontów SC/OsF dla URW Palladio L, które są
kompatybilne co do metryk z fontami Palatino SC/OsF firmy Adobe.
Należy jednak zaznaczyć, że celem autora nie jest dokładne odtworzenie
kształtów oryginalnych fontów Adobe. SC i OsF w fontach FPL były
projektowane w oparciu o glify z URW Palladio L. Dla niektórych glifów
(np. 'o') autor uzyskał najlepszy wynik poprzez skalowanie i
pogrubianie. Dla innych (np. 'h') przesuwanie wybranych części znaku
dało lepsze wyniki. Wszystko to zostało zrobione przy użyciu
wolnodostępnego edytora fontów FontForge <http://fontforge.sf.net/>.
Dane dla kerningu w tych fontach pochodzą z ulepszonych metryk
Palatino Waltera Schmidta.

%package fonts-type1-hoekwater
Summary:	Converted mflogo font
Summary(pl.UTF-8):	Przekonwertowany font mflogo
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-hoekwater < 1:3.1
BuildArch:	noarch

%description fonts-type1-hoekwater
Fonts originally created in MetaFont, transformed to PostScript by
Taco Hoekwater; includes logo, manfnt, rsfs, stmaryrd, wasy, wasy2,
xipa.

%description fonts-type1-hoekwater -l pl.UTF-8
Fonty oryginalnie stworzone w MetaFoncie, przekształcone do
PostScriptu przez Taco Hoekwatera; zawierają: logo, manfnt, rsfs,
stmaryrd, wasy, wasy2, xipa.

%package fonts-type1-lm
Summary:	Type1 Latin Modern family fonts
Summary(pl.UTF-8):	Fonty Type1 z rodziny Latin Modern
Group:		Applications/Publishing/TeX
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-lm < 1:3.1

%description fonts-type1-lm
Latin Modern family of fonts, based on the Computer Modern fonts
released into public domain by AMS (copyright (C) 1997 AMS). Contain a
lot of additional characters, mainly accented ones, but not only.
There is a one set of PostScript fonts and four sets of TeX Font
Metric files, corresponding to: Cork encoding (cork-*.tfm); QX
encoding (qx-*.tfm); TeX'n'ANSI aka LY1 encoding (texnansi-*.tfm); and
Text Companion for EC fonts aka TS1 (ts1-*.tfm). It is presumed that a
potential user knows what to do with all these files. The author is
Boguslaw Jackowski.

%description fonts-type1-lm -l pl.UTF-8
Rodzina fontów Latin Modern, oparta na fontach Computer Modern
przekazanych do domeny publicznej przez AMS (copyright (C) 1997 AMS).
Zawiera wiele dodatkowych znaków, głównie z akcentami, ale nie tylko.
Jest jeden zbiór fontów postscriptowych oraz cztery zbiory plików TeX
Font Metric, odpowiadających: kodowaniu Cork (cork-*.tfm); kodowaniu
QX (qx-*.tfm); kodowaniu TeX'n'ANSI zwanemu także LY1
(texnansi-*.tfm); oraz Text Companion dla fontów EC zwanemu także TS1
(ts1-*.tfm). Zakłada się, że potencjalny użytkownik wie, co zrobić z
tymi wszystkimi plikami. Autorem jest Bogusław Jackowski.

%package fonts-type1-marvosym
Summary:	Martin Vogel's Symbol (marvosym) font
Summary(pl.UTF-8):	Font Symbol Martina Vogela (marvosym)
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-marvosym < 1:3.1
BuildArch:	noarch

%description fonts-type1-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols for
structural engineering; Symbols for steel cross-sections; Astronomy
signs (Sun, Moon, planets); The 12 signs of the zodiac; Scissor
symbols; CE sign and others.

%description fonts-type1-marvosym -l pl.UTF-8
Font Symbol Martina Vogela (marvosym) to font zawierający: symbol
waluty Euro zdefiniowany przez Komisję Europejską; symbole waluty Euro
dla krojów Times, Helvetica i Courier; symbole dla inżynierii
strukturalnej; symbole dla przekroi poprzecznych; symbole
astronomiczne (Słońce, Księżyc, planety); 12 znaków Zodiaku; symbole
krawieckie; znak CE i inne.

%package fonts-type1-mathpazo
Summary:	Pazo Math fonts
Summary(pl.UTF-8):	Fonty matematyczne Pazo Math
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-mathpazo < 1:3.1
BuildArch:	noarch

%description fonts-type1-mathpazo
Pazo Math fonts.

%description fonts-type1-mathpazo -l pl.UTF-8
Fonty matematyczne Pazo Math.

%package fonts-type1-omega
Summary:	Type1 fonts for Omega - extended unicode TeX
Summary(pl.UTF-8):	Fonty Type1 dla Omegi - TeXa ze wsparciem dla unikodu
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-omega < 1:3.1
BuildArch:	noarch

%description fonts-type1-omega
Type1 fonts for Omega - extended unicode TeX.

%description fonts-type1-omega -l pl.UTF-8
Fonty Type1 dla Omegi - TeXa ze wsparciem dla unikodu.

%package fonts-type1-pl
Summary:	Polish fonts
Summary(pl.UTF-8):	Polskie fonty
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-type1-bluesky = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-pl < 1:3.1
BuildArch:	noarch

%description fonts-type1-pl
Polish fonts.

%description fonts-type1-pl -l pl.UTF-8
Polskie fonty.

%package fonts-type1-px
Summary:	PX Type1 fonts
Summary(pl.UTF-8):	Fonty Type1 PX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-px < 1:3.1
BuildArch:	noarch

%description fonts-type1-px
PX Type1 fonts.

%description fonts-type1-px -l pl.UTF-8
Fonty Type1 PX.

%package fonts-type1-tx
Summary:	TX Type1 fonts
Summary(pl.UTF-8):	Fonty Type1 TX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-tx < 1:3.1
BuildArch:	noarch

%description fonts-type1-tx
TX Type1 fonts.

%description fonts-type1-tx -l pl.UTF-8
Fonty Type1 TX.

%package fonts-type1-uhc
Summary:	Type1 UHC fonts
Summary(pl.UTF-8):	Fonty Type1 UHC
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description fonts-type1-uhc
Type1 UHC fonts.

%description fonts-type1-uhc -l pl.UTF-8
Fonty Type1 UHC.

%package fonts-type1-urw
Summary:	URW fonts
Summary(pl.UTF-8):	Fonty URW
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-type1-urw
Obsoletes:	tetex-fonts-type1-urw < 1:3.1
BuildArch:	noarch

%description fonts-type1-urw
URW fonts.

%description fonts-type1-urw -l pl.UTF-8
Fonty URW.

%package fonts-type1-vnr
Summary:	Type1 VNR fonts
Summary(pl.UTF-8):	Fonty Type1 VNR
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-vnr < 1:3.1
BuildArch:	noarch

%description fonts-type1-vnr
Type1 VNR fonts.

%description fonts-type1-vnr -l pl.UTF-8
Fonty Type1 VNR.

%package fonts-type1-wadalab
Summary:	Type1 Wadalab fonts
Summary(pl.UTF-8):	Fonty Type1 Wadalab
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description fonts-type1-wadalab
Type1 Wadalab fonts.

%description fonts-type1-wadalab -l pl.UTF-8
Fonty Type1 Wadalab.

%package fonts-type1-xypic
Summary:	Xy-pic fonts
Summary(pl.UTF-8):	Fonty Xy-pic
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-xypic < 1:3.1
BuildArch:	noarch

%description fonts-type1-xypic
Xy-pic fonts.

%description fonts-type1-xypic -l pl.UTF-8
Fonty Xy-pic.

# TeXLive-specific packages - there wasn't before...
%package afm2pl
Summary:	Convert an Adobe font metric file to a TeX font property list
Summary(pl.UTF-8):	Konwersja plików metryk fontów Adobe na listę własności fontów TeXa
Group:		Fonts

%description afm2pl
Convert an Adobe font metric file to a TeX font property list.

%description afm2pl -l pl.UTF-8
Konwersja plików metryk fontów Adobe na listę własności fontów TeXa.

%package bbox
Summary:	Printing the bounding box of images
Summary(pl.UTF-8):	Wypisywanie pola ograniczającego obrazy
Group:		Applications/Publishing/TeX

%description bbox
bbox reads a rawppm or rawpbm file and prints out the bounding box of
the image.

%description bbox -l pl.UTF-8
bbox czyta plik rawppm lub rawpbm i wypisuje pole ograniczające obraz.

%package cefutils
Summary:	CEF-compatible utils
Summary(pl.UTF-8):	Narzędzia zgodne z CEF
Group:		Applications/Publishing/TeX

%description cefutils
In cefutils there are CEF-compatible (Chinese Encoding Framework)
utils.

%description cefutils -l pl.UTF-8
Pakiet cefutils zawiera narzędzia zgodne z CEF (Chinese Encoding
Framework - szkieletem kodowania chińskiego).

%package detex
Summary:	A filter to strip TeX commands from a .tex file
Summary(hu.UTF-8):	Egy szűrő, amely .tex fájlokból szűri ki a TeX parancsokat
Summary(pl.UTF-8):	Filtr do usuwania poleceń TeXa z pliku .tex
Group:		Applications/Publishing/TeX

%description detex
A filter to strip TeX commands from a .tex file.

%description detex -l hu.UTF-8
Egy szűrő, amely .tex fájlokból szűri ki a TeX parancsokat.

%description detex -l pl.UTF-8
Filtr do usuwania poleceń TeXa z pliku .tex.

%package dviutils
Summary:	Various DVI utils
Summary(hu.UTF-8):	Vegyes DVI eszközök
Summary(pl.UTF-8):	Różne narzędzia DVI
Group:		Applications/Publishing/TeX
Provides:	dvi2tty
Obsoletes:	dvi2tty < 5.4

%description dviutils
This package contains various DVI utils.

%description dviutils -l hu.UTF-8
Ez a csomag mindenféle DVI eszközt tartalmaz.

%description dviutils -l pl.UTF-8
Ten pakiet zawiera różne narzędzia DVI.

%package uncategorized-utils
Summary:	Uncategorized utils
Summary(pl.UTF-8):	Narzędzia nieskategoryzowane
Group:		Applications/Publishing/TeX

%description uncategorized-utils
Uncategorized utilities. Needs check and categorizing.

%description uncategorized-utils -l pl.UTF-8
Narzędzia nieskategoryzowane. Wymagają sprawdzenia i pogrupowania.

%package tex4ht
Summary:	LaTeX and TeX for hypertext
Summary(pl.UTF-8):	LaTeX i TeX do hipertekstu
Group:		Applications/Publishing/TeX

%description tex4ht
A converter from TeX and LaTeX to hypertext (HTML, XML, etc.),
providing a configurable (La)TeX-based authoring system for hypertext.
When converting to XML, you can use MathML instead of images for
equation representation.

%description tex4ht -l pl.UTF-8
Konwerter z TeXa i LaTeXa do hipertekstu (HTML-a, XML-a itp.),
dostarczający konfigurowalny system tworzenia hipertekstu oparty na
(La)TeXu. Przy konwersji do XML-a można używać MathML-a zamiast
grafiki do reprezentacji równań.

%package xetex
Summary:	Extended TeX / LaTeX version for unicode
Summary(pl.UTF-8):	Rozszerzona wersja TeXa/LaTeXa dla unikodu
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-misc = %{epoch}:%{version}-%{release}

%description xetex
XeTeX extends the TeX typesetting system (and macro packages such as
LaTeX and ConTeXt) to have native support for the Unicode character
set, including complex Asian scripts, and for OpenType and TrueType
fonts.

%description xetex -l pl.UTF-8
XeTeX rozszerza system składu TeX (oraz pakiety makr, takie jak
LaTeX czy ConTeXt), aby miał natywną obsługę zestawu znaków Unicode,
w tym pism azjatycjich oraz fontów OpenType i TrueType.

%package xmltex
Summary:	TeX package for processing XML files
Summary(pl.UTF-8):	Pakiet TeXa do przetwarzania plików XML
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Provides:	passivetex = 1.26
Provides:	xmltex
Obsoletes:	passivetex < 1.26
Obsoletes:	xmltex < 20020626
BuildArch:	noarch

%description xmltex
XMLTeX is a non-validating, namespace-aware XML parser written in TeX.
It allows TeX to directly process XML files.

%description xmltex -l pl.UTF-8
XMLTeX to nie sprawdzający poprawności, obsługujący przestrzenie nazw
parser XML, napisany w TeXu. Pozwala na przetwarzanie plików XML
bezpośrednio z TeXa.

%package luatex
Summary:	Extended version of pdfTeX using Lua as an embedded scripting language
Summary(pl.UTF-8):	Rozszerzona wersja pdfTeXa wykorzystująca Lua jako wbudowany język skryptowy
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description luatex
LuaTeX is an extended version of pdfTeX using Lua as an embedded
scripting language.

%description luatex -l pl.UTF-8
LuaTeX to rozszerzona wersja pdfTeXa, wykorzystująca Lua jako
wbudowany język skryptowy.

%prep
%setup -q -c -T -n %{name}-%{version}-source
lzma -dc %{SOURCE0} | tar xf - -C ..
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p1
%patch8 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1

CURDIR=$(pwd)
cd utils/xindy/make-rules/alphabets
tar xvf %{SOURCE11}
cp $(find fonts -type f) .
for i in larm?00.tfm; do ln -s $i $(echo $i | sed "s@larm\(.\).*@larm0\100.tfm@") ; done
cd ${CURDIR}

%build
find . -name "config.sub" -exec cp /usr/share/automake/config.sub '{}' ';'
%{__sed} -i 's@"extend/\(.*\)"@<\1>@' texk/ttf2pk/*.c
%{__sed} -e 's@^TEXMFMAIN =.*@TEXMFMAIN = %{texmf}@' \
	-e 's@^TEXMFDIST =.*@TEXMFDIST = %{texmfdist}@' \
	-e 's@^TEXMFLOCAL =.*@TEXMFLOCAL = %{texmf}@' \
	-e 's@^TEXMFSYSVAR =.*@TEXMFSYSVAR = %{_localstatedir}@' \
	-e 's@^TEXMFSYSCONFIG =.*@TEXMFSYSCONFIG = %{_sysconfdir}/%{name}@' \
	-e 's@^TEXMFVAR =.*@TEXMFVAR = %{_localstatedir}@' \
	-e 's@^trie_size.*@trie_size = 1262000@' -i texk/kpathsea/texmf.cnf

cd libs/teckit
cat ax*.m4 > acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd ../..

%ifarch ppc ppc64
# clisp does not work properly on forge
ulimit -s unlimited
%endif

# force texinfo regeneration (normally it requires maintainer mode)
cd texk/kpathsea
makeinfo --paragraph-indent=2 kpathsea.texi -o kpathsea.info
cd ../dvipsk
makeinfo --paragraph-indent=2 dvips.texi -o dvips.info
cd ../web2c/doc
makeinfo --paragraph-indent=2 web2c.texi -o web2c.info
cd ../../..

install -d build/utils/xindy/make-rules/alphabets
for f in utils/xindy/make-rules/alphabets/larm????.* ; do ln -sf ../../../../../$f build/$f ; done
cd build
../%configure \
	--with-xindy%{!?with_xindy:=no}\
	--disable-multiplatform \
	--disable-static \
	--enable-a4 \
	--enable-gf \
	--enable-ipc \
	--enable-shared \
	--with-fontconfig \
	--with-fonts-dir=/var/cache/fonts \
	--with-ncurses \
	--with-system-freetype \
	--with-freetype-include=/usr/include/freetype \
	--with-system-freetype2 \
	--with-freetype2-include=/usr/include/freetype2 \
	--with-system-gd \
	--with-system-ncurses \
	--with-system-pnglib \
	--with-system-t1lib \
	--with-system-zlib \
	--with-xdvi-x-toolkit=xaw \
	--without-dialog \
	--without-t1utils \
	--without-texinfo

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_mandir}/man5 \
	$RPM_BUILD_ROOT/var/cache/fonts \
	$RPM_BUILD_ROOT/etc/cron.daily \
	$RPM_BUILD_ROOT/etc/sysconfig/tetex-updmap \
	$RPM_BUILD_ROOT%{_localstatedir}/fonts/map

lzma -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_datadir}

# we don't care that our tex is more than 5 years old
patch --directory=$RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf -p1 < %{PATCH9}

%{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf/texmf $RPM_BUILD_ROOT%{texmf}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf/texmf-dist $RPM_BUILD_ROOT%{texmfdist}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf/texmf-doc $RPM_BUILD_ROOT%{texmfdoc}
%{__mv} $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pgfplots/* $RPM_BUILD_ROOT%{texmfdist}/doc/latex/pgfplots
rmdir $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pgfplots
# imho it is unneeded
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/doc/fonts/{ec,fc,utopia}
%{__rm} -r $RPM_BUILD_ROOT%{texmf}/doc/cefconv

# This is an empty directory
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf
# Useless binary
%{__rm} $RPM_BUILD_ROOT%{_datadir}/texmf-dist/doc/latex/splitindex/splitindex{.exe,-Linux-i386,-OpenBSD-i386}

# commented out because of following (non-fatal) error:
# Can't open texmf/web2c/texmf.cnf: No such file or directory.
#perl -pi \
#	-e "s|\.\./\.\./texmf|$RPM_BUILD_ROOT%{texmf}|g;" \
#	-e "s|/var/cache/fonts|$RPM_BUILD_ROOT/var/cache/fonts|g;" \
#	texmf/web2c/texmf.cnf

# dirs for external packages (must be created after the above moves)
install -d $RPM_BUILD_ROOT%{texmf}/doc/latex
# needed for make install???
install -d $RPM_BUILD_ROOT%{texmf}/fonts/opentype/public

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}; export LD_LIBRARY_PATH

%{__make} -C build install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	texmf=$RPM_BUILD_ROOT%{texmf} \
	texmfsysvar=$RPM_BUILD_ROOT%{_localstatedir} \
	texmfsysconfig=$RPM_BUILD_ROOT%{texmf}

%{__rm} $RPM_BUILD_ROOT%{texmfdist}/scripts/pst-pdf/ps4pdf.bat*
%{__rm} $RPM_BUILD_ROOT%{texmf}/scripts/texlive/uninstall-win32.pl
# Fix broken symlinks
CURDIR=$(pwd)
cd $RPM_BUILD_ROOT%{_bindir}
ln -sf ../share/texmf/scripts/a2ping/a2ping.pl a2ping
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/context context
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/ctxtools ctxtools
ln -sf ../share/texmf-dist/scripts/dviasm/dviasm.py dviasm
ln -sf ../share/texmf/scripts/tetex/e2pall.pl e2pall
ln -sf ../share/texmf-dist/scripts/bengali/ebong.py ebong
ln -sf ../share/texmf-dist/scripts/epspdf/epspdf epspdf
ln -sf ../share/texmf-dist/scripts/epspdf/epspdftk epspdftk
ln -sf ../share/texmf/scripts/epstopdf/epstopdf.pl epstopdf
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/exatools exatools
ln -sf ../share/texmf/scripts/texlive/getnonfreefonts.pl getnonfreefonts
ln -sf ../share/texmf/scripts/texlive/getnonfreefonts.pl getnonfreefonts-sys
ln -sf ../share/texmf-dist/scripts/tex4ht/ht.sh ht
ln -sf ../share/texmf-dist/scripts/tex4ht/htcontext.sh htcontext
ln -sf ../share/texmf-dist/scripts/tex4ht/htlatex.sh htlatex
ln -sf ../share/texmf-dist/scripts/tex4ht/htmex.sh htmex
ln -sf ../share/texmf-dist/scripts/tex4ht/httex.sh httex
ln -sf ../share/texmf-dist/scripts/tex4ht/httexi.sh httexi
ln -sf ../share/texmf-dist/scripts/tex4ht/htxelatex.sh htxelatex
ln -sf ../share/texmf-dist/scripts/tex4ht/htxetex.sh htxetex
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/luatools luatools
ln -sf ../share/texmf-dist/scripts/glossaries/makeglossaries makeglossaries
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/makempy makempy
ln -sf ../share/texmf-dist/scripts/tex4ht/mk4ht.pl mk4ht
ln -sf ../share/texmf-dist/scripts/mkjobtexmf/mkjobtexmf.pl mkjobtexmf
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/mpstools mpstools
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/mptopdf mptopdf
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/mtxrun mtxrun
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/mtxtools mtxtools
ln -sf ../share/texmf-dist/scripts/oberdiek/pdfatfi.pl pdfatfi
ln -sf ../share/texmf-dist/scripts/pdfcrop/pdfcrop.pl pdfcrop
ln -sf ../share/texmf-dist/scripts/ppower4/pdfthumb.texlua pdfthumb
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/pdftools pdftools
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/pdftrimwhite pdftrimwhite
ln -sf ../share/texmf-dist/scripts/perltex/perltex.pl perltex
ln -sf ../share/texmf/scripts/pkfix/pkfix.pl pkfix
ln -sf ../share/texmf-dist/scripts/ppower4/ppower4.texlua ppower4
ln -sf ../share/texmf/scripts/ps2eps/ps2eps.pl ps2eps
ln -sf ../share/texmf-dist/scripts/pst-pdf/ps4pdf ps4pdf
ln -sf ../share/texmf-dist/scripts/pst2pdf/pst2pdf.pl pst2pdf
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/pstopdf pstopdf
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/rlxtools rlxtools
ln -sf ../share/texmf/scripts/texlive/rungs.tlu rungs
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/runtools runtools
ln -sf ../share/texmf/scripts/simpdftex/simpdftex simpdftex
ln -sf ../share/texmf-dist/scripts/texcount/TeXcount.pl texcount
ln -sf ../share/texmf/scripts/texlive/texdoc.tlu texdoc
ln -sf ../share/texmf/scripts/tetex/texdoctk.pl texdoctk
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texexec texexec
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texfind texfind
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texfont texfont
ln -sf ../share/texmf-dist/scripts/context/ruby/texmfstart.rb texmfstart
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texshow texshow
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/textools textools
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texutil texutil
ln -sf ../share/texmf-dist/scripts/thumbpdf/thumbpdf.pl thumbpdf
ln -sf ../share/texmf/scripts/texlive/tlmgr.pl tlmgr
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/tmftools tmftools
ln -sf ../share/texmf-dist/scripts/vpe/vpe.pl vpe
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/xmltools xmltools

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE50} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE51} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE52} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE53} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE54} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE55} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE56} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE57} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE58} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE59} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE60} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE61} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE62} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive

install -d $RPM_BUILD_ROOT%{texmf}/tex/latex/misc

cd $RPM_BUILD_ROOT%{texmfdist}/tex/latex

# floatflt
unzip %{SOURCE10}
cd floatflt
latex floatflt.ins
%{__rm} *.log
install -d $RPM_BUILD_ROOT%{texmfdist}/doc/latex/floatflt
%{__mv} *.txt *.tex *.pdf README $RPM_BUILD_ROOT%{texmfdist}/doc/latex/floatflt
cd ..

# foiltex
unzip %{SOURCE12}
cd foiltex
latex foiltex.ins
%{__rm} *.log
install -d $RPM_BUILD_ROOT%{texmfdist}/doc/latex/foiltex
%{__mv} *.tex *.pdf README $RPM_BUILD_ROOT%{texmfdist}/doc/latex/foiltex
cd ..

# larm fonts
cd $RPM_BUILD_ROOT%{texmfdist}
tar xvf %{SOURCE11}
cd fonts/tfm/la
for i in larm?00.tfm; do ln -s $i $(echo $i | sed "s@larm\(.\).*@larm0\100.tfm@") ; done

# wrong dvi in formlett, should be regenerate
cd $RPM_BUILD_ROOT%{texmfdist}/doc/latex/formlett
cp $RPM_BUILD_ROOT%{texmfdist}/tex/latex/formlett/formlett.sty .
tex user_manual.tex
yes | tex prog_manual.tex
tex example1.tex
tex example2.tex
%{__rm} formlett.sty

cd $CURDIR

# some tex-files need xstring.tex and doc/latex isn't in kpathsea search path
cp $RPM_BUILD_ROOT%{texmfdist}/doc/latex/xstring/xstring.tex $RPM_BUILD_ROOT%{texmfdist}/tex/latex/xstring

#install %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}
#touch $RPM_BUILD_ROOT/etc/sysconfig/tetex-updmap/maps.lst

# %{__make} init \
# 	prefix=$RPM_BUILD_ROOT%{_prefix} \
# 	bindir=$RPM_BUILD_ROOT%{_bindir} \
# 	mandir=$RPM_BUILD_ROOT%{_mandir} \
# 	libdir=$RPM_BUILD_ROOT%{_libdir} \
# 	datadir=$RPM_BUILD_ROOT%{_datadir} \
# 	infodir=$RPM_BUILD_ROOT%{_infodir} \
# 	includedir=$RPM_BUILD_ROOT%{_includedir} \
# 	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
# 	texmf=$RPM_BUILD_ROOT%{texmf}

%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/texmf
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/texmf-dist
# We don't need it
%{__rm} -r $RPM_BUILD_ROOT%{texmf}/doc/man
%{__rm} -r $RPM_BUILD_ROOT%{texmfdoc}/source

%{__perl} -pi \
	-e "s|$RPM_BUILD_ROOT||g;" \
	$RPM_BUILD_ROOT%{texmf}/web2c/texmf.cnf

install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.daily/texlive

install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE6} $RPM_BUILD_ROOT%{_pixmapsdir}

# not included in package
rm -f $RPM_BUILD_ROOT%{_datadir}/texinfo/html/texi2html.html
rm -f $RPM_BUILD_ROOT%{_infodir}/dir*
%{__rm} $RPM_BUILD_ROOT%{_infodir}/dvipng*
%{__rm} $RPM_BUILD_ROOT%{texmf}/tex/generic/pdftex/glyphtounicode.tex
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/lcdf-typetools
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pdf-trans
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/source/generic/hyph-utf8
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/source/generic/patch
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/source/plain/plgraph
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/tex/generic/pdf-trans
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/tex/generic/xecyr
%{__rm} -r $RPM_BUILD_ROOT%{texmf}/chktex
%{__rm} -r $RPM_BUILD_ROOT%{texmf}/doc/cef5conv
%{__rm} -r $RPM_BUILD_ROOT%{texmf}/doc/cefsconv
%{__rm} -r $RPM_BUILD_ROOT%{texmf}/doc/chktex
%{__rm} -r $RPM_BUILD_ROOT%{texmf}/doc/gzip

# move format logs to BUILD, so $RPM_BUILD_ROOT is not polluted
# and we can still analyze them
# install -d format-logs
# mv -fv $RPM_BUILD_ROOT%{fmtdir}/*.log format-logs

# xindy files are in %%{texmf}
%if %{with xindy}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/xindy
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}
%endif

# Create format files
for format_dir in \
	aleph:aleph \
	csplain:pdftex \
	etex:pdftex \
	lambda:omega \
	lamed:aleph \
	latex:pdftex \
	lualatex:luatex \
	luatex:luatex \
	mex:pdftex \
	mllatex:pdftex \
	mptopdf:pdftex \
	omega:omega \
	pdfcsplain:pdftex \
	pdfetex:pdftex \
	pdflatex:pdftex \
	pdftex:pdftex \
	pdfxmltex:pdftex \
	physe:pdftex \
	phyzzx:pdftex \
	tex:tex \
	texsis:pdftex \
	xetex:xetex \
	xelatex:xetex \
	xmltex:pdftex ; do
	format=${format_dir%:*}
	subdir=${format_dir#*:}
%if %{with bootstrap}
	install -d $RPM_BUILD_ROOT%{fmtdir}/${subdir}
	touch $RPM_BUILD_ROOT%{fmtdir}/${subdir}/${format}.fmt
%else
	PATH=$RPM_BUILD_ROOT%{_bindir}:$PATH \
	fmtutil --fmtdir $RPM_BUILD_ROOT%{fmtdir} --byfmt=${format}
%endif
done

# fix shebangs
%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' \
	$RPM_BUILD_ROOT%{_bindir}/{extractres,fix{dlsr,fm,mac,psdit,psp,scribe,tp,wfw,wp,ww}ps,includeres,psmerge} \
%if %{with xindy}
	$RPM_BUILD_ROOT%{_bindir}/{texindy,xindy} \
%endif
	$RPM_BUILD_ROOT%{texmf}/scripts/tetex/{e2pall,texdoctk}.pl \
	$RPM_BUILD_ROOT%{texmf}/scripts/texlive/{getnonfreefonts,tlmgr}.pl \
	$RPM_BUILD_ROOT%{texmf}/scripts/texlive/tlmgrgui/{tlmgrgui,tlmgrgui-real}.pl \
	$RPM_BUILD_ROOT%{texmf}/scripts/xindy/{texindy,xindy}.pl \
	$RPM_BUILD_ROOT%{texmfdist}/doc/bibtex/bibhtml/bibhtml \
	$RPM_BUILD_ROOT%{texmfdist}/doc/latex/urlbst/urlbst \
	$RPM_BUILD_ROOT%{texmfdist}/doc/latex/register/reg_list.pl \
	$RPM_BUILD_ROOT%{texmfdist}/scripts/glossaries/makeglossaries \
	$RPM_BUILD_ROOT%{texmfdist}/scripts/mkjobtexmf/mkjobtexmf.pl \
	$RPM_BUILD_ROOT%{texmfdist}/scripts/perltex/perltex.pl \
	$RPM_BUILD_ROOT%{texmfdist}/scripts/tex4ht/mk4ht.pl \
	$RPM_BUILD_ROOT%{texmfdist}/scripts/texcount/TeXcount.pl \
	$RPM_BUILD_ROOT%{texmfdist}/source/latex/latex-tds/build.pl

%{__sed} -i -e '1s,/usr/bin/python$,%{__python},' \
	$RPM_BUILD_ROOT%{texmfdist}/doc/generic/enctex/unimap.py \

%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' \
	$RPM_BUILD_ROOT%{texmfdist}/scripts/bengali/ebong.py \
	$RPM_BUILD_ROOT%{texmfdist}/scripts/dviasm/dviasm.py

%{__sed} -i -e '1s,/usr/bin/env ruby,%{__ruby},' \
	$RPM_BUILD_ROOT%{texmfdist}/scripts/context/ruby/{texmfstart,kpseserver,kpseclient}.rb \
	$RPM_BUILD_ROOT%{texmfdist}/scripts/epspdf/{epspdf,epspdftk}.rb

%{__sed} -i -e '1s,/usr/bin/env texlua,%{_bindir}/texlua,' \
	$RPM_BUILD_ROOT%{texmf}/scripts/texlive/{rungs,test-tlpdb,texconf,texdoc}.tlu \
	$RPM_BUILD_ROOT%{texmf}/scripts/texlive/gswin32/*.tlu \
	$RPM_BUILD_ROOT%{texmfdist}/scripts/context/stubs/unix/{luatools,mtxrun} \
	$RPM_BUILD_ROOT%{texmfdist}/scripts/ppower4/{ppower4,pdfthumb}.texlua

# We don't need the log files
find $RPM_BUILD_ROOT%{fmtdir} -name "*.log" | xargs -r %{__rm}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%fixinfodir
%texhash

%postun
%fixinfodir
if [ "$1" = "1" ]; then
	%texhash
fi

%post other-utils
%texhash

%postun other-utils
%texhash

%post jadetex
%texhash

%postun jadetex
%texhash

%post	-n kpathsea -p /sbin/ldconfig
%postun	-n kpathsea -p /sbin/ldconfig

%post -n kpathsea-devel
%fixinfodir

%postun -n kpathsea-devel
%fixinfodir

%post dvips
%fixinfodir
%texhash

%postun dvips
%fixinfodir
%texhash

%post dvilj
%texhash

%postun dvilj
%texhash

%post makeindex
%texhash

%postun makeindex
%texhash

%post scripts
%texhash

%postun scripts
%texhash

%post tex-arrayjob
%texhash

%postun tex-arrayjob
%texhash

%post tex-kastrup
%texhash

%postun tex-kastrup
%texhash

%post tex-insbox
%texhash

%postun tex-insbox
%texhash

%post tex-mathdots
%texhash

%postun tex-mathdots
%texhash

%post tex-midnight
%texhash

%postun tex-midnight
%texhash

%post tex-ofs
%texhash

%postun tex-ofs
%texhash

%post tex-physe
%texhash

%postun tex-physe
%texhash

%post tex-velthuis
%texhash

%postun tex-velthuis
%texhash

%post tex-ytex
%texhash

%postun tex-ytex
%texhash

%post metapost
%texhash

%postun metapost
%texhash

%post metapost-other
%texhash

%postun metapost-other
%texhash

%post mptopdf
%texhash

%postun mptopdf
%texhash

%post texdoctk
%texhash

%postun texdoctk
%texhash

%post -n xdvi
%texhash

%postun -n xdvi
%texhash

%post pdftex
%texhash

%postun pdftex
%texhash

%post phyzzx
%texhash

%postun phyzzx
%texhash

%post omega
%texhash

%postun omega
%texhash

%post plain
%texhash

%postun plain
%texhash

%post mex
%texhash

%postun mex
%texhash

%post format-mex
%texhash

%postun format-mex
%texhash

%post format-pdfmex
%texhash

%postun format-pdfmex
%texhash

%postun format-utf8mex
%texhash

%post amstex
%texhash

%postun amstex
%texhash

%post format-amstex
%texhash

%postun format-amstex
%texhash

%post csplain
%texhash

%postun csplain
%texhash

%post format-csplain
%texhash

%postun format-csplain
%texhash

%post format-pdfcsplain
%texhash

%postun format-pdfcsplain
%texhash

%post cslatex
%texhash

%postun cslatex
%texhash

%post format-cslatex
%texhash

%postun format-cslatex
%texhash

%post format-pdfcslatex
%texhash

%postun format-pdfcslatex
%texhash

%post eplain
%texhash

%postun eplain
%texhash

%post format-eplain
%texhash

%postun format-eplain
%texhash

# ConTeXt format

%post context
%texhash

%postun context
%texhash

%post format-context-de
%texhash

%postun format-context-de
%texhash

%post format-context-en
%texhash

%postun format-context-en
%texhash

%post format-context-nl
%texhash

%postun format-context-nl
%texhash

%post latex
%fixinfodir
%texhash

%postun latex
%fixinfodir
%texhash

%post latex-lang
%texhash

%postun latex-lang
%texhash

%post latex-styles
%texhash

%postun latex-styles
%texhash

%post latex-pdftools
%texhash

%postun latex-pdftools
%texhash

%post latex-extend
%texhash

%postun latex-extend
%texhash

%post latex-presentation
%texhash

%postun latex-presentation
%texhash

%post latex-programming
%texhash

%postun latex-programming
%texhash

%post latex-metre
%texhash

%postun latex-metre
%texhash

%post latex-misc
%texhash

%postun latex-misc
%texhash

%post latex-effects
%texhash

%postun latex-effects
%texhash

%post latex-math
%texhash

%postun latex-math
%texhash

%post latex-music
%texhash

%postun latex-music
%texhash

%post latex-physics
%texhash

%postun latex-physics
%texhash

%post latex-games
%texhash

%postun latex-games
%texhash

%post latex-biology
%texhash

%postun latex-biology
%texhash

%post latex-chem
%texhash

%postun latex-chem
%texhash

%post latex-informatic
%texhash

%postun latex-informatic
%texhash

%post latex-12many
%texhash

%postun latex-12many
%texhash

%post latex-abstract
%texhash

%postun latex-abstract
%texhash

%post latex-accfonts
%texhash

%postun latex-accfonts
%texhash

%post latex-adrconv
%texhash

%postun latex-adrconv
%texhash

%post latex-ae
%texhash

%postun latex-ae
%texhash

%post latex-ams
%texhash

%postun latex-ams
%texhash

%post latex-antp
%texhash

%postun latex-antp
%texhash

%post latex-antt
%texhash

%postun latex-antt
%texhash

%post latex-appendix
%texhash

%postun latex-appendix
%texhash

%post latex-bardiag
%texhash

%postun latex-bardiag
%texhash

%post latex-bbm
%texhash

%postun latex-bbm
%texhash

%post latex-bbold
%texhash

%postun latex-bbold
%texhash

%post latex-beamer
%texhash

%postun latex-beamer
%texhash

%post latex-bezos
%texhash

%postun latex-bezos
%texhash

%post latex-bibtex
%texhash

%postun latex-bibtex
%texhash

%post latex-bibtex-ams
%texhash

%postun latex-bibtex-ams
%texhash

%post latex-bibtex-pl
%texhash

%postun latex-bibtex-pl
%texhash

%post latex-bibtex-german
%texhash

%postun latex-bibtex-german
%texhash

%post latex-bibtex-revtex4
%texhash

%postun latex-bibtex-revtex4
%texhash

%post latex-bibtex-jurabib
%texhash

%postun latex-bibtex-jurabib
%texhash

%post latex-bibtex-styles
%texhash

%postun latex-bibtex-styles
%texhash

%post latex-booktabs
%texhash

%postun latex-booktabs
%texhash

%post latex-caption
%texhash

%postun latex-caption
%texhash

%post latex-carlisle
%texhash

%postun latex-carlisle
%texhash

%post latex-ccfonts
%texhash

%postun latex-ccfonts
%texhash

%post latex-cite
%texhash

%postun latex-cite
%texhash

%post latex-cmbright
%texhash

%postun latex-cmbright
%texhash

%post latex-colortab
%texhash

%postun latex-colortab
%texhash

%post latex-comment
%texhash

%postun latex-comment
%texhash

%post latex-concmath
%texhash

%postun latex-concmath
%texhash

%post latex-currvita
%texhash

%postun latex-currvita
%texhash

%post latex-curves
%texhash

%postun latex-curves
%texhash

%post latex-custom-bib
%texhash

%postun latex-custom-bib
%texhash

%post latex-cyrillic
%texhash

%postun latex-cyrillic
%texhash

%post latex-enumitem
%texhash

%postun latex-enumitem
%texhash

%post latex-exams
%texhash

%postun latex-exams
%texhash

%post latex-float
%texhash

%postun latex-float
%texhash

%post latex-foiltex
%texhash

%postun latex-foiltex
%texhash

%post latex-formlett
%texhash

%postun latex-formlett
%texhash

%post latex-formular
%texhash

%postun latex-formular
%texhash

%post latex-gbrief
%texhash

%postun latex-gbrief
%texhash

%post latex-keystroke
%texhash

%postun latex-keystroke
%texhash

%post latex-labbook
%texhash

%postun latex-labbook
%texhash

%post latex-lcd
%texhash

%postun latex-lcd
%texhash

%post latex-leaflet
%texhash

%postun latex-leaflet
%texhash

%post latex-leftidx
%texhash

%postun latex-leftidx
%texhash

%post latex-lewis
%texhash

%postun latex-lewis
%texhash

%post latex-lm
%texhash

%post latex-lastpage
%texhash

%postun latex-lastpage
%texhash

%postun latex-lm
%texhash

%post latex-lucidabr
%texhash

%postun latex-lucidabr
%texhash

%post latex-marvosym
%texhash

%postun latex-marvosym
%texhash

%post latex-mflogo
%texhash

%postun latex-mflogo
%texhash

%post latex-mfnfss
%texhash

%postun latex-mfnfss
%texhash

%post latex-minitoc
%texhash

%postun latex-minitoc
%texhash

%post latex-mltex
%texhash

%postun latex-mltex
%texhash

%post latex-moreverb
%texhash

%postun latex-moreverb
%texhash

%post latex-multienum
%texhash

%postun latex-multienum
%texhash

%post latex-musictex
%texhash

%postun latex-musictex
%texhash

%post latex-ntheorem
%texhash

%postun latex-ntheorem
%texhash

%post latex-other
%texhash

%postun latex-other
%texhash

%post latex-other-doc
%texhash

%postun latex-other-doc
%texhash

%post latex-pdfslide
%texhash

%postun latex-pdfslide
%texhash

%post latex-pgf
%texhash

%postun latex-pgf
%texhash

%post latex-polynom
%texhash

%postun latex-polynom
%texhash

%post latex-polynomial
%texhash

%postun latex-polynomial
%texhash

%post latex-prosper
%texhash

%postun latex-prosper
%texhash

%post latex-pseudocode
%texhash

%postun latex-pseudocode
%texhash

%post latex-psnfss
%texhash

%postun latex-psnfss
%texhash

%post latex-pst-2dplot
%texhash

%postun latex-pst-2dplot
%texhash

%post latex-pst-3dplot
%texhash

%postun latex-pst-3dplot
%texhash

%post latex-pst-bar
%texhash

%postun latex-pst-bar
%texhash

%post latex-pst-circ
%texhash

%postun latex-pst-circ
%texhash

%post latex-pst-eucl
%texhash

%postun latex-pst-eucl
%texhash

%post latex-pst-diffraction
%texhash

%postun latex-pst-diffraction
%texhash

%post latex-pst-fun
%texhash

%postun latex-pst-fun
%texhash

%post latex-pst-func
%texhash

%postun latex-pst-func
%texhash

%post latex-pst-infixplot
%texhash

%postun latex-pst-infixplot
%texhash

%post latex-pst-fr3d
%texhash

%postun latex-pst-fr3d
%texhash

%post latex-pst-fractal
%texhash

%postun latex-pst-fractal
%texhash

%post latex-pxfonts
%texhash

%post latex-pst-math
%texhash

%postun latex-pst-math
%texhash

%post latex-pst-ob3d
%texhash

%postun latex-pst-ob3d
%texhash

%post latex-pst-optic
%texhash

%postun latex-pst-optic
%texhash

%post latex-pst-optexp
%texhash

%postun latex-pst-optexp
%texhash

%post latex-pst-text
%texhash

%postun latex-pst-text
%texhash

%post latex-pst-uncategorized
%texhash

%postun latex-pst-uncategorized
%texhash

%postun latex-pxfonts
%texhash

%post latex-SIstyle
%texhash

%postun latex-SIstyle
%texhash

%post latex-SIunits
%texhash

%postun latex-SIunits
%texhash

%post latex-siunitx
%texhash

%postun latex-siunitx
%texhash

%post latex-Tabbing
%texhash

%postun latex-Tabbing
%texhash

%post latex-txfonts
%texhash

%postun latex-txfonts
%texhash

%post latex-ucs
%texhash

%postun latex-ucs
%texhash

%post latex-umlaute
%texhash

%postun latex-umlaute
%texhash

%post latex-variations
%texhash

%postun latex-variations
%texhash

%post latex-wasysym
%texhash

%postun latex-wasysym
%texhash

%post latex-xcolor
%texhash

%postun latex-xcolor
%texhash

%post format-pdflatex
%texhash

%postun format-pdflatex
%texhash

%post tex-babel
%texhash

%postun tex-babel
%texhash

%post tex-german
%texhash

%postun tex-german
%texhash

%post tex-mfpic
%texhash

%postun tex-mfpic
%texhash

%post tex-misc
%texhash

%postun tex-misc
%texhash

%post tex-pictex
%texhash

%postun tex-pictex
%texhash

%post tex-psizzl
%texhash

%postun tex-psizzl
%texhash

%post tex-pstricks
%texhash

%postun tex-pstricks
%texhash

%post tex-qpxqtx
%texhash

%postun tex-qpxqtx
%texhash

%post tex-huhyphen
%texhash

%postun tex-huhyphen
%texhash

%post tex-ruhyphen
%texhash

%postun tex-ruhyphen
%texhash

%post tex-spanish
%texhash

%postun tex-spanish
%texhash

%post tex-texdraw
%texhash

%postun tex-texdraw
%texhash

%post tex-thumbpdf
%texhash

%postun tex-thumbpdf
%texhash

%post tex-ukrhyph
%texhash

%postun tex-ukrhyph
%texhash

%post latex-vietnam
%texhash

%postun latex-vietnam
%texhash

%post tex-xkeyval
%texhash

%postun tex-xkeyval
%texhash

%post tex-xypic
%texhash

%postun tex-xypic
%texhash

%post fonts-adobe
%texhash

%postun fonts-adobe
%texhash

%post fonts-larm
%texhash

%postun fonts-larm
%texhash

%post fonts-ae
%texhash

%postun fonts-ae
%texhash

%post fonts-ams
%texhash

%postun fonts-ams
%texhash

%post fonts-antp
%texhash

%postun fonts-antp
%texhash

%post fonts-antt
%texhash

%postun fonts-antt
%texhash

%post fonts-bbm
%texhash

%postun fonts-bbm
%texhash

%post fonts-bbold
%texhash

%postun fonts-bbold
%texhash

%post fonts-bitstream
%texhash

%postun fonts-bitstream
%texhash

%post fonts-cc-pl
%texhash

%postun fonts-cc-pl
%texhash

%post fonts-cg
%texhash

%postun fonts-cg
%texhash

%post fonts-cm
%texhash

%postun fonts-cm
%texhash

%post fonts-cmbright
%texhash

%postun fonts-cmbright
%texhash

%post fonts-cmcyr
%texhash

%postun fonts-cmcyr
%texhash

%post fonts-cmextra
%texhash

%postun fonts-cmextra
%texhash

%post fonts-cmsuper
%texhash

%postun fonts-cmsuper
%texhash

%post fonts-concmath
%texhash

%postun fonts-concmath
%texhash

%post fonts-concrete
%texhash

%postun fonts-concrete
%texhash

%post fonts-cs
%texhash

%postun fonts-cs
%texhash

%post fonts-ecc
%texhash

%postun fonts-ecc
%texhash

%post fonts-eurosym
%texhash

%postun fonts-eurosym
%texhash

%post fonts-euxm
%texhash

%postun fonts-euxm
%texhash

%post fonts-gothic
%texhash

%postun fonts-gothic
%texhash

%post fonts-hoekwater
%texhash

%postun fonts-hoekwater
%texhash

%post fonts-jknappen
%texhash

%postun fonts-jknappen
%texhash

%post fonts-latex
%texhash

%postun fonts-latex
%texhash

%post fonts-kpfonts
%texhash

%postun fonts-kpfonts
%texhash

%post fonts-lh
%texhash

%postun fonts-lh
%texhash

%post fonts-lm
%texhash

%postun fonts-lm
%texhash

%post fonts-marvosym
%texhash

%postun fonts-marvosym
%texhash

%post fonts-mflogo
%texhash

%postun fonts-mflogo
%texhash

%post fonts-misc
%texhash

%postun fonts-misc
%texhash

%post fonts-monotype
%texhash

%postun fonts-monotype
%texhash

%post fonts-omega
%texhash

%postun fonts-omega
%texhash

%post fonts-other
%texhash

%postun fonts-other
%texhash

%post fonts-pl
%texhash

%postun fonts-pl
%texhash

%post fonts-px
%texhash

%postun fonts-px
%texhash

%post fonts-qpxqtx
%texhash

%postun fonts-qpxqtx
%texhash

%post fonts-rsfs
%texhash

%postun fonts-rsfs
%texhash

%post fonts-stmaryrd
%texhash

%postun fonts-stmaryrd
%texhash

%post fonts-tx
%texhash

%postun fonts-tx
%texhash

%post fonts-urw
%texhash

%postun fonts-urw
%texhash

%post fonts-urw35vf
%texhash

%postun fonts-urw35vf
%texhash

%post fonts-vnr
%texhash

%postun fonts-vnr
%texhash

%post fonts-wasy
%texhash

%postun fonts-wasy
%texhash

%post fonts-xypic
%texhash

%postun fonts-xypic
%texhash

%post fonts-yandy
%texhash

%postun fonts-yandy
%texhash

%post fonts-type1-antp
%texhash

%postun fonts-type1-antp
%texhash

%post fonts-type1-antt
%texhash

%postun fonts-type1-antt
%texhash

%post fonts-type1-belleek
%texhash

%postun fonts-type1-belleek
%texhash

%post fonts-type1-bitstream
%texhash

%postun fonts-type1-bitstream
%texhash

%post fonts-type1-bluesky
%texhash

%postun fonts-type1-bluesky
%texhash

%post fonts-type1-cc-pl
%texhash

%postun fonts-type1-cc-pl
%texhash

%post fonts-type1-cmcyr
%texhash

%postun fonts-type1-cmcyr
%texhash

%post fonts-type1-cs
%texhash

%postun fonts-type1-cs
%texhash

%post fonts-type1-eurosym
%texhash

%postun fonts-type1-eurosym
%texhash

%post fonts-type1-hoekwater
%texhash

%postun fonts-type1-hoekwater
%texhash

%post fonts-type1-lm
%texhash

%postun fonts-type1-lm
%texhash

%post fonts-type1-marvosym
%texhash

%postun fonts-type1-marvosym
%texhash

%post fonts-type1-mathpazo
%texhash

%postun fonts-type1-mathpazo
%texhash

%post fonts-type1-omega
%texhash

%postun fonts-type1-omega
%texhash

%post fonts-type1-pl
%texhash

%postun fonts-type1-pl
%texhash

%post fonts-type1-px
%texhash

%postun fonts-type1-px
%texhash

%post fonts-type1-tx
%texhash

%postun fonts-type1-tx
%texhash

%post fonts-type1-urw
%texhash

%postun fonts-type1-urw
%texhash

%post fonts-type1-vnr
%texhash

%postun fonts-type1-vnr
%texhash

%post fonts-type1-xypic
%texhash

%postun fonts-type1-xypic
%texhash

%post -n texconfig
%texhash

%postun -n texconfig
%texhash

%post xetex
%texhash

%postun xetex
%texhash

%post xmltex
%texhash

%postun xmltex
%texhash

%post luatex
%texhash

%postun luatex
%texhash

%files
%defattr(644,root,root,755)
# There isn't doc/fonts directory
%dir %{texmfdist}/doc/fonts
%doc %{texmfdist}/doc/fontname

# ***********
# executables
# ***********
%attr(755,root,root) %{_bindir}/afm2tfm
%attr(755,root,root) %{_bindir}/allcm
%attr(755,root,root) %{_bindir}/allec
%attr(755,root,root) %{_bindir}/allneeded
%attr(755,root,root) %{_bindir}/cweave
%attr(755,root,root) %{_bindir}/ctangle
%attr(755,root,root) %{_bindir}/ctie
%attr(755,root,root) %{_bindir}/dmp
%attr(755,root,root) %{_bindir}/dvipng
%attr(755,root,root) %{_bindir}/ebb
%attr(755,root,root) %{_bindir}/fmtutil
%attr(755,root,root) %{_bindir}/fmtutil-sys
%attr(755,root,root) %{_bindir}/fontinst
%attr(755,root,root) %{_bindir}/gftodvi
%attr(755,root,root) %{_bindir}/gftopk
%attr(755,root,root) %{_bindir}/gftype
%attr(755,root,root) %{_bindir}/gsftopk
%attr(755,root,root) %{_bindir}/kpseaccess
%attr(755,root,root) %{_bindir}/kpsereadlink
%attr(755,root,root) %{_bindir}/kpsewhere
%attr(755,root,root) %{_bindir}/mag
%attr(755,root,root) %{_bindir}/makempx
%attr(755,root,root) %{_bindir}/mf
%attr(755,root,root) %{_bindir}/mf-nowin
%attr(755,root,root) %{_bindir}/mft
%attr(755,root,root) %{_bindir}/mktexmf
%attr(755,root,root) %{_bindir}/mktexpk
%attr(755,root,root) %{_bindir}/mktextfm
%attr(755,root,root) %{_bindir}/mktexfmt
%attr(755,root,root) %{_bindir}/mktexlsr
%attr(755,root,root) %{_bindir}/newer
%attr(755,root,root) %{_bindir}/patgen
%attr(755,root,root) %{_bindir}/pdfetex
%attr(755,root,root) %{_bindir}/pfb2pfa
%attr(755,root,root) %{_bindir}/pk2bm
%attr(755,root,root) %{_bindir}/pktogf
%attr(755,root,root) %{_bindir}/pktype
%attr(755,root,root) %{_bindir}/pltotf
%attr(755,root,root) %{_bindir}/pooltype
%attr(755,root,root) %{_bindir}/ps2frag
%attr(755,root,root) %{_bindir}/ps2pk
%attr(755,root,root) %{_bindir}/tangle
%attr(755,root,root) %{_bindir}/tex
%attr(755,root,root) %{_bindir}/texhash
%attr(755,root,root) %{_bindir}/texlinks
%attr(755,root,root) %{_bindir}/tftopl
%attr(755,root,root) %{_bindir}/tie
%attr(755,root,root) %{_bindir}/ttf2afm
%attr(755,root,root) %{_bindir}/updmap
%attr(755,root,root) %{_bindir}/updmap-sys
%attr(755,root,root) %{_bindir}/vftovp
%attr(755,root,root) %{_bindir}/vptovf
%attr(755,root,root) %{_bindir}/weave

%attr(755,root,root) %{texmf}/web2c/mktexnam
%attr(755,root,root) %{texmf}/web2c/mktexdir
%attr(755,root,root) %{texmf}/web2c/mktexupd

%attr(750,root,root) /etc/cron.daily/texlive

%ghost %{texmf}/ls-R
%ghost %{texmfdist}/ls-R

%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.dat
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.def
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.us
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.us.def

%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/fmtutil.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktex.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktex.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktexdir.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktexnam.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/texmf.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/updmap.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/updmap-hdr.cfg

%attr(1777,root,root) /var/cache/fonts

%{_datadir}/info/web2c.info*

# ***********
# Directories
# ***********
%attr(1777,root,root) %dir %{_localstatedir}
%attr(1777,root,root) %dir %{_localstatedir}/fonts
%attr(1777,root,root) %dir %{_localstatedir}/fonts/map
%attr(1777,root,root) %dir %{fmtdir}

%dir %{texmfdist}/doc
%dir %{texmfdist}/doc/generic
%dir %{texmfdist}/doc/generic/enctex
%dir %{texmfdist}/doc/latex
%dir %{texmfdist}/dvips
%dir %{texmfdist}/mft
%dir %{texmfdist}/makeindex
%dir %{texmfdist}/tex
%dir %{texmfdist}/tex/generic
%dir %{texmfdist}/tex/generic/dehyph-exptl
%dir %{texmfdist}/tex/generic/enctex
%dir %{texmfdist}/tex/generic/hyph-utf8
%dir %{texmfdist}/tex/generic/misc
%dir %{texmfdist}/tex/latex
%dir %{texmfdist}/tex/latex/base
%dir %{texmfdist}/tex/plain
%dir %{texmfdist}/scripts
%dir %{texmfdist}/source/generic
%dir %{texmfdist}/source/latex
%dir %{texmf}/doc
%dir %{texmf}/doc/generic
%dir %{texmf}/doc/latex
%dir %{texmf}/doc/tetex
%dir %{texmf}/dvips
%dir %{texmf}/dvips/config
%dir %{texmf}/dvips/tetex
%dir %{texmf}/fmtutil
%dir %{texmf}/scripts
%dir %{texmf}/scripts/texlive
%dir %{texmf}/tex
%dir %{texmf}/tex/generic
%dir %{texmf}/tex/generic/config
%dir %{texmf}/web2c

# Docs
%doc %{texmfdist}/README
%doc %{texmfdist}/doc/generic/epsf
%doc %{texmfdist}/doc/generic/hyph-utf8
%doc %{texmfdist}/doc/generic/tex-ps
%doc %{texmfdist}/source/fontinst
%doc %{texmf}/README
%doc %{texmf}/doc/dvipng
%doc %{texmf}/doc/tetex/TETEXDOC.*
%doc %{texmf}/doc/tetex/teTeX-FAQ
%doc %{texmf}/doc/texinfo
%doc %{texmf}/doc/web2c

%{texmf}/doc/info

%dir %{texmfdist}/fonts/enc/dvips/vntex
%{texmfdist}/fonts/enc/dvips/vntex/8b.enc
%{texmfdist}/fonts/enc/dvips/vntex/t5.enc
%{texmfdist}/fonts/map/fontname

%{texmf}/fonts/enc/dvips/tetex/09fbbfac.enc
%{texmf}/fonts/enc/dvips/tetex/0ef0afca.enc
%{texmf}/fonts/enc/dvips/tetex/10037936.enc
%{texmf}/fonts/enc/dvips/tetex/1b6d048e.enc
%{texmf}/fonts/enc/dvips/tetex/71414f53.enc
%{texmf}/fonts/enc/dvips/tetex/74afc74c.enc
%{texmf}/fonts/enc/dvips/tetex/aae443f0.enc
%{texmf}/fonts/enc/dvips/tetex/b6a4d7c7.enc
%{texmf}/fonts/enc/dvips/tetex/bbad153f.enc
%{texmf}/fonts/enc/dvips/tetex/d9b29452.enc
%{texmf}/fonts/enc/dvips/tetex/f7b6d320.enc
%{texmf}/fonts/map/dvips/tetex/ps2pk35.map

%{texmfdist}/metafont
%{texmfdist}/mft/base
%{texmfdist}/source/metafont
%{texmfdist}/tex/fontinst
%{texmfdist}/tex/generic/dehyph-exptl/*
%{texmfdist}/tex/generic/encodings
%{texmfdist}/tex/generic/epsf
%{texmfdist}/tex/generic/hyph-utf8/*
%{texmfdist}/tex/generic/genmisc
%{texmfdist}/tex/generic/misc/null.tex
%{texmfdist}/tex/generic/misc/texnames.sty
%{texmfdist}/tex/generic/tap
%{texmfdist}/tex/generic/tex-ps
%{texmfdist}/tex/texinfo
%{texmf}/tex/fontinst
%{texmf}/tex/generic/hyphen
%{texmf}/fmtutil/format.metafont.cnf
%{texmf}/fonts/map/dvips/updmap/*
%{texmf}/web2c/*.tcx

%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/allcm.1*
%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*
%{_mandir}/man1/ctangle.1*
%{_mandir}/man1/ctie.1*
%{_mandir}/man1/cweave.1*
%{_mandir}/man1/cweb.1*
%{_mandir}/man1/dmp.1*
%{_mandir}/man1/dvipdft.1*
%{_mandir}/man1/dvipng.1*
%{_mandir}/man1/ebb.1*
%{_mandir}/man1/fmtutil.1*
%{_mandir}/man1/fmtutil-sys.1*
%{_mandir}/man1/fontinst.1*
%{_mandir}/man1/gftodvi.1*
%{_mandir}/man1/gftopk.1*
%{_mandir}/man1/gftype.1*
%{_mandir}/man1/gsftopk.1*
%{_mandir}/man1/kpseaccess.1*
%{_mandir}/man1/kpsereadlink.1*
%{_mandir}/man1/kpsewhere.1*
%{_mandir}/man1/mag.1*
%{_mandir}/man1/makempx.1*
%{_mandir}/man1/makempy.1*
%{_mandir}/man1/mf.1*
%{_mandir}/man1/mf-nowin.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*
%{_mandir}/man1/mktexfmt.1*
%{_mandir}/man1/mktexlsr.1*
%{_mandir}/man1/newer.1*
%{_mandir}/man1/patgen.1*
%{_mandir}/man1/pdfetex.1*
%{_mandir}/man1/pfb2pfa.1*
%{_mandir}/man1/pk2bm.1*
%{_mandir}/man1/pktogf.1*
%{_mandir}/man1/pktype.1*
%{_mandir}/man1/pltotf.1*
%{_mandir}/man1/pooltype.1*
%{_mandir}/man1/ps2frag.1*
%{_mandir}/man1/ps2pk.1*
%{_mandir}/man1/tangle.1*
%{_mandir}/man1/tex.1*
%{_mandir}/man1/texexec.1*
%{_mandir}/man1/texhash.1*
%{_mandir}/man1/texlinks.1*
%{_mandir}/man1/tftopl.1*
%{_mandir}/man1/tie.1*
%{_mandir}/man1/ttf2afm.1*
%{_mandir}/man1/updmap.1*
%{_mandir}/man1/updmap-sys.1*
%{_mandir}/man1/vftovp.1*
%{_mandir}/man1/vptovf.1*
%{_mandir}/man1/weave.1*
%{_mandir}/man5/fmtutil.cnf.5*
%{_mandir}/man5/updmap.cfg.5*
%dir %{fmtdir}/pdftex
%{fmtdir}/pdftex/pdfetex.fmt
%dir %{fmtdir}/tex
%{fmtdir}/tex/tex.fmt

%files other-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bg5+latex
%attr(755,root,root) %{_bindir}/bg5+pdflatex
%attr(755,root,root) %{_bindir}/bg5conv
%attr(755,root,root) %{_bindir}/bg5latex
%attr(755,root,root) %{_bindir}/bg5pdflatex
%attr(755,root,root) %{_bindir}/bibtex8
%attr(755,root,root) %{_bindir}/cfftot1
%attr(755,root,root) %{_bindir}/ebong
%attr(755,root,root) %{_bindir}/extconv
%attr(755,root,root) %{_bindir}/extractbb
%attr(755,root,root) %{_bindir}/gbklatex
%attr(755,root,root) %{_bindir}/gbkpdflatex
%attr(755,root,root) %{_bindir}/getnonfreefonts
%attr(755,root,root) %{_bindir}/getnonfreefonts-sys
%attr(755,root,root) %{_bindir}/hbf2gf
%attr(755,root,root) %{_bindir}/lamed
%attr(755,root,root) %{_bindir}/makeglossaries
%attr(755,root,root) %{_bindir}/metafun
%attr(755,root,root) %{_bindir}/mkjobtexmf
%attr(755,root,root) %{_bindir}/mllatex
%attr(755,root,root) %{_bindir}/mltex
%attr(755,root,root) %{_bindir}/mmafm
%attr(755,root,root) %{_bindir}/mmpfb
%attr(755,root,root) %{_bindir}/musixflx
%attr(755,root,root) %{_bindir}/ofm2opl
%attr(755,root,root) %{_bindir}/otfinfo
%attr(755,root,root) %{_bindir}/otftotfm
%attr(755,root,root) %{_bindir}/oxdvi
%attr(755,root,root) %{_bindir}/pdfatfi
%attr(755,root,root) %{_bindir}/pdfclose
%attr(755,root,root) %{_bindir}/pdfopen
%attr(755,root,root) %{_bindir}/pdftosrc
%attr(755,root,root) %{_bindir}/perltex
%attr(755,root,root) %{_bindir}/physe
%attr(755,root,root) %{_bindir}/pkfix
%attr(755,root,root) %{_bindir}/rungs
%attr(755,root,root) %{_bindir}/simpdftex
%attr(755,root,root) %{_bindir}/sjisconv
%attr(755,root,root) %{_bindir}/sjislatex
%attr(755,root,root) %{_bindir}/sjispdflatex
%attr(755,root,root) %{_bindir}/synctex
%attr(755,root,root) %{_bindir}/t1dotlessj
%attr(755,root,root) %{_bindir}/t1lint
%attr(755,root,root) %{_bindir}/t1reencode
%attr(755,root,root) %{_bindir}/t1testpage
%attr(755,root,root) %{_bindir}/texcount
%attr(755,root,root) %{_bindir}/texsis
%attr(755,root,root) %{_bindir}/tpic2pdftex
%attr(755,root,root) %{_bindir}/ttf2pk
%attr(755,root,root) %{_bindir}/ttf2tfm
%attr(755,root,root) %{_bindir}/ttftotype42
%attr(755,root,root) %{_bindir}/vlna
%attr(755,root,root) %{_bindir}/vpe
%{_mandir}/man1/cfftot1.1*
%{_mandir}/man1/getnonfreefonts-sys.1
%{_mandir}/man1/getnonfreefonts.1*
%{_mandir}/man1/hbf2gf.1*
%{_mandir}/man1/mkjobtexmf.1*
%{_mandir}/man1/mmafm.1*
%{_mandir}/man1/mmpfb.1*
%{_mandir}/man1/otfinfo.1*
%{_mandir}/man1/otftotfm.1*
%{_mandir}/man1/oxdvi.1
%{_mandir}/man1/pdftosrc.1*
%{_mandir}/man1/synctex.1*
%{_mandir}/man1/t1dotlessj.1*
%{_mandir}/man1/t1lint.1*
%{_mandir}/man1/t1reencode.1*
%{_mandir}/man1/t1testpage.1*
%{_mandir}/man1/ttf2pk.1*
%{_mandir}/man1/ttf2tfm.1*
%{_mandir}/man1/ttftotype42.1*
%{_mandir}/man1/vlna.1*
%{_mandir}/man5/synctex.5*
%dir %{texmfdist}/scripts/mkjobtexmf
%attr(755,root,root) %{texmfdist}/scripts/mkjobtexmf/mkjobtexmf.pl
%{texmfdist}/source/startex
%{texmfdist}/tex/texsis
%{texmfdist}/tex/startex
%{texmf}/fmtutil/fmtutil-hdr.cnf
%{texmf}/fmtutil/format.cyrtex.cnf
%{texmf}/fmtutil/format.cyrtexinfo.cnf
%{texmf}/fmtutil/format.mltex.cnf
%{texmf}/ttf2pk
%{texmf}/fonts/enc/ttf2pk
%{texmf}/fonts/map/ttf2pk
%{texmfdist}/tex/generic/abbr
%{texmfdist}/tex/generic/abstyles
%{texmfdist}/tex/generic/barr
%{texmfdist}/tex/generic/borceux
%{texmfdist}/source/generic/borceux
%{texmfdist}/tex/generic/c-pascal
%{texmfdist}/tex/generic/cirth
%{texmfdist}/tex/generic/dratex
%{texmfdist}/tex/generic/ean
%{texmfdist}/tex/generic/edmac
%{texmfdist}/tex/generic/elvish
%{texmfdist}/tex/generic/fenixpar
%{texmfdist}/tex/generic/fltpoint
%{texmfdist}/source/generic/fltpoint
%{texmfdist}/tex/generic/musixtex
%{texmfdist}/source/generic/hyphenex
%{texmfdist}/source/generic/mkjobtexmf
%{texmf}/hbf2gf
%{texmf}/fmtutil/format.texsis.cnf
%{fmtdir}/pdftex/texsis.fmt
# rungs and friends
%dir %{texmf}/scripts/texlive/gswin32
%attr(755,root,root) %{texmf}/scripts/texlive/psv.tlu
%attr(755,root,root) %{texmf}/scripts/texlive/rungs.tlu
%attr(755,root,root) %{texmf}/scripts/texlive/gswin32/*

%files jadetex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jadetex
%attr(755,root,root) %{_bindir}/pdfjadetex
%dir %{texmfdist}/doc/jadetex
%doc %{texmfdist}/doc/jadetex/base
%dir %{texmfdist}/source/jadetex
%dir %{texmfdist}/source/jadetex/base
%doc %{texmfdist}/source/jadetex/base/ChangeLog*
%{texmfdist}/source/jadetex/base/Makefile
%{texmfdist}/source/jadetex/base/jadetex.*
%{texmfdist}/tex/jadetex
%{texmf}/fmtutil/format.jadetex.cnf

%files other-utils-doc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/abbr
%doc %{texmfdist}/doc/texsis
%doc %{texmfdist}/doc/startex
%doc %{texmfdist}/doc/generic/c-pascal
%doc %{texmfdist}/doc/generic/barr
%doc %{texmfdist}/doc/generic/borceux
%doc %{texmfdist}/doc/generic/dratex
%doc %{texmfdist}/doc/generic/mkjobtexmf
%doc %{texmfdist}/doc/support/texcount
%doc %{texmf}/doc/tpic2pdftex
%doc %{texmf}/doc/extconv
%doc %{texmfdist}/doc/generic/fenixpar
%doc %{texmfdist}/doc/generic/fltpoint
%doc %{texmf}/doc/bg5conv
%doc %{texmf}/doc/pkfix
%doc %{texmf}/doc/hbf2gf
%doc %{texmf}/doc/ttf2pk
%doc %{texmf}/doc/sjisconv
%doc %{texmf}/doc/vlna

%files dirs-fonts
%defattr(644,root,root,755)
%dir %{texmfdist}
%dir %{texmfdist}/fonts
%dir %{texmfdist}/fonts/afm
%dir %{texmfdist}/fonts/afm/hoekwater
%dir %{texmfdist}/fonts/afm/public
%dir %{texmfdist}/fonts/afm/vntex
%dir %{texmfdist}/fonts/enc
%dir %{texmfdist}/fonts/enc/dvips
%dir %{texmfdist}/fonts/map
%dir %{texmfdist}/fonts/map/dvipdfm
%dir %{texmfdist}/fonts/map/dvips
%dir %{texmfdist}/fonts/map/dvips/vntex
%dir %{texmfdist}/fonts/map/public
%dir %{texmfdist}/fonts/map/vtex
%dir %{texmfdist}/fonts/ofm
%dir %{texmfdist}/fonts/ofm/public
%dir %{texmfdist}/fonts/ovf
%dir %{texmfdist}/fonts/ovf/public
%dir %{texmfdist}/fonts/ovp
%dir %{texmfdist}/fonts/ovp/public
%dir %{texmfdist}/fonts/opentype
%dir %{texmfdist}/fonts/opentype/public
%dir %{texmfdist}/fonts/pk
%dir %{texmfdist}/fonts/pk/ljfour
%dir %{texmfdist}/fonts/source
%dir %{texmfdist}/fonts/source/public
%dir %{texmfdist}/fonts/source/vntex
%dir %{texmfdist}/fonts/tfm
%dir %{texmfdist}/fonts/tfm/public
%dir %{texmfdist}/fonts/tfm/vntex
%dir %{texmfdist}/fonts/truetype
%dir %{texmfdist}/fonts/type1
%dir %{texmfdist}/fonts/type1/hoekwater
%dir %{texmfdist}/fonts/type1/public
%dir %{texmfdist}/fonts/type1/vntex
%dir %{texmfdist}/fonts/vf
%dir %{texmfdist}/fonts/vf/public
%dir %{texmfdist}/fonts/vf/vntex
%dir %{texmfdist}/source
%dir %{texmfdist}/source/fonts
%dir %{texmfdist}/source/fonts/eurofont
%dir %{texmf}
%dir %{texmf}/fonts
%dir %{texmf}/fonts/enc
%dir %{texmf}/fonts/enc/dvips
%dir %{texmf}/fonts/enc/dvips/tetex
%dir %{texmf}/fonts/map
%dir %{texmf}/fonts/map/dvips
%dir %{texmf}/fonts/map/dvips/tetex
%dir %{texmf}/fonts/map/dvips/updmap
%dir %{texmf}/fonts/opentype
%dir %{texmf}/fonts/opentype/public

%files doc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/dehyph-exptl
%dir %{texmfdoc}
%dir %{texmfdoc}/doc
%{texmfdoc}/README
%{texmfdoc}/ls-R
%{texmfdoc}/doc/english
%{texmfdist}/doc/fontinst

%files doc-bg
%defattr(644,root,root,755)
%{texmfdoc}/doc/bulgarian

%files doc-cs
%defattr(644,root,root,755)
%{texmfdoc}/doc/czechslovak

%files doc-de
%defattr(644,root,root,755)
%{texmfdoc}/doc/german

%files doc-el
%defattr(644,root,root,755)
%{texmfdoc}/doc/greek
%{texmf}/doc/generic/elhyphen

%files doc-es
%defattr(644,root,root,755)
%{texmfdoc}/doc/spanish

%files doc-fi
%defattr(644,root,root,755)
%{texmfdoc}/doc/finnish

%files doc-fr
%defattr(644,root,root,755)
%{texmfdoc}/doc/french

%files doc-it
%defattr(644,root,root,755)
%{texmfdoc}/doc/italian

%files doc-ja
%defattr(644,root,root,755)
%{texmfdoc}/doc/japanese

%files doc-ko
%defattr(644,root,root,755)
%{texmfdoc}/doc/korean

%files doc-mn
%defattr(644,root,root,755)
%{texmfdoc}/doc/mongolian

%files doc-nl
%defattr(644,root,root,755)
%{texmfdoc}/doc/dutch

%files doc-pl
%defattr(644,root,root,755)
%{texmfdoc}/doc/polish

%files doc-pt
%defattr(644,root,root,755)
%{texmfdoc}/doc/portuguese

%files doc-ru
%defattr(644,root,root,755)
%{texmfdoc}/doc/russian

%files doc-sk
%defattr(644,root,root,755)
%{texmfdoc}/doc/slovak

%files doc-sl
%defattr(644,root,root,755)
%{texmfdoc}/doc/slovenian

%files doc-th
%defattr(644,root,root,755)
%{texmfdoc}/doc/thai

%files doc-tr
%defattr(644,root,root,755)
%{texmfdoc}/doc/turkish

%files doc-uk
%defattr(644,root,root,755)
%{texmfdoc}/doc/ukrainian

%files doc-vi
%defattr(644,root,root,755)
%{texmfdoc}/doc/vietnamese

%files doc-zh_CN
%defattr(644,root,root,755)
%{texmfdoc}/doc/chinese

%files doc-latex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/calrsfs
%doc %{texmfdist}/doc/generic/encxvlna
%doc %{texmfdist}/doc/generic/shapepar
%doc %{texmfdist}/doc/generic/textmerg
%doc %{texmfdist}/doc/latex/acronym
%doc %{texmfdist}/doc/latex/aeguill
%doc %{texmfdist}/doc/latex/anysize
%doc %{texmfdist}/doc/latex/base
%doc %{texmfdist}/doc/latex/beton
%doc %{texmfdist}/doc/latex/cjk
%doc %{texmfdist}/doc/latex/concmath
%doc %{texmfdist}/doc/latex/crop
%doc %{texmfdist}/doc/latex/draftcopy
%doc %{texmfdist}/doc/latex/eepic
%doc %{texmfdist}/doc/latex/endfloat
%doc %{texmfdist}/doc/latex/eso-pic
%doc %{texmfdist}/doc/latex/euler
%doc %{texmfdist}/doc/latex/eulervm
%doc %{texmfdist}/doc/latex/extsizes
%doc %{texmfdist}/doc/latex/fancybox
%doc %{texmfdist}/doc/latex/fancyhdr
%doc %{texmfdist}/doc/latex/fancyvrb
%doc %{texmfdist}/doc/latex/filecontents
%doc %{texmfdist}/doc/latex/float
%doc %{texmfdist}/doc/latex/floatflt
%doc %{texmfdist}/doc/latex/footmisc
%doc %{texmfdist}/doc/latex/footnpag
%doc %{texmfdist}/doc/latex/fp
%doc %{texmfdist}/doc/latex/geometry
%doc %{texmfdist}/doc/latex/graphics
%doc %{texmfdist}/doc/latex/hyperref
%doc %{texmfdist}/doc/latex/hyphenat
%doc %{texmfdist}/doc/latex/index
%doc %{texmfdist}/doc/latex/koma-script
%doc %{texmfdist}/doc/latex/labels
%doc %{texmfdist}/doc/latex/layouts
%doc %{texmfdist}/doc/latex/listings
%doc %{texmfdist}/doc/latex/localloc
%doc %{texmfdist}/doc/latex/ltabptch
%doc %{texmfdist}/doc/latex/mdwtools
%doc %{texmfdist}/doc/latex/memoir
%doc %{texmfdist}/doc/latex/mh
%doc %{texmfdist}/doc/latex/mparhack
%doc %{texmfdist}/doc/latex/ms
%doc %{texmfdist}/doc/latex/multibib
%doc %{texmfdist}/doc/latex/mwcls
%doc %{texmfdist}/doc/latex/nomencl
%doc %{texmfdist}/doc/latex/ntgclass
%doc %{texmfdist}/doc/latex/oberdiek
%doc %{texmfdist}/doc/latex/overpic
%doc %{texmfdist}/doc/latex/paralist
%doc %{texmfdist}/doc/latex/pb-diagram
%doc %{texmfdist}/doc/latex/pdfpages
%doc %{texmfdist}/doc/latex/picinpar
%doc %{texmfdist}/doc/latex/pict2e
%doc %{texmfdist}/doc/latex/placeins
%doc %{texmfdist}/doc/latex/preprint
%doc %{texmfdist}/doc/latex/preview
%doc %{texmfdist}/doc/latex/program
%doc %{texmfdist}/doc/latex/psfrag
%doc %{texmfdist}/doc/latex/revtex
%doc %{texmfdist}/doc/latex/rotating
%doc %{texmfdist}/doc/latex/rotfloat
%doc %{texmfdist}/doc/latex/scale
%doc %{texmfdist}/doc/latex/sectsty
%doc %{texmfdist}/doc/latex/seminar
%doc %{texmfdist}/doc/latex/showlabels
%doc %{texmfdist}/doc/latex/sidecap
%doc %{texmfdist}/doc/latex/slashbox
%doc %{texmfdist}/doc/latex/soul
%doc %{texmfdist}/doc/latex/stdclsdv
%doc %{texmfdist}/doc/latex/subfig
%doc %{texmfdist}/doc/latex/subfigure
%doc %{texmfdist}/doc/latex/textfit
%doc %{texmfdist}/doc/latex/textpos
%doc %{texmfdist}/doc/latex/titlesec
%doc %{texmfdist}/doc/latex/tocbibind
%doc %{texmfdist}/doc/latex/tocloft
%doc %{texmfdist}/doc/latex/tools
%doc %{texmfdist}/doc/latex/totpages
%doc %{texmfdist}/doc/latex/type1cm
%doc %{texmfdist}/doc/latex/units
%doc %{texmfdist}/doc/latex/vmargin
%doc %{texmfdist}/doc/latex/was
%doc %{texmfdist}/doc/latex/wrapfig
%doc %{texmfdist}/doc/latex/xtab
%doc %{texmfdist}/doc/latex/yfonts

%files -n kpathsea
%defattr(644,root,root,755)
%doc %{texmf}/doc/kpathsea
%attr(755,root,root) %{_bindir}/kpsepath
%attr(755,root,root) %{_bindir}/kpsestat
%attr(755,root,root) %{_bindir}/kpsetool
%attr(755,root,root) %{_bindir}/kpsewhich
%attr(755,root,root) %{_bindir}/kpsexpand
%attr(755,root,root) %{_libdir}/libkpathsea.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkpathsea.so.4
%{_libdir}/libkpathsea.la
%{_mandir}/man1/kpsexpand.1*
%{_mandir}/man1/kpsepath.1*
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsetool.1*
%{_mandir}/man1/kpsewhich.1*

%files -n kpathsea-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkpathsea.so
%{_includedir}/kpathsea
%{_infodir}/kpathsea.info*

%files dvips
%defattr(644,root,root,755)
%dir %{texmfdist}/fonts/map/dvips/cmex
%dir %{texmf}/dvipdfm
%dir %{texmf}/fonts/map/dvipdfm
%dir %{texmf}/fonts/map/dvips
%dir %{texmf}/fonts/map/dvips/tetex
%doc %{texmf}/doc/dvips
%doc %{texmf}/doc/dvipdfm
# dvi2fax requires ghostscript
%attr(755,root,root) %{_bindir}/dvi2fax
%attr(755,root,root) %{_bindir}/dvicopy
%attr(755,root,root) %{_bindir}/dvipdfm
%attr(755,root,root) %{_bindir}/dvipdft
%attr(755,root,root) %{_bindir}/dvips
%attr(755,root,root) %{_bindir}/dvired
%attr(755,root,root) %{_bindir}/dvitomp
%attr(755,root,root) %{_bindir}/dvitype
%{_infodir}/dvips.info*
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvicopy.1*
%{_mandir}/man1/dvipdfm.1*
%{_mandir}/man1/dvips.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/dvitype.1*
%{texmfdist}/fonts/enc/dvips/base
%{texmfdist}/fonts/map/dvips/allrunes
%{texmfdist}/fonts/map/dvips/cmex/ttcmex.map
%{texmfdist}/tex/generic/dvips
%{texmfdist}/dvips/ams
%{texmfdist}/dvips/antiqua
%{texmfdist}/dvips/antp
%{texmfdist}/dvips/arphic
%{texmfdist}/dvips/avantgar
%{texmfdist}/dvips/base
%{texmfdist}/dvips/bookman
%{texmfdist}/dvips/brushscr
%{texmfdist}/dvips/cm
%{texmfdist}/dvips/cm-super
%{texmfdist}/dvips/colorsep
%{texmfdist}/dvips/courier
%{texmfdist}/dvips/cs
%{texmfdist}/dvips/dvipsconfig
%{texmfdist}/dvips/esint-type1
%{texmfdist}/dvips/garuda
%{texmfdist}/dvips/gastex
%{texmfdist}/dvips/geomsty
%{texmfdist}/dvips/gothic
%{texmfdist}/dvips/grotesq
%{texmfdist}/dvips/helvetic
%{texmfdist}/dvips/hfbright
%{texmfdist}/dvips/initials
%{texmfdist}/dvips/libertine
%{texmfdist}/dvips/mathdesign
%{texmfdist}/dvips/multi
%{texmfdist}/dvips/musixps
%{texmfdist}/dvips/musixtex
%{texmfdist}/dvips/ncntrsbk
%{texmfdist}/dvips/norasi
%{texmfdist}/dvips/ot2cyr
%{texmfdist}/dvips/palatino
%{texmfdist}/dvips/pl
%{texmfdist}/dvips/psfrag
%{texmfdist}/dvips/pspicture
%{texmfdist}/dvips/pst-*
%{texmfdist}/dvips/pstricks
%{texmfdist}/dvips/pstricks-add
%{texmfdist}/dvips/symbol
%{texmfdist}/dvips/tex-ps
%{texmfdist}/dvips/times
%{texmfdist}/dvips/tree-dvips
%{texmfdist}/dvips/uhc
%{texmfdist}/dvips/xcolor
%{texmfdist}/dvips/xypic
%{texmfdist}/dvips/zapfchan
%{texmfdist}/dvips/zapfding
%{texmfdist}/dvips/zefonts
%{texmf}/dvipdfm/config
%{texmf}/dvips/base
%{texmf}/dvips/config
%{texmf}/dvips/getafm
%{texmf}/dvips/gsftopk
%{texmf}/dvips/tetex/config.*
%{texmf}/fonts/enc/dvips/tetex/mtex.enc
%{texmf}/fonts/enc/dvips/afm2pl
%{texmf}/fonts/map/dvipdfm/updmap
%{texmf}/fonts/map/dvipdfm/dvipdfmx
%{texmf}/fonts/map/dvipdfm/tetex
%{texmf}/fonts/map/dvips/tetex/dvipdfm35.map
%{texmf}/fonts/map/dvips/tetex/dvips35.map
%{texmf}/fonts/map/dvips/tetex/mathpple.map
%{texmf}/fonts/map/dvips/tetex/mt-belleek.map
%{texmf}/fonts/map/dvips/tetex/mt-plus.map
%{texmf}/fonts/map/dvips/tetex/mt-yy.map
%{texmf}/fonts/map/dvips/tetex/pdftex35.map

%files dvilj
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvihp
%attr(755,root,root) %{_bindir}/dvilj
%attr(755,root,root) %{_bindir}/dvilj2p
%attr(755,root,root) %{_bindir}/dvilj4
%attr(755,root,root) %{_bindir}/dvilj4l
%attr(755,root,root) %{_bindir}/dvilj6
%{_mandir}/man1/dvihp.1*
%{_mandir}/man1/dvilj.1*
%{_mandir}/man1/dvilj2p.1*
%{_mandir}/man1/dvilj4.1*
%{_mandir}/man1/dvilj4l.1*
%{_mandir}/man1/dvilj6.1*

%files makeindex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/makeindex
%attr(755,root,root) %{_bindir}/makeindex
%attr(755,root,root) %{_bindir}/mkindex
%attr(755,root,root) %{_bindir}/rumakeindex
%{texmfdist}/makeindex/babel
%{texmfdist}/makeindex/base
%{texmfdist}/makeindex/bibarts
%{texmfdist}/makeindex/circ
%{texmfdist}/makeindex/confproc
%{texmfdist}/makeindex/dtk
%{texmfdist}/makeindex/gatech-thesis
%{texmfdist}/makeindex/gmdoc
%{texmfdist}/makeindex/index
%{texmfdist}/makeindex/iso
%{texmfdist}/makeindex/juraabbrev
%{texmfdist}/makeindex/latex
%{texmfdist}/makeindex/memoir
%{texmfdist}/makeindex/mkind-english
%{texmfdist}/makeindex/mkind-german
%{texmfdist}/makeindex/multibib
%{texmfdist}/makeindex/nomencl
%{texmfdist}/makeindex/nomentbl
%{texmfdist}/makeindex/nostarch
%{texmfdist}/makeindex/plain
%{texmfdist}/makeindex/progkeys
%{texmfdist}/makeindex/repeatindex
%{texmfdist}/makeindex/songbook
%{texmfdist}/makeindex/startex
%{texmfdist}/makeindex/stex
%{texmfdist}/makeindex/xdoc
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/mkindex.1*
%{_mandir}/man1/rumakeindex.1*

%files tlmgr
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tlmgr
%{perl_vendorlib}/TeXLive
%dir %{texmf}/scripts/texlive/lua
%dir %{texmf}/scripts/texlive/lua/texlive
%dir %{texmf}/scripts/texlive/tlmgrgui
%attr(755,root,root) %{texmf}/scripts/texlive/getnonfreefonts.pl
%attr(755,root,root) %{texmf}/scripts/texlive/tlmgr.pl
%attr(755,root,root) %{texmf}/scripts/texlive/test-tlpdb.tlu
%attr(755,root,root) %{texmf}/scripts/texlive/texconf.tlu
%attr(755,root,root) %{texmf}/scripts/texlive/texdoc.tlu
%attr(755,root,root) %{texmf}/scripts/texlive/lua/texlive/*.tlu
%attr(755,root,root) %{texmf}/scripts/texlive/tlmgrgui/*.pl
%dir %{texmf}/scripts/texlive/tlmgrgui/lang
%lang(cs) %{texmf}/scripts/texlive/tlmgrgui/lang/cs
%lang(de) %{texmf}/scripts/texlive/tlmgrgui/lang/de
%{texmf}/scripts/texlive/tlmgrgui/lang/en.sample
%lang(fr) %{texmf}/scripts/texlive/tlmgrgui/lang/fr
%lang(pl) %{texmf}/scripts/texlive/tlmgrgui/lang/pl
%lang(vi) %{texmf}/scripts/texlive/tlmgrgui/lang/vi

%files scripts
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/bengali
%dir %{texmfdist}/scripts/glossaries
%dir %{texmfdist}/scripts/oberdiek
%dir %{texmfdist}/scripts/perltex
%dir %{texmfdist}/scripts/pgfplots
%dir %{texmfdist}/scripts/pst2pdf
%dir %{texmfdist}/scripts/shipunov
%dir %{texmfdist}/scripts/texcount
%dir %{texmfdist}/scripts/vpe
%dir %{texmf}/scripts/a2ping
%dir %{texmf}/scripts/pkfix
%dir %{texmf}/scripts/simpdftex
%dir %{texmf}/scripts/tetex
%attr(755,root,root) %{texmfdist}/scripts/bengali/*
%attr(755,root,root) %{texmfdist}/scripts/glossaries/*
%attr(755,root,root) %{texmfdist}/scripts/oberdiek/*
%attr(755,root,root) %{texmfdist}/scripts/perltex/perltex*
%attr(755,root,root) %{texmfdist}/scripts/pgfplots/*
%attr(755,root,root) %{texmfdist}/scripts/pst2pdf/pst2pdf*
%attr(755,root,root) %{texmfdist}/scripts/shipunov/*
%attr(755,root,root) %{texmfdist}/scripts/texcount/*
%attr(755,root,root) %{texmfdist}/scripts/vpe/vpe.pl
%attr(755,root,root) %{texmf}/scripts/a2ping/a2ping*
%attr(755,root,root) %{texmf}/scripts/pkfix/pkfix*
%attr(755,root,root) %{texmf}/scripts/simpdftex/simpdftex*
%attr(755,root,root) %{texmf}/scripts/tetex/*
%attr(755,root,root) %{_bindir}/a2ping
%attr(755,root,root) %{_bindir}/e2pall
%{_mandir}/man1/e2pall.1*
%dir %{texmf}/texdoc
%doc %{texmf}/doc/texdoc
%attr(755,root,root) %{_bindir}/texdoc
%config(noreplace) %verify(not md5 mtime size) %{texmf}/texdoc/texdoc.cnf

%files tex-arrayjob
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/arrayjob
%{texmfdist}/tex/generic/arrayjob

%files tex-insbox
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/insbox
%{texmfdist}/tex/generic/insbox

%files tex-kastrup
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/kastrup
%{texmfdist}/source/generic/kastrup
%{texmfdist}/tex/generic/kastrup

%files tex-mathdots
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/mathdots
%{texmfdist}/source/generic/mathdots
%{texmfdist}/tex/generic/mathdots

%files tex-ofs
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/ofs
%{texmfdist}/tex/generic/ofs

%files tex-physe
%defattr(644,root,root,755)
%{texmfdist}/tex/physe
%{texmf}/fmtutil/format.physe.cnf
%{fmtdir}/pdftex/physe.fmt

%files tex-velthuis
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/velthuis
%{texmfdist}/tex/generic/velthuis

%files tex-ytex
%defattr(644,root,root,755)
%{texmfdist}/tex/ytex

%files metapost
%defattr(644,root,root,755)
%dir %{texmfdist}/metapost
%doc %{texmfdist}/doc/metapost
%attr(755,root,root) %{_bindir}/mpost
%attr(755,root,root) %{_bindir}/mpto
%{texmfdist}/metapost/base
%{texmfdist}/metapost/config
%{texmfdist}/metapost/mfpic
%{texmfdist}/metapost/misc
%{texmfdist}/metapost/support
%{texmfdist}/source/metapost
%{_mandir}/man1/mpost.1*
%{_mandir}/man1/mpto.1*
%{texmf}/fmtutil/format.metapost.cnf

%files metapost-other
%defattr(644,root,root,755)
%{texmfdist}/metapost/automata
%{texmfdist}/metapost/bbcard
%{texmfdist}/metapost/blockdraw_mp
%{texmfdist}/metapost/bpolynomial
%{texmfdist}/metapost/cmarrows
%{texmfdist}/metapost/dviincl
%{texmfdist}/metapost/epsincl
%{texmfdist}/metapost/expressg
%{texmfdist}/metapost/exteps
%{texmfdist}/metapost/featpost
%{texmfdist}/metapost/frcursive
%{texmfdist}/metapost/hatching
%{texmfdist}/metapost/metaobj
%{texmfdist}/metapost/metaplot
%{texmfdist}/metapost/metauml
%{texmfdist}/metapost/mp3d
%{texmfdist}/metapost/mpattern
%{texmfdist}/metapost/nkarta
%{texmfdist}/metapost/piechartmp
%{texmfdist}/metapost/slideshow
%{texmfdist}/metapost/splines
%{texmfdist}/metapost/tabvar
%{texmfdist}/metapost/textpath
%{texmfdist}/metapost/venn

%files mptopdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mptopdf
%{_mandir}/man1/mptopdf.1*
%{texmfdist}/tex/mptopdf
%{fmtdir}/pdftex/mptopdf.fmt

%files texdoctk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/texdoctk
%{texmf}/texdoctk
%{_mandir}/man1/texdoctk.1*

%files -n texconfig
%defattr(644,root,root,755)
%dir %{texmf}/texconfig
%doc %{texmf}/texconfig/README
%attr(755,root,root) %{_bindir}/texconfig
%attr(755,root,root) %{_bindir}/texconfig-dialog
%attr(755,root,root) %{_bindir}/texconfig-sys
%attr(755,root,root) %{texmf}/texconfig/tcfmgr
%{_mandir}/man1/texconfig.1*
%{_mandir}/man1/texconfig-sys.1*
%{texmf}/texconfig/g
%{texmf}/texconfig/generic
%{texmf}/texconfig/tcfmgr.map
%{texmf}/texconfig/v
%{texmf}/texconfig/x

%if %{with xindy}
%files -n xindy
%defattr(644,root,root,755)
%doc %{texmf}/doc/xindy
%attr(755,root,root) %{_bindir}/tex2xindy
%attr(755,root,root) %{_bindir}/xindy
%attr(755,root,root) %{_bindir}/texindy
%{_libdir}/xindy
%dir %{texmf}/scripts/xindy
%dir %{texmf}/xindy
%dir %{texmf}/xindy/lang
%attr(755,root,root) %{texmf}/scripts/xindy/*
%{texmf}/xindy/base
%{texmf}/xindy/class
%{texmf}/xindy/ord
%{texmf}/xindy/rules
%{texmf}/xindy/styles
%{texmf}/xindy/tex
%{_mandir}/man1/tex2xindy.1*
%{_mandir}/man1/texindy.1*
%{_mandir}/man1/xindy.1*

%files -n xindy-albanian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/albanian

%files -n xindy-belarusian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/belarusian

%files -n xindy-bulgarian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/bulgarian

%files -n xindy-croatian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/croatian

%files -n xindy-czech
%defattr(644,root,root,755)
%{texmf}/xindy/lang/czech

%files -n xindy-danish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/danish

%files -n xindy-dutch
%defattr(644,root,root,755)
%{texmf}/xindy/lang/dutch

%files -n xindy-english
%defattr(644,root,root,755)
%{texmf}/xindy/lang/english

%files -n xindy-esperanto
%defattr(644,root,root,755)
%{texmf}/xindy/lang/esperanto

%files -n xindy-estonian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/estonian

%files -n xindy-finnish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/finnish

%files -n xindy-french
%defattr(644,root,root,755)
%{texmf}/xindy/lang/french

%files -n xindy-general
%defattr(644,root,root,755)
%{texmf}/xindy/lang/general

%files -n xindy-georgian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/georgian

%files -n xindy-german
%defattr(644,root,root,755)
%{texmf}/xindy/lang/german

%files -n xindy-greek
%defattr(644,root,root,755)
%{texmf}/xindy/lang/greek

%files -n xindy-gypsy
%defattr(644,root,root,755)
%{texmf}/xindy/lang/gypsy

%files -n xindy-hausa
%defattr(644,root,root,755)
%{texmf}/xindy/lang/hausa

%files -n xindy-hebrew
%defattr(644,root,root,755)
%{texmf}/xindy/lang/hebrew

%files -n xindy-hungarian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/hungarian

%files -n xindy-icelandic
%defattr(644,root,root,755)
%{texmf}/xindy/lang/icelandic

%files -n xindy-italian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/italian

%files -n xindy-klingon
%defattr(644,root,root,755)
%{texmf}/xindy/lang/klingon

%files -n xindy-kurdish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/kurdish

%files -n xindy-latin
%defattr(644,root,root,755)
%{texmf}/xindy/lang/latin

%files -n xindy-latvian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/latvian

%files -n xindy-lithuanian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/lithuanian

%files -n xindy-lower-sorbian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/lower-sorbian

%files -n xindy-macedonian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/macedonian

%files -n xindy-mongolian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/mongolian

%files -n xindy-norwegian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/norwegian

%files -n xindy-polish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/polish

%files -n xindy-portuguese
%defattr(644,root,root,755)
%{texmf}/xindy/lang/portuguese

%files -n xindy-romanian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/romanian

%files -n xindy-russian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/russian

%files -n xindy-serbian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/serbian

%files -n xindy-slovak
%defattr(644,root,root,755)
%{texmf}/xindy/lang/slovak

%files -n xindy-slovenian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/slovenian

%files -n xindy-spanish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/spanish

%files -n xindy-swedish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/swedish

%files -n xindy-turkish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/turkish

%files -n xindy-ukrainian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/ukrainian

%files -n xindy-upper-sorbian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/upper-sorbian

%files -n xindy-vietnamese
%defattr(644,root,root,755)
%{texmf}/xindy/lang/vietnamese
%endif

%files -n xdvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdvi-xaw
%attr(755,root,root) %{_bindir}/xdvi
%{_mandir}/man1/xdvi.1*
%{_desktopdir}/xdvi.desktop
%{_pixmapsdir}/xdvi.png
%{texmf}/xdvi

%files pdftex
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/pdftexconfig.tex
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/pdftex-dvi.tex
%dir %{texmfdist}/doc/support
%dir %{texmf}/fonts/map/pdftex
%dir %{texmf}/scripts/epstopdf
%doc %{texmfdist}/doc/pdftex
%doc %{texmfdist}/doc/support/pdfcrop
%attr(755,root,root) %{_bindir}/epstopdf
%attr(755,root,root) %{_bindir}/pdfcrop
%attr(755,root,root) %{_bindir}/pdftex
%attr(755,root,root) %{texmf}/scripts/epstopdf/epstopdf*
%{_mandir}/man1/epstopdf.1*
%{_mandir}/man1/pdftex.1*
%{texmfdist}/fonts/enc/pdftex
%{texmfdist}/fonts/map/pdftex
%{texmfdist}/scripts/pdfcrop
%{texmf}/fmtutil/format.pdftex.cnf
%{texmf}/fonts/map/pdftex/updmap
%{fmtdir}/pdftex/pdftex.fmt

%files phyzzx
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/phyzzx
%dir %{texmfdist}/doc/phyzzx
%dir %{texmfdist}/tex/phyzzx
%doc %{texmfdist}/doc/phyzzx/base
%{texmfdist}/tex/phyzzx/base
%{texmfdist}/tex/phyzzx/config
%{texmf}/fmtutil/format.phyzzx.cnf
%{fmtdir}/pdftex/phyzzx.fmt

%files omega
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aleph
%attr(755,root,root) %{_bindir}/lambda
%attr(755,root,root) %{_bindir}/mkocp
%attr(755,root,root) %{_bindir}/mkofm
%attr(755,root,root) %{_bindir}/odvicopy
%attr(755,root,root) %{_bindir}/odvips
%attr(755,root,root) %{_bindir}/odvitype
%attr(755,root,root) %{_bindir}/omega
%attr(755,root,root) %{_bindir}/omfonts
%attr(755,root,root) %{_bindir}/opl2ofm
%attr(755,root,root) %{_bindir}/otangle
%attr(755,root,root) %{_bindir}/otp2ocp
%attr(755,root,root) %{_bindir}/outocp
%attr(755,root,root) %{_bindir}/ovf2ovp
%attr(755,root,root) %{_bindir}/ovp2ovf
%doc %{texmfdist}/doc/aleph
%doc %{texmfdist}/doc/omega
%doc %{texmfdist}/doc/lambda
%{texmfdist}/dvips/omega
%{texmfdist}/omega/ocp/antomega
%{texmfdist}/omega/ocp/char2uni
%{texmfdist}/omega/ocp/ethiop
%{texmfdist}/omega/ocp/misc
%{texmfdist}/omega/ocp/ocherokee
%{texmfdist}/omega/ocp/oinuit
%{texmfdist}/omega/ocp/otibet
%{texmfdist}/omega/ocp/uni2char
%{texmfdist}/omega/otp/antomega
%{texmfdist}/omega/otp/char2uni
%{texmfdist}/omega/otp/ethiop
%{texmfdist}/omega/otp/misc
%{texmfdist}/omega/otp/ocherokee
%{texmfdist}/omega/otp/omega-devanagari
%{texmfdist}/omega/otp/otibet
%{texmfdist}/omega/otp/uni2char
%{texmfdist}/source/lambda
%{texmfdist}/tex/generic/omegahyph
%{texmfdist}/tex/lambda
%{texmf}/fmtutil/format.omega.cnf
%{texmf}/fmtutil/format.aleph.cnf
%{_mandir}/man1/lambda.1*
%{_mandir}/man1/mkocp.1*
%{_mandir}/man1/mkofm.1*
%{_mandir}/man1/omega.1*
%{_mandir}/man1/odvicopy.1*
%{_mandir}/man1/odvips.1*
%{_mandir}/man1/odvitype.1*
%{_mandir}/man1/ofm2opl.1*
%{_mandir}/man1/opl2ofm.1*
%{_mandir}/man1/otp2ocp.1*
%{_mandir}/man1/outocp.1*
%{_mandir}/man1/ovf2ovp.1*
%{_mandir}/man1/ovp2ovf.1*
%dir %{fmtdir}/aleph
%{fmtdir}/aleph/aleph.fmt
%{fmtdir}/aleph/lamed.fmt
%dir %{fmtdir}/omega
%{fmtdir}/omega/lambda.fmt
%{fmtdir}/omega/omega.fmt

%files plain
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/plain
%{texmfdist}/tex/plain/armenian
%{texmfdist}/tex/plain/base
%{texmfdist}/tex/plain/cellular
%dir %{texmfdist}/tex/plain/config
%{texmfdist}/tex/plain/config/aleph.ini
%{texmfdist}/tex/plain/config/bplain.ini
%{texmfdist}/tex/plain/config/etex.ini
%{texmfdist}/tex/plain/config/luatex.ini
%{texmfdist}/tex/plain/config/omega.ini
%{texmfdist}/tex/plain/config/pdfbplain.ini
%{texmfdist}/tex/plain/config/pdfetex.ini
%{texmfdist}/tex/plain/config/pdfluatex.ini
%{texmfdist}/tex/plain/config/pdftexmagfix.tex
%{texmfdist}/tex/plain/config/tex.ini
%{texmfdist}/tex/plain/croatian
%{texmfdist}/tex/plain/cweb
%{texmfdist}/tex/plain/cyrplain
%{texmfdist}/tex/plain/encxvlna
%{texmfdist}/tex/plain/esint-type1
%{texmfdist}/tex/plain/fixpdfmag
%{texmfdist}/tex/plain/fontch
%{texmfdist}/tex/plain/fp
%{texmfdist}/tex/plain/gustlib
%{texmfdist}/tex/plain/harvmac
%{texmfdist}/tex/plain/hyplain
%{texmfdist}/tex/plain/iwona
%{texmfdist}/tex/plain/jsmisc
%{texmfdist}/tex/plain/kdgreek
%{texmfdist}/tex/plain/kurier
%{texmfdist}/tex/plain/levy
%{texmfdist}/tex/plain/metatex
%{texmfdist}/tex/plain/misc
%{texmfdist}/tex/plain/mkpattern
%{texmfdist}/tex/plain/newsletr
%{texmfdist}/tex/plain/pgf
%{texmfdist}/tex/plain/pgfplots
%{texmfdist}/tex/plain/plgraph
%{texmfdist}/tex/plain/plnfss
%{texmfdist}/tex/plain/rsfs
%{texmfdist}/tex/plain/semaphor
%{texmfdist}/tex/plain/treetex
%{texmfdist}/tex/plain/tugboat-plain
%{texmfdist}/tex/plain/typespec
%{texmfdist}/tex/plain/velthuis
%{texmfdist}/tex/plain/vertex
%{texmfdist}/tex/plain/vntex
%{texmfdist}/tex/plain/wasy
%{texmf}/fmtutil/format.tex.cnf

%files mex
%defattr(644,root,root,755)
%dir %{texmfdist}/tex/mex
%dir %{texmfdist}/tex/mex/config
%doc %{texmfdist}/doc/mex
%{texmfdist}/source/mex
%{texmfdist}/tex/mex/base
%{texmf}/fmtutil/format.mex.cnf
%{texmf}/fmtutil/format.utf8mex.cnf

%files format-mex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mex
%{texmfdist}/tex/mex/config/mex.ini
%{fmtdir}/pdftex/mex.fmt

%files format-pdfmex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfmex
%{texmfdist}/tex/mex/config/pdfmex.ini

%files format-utf8mex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/utf8mex
%{texmfdist}/tex/mex/utf8mex

%files amstex
%defattr(644,root,root,755)
%{texmfdist}/tex/amstex
%{texmfdist}/tex/plain/amsfonts

%files format-amstex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/amstex
%doc %{texmfdist}/doc/amstex
%{texmf}/fmtutil/format.amstex.cnf
%{texmf}/fmtutil/format.cyramstex.cnf
%{_mandir}/man1/amstex.1*

%files csplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/csplain
%{texmfdist}/tex/csplain
%{texmf}/fmtutil/format.csplain.cnf

%files format-csplain
%defattr(644,root,root,755)
%{fmtdir}/pdftex/csplain.fmt

%files format-pdfcsplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfcsplain
%{fmtdir}/pdftex/pdfcsplain.fmt

%files cslatex
%defattr(644,root,root,755)
%dir %{texmfdist}/doc/cslatex
%doc %{texmfdist}/doc/cslatex/base
%dir %{texmfdist}/tex/cslatex
%dir %{texmfdist}/tex/cslatex/base
%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/cslatex/base/fonttext.cfg
%{texmfdist}/tex/cslatex/base/cslatex*.ini
%{texmfdist}/tex/cslatex/base/cspsfont.*
%{texmfdist}/tex/cslatex/base/hyphen.cfg
%{texmfdist}/tex/cslatex/base/*.fd
%{texmfdist}/tex/cslatex/base/*.sty
%{texmfdist}/tex/latex/cslatex

%files format-cslatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cslatex
%{texmf}/fmtutil/format.cslatex.cnf

%files format-pdfcslatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfcslatex

%files eplain
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/etex
%doc %{texmfdist}/doc/eplain
%{texmfdist}/tex/plain/etex
%{texmfdist}/tex/eplain
%dir %{texmfdist}/source/eplain
%{texmfdist}/source/eplain/eplain-source-3.2.zip

%files format-eplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eplain
%attr(755,root,root) %{_bindir}/etex
%{_mandir}/man1/eplain.1*
%{_mandir}/man1/etex.1*
%{texmf}/fmtutil/format.eplain.cnf
%{fmtdir}/pdftex/etex.fmt

%files context
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/context
%attr(755,root,root) %{_bindir}/context
%attr(755,root,root) %{_bindir}/ctxtools
%attr(755,root,root) %{_bindir}/exatools
%attr(755,root,root) %{_bindir}/luatools
%attr(755,root,root) %{_bindir}/makempy
%attr(755,root,root) %{_bindir}/mpstools
%attr(755,root,root) %{_bindir}/mtxrun
%attr(755,root,root) %{_bindir}/mtxtools
%attr(755,root,root) %{_bindir}/pdftools
%attr(755,root,root) %{_bindir}/pdftrimwhite
%attr(755,root,root) %{_bindir}/pstopdf
%attr(755,root,root) %{_bindir}/rlxtools
%attr(755,root,root) %{_bindir}/runtools
%attr(755,root,root) %{_bindir}/texexec
%attr(755,root,root) %{_bindir}/texfind
%attr(755,root,root) %{_bindir}/texfont
%attr(755,root,root) %{_bindir}/texmfstart
%attr(755,root,root) %{_bindir}/texshow
%attr(755,root,root) %{_bindir}/textools
%attr(755,root,root) %{_bindir}/texutil
%attr(755,root,root) %{_bindir}/tmftools
%attr(755,root,root) %{_bindir}/xmltools
%{_mandir}/man1/ctxtools.1*
%{_mandir}/man1/pdftools.1*
%{_mandir}/man1/pstopdf.1*
%{_mandir}/man1/texfind.1*
%{_mandir}/man1/texfont.1*
%{_mandir}/man1/texmfstart.1*
%{_mandir}/man1/textools.1*
%{_mandir}/man1/texutil.1*
%{texmfdist}/context
%{texmfdist}/fonts/enc/dvips/context
%{texmfdist}/metapost/context
%{texmfdist}/scripts/context
%{texmfdist}/tex/context
%exclude %{texmfdist}/tex/context/config/cont-de.ini
%exclude %{texmfdist}/tex/context/config/cont-en.ini
%exclude %{texmfdist}/tex/context/config/cont-nl.ini
%exclude %{texmfdist}/tex/context/config/cont-uk.ini
%{texmfdist}/tex/generic/context
%{texmfdist}/tex/latex/context
%{texmfdist}/bibtex/bst/context
%{texmf}/fmtutil/format.context.cnf
%{texmf}/web2c/context.cnf

%files format-context-de
%defattr(644,root,root,755)
%{texmfdist}/tex/context/config/cont-de.ini

%files format-context-en
%defattr(644,root,root,755)
%{texmfdist}/tex/context/config/cont-en.ini
# what is the difference betwen uk and en in this particular situation?
%{texmfdist}/tex/context/config/cont-uk.ini

%files format-context-nl
%defattr(644,root,root,755)
%{texmfdist}/tex/context/config/cont-nl.ini

%files latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lacheck
%attr(755,root,root) %{_bindir}/latex
%attr(755,root,root) %{_bindir}/pslatex
%{_mandir}/man1/lacheck.1*
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pslatex.1*
%dir %{texmfdist}/source/generic
%dir %{texmfdist}/tex/latex
%{texmfdist}/tex/latex/floatflt
%dir %{texmfdist}/tex/latex/latexconfig
%{texmfdist}/tex/generic/shapepar
%{texmfdist}/source/generic/textmerg
%{texmfdist}/tex/generic/textmerg
%{texmfdist}/tex/latex/12many
%{texmfdist}/tex/latex/AkkTeX
%{texmfdist}/tex/latex/GuIT
%{texmfdist}/tex/latex/IEEEtran
%{texmfdist}/tex/latex/Tabbing
%{texmfdist}/tex/latex/a0poster
%{texmfdist}/tex/latex/acmtrans
%{texmfdist}/tex/latex/acronym
%{texmfdist}/tex/latex/adrlist
%{texmfdist}/tex/latex/aeguill
%{texmfdist}/tex/latex/afthesis
%{texmfdist}/tex/latex/aguplus
%{texmfdist}/tex/latex/akletter
%{texmfdist}/tex/latex/algorithm2e
%{texmfdist}/tex/latex/algorithmicx
%{texmfdist}/tex/latex/allrunes
%{texmfdist}/tex/latex/altfont
%{texmfdist}/tex/latex/ametsoc
%{texmfdist}/tex/latex/amsaddr
%{texmfdist}/tex/latex/amsrefs
%{texmfdist}/tex/latex/animate
%{texmfdist}/tex/latex/answers
%{texmfdist}/tex/latex/antiqua
%{texmfdist}/tex/latex/anyfontsize
%{texmfdist}/tex/latex/anysize
%{texmfdist}/tex/latex/apa
%{texmfdist}/tex/latex/apl
%{texmfdist}/tex/latex/ar
%{texmfdist}/tex/latex/arabi
%{texmfdist}/tex/latex/arabtex
%{texmfdist}/tex/latex/archaic
%{texmfdist}/tex/latex/arev
%{texmfdist}/tex/latex/armenian
%{texmfdist}/tex/latex/ascelike
%{texmfdist}/tex/latex/ascii
%{texmfdist}/tex/latex/assignment
%{texmfdist}/tex/latex/augie
%{texmfdist}/tex/latex/auncial-new
%{texmfdist}/tex/latex/aurical
%{texmfdist}/tex/latex/authoraftertitle
%{texmfdist}/tex/latex/authorindex
%{texmfdist}/tex/latex/auto-pst-pdf
%{texmfdist}/tex/latex/autoarea
%{texmfdist}/tex/latex/autotab
%{texmfdist}/tex/latex/avantgar
%{texmfdist}/tex/latex/bangtex
%{texmfdist}/tex/latex/barcodes
%dir %{texmfdist}/tex/latex/base
%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/latex/base/fontmath.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/latex/base/fonttext.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/latex/base/preload.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/latex/base/texsys.cfg
%{texmfdist}/tex/latex/base/*.clo
%{texmfdist}/tex/latex/base/*.cls
%{texmfdist}/tex/latex/base/*.def
%{texmfdist}/tex/latex/base/*.dfu
%{texmfdist}/tex/latex/base/*.fd
%{texmfdist}/tex/latex/base/*.ltx
%{texmfdist}/tex/latex/base/*.sty
%{texmfdist}/tex/latex/base/*.tex
%{texmfdist}/tex/latex/bayer
%{texmfdist}/tex/latex/bbding
%{texmfdist}/tex/latex/bbm-macros
%{texmfdist}/tex/latex/begriff
%{texmfdist}/tex/latex/bengali
%{texmfdist}/tex/latex/bera
%{texmfdist}/tex/latex/betababel
%{texmfdist}/tex/latex/beton
%{texmfdist}/tex/latex/bibarts
%{texmfdist}/tex/latex/bibleref
%{texmfdist}/tex/latex/biblist
%{texmfdist}/tex/latex/bigfoot
%{texmfdist}/tex/latex/bizcard
%{texmfdist}/tex/latex/blacklettert1
%{texmfdist}/tex/latex/blindtext
%{texmfdist}/tex/latex/boisik
%{texmfdist}/tex/latex/boldtensors
%{texmfdist}/tex/latex/bookest
%{texmfdist}/tex/latex/bookhands
%{texmfdist}/tex/latex/bookman
%{texmfdist}/tex/latex/bophook
%{texmfdist}/tex/latex/boxhandler
%{texmfdist}/tex/latex/braille
%{texmfdist}/tex/latex/breakurl
%{texmfdist}/tex/latex/bridge
%{texmfdist}/tex/latex/brushscr
%{texmfdist}/tex/latex/burmese
%{texmfdist}/tex/latex/bussproofs
%{texmfdist}/tex/latex/calrsfs
%{texmfdist}/tex/latex/calxxxx
%{texmfdist}/tex/latex/captcont
%{texmfdist}/tex/latex/casyl
%{texmfdist}/tex/latex/catechis
%{texmfdist}/tex/latex/cbcoptic
%{texmfdist}/tex/latex/cbfonts
%{texmfdist}/tex/latex/cclicenses
%{texmfdist}/tex/latex/cd-cover
%{texmfdist}/tex/latex/cd
%{texmfdist}/tex/latex/cdpbundl
%{texmfdist}/tex/latex/cellspace
%{texmfdist}/tex/latex/changepage
%{texmfdist}/tex/latex/changes
%{texmfdist}/tex/latex/chapterfolder
%{texmfdist}/tex/latex/cherokee
%{texmfdist}/tex/latex/chicago
%{texmfdist}/tex/latex/china2e
%{texmfdist}/tex/latex/citeref
%{texmfdist}/tex/latex/cjhebrew
%dir %{texmfdist}/tex/latex/cjk
%{texmfdist}/tex/latex/cjk/Bg5
%{texmfdist}/tex/latex/cjk/CNS
%{texmfdist}/tex/latex/cjk/GB
%{texmfdist}/tex/latex/cjk/JIS
%{texmfdist}/tex/latex/cjk/KS
%{texmfdist}/tex/latex/cjk/SJIS
%{texmfdist}/tex/latex/cjk/UTF8
%{texmfdist}/tex/latex/cjk/contrib
%{texmfdist}/tex/latex/cjk/mule
%{texmfdist}/tex/latex/cjk/thai
%{texmfdist}/tex/latex/cjk/*.bdg
%{texmfdist}/tex/latex/cjk/*.chr
%{texmfdist}/tex/latex/cjk/*.enc
%{texmfdist}/tex/latex/cjk/*.sty
%{texmfdist}/tex/latex/classicthesis
%{texmfdist}/tex/latex/cleveref
%{texmfdist}/tex/latex/clock
%{texmfdist}/tex/latex/clrscode
%{texmfdist}/tex/latex/cm-lgc
%{texmfdist}/tex/latex/cm-super
%{texmfdist}/tex/latex/cmap
%{texmfdist}/tex/latex/cmcyralt
%{texmfdist}/tex/latex/cmdstring
%{texmfdist}/tex/latex/cmsd
%{texmfdist}/tex/latex/codepage
%{texmfdist}/tex/latex/colorinfo
%{texmfdist}/tex/latex/commath
%{texmfdist}/tex/latex/compactbib
%{texmfdist}/tex/latex/complexity
%{texmfdist}/tex/latex/concprog
%{texmfdist}/tex/latex/confproc
%{texmfdist}/tex/latex/courier-scaled
%{texmfdist}/tex/latex/courier
%{texmfdist}/tex/latex/courseoutline
%{texmfdist}/tex/latex/coursepaper
%{texmfdist}/tex/latex/coverpage
%{texmfdist}/tex/latex/covington
%{texmfdist}/tex/latex/crop
%{texmfdist}/tex/latex/crossreference
%{texmfdist}/tex/latex/csbulletin
%{texmfdist}/tex/latex/csquotes
%{texmfdist}/tex/latex/ctib
%{texmfdist}/tex/latex/cursor
%{texmfdist}/tex/latex/cv
%{texmfdist}/tex/latex/cweb-latex
%{texmfdist}/tex/latex/cyklop
%{texmfdist}/tex/latex/dateiliste
%{texmfdist}/tex/latex/datetime
%{texmfdist}/tex/latex/dcpic
%{texmfdist}/tex/latex/decimal
%{texmfdist}/tex/latex/diagnose
%{texmfdist}/tex/latex/dichokey
%{texmfdist}/tex/latex/dictsym
%{texmfdist}/tex/latex/digiconfigs
%{texmfdist}/tex/latex/dingbat
%{texmfdist}/tex/latex/directory
%{texmfdist}/tex/latex/dlfltxb
%{texmfdist}/tex/latex/docmfp
%{texmfdist}/tex/latex/doi
%{texmfdist}/tex/latex/doipubmed
%{texmfdist}/tex/latex/dotarrow
%{texmfdist}/tex/latex/dottex
%{texmfdist}/tex/latex/doublestroke
%{texmfdist}/tex/latex/dpfloat
%{texmfdist}/tex/latex/drac
%{texmfdist}/tex/latex/draftcopy
%{texmfdist}/tex/latex/dramatist
%{texmfdist}/tex/latex/duerer-latex
%{texmfdist}/tex/latex/dvdcoll
%{texmfdist}/tex/latex/dvipdfmx-def
%{texmfdist}/tex/latex/eCards
%{texmfdist}/tex/latex/ean13isbn
%{texmfdist}/tex/latex/easy
%{texmfdist}/tex/latex/ebezier
%{texmfdist}/tex/latex/ebsthesis
%{texmfdist}/tex/latex/ecclesiastic
%{texmfdist}/tex/latex/ecltree
%{texmfdist}/tex/latex/eco
%{texmfdist}/tex/latex/economic
%{texmfdist}/tex/latex/ed
%{texmfdist}/tex/latex/edmargin
%{texmfdist}/tex/latex/ednotes
%{texmfdist}/tex/latex/eemeir
%{texmfdist}/tex/latex/eepic
%{texmfdist}/tex/latex/egameps
%{texmfdist}/tex/latex/eiad
%{texmfdist}/tex/latex/ellipsis
%{texmfdist}/tex/latex/elpres
%{texmfdist}/tex/latex/elsevier
%{texmfdist}/tex/latex/em
%{texmfdist}/tex/latex/emp
%{texmfdist}/tex/latex/emulateapj
%{texmfdist}/tex/latex/encxvlna
%{texmfdist}/tex/latex/endfloat
%{texmfdist}/tex/latex/endheads
%{texmfdist}/tex/latex/engpron
%{texmfdist}/tex/latex/engrec
%{texmfdist}/tex/latex/envbig
%{texmfdist}/tex/latex/envlab
%{texmfdist}/tex/latex/epigrafica
%{texmfdist}/tex/latex/epigraph
%{texmfdist}/tex/latex/epiolmec
%{texmfdist}/tex/latex/epsdice
%{texmfdist}/tex/latex/epspdfconversion
%{texmfdist}/tex/latex/eqname
%{texmfdist}/tex/latex/eqparbox
%{texmfdist}/tex/latex/errata
%{texmfdist}/tex/latex/eskdx
%{texmfdist}/tex/latex/eso-pic
%{texmfdist}/tex/latex/etex-pkg
%{texmfdist}/tex/latex/ethiop
%{texmfdist}/tex/latex/etoolbox
%{texmfdist}/tex/latex/eukdate
%{texmfdist}/tex/latex/euler
%{texmfdist}/tex/latex/euproposal
%{texmfdist}/tex/latex/euro
%{texmfdist}/tex/latex/eurofont
%{texmfdist}/tex/latex/europecv
%{texmfdist}/tex/latex/eurosans
%{texmfdist}/tex/latex/everypage
%{texmfdist}/tex/latex/examplep
%{texmfdist}/tex/latex/exceltex
%{texmfdist}/tex/latex/exercise
%{texmfdist}/tex/latex/expl3
%{texmfdist}/tex/latex/extarrows
%{texmfdist}/tex/latex/extract
%{texmfdist}/tex/latex/extsizes
%{texmfdist}/tex/latex/facsimile
%{texmfdist}/tex/latex/fancybox
%{texmfdist}/tex/latex/fancyhdr
%{texmfdist}/tex/latex/fancynum
%{texmfdist}/tex/latex/fancyref
%{texmfdist}/tex/latex/fancytooltips
%{texmfdist}/tex/latex/fancyvrb
%{texmfdist}/tex/latex/fax
%{texmfdist}/tex/latex/fc
%{texmfdist}/tex/latex/feyn
%{texmfdist}/tex/latex/fge
%{texmfdist}/tex/latex/figbib
%{texmfdist}/tex/latex/figsize
%{texmfdist}/tex/latex/filecontents
%{texmfdist}/tex/latex/fink
%{texmfdist}/tex/latex/fixfoot
%{texmfdist}/tex/latex/flabels
%{texmfdist}/tex/latex/flacards
%{texmfdist}/tex/latex/flagderiv
%{texmfdist}/tex/latex/flashcards
%{texmfdist}/tex/latex/float
%{texmfdist}/tex/latex/floatrow
%{texmfdist}/tex/latex/fmp
%{texmfdist}/tex/latex/fnbreak
%{texmfdist}/tex/latex/fncychap
%{texmfdist}/tex/latex/foekfont
%{texmfdist}/tex/latex/foilhtml
%{texmfdist}/tex/latex/fonetika
%{texmfdist}/tex/latex/fontinst
%{texmfdist}/tex/latex/fonttable
%{texmfdist}/tex/latex/footmisc
%{texmfdist}/tex/latex/footnpag
%{texmfdist}/tex/latex/fourier
%{texmfdist}/tex/latex/fouriernc
%{texmfdist}/tex/latex/fp
%{texmfdist}/tex/latex/frankenstein
%{texmfdist}/tex/latex/frcursive
%{texmfdist}/tex/latex/frenchle
%{texmfdist}/tex/latex/fribrief
%{texmfdist}/tex/latex/frletter
%{texmfdist}/tex/latex/frontespizio
%{texmfdist}/tex/latex/fullblck
%{texmfdist}/tex/latex/fullpict
%{texmfdist}/tex/latex/fundus
%{texmfdist}/tex/latex/gaceta
%{texmfdist}/tex/latex/gastex
%{texmfdist}/tex/latex/gatech-thesis
%{texmfdist}/tex/latex/gauss
%{texmfdist}/tex/latex/gb4e
%{texmfdist}/tex/latex/gcard
%{texmfdist}/tex/latex/gcite
%{texmfdist}/tex/latex/genmpage
%{texmfdist}/tex/latex/geometry
%{texmfdist}/tex/latex/geomsty
%{texmfdist}/tex/latex/gfsartemisia
%{texmfdist}/tex/latex/gfsbaskerville
%{texmfdist}/tex/latex/gfsbodoni
%{texmfdist}/tex/latex/gfscomplutum
%{texmfdist}/tex/latex/gfsdidot
%{texmfdist}/tex/latex/gfsneohellenic
%{texmfdist}/tex/latex/gfsporson
%{texmfdist}/tex/latex/gfssolomos
%{texmfdist}/tex/latex/gloss
%{texmfdist}/tex/latex/glossaries
%{texmfdist}/tex/latex/gmdoc
%{texmfdist}/tex/latex/gmeometric
%{texmfdist}/tex/latex/gmiflink
%{texmfdist}/tex/latex/gmutils
%{texmfdist}/tex/latex/gmverb
%{texmfdist}/tex/latex/graphics
%{texmfdist}/tex/latex/graphicx-psmin
%{texmfdist}/tex/latex/greek-inputenc
%{texmfdist}/tex/latex/greekdates
%{texmfdist}/tex/latex/greektex
%{texmfdist}/tex/latex/grfpaste
%{texmfdist}/tex/latex/grnumalt
%{texmfdist}/tex/latex/grotesq
%{texmfdist}/tex/latex/grverb
%{texmfdist}/tex/latex/gu
%{texmfdist}/tex/latex/guitbeamer
%{texmfdist}/tex/latex/hanging
%{texmfdist}/tex/latex/har2nat
%{texmfdist}/tex/latex/harmony
%{texmfdist}/tex/latex/harpoon
%{texmfdist}/tex/latex/harvard
%{texmfdist}/tex/latex/hc
%{texmfdist}/tex/latex/helvetic
%{texmfdist}/tex/latex/hep
%{texmfdist}/tex/latex/hepnames
%{texmfdist}/tex/latex/hepparticles
%{texmfdist}/tex/latex/hepthesis
%{texmfdist}/tex/latex/hepunits
%{texmfdist}/tex/latex/hexgame
%{texmfdist}/tex/latex/hfoldsty
%{texmfdist}/tex/latex/hilowres
%{texmfdist}/tex/latex/histogr
%{texmfdist}/tex/latex/hitec
%{texmfdist}/tex/latex/hpsdiss
%{texmfdist}/tex/latex/hvfloat
%{texmfdist}/tex/latex/hypdvips
%{texmfdist}/tex/latex/hyper
%{texmfdist}/tex/latex/hyperref
%{texmfdist}/tex/latex/hyperxmp
%{texmfdist}/tex/latex/hyphenat
%{texmfdist}/tex/latex/ibycus-babel
%{texmfdist}/tex/latex/icsv
%{texmfdist}/tex/latex/ieeepes
%{texmfdist}/tex/latex/ifmslide
%{texmfdist}/tex/latex/ifplatform
%{texmfdist}/tex/latex/ifsym
%{texmfdist}/tex/latex/ijmart
%{texmfdist}/tex/latex/imac
%{texmfdist}/tex/latex/image-gallery
%{texmfdist}/tex/latex/imtekda
%{texmfdist}/tex/latex/index
%{texmfdist}/tex/latex/initials
%{texmfdist}/tex/latex/inlinebib
%{texmfdist}/tex/latex/inlinedef
%{texmfdist}/tex/latex/interactiveworkbook
%{texmfdist}/tex/latex/invoice
%{texmfdist}/tex/latex/ipa
%{texmfdist}/tex/latex/iso
%{texmfdist}/tex/latex/iso10303
%{texmfdist}/tex/latex/isodate
%{texmfdist}/tex/latex/isodoc
%{texmfdist}/tex/latex/isonums
%{texmfdist}/tex/latex/itnumpar
%{texmfdist}/tex/latex/itrans
%{texmfdist}/tex/latex/iwona
%{texmfdist}/tex/latex/jhep
%{texmfdist}/tex/latex/jknapltx
%{texmfdist}/tex/latex/jneurosci
%{texmfdist}/tex/latex/jpsj
%{texmfdist}/tex/latex/jura
%{texmfdist}/tex/latex/juraabbrev
%{texmfdist}/tex/latex/juramisc
%{texmfdist}/tex/latex/jurarsp
%{texmfdist}/tex/latex/koma-script
%{texmfdist}/tex/latex/labels
%{texmfdist}/tex/latex/latexconfig/latex.ini
%{texmfdist}/tex/latex/latexconfig/mllatex.ini
%{texmfdist}/tex/latex/latexconfig/pdflatex.ini
%{texmfdist}/tex/latex/layouts
%{texmfdist}/tex/latex/listings
%{texmfdist}/tex/latex/ltabptch
%{texmfdist}/tex/latex/localloc
%{texmfdist}/tex/latex/ltxmisc
%{texmfdist}/tex/latex/mathcomp
%{texmfdist}/tex/latex/mdwtools
%{texmfdist}/tex/latex/memoir
%{texmfdist}/tex/latex/mh
%{texmfdist}/tex/latex/misc209
%{texmfdist}/tex/latex/mmap
%{texmfdist}/tex/latex/mnsymbol
%{texmfdist}/tex/latex/moderncv
%{texmfdist}/tex/latex/modroman
%{texmfdist}/tex/latex/mongolian-babel
%{texmfdist}/tex/latex/montex
%{texmfdist}/tex/latex/mparhack
%{texmfdist}/tex/latex/ms
%{texmfdist}/tex/latex/multibib
%{texmfdist}/tex/latex/multirow
%{texmfdist}/tex/latex/mwcls
%{texmfdist}/tex/latex/ncclatex
%{texmfdist}/tex/latex/ncctools
%{texmfdist}/tex/latex/ncntrsbk
%{texmfdist}/tex/latex/nddiss
%{texmfdist}/tex/latex/newalg
%{texmfdist}/tex/latex/newfile
%{texmfdist}/tex/latex/newlfm
%{texmfdist}/tex/latex/newspaper
%{texmfdist}/tex/latex/newthm
%{texmfdist}/tex/latex/nomencl
%{texmfdist}/tex/latex/ntgclass
%{texmfdist}/tex/generic/oberdiek
%{texmfdist}/tex/latex/oberdiek
%{texmfdist}/tex/latex/overpic
%{texmfdist}/tex/latex/paralist
%{texmfdist}/tex/latex/pb-diagram
%{texmfdist}/tex/latex/pdftex-def
%{texmfdist}/tex/latex/pdfpages
%{texmfdist}/tex/latex/picinpar
%{texmfdist}/tex/latex/pict2e
%{texmfdist}/tex/latex/placeins
%{texmfdist}/tex/latex/preprint
%{texmfdist}/tex/latex/preview
%{texmfdist}/tex/latex/program
%{texmfdist}/tex/latex/psfrag
%{texmfdist}/tex/latex/pslatex
%{texmfdist}/tex/latex/revtex
%{texmfdist}/tex/latex/rotating
%{texmfdist}/tex/latex/rotfloat
%{texmfdist}/tex/latex/scale
%{texmfdist}/tex/latex/sectsty
%{texmfdist}/tex/latex/seminar
%{texmfdist}/tex/latex/setspace
%{texmfdist}/tex/latex/showdim
%{texmfdist}/tex/latex/showlabels
%{texmfdist}/tex/latex/sidecap
%{texmfdist}/tex/latex/slashbox
%{texmfdist}/tex/latex/soul
%{texmfdist}/tex/latex/stdclsdv
%{texmfdist}/tex/latex/stmaryrd
%{texmfdist}/tex/latex/subfig
%{texmfdist}/tex/latex/subfigure
%{texmfdist}/tex/latex/supertabular
%{texmfdist}/tex/latex/t2
%{texmfdist}/tex/latex/t-angles
%{texmfdist}/tex/latex/tableaux
%{texmfdist}/tex/latex/tablists
%{texmfdist}/tex/latex/tablor
%{texmfdist}/tex/latex/tabto-ltx
%{texmfdist}/tex/latex/tabulary
%{texmfdist}/tex/latex/tabvar
%{texmfdist}/tex/latex/talk
%{texmfdist}/tex/latex/taupin
%{texmfdist}/tex/latex/tcldoc
%{texmfdist}/tex/latex/tdsfrmath
%{texmfdist}/tex/latex/technics
%{texmfdist}/tex/latex/ted
%{texmfdist}/tex/latex/tengwarscript
%{texmfdist}/tex/latex/tensor
%{texmfdist}/tex/latex/teubner
%{texmfdist}/tex/latex/tex-gyre
%{texmfdist}/tex/latex/texilikecover
%{texmfdist}/tex/latex/texlogos
%{texmfdist}/tex/latex/texmate
%{texmfdist}/tex/latex/texpower
%{texmfdist}/tex/latex/texshade
%{texmfdist}/tex/latex/textcase
%{texmfdist}/tex/latex/textfit
%{texmfdist}/tex/latex/textopo
%{texmfdist}/tex/latex/textpath
%{texmfdist}/tex/latex/textpos
%{texmfdist}/tex/latex/theoremref
%{texmfdist}/tex/latex/thesis-titlepage-fhac
%{texmfdist}/tex/latex/thinsp
%{texmfdist}/tex/latex/thmtools
%{texmfdist}/tex/latex/thumb
%{texmfdist}/tex/latex/thuthesis
%{texmfdist}/tex/latex/ticket
%{texmfdist}/tex/latex/tikz-inet
%{texmfdist}/tex/latex/times
%{texmfdist}/tex/latex/timesht
%{texmfdist}/tex/latex/tipa
%{texmfdist}/tex/latex/titlefoot
%{texmfdist}/tex/latex/titlesec
%{texmfdist}/tex/latex/titling
%{texmfdist}/tex/latex/tocbibind
%{texmfdist}/tex/latex/tocloft
%{texmfdist}/tex/latex/tools
%{texmfdist}/tex/latex/totpages
%{texmfdist}/tex/latex/type1cm
%{texmfdist}/tex/latex/undertilde
%{texmfdist}/tex/latex/units
%{texmfdist}/tex/latex/unitsdef
%{texmfdist}/tex/latex/universa
%{texmfdist}/tex/latex/unroman
%{texmfdist}/tex/latex/upmethodology
%{texmfdist}/tex/latex/upquote
%{texmfdist}/tex/latex/varindex
%{texmfdist}/tex/latex/varsfromjobname
%{texmfdist}/tex/latex/vector
%{texmfdist}/tex/latex/velthuis
%{texmfdist}/tex/latex/verse
%{texmfdist}/tex/latex/versions
%{texmfdist}/tex/latex/vhistory
%{texmfdist}/tex/latex/vita
%{texmfdist}/tex/latex/vmargin
%{texmfdist}/tex/latex/volumes
%{texmfdist}/tex/latex/vpe
%{texmfdist}/tex/latex/vrsion
%{texmfdist}/tex/latex/vwcol
%{texmfdist}/tex/latex/vxu
%{texmfdist}/tex/latex/wallpaper
%{texmfdist}/tex/latex/warning
%{texmfdist}/tex/latex/warpcol
%{texmfdist}/tex/latex/was
%{texmfdist}/tex/latex/williams
%{texmfdist}/tex/latex/wnri
%{texmfdist}/tex/latex/wordlike
%{texmfdist}/source/wordlike
%{texmfdist}/tex/latex/wrapfig
%{texmfdist}/tex/latex/wsuipa
%{texmfdist}/source/generic/wsuipa
%{texmfdist}/tex/latex/xargs
%{texmfdist}/tex/latex/xcolor
%{texmfdist}/tex/latex/xdoc
%{texmfdist}/tex/latex/xfor
%{texmfdist}/tex/latex/xifthen
%{texmfdist}/tex/latex/xmpincl
%{texmfdist}/tex/latex/xnewcommand
%{texmfdist}/tex/latex/xoptarg
%{texmfdist}/tex/latex/xpackages
%{texmfdist}/tex/latex/xq
%{texmfdist}/tex/latex/xskak
%{texmfdist}/tex/latex/xstring
%{texmfdist}/tex/latex/xtab
%{texmfdist}/tex/latex/xtcapts
%{texmfdist}/tex/latex/xyling
%{texmfdist}/tex/latex/xytree
%{texmfdist}/tex/latex/yafoot
%{texmfdist}/tex/latex/yfonts
%{texmfdist}/tex/latex/yhmath
%{texmfdist}/tex/latex/yi4latex
%{texmfdist}/tex/latex/york-thesis
%{texmfdist}/tex/latex/youngtab
%{texmfdist}/tex/latex/yplan
%{texmfdist}/tex/latex/zapfchan
%{texmfdist}/tex/latex/zapfding
%{texmfdist}/tex/latex/zed-csp
%{texmfdist}/tex/latex/zefonts
%{texmfdist}/tex/latex/ziffer
%{texmfdist}/tex/latex/zwgetfdate
%{texmf}/fmtutil/format.latex.cnf
%dir %{texmf}/tex/latex
%{texmf}/tex/latex/config
%{texmf}/tex/latex/dvipdfm
%dir %{texmf}/tex/latex/misc
%{fmtdir}/pdftex/latex.fmt
%{fmtdir}/pdftex/mllatex.fmt

%files latex-12many
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/12many
%{texmfdist}/source/latex/12many

%files latex-abstract
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/abstract
%{texmfdist}/tex/latex/abstract
%{texmfdist}/source/latex/abstract

%files latex-accfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/accfonts
%{texmfdist}/tex/latex/accfonts

%files latex-adrconv
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/adrconv
%{texmfdist}/doc/latex/adrconv

%files latex-algorithms
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/algorithms
%{texmfdist}/tex/latex/algorithms

%files latex-ae
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/ae

%files latex-ams
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/amsfonts
%doc %{texmfdist}/doc/latex/amscls
%doc %{texmfdist}/doc/latex/amsmath
%doc %{texmfdist}/doc/latex/onlyamsmath
%{texmfdist}/tex/latex/amscls
%{texmfdist}/tex/latex/amsmath
%{texmfdist}/tex/latex/amsfonts
%{texmfdist}/tex/latex/onlyamsmath
%{texmfdist}/source/latex/onlyamsmath
%{texmfdist}/source/latex/amsaddr
%{texmfdist}/source/latex/amscls
%{texmfdist}/source/latex/amsfonts
%{texmfdist}/source/latex/amsmath
%{texmfdist}/source/latex/amsrefs

%files latex-antp
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/antp

%files latex-antt
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/antt

%files latex-appendix
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/appendix
%{texmfdist}/tex/latex/appendix
%{texmfdist}/source/latex/appendix

%files latex-bardiag
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bardiag
%{texmfdist}/tex/latex/bardiag

%files latex-bbm
%defattr(644,root,root,755)
%{texmfdist}/source/latex/bbm
%{texmfdist}/tex/latex/bbm

%files latex-bbold
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bbold
%{texmfdist}/tex/latex/bbold
%{texmfdist}/source/latex/bbold

%files latex-beamer
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/beamer
%{texmfdist}/tex/latex/beamer-contrib
%{texmfdist}/tex/latex/beamer

%files latex-bezos
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bezos
%{texmfdist}/tex/latex/bezos

%files latex-bibtex
%defattr(644,root,root,755)
%dir %{texmfdist}/bibtex
%dir %{texmfdist}/bibtex/bib
%dir %{texmfdist}/bibtex/bst
%dir %{texmfdist}/bibtex/csf
%dir %{texmfdist}/doc/bibtex
%dir %{texmf}/bibtex
%doc %{texmfdist}/doc/bibtex/base
%doc %{texmfdist}/doc/latex/bibtopic
%doc %{texmfdist}/doc/latex/bibunits
%doc %{texmfdist}/doc/latex/footbib
%doc %{texmfdist}/doc/latex/natbib
%doc %{texmf}/doc/bibtex8
%{_mandir}/man1/bibtex.1*
%{_mandir}/man1/rubibtex.1*

%attr(755,root,root) %{_bindir}/bibtex
%attr(755,root,root) %{_bindir}/rubibtex
%{texmfdist}/bibtex/bib/adrconv
%{texmfdist}/bibtex/bib/base
%{texmfdist}/bibtex/bst/adrconv
%{texmfdist}/bibtex/bst/base
%{texmfdist}/bibtex/bst/natbib
%{texmfdist}/bibtex/csf/base
%{texmfdist}/source/latex/adrconv
%{texmfdist}/source/latex/bibtopic
%{texmfdist}/source/latex/bibunits
%{texmfdist}/source/latex/footbib
%{texmfdist}/tex/latex/bibtopic
%{texmfdist}/tex/latex/bibunits
%{texmfdist}/tex/latex/footbib
%{texmfdist}/tex/latex/natbib
%{texmf}/bibtex/csf

%files latex-bibtex-ams
%defattr(644,root,root,755)
%{texmfdist}/bibtex/bst/ams
%{texmfdist}/bibtex/bib/ams

%files latex-bibtex-pl
%defattr(644,root,root,755)
%dir %{texmfdist}/bibtex/bib/gustlib
%{texmfdist}/bibtex/bib/gustlib/plbib.bib

%files latex-bibtex-german
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/bibtex/germbib
%{texmfdist}/bibtex/bst/germbib
%{texmfdist}/tex/latex/germbib

%files latex-bibtex-revtex4
%defattr(644,root,root,755)
%{texmfdist}/bibtex/bib/revtex
%{texmfdist}/bibtex/bst/revtex

%files latex-bibtex-jurabib
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/jurabib
%{texmfdist}/bibtex/bst/jurabib
%{texmfdist}/bibtex/bib/jurabib
%{texmfdist}/source/latex/jurabib
%{texmfdist}/tex/latex/jurabib

%files latex-bibtex-dk
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/dk-bib
%{texmfdist}/bibtex/bst/dk-bib
%{texmfdist}/bibtex/csf/dk-bib
%{texmfdist}/bibtex/bib/dk-bib
%{texmfdist}/source/latex/dk-bib
%{texmfdist}/tex/latex/dk-bib

%files latex-bibtex-styles
%defattr(644,root,root,755)
%dir %{texmfdist}/source/bibtex
%doc %{texmfdist}/doc/bibtex/abstyles
%doc %{texmfdist}/doc/bibtex/bibhtml
%doc %{texmfdist}/doc/bibtex/dinat
%doc %{texmfdist}/doc/bibtex/economic
%doc %{texmfdist}/doc/bibtex/elsevier-bib
%doc %{texmfdist}/doc/bibtex/gost
%doc %{texmfdist}/doc/bibtex/ijqc
%doc %{texmfdist}/doc/bibtex/iopart-num
%doc %{texmfdist}/doc/generic/t2
%doc %{texmfdist}/doc/latex/IEEEtran
%{texmfdist}/bibtex/bib/IEEEtran
%{texmfdist}/bibtex/bib/abstyles
%{texmfdist}/bibtex/bib/achemso
%{texmfdist}/bibtex/bib/acmtrans
%{texmfdist}/bibtex/bib/ascelike
%{texmfdist}/bibtex/bib/beebe
%{texmfdist}/bibtex/bib/bibhtml
%{texmfdist}/bibtex/bib/bibtopic
%{texmfdist}/bibtex/bib/din1505
%{texmfdist}/bibtex/bib/directory
%{texmfdist}/bibtex/bib/figbib
%{texmfdist}/bibtex/bib/frankenstein
%{texmfdist}/bibtex/bib/gatech-thesis
%{texmfdist}/bibtex/bib/geomsty
%{texmfdist}/bibtex/bib/gloss
%{texmfdist}/bibtex/bib/harvard
%{texmfdist}/bibtex/bib/ieeepes
%{texmfdist}/bibtex/bib/ijmart
%{texmfdist}/bibtex/bib/imac
%{texmfdist}/bibtex/bib/index
%{texmfdist}/bibtex/bib/lsc
%{texmfdist}/bibtex/bib/msc
%{texmfdist}/bibtex/bib/nostarch
%{texmfdist}/bibtex/bib/spie
%{texmfdist}/bibtex/bib/urlbst
%{texmfdist}/bibtex/bst/IEEEtran
%{texmfdist}/bibtex/bst/abstyles
%{texmfdist}/bibtex/bst/achemso
%{texmfdist}/bibtex/bst/acmtrans
%{texmfdist}/bibtex/bst/afthesis
%{texmfdist}/bibtex/bst/aguplus
%{texmfdist}/bibtex/bst/aichej
%{texmfdist}/bibtex/bst/ametsoc
%{texmfdist}/bibtex/bst/ascelike
%{texmfdist}/bibtex/bst/beebe
%{texmfdist}/bibtex/bst/bibhtml
%{texmfdist}/bibtex/bst/chem-journal
%{texmfdist}/bibtex/bst/chicago
%{texmfdist}/bibtex/bst/confproc
%{texmfdist}/bibtex/bst/datatool
%{texmfdist}/bibtex/bst/din1505
%{texmfdist}/bibtex/bst/dinat
%{texmfdist}/bibtex/bst/directory
%{texmfdist}/bibtex/bst/dvdcoll
%{texmfdist}/bibtex/bst/economic
%{texmfdist}/bibtex/bst/elsevier-bib
%{texmfdist}/bibtex/bst/fbs
%{texmfdist}/bibtex/bst/figbib
%{texmfdist}/bibtex/bst/finbib
%{texmfdist}/bibtex/bst/frankenstein
%{texmfdist}/bibtex/bst/gatech-thesis
%{texmfdist}/bibtex/bst/gloss
%{texmfdist}/bibtex/bst/gost
%{texmfdist}/bibtex/bst/gustlib
%{texmfdist}/bibtex/bst/harvard
%{texmfdist}/bibtex/bst/hc
%{texmfdist}/bibtex/bst/ieeepes
%{texmfdist}/bibtex/bst/ijmart
%{texmfdist}/bibtex/bst/ijqc
%{texmfdist}/bibtex/bst/imac
%{texmfdist}/bibtex/bst/index
%{texmfdist}/bibtex/bst/inlinebib
%{texmfdist}/bibtex/bst/iopart-num
%{texmfdist}/bibtex/bst/jneurosci
%{texmfdist}/bibtex/bst/jurarsp
%{texmfdist}/bibtex/bst/kluwer
%{texmfdist}/bibtex/bst/mslapa
%{texmfdist}/bibtex/bst/multibib
%{texmfdist}/bibtex/bst/munich
%{texmfdist}/bibtex/bst/nature
%{texmfdist}/bibtex/bst/nddiss
%{texmfdist}/bibtex/bst/opcit
%{texmfdist}/bibtex/bst/perception
%{texmfdist}/bibtex/bst/savetrees
%{texmfdist}/bibtex/bst/shipunov
%{texmfdist}/bibtex/bst/smflatex
%{texmfdist}/bibtex/bst/sort-by-letters
%{texmfdist}/bibtex/bst/spie
%{texmfdist}/bibtex/bst/stellenbosch
%{texmfdist}/bibtex/bst/swebib
%{texmfdist}/bibtex/bst/texsis
%{texmfdist}/bibtex/bst/thuthesis
%{texmfdist}/bibtex/bst/tugboat
%{texmfdist}/bibtex/bst/urlbst
%{texmfdist}/bibtex/csf/gost
%{texmfdist}/source/bibtex/gost

%files latex-bibtex-vancouver
%defattr(644,root,root,755)
%dir %{texmfdist}/bibtex/bib/vancouver
%dir %{texmfdist}/bibtex/bst/vancouver
%dir %{texmfdist}/doc/bibtex/vancouver
%doc %{texmfdist}/doc/bibtex/vancouver/README
%doc %{texmfdist}/doc/bibtex/vancouver/vancouver.pdf
%doc %{texmfdist}/doc/bibtex/vancouver/vancouver.tex
%{texmfdist}/bibtex/bib/vancouver/vancouver.bib
%{texmfdist}/bibtex/bst/vancouver/vancouver.bst

%files latex-booktabs
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/booktabs
%{texmfdist}/source/latex/booktabs
%{texmfdist}/tex/latex/booktabs

%files latex-caption
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/caption
%{texmfdist}/tex/latex/caption
%{texmfdist}/source/latex/caption

%files latex-carlisle
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/carlisle
%{texmfdist}/tex/latex/carlisle
%{texmfdist}/source/latex/carlisle

%files latex-ccfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ccfonts
%{texmfdist}/source/latex/ccfonts
%{texmfdist}/tex/latex/ccfonts

%files latex-cite
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/cite

%files latex-cmbright
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/cmbright
%{texmfdist}/tex/latex/cmbright

%files latex-colortab
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/colortab
%{texmfdist}/tex/latex/colortab
%{texmfdist}/tex/generic/colortab

%files latex-comment
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/comment
%{texmfdist}/source/latex/comment
%{texmfdist}/tex/latex/comment

%files latex-concmath
%defattr(644,root,root,755)
%{texmfdist}/source/latex/concmath
%{texmfdist}/tex/latex/concmath

%files latex-currvita
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/currvita
%{texmfdist}/source/latex/currvita
%{texmfdist}/tex/latex/currvita
%doc %{texmfdist}/doc/latex/curve
%{texmfdist}/source/latex/curve
%{texmfdist}/tex/latex/curve
%doc %{texmfdist}/doc/latex/ecv
%{texmfdist}/source/latex/ecv
%{texmfdist}/tex/latex/ecv
%doc %{texmfdist}/doc/latex/simplecv
%{texmfdist}/source/latex/simplecv
%{texmfdist}/tex/latex/simplecv

%files latex-curves
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/curves
%{texmfdist}/source/latex/curves
%{texmfdist}/tex/latex/curves

%files latex-custom-bib
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/custom-bib
%{texmfdist}/source/latex/custom-bib
%{texmfdist}/tex/latex/custom-bib

%files latex-cyrillic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/cyrillic
%{texmfdist}/source/latex/cyrillic
%{texmfdist}/tex/latex/cyrillic

%files latex-enumitem
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/enumitem
%{texmfdist}/tex/latex/enumitem

%files latex-exams
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/exam
%doc %{texmfdist}/doc/latex/examdesign
%doc %{texmfdist}/doc/latex/mathexam
%doc %{texmfdist}/doc/latex/probsoln
%doc %{texmfdist}/doc/latex/qcm
%doc %{texmfdist}/doc/latex/uebungsblatt
%{texmfdist}/source/latex/examdesign
%{texmfdist}/source/latex/mathexam
%{texmfdist}/source/latex/probsoln
%{texmfdist}/source/latex/qcm
%{texmfdist}/tex/latex/exam
%{texmfdist}/tex/latex/examdesign
%{texmfdist}/tex/latex/mathexam
%{texmfdist}/tex/latex/probsoln
%{texmfdist}/tex/latex/qcm
%{texmfdist}/tex/latex/uebungsblatt

%files latex-float
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ccaption
%doc %{texmfdist}/doc/latex/photo
%doc %{texmfdist}/doc/latex/topfloat
%{texmfdist}/source/latex/ccaption
%{texmfdist}/source/latex/photo
%{texmfdist}/tex/latex/ccaption
%{texmfdist}/tex/latex/photo
%{texmfdist}/tex/latex/topfloat

%files latex-foiltex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/foiltex
%{texmfdist}/tex/latex/foiltex

%files latex-formlett
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/formlett
%{texmfdist}/tex/latex/formlett

%files latex-formular
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/formular
%{texmfdist}/tex/latex/formular
%{texmfdist}/source/latex/formular

%files latex-gbrief
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/g-brief
%{texmfdist}/source/latex/g-brief
%{texmfdist}/tex/latex/g-brief

%files latex-keystroke
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/keystroke
%doc %{texmfdist}/doc/latex/keystroke

%files latex-labbook
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/labbook
%{texmfdist}/source/latex/labbook
%{texmfdist}/tex/latex/labbook

%files latex-lastpage
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lastpage
%{texmfdist}/tex/latex/lastpage
%{texmfdist}/source/latex/lastpage

%files latex-lcd
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lcd
%{texmfdist}/source/latex/lcd
%{texmfdist}/tex/latex/lcd

%files latex-leaflet
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/leaflet
%{texmfdist}/source/latex/leaflet
%{texmfdist}/tex/latex/leaflet

%files latex-leftidx
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/leftidx
%{texmfdist}/tex/latex/leftidx
%{texmfdist}/source/latex/leftidx

%files latex-lewis
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lewis
%{texmfdist}/tex/latex/lewis

%files latex-lm
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/lm

%files latex-lucidabr
%defattr(644,root,root,755)
%dir %{texmfdist}/vtex
%{texmfdist}/vtex/config

%files latex-lineno
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lineno
%{texmfdist}/tex/latex/lineno

%files latex-metre
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/metre
%{texmfdist}/source/latex/metre
%{texmfdist}/tex/latex/metre

%files latex-marvosym
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/marvosym
%{texmfdist}/tex/latex/marvosym

%files latex-microtype
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/microtype
%{texmfdist}/source/latex/microtype
%{texmfdist}/tex/latex/microtype

%files latex-misc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/fixme
%{texmfdist}/source/latex/fixme
%{texmfdist}/tex/latex/fixme
%doc %{texmfdist}/doc/latex/recipecard
%{texmfdist}/source/latex/recipecard
%{texmfdist}/tex/latex/recipecard
%doc %{texmfdist}/doc/latex/cooking
%{texmfdist}/source/latex/cooking
%{texmfdist}/tex/latex/cooking
%doc %{texmfdist}/doc/latex/cuisine
%{texmfdist}/source/latex/cuisine
%{texmfdist}/tex/latex/cuisine
%doc %{texmfdist}/doc/latex/todo
%{texmfdist}/source/latex/todo
%{texmfdist}/tex/latex/todo

%files latex-mflogo
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/mflogo
%{texmfdist}/source/latex/mflogo
%{texmfdist}/tex/latex/mflogo

%files latex-mfnfss
%defattr(644,root,root,755)
%{texmfdist}/source/latex/mfnfss
%{texmfdist}/tex/latex/mfnfss

%files latex-minitoc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/minitoc
%{texmfdist}/bibtex/bst/minitoc
%{texmfdist}/makeindex/minitoc
%{texmfdist}/scripts/minitoc
%{texmfdist}/source/latex/minitoc
%{texmfdist}/tex/latex/minitoc

%files latex-mltex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/mltex
%{texmfdist}/tex/latex/mltex
%dir %{texmfdist}/tex/mltex
%{texmfdist}/tex/mltex/config

%files latex-moreverb
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/moreverb
%{texmfdist}/tex/latex/moreverb
%{texmfdist}/source/latex/moreverb

%files latex-multienum
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/multenum
%dir %{texmfdist}/tex/latex/multenum
%{texmfdist}/tex/latex/multenum/*

%files latex-musictex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/musictex
%{texmfdist}/fonts/source/public/musictex
%{texmfdist}/fonts/tfm/public/musictex
%{texmfdist}/tex/generic/musictex
%{texmfdist}/tex/latex/musictex

%files latex-ntheorem
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ntheorem
%{texmfdist}/tex/latex/ntheorem
%{texmfdist}/source/latex/ntheorem

%files latex-other-doc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/alatex
%doc %{texmfdist}/doc/generic/wsuipa
%doc %{texmfdist}/doc/latex/ANUfinalexam
%doc %{texmfdist}/doc/latex/AkkTeX
%doc %{texmfdist}/doc/latex/GuIT
%doc %{texmfdist}/doc/latex/a0poster
%doc %{texmfdist}/doc/latex/acmtrans
%doc %{texmfdist}/doc/latex/adrlist
%doc %{texmfdist}/doc/latex/afthesis
%doc %{texmfdist}/doc/latex/aguplus
%doc %{texmfdist}/doc/latex/akletter
%doc %{texmfdist}/doc/latex/algorithm2e
%doc %{texmfdist}/doc/latex/algorithmicx
%doc %{texmfdist}/doc/latex/altfont
%doc %{texmfdist}/doc/latex/ametsoc
%doc %{texmfdist}/doc/latex/amsaddr
%doc %{texmfdist}/doc/latex/amsrefs
%doc %{texmfdist}/doc/latex/animate
%doc %{texmfdist}/doc/latex/answers
%doc %{texmfdist}/doc/latex/anyfontsize
%doc %{texmfdist}/doc/latex/apa
%doc %{texmfdist}/doc/latex/ar
%doc %{texmfdist}/doc/latex/arabi
%doc %{texmfdist}/doc/latex/arabtex
%doc %{texmfdist}/doc/latex/ascelike
%doc %{texmfdist}/doc/latex/assignment
%doc %{texmfdist}/doc/latex/augie
%doc %{texmfdist}/doc/latex/aurical
%doc %{texmfdist}/doc/latex/authorindex
%doc %{texmfdist}/doc/latex/autoarea
%doc %{texmfdist}/doc/latex/autotab
%doc %{texmfdist}/doc/latex/bangtex
%doc %{texmfdist}/doc/latex/barcodes
%doc %{texmfdist}/doc/latex/bayer
%doc %{texmfdist}/doc/latex/bbm-macros
%doc %{texmfdist}/doc/latex/beamer-contrib
%doc %{texmfdist}/doc/latex/begriff
%doc %{texmfdist}/doc/latex/betababel
%doc %{texmfdist}/doc/latex/bibarts
%doc %{texmfdist}/doc/latex/bibleref
%doc %{texmfdist}/doc/latex/biblist
%doc %{texmfdist}/doc/latex/bigfoot
%doc %{texmfdist}/doc/latex/bizcard
%doc %{texmfdist}/doc/latex/blindtext
%doc %{texmfdist}/doc/latex/boldtensors
%doc %{texmfdist}/doc/latex/bookest
%doc %{texmfdist}/doc/latex/boxhandler
%doc %{texmfdist}/doc/latex/braille
%doc %{texmfdist}/doc/latex/breakurl
%doc %{texmfdist}/doc/latex/brushscr
%doc %{texmfdist}/doc/latex/bussproofs
%doc %{texmfdist}/doc/latex/calxxxx
%doc %{texmfdist}/doc/latex/captcont
%doc %{texmfdist}/doc/latex/casyl
%doc %{texmfdist}/doc/latex/catechis
%doc %{texmfdist}/doc/latex/cbcoptic
%doc %{texmfdist}/doc/latex/cclicenses
%doc %{texmfdist}/doc/latex/cd-cover
%doc %{texmfdist}/doc/latex/cd
%doc %{texmfdist}/doc/latex/cdpbundl
%doc %{texmfdist}/doc/latex/cellspace
%doc %{texmfdist}/doc/latex/changes
%doc %{texmfdist}/doc/latex/chapterfolder
%doc %{texmfdist}/doc/latex/china2e
%doc %{texmfdist}/doc/latex/cite
%doc %{texmfdist}/doc/latex/classicthesis
%doc %{texmfdist}/doc/latex/cleveref
%doc %{texmfdist}/doc/latex/clock
%doc %{texmfdist}/doc/latex/clrscode
%doc %{texmfdist}/doc/latex/cm-lgc
%doc %{texmfdist}/doc/latex/cmap
%doc %{texmfdist}/doc/latex/cmcyralt
%doc %{texmfdist}/doc/latex/cmdstring
%doc %{texmfdist}/doc/latex/codepage
%doc %{texmfdist}/doc/latex/colorinfo
%doc %{texmfdist}/doc/latex/commath
%doc %{texmfdist}/doc/latex/complexity
%doc %{texmfdist}/doc/latex/concprog
%doc %{texmfdist}/doc/latex/confproc
%doc %{texmfdist}/doc/latex/courier-scaled
%doc %{texmfdist}/doc/latex/courseoutline
%doc %{texmfdist}/doc/latex/coursepaper
%doc %{texmfdist}/doc/latex/coverpage
%doc %{texmfdist}/doc/latex/covington
%doc %{texmfdist}/doc/latex/crossreference
%doc %{texmfdist}/doc/latex/cryst
%doc %{texmfdist}/doc/latex/csbulletin
%doc %{texmfdist}/doc/latex/csquotes
%doc %{texmfdist}/doc/latex/ctib
%doc %{texmfdist}/doc/latex/cursor
%doc %{texmfdist}/doc/latex/cv
%doc %{texmfdist}/doc/latex/cweb-latex
%doc %{texmfdist}/doc/latex/dateiliste
%doc %{texmfdist}/doc/latex/datetime
%doc %{texmfdist}/doc/latex/dcpic
%doc %{texmfdist}/doc/latex/diagnose
%doc %{texmfdist}/doc/latex/dichokey
%doc %{texmfdist}/doc/latex/digiconfigs
%doc %{texmfdist}/doc/latex/din1505
%doc %{texmfdist}/doc/latex/directory
%doc %{texmfdist}/doc/latex/dlfltxb
%doc %{texmfdist}/doc/latex/docmfp
%doc %{texmfdist}/doc/latex/doi
%doc %{texmfdist}/doc/latex/doipubmed
%doc %{texmfdist}/doc/latex/dotarrow
%doc %{texmfdist}/doc/latex/dottex
%doc %{texmfdist}/doc/latex/dpfloat
%doc %{texmfdist}/doc/latex/drac
%doc %{texmfdist}/doc/latex/dramatist
%doc %{texmfdist}/doc/latex/dtxgallery
%doc %{texmfdist}/doc/latex/duerer-latex
%doc %{texmfdist}/doc/latex/dvdcoll
%doc %{texmfdist}/doc/latex/eCards
%doc %{texmfdist}/doc/latex/ean13isbn
%doc %{texmfdist}/doc/latex/easy
%doc %{texmfdist}/doc/latex/ebezier
%doc %{texmfdist}/doc/latex/ebong
%doc %{texmfdist}/doc/latex/ebsthesis
%doc %{texmfdist}/doc/latex/ecclesiastic
%doc %{texmfdist}/doc/latex/ecltree
%doc %{texmfdist}/doc/latex/ed
%doc %{texmfdist}/doc/latex/edmac
%doc %{texmfdist}/doc/latex/edmargin
%doc %{texmfdist}/doc/latex/ednotes
%doc %{texmfdist}/doc/latex/eemeir
%doc %{texmfdist}/doc/latex/egameps
%doc %{texmfdist}/doc/latex/ellipsis
%doc %{texmfdist}/doc/latex/elpres
%doc %{texmfdist}/doc/latex/elsevier
%doc %{texmfdist}/doc/latex/em
%doc %{texmfdist}/doc/latex/emp
%doc %{texmfdist}/doc/latex/emulateapj
%doc %{texmfdist}/doc/latex/endheads
%doc %{texmfdist}/doc/latex/engpron
%doc %{texmfdist}/doc/latex/engrec
%doc %{texmfdist}/doc/latex/envlab
%doc %{texmfdist}/doc/latex/epigraph
%doc %{texmfdist}/doc/latex/epiolmec
%doc %{texmfdist}/doc/latex/epsdice
%doc %{texmfdist}/doc/latex/epspdfconversion
%doc %{texmfdist}/doc/latex/eqparbox
%doc %{texmfdist}/doc/latex/errata
%doc %{texmfdist}/doc/latex/eskdx
%doc %{texmfdist}/doc/latex/etex-pkg
%doc %{texmfdist}/doc/latex/ethiop-t1
%doc %{texmfdist}/doc/latex/ethiop
%doc %{texmfdist}/doc/latex/etoolbox
%doc %{texmfdist}/doc/latex/eukdate
%doc %{texmfdist}/doc/latex/euproposal
%doc %{texmfdist}/doc/latex/euro
%doc %{texmfdist}/doc/latex/europecv
%doc %{texmfdist}/doc/latex/eurosans
%doc %{texmfdist}/doc/latex/everypage
%doc %{texmfdist}/doc/latex/examplep
%doc %{texmfdist}/doc/latex/exceltex
%doc %{texmfdist}/doc/latex/exercise
%doc %{texmfdist}/doc/latex/expl3
%doc %{texmfdist}/doc/latex/extarrows
%doc %{texmfdist}/doc/latex/extract
%doc %{texmfdist}/doc/latex/facsimile
%doc %{texmfdist}/doc/latex/fancynum
%doc %{texmfdist}/doc/latex/fancyref
%doc %{texmfdist}/doc/latex/fancytooltips
%doc %{texmfdist}/doc/latex/fax
%doc %{texmfdist}/doc/latex/figbib
%doc %{texmfdist}/doc/latex/figsize
%doc %{texmfdist}/doc/latex/fink
%doc %{texmfdist}/doc/latex/fixfoot
%doc %{texmfdist}/doc/latex/flabels
%doc %{texmfdist}/doc/latex/flacards
%doc %{texmfdist}/doc/latex/flagderiv
%doc %{texmfdist}/doc/latex/flashcards
%doc %{texmfdist}/doc/latex/floatrow
%doc %{texmfdist}/doc/latex/fmp
%doc %{texmfdist}/doc/latex/fnbreak
%doc %{texmfdist}/doc/latex/fncychap
%doc %{texmfdist}/doc/latex/foekfont
%doc %{texmfdist}/doc/latex/fonttable
%doc %{texmfdist}/doc/latex/frankenstein
%doc %{texmfdist}/doc/latex/frenchle
%doc %{texmfdist}/doc/latex/fribrief
%doc %{texmfdist}/doc/latex/frletter
%doc %{texmfdist}/doc/latex/frontespizio
%doc %{texmfdist}/doc/latex/fullblck
%doc %{texmfdist}/doc/latex/fullpict
%doc %{texmfdist}/doc/latex/fundus
%doc %{texmfdist}/doc/latex/gaceta
%doc %{texmfdist}/doc/latex/gastex
%doc %{texmfdist}/doc/latex/gatech-thesis
%doc %{texmfdist}/doc/latex/gauss
%doc %{texmfdist}/doc/latex/gb4e
%doc %{texmfdist}/doc/latex/gcard
%doc %{texmfdist}/doc/latex/gcite
%doc %{texmfdist}/doc/latex/genmpage
%doc %{texmfdist}/doc/latex/geomsty
%doc %{texmfdist}/doc/latex/gloss
%doc %{texmfdist}/doc/latex/glossaries
%doc %{texmfdist}/doc/latex/gmdoc
%doc %{texmfdist}/doc/latex/gmeometric
%doc %{texmfdist}/doc/latex/gmiflink
%doc %{texmfdist}/doc/latex/gmutils
%doc %{texmfdist}/doc/latex/gmverb
%doc %{texmfdist}/doc/latex/graphicx-psmin
%doc %{texmfdist}/doc/latex/greek-inputenc
%doc %{texmfdist}/doc/latex/greekdates
%doc %{texmfdist}/doc/latex/greektex
%doc %{texmfdist}/doc/latex/grfpaste
%doc %{texmfdist}/doc/latex/grnumalt
%doc %{texmfdist}/doc/latex/grverb
%doc %{texmfdist}/doc/latex/gu
%doc %{texmfdist}/doc/latex/guitbeamer
%doc %{texmfdist}/doc/latex/hanging
%doc %{texmfdist}/doc/latex/har2nat
%doc %{texmfdist}/doc/latex/harmony
%doc %{texmfdist}/doc/latex/harpoon
%doc %{texmfdist}/doc/latex/harvard
%doc %{texmfdist}/doc/latex/hc
%doc %{texmfdist}/doc/latex/hep
%doc %{texmfdist}/doc/latex/hepnames
%doc %{texmfdist}/doc/latex/hepparticles
%doc %{texmfdist}/doc/latex/hepthesis
%doc %{texmfdist}/doc/latex/hepunits
%doc %{texmfdist}/doc/latex/hexgame
%doc %{texmfdist}/doc/latex/histogr
%doc %{texmfdist}/doc/latex/hitec
%doc %{texmfdist}/doc/latex/hpsdiss
%doc %{texmfdist}/doc/latex/hvfloat
%doc %{texmfdist}/doc/latex/hypdvips
%doc %{texmfdist}/doc/latex/hyperref-docsrc
%doc %{texmfdist}/doc/latex/hyperxmp
%doc %{texmfdist}/doc/latex/ibycus-babel
%doc %{texmfdist}/doc/latex/icsv
%doc %{texmfdist}/doc/latex/ieeepes
%doc %{texmfdist}/doc/latex/ifmslide
%doc %{texmfdist}/doc/latex/ifplatform
%doc %{texmfdist}/doc/latex/ijmart
%doc %{texmfdist}/doc/latex/imac
%doc %{texmfdist}/doc/latex/image-gallery
%doc %{texmfdist}/doc/latex/imtekda
%doc %{texmfdist}/doc/latex/inlinebib
%doc %{texmfdist}/doc/latex/inlinedef
%doc %{texmfdist}/doc/latex/interactiveworkbook
%doc %{texmfdist}/doc/latex/invoice
%doc %{texmfdist}/doc/latex/ipa
%doc %{texmfdist}/doc/latex/iso
%doc %{texmfdist}/doc/latex/iso10303
%doc %{texmfdist}/doc/latex/isodate
%doc %{texmfdist}/doc/latex/isodoc
%doc %{texmfdist}/doc/latex/itnumpar
%doc %{texmfdist}/doc/latex/jknapltx
%doc %{texmfdist}/doc/latex/jneurosci
%doc %{texmfdist}/doc/latex/jpsj
%doc %{texmfdist}/doc/latex/jura
%doc %{texmfdist}/doc/latex/juraabbrev
%doc %{texmfdist}/doc/latex/juramisc
%doc %{texmfdist}/doc/latex/jurarsp
%doc %{texmfdist}/doc/latex/karnaugh
%doc %{texmfdist}/doc/latex/kerkis
%doc %{texmfdist}/doc/latex/kerntest
%doc %{texmfdist}/doc/latex/kluwer
%doc %{texmfdist}/doc/latex/lazylist
%doc %{texmfdist}/doc/latex/lcyw
%doc %{texmfdist}/doc/latex/ledmac
%doc %{texmfdist}/doc/latex/lgreek
%doc %{texmfdist}/doc/latex/lhelp
%doc %{texmfdist}/doc/latex/linguex
%doc %{texmfdist}/doc/latex/lipsum
%doc %{texmfdist}/doc/latex/listbib
%doc %{texmfdist}/doc/latex/lkproof
%doc %{texmfdist}/doc/latex/logic
%doc %{texmfdist}/doc/latex/ltxindex
%doc %{texmfdist}/doc/latex/mafr
%doc %{texmfdist}/doc/latex/magyar
%doc %{texmfdist}/doc/latex/mailing
%doc %{texmfdist}/doc/latex/makebarcode
%doc %{texmfdist}/doc/latex/makedtx
%doc %{texmfdist}/doc/latex/makeglos
%doc %{texmfdist}/doc/latex/mathdesign
%doc %{texmfdist}/doc/latex/mathpazo
%doc %{texmfdist}/doc/latex/mceinleger
%doc %{texmfdist}/doc/latex/memexsupp
%doc %{texmfdist}/doc/latex/metaplot
%doc %{texmfdist}/doc/latex/mff
%doc %{texmfdist}/doc/latex/mftinc
%doc %{texmfdist}/doc/latex/minutes
%doc %{texmfdist}/doc/latex/mmap
%doc %{texmfdist}/doc/latex/mnsymbol
%doc %{texmfdist}/doc/latex/moderncv
%doc %{texmfdist}/doc/latex/modroman
%doc %{texmfdist}/doc/latex/mongolian-babel
%doc %{texmfdist}/doc/latex/montex
%doc %{texmfdist}/doc/latex/moresize
%doc %{texmfdist}/doc/latex/msg
%doc %{texmfdist}/doc/latex/mslapa
%doc %{texmfdist}/doc/latex/mtgreek
%doc %{texmfdist}/doc/latex/multibbl
%doc %{texmfdist}/doc/latex/multirow
%doc %{texmfdist}/doc/latex/munich
%doc %{texmfdist}/doc/latex/muthesis
%doc %{texmfdist}/doc/latex/mxd
%doc %{texmfdist}/doc/latex/mxedruli
%doc %{texmfdist}/doc/latex/ncclatex
%doc %{texmfdist}/doc/latex/ncctools
%doc %{texmfdist}/doc/latex/nddiss
%doc %{texmfdist}/doc/latex/newalg
%doc %{texmfdist}/doc/latex/newfile
%doc %{texmfdist}/doc/latex/newlfm
%doc %{texmfdist}/doc/latex/newspaper
%doc %{texmfdist}/doc/latex/nomentbl
%doc %{texmfdist}/doc/latex/nonfloat
%doc %{texmfdist}/doc/latex/numname
%doc %{texmfdist}/doc/latex/ocr-latex
%doc %{texmfdist}/doc/latex/ogham
%doc %{texmfdist}/doc/latex/ogonek
%doc %{texmfdist}/doc/latex/opcit
%doc %{texmfdist}/doc/latex/ordinalpt
%doc %{texmfdist}/doc/latex/otibet
%doc %{texmfdist}/doc/latex/outline
%doc %{texmfdist}/doc/latex/outliner
%doc %{texmfdist}/doc/latex/pagenote
%doc %{texmfdist}/doc/latex/papercdcase
%doc %{texmfdist}/doc/latex/paresse
%doc %{texmfdist}/doc/latex/parrun
%doc %{texmfdist}/doc/latex/pauldoc
%doc %{texmfdist}/doc/latex/pdfwin
%doc %{texmfdist}/doc/latex/pecha
%doc %{texmfdist}/doc/latex/perception
%doc %{texmfdist}/doc/latex/perltex
%doc %{texmfdist}/doc/latex/pgf-soroban
%doc %{texmfdist}/doc/latex/pgfopts
%doc %{texmfdist}/doc/latex/philex
%doc %{texmfdist}/doc/latex/plates
%doc %{texmfdist}/doc/latex/plweb
%doc %{texmfdist}/doc/latex/pmgraph
%doc %{texmfdist}/doc/latex/polski
%doc %{texmfdist}/doc/latex/polyglot
%doc %{texmfdist}/doc/latex/postcards
%doc %{texmfdist}/doc/latex/prettyref
%doc %{texmfdist}/doc/latex/proba
%doc %{texmfdist}/doc/latex/procIAGssymp
%doc %{texmfdist}/doc/latex/protex
%doc %{texmfdist}/doc/latex/protocol
%doc %{texmfdist}/doc/latex/psfragx
%doc %{texmfdist}/doc/latex/psgo
%doc %{texmfdist}/doc/latex/pspicture
%doc %{texmfdist}/doc/latex/pst2pdf
%doc %{texmfdist}/doc/latex/qobitree
%doc %{texmfdist}/doc/latex/qstest
%doc %{texmfdist}/doc/latex/quotmark
%doc %{texmfdist}/doc/latex/r_und_s
%doc %{texmfdist}/doc/latex/randbild
%doc %{texmfdist}/doc/latex/rcs
%doc %{texmfdist}/doc/latex/rcsinfo
%doc %{texmfdist}/doc/latex/rectopma
%doc %{texmfdist}/doc/latex/refcheck
%doc %{texmfdist}/doc/latex/refstyle
%doc %{texmfdist}/doc/latex/relenc
%doc %{texmfdist}/doc/latex/repeatindex
%doc %{texmfdist}/doc/latex/rlepsf
%doc %{texmfdist}/doc/latex/rmpage
%doc %{texmfdist}/doc/latex/robustindex
%doc %{texmfdist}/doc/latex/rst
%doc %{texmfdist}/doc/latex/rtkinenc
%doc %{texmfdist}/doc/latex/rtklage
%doc %{texmfdist}/doc/latex/sagetex
%doc %{texmfdist}/doc/latex/sanskrit
%doc %{texmfdist}/doc/latex/sauerj
%doc %{texmfdist}/doc/latex/sauterfonts
%doc %{texmfdist}/doc/latex/savefnmark
%doc %{texmfdist}/doc/latex/savetrees
%doc %{texmfdist}/doc/latex/scalebar
%doc %{texmfdist}/doc/latex/scientificpaper
%doc %{texmfdist}/doc/latex/sciwordconv
%doc %{texmfdist}/doc/latex/semioneside
%doc %{texmfdist}/doc/latex/seqsplit
%doc %{texmfdist}/doc/latex/sf298
%doc %{texmfdist}/doc/latex/sffms
%doc %{texmfdist}/doc/latex/sfg
%doc %{texmfdist}/doc/latex/shorttoc
%doc %{texmfdist}/doc/latex/show2e
%doc %{texmfdist}/doc/latex/showexpl
%doc %{texmfdist}/doc/latex/slantsc
%doc %{texmfdist}/doc/latex/smalltableof
%doc %{texmfdist}/doc/latex/smartref
%doc %{texmfdist}/doc/latex/smflatex
%doc %{texmfdist}/doc/latex/snapshot
%doc %{texmfdist}/doc/latex/sort-by-letters
%doc %{texmfdist}/doc/latex/soyombo
%doc %{texmfdist}/doc/latex/sparklines
%doc %{texmfdist}/doc/latex/spie
%doc %{texmfdist}/doc/latex/splitbib
%doc %{texmfdist}/doc/latex/spotcolor
%doc %{texmfdist}/doc/latex/sprite
%doc %{texmfdist}/doc/latex/srcltx
%doc %{texmfdist}/doc/latex/ssqquote
%doc %{texmfdist}/doc/latex/statistik
%doc %{texmfdist}/doc/latex/stdpage
%doc %{texmfdist}/doc/latex/stellenbosch
%doc %{texmfdist}/doc/latex/stex
%doc %{texmfdist}/doc/latex/struktex
%doc %{texmfdist}/doc/latex/sttools
%doc %{texmfdist}/doc/latex/stubs
%doc %{texmfdist}/doc/latex/sugconf
%doc %{texmfdist}/doc/latex/supertabular
%doc %{texmfdist}/doc/latex/svgcolor
%doc %{texmfdist}/doc/latex/svn-multi
%doc %{texmfdist}/doc/latex/svn
%doc %{texmfdist}/doc/latex/svninfo
%doc %{texmfdist}/doc/latex/swebib
%doc %{texmfdist}/doc/latex/swimgraf
%doc %{texmfdist}/doc/latex/synproof
%doc %{texmfdist}/doc/latex/syntax
%doc %{texmfdist}/doc/latex/syntrace
%doc %{texmfdist}/doc/latex/synttree
%doc %{texmfdist}/doc/latex/t-angles
%doc %{texmfdist}/doc/latex/tableaux
%doc %{texmfdist}/doc/latex/tablists
%doc %{texmfdist}/doc/latex/tablor
%doc %{texmfdist}/doc/latex/tabto-ltx
%doc %{texmfdist}/doc/latex/tabulary
%doc %{texmfdist}/doc/latex/tabvar
%doc %{texmfdist}/doc/latex/talk
%doc %{texmfdist}/doc/latex/tapir
%doc %{texmfdist}/doc/latex/tcldoc
%doc %{texmfdist}/doc/latex/tdsfrmath
%doc %{texmfdist}/doc/latex/technics
%doc %{texmfdist}/doc/latex/ted
%doc %{texmfdist}/doc/latex/tengwarscript
%doc %{texmfdist}/doc/latex/tensor
%doc %{texmfdist}/doc/latex/teubner
%doc %{texmfdist}/doc/latex/texmate
%doc %{texmfdist}/doc/latex/texpower
%doc %{texmfdist}/doc/latex/texshade
%doc %{texmfdist}/doc/latex/textcase
%doc %{texmfdist}/doc/latex/textopo
%doc %{texmfdist}/doc/latex/theoremref
%doc %{texmfdist}/doc/latex/thesis-titlepage-fhac
%doc %{texmfdist}/doc/latex/thinsp
%doc %{texmfdist}/doc/latex/thmtools
%doc %{texmfdist}/doc/latex/thumb
%doc %{texmfdist}/doc/latex/thuthesis
%doc %{texmfdist}/doc/latex/ticket
%doc %{texmfdist}/doc/latex/tikz-inet
%doc %{texmfdist}/doc/latex/timesht
%doc %{texmfdist}/doc/latex/titling
%doc %{texmfdist}/doc/latex/tocvsec2
%doc %{texmfdist}/doc/latex/tokenizer
%doc %{texmfdist}/doc/latex/toolbox
%doc %{texmfdist}/doc/latex/toptesi
%doc %{texmfdist}/doc/latex/trajan
%doc %{texmfdist}/doc/latex/translator
%doc %{texmfdist}/doc/latex/trivfloat
%doc %{texmfdist}/doc/latex/turnstile
%doc %{texmfdist}/doc/latex/twoup
%doc %{texmfdist}/doc/latex/typogrid
%doc %{texmfdist}/doc/latex/umlaute
%doc %{texmfdist}/doc/latex/undertilde
%doc %{texmfdist}/doc/latex/unitsdef
%doc %{texmfdist}/doc/latex/unroman
%doc %{texmfdist}/doc/latex/upmethodology
%doc %{texmfdist}/doc/latex/urlbst
%doc %{texmfdist}/doc/latex/varindex
%doc %{texmfdist}/doc/latex/varsfromjobname
%doc %{texmfdist}/doc/latex/vector
%doc %{texmfdist}/doc/latex/verse
%doc %{texmfdist}/doc/latex/vhistory
%doc %{texmfdist}/doc/latex/vita
%doc %{texmfdist}/doc/latex/volumes
%doc %{texmfdist}/doc/latex/vpe
%doc %{texmfdist}/doc/latex/vrsion
%doc %{texmfdist}/doc/latex/vwcol
%doc %{texmfdist}/doc/latex/vxu
%doc %{texmfdist}/doc/latex/wadalab
%doc %{texmfdist}/doc/latex/wallpaper
%doc %{texmfdist}/doc/latex/warpcol
%doc %{texmfdist}/doc/latex/wnri
%doc %{texmfdist}/doc/latex/wordlike
%doc %{texmfdist}/doc/latex/xargs
%doc %{texmfdist}/doc/latex/xdoc
%doc %{texmfdist}/doc/latex/xfor
%doc %{texmfdist}/doc/latex/xifthen
%doc %{texmfdist}/doc/latex/xmpincl
%doc %{texmfdist}/doc/latex/xnewcommand
%doc %{texmfdist}/doc/latex/xoptarg
%doc %{texmfdist}/doc/latex/xpackages
%doc %{texmfdist}/doc/latex/xskak
%doc %{texmfdist}/doc/latex/xstring
%doc %{texmfdist}/doc/latex/xtcapts
%doc %{texmfdist}/doc/latex/xyling
%doc %{texmfdist}/doc/latex/xytree
%doc %{texmfdist}/doc/latex/yafoot
%doc %{texmfdist}/doc/latex/yhmath
%doc %{texmfdist}/doc/latex/york-thesis
%doc %{texmfdist}/doc/latex/yplan
%doc %{texmfdist}/doc/latex/zed-csp
%doc %{texmfdist}/doc/latex/zefonts
%doc %{texmfdist}/doc/latex/ziffer
%doc %{texmfdist}/doc/latex/zwgetfdate

%files latex-math-sources
%defattr(644,root,root,755)
%{texmfdist}/source/latex/bez123
%{texmfdist}/source/latex/binomexp
%{texmfdist}/source/latex/cmll
%{texmfdist}/source/latex/constants
%{texmfdist}/source/latex/coordsys
%{texmfdist}/source/latex/dotseqn
%{texmfdist}/source/latex/egplot
%{texmfdist}/source/latex/eqlist
%{texmfdist}/source/latex/eqnarray
%{texmfdist}/source/latex/esdiff
%{texmfdist}/source/latex/esvect
%{texmfdist}/source/latex/extpfeil
%{texmfdist}/source/latex/fouridx
%{texmfdist}/source/latex/functan
%{texmfdist}/source/latex/galois
%{texmfdist}/source/latex/gnuplottex
%{texmfdist}/source/latex/hhtensor
%{texmfdist}/source/latex/logpap
%{texmfdist}/source/latex/noitcrul
%{texmfdist}/source/latex/permute
%{texmfdist}/source/latex/qsymbols
%{texmfdist}/source/latex/subdepth
%{texmfdist}/source/latex/faktor
%{texmfdist}/source/latex/sseq
%{texmfdist}/source/latex/trsym
%{texmfdist}/source/latex/petri-nets
%{texmfdist}/source/latex/mlist
%{texmfdist}/source/latex/numprint

%files latex-math
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/eco
%doc %{texmfdist}/doc/latex/bez123
%doc %{texmfdist}/doc/latex/binomexp
%doc %{texmfdist}/doc/latex/cmll
%doc %{texmfdist}/doc/latex/constants
%doc %{texmfdist}/doc/latex/coordsys
%doc %{texmfdist}/doc/latex/egplot
%doc %{texmfdist}/doc/latex/eqlist
%doc %{texmfdist}/doc/latex/eqnarray
%doc %{texmfdist}/doc/latex/esdiff
%doc %{texmfdist}/doc/latex/esvect
%doc %{texmfdist}/doc/latex/extpfeil
%doc %{texmfdist}/doc/latex/faktor
%doc %{texmfdist}/doc/latex/fouridx
%doc %{texmfdist}/doc/latex/functan
%doc %{texmfdist}/doc/latex/galois
%doc %{texmfdist}/doc/latex/gnuplottex
%doc %{texmfdist}/doc/latex/hhtensor
%doc %{texmfdist}/doc/latex/logpap
%doc %{texmfdist}/doc/latex/makeplot
%doc %{texmfdist}/doc/latex/maybemath
%doc %{texmfdist}/doc/latex/mfpic4ode
%doc %{texmfdist}/doc/latex/mhequ
%doc %{texmfdist}/doc/latex/mlist
%doc %{texmfdist}/doc/latex/nath
%doc %{texmfdist}/doc/latex/noitcrul
%doc %{texmfdist}/doc/latex/numprint
%doc %{texmfdist}/doc/latex/permute
%doc %{texmfdist}/doc/latex/petri-nets
%doc %{texmfdist}/doc/latex/qsymbols
%doc %{texmfdist}/doc/latex/qtree
%doc %{texmfdist}/doc/latex/sdrt
%doc %{texmfdist}/doc/latex/semantic
%doc %{texmfdist}/doc/latex/simplewick
%doc %{texmfdist}/doc/latex/sseq
%doc %{texmfdist}/doc/latex/subdepth
%doc %{texmfdist}/doc/latex/subeqn
%doc %{texmfdist}/doc/latex/subeqnarray
%doc %{texmfdist}/doc/latex/trfsigns
%doc %{texmfdist}/doc/latex/trsym
%doc %{texmfdist}/doc/latex/ulsy
%{texmfdist}/fonts/map/dvips/cmll
%{texmfdist}/fonts/map/dvips/esvect
%{texmfdist}/fonts/source/public/cmll
%{texmfdist}/fonts/source/public/esvect
%{texmfdist}/fonts/source/public/trsym
%{texmfdist}/fonts/source/public/ulsy
%{texmfdist}/fonts/tfm/public/cmll
%{texmfdist}/fonts/tfm/public/eco
%{texmfdist}/fonts/tfm/public/esvect
%{texmfdist}/fonts/tfm/public/trsym
%{texmfdist}/fonts/tfm/public/ulsy
%{texmfdist}/fonts/type1/public/cmll
%{texmfdist}/fonts/type1/public/esvect
%{texmfdist}/fonts/vf/public/eco
%{texmfdist}/source/fonts/eco
%{texmfdist}/source/latex/makeplot
%{texmfdist}/source/latex/mfpic4ode
%{texmfdist}/source/latex/semantic
%{texmfdist}/source/latex/simplewick
%{texmfdist}/source/latex/subeqn
%{texmfdist}/source/latex/subeqnarray
%{texmfdist}/source/latex/trfsigns
%{texmfdist}/source/latex/ulsy
%{texmfdist}/tex/latex/bez123
%{texmfdist}/tex/latex/binomexp
%{texmfdist}/tex/latex/cmll
%{texmfdist}/tex/latex/constants
%{texmfdist}/tex/latex/coordsys
%{texmfdist}/tex/latex/dotseqn
%{texmfdist}/tex/latex/egplot
%{texmfdist}/tex/latex/eqlist
%{texmfdist}/tex/latex/eqnarray
%{texmfdist}/tex/latex/esdiff
%{texmfdist}/tex/latex/esvect
%{texmfdist}/tex/latex/extpfeil
%{texmfdist}/tex/latex/faktor
%{texmfdist}/tex/latex/fouridx
%{texmfdist}/tex/latex/functan
%{texmfdist}/tex/latex/galois
%{texmfdist}/tex/latex/gnuplottex
%{texmfdist}/tex/latex/hhtensor
%{texmfdist}/tex/latex/logpap
%{texmfdist}/tex/latex/makeplot
%{texmfdist}/tex/latex/maybemath
%{texmfdist}/tex/latex/mfpic4ode
%{texmfdist}/tex/latex/mhequ
%{texmfdist}/tex/latex/mhs
%{texmfdist}/tex/latex/mlist
%{texmfdist}/tex/latex/nath
%{texmfdist}/tex/latex/noitcrul
%{texmfdist}/tex/latex/numprint
%{texmfdist}/tex/latex/permute
%{texmfdist}/tex/latex/petri-nets
%{texmfdist}/tex/latex/qsymbols
%{texmfdist}/tex/latex/qtree
%{texmfdist}/tex/latex/sdrt
%{texmfdist}/tex/latex/semantic
%{texmfdist}/tex/latex/sfmath
%{texmfdist}/tex/latex/simplewick
%{texmfdist}/tex/latex/sseq
%{texmfdist}/tex/latex/subdepth
%{texmfdist}/tex/latex/subeqn
%{texmfdist}/tex/latex/subeqnarray
%{texmfdist}/tex/latex/trfsigns
%{texmfdist}/tex/latex/trsym
%{texmfdist}/tex/latex/ulsy
%doc %{texmfdist}/doc/latex/tree-dvips
%{texmfdist}/source/latex/tree-dvips
%{texmfdist}/tex/latex/tree-dvips

%files latex-physics
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/circ
%doc %{texmfdist}/doc/latex/colorwav
%doc %{texmfdist}/doc/latex/dyntree
%doc %{texmfdist}/doc/latex/feynmf
%doc %{texmfdist}/doc/latex/formula
%doc %{texmfdist}/doc/latex/listofsymbols
%doc %{texmfdist}/doc/latex/miller
%doc %{texmfdist}/doc/latex/susy
%{texmfdist}/metapost/feynmf
%{texmfdist}/source/latex/circ
%{texmfdist}/source/latex/colorwav
%{texmfdist}/source/latex/dyntree
%{texmfdist}/source/latex/feynmf
%{texmfdist}/source/latex/formula
%{texmfdist}/source/latex/isotope
%{texmfdist}/source/latex/miller
%{texmfdist}/tex/latex/circ
%{texmfdist}/tex/latex/colorwav
%{texmfdist}/tex/latex/dyntree
%{texmfdist}/tex/latex/feynmf
%{texmfdist}/tex/latex/formula
%{texmfdist}/tex/latex/isotope
%{texmfdist}/tex/latex/listofsymbols
%{texmfdist}/tex/latex/miller
%{texmfdist}/tex/latex/susy
%{texmfdist}/fonts/source/public/circ
%{texmfdist}/fonts/tfm/public/circ

%files latex-chem
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/achemso
%doc %{texmfdist}/doc/latex/bpchem
%doc %{texmfdist}/doc/latex/chemstyle
%doc %{texmfdist}/doc/latex/mhchem
%doc %{texmfdist}/doc/fonts/chemarrow
%doc %{texmfdist}/doc/latex/chemcompounds
%doc %{texmfdist}/doc/latex/chemcono
%{texmfdist}/fonts/afm/public/chemarrow
%{texmfdist}/fonts/map/dvips/chemarrow
%{texmfdist}/fonts/source/public/chemarrow
%{texmfdist}/fonts/tfm/public/chemarrow
%{texmfdist}/fonts/type1/public/chemarrow
%{texmfdist}/source/latex/achemso
%{texmfdist}/source/latex/bpchem
%{texmfdist}/source/latex/chemcompounds
%{texmfdist}/source/latex/chemstyle
%{texmfdist}/tex/latex/achemso
%{texmfdist}/tex/latex/bpchem
%{texmfdist}/tex/latex/chemarrow
%{texmfdist}/tex/latex/chemcompounds
%{texmfdist}/tex/latex/chemcono
%{texmfdist}/tex/latex/chemstyle
%{texmfdist}/tex/latex/mhchem

%files latex-biology
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/biocon
%doc %{texmfdist}/doc/latex/dnaseq
%{texmfdist}/bibtex/bib/biocon
%{texmfdist}/source/latex/biocon
%{texmfdist}/source/latex/dnaseq
%{texmfdist}/tex/latex/biocon
%{texmfdist}/tex/latex/dnaseq

%files latex-pdftools
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/attachfile
%doc %{texmfdist}/doc/latex/cooltooltips
%doc %{texmfdist}/doc/latex/movie15
%doc %{texmfdist}/doc/latex/pdfcprot
%doc %{texmfdist}/doc/latex/pdfscreen
%doc %{texmfdist}/doc/latex/pdfsync
%doc %{texmfdist}/doc/latex/pdftricks
%{texmfdist}/source/latex/attachfile
%{texmfdist}/source/latex/cooltooltips
%{texmfdist}/source/latex/pdfcprot
%{texmfdist}/tex/latex/attachfile
%{texmfdist}/tex/latex/cooltooltips
%{texmfdist}/tex/latex/movie15
%{texmfdist}/tex/latex/pdfcprot
%{texmfdist}/tex/latex/pdfscreen
%{texmfdist}/tex/latex/pdfsync
%{texmfdist}/tex/latex/pdftricks

%files latex-informatic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/alg
%doc %{texmfdist}/doc/latex/bytefield
%doc %{texmfdist}/doc/latex/lsc
%doc %{texmfdist}/doc/latex/method
%doc %{texmfdist}/doc/latex/msc
%doc %{texmfdist}/doc/latex/progkeys
%doc %{texmfdist}/doc/latex/register
%doc %{texmfdist}/doc/latex/uml
%{texmfdist}/source/latex/alg
%{texmfdist}/source/latex/bytefield
%{texmfdist}/source/latex/method
%{texmfdist}/source/latex/progkeys
%{texmfdist}/source/latex/register
%{texmfdist}/source/latex/uml
%{texmfdist}/tex/latex/alg
%{texmfdist}/tex/latex/bytefield
%{texmfdist}/tex/latex/lsc
%{texmfdist}/tex/latex/method
%{texmfdist}/tex/latex/msc
%{texmfdist}/tex/latex/progkeys
%{texmfdist}/tex/latex/register
%{texmfdist}/tex/latex/uml

%files latex-games
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/backgammon
%doc %{texmfdist}/doc/latex/chessboard
%doc %{texmfdist}/doc/latex/chessfss
%doc %{texmfdist}/doc/latex/crosswrd
%doc %{texmfdist}/doc/latex/cwpuzzle
%doc %{texmfdist}/doc/latex/jeopardy
%doc %{texmfdist}/doc/latex/othello
%doc %{texmfdist}/doc/latex/sgame
%doc %{texmfdist}/doc/latex/skak
%doc %{texmfdist}/doc/latex/sudoku
%doc %{texmfdist}/doc/latex/sudokubundle
%{texmfdist}/fonts/enc/dvips/chessfss
%{texmfdist}/fonts/map/dvips/skak
%{texmfdist}/fonts/source/public/backgammon
%{texmfdist}/fonts/source/public/cchess
%{texmfdist}/fonts/source/public/chess
%{texmfdist}/fonts/source/public/go
%{texmfdist}/fonts/source/public/othello
%{texmfdist}/fonts/source/public/skak
%{texmfdist}/fonts/tfm/public/backgammon
%{texmfdist}/fonts/tfm/public/cchess
%{texmfdist}/fonts/tfm/public/go
%{texmfdist}/fonts/tfm/public/othello
%{texmfdist}/fonts/tfm/public/skak
%{texmfdist}/source/latex/backgammon
%{texmfdist}/source/latex/chessboard
%{texmfdist}/source/latex/chessfss
%{texmfdist}/source/latex/crosswrd
%{texmfdist}/source/latex/cwpuzzle
%{texmfdist}/source/latex/go
%{texmfdist}/source/latex/jeopardy
%{texmfdist}/source/latex/othello
%{texmfdist}/source/latex/sudoku
%{texmfdist}/source/latex/sudokubundle
%{texmfdist}/tex/latex/backgammon
%{texmfdist}/tex/latex/cchess
%{texmfdist}/tex/latex/chess
%{texmfdist}/tex/latex/chessboard
%{texmfdist}/tex/latex/chessfss
%{texmfdist}/tex/latex/crosswrd
%{texmfdist}/tex/latex/cwpuzzle
%{texmfdist}/tex/latex/go
%{texmfdist}/tex/latex/jeopardy
%{texmfdist}/tex/latex/othello
%{texmfdist}/tex/latex/sgame
%{texmfdist}/tex/latex/skak
%{texmfdist}/tex/latex/sudoku
%{texmfdist}/tex/latex/sudokubundle

%files latex-sources
%defattr(644,root,root,755)
%{texmfdist}/source/latex/acronym
%{texmfdist}/source/latex/adrlist
%{texmfdist}/source/latex/altfont
%{texmfdist}/source/latex/answers
%{texmfdist}/source/latex/ascii
%{texmfdist}/source/latex/augie
%{texmfdist}/source/latex/barcodes
%{texmfdist}/source/latex/bbding
%{texmfdist}/source/latex/bbm-macros
%{texmfdist}/source/latex/bengali
%{texmfdist}/source/latex/beton
%{texmfdist}/source/latex/bibarts
%{texmfdist}/source/latex/bibleref
%{texmfdist}/source/latex/biblist
%{texmfdist}/source/latex/bigfoot
%{texmfdist}/source/latex/bizcard
%{texmfdist}/source/latex/blindtext
%{texmfdist}/source/latex/bookhands
%{texmfdist}/source/latex/bophook
%{texmfdist}/source/latex/boxhandler
%{texmfdist}/source/latex/braille
%{texmfdist}/source/latex/breakurl
%{texmfdist}/source/latex/brushscr
%{texmfdist}/source/latex/burmese
%{texmfdist}/source/latex/captcont
%{texmfdist}/source/latex/catechis
%{texmfdist}/source/latex/cclicenses
%{texmfdist}/source/latex/cd
%{texmfdist}/source/latex/cd-cover
%{texmfdist}/source/latex/cdpbundl
%{texmfdist}/source/latex/changes
%{texmfdist}/source/latex/chapterfolder
%{texmfdist}/source/latex/cleveref
%{texmfdist}/source/latex/cmcyralt
%{texmfdist}/source/latex/cmsd
%{texmfdist}/source/latex/codepage
%{texmfdist}/source/latex/confproc
%{texmfdist}/source/latex/coverpage
%{texmfdist}/source/latex/crop
%{texmfdist}/source/latex/crossreference
%{texmfdist}/source/latex/ctib
%{texmfdist}/source/latex/cweb-latex
%{texmfdist}/source/latex/dateiliste
%{texmfdist}/source/latex/datetime
%{texmfdist}/source/latex/decimal
%{texmfdist}/source/latex/diagnose
%{texmfdist}/source/latex/docmfp
%{texmfdist}/source/latex/doipubmed
%{texmfdist}/source/latex/dotarrow
%{texmfdist}/source/latex/dottex
%{texmfdist}/source/latex/drac
%{texmfdist}/source/latex/draftcopy
%{texmfdist}/source/latex/dramatist
%{texmfdist}/source/latex/eCards
%{texmfdist}/source/latex/ebezier
%{texmfdist}/source/latex/ebsthesis
%{texmfdist}/source/latex/ecclesiastic
%{texmfdist}/source/latex/edmargin
%{texmfdist}/source/latex/eemeir
%{texmfdist}/source/latex/eiad
%{texmfdist}/source/latex/ellipsis
%{texmfdist}/source/latex/em
%{texmfdist}/source/latex/emp
%{texmfdist}/source/latex/endfloat
%{texmfdist}/source/latex/endheads
%{texmfdist}/source/latex/engpron
%{texmfdist}/source/latex/engrec
%{texmfdist}/source/latex/envlab
%{texmfdist}/source/latex/epigraph
%{texmfdist}/source/latex/epiolmec
%{texmfdist}/source/latex/epsdice
%{texmfdist}/source/latex/eqparbox
%{texmfdist}/source/latex/errata
%{texmfdist}/source/latex/eso-pic
%{texmfdist}/source/latex/ethiop
%{texmfdist}/source/latex/eukdate
%{texmfdist}/source/latex/euproposal
%{texmfdist}/source/latex/euro
%{texmfdist}/source/latex/everypage
%{texmfdist}/source/latex/exercise
%{texmfdist}/source/latex/expl3
%{texmfdist}/source/latex/extract
%{texmfdist}/source/latex/facsimile
%{texmfdist}/source/latex/fancynum
%{texmfdist}/source/latex/fancyref
%{texmfdist}/source/latex/fancytooltips
%{texmfdist}/source/latex/fancyvrb
%{texmfdist}/source/latex/figsize
%{texmfdist}/source/latex/filecontents
%{texmfdist}/source/latex/fink
%{texmfdist}/source/latex/flabels
%{texmfdist}/source/latex/flagderiv
%{texmfdist}/source/latex/flashcards
%{texmfdist}/source/latex/float
%{texmfdist}/source/latex/floatrow
%{texmfdist}/source/latex/fmp
%{texmfdist}/source/latex/fnbreak
%{texmfdist}/source/latex/foilhtml
%{texmfdist}/source/latex/fonttable
%{texmfdist}/source/latex/footmisc
%{texmfdist}/source/latex/footnpag
%{texmfdist}/source/latex/frankenstein
%{texmfdist}/source/latex/frontespizio
%{texmfdist}/source/latex/fullblck
%{texmfdist}/source/latex/fundus
%{texmfdist}/source/latex/gcite
%{texmfdist}/source/latex/genmpage
%{texmfdist}/source/latex/geometry
%{texmfdist}/source/latex/geomsty
%{texmfdist}/source/latex/glossaries
%{texmfdist}/source/latex/graphics
%{texmfdist}/source/latex/graphicx-psmin
%{texmfdist}/source/latex/greekdates
%{texmfdist}/source/latex/grnumalt
%{texmfdist}/source/latex/grverb
%{texmfdist}/source/latex/hanging
%{texmfdist}/source/latex/harvard
%{texmfdist}/source/latex/hc
%{texmfdist}/source/latex/hepthesis
%{texmfdist}/source/latex/hilowres
%{texmfdist}/source/latex/histogr
%{texmfdist}/source/latex/hpsdiss
%{texmfdist}/source/latex/hyper
%{texmfdist}/source/latex/hyperref
%{texmfdist}/source/latex/hyperxmp
%{texmfdist}/source/latex/hyphenat
%{texmfdist}/source/latex/ibycus-babel
%{texmfdist}/source/latex/icsv
%{texmfdist}/source/latex/ifmslide
%{texmfdist}/source/latex/ifplatform
%{texmfdist}/source/latex/ijmart
%{texmfdist}/source/latex/imtekda
%{texmfdist}/source/latex/index
%{texmfdist}/source/latex/inlinedef
%{texmfdist}/source/latex/iso
%{texmfdist}/source/latex/iso10303
%{texmfdist}/source/latex/isodate
%{texmfdist}/source/latex/isodoc
%{texmfdist}/source/latex/itnumpar
%{texmfdist}/source/latex/jura
%{texmfdist}/source/latex/juraabbrev
%{texmfdist}/source/latex/jurarsp
%{texmfdist}/source/latex/kdgreek
%{texmfdist}/source/latex/koma-script
%{texmfdist}/source/latex/labels
%{texmfdist}/source/latex/layouts
%{texmfdist}/source/latex/listings
%{texmfdist}/source/latex/localloc
%{texmfdist}/source/latex/mathcomp
%{texmfdist}/source/latex/mathpazo
%{texmfdist}/source/latex/mdwtools
%{texmfdist}/source/latex/memoir
%{texmfdist}/source/latex/mh
%{texmfdist}/source/latex/mnsymbol
%{texmfdist}/source/latex/modroman
%{texmfdist}/source/latex/mongolian-babel
%{texmfdist}/source/latex/montex
%{texmfdist}/source/latex/mparhack
%{texmfdist}/source/latex/ms
%{texmfdist}/source/latex/multibib
%{texmfdist}/source/latex/mwcls
%{texmfdist}/source/latex/natbib
%{texmfdist}/source/latex/ncctools
%{texmfdist}/source/latex/nddiss
%{texmfdist}/source/latex/newalg
%{texmfdist}/source/latex/newfile
%{texmfdist}/source/latex/newlfm
%{texmfdist}/source/latex/newspaper
%{texmfdist}/source/latex/nomencl
%{texmfdist}/source/latex/ntgclass
%{texmfdist}/source/latex/oberdiek
%{texmfdist}/source/latex/paralist
%{texmfdist}/source/latex/pdfpages
%{texmfdist}/source/latex/pict2e
%{texmfdist}/source/latex/preprint
%{texmfdist}/source/latex/preview
%{texmfdist}/source/latex/psfrag
%{texmfdist}/source/latex/pslatex
%{texmfdist}/source/latex/revtex
%{texmfdist}/source/latex/rotating
%{texmfdist}/source/latex/rotfloat
%{texmfdist}/source/latex/scale
%{texmfdist}/source/latex/sectsty
%{texmfdist}/source/latex/showlabels
%{texmfdist}/source/latex/sidecap
%{texmfdist}/source/latex/soul
%{texmfdist}/source/latex/stdclsdv
%{texmfdist}/source/latex/subfig
%{texmfdist}/source/latex/subfigure
%{texmfdist}/source/latex/supertabular
%{texmfdist}/source/latex/tablists
%{texmfdist}/source/latex/tabulary
%{texmfdist}/source/latex/tabvar
%{texmfdist}/source/latex/talk
%{texmfdist}/source/latex/tcldoc
%{texmfdist}/source/latex/tdsfrmath
%{texmfdist}/source/latex/technics
%{texmfdist}/source/latex/ted
%{texmfdist}/source/latex/tengwarscript
%{texmfdist}/source/latex/tensor
%{texmfdist}/source/latex/teubner
%{texmfdist}/source/latex/texmate
%{texmfdist}/source/latex/texpower
%{texmfdist}/source/latex/texshade
%{texmfdist}/source/latex/textcase
%{texmfdist}/source/latex/textfit
%{texmfdist}/source/latex/textopo
%{texmfdist}/source/latex/textpos
%{texmfdist}/source/latex/thesis-titlepage-fhac
%{texmfdist}/source/latex/thmtools
%{texmfdist}/source/latex/thumb
%{texmfdist}/source/latex/thuthesis
%{texmfdist}/source/latex/timesht
%{texmfdist}/source/latex/titling
%{texmfdist}/source/latex/tocbibind
%{texmfdist}/source/latex/tocloft
%{texmfdist}/source/latex/tools
%{texmfdist}/source/latex/totpages
%{texmfdist}/source/latex/type1cm
%{texmfdist}/source/latex/undertilde
%{texmfdist}/source/latex/units
%{texmfdist}/source/latex/unitsdef
%{texmfdist}/source/latex/unroman
%{texmfdist}/source/latex/upmethodology
%{texmfdist}/source/latex/urlbst
%{texmfdist}/source/latex/varindex
%{texmfdist}/source/latex/vector
%{texmfdist}/source/latex/verse
%{texmfdist}/source/latex/vmargin
%{texmfdist}/source/latex/volumes
%{texmfdist}/source/latex/vrsion
%{texmfdist}/source/latex/vwcol
%{texmfdist}/source/latex/vxu
%{texmfdist}/source/latex/warning
%{texmfdist}/source/latex/warpcol
%{texmfdist}/source/latex/was
%{texmfdist}/source/latex/xargs
%{texmfdist}/source/latex/xdoc
%{texmfdist}/source/latex/xfor
%{texmfdist}/source/latex/xmpincl
%{texmfdist}/source/latex/xpackages
%{texmfdist}/source/latex/xskak
%{texmfdist}/source/latex/xtab
%{texmfdist}/source/latex/xtcapts
%{texmfdist}/source/latex/yafoot
%{texmfdist}/source/latex/yfonts
%{texmfdist}/source/latex/yhmath
%{texmfdist}/source/latex/york-thesis
%{texmfdist}/source/latex/youngtab

%files latex-styles
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/IEEEconf
%doc %{texmfdist}/doc/latex/aastex
%doc %{texmfdist}/doc/latex/acmconf
%doc %{texmfdist}/doc/latex/active-conf
%doc %{texmfdist}/doc/latex/aiaa
%doc %{texmfdist}/doc/latex/apacite
%doc %{texmfdist}/doc/latex/asaetr
%doc %{texmfdist}/doc/latex/computational-complexity
%doc %{texmfdist}/doc/latex/dtk
%doc %{texmfdist}/doc/latex/elsarticle
%doc %{texmfdist}/doc/latex/lettre
%doc %{texmfdist}/doc/latex/lexikon
%doc %{texmfdist}/doc/latex/lps
%doc %{texmfdist}/doc/latex/manuscript
%doc %{texmfdist}/doc/latex/maple
%doc %{texmfdist}/doc/latex/mentis
%doc %{texmfdist}/doc/latex/nature
%doc %{texmfdist}/doc/latex/nih
%doc %{texmfdist}/doc/latex/nostarch
%doc %{texmfdist}/doc/latex/nrc
%doc %{texmfdist}/doc/latex/octavo
%doc %{texmfdist}/doc/latex/paper
%doc %{texmfdist}/doc/latex/papertex
%doc %{texmfdist}/doc/latex/pbsheet
%doc %{texmfdist}/doc/latex/petiteannonce
%doc %{texmfdist}/doc/latex/philosophersimprint
%doc %{texmfdist}/doc/latex/pittetd
%doc %{texmfdist}/doc/latex/plari
%doc %{texmfdist}/doc/latex/play
%doc %{texmfdist}/doc/latex/poemscol
%doc %{texmfdist}/doc/latex/pracjourn
%doc %{texmfdist}/doc/latex/ptptex
%doc %{texmfdist}/doc/latex/refman
%doc %{texmfdist}/doc/latex/rsc
%doc %{texmfdist}/doc/latex/screenplay
%doc %{texmfdist}/doc/latex/script
%doc %{texmfdist}/doc/latex/shipunov
%doc %{texmfdist}/doc/latex/sides
%doc %{texmfdist}/doc/latex/siggraph
%doc %{texmfdist}/doc/latex/stage
%doc %{texmfdist}/doc/latex/tufte-latex
%doc %{texmfdist}/doc/latex/tugboat
%doc %{texmfdist}/doc/latex/uaclasses
%doc %{texmfdist}/doc/latex/ucthesis
%doc %{texmfdist}/doc/latex/uiucthesis
%doc %{texmfdist}/doc/latex/umich-thesis
%doc %{texmfdist}/doc/latex/umthesis
%doc %{texmfdist}/doc/latex/uwthesis
%{texmfdist}/bibtex/bib/aiaa
%{texmfdist}/bibtex/bib/apacite
%{texmfdist}/bibtex/bib/asaetr
%{texmfdist}/bibtex/bib/computational-complexity
%{texmfdist}/bibtex/bib/dtk
%{texmfdist}/bibtex/bib/philosophersimprint
%{texmfdist}/bibtex/bst/aiaa
%{texmfdist}/bibtex/bst/apacite
%{texmfdist}/bibtex/bst/asaetr
%{texmfdist}/bibtex/bst/computational-complexity
%{texmfdist}/bibtex/bst/dtk
%{texmfdist}/bibtex/bst/rsc
%{texmfdist}/source/latex/IEEEconf
%{texmfdist}/source/latex/aastex
%{texmfdist}/source/latex/acmconf
%{texmfdist}/source/latex/active-conf
%{texmfdist}/source/latex/aiaa
%{texmfdist}/source/latex/apacite
%{texmfdist}/source/latex/asaetr
%{texmfdist}/source/latex/computational-complexity
%{texmfdist}/source/latex/dtk
%{texmfdist}/source/latex/elsarticle
%{texmfdist}/source/latex/lexikon
%{texmfdist}/source/latex/lps
%{texmfdist}/source/latex/manuscript
%{texmfdist}/source/latex/mentis
%{texmfdist}/source/latex/menu
%{texmfdist}/source/latex/nostarch
%{texmfdist}/source/latex/nrc
%{texmfdist}/source/latex/octavo
%{texmfdist}/source/latex/paper
%{texmfdist}/source/latex/papertex
%{texmfdist}/source/latex/pbsheet
%{texmfdist}/source/latex/philosophersimprint
%{texmfdist}/source/latex/pittetd
%{texmfdist}/source/latex/plari
%{texmfdist}/source/latex/play
%{texmfdist}/source/latex/poemscol
%{texmfdist}/source/latex/pracjourn
%{texmfdist}/source/latex/refman
%{texmfdist}/source/latex/rsc
%{texmfdist}/source/latex/screenplay
%{texmfdist}/source/latex/siggraph
%{texmfdist}/source/latex/tugboat
%{texmfdist}/source/latex/uaclasses
%{texmfdist}/source/latex/uiucthesis
%{texmfdist}/tex/latex/IEEEconf
%{texmfdist}/tex/latex/aastex
%{texmfdist}/tex/latex/acmconf
%{texmfdist}/tex/latex/active-conf
%{texmfdist}/tex/latex/aiaa
%{texmfdist}/tex/latex/apacite
%{texmfdist}/tex/latex/asaetr
%{texmfdist}/tex/latex/computational-complexity
%{texmfdist}/tex/latex/dtk
%{texmfdist}/tex/latex/elsarticle
%{texmfdist}/tex/latex/lettre
%{texmfdist}/tex/latex/lexikon
%{texmfdist}/tex/latex/lps
%{texmfdist}/tex/latex/manuscript
%{texmfdist}/tex/latex/maple
%{texmfdist}/tex/latex/mentis
%{texmfdist}/tex/latex/menu
%{texmfdist}/tex/latex/muthesis
%{texmfdist}/tex/latex/nature
%{texmfdist}/tex/latex/nih
%{texmfdist}/tex/latex/nostarch
%{texmfdist}/tex/latex/nrc
%{texmfdist}/tex/latex/octavo
%{texmfdist}/tex/latex/paper
%{texmfdist}/tex/latex/papertex
%{texmfdist}/tex/latex/pbsheet
%{texmfdist}/tex/latex/petiteannonce
%{texmfdist}/tex/latex/philosophersimprint
%{texmfdist}/tex/latex/pittetd
%{texmfdist}/tex/latex/plari
%{texmfdist}/tex/latex/play
%{texmfdist}/tex/latex/poemscol
%{texmfdist}/tex/latex/pracjourn
%{texmfdist}/tex/latex/ptptex
%{texmfdist}/tex/latex/refman
%{texmfdist}/tex/latex/rsc
%{texmfdist}/tex/latex/screenplay
%{texmfdist}/tex/latex/script
%{texmfdist}/tex/latex/shipunov
%{texmfdist}/tex/latex/sides
%{texmfdist}/tex/latex/siggraph
%{texmfdist}/tex/latex/stage
%{texmfdist}/tex/latex/tufte-latex
%{texmfdist}/tex/latex/tugboat
%{texmfdist}/tex/latex/uaclasses
%{texmfdist}/tex/latex/ucthesis
%{texmfdist}/tex/latex/uiucthesis
%{texmfdist}/tex/latex/umich-thesis
%{texmfdist}/tex/latex/umthesis
%{texmfdist}/tex/latex/uwthesis

%files latex-lang
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ESIEEcv
%doc %{texmfdist}/doc/latex/chletter
%doc %{texmfdist}/doc/latex/dinbrief
%doc %{texmfdist}/doc/latex/disser
%doc %{texmfdist}/doc/latex/elmath
%doc %{texmfdist}/doc/latex/eskd
%doc %{texmfdist}/doc/latex/ginpenc
%doc %{texmfdist}/doc/latex/hrlatex
%doc %{texmfdist}/doc/latex/mla-paper
%{texmfdist}/source/latex/ESIEEcv
%{texmfdist}/source/latex/chletter
%{texmfdist}/source/latex/dinbrief
%{texmfdist}/source/latex/disser
%{texmfdist}/source/latex/elmath
%{texmfdist}/source/latex/eskd
%{texmfdist}/source/latex/ginpenc
%{texmfdist}/source/latex/hrlatex
%{texmfdist}/tex/latex/ESIEEcv
%{texmfdist}/tex/latex/chletter
%{texmfdist}/tex/latex/dinbrief
%{texmfdist}/tex/latex/disser
%{texmfdist}/tex/latex/elmath
%{texmfdist}/tex/latex/eskd
%{texmfdist}/tex/latex/ginpenc
%{texmfdist}/tex/latex/hrlatex
%{texmfdist}/tex/latex/mla-paper

%files latex-music
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/musixps
%doc %{texmfdist}/doc/latex/abc
%doc %{texmfdist}/doc/latex/guitar
%doc %{texmfdist}/doc/latex/musixlyr
%doc %{texmfdist}/doc/latex/songbook
%{texmfdist}/fonts/source/public/musixps
%{texmfdist}/fonts/tfm/public/musixps
%{texmfdist}/source/latex/abc
%{texmfdist}/source/latex/guitar
%{texmfdist}/source/latex/songbook
%{texmfdist}/tex/generic/musixlyr
%{texmfdist}/tex/generic/musixps
%{texmfdist}/tex/latex/abc
%{texmfdist}/tex/latex/guitar
%{texmfdist}/tex/latex/songbook

%files latex-extend
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/HA-prosper
%doc %{texmfdist}/doc/latex/addlines
%doc %{texmfdist}/doc/latex/alnumsec
%doc %{texmfdist}/doc/latex/arydshln
%doc %{texmfdist}/doc/latex/babelbib
%doc %{texmfdist}/doc/latex/bibtopicprefix
%doc %{texmfdist}/doc/latex/boites
%doc %{texmfdist}/doc/latex/booklet
%doc %{texmfdist}/doc/latex/bullcntr
%doc %{texmfdist}/doc/latex/chappg
%doc %{texmfdist}/doc/latex/clefval
%doc %{texmfdist}/doc/latex/colortbl
%doc %{texmfdist}/doc/latex/combine
%doc %{texmfdist}/doc/latex/contour
%doc %{texmfdist}/doc/latex/ctable
%doc %{texmfdist}/doc/latex/curve2e
%doc %{texmfdist}/doc/latex/dashrule
%doc %{texmfdist}/doc/latex/etaremune
%doc %{texmfdist}/doc/latex/expdlist
%doc %{texmfdist}/doc/latex/leading
%doc %{texmfdist}/doc/latex/listliketab
%doc %{texmfdist}/doc/latex/makebox
%doc %{texmfdist}/doc/latex/makecell
%doc %{texmfdist}/doc/latex/marginnote
%doc %{texmfdist}/doc/latex/mcaption
%doc %{texmfdist}/doc/latex/mcite
%doc %{texmfdist}/doc/latex/mciteplus
%doc %{texmfdist}/doc/latex/minipage-marginpar
%doc %{texmfdist}/doc/latex/miniplot
%doc %{texmfdist}/doc/latex/multicap
%doc %{texmfdist}/doc/latex/newvbtm
%doc %{texmfdist}/doc/latex/notes2bib
%doc %{texmfdist}/doc/latex/ntabbing
%doc %{texmfdist}/doc/latex/pbox
%doc %{texmfdist}/doc/latex/pinlabel
%doc %{texmfdist}/doc/latex/polytable
%doc %{texmfdist}/doc/latex/rccol
%doc %{texmfdist}/doc/latex/romannum
%doc %{texmfdist}/doc/latex/schedule
%doc %{texmfdist}/doc/latex/subfloat
%doc %{texmfdist}/doc/latex/umoline
%doc %{texmfdist}/doc/latex/underlin
%{texmfdist}/bibtex/bst/babelbib
%{texmfdist}/bibtex/bst/mciteplus
%{texmfdist}/source/latex/HA-prosper
%{texmfdist}/source/latex/addlines
%{texmfdist}/source/latex/alnumsec
%{texmfdist}/source/latex/arydshln
%{texmfdist}/source/latex/babelbib
%{texmfdist}/source/latex/bibtopicprefix
%{texmfdist}/source/latex/boites
%{texmfdist}/source/latex/booklet
%{texmfdist}/source/latex/bullcntr
%{texmfdist}/source/latex/chappg
%{texmfdist}/source/latex/cjw
%{texmfdist}/source/latex/clefval
%{texmfdist}/source/latex/colortbl
%{texmfdist}/source/latex/combine
%{texmfdist}/source/latex/contour
%{texmfdist}/source/latex/ctable
%{texmfdist}/source/latex/curve2e
%{texmfdist}/source/latex/dashbox
%{texmfdist}/source/latex/dashrule
%{texmfdist}/source/latex/etaremune
%{texmfdist}/source/latex/expdlist
%{texmfdist}/source/latex/leading
%{texmfdist}/source/latex/listliketab
%{texmfdist}/source/latex/makebox
%{texmfdist}/source/latex/makecell
%{texmfdist}/source/latex/marginnote
%{texmfdist}/source/latex/mcaption
%{texmfdist}/source/latex/mcite
%{texmfdist}/source/latex/minipage-marginpar
%{texmfdist}/source/latex/multicap
%{texmfdist}/source/latex/newvbtm
%{texmfdist}/source/latex/notes2bib
%{texmfdist}/source/latex/pbox
%{texmfdist}/source/latex/polytable
%{texmfdist}/source/latex/rccol
%{texmfdist}/source/latex/romannum
%{texmfdist}/source/latex/schedule
%{texmfdist}/source/latex/subfloat
%{texmfdist}/source/latex/umoline
%{texmfdist}/source/latex/underlin
%{texmfdist}/tex/latex/HA-prosper
%{texmfdist}/tex/latex/addlines
%{texmfdist}/tex/latex/alnumsec
%{texmfdist}/tex/latex/arydshln
%{texmfdist}/tex/latex/babelbib
%{texmfdist}/tex/latex/bibtopicprefix
%{texmfdist}/tex/latex/boites
%{texmfdist}/tex/latex/booklet
%{texmfdist}/tex/latex/bullcntr
%{texmfdist}/tex/latex/chappg
%{texmfdist}/tex/latex/cjw
%{texmfdist}/tex/latex/clefval
%{texmfdist}/tex/latex/colortbl
%{texmfdist}/tex/latex/combine
%{texmfdist}/tex/latex/contour
%{texmfdist}/tex/latex/ctable
%{texmfdist}/tex/latex/curve2e
%{texmfdist}/tex/latex/dashbox
%{texmfdist}/tex/latex/dashrule
%{texmfdist}/tex/latex/etaremune
%{texmfdist}/tex/latex/expdlist
%{texmfdist}/tex/latex/leading
%{texmfdist}/tex/latex/listliketab
%{texmfdist}/tex/latex/ltablex
%{texmfdist}/tex/latex/makebox
%{texmfdist}/tex/latex/makecell
%{texmfdist}/tex/latex/marginnote
%{texmfdist}/tex/latex/mcaption
%{texmfdist}/tex/latex/mcite
%{texmfdist}/tex/latex/mciteplus
%{texmfdist}/tex/latex/minipage-marginpar
%{texmfdist}/tex/latex/miniplot
%{texmfdist}/tex/latex/multicap
%{texmfdist}/tex/latex/newvbtm
%{texmfdist}/tex/latex/notes2bib
%{texmfdist}/tex/latex/ntabbing
%{texmfdist}/tex/latex/numline
%{texmfdist}/tex/latex/pbox
%{texmfdist}/tex/latex/pinlabel
%{texmfdist}/tex/latex/polytable
%{texmfdist}/tex/latex/rccol
%{texmfdist}/tex/latex/romannum
%{texmfdist}/tex/latex/schedule
%{texmfdist}/tex/latex/subfloat
%{texmfdist}/tex/latex/umoline
%{texmfdist}/tex/latex/underlin

%files latex-presentation
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppower4
%attr(755,root,root) %{_bindir}/pdfthumb
%doc %{texmfdist}/doc/latex/powerdot
%doc %{texmfdist}/doc/latex/ppower4
%doc %{texmfdist}/doc/latex/sciposter
%doc %{texmfdist}/doc/latex/tpslifonts
%{texmfdist}/scripts/ppower4
%{texmfdist}/source/latex/powerdot
%{texmfdist}/tex/latex/powerdot
%{texmfdist}/tex/latex/ppower4
%{texmfdist}/tex/latex/sciposter
%{texmfdist}/tex/latex/tpslifonts

%files latex-programming
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/cool
%doc %{texmfdist}/doc/latex/coollist
%doc %{texmfdist}/doc/latex/coolstr
%doc %{texmfdist}/doc/latex/csvtools
%doc %{texmfdist}/doc/latex/datatool
%doc %{texmfdist}/doc/latex/datenumber
%doc %{texmfdist}/doc/latex/delimtxt
%doc %{texmfdist}/doc/latex/dialogl
%doc %{texmfdist}/doc/latex/dprogress
%doc %{texmfdist}/doc/latex/environ
%doc %{texmfdist}/doc/latex/export
%doc %{texmfdist}/doc/latex/fmtcount
%doc %{texmfdist}/doc/latex/forarray
%doc %{texmfdist}/doc/latex/forloop
%doc %{texmfdist}/doc/latex/inversepath
%doc %{texmfdist}/doc/latex/labelcas
%doc %{texmfdist}/doc/latex/makecmds
%doc %{texmfdist}/doc/latex/nag
%doc %{texmfdist}/doc/latex/namespc
%doc %{texmfdist}/doc/latex/progress
%doc %{texmfdist}/doc/latex/randtext
%doc %{texmfdist}/doc/latex/regcount
%doc %{texmfdist}/doc/latex/robustcommand
%doc %{texmfdist}/doc/latex/splitindex
%doc %{texmfdist}/doc/latex/stringstrings
%doc %{texmfdist}/doc/latex/substr
%doc %{texmfdist}/doc/latex/typedref
%{texmfdist}/source/latex/cmdtrack
%{texmfdist}/source/latex/cool
%{texmfdist}/source/latex/coollist
%{texmfdist}/source/latex/coolstr
%{texmfdist}/source/latex/csvtools
%{texmfdist}/source/latex/datatool
%{texmfdist}/source/latex/datenumber
%{texmfdist}/source/latex/delimtxt
%{texmfdist}/source/latex/dialogl
%{texmfdist}/source/latex/dprogress
%{texmfdist}/source/latex/environ
%{texmfdist}/source/latex/export
%{texmfdist}/source/latex/fmtcount
%{texmfdist}/source/latex/forarray
%{texmfdist}/source/latex/forloop
%{texmfdist}/source/latex/inversepath
%{texmfdist}/source/latex/labelcas
%{texmfdist}/source/latex/lcg
%{texmfdist}/source/latex/makecmds
%{texmfdist}/source/latex/nag
%{texmfdist}/source/latex/namespc
%{texmfdist}/source/latex/patchcmd
%{texmfdist}/source/latex/regcount
%{texmfdist}/source/latex/robustcommand
%{texmfdist}/source/latex/splitindex
%{texmfdist}/source/latex/stack
%{texmfdist}/source/latex/stringstrings
%{texmfdist}/source/latex/typedref
%{texmfdist}/tex/latex/cmdtrack
%{texmfdist}/tex/latex/cool
%{texmfdist}/tex/latex/coollist
%{texmfdist}/tex/latex/coolstr
%{texmfdist}/tex/latex/csvtools
%{texmfdist}/tex/latex/datatool
%{texmfdist}/tex/latex/datenumber
%{texmfdist}/tex/latex/delimtxt
%{texmfdist}/tex/latex/dialogl
%{texmfdist}/tex/latex/dprogress
%{texmfdist}/tex/latex/environ
%{texmfdist}/tex/latex/export
%{texmfdist}/tex/latex/fmtcount
%{texmfdist}/tex/latex/forarray
%{texmfdist}/tex/latex/forloop
%{texmfdist}/tex/latex/inversepath
%{texmfdist}/tex/latex/labelcas
%{texmfdist}/tex/latex/lcg
%{texmfdist}/tex/latex/makecmds
%{texmfdist}/tex/latex/multido
%{texmfdist}/tex/latex/nag
%{texmfdist}/tex/latex/namespc
%{texmfdist}/tex/latex/patchcmd
%{texmfdist}/tex/latex/progress
%{texmfdist}/tex/latex/randtext
%{texmfdist}/tex/latex/regcount
%{texmfdist}/tex/latex/robustcommand
%{texmfdist}/tex/latex/splitindex
%{texmfdist}/tex/latex/stack
%{texmfdist}/tex/latex/stringstrings
%{texmfdist}/tex/latex/substr
%{texmfdist}/tex/latex/typedref

%files latex-effects
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/umrand
%doc %{texmfdist}/doc/latex/arcs
%doc %{texmfdist}/doc/latex/blowup
%doc %{texmfdist}/doc/latex/changebar
%doc %{texmfdist}/doc/latex/draftwatermark
%doc %{texmfdist}/doc/latex/flippdf
%doc %{texmfdist}/doc/latex/flowfram
%doc %{texmfdist}/doc/latex/isorot
%doc %{texmfdist}/doc/latex/lettrine
%doc %{texmfdist}/doc/latex/niceframe
%doc %{texmfdist}/doc/latex/notes
%doc %{texmfdist}/doc/latex/objectz
%doc %{texmfdist}/doc/latex/parallel
%doc %{texmfdist}/doc/latex/quotchap
%doc %{texmfdist}/doc/latex/rotpages
%doc %{texmfdist}/doc/latex/sectionbox
%doc %{texmfdist}/doc/latex/shadethm
%doc %{texmfdist}/doc/latex/ushort
%{texmfdist}/fonts/source/public/niceframe
%{texmfdist}/fonts/source/public/umrand
%{texmfdist}/fonts/tfm/public/niceframe
%{texmfdist}/fonts/tfm/public/umrand
%{texmfdist}/source/latex/arcs
%{texmfdist}/source/latex/blowup
%{texmfdist}/source/latex/changebar
%{texmfdist}/source/latex/draftwatermark
%{texmfdist}/source/latex/flippdf
%{texmfdist}/source/latex/flowfram
%{texmfdist}/source/latex/isorot
%{texmfdist}/source/latex/lettrine
%{texmfdist}/source/latex/niceframe
%{texmfdist}/source/latex/notes
%{texmfdist}/source/latex/objectz
%{texmfdist}/source/latex/parallel
%{texmfdist}/source/latex/quotchap
%{texmfdist}/source/latex/ushort
%{texmfdist}/tex/latex/arcs
%{texmfdist}/tex/latex/blowup
%{texmfdist}/tex/latex/changebar
%{texmfdist}/tex/latex/draftwatermark
%{texmfdist}/tex/latex/flippdf
%{texmfdist}/tex/latex/flowfram
%{texmfdist}/tex/latex/isorot
%{texmfdist}/tex/latex/lettrine
%{texmfdist}/tex/latex/niceframe
%{texmfdist}/tex/latex/notes
%{texmfdist}/tex/latex/objectz
%{texmfdist}/tex/latex/parallel
%{texmfdist}/tex/latex/quotchap
%{texmfdist}/tex/latex/rotpages
%{texmfdist}/tex/latex/sectionbox
%{texmfdist}/tex/latex/shadethm
%{texmfdist}/tex/latex/umrand
%{texmfdist}/tex/latex/ushort

# I don't sort them, because maybe can splitting and grouping them
%files latex-other
%defattr(644,root,root,755)
%{texmfdist}/metapost/latexmp
%{texmfdist}/metapost/makecirc
# -- misc packages
%dir %{texmfdist}/source/alatex
%{texmfdist}/source/alatex/base
%{texmfdist}/tex/alatex
%doc %{texmfdist}/doc/generic/enctex
%{texmfdist}/tex/generic/enctex
# Create a calendar, in German.
%{texmfdist}/tex/latex/kalender
# Typeset Karnaugh-Veitch-maps.
%{texmfdist}/tex/latex/karnaugh
# Kerkis (Greek) font family.
%{texmfdist}/tex/latex/kerkis
# Print tables and generate control files to adjust kernings.
%{texmfdist}/source/latex/kerntest
%{texmfdist}/tex/latex/kerntest
%{texmfdist}/source/latex/kluwer
%{texmfdist}/tex/latex/kluwer
# A two-element sans-serif typeface.
%{texmfdist}/tex/latex/kurier
# Lists in TeX's "mouth".
%{texmfdist}/tex/latex/lazylist
# This package makes available Classic Cyrillic CM fonts
%{texmfdist}/source/latex/lcyw
%{texmfdist}/tex/latex/lcyw
# Typeset scholarly editions in parallel texts.
%{texmfdist}/source/latex/ledmac
%{texmfdist}/tex/latex/ledmac
%{texmfdist}/tex/latex/levy
# Macros for using Silvio Levy's Greek fonts.
%{texmfdist}/tex/latex/lgreek
# A non-standard Cyrillic input scheme.
%{texmfdist}/source/latex/lhcyr
%{texmfdist}/tex/latex/lhcyr
# Miscellaneous helper packages.
%{texmfdist}/source/latex/lhelp
%{texmfdist}/tex/latex/lhelp
# Use the font Libertine with LaTeX.
%{texmfdist}/tex/latex/libertine
# Typeset maps and blocks according to the Information Mapping
%{texmfdist}/source/latex/limap
%{texmfdist}/tex/latex/limap
%{texmfdist}/tex/latex/linearA
# Format linguists' examples.
%{texmfdist}/tex/latex/linguex
# Easy access to the Lorem Ipsum dummy text.
%{texmfdist}/source/latex/lipsum
%{texmfdist}/tex/latex/lipsum
# Lists contents of BibTeX files.
%{texmfdist}/source/latex/listbib
%{texmfdist}/tex/latex/listbib
# LK Proof figure macros.
%{texmfdist}/tex/latex/lkproof
# A font for electronic logic design.
%{texmfdist}/tex/latex/logic
# A LaTeX package to typeset indices with GNU's Texindex.
%{texmfdist}/source/latex/ltxindex
%{texmfdist}/tex/latex/ltxindex
# Set of slide fonts based on CM.
%{texmfdist}/tex/latex/lxfonts
# Support for LY1 LaTeX encoding.
%{texmfdist}/tex/latex/ly1
# Mathematics in accord with French usage.
%{texmfdist}/tex/latex/mafr
# Macros for mail merging.
%{texmfdist}/source/latex/mailing
%{texmfdist}/tex/latex/mailing
# Print various kinds 2/5 and Code 39 bar codes.
%{texmfdist}/tex/latex/makebarcode
# Perl script to help generate dtx and ins files
%{texmfdist}/source/latex/makedtx
%{texmfdist}/tex/latex/makedtx
# Include a glossary into a document.
%{texmfdist}/tex/latex/makeglos
# LaTeX support for the TeX book symbols.
%{texmfdist}/source/latex/manfnt
%{texmfdist}/tex/latex/manfnt
# Support for multiple character sets and encodings.
%{texmfdist}/source/latex/mapcodes
%{texmfdist}/tex/latex/mapcodes
# Mathematical fonts to fit with particular text fonts.
%{texmfdist}/tex/latex/mathdesign
# Creating covers for music cassettes.
%{texmfdist}/tex/latex/mceinleger
# Experimental memoir support.
%{texmfdist}/tex/latex/memexsupp
# Multiple font formats.
%{texmfdist}/source/latex/mff
%{texmfdist}/tex/latex/mff
# Pretty-print Metafont source.
%{texmfdist}/source/latex/mftinc
%{texmfdist}/tex/latex/mftinc
# Package for writing minutes of meetings.
%{texmfdist}/source/latex/minutes
%{texmfdist}/tex/latex/minutes
# Allows font sizes up to 35.83pt.
%{texmfdist}/source/latex/moresize
%{texmfdist}/tex/latex/moresize
# A package for LaTeX localisation.
%{texmfdist}/source/latex/msg
%{texmfdist}/tex/latex/msg
# Michael Landy's APA citation style.
%{texmfdist}/tex/latex/mslapa
# Use italic and upright greek letters with mathtime.
%{texmfdist}/source/latex/mtgreek
%{texmfdist}/tex/latex/mtgreek
# Multiple bibliographies.
%{texmfdist}/source/latex/multibbl
%{texmfdist}/tex/latex/multibbl
# Support for Mongolian "horizontal" (Xewtee Dorwoljin) script.
%{texmfdist}/source/latex/mxd
%{texmfdist}/tex/latex/mxd
# A pair of Georgian fonts.
%{texmfdist}/tex/latex/mxedruli
# Nomenclature typeset in a longtable
%{texmfdist}/source/latex/nomentbl
%{texmfdist}/tex/latex/nomentbl
# Non-floating table and figure captions.
%{texmfdist}/source/latex/nonfloat
%{texmfdist}/tex/latex/nonfloat
# Convert a number to its English expression.
%{texmfdist}/tex/latex/numname
# LaTeX support for ocr fonts.
%{texmfdist}/tex/latex/ocr-latex
# Support for Polish typography and the ogonek.
%{texmfdist}/source/latex/ogonek
%{texmfdist}/tex/latex/ogonek
# Old style numbers in OT1 encoding.
%{texmfdist}/source/latex/oldstyle
%{texmfdist}/tex/latex/oldstyle
# Footnote-style bibliographical references.
%{texmfdist}/source/latex/opcit
%{texmfdist}/tex/latex/opcit
# Counters as ordinal numbers in Portuguese.
%{texmfdist}/source/latex/ordinalpt
%{texmfdist}/tex/latex/ordinalpt
# Macros, metrics, etc., to use the OT2 Cyrillic encoding.
%{texmfdist}/tex/latex/ot2cyr
%{texmfdist}/source/latex/otibet
%{texmfdist}/tex/latex/otibet
# List environment for making outlines.
%{texmfdist}/tex/latex/outline
# Change section levels easily.
%{texmfdist}/tex/latex/outliner
# Fonts designed by Fra Luca de Pacioli in 1497.
%{texmfdist}/source/latex/pacioli
%{texmfdist}/tex/latex/pacioli
# Page number-only page styles.
%{texmfdist}/source/latex/pageno
%{texmfdist}/tex/latex/pageno
# Notes at end of document.
%{texmfdist}/source/latex/pagenote
%{texmfdist}/tex/latex/pagenote
%{texmfdist}/tex/latex/palatino
# Origami-style folding paper CD case.
%{texmfdist}/source/latex/papercdcase
%{texmfdist}/tex/latex/papercdcase
# Defines simple macros for greek letters.
%{texmfdist}/source/latex/paresse
%{texmfdist}/tex/latex/paresse
# Typesets (two) streams of text running parallel.
%{texmfdist}/source/latex/parrun
%{texmfdist}/tex/latex/parrun
# German LaTeX package documentation.
%{texmfdist}/source/latex/pauldoc
%{texmfdist}/tex/latex/pauldoc
# Using graphics from PAW.
%{texmfdist}/source/latex/pawpict
%{texmfdist}/tex/latex/pawpict
# Font support for current PCL printers.
%{texmfdist}/tex/latex/pclnfss
%{texmfdist}/tex/latex/pdfwin
# Print Tibetan text in the classic pecha layout style.
%{texmfdist}/tex/latex/pecha
# Define LaTeX macros in terms of Perl code
%{texmfdist}/source/latex/perltex
%{texmfdist}/tex/latex/perltex
# Create images of the soroban using TikZ/PGF.
%{texmfdist}/tex/latex/pgf-soroban
# Disk of Phaistos font.
%{texmfdist}/tex/latex/phaistos
# Cross references for named and numbered environments.
%{texmfdist}/tex/latex/philex
# MetaFont Phonetic fonts, based on Computer Modern.
%{texmfdist}/tex/latex/phonetic
# Adds relative coordinates and improves the \plot command.
%{texmfdist}/tex/latex/pictex2
# Arrange for "plates" sections of documents.
%{texmfdist}/tex/latex/plates
%{texmfdist}/source/latex/plweb
%{texmfdist}/tex/latex/plweb
# "Poor man's" graphics.
%{texmfdist}/tex/latex/pmgraph
# Typeset Polish documents with LaTeX and Polish fonts.
%{texmfdist}/source/latex/polski
%{texmfdist}/tex/latex/polski
%{texmfdist}/source/latex/polyglot
%{texmfdist}/tex/latex/polyglot
# Facilitates mass-mailing of postcards (junkmail).
%{texmfdist}/tex/latex/postcards
# Make label references "self-identify".
%{texmfdist}/source/latex/prettyref
%{texmfdist}/tex/latex/prettyref
# Shortcuts commands to symbols used in probability texts.
%{texmfdist}/source/latex/proba
%{texmfdist}/tex/latex/proba
%{texmfdist}/tex/latex/procIAGssymp
# Literate programming package.
%{texmfdist}/tex/latex/protex
# A class for typesetting minutes (only german).
%{texmfdist}/source/latex/protocol
%{texmfdist}/tex/latex/protocol
# A psfrag eXtension.
%{texmfdist}/source/latex/psfragx
%{texmfdist}/tex/latex/psfragx
%{texmfdist}/tex/latex/psgo
# PostScript picture support.
%{texmfdist}/source/latex/pspicture
%{texmfdist}/tex/latex/pspicture
# LaTeX macros for typesetting trees.
%{texmfdist}/tex/latex/qobitree
# Bundle for unit tests and pattern matching.
%{texmfdist}/source/latex/qstest
%{texmfdist}/tex/latex/qstest
# Consistent quote marks.
%{texmfdist}/source/latex/quotmark
%{texmfdist}/tex/latex/quotmark
%{texmfdist}/tex/latex/r_und_s
# Marginal pictures.
%{texmfdist}/source/latex/randbild
%{texmfdist}/tex/latex/randbild
# Use RCS (revision control system) tags in LaTeX documents.
%{texmfdist}/source/latex/rcs
%{texmfdist}/tex/latex/rcs
# Support for the revision control system.
%{texmfdist}/source/latex/rcsinfo
%{texmfdist}/tex/latex/rcsinfo
# Recycle top matter.
%{texmfdist}/tex/latex/rectopma
# Check references (in figures, table, equations, etc).
%{texmfdist}/tex/latex/refcheck
# Advanced formatting of cross references.
%{texmfdist}/source/latex/refstyle
%{texmfdist}/tex/latex/refstyle
# A "relaxed" font encoding.
%{texmfdist}/source/latex/relenc
%{texmfdist}/tex/latex/relenc
# Repeat items in an index after a page or column break
%{texmfdist}/tex/latex/repeatindex
%{texmfdist}/tex/latex/resume
# Rewrite labels in EPS graphics.
%{texmfdist}/tex/latex/rlepsf
# A package to help change page layout parameters in LaTeX.
%{texmfdist}/source/latex/rmpage
%{texmfdist}/tex/latex/rmpage
# Create index with pagerefs.
%{texmfdist}/tex/latex/robustindex
# Drawing rhetorical structure analysis diagrams in LaTeX.
%{texmfdist}/source/latex/rst
%{texmfdist}/tex/latex/rst
# Input encoding with fallback procedures.
%{texmfdist}/source/latex/rtkinenc
%{texmfdist}/tex/latex/rtkinenc
%{texmfdist}/tex/latex/rtklage
# Embed Sage code and plots into LaTeX.
%{texmfdist}/source/latex/sagetex
%{texmfdist}/tex/latex/sagetex
# Sanskrit support.
%{texmfdist}/source/latex/sanskrit
%{texmfdist}/tex/latex/sanskrit
# A bundle of utilities by Jonathan Sauer.
%{texmfdist}/source/latex/sauerj
%{texmfdist}/tex/latex/sauerj
# Use sauter fonts in LaTeX.
%{texmfdist}/source/latex/sauterfonts
%{texmfdist}/tex/latex/sauterfonts
# Save name of the footnote mark for reuse.
%{texmfdist}/source/latex/savefnmark
%{texmfdist}/tex/latex/savefnmark
# Redefine symbols where names conflict.
%{texmfdist}/tex/latex/savesym
# Pack as much as possible onto each page of a LaTeX document.
%{texmfdist}/source/latex/savetrees
%{texmfdist}/tex/latex/savetrees
# Create scalebars for maps, diagrams or photos.
%{texmfdist}/source/latex/scalebar
%{texmfdist}/tex/latex/scalebar
# Format a scientific paper for journal
%{texmfdist}/tex/latex/scientificpaper
# Use Scientific Word/WorkPlace files with another TeX.
%{texmfdist}/source/latex/sciwordconv
%{texmfdist}/tex/latex/sciwordconv
# Semaphore alphabet font.
%{texmfdist}/tex/latex/semaphor
# Put only special contents on left-hand pages in two sided layout.
%{texmfdist}/source/latex/semioneside
%{texmfdist}/tex/latex/semioneside
# Split long sequences of characters in a neutral way.
%{texmfdist}/source/latex/seqsplit
%{texmfdist}/tex/latex/seqsplit
%{texmfdist}/source/latex/sf298
%{texmfdist}/tex/latex/sf298
# Typesetting science fiction/fantasy manuscripts.
%{texmfdist}/source/latex/sffms
%{texmfdist}/tex/latex/sffms
# Draw signal flow graphs.
%{texmfdist}/tex/latex/sfg
# Shade the background of any box.
%{texmfdist}/tex/latex/shadbox
# Table of contents with different depths.
%{texmfdist}/source/latex/shorttoc
%{texmfdist}/tex/latex/shorttoc
# Variants of \show for LaTeX2e.
%{texmfdist}/source/latex/show2e
%{texmfdist}/tex/latex/show2e
%{texmfdist}/source/latex/showexpl
%{texmfdist}/tex/latex/showexpl
# A font to draw a skull.
%{texmfdist}/source/latex/skull
%{texmfdist}/tex/latex/skull
# Access different-shaped small-caps fonts.
%{texmfdist}/source/latex/slantsc
%{texmfdist}/tex/latex/slantsc
# Create listoffigures etc. in a single chapter.
%{texmfdist}/tex/latex/smalltableof
# Extend LaTeX's \ref capability.
%{texmfdist}/tex/latex/smartref
# Classes for Société mathématique de France publications.
%{texmfdist}/tex/latex/smflatex
# List the external dependencies of a LaTeX document.
%{texmfdist}/source/latex/snapshot
%{texmfdist}/tex/latex/snapshot
# Fonts and a macro for Soyombo under LaTeX.
%{texmfdist}/tex/latex/soyombo
# Drawing sparklines: intense, simple, wordlike graphics.
%{texmfdist}/tex/latex/sparklines
# Support for formatting SPIE Proceedings manuscripts.
%{texmfdist}/tex/latex/spie
# Split and reorder your bibliography.
%{texmfdist}/source/latex/splitbib
%{texmfdist}/tex/latex/splitbib
# Macros to typeset simple bitmaps with LaTeX.
%{texmfdist}/tex/latex/sprite
# Jump between DVI and TeX files.
%{texmfdist}/source/latex/srcltx
%{texmfdist}/tex/latex/srcltx
# Use the cmssq fonts.
%{texmfdist}/source/latex/ssqquote
%{texmfdist}/tex/latex/ssqquote
# Statistics style.
%{texmfdist}/tex/latex/statex2
# Store statistics of a document.
%{texmfdist}/source/latex/statistik
%{texmfdist}/tex/latex/statistik
# Typeset Icelandic staves and runic letters.
%{texmfdist}/source/latex/staves
%{texmfdist}/tex/latex/staves
# Standard pages with n lines of at most m characters each.
%{texmfdist}/source/latex/stdpage
%{texmfdist}/tex/latex/stdpage
# Stellenbosch thesis bundle.
%{texmfdist}/source/latex/stellenbosch
%{texmfdist}/tex/latex/stellenbosch
# An Infrastructure for Semantic Preloading of LaTeX Documents.
%{texmfdist}/source/latex/stex
%{texmfdist}/tex/latex/stex
# Draw Nassi-Schneidermann charts
%{texmfdist}/source/latex/struktex
%{texmfdist}/tex/latex/struktex
# Various macros.
%{texmfdist}/tex/latex/sttools
# Create tear-off stubs at the bottom of a page.
%{texmfdist}/tex/latex/stubs
# SAS(R) user group conference proceedings document class.
%{texmfdist}/tex/latex/sugconf
# Define SVG named colours.
%{texmfdist}/tex/latex/svgcolor
# Subversion keywords in multi-file LaTeX documents
%{texmfdist}/source/latex/svn-multi
%{texmfdist}/tex/latex/svn-multi
# Typeset Subversion keywords.
%{texmfdist}/source/latex/svn
%{texmfdist}/tex/latex/svn
# Typeset Subversion Keywords.
%{texmfdist}/source/latex/svninfo
%{texmfdist}/tex/latex/svninfo
# Graphical/textual representations of swimming performances
%{texmfdist}/source/latex/swimgraf
%{texmfdist}/tex/latex/swimgraf
%{texmfdist}/tex/latex/symbol
# Easy drawing of syntactic proofs.
%{texmfdist}/tex/latex/synproof
%{texmfdist}/tex/latex/syntax
# Labels for tracing in a syntax tree.
%{texmfdist}/source/latex/syntrace
%{texmfdist}/tex/latex/syntrace
# Typeset syntactic trees.
%{texmfdist}/source/latex/synttree
%{texmfdist}/tex/latex/synttree
# Fonts and macro package for drawing timing diagrams.
%{texmfdist}/tex/latex/timing
# Section numbering and table of contents control.
%{texmfdist}/source/latex/tocvsec2
%{texmfdist}/tex/latex/tocvsec2
# A tokenizer.
%{texmfdist}/tex/latex/tokenizer
# Macros for writing indices, glossaries.
%{texmfdist}/source/latex/toolbox
%{texmfdist}/tex/latex/toolbox
# Bundle of files for typsetting theses.
%{texmfdist}/source/latex/toptesi
%{texmfdist}/tex/latex/toptesi
# Adjust tracking of strings.
%{texmfdist}/tex/latex/tracking
# Fonts from the Trajan column in Rome.
%{texmfdist}/source/latex/trajan
%{texmfdist}/tex/latex/trajan
# Provide an open platform for packages to be localized.
%{texmfdist}/tex/latex/translator
# Quick float definitions in LaTeX.
%{texmfdist}/source/latex/trivfloat
%{texmfdist}/tex/latex/trivfloat
# Typeset the (logic) turnstile notation.
%{texmfdist}/source/latex/turnstile
%{texmfdist}/tex/latex/turnstile
%{texmfdist}/source/latex/twoup
%{texmfdist}/tex/latex/twoup
# Print a typographic grid.
%{texmfdist}/source/latex/typogrid
%{texmfdist}/tex/latex/typogrid
# Time printing, in German.
%{texmfdist}/tex/latex/uhrzeit
# -- sources for other packages
%dir %{texmfdist}/source/cslatex
%{texmfdist}/source/cslatex/base
%{texmfdist}/source/generic/xypic
%{texmfdist}/source/latex/GuIT
# Definitive source of Plain TeX on CTAN.
%{texmfdist}/source/latex/base
%{texmfdist}/source/latex/bayer
# -- examples
# A small collection of minimal DTX examples.
%{texmfdist}/source/latex/dtxgallery
# Editorial Notes for LaTeX documents.
%{texmfdist}/source/latex/ed
# Typeset scholarly edition.
%{texmfdist}/source/latex/edmac
# Use AMS Euler fonts for math.
%{texmfdist}/source/latex/euler
# Ridgeway's fonts.
%{texmfdist}/source/latex/wnri
%dir %{texmfdist}/source/plain
%{texmfdist}/source/plain/jsmisc
%{texmfdist}/source/xelatex


%files latex-pdfslide
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/pdfslide
%{texmfdist}/tex/latex/pdfslide

%files latex-pgf
%defattr(644,root,root,755)
%dir %{texmfdist}/source/context
%dir %{texmfdist}/source/context/third
%doc %{texmfdist}/doc/generic/pgf
%doc %{texmfdist}/doc/latex/pgfplots
%{texmfdist}/source/context/third/pgfplots
%{texmfdist}/source/latex/pgfopts
%{texmfdist}/source/latex/pgfplots
%{texmfdist}/tex/generic/pgf
%{texmfdist}/tex/generic/pgfplots
%{texmfdist}/tex/latex/pgf
%{texmfdist}/tex/latex/pgfopts
%{texmfdist}/tex/latex/pgfplots

%files latex-prosper
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ppr-prv
%doc %{texmfdist}/doc/latex/prosper
%{texmfdist}/source/latex/ppr-prv
%{texmfdist}/source/latex/prosper
%{texmfdist}/tex/latex/ppr-prv
%{texmfdist}/tex/latex/prosper

%files latex-polynom
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/polynom
%{texmfdist}/source/latex/polynom
%{texmfdist}/tex/latex/polynom

%files latex-polynomial
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/polynomial
%{texmfdist}/source/latex/polynomial
%{texmfdist}/tex/latex/polynomial

%files latex-pseudocode
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/pseudocode
%{texmfdist}/tex/latex/pseudocode

%files latex-pst-2dplot
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-2dplot
%{texmfdist}/tex/latex/pst-2dplot

%files latex-pst-3dplot
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-3d
%doc %{texmfdist}/doc/generic/pst-3dplot
%{texmfdist}/source/generic/pst-3d
%{texmfdist}/source/generic/pst-3dplot
%{texmfdist}/tex/generic/pst-3d
%{texmfdist}/tex/generic/pst-3dplot
%{texmfdist}/tex/latex/pst-3d
%{texmfdist}/tex/latex/pst-3dplot

%files latex-pst-bar
%defattr(644,root,root,755)
%{texmfdist}/tex/generic/pst-bar
%{texmfdist}/tex/latex/pst-bar

%files latex-pst-circ
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-circ
%{texmfdist}/tex/generic/pst-circ
%{texmfdist}/tex/latex/pst-circ

%files latex-pst-diffraction
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-diffraction
%{texmfdist}/tex/generic/pst-diffraction
%{texmfdist}/tex/latex/pst-diffraction

%files latex-pst-eucl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-eucl
%{texmfdist}/tex/generic/pst-eucl
%{texmfdist}/tex/latex/pst-eucl

%files latex-pst-fun
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-fun
%{texmfdist}/tex/generic/pst-fun
%{texmfdist}/tex/latex/pst-fun

%files latex-pst-func
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-func
%{texmfdist}/tex/generic/pst-func
%{texmfdist}/tex/latex/pst-func

%files latex-pst-infixplot
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-infixplot
%{texmfdist}/tex/generic/pst-infixplot
%{texmfdist}/tex/latex/pst-infixplot

%files latex-pst-fr3d
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-fr3d
%{texmfdist}/source/generic/pst-fr3d
%{texmfdist}/tex/generic/pst-fr3d
%{texmfdist}/tex/latex/pst-fr3d

%files latex-pst-fractal
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-fractal
%{texmfdist}/tex/generic/pst-fractal
%{texmfdist}/tex/latex/pst-fractal

%files latex-pst-math
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-math
%{texmfdist}/tex/generic/pst-math
%{texmfdist}/tex/latex/pst-math

%files latex-pst-ob3d
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-ob3d
%{texmfdist}/source/generic/pst-ob3d
%{texmfdist}/tex/generic/pst-ob3d
%{texmfdist}/tex/latex/pst-ob3d

%files latex-pst-optexp
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-optexp
%{texmfdist}/tex/generic/pst-optexp
%{texmfdist}/tex/latex/pst-optexp

%files latex-pst-optic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-optic
%{texmfdist}/tex/generic/pst-optic
%{texmfdist}/tex/latex/pst-optic

%files latex-pst-text
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-text
%{texmfdist}/tex/generic/pst-text
%{texmfdist}/tex/latex/pst-text

%files latex-pst-uncategorized
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ps4pdf
%doc %{texmfdist}/doc/generic/pst-asr
%doc %{texmfdist}/doc/generic/pst-bar
%doc %{texmfdist}/doc/generic/pst-barcode
%doc %{texmfdist}/doc/generic/pst-blur
%doc %{texmfdist}/doc/generic/pst-coil
%doc %{texmfdist}/doc/generic/pst-cox
%doc %{texmfdist}/doc/generic/pst-dbicons
%doc %{texmfdist}/doc/generic/pst-eps
%doc %{texmfdist}/doc/generic/pst-fill
%doc %{texmfdist}/doc/generic/pst-geo
%doc %{texmfdist}/doc/generic/pst-ghsb
%doc %{texmfdist}/doc/generic/pst-gr3d
%doc %{texmfdist}/doc/generic/pst-grad
%doc %{texmfdist}/doc/generic/pst-jtree
%doc %{texmfdist}/doc/generic/pst-labo
%doc %{texmfdist}/doc/generic/pst-lens
%doc %{texmfdist}/doc/generic/pst-light3d
%doc %{texmfdist}/doc/generic/pst-osci
%doc %{texmfdist}/doc/generic/pst-pad
%doc %{texmfdist}/doc/generic/pst-pdgr
%doc %{texmfdist}/doc/generic/pst-poly
%doc %{texmfdist}/doc/generic/pst-qtree
%doc %{texmfdist}/doc/generic/pst-slpe
%doc %{texmfdist}/doc/generic/pst-solides3d
%doc %{texmfdist}/doc/generic/pst-soroban
%doc %{texmfdist}/doc/generic/pst-spectra
%doc %{texmfdist}/doc/generic/pst-stru
%doc %{texmfdist}/doc/generic/pst-uml
%doc %{texmfdist}/doc/generic/pst-vue3d
%doc %{texmfdist}/doc/latex/auto-pst-pdf
%doc %{texmfdist}/doc/latex/pst-pdf
%dir %{texmfdist}/scripts/pst-pdf
%attr(755,root,root) %{texmfdist}/scripts/pst-pdf/ps4pdf
%{texmfdist}/source/generic/pst-barcode
%{texmfdist}/source/generic/pst-blur
%{texmfdist}/source/generic/pst-circ
%{texmfdist}/source/generic/pst-coil
%{texmfdist}/source/generic/pst-dbicons
%{texmfdist}/source/generic/pst-diffraction
%{texmfdist}/source/generic/pst-eps
%{texmfdist}/source/generic/pst-fill
%{texmfdist}/source/generic/pst-fractal
%{texmfdist}/source/generic/pst-fun
%{texmfdist}/source/generic/pst-func
%{texmfdist}/source/generic/pst-lens
%{texmfdist}/source/generic/pst-light3d
%{texmfdist}/source/generic/pst-optic
%{texmfdist}/source/generic/pst-pad
%{texmfdist}/source/generic/pst-pdgr
%{texmfdist}/source/generic/pst-slpe
%{texmfdist}/source/generic/pst-soroban
%{texmfdist}/source/generic/pst-text
%{texmfdist}/source/generic/pst-uml
%{texmfdist}/source/generic/pst-vue3d
%{texmfdist}/source/latex/auto-pst-pdf
%{texmfdist}/source/latex/pst-gr3d
%{texmfdist}/source/latex/pst-pdf
%{texmfdist}/source/latex/pst-poly
%{texmfdist}/tex/generic/pst-asr
%{texmfdist}/tex/generic/pst-barcode
%{texmfdist}/tex/generic/pst-blur
%{texmfdist}/tex/generic/pst-coil
%{texmfdist}/tex/generic/pst-cox
%{texmfdist}/tex/generic/pst-eps
%{texmfdist}/tex/generic/pst-fill
%{texmfdist}/tex/generic/pst-geo
%{texmfdist}/tex/generic/pst-ghsb
%{texmfdist}/tex/generic/pst-gr3d
%{texmfdist}/tex/generic/pst-grad
%{texmfdist}/tex/generic/pst-jtree
%{texmfdist}/tex/generic/pst-labo
%{texmfdist}/tex/generic/pst-lens
%{texmfdist}/tex/generic/pst-light3d
%{texmfdist}/tex/generic/pst-osci
%{texmfdist}/tex/generic/pst-pad
%{texmfdist}/tex/generic/pst-pdgr
%{texmfdist}/tex/generic/pst-poly
%{texmfdist}/tex/generic/pst-qtree
%{texmfdist}/tex/generic/pst-slpe
%{texmfdist}/tex/generic/pst-solides3d
%{texmfdist}/tex/generic/pst-spectra
%{texmfdist}/tex/generic/pst-stru
%{texmfdist}/tex/generic/pst-vue3d
%{texmfdist}/tex/latex/pst-asr
%{texmfdist}/tex/latex/pst-barcode
%{texmfdist}/tex/latex/pst-blur
%{texmfdist}/tex/latex/pst-coil
%{texmfdist}/tex/latex/pst-cox
%{texmfdist}/tex/latex/pst-dbicons
%{texmfdist}/tex/latex/pst-eps
%{texmfdist}/tex/latex/pst-fill
%{texmfdist}/tex/latex/pst-geo
%{texmfdist}/tex/latex/pst-ghsb
%{texmfdist}/tex/latex/pst-gr3d
%{texmfdist}/tex/latex/pst-grad
%{texmfdist}/tex/latex/pst-jtree
%{texmfdist}/tex/latex/pst-labo
%{texmfdist}/tex/latex/pst-lens
%{texmfdist}/tex/latex/pst-light3d
%{texmfdist}/tex/latex/pst-osci
%{texmfdist}/tex/latex/pst-pad
%{texmfdist}/tex/latex/pst-pdf
%{texmfdist}/tex/latex/pst-pdgr
%{texmfdist}/tex/latex/pst-poly
%{texmfdist}/tex/latex/pst-qtree
%{texmfdist}/tex/latex/pst-slpe
%{texmfdist}/tex/latex/pst-solides3d
%{texmfdist}/tex/latex/pst-soroban
%{texmfdist}/tex/latex/pst-spectra
%{texmfdist}/tex/latex/pst-stru
%{texmfdist}/tex/latex/pst-uml
%{texmfdist}/tex/latex/pst-vue3d

%files latex-psnfss
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/psnfss
%{texmfdist}/fonts/map/dvips/psnfss
%{texmfdist}/source/latex/psnfss
%{texmfdist}/source/latex/latex-tds
%{texmfdist}/tex/latex/psnfss

%files latex-pxfonts
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/pxfonts

%files latex-SIstyle
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/SIstyle
%{texmfdist}/source/latex/SIstyle
%{texmfdist}/tex/latex/SIstyle

%files latex-SIunits
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/SIunits
%{texmfdist}/tex/latex/SIunits
%{texmfdist}/source/latex/SIunits

%files latex-siunitx
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/siunitx
%{texmfdist}/tex/latex/siunitx
%{texmfdist}/source/latex/siunitx

%files latex-Tabbing
%defattr(644,root,root,755)
%{texmfdist}/source/latex/Tabbing
%{texmfdist}/doc/latex/Tabbing

%files latex-txfonts
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/txfonts

%files latex-ucs
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ucs
%{texmfdist}/tex/latex/ucs

%files latex-umlaute
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/umlaute
%{texmfdist}/source/latex/umlaute

%files latex-variations
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/variations
%{texmfdist}/tex/generic/variations

%files latex-wasysym
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/wasysym
%{texmfdist}/tex/latex/wasysym
%{texmfdist}/source/latex/wasysym

%files latex-xcolor
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/xcolor
%{texmfdist}/source/latex/xcolor

%files format-pdflatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdflatex
%{fmtdir}/pdftex/pdflatex.fmt
%{_mandir}/man1/pdflatex.1*

%files tex-babel
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/babel
%{texmfdist}/source/generic/babel
%{texmfdist}/tex/generic/babel

%files tex-german
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/german
%{texmfdist}/tex/generic/german
%{texmfdist}/source/generic/german

%files tex-mfpic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/mfpic
%{texmfdist}/tex/generic/mfpic
%{texmfdist}/source/generic/mfpic

%files tex-midnight
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/midnight
%{texmfdist}/tex/generic/midnight

%files tex-misc
%defattr(644,root,root,755)
%{texmfdist}/source/generic/tap
%doc %{texmfdist}/doc/generic/multido
%doc %{texmfdist}/doc/generic/tap
%doc %{texmfdist}/doc/generic/vrb

%{texmfdist}/tex/generic/eijkhout
%{texmfdist}/tex/generic/multido
%{texmfdist}/tex/generic/misc/mproof.tex
%{texmfdist}/tex/generic/vrb

%files tex-pictex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pictex
%{texmfdist}/tex/generic/pictex

%files tex-psizzl
%defattr(644,root,root,755)
%{texmfdist}/doc/psizzl
%{texmfdist}/source/psizzl
%{texmfdist}/tex/psizzl

%files tex-pstricks
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pstricks
%doc %{texmfdist}/doc/generic/pstricks-add
%{texmfdist}/source/generic/pstricks-add
%{texmfdist}/tex/generic/pstricks
%{texmfdist}/tex/generic/pstricks-add
%{texmfdist}/tex/latex/pstricks-add

%files tex-qpxqtx
%defattr(644,root,root,755)
%{texmfdist}/tex/generic/qpxqtx

%files tex-ruhyphen
%defattr(644,root,root,755)
%{texmfdist}/tex/generic/ruhyphen
%{texmfdist}/source/generic/ruhyphen

%files tex-huhyphen
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/huhyphen

%files tex-spanish
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/spanish-mx
%{texmfdist}/tex/latex/spanish-mx

%files tex-texdraw
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/texdraw
%{texmfdist}/tex/generic/texdraw

%files tex-thumbpdf
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/thumbpdf
%attr(755,root,root) %{_bindir}/thumbpdf
%{_mandir}/man1/thumbpdf.1*
%{texmfdist}/tex/generic/thumbpdf
%{texmfdist}/scripts/thumbpdf

%files tex-ukrhyph
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/ukrhyph
%{texmfdist}/tex/generic/ukrhyph

%files latex-vietnam
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/vntex
%{texmfdist}/tex/latex/vntex

%files tex-xypic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/xypic
%{texmfdist}/tex/generic/xypic

%files tex-xkeyval
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/xkeyval
%{texmfdist}/source/latex/xkeyval
%{texmfdist}/tex/generic/xkeyval
%{texmfdist}/tex/latex/xkeyval

%files fonts-adobe
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/adobe
%{texmfdist}/fonts/afm/adobe
%{texmfdist}/fonts/tfm/adobe
%{texmfdist}/fonts/vf/adobe

%files fonts-larm
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/la
%{texmfdist}/fonts/type1/la/
%{texmfdist}/fonts/enc/larm.enc

%files fonts-ae
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/ae
%{texmfdist}/fonts/tfm/public/ae
%{texmfdist}/fonts/vf/public/ae
%{texmfdist}/source/fonts/ae

%files fonts-ams
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/ams
%{texmfdist}/fonts/tfm/public/ams
%{texmfdist}/fonts/map/dvips/ams

%files fonts-antp
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/antp
%{texmfdist}/fonts/enc/dvips/antp
%{texmfdist}/fonts/map/dvips/antp
%{texmfdist}/fonts/afm/public/antp
%{texmfdist}/fonts/tfm/public/antp

%files fonts-antt
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/antt
%{texmfdist}/fonts/afm/public/antt
%{texmfdist}/fonts/enc/dvips/antt
%{texmfdist}/fonts/map/dvips/antt
%{texmfdist}/fonts/opentype/public/antt
%{texmfdist}/fonts/tfm/public/antt
%{texmfdist}/tex/plain/antt

%files fonts-arphic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/arphic
%{texmfdist}/fonts/afm/arphic
%{texmfdist}/fonts/tfm/arphic
%{texmfdist}/fonts/vf/arphic

%files fonts-bbm
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/bbm
%{texmfdist}/fonts/source/public/bbm
%{texmfdist}/fonts/tfm/public/bbm

%files fonts-bbold
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/bbold
%{texmfdist}/fonts/tfm/public/bbold

%files fonts-bitstream
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/bitstrea
%{texmfdist}/fonts/tfm/bitstrea
%{texmfdist}/fonts/vf/bitstrea

%files fonts-cc-pl
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cc-pl
%{texmfdist}/fonts/enc/dvips/cc-pl
%{texmfdist}/fonts/tfm/public/cc-pl
%{texmfdist}/fonts/map/dvips/cc-pl

%files fonts-cg
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/cg
%{texmfdist}/fonts/vf/cg

%files fonts-cm
%defattr(644,root,root,755)
%dir %{texmfdist}/doc/fonts
%dir %{texmfdist}/fonts/afm/bluesky
%dir %{texmfdist}/fonts/map/dvips
%dir %{texmfdist}/fonts/pk/ljfour/public
%doc %{texmfdist}/doc/fonts/cm
%{texmfdist}/fonts/afm/bluesky/ams
%{texmfdist}/fonts/afm/bluesky/cm
%{texmfdist}/fonts/map/dvips/cm
%{texmfdist}/fonts/pk/ljfour/public/cm
%{texmfdist}/fonts/source/public/cm
%{texmfdist}/fonts/tfm/public/cm

%files fonts-cmbright
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cmbright
%{texmfdist}/fonts/tfm/public/cmbright
%{texmfdist}/source/latex/cmbright

%files fonts-cmcyr
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/cmcyr
%{texmfdist}/fonts/source/public/cmcyr
%{texmfdist}/fonts/type1/public/cmcyr
%{texmfdist}/fonts/tfm/public/cmcyr
%{texmfdist}/fonts/vf/public/cmcyr
%{texmfdist}/fonts/map/dvips/cmcyr

%files fonts-cmextra
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cmextra
%{texmfdist}/fonts/tfm/public/cmextra

%files fonts-cmsuper
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/cm-super
%{texmfdist}/fonts/afm/public/cm-super
%{texmfdist}/fonts/enc/dvips/cm-super
%{texmfdist}/fonts/map/dvips/cm-super
%{texmfdist}/fonts/map/vtex/cm-super
%{texmfdist}/fonts/type1/public/cm-super

%files fonts-concmath
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/concmath
%{texmfdist}/fonts/source/public/concmath
%{texmfdist}/fonts/tfm/public/concmath

%files fonts-concrete
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/concrete
%{texmfdist}/fonts/source/public/concrete
%{texmfdist}/fonts/tfm/public/concrete

%files fonts-cs
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cs
%{texmfdist}/fonts/enc/dvips/cs
%{texmfdist}/fonts/tfm/public/cs
%{texmfdist}/fonts/map/dvips/cs

%files fonts-ecc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/ecc
%{texmfdist}/fonts/source/public/ecc
%{texmfdist}/fonts/tfm/public/ecc

%files fonts-eurosym
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/eurosym
%{texmfdist}/fonts/source/public/eurosym
%{texmfdist}/fonts/tfm/public/eurosym
%{texmfdist}/fonts/map/dvips/eurosym
%{texmfdist}/source/fonts/eurosym
%{texmfdist}/tex/latex/eurosym

%files fonts-eulervm
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/public/eulervm
%{texmfdist}/fonts/vf/public/eulervm
%{texmfdist}/source/latex/eulervm
%{texmfdist}/tex/latex/eulervm

%files fonts-euxm
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/euxm
%{texmfdist}/fonts/tfm/public/euxm

%files fonts-gothic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/gothic
%{texmfdist}/fonts/source/public/gothic
%{texmfdist}/fonts/type1/public/gothic
%{texmfdist}/fonts/afm/public/gothic
%{texmfdist}/fonts/tfm/public/gothic
%{texmfdist}/fonts/vf/public/gothic
%{texmfdist}/fonts/map/dvips/gothic

%files fonts-hoekwater
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/hoekwater/context
%{texmfdist}/fonts/afm/hoekwater/manfnt
%{texmfdist}/fonts/afm/hoekwater/rsfs
%{texmfdist}/fonts/afm/hoekwater/stmaryrd
%dir %{texmfdist}/fonts/tfm/hoekwater
%{texmfdist}/fonts/tfm/hoekwater/context
%dir %{texmfdist}/fonts/truetype/hoekwater
%{texmfdist}/fonts/truetype/hoekwater/lmextra

%files fonts-jknappen
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/jknappen
%{texmfdist}/fonts/tfm/jknappen

%files fonts-kpfonts
%defattr(644,root,root,755)
%dir %{texmfdist}/doc/fonts
%doc %{texmfdist}/doc/fonts/kpfonts
%{texmfdist}/fonts/afm/public/kpfonts
%{texmfdist}/fonts/map/public/kpfonts
%{texmfdist}/fonts/source/public/kpfonts
%{texmfdist}/fonts/tfm/public/kpfonts
%{texmfdist}/fonts/type1/public/kpfonts
%{texmfdist}/fonts/vf/public/kpfonts
%{texmfdist}/tex/latex/kpfonts

%files fonts-latex
%defattr(644,root,root,755)
%dir %{texmfdist}/fonts/afm/bluesky/latex-fonts
%dir %{texmfdist}/fonts/map/dvips/latex-fonts
%dir %{texmfdist}/fonts/source/public/latex-fonts
%dir %{texmfdist}/fonts/tfm/public/latex-fonts
%doc %{texmfdist}/doc/latex/esint
%{texmfdist}/fonts/afm/bluesky/latex-fonts/*
%{texmfdist}/fonts/map/dvips/latex-fonts/*
%{texmfdist}/fonts/source/public/esint
%{texmfdist}/fonts/source/public/latex-fonts/*
%{texmfdist}/fonts/tfm/public/esint
%{texmfdist}/fonts/tfm/public/latex-fonts/*
%{texmfdist}/source/latex/esint
%{texmfdist}/tex/latex/esint

%files fonts-lh
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/lh
%{texmfdist}/fonts/source/lh
%{texmfdist}/source/fonts/lh
%{texmfdist}/source/latex/lh

%files fonts-lm
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/lm
%{texmfdist}/fonts/type1/public/lm
%{texmfdist}/fonts/afm/public/lm
%{texmfdist}/fonts/enc/dvips/lm
%{texmfdist}/fonts/map/dvipdfm/lm
%{texmfdist}/fonts/map/dvips/lm
%{texmfdist}/fonts/opentype/public/lm
%{texmfdist}/fonts/tfm/public/lm
%{texmfdist}/source/fonts/lm

%files fonts-marvosym
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/public/marvosym
%{texmfdist}/fonts/tfm/public/marvosym
%{texmfdist}/fonts/map/dvips/marvosym
%dir %{texmfdist}/source/fonts/eurofont/marvosym
%{texmfdist}/source/fonts/eurofont/marvosym/*.afm
%{texmfdist}/source/fonts/eurofont/marvosym/*.tex
%dir %{texmfdist}/source/fonts/eurofont/marvosym/tfmfiles
%{texmfdist}/source/fonts/eurofont/marvosym/tfmfiles/original

%files fonts-mflogo
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/mflogo
%{texmfdist}/fonts/afm/hoekwater/mflogo
%{texmfdist}/fonts/map/dvips/mflogo
%{texmfdist}/fonts/tfm/public/mflogo
%{texmfdist}/fonts/type1/hoekwater/mflogo

%files fonts-misc
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/misc
%{texmfdist}/fonts/tfm/public/misc
%{texmfdist}/fonts/misc

%files fonts-monotype
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/monotype
%{texmfdist}/fonts/vf/monotype

%files fonts-other
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/yi4latex
%{texmf}/fonts/sfd
%{texmfdist}/fonts/afm/itc
%{texmf}/fonts/map/glyphlist
%{texmfdist}/fonts/map/glyphlist
%{texmfdist}/fonts/source/public/knuthotherfonts
%{texmfdist}/fonts/source/public/yi4latex
%{texmfdist}/fonts/tfm/public/yi4latex

%{texmfdist}/fonts/tfm/public/pslatex
%{texmfdist}/fonts/map/dvips/pslatex
%{texmfdist}/fonts/vf/public/pslatex

%doc %{texmfdist}/doc/fonts/allrunes
%{texmfdist}/fonts/source/public/allrunes
%{texmfdist}/fonts/tfm/public/allrunes
%{texmfdist}/fonts/type1/public/allrunes
%{texmfdist}/source/fonts/allrunes

%doc %{texmfdist}/doc/fonts/antiqua
%{texmfdist}/fonts/map/dvips/antiqua

%{texmfdist}/fonts/source/public/apl
%{texmfdist}/fonts/tfm/public/apl
%{texmfdist}/source/fonts/apl

%{texmfdist}/fonts/afm/arabi
%{texmfdist}/fonts/tfm/arabi
%{texmfdist}/fonts/type1/arabi
%{texmfdist}/fonts/enc/dvips/arabi
%{texmfdist}/fonts/map/dvips/arabi

%{texmfdist}/fonts/map/dvips/arabtex
%{texmfdist}/fonts/source/public/arabtex
%{texmfdist}/fonts/tfm/public/arabtex
%{texmfdist}/fonts/type1/public/arabtex

%doc %{texmfdist}/doc/fonts/archaic
%{texmfdist}/fonts/afm/public/archaic
%{texmfdist}/fonts/map/dvips/archaic
%{texmfdist}/fonts/source/public/archaic
%{texmfdist}/fonts/tfm/public/archaic
%{texmfdist}/fonts/type1/public/archaic
%{texmfdist}/source/fonts/archaic

%doc %{texmfdist}/doc/fonts/arev
%{texmfdist}/fonts/afm/public/arev
%{texmfdist}/fonts/enc/dvips/arev
%{texmfdist}/fonts/map/dvips/arev
%{texmfdist}/fonts/tfm/public/arev
%{texmfdist}/fonts/type1/public/arev
%{texmfdist}/fonts/vf/public/arev
%{texmfdist}/source/fonts/arev

%{texmfdist}/fonts/map/dvips/vntex/arevvn.map
%{texmfdist}/fonts/tfm/vntex/arevvn
%{texmfdist}/fonts/type1/vntex/arevvn

%{texmfdist}/fonts/source/public/ar
%{texmfdist}/fonts/tfm/public/ar

%doc %{texmfdist}/doc/fonts/armenian
%{texmfdist}/fonts/source/public/armenian
%{texmfdist}/fonts/tfm/public/armenian

%{texmfdist}/fonts/map/dvips/arphic

%doc %{texmfdist}/doc/fonts/malayalam
%doc %{texmfdist}/doc/fonts/Asana-Math
%{texmfdist}/fonts/opentype/public/Asana-Math

%doc %{texmfdist}/doc/fonts/ascii
%{texmfdist}/fonts/map/dvips/ascii
%{texmfdist}/fonts/tfm/public/ascii
%{texmfdist}/fonts/type1/public/ascii

%doc %{texmfdist}/doc/fonts/astro
%{texmfdist}/fonts/source/public/astro
%{texmfdist}/fonts/tfm/public/astro

%{texmfdist}/fonts/afm/public/augie
%{texmfdist}/fonts/map/dvips/augie
%{texmfdist}/fonts/tfm/public/augie
%{texmfdist}/fonts/type1/public/augie
%{texmfdist}/fonts/vf/public/augie

%doc %{texmfdist}/doc/fonts/auncial-new
%{texmfdist}/fonts/afm/public/auncial-new
%{texmfdist}/fonts/map/dvips/auncial-new
%{texmfdist}/fonts/tfm/public/auncial-new
%{texmfdist}/fonts/type1/public/auncial-new
%{texmfdist}/source/fonts/auncial-new

%{texmfdist}/fonts/afm/public/aurical
%{texmfdist}/fonts/map/dvips/aurical
%{texmfdist}/fonts/source/public/aurical
%{texmfdist}/fonts/tfm/public/aurical
%{texmfdist}/fonts/type1/public/aurical

%{texmfdist}/fonts/map/dvips/avantgar

%{texmfdist}/fonts/source/public/bangtex
%{texmfdist}/fonts/tfm/public/bangtex

%{texmfdist}/fonts/source/public/barcodes
%{texmfdist}/fonts/tfm/public/barcodes

%{texmfdist}/fonts/source/public/bayer
%{texmfdist}/fonts/tfm/public/bayer

%{texmfdist}/fonts/source/public/bbding
%{texmfdist}/fonts/tfm/public/bbding

%{texmfdist}/fonts/truetype/public

%{texmfdist}/fonts/source/public/bengali
%{texmfdist}/fonts/tfm/public/bengali

%doc %{texmfdist}/doc/fonts/bera
%{texmfdist}/fonts/afm/public/bera
%{texmfdist}/fonts/map/dvips/bera
%{texmfdist}/fonts/map/vtex/bera
%{texmfdist}/fonts/tfm/public/bera
%{texmfdist}/fonts/type1/public/bera
%{texmfdist}/fonts/vf/public/bera

%doc %{texmfdist}/doc/fonts/blacklettert1
%{texmfdist}/fonts/tfm/public/blacklettert1
%{texmfdist}/fonts/vf/public/blacklettert1
%{texmfdist}/source/fonts/blacklettert1

%doc %{texmfdist}/doc/fonts/boisik
%{texmfdist}/fonts/source/public/boisik

%doc %{texmfdist}/doc/fonts/bookhands
%{texmfdist}/fonts/source/public/bookhands

%{texmfdist}/fonts/map/dvips/bookman

%{texmfdist}/fonts/afm/public/brushscr
%{texmfdist}/fonts/map/dvips/brushscr
%{texmfdist}/fonts/tfm/public/brushscr
%{texmfdist}/fonts/type1/public/brushscr
%{texmfdist}/fonts/vf/public/brushscr

%doc %{texmfdist}/doc/fonts/burmese
%{texmfdist}/fonts/map/dvips/burmese
%{texmfdist}/fonts/tfm/public/burmese
%{texmfdist}/fonts/type1/public/burmese

%doc %{texmfdist}/doc/fonts/cns
%{texmfdist}/fonts/tfm/cns

%{texmfdist}/fonts/enc/dvips/c90enc

%{texmfdist}/fonts/source/public/calligra
%{texmfdist}/fonts/tfm/public/calligra

%doc %{texmfdist}/doc/fonts/carolmin-ps
%{texmfdist}/fonts/afm/public/carolmin-ps
%{texmfdist}/fonts/map/dvips/carolmin-ps
%{texmfdist}/fonts/type1/public/carolmin-ps

%{texmfdist}/fonts/source/public/casyl
%{texmfdist}/fonts/tfm/public/casyl

%{texmfdist}/fonts/source/public/cbcoptic
%{texmfdist}/fonts/tfm/public/cbcoptic
%{texmfdist}/fonts/type1/public/cbcoptic

%doc %{texmfdist}/doc/fonts/cbfonts
%{texmfdist}/fonts/enc/dvips/cbfonts
%{texmfdist}/fonts/map/dvips/cbfonts
%{texmfdist}/fonts/source/public/cbfonts
%{texmfdist}/fonts/tfm/public/cbfonts
%{texmfdist}/fonts/type1/public/cbfonts

%doc %{texmfdist}/doc/fonts/charter
%{texmfdist}/fonts/afm/vntex/chartervn
%{texmfdist}/fonts/map/dvips/vntex/chartervn.map
%{texmfdist}/fonts/tfm/vntex/chartervn
%{texmfdist}/fonts/type1/vntex/chartervn
%{texmfdist}/fonts/vf/vntex/chartervn

%{texmfdist}/fonts/source/public/cherokee
%{texmfdist}/fonts/tfm/public/cherokee

%{texmfdist}/fonts/source/public/china2e
%{texmfdist}/fonts/tfm/public/china2e

%doc %{texmfdist}/doc/fonts/cirth
%{texmfdist}/fonts/source/public/cirth
%{texmfdist}/fonts/tfm/public/cirth

%doc %{texmfdist}/doc/fonts/cjhebrew
%{texmfdist}/fonts/afm/public/cjhebrew
%{texmfdist}/fonts/enc/dvips/cjhebrew
%{texmfdist}/fonts/map/dvips/cjhebrew
%{texmfdist}/fonts/tfm/public/cjhebrew
%{texmfdist}/fonts/type1/public/cjhebrew
%{texmfdist}/fonts/vf/public/cjhebrew

%{texmfdist}/fonts/source/public/clock
%{texmfdist}/fonts/tfm/public/clock

%doc %{texmfdist}/doc/fonts/cmastro
%{texmfdist}/fonts/source/public/cmastro
%{texmfdist}/fonts/tfm/public/cmastro

%{texmfdist}/fonts/map/dvips/vntex/cmbrightvn.map
%{texmfdist}/fonts/tfm/vntex/cmbrightvn
%{texmfdist}/fonts/type1/vntex/cmbrightvn

%{texmfdist}/fonts/type1/public/cmex

%{texmfdist}/fonts/afm/public/cm-lgc
%{texmfdist}/fonts/enc/dvips/cm-lgc
%{texmfdist}/fonts/map/dvips/cm-lgc
%{texmfdist}/fonts/ofm/public/cm-lgc
%{texmfdist}/fonts/ovf/public/cm-lgc
%{texmfdist}/fonts/tfm/public/cm-lgc
%{texmfdist}/fonts/type1/public/cm-lgc
%{texmfdist}/fonts/vf/public/cm-lgc

%doc %{texmfdist}/doc/fonts/cmpica
%{texmfdist}/fonts/source/public/cmpica
%{texmfdist}/fonts/tfm/public/cmpica

%{texmfdist}/fonts/map/dvips/vntex/comicvn.map
%{texmfdist}/fonts/tfm/vntex/comicsansvn
%{texmfdist}/fonts/type1/vntex/comicsansvn
%{texmfdist}/fonts/vf/vntex/comicsansvn

%{texmfdist}/fonts/map/dvips/vntex/concretevn.map
%{texmfdist}/fonts/tfm/vntex/concretevn
%{texmfdist}/fonts/type1/vntex/concretevn

%{texmfdist}/fonts/afm/ibm
%{texmfdist}/fonts/tfm/ibm
%{texmfdist}/fonts/vf/ibm
%{texmfdist}/fonts/map/dvips/courier
%{texmfdist}/fonts/tfm/cspsfonts-adobe
%{texmfdist}/fonts/vf/cspsfonts-adobe

%doc %{texmfdist}/doc/fonts/croatian
%{texmfdist}/fonts/source/public/croatian

%{texmfdist}/fonts/afm/public/cryst
%{texmfdist}/fonts/source/public/cryst
%{texmfdist}/fonts/tfm/public/cryst
%{texmfdist}/fonts/type1/public/cryst

%{texmfdist}/fonts/source/public/ctib
%{texmfdist}/fonts/tfm/public/ctib

%doc %{texmfdist}/doc/fonts/cyklop
%{texmfdist}/fonts/afm/public/cyklop
%{texmfdist}/fonts/enc/dvips/cyklop
%{texmfdist}/fonts/map/dvips/cyklop
%{texmfdist}/fonts/opentype/public/cyklop
%{texmfdist}/fonts/tfm/public/cyklop
%{texmfdist}/fonts/type1/public/cyklop

%{texmfdist}/fonts/source/public/dancers
%{texmfdist}/fonts/tfm/public/dancers

%doc %{texmfdist}/doc/fonts/dice
%{texmfdist}/fonts/source/public/dice
%{texmfdist}/fonts/tfm/public/dice

%doc %{texmfdist}/doc/fonts/dictsym
%{texmfdist}/fonts/afm/public/dictsym
%{texmfdist}/fonts/map/dvips/dictsym
%{texmfdist}/fonts/map/vtex/dictsym
%{texmfdist}/fonts/tfm/public/dictsym
%{texmfdist}/fonts/type1/public/dictsym

%doc %{texmfdist}/doc/fonts/dingbat
%{texmfdist}/fonts/tfm/public/dingbat
%{texmfdist}/source/fonts/dingbat

%doc %{texmfdist}/doc/fonts/doublestroke
%{texmfdist}/fonts/map/dvips/doublestroke
%{texmfdist}/fonts/source/public/doublestroke
%{texmfdist}/fonts/tfm/public/doublestroke
%{texmfdist}/fonts/type1/public/doublestroke

%doc %{texmfdist}/doc/fonts/duerer
%{texmfdist}/fonts/source/public/duerer
%{texmfdist}/fonts/tfm/public/duerer

%doc %{texmfdist}/doc/fonts/ean
%{texmfdist}/fonts/source/public/ean
%{texmfdist}/fonts/tfm/public/ean

%doc %{texmfdist}/doc/fonts/eiad
%{texmfdist}/fonts/source/public/eiad
%{texmfdist}/fonts/tfm/public/eiad

%doc %{texmfdist}/doc/fonts/elvish
%{texmfdist}/fonts/source/public/elvish
%{texmfdist}/fonts/tfm/public/elvish

%doc %{texmfdist}/doc/fonts/epigrafica
%{texmfdist}/fonts/afm/public/epigrafica
%{texmfdist}/fonts/enc/dvips/epigrafica
%{texmfdist}/fonts/map/dvips/epigrafica
%{texmfdist}/fonts/tfm/public/epigrafica
%{texmfdist}/fonts/type1/public/epigrafica
%{texmfdist}/fonts/vf/public/epigrafica

%{texmfdist}/fonts/map/dvips/epiolmec
%{texmfdist}/fonts/tfm/public/epiolmec
%{texmfdist}/fonts/type1/public/epiolmec

%doc %{texmfdist}/doc/fonts/esint-type1
%{texmfdist}/fonts/map/dvips/esint-type1
%{texmfdist}/fonts/type1/public/esint-type1

%{texmfdist}/fonts/ofm/public/ethiop
%{texmfdist}/fonts/ovf/public/ethiop
%{texmfdist}/fonts/ovp/public/ethiop
%{texmfdist}/fonts/source/public/ethiop
%{texmfdist}/fonts/tfm/public/ethiop

%{texmfdist}/fonts/map/dvips/ethiop-t1
%{texmfdist}/fonts/type1/public/ethiop-t1

%doc %{texmfdist}/doc/fonts/euro-ce
%{texmfdist}/fonts/source/public/euro-ce
%{texmfdist}/fonts/tfm/public/euro-ce

%doc %{texmfdist}/doc/fonts/eurofont
%{texmfdist}/fonts/map/dvips/eurofont
%{texmfdist}/source/fonts/eurofont/europs.*
%{texmfdist}/source/fonts/eurofont/install.sh

%doc %{texmfdist}/doc/fonts/feyn
%{texmfdist}/fonts/source/public/feyn
%{texmfdist}/fonts/tfm/public/feyn
%{texmfdist}/source/fonts/feyn

%doc %{texmfdist}/doc/fonts/fge
%{texmfdist}/fonts/source/public/fge
%{texmfdist}/fonts/tfm/public/fge
%{texmfdist}/source/fonts/fge

%{texmfdist}/fonts/map/dvips/foekfont
%{texmfdist}/fonts/tfm/public/foekfont
%{texmfdist}/fonts/type1/public/foekfont

%doc %{texmfdist}/doc/fonts/fonetika
%{texmfdist}/fonts/afm/public/fonetika
%{texmfdist}/fonts/map/dvips/fonetika
%{texmfdist}/fonts/tfm/public/fonetika
%{texmfdist}/fonts/type1/public/fonetika

%doc %{texmfdist}/doc/fonts/fourier
%{texmfdist}/fonts/afm/public/fourier
%{texmfdist}/fonts/map/dvips/fourier
%{texmfdist}/fonts/tfm/public/fourier
%{texmfdist}/fonts/type1/public/fourier
%{texmfdist}/fonts/vf/public/fourier
%{texmfdist}/source/fonts/fourier

%doc %{texmfdist}/doc/fonts/fouriernc
%{texmfdist}/fonts/afm/public/fouriernc
%{texmfdist}/fonts/tfm/public/fouriernc
%{texmfdist}/fonts/vf/public/fouriernc

%doc %{texmfdist}/doc/fonts/frcursive
%{texmfdist}/fonts/source/public/frcursive
%{texmfdist}/fonts/tfm/public/frcursive
%{texmfdist}/source/fonts/frcursive

%doc %{texmfdist}/doc/fonts/futhark
%{texmfdist}/fonts/source/public/futhark
%{texmfdist}/fonts/tfm/public/futhark

%{texmfdist}/fonts/afm/public/garuda
%{texmfdist}/fonts/map/dvips/garuda
%{texmfdist}/fonts/tfm/public/garuda
%{texmfdist}/fonts/type1/public/garuda

%doc %{texmfdist}/doc/fonts/genealogy
%{texmfdist}/fonts/source/public/genealogy
%{texmfdist}/fonts/tfm/public/genealogy

%doc %{texmfdist}/doc/fonts/gfsartemisia
%{texmfdist}/fonts/afm/public/gfsartemisia
%{texmfdist}/fonts/enc/dvips/gfsartemisia
%{texmfdist}/fonts/map/dvips/gfsartemisia
%{texmfdist}/fonts/opentype/public/gfsartemisia
%{texmfdist}/fonts/tfm/public/gfsartemisia
%{texmfdist}/fonts/type1/public/gfsartemisia
%{texmfdist}/fonts/vf/public/gfsartemisia

%doc %{texmfdist}/doc/fonts/gfsbaskerville
%{texmfdist}/fonts/afm/public/gfsbaskerville
%{texmfdist}/fonts/enc/dvips/gfsbaskerville
%{texmfdist}/fonts/map/dvips/gfsbaskerville
%{texmfdist}/fonts/opentype/public/gfsbaskerville
%{texmfdist}/fonts/tfm/public/gfsbaskerville
%{texmfdist}/fonts/type1/public/gfsbaskerville
%{texmfdist}/fonts/vf/public/gfsbaskerville

%doc %{texmfdist}/doc/fonts/gfsbodoni
%{texmfdist}/fonts/afm/public/gfsbodoni
%{texmfdist}/fonts/enc/dvips/gfsbodoni
%{texmfdist}/fonts/map/dvips/gfsbodoni
%{texmfdist}/fonts/opentype/public/gfsbodoni
%{texmfdist}/fonts/tfm/public/gfsbodoni
%{texmfdist}/fonts/type1/public/gfsbodoni
%{texmfdist}/fonts/vf/public/gfsbodoni

%doc %{texmfdist}/doc/fonts/gfscomplutum
%{texmfdist}/fonts/afm/public/gfscomplutum
%{texmfdist}/fonts/enc/dvips/gfscomplutum
%{texmfdist}/fonts/map/dvips/gfscomplutum
%{texmfdist}/fonts/opentype/public/gfscomplutum
%{texmfdist}/fonts/tfm/public/gfscomplutum
%{texmfdist}/fonts/type1/public/gfscomplutum
%{texmfdist}/fonts/vf/public/gfscomplutum

%doc %{texmfdist}/doc/fonts/gfsdidot
%{texmfdist}/fonts/afm/public/gfsdidot
%{texmfdist}/fonts/enc/dvips/gfsdidot
%{texmfdist}/fonts/map/dvips/gfsdidot
%{texmfdist}/fonts/opentype/public/gfsdidot
%{texmfdist}/fonts/tfm/public/gfsdidot
%{texmfdist}/fonts/type1/public/gfsdidot
%{texmfdist}/fonts/vf/public/gfsdidot

%doc %{texmfdist}/doc/fonts/gfsneohellenic
%{texmfdist}/fonts/afm/public/gfsneohellenic
%{texmfdist}/fonts/enc/dvips/gfsneohellenic
%{texmfdist}/fonts/map/dvips/gfsneohellenic
%{texmfdist}/fonts/opentype/public/gfsneohellenic
%{texmfdist}/fonts/tfm/public/gfsneohellenic
%{texmfdist}/fonts/type1/public/gfsneohellenic
%{texmfdist}/fonts/vf/public/gfsneohellenic

%doc %{texmfdist}/doc/fonts/gfsporson
%{texmfdist}/fonts/afm/public/gfsporson
%{texmfdist}/fonts/enc/dvips/gfsporson
%{texmfdist}/fonts/map/dvips/gfsporson
%{texmfdist}/fonts/opentype/public/gfsporson
%{texmfdist}/fonts/tfm/public/gfsporson
%{texmfdist}/fonts/type1/public/gfsporson
%{texmfdist}/fonts/vf/public/gfsporson

%doc %{texmfdist}/doc/fonts/gfssolomos
%{texmfdist}/fonts/afm/public/gfssolomos
%{texmfdist}/fonts/enc/dvips/gfssolomos
%{texmfdist}/fonts/map/dvips/gfssolomos
%{texmfdist}/fonts/opentype/public/gfssolomos
%{texmfdist}/fonts/tfm/public/gfssolomos
%{texmfdist}/fonts/type1/public/gfssolomos
%{texmfdist}/fonts/vf/public/gfssolomos

%doc %{texmfdist}/doc/fonts/greenpoint
%{texmfdist}/fonts/source/public/greenpoint
%{texmfdist}/fonts/tfm/public/greenpoint

%{texmfdist}/fonts/afm/groff
%{texmfdist}/fonts/enc/dvips/groff
%{texmfdist}/fonts/map/dvips/groff
%{texmfdist}/fonts/tfm/groff
%{texmfdist}/fonts/type1/groff

%doc %{texmfdist}/doc/fonts/grotesq
%{texmfdist}/fonts/map/dvips/grotesq

%{texmfdist}/fonts/afm/vntex/grotesqvn
%{texmfdist}/fonts/map/dvips/vntex/grotesqvn.map
%{texmfdist}/fonts/tfm/vntex/grotesqvn
%{texmfdist}/fonts/type1/vntex/grotesqvn

%{texmfdist}/fonts/afm/public/grverb
%{texmfdist}/fonts/map/dvips/grverb
%{texmfdist}/fonts/tfm/public/grverb
%{texmfdist}/fonts/type1/public/grverb
%{texmfdist}/fonts/vf/public/grverb

%{texmfdist}/fonts/source/public/hands
%{texmfdist}/fonts/tfm/public/hands

%{texmfdist}/fonts/afm/jmn
%{texmfdist}/fonts/tfm/jmn
%{texmfdist}/fonts/type1/jmn

%{texmfdist}/fonts/map/dvips/helvetic

%doc %{texmfdist}/doc/fonts/hfbright
%{texmfdist}/fonts/afm/public/hfbright
%{texmfdist}/fonts/enc/dvips/hfbright
%{texmfdist}/fonts/map/dvips/hfbright
%{texmfdist}/fonts/type1/public/hfbright
%{texmfdist}/source/fonts/hfbright

%doc %{texmfdist}/doc/fonts/hfoldsty
%{texmfdist}/fonts/tfm/public/hfoldsty
%{texmfdist}/fonts/vf/public/hfoldsty
%{texmfdist}/source/fonts/hfoldsty

%doc %{texmfdist}/doc/fonts/ibygrk
%{texmfdist}/tex/generic/ibygrk
%{texmfdist}/fonts/afm/public/ibygrk
%{texmfdist}/fonts/enc/dvips/ibygrk
%{texmfdist}/fonts/map/dvips/ibygrk
%{texmfdist}/fonts/source/public/ibygrk
%{texmfdist}/fonts/tfm/public/ibygrk
%{texmfdist}/fonts/type1/public/ibygrk

%doc %{texmfdist}/doc/fonts/ifsym
%{texmfdist}/fonts/source/public/ifsym
%{texmfdist}/fonts/tfm/public/ifsym

%doc %{texmfdist}/doc/fonts/initials
%{texmfdist}/fonts/afm/public/initials
%{texmfdist}/fonts/map/dvips/initials
%{texmfdist}/fonts/tfm/public/initials
%{texmfdist}/fonts/type1/public/initials

%doc %{texmfdist}/doc/fonts/itrans
%{texmfdist}/fonts/afm/public/itrans
%{texmfdist}/fonts/source/public/itrans
%{texmfdist}/fonts/tfm/public/itrans
%{texmfdist}/fonts/type1/public/itrans

%doc %{texmfdist}/doc/fonts/iwona
%{texmfdist}/fonts/afm/public/iwona
%{texmfdist}/fonts/enc/dvips/iwona
%{texmfdist}/fonts/map/dvips/iwona
%{texmfdist}/fonts/opentype/public/iwona
%{texmfdist}/fonts/tfm/public/iwona
%{texmfdist}/fonts/type1/public/iwona

%{texmfdist}/fonts/enc/dvips/jmn
%{texmfdist}/fonts/map/dvips/jmn

%doc %{texmfdist}/doc/fonts/kdgreek
%{texmfdist}/fonts/source/public/kdgreek
%{texmfdist}/fonts/tfm/public/kdgreek

%{texmfdist}/fonts/afm/public/kerkis
%{texmfdist}/fonts/enc/dvips/kerkis
%{texmfdist}/fonts/map/dvips/kerkis
%{texmfdist}/fonts/tfm/public/kerkis
%{texmfdist}/fonts/type1/public/kerkis
%{texmfdist}/fonts/vf/public/kerkis

%doc %{texmfdist}/doc/fonts/kixfont
%{texmfdist}/fonts/source/public/kixfont
%{texmfdist}/fonts/tfm/public/kixfont

%dir %{texmfdist}/fonts/map/public
%doc %{texmfdist}/doc/fonts/kurier
%{texmfdist}/fonts/afm/public/kurier
%{texmfdist}/fonts/enc/dvips/kurier
%{texmfdist}/fonts/map/dvips/kurier
%{texmfdist}/fonts/opentype/public/kurier
%{texmfdist}/fonts/tfm/public/kurier
%{texmfdist}/fonts/type1/public/kurier

%doc %{texmfdist}/doc/fonts/levy
%{texmfdist}/fonts/source/public/levy

%doc %{texmfdist}/doc/fonts/lfb
%{texmfdist}/fonts/source/public/lfb
%{texmfdist}/fonts/tfm/public/lfb

%doc %{texmfdist}/doc/fonts/libertine
%{texmfdist}/fonts/afm/public/libertine
%{texmfdist}/fonts/enc/dvips/libertine
%{texmfdist}/fonts/map/dvips/libertine
%{texmfdist}/fonts/tfm/public/libertine
%{texmfdist}/fonts/type1/public/libertine
%{texmfdist}/fonts/vf/public/libertine

%doc %{texmfdist}/doc/fonts/linearA
%{texmfdist}/fonts/afm/public/linearA
%{texmfdist}/fonts/map/dvips/linearA
%{texmfdist}/fonts/tfm/public/linearA
%{texmfdist}/fonts/type1/public/linearA
%{texmfdist}/source/fonts/linearA

%{texmfdist}/fonts/source/public/logic
%{texmfdist}/fonts/tfm/public/logic

%doc %{texmfdist}/doc/fonts/lxfonts
%{texmfdist}/fonts/map/dvips/lxfonts
%{texmfdist}/fonts/source/public/lxfonts
%{texmfdist}/fonts/tfm/public/lxfonts
%{texmfdist}/fonts/type1/public/lxfonts

%doc %{texmfdist}/doc/fonts/ly1
%{texmfdist}/fonts/map/dvips/ly1

%{texmfdist}/fonts/source/public/malayalam
%{texmfdist}/fonts/tfm/public/malayalam

%{texmfdist}/fonts/map/dvips/manfnt

%{texmfdist}/fonts/map/dvips/mathdesign

%{texmfdist}/fonts/tfm/public/mathpazo
%{texmfdist}/fonts/vf/public/mathpazo

%{texmfdist}/fonts/afm/mathdesign
%{texmfdist}/fonts/tfm/mathdesign
%{texmfdist}/fonts/type1/mathdesign
%{texmfdist}/fonts/vf/mathdesign

%{texmfdist}/fonts/enc/dvips/mnsymbol
%{texmfdist}/fonts/map/dvips/mnsymbol
%dir %{texmfdist}/fonts/map/vtex
%{texmfdist}/fonts/map/vtex/mnsymbol
%{texmfdist}/fonts/opentype/public/mnsymbol
%{texmfdist}/fonts/source/public/mnsymbol
%{texmfdist}/fonts/tfm/public/mnsymbol
%{texmfdist}/fonts/type1/public/mnsymbol

%{texmfdist}/fonts/map/dvips/montex
%{texmfdist}/fonts/source/public/montex
%{texmfdist}/fonts/tfm/public/montex
%{texmfdist}/fonts/type1/public/montex

%{texmfdist}/fonts/tfm/vntex/mscorevn
%{texmfdist}/fonts/vf/vntex/mscorevn

%doc %{texmfdist}/doc/generic/musixtex
%{texmfdist}/fonts/map/dvips/musixtex
%{texmfdist}/fonts/source/public/musixtex
%{texmfdist}/fonts/tfm/public/musixtex
%{texmfdist}/fonts/type1/public/musixtex

%{texmfdist}/fonts/source/public/mxd
%{texmfdist}/fonts/tfm/public/mxd

%{texmfdist}/fonts/source/public/mxedruli
%{texmfdist}/fonts/tfm/public/mxedruli

%{texmfdist}/fonts/map/dvips/ncntrsbk

%doc %{texmfdist}/doc/fonts/nkarta
%{texmfdist}/fonts/source/public/nkarta
%{texmfdist}/fonts/tfm/public/nkarta

%{texmfdist}/fonts/afm/public/norasi
%{texmfdist}/fonts/map/dvips/norasi
%{texmfdist}/fonts/tfm/public/norasi
%{texmfdist}/fonts/type1/public/norasi

%{texmfdist}/fonts/source/public/oca

%{texmfdist}/fonts/afm/public/ocherokee
%{texmfdist}/fonts/map/dvips/ocherokee
%{texmfdist}/fonts/ofm/public/ocherokee
%{texmfdist}/fonts/ovf/public/ocherokee
%{texmfdist}/fonts/ovp/public/ocherokee
%{texmfdist}/fonts/tfm/public/ocherokee
%{texmfdist}/fonts/type1/public/ocherokee

%{texmfdist}/fonts/source/public/ogham
%{texmfdist}/fonts/tfm/public/ogham

%doc %{texmfdist}/doc/fonts/oinuit
%{texmfdist}/fonts/map/dvips/oinuit
%{texmfdist}/fonts/ofm/public/oinuit
%{texmfdist}/fonts/ovf/public/oinuit
%{texmfdist}/fonts/tfm/public/oinuit
%{texmfdist}/fonts/type1/public/oinuit

%{texmfdist}/fonts/source/public/osmanian

%doc %{texmfdist}/doc/fonts/ot2cyr
%{texmfdist}/fonts/map/dvips/ot2cyr
%{texmfdist}/source/fonts/ot2cyr

%{texmfdist}/fonts/ofm/public/otibet
%{texmfdist}/fonts/ovf/public/otibet
%{texmfdist}/fonts/ovp/public/otibet
%{texmfdist}/fonts/source/public/otibet
%{texmfdist}/fonts/tfm/public/otibet

%doc %{texmfdist}/doc/fonts/pacioli
%{texmfdist}/fonts/source/public/pacioli
%{texmfdist}/fonts/tfm/public/pacioli

%{texmfdist}/fonts/map/dvips/palatino

%doc %{texmfdist}/doc/fonts/phaistos
%{texmfdist}/fonts/afm/public/phaistos
%{texmfdist}/fonts/map/dvips/phaistos
%{texmfdist}/fonts/opentype/public/phaistos
%{texmfdist}/fonts/tfm/public/phaistos
%{texmfdist}/fonts/type1/public/phaistos
%{texmfdist}/source/fonts/phaistos

%{texmfdist}/fonts/opentype/public/philokalia

%doc %{texmfdist}/doc/fonts/phonetic
%{texmfdist}/fonts/source/public/phonetic
%{texmfdist}/fonts/tfm/public/phonetic
%{texmfdist}/source/fonts/phonetic

%{texmfdist}/source/fonts/malayalam

%{texmfdist}/fonts/source/public/punk
%{texmfdist}/fonts/tfm/public/punk

%{texmfdist}/fonts/tfm/public/relenc
%{texmfdist}/fonts/vf/public/relenc

%doc %{texmfdist}/doc/fonts/rsfs
%{texmfdist}/fonts/map/dvips/rsfs

%{texmfdist}/fonts/map/dvips/sanskrit
%{texmfdist}/fonts/source/public/sanskrit
%{texmfdist}/fonts/tfm/public/sanskrit
%{texmfdist}/fonts/type1/public/sanskrit

%{texmfdist}/fonts/source/public/sauter

%doc %{texmfdist}/doc/fonts/semaphor
%{texmfdist}/fonts/afm/public/semaphor
%{texmfdist}/fonts/enc/dvips/semaphor
%{texmfdist}/fonts/map/dvips/semaphor
%{texmfdist}/fonts/opentype/public/semaphor
%{texmfdist}/fonts/source/public/semaphor
%{texmfdist}/fonts/tfm/public/semaphor
%{texmfdist}/fonts/type1/public/semaphor

%{texmfdist}/fonts/source/public/simpsons

%doc %{texmfdist}/doc/fonts/skaknew
%{texmfdist}/fonts/afm/public/skaknew
%{texmfdist}/fonts/map/dvips/skaknew
%{texmfdist}/fonts/map/vtex/skaknew
%{texmfdist}/fonts/tfm/public/skaknew
%{texmfdist}/fonts/type1/public/skaknew

%{texmfdist}/fonts/source/public/skull

%{texmfdist}/fonts/source/public/soyombo
%{texmfdist}/fonts/tfm/public/soyombo

%doc %{texmfdist}/doc/fonts/staves
%{texmfdist}/fonts/map/dvips/staves
%{texmfdist}/fonts/tfm/public/staves
%{texmfdist}/fonts/type1/public/staves

%{texmfdist}/fonts/map/dvips/stmaryrd
%{texmfdist}/fonts/source/public/stmaryrd

%{texmfdist}/fonts/map/dvips/symbol

%{texmfdist}/fonts/afm/public/tabvar
%{texmfdist}/fonts/map/dvips/tabvar
%{texmfdist}/fonts/tfm/public/tabvar
%{texmfdist}/fonts/type1/public/tabvar

%{texmfdist}/fonts/source/public/tapir
%{texmfdist}/fonts/type1/public/tapir

%{texmfdist}/fonts/enc/dvips/tengwarscript
%{texmfdist}/fonts/map/dvips/tengwarscript
%{texmfdist}/fonts/tfm/public/tengwarscript
%{texmfdist}/fonts/vf/public/tengwarscript

%{texmfdist}/doc/fonts/pclnfss
%{texmfdist}/source/fonts/pclnfss

%doc %{texmfdist}/doc/fonts/tex-gyre
%{texmfdist}/fonts/afm/public/tex-gyre
%{texmfdist}/fonts/enc/dvips/tex-gyre
%{texmfdist}/fonts/map/dvips/tex-gyre
%{texmfdist}/fonts/opentype/public/tex-gyre
%{texmfdist}/fonts/tfm/public/tex-gyre
%{texmfdist}/fonts/type1/public/tex-gyre

%{texmfdist}/fonts/map/dvips/times

%doc %{texmfdist}/doc/fonts/timing
%{texmfdist}/fonts/source/public/timing
%{texmfdist}/fonts/tfm/public/timing

%doc %{texmfdist}/doc/fonts/tipa
%{texmfdist}/fonts/map/dvips/tipa
%{texmfdist}/fonts/source/public/tipa
%{texmfdist}/fonts/tfm/public/tipa
%{texmfdist}/fonts/type1/public/tipa

%{texmfdist}/fonts/afm/public/trajan
%{texmfdist}/fonts/map/dvips/trajan
%{texmfdist}/fonts/tfm/public/trajan
%{texmfdist}/fonts/type1/public/trajan

%{texmfdist}/fonts/map/dvips/vntex/txttvn.map
%{texmfdist}/fonts/tfm/vntex/txttvn
%{texmfdist}/fonts/type1/vntex/txttvn

%{texmfdist}/fonts/map/dvips/uhc

%doc %{texmfdist}/doc/fonts/umtypewriter
%{texmfdist}/fonts/opentype/public/umtypewriter

%doc %{texmfdist}/doc/fonts/universa
%{texmfdist}/fonts/source/public/universa
%{texmfdist}/fonts/tfm/public/universa
%{texmfdist}/source/fonts/universa

%{texmfdist}/fonts/afm/public/velthuis
%{texmfdist}/fonts/map/dvips/velthuis
%{texmfdist}/fonts/source/public/velthuis
%{texmfdist}/fonts/tfm/public/velthuis
%{texmfdist}/fonts/type1/public/velthuis

%{texmfdist}/fonts/afm/vntex/vntopia
%{texmfdist}/fonts/map/dvips/vntex/vntopia.map
%{texmfdist}/fonts/tfm/vntex/vntopia
%{texmfdist}/fonts/type1/vntex/vntopia
%{texmfdist}/fonts/vf/vntex/vntopia

%{texmfdist}/fonts/map/dvips/wadalab

%doc %{texmfdist}/doc/fonts/wasy
%{texmfdist}/fonts/afm/public/wasy
%{texmfdist}/fonts/map/dvips/wasy
%{texmfdist}/fonts/type1/public/wasy

%{texmfdist}/fonts/source/public/wnri
%{texmfdist}/fonts/tfm/public/wnri

%{texmfdist}/fonts/source/public/wsuipa
%{texmfdist}/fonts/tfm/public/wsuipa

%{texmfdist}/fonts/source/public/xbmc
%{texmfdist}/fonts/tfm/public/xbmc

%doc %{texmfdist}/doc/fonts/xq
%{texmfdist}/fonts/source/public/xq
%{texmfdist}/fonts/tfm/public/xq

%{texmfdist}/fonts/source/public/yannisgr

%{texmfdist}/fonts/map/dvips/yhmath
%{texmfdist}/fonts/source/public/yhmath
%{texmfdist}/fonts/tfm/public/yhmath
%{texmfdist}/fonts/type1/public/yhmath
%{texmfdist}/fonts/vf/public/yhmath

%{texmfdist}/fonts/map/dvips/zapfchan
%{texmfdist}/fonts/tfm/urw35vf

%{texmfdist}/fonts/map/dvips/zapfding

%{texmfdist}/fonts/map/dvips/zefonts
%{texmfdist}/fonts/tfm/public/zefonts
%{texmfdist}/fonts/vf/public/zefonts

%files fonts-omega
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/public/omega
%{texmfdist}/fonts/map/dvips/omega
%{texmfdist}/fonts/ofm/public/omega
%{texmfdist}/fonts/ovf/public/omega
%{texmfdist}/fonts/ovp/public/omega
%{texmfdist}/fonts/tfm/public/omega
%dir %{texmfdist}/omega
%dir %{texmfdist}/omega/ocp
%{texmfdist}/omega/ocp/omega
%dir %{texmfdist}/omega/otp
%{texmfdist}/omega/otp/omega
%{texmfdist}/tex/plain/omega

%files fonts-pl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/pl
%{texmfdist}/fonts/source/public/pl
%{texmfdist}/fonts/afm/public/pl
%{texmfdist}/fonts/enc/dvips/pl
%{texmfdist}/fonts/tfm/public/pl
%{texmfdist}/fonts/map/dvips/pl

%files fonts-px
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/pxfonts
%{texmfdist}/fonts/map/dvips/pxfonts
%{texmfdist}/fonts/afm/public/pxfonts
%{texmfdist}/fonts/tfm/public/pxfonts
%{texmfdist}/fonts/vf/public/pxfonts

%files fonts-qpxqtx
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/qpxqtx
%{texmfdist}/fonts/tfm/public/qpxqtx
%{texmfdist}/fonts/vf/public/qpxqtx

%files fonts-rsfs
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/rsfs
%{texmfdist}/fonts/tfm/public/rsfs

%files fonts-stmaryrd
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/stmaryrd
%{texmfdist}/source/fonts/stmaryrd
%{texmfdist}/fonts/tfm/public/stmaryrd

%files fonts-tx
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/txfonts
%{texmfdist}/fonts/afm/public/txfonts
%{texmfdist}/fonts/enc/dvips/txfonts
%{texmfdist}/fonts/map/dvips/txfonts
%{texmfdist}/fonts/tfm/public/txfonts
%{texmfdist}/fonts/vf/public/txfonts

%files fonts-uhc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/uhc
%{texmfdist}/fonts/afm/uhc
%{texmfdist}/fonts/tfm/uhc
%{texmfdist}/fonts/vf/uhc

%files fonts-urw
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/urw
%{texmfdist}/fonts/tfm/urw
%{texmfdist}/fonts/vf/urw

%files fonts-urwvn
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/vntex/urwvn
%{texmfdist}/fonts/map/dvips/vntex/urwvn.map
%{texmfdist}/fonts/tfm/vntex/urwvn
%{texmfdist}/fonts/type1/vntex/urwvn
%{texmfdist}/fonts/vf/vntex/urwvn

%files fonts-vnr
%defattr(644,root,root,755)
%{texmfdist}/fonts/map/dvips/vntex/vnrother.map
%{texmfdist}/fonts/map/dvips/vntex/vnrtext.map
%{texmfdist}/fonts/source/vntex/vnr
%{texmfdist}/fonts/tfm/vntex/vnr

%files fonts-urw35vf
%defattr(644,root,root,755)
%{texmfdist}/fonts/vf/urw35vf

%files fonts-wadalab
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/wadalab
%{texmfdist}/fonts/afm/wadalab
%{texmfdist}/fonts/tfm/wadalab
%{texmfdist}/fonts/vf/wadalab

%files fonts-wasy
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/wasy
%{texmfdist}/fonts/tfm/public/wasy

%files fonts-xypic
%defattr(644,root,root,755)
%{texmfdist}/fonts/map/dvips/xypic
%{texmfdist}/fonts/source/public/xypic
%{texmfdist}/fonts/tfm/public/xypic

%files fonts-yandy
%defattr(644,root,root,755)
%{texmfdist}/source/fonts/eurofont/marvosym/tfmfiles/yandy

%files fonts-type1-antp
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/antp

%files fonts-type1-antt
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/antt

%files fonts-type1-arphic
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/arphic

%files fonts-type1-belleek
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/belleek
%{texmfdist}/source/latex/belleek
%{texmfdist}/fonts/type1/public/belleek
%{texmfdist}/fonts/map/dvips/belleek

%files fonts-type1-bitstream
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/bitstrea

%files fonts-type1-bluesky
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/bluesky

%files fonts-type1-cc-pl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/cc-pl
%{texmfdist}/fonts/type1/public/cc-pl

%files fonts-type1-cs
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/cs

%files fonts-type1-eurosym
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/eurosym

%files fonts-type1-fpl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/fpl
%{texmfdist}/fonts/afm/public/fpl
%{texmfdist}/fonts/type1/public/fpl
%{texmfdist}/source/fonts/fpl

%files fonts-type1-hoekwater
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/hoekwater/context
%{texmfdist}/fonts/type1/hoekwater/manfnt
%{texmfdist}/fonts/type1/hoekwater/rsfs
%{texmfdist}/fonts/type1/hoekwater/stmaryrd

%files fonts-type1-marvosym
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/marvosym

%files fonts-type1-mathpazo
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/public/mathpazo
%{texmfdist}/fonts/type1/public/mathpazo

%files fonts-type1-omega
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/omega

%files fonts-type1-pl
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/pl

%files fonts-type1-px
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/pxfonts

%files fonts-type1-tx
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/txfonts

%files fonts-type1-uhc
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/uhc

%files fonts-type1-urw
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/urw

%files fonts-type1-vnr
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/vntex/vnr

%files fonts-type1-wadalab
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/wadalab

%files fonts-type1-xypic
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/xypic

%files afm2pl
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex
%attr(755,root,root) %{_bindir}/afm2pl
%{_mandir}/man1/afm2pl.1*
%dir %{texmf}/fonts/lig
%{texmf}/fonts/lig/afm2pl
%{texmf}/tex/latex/afm2pl

%files bbox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bbox
%{_mandir}/man1/bbox.1*

%files cefutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cef*
%{texmfdist}/source/latex/cjk
%{texmfdist}/tex/latex/cjk/CEF

%files detex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/detex
%{_mandir}/man1/detex.1*

%files dviutils
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/dviasm
%dir %{texmf}/fonts/cmap
%doc %{texmf}/fonts/cmap/README
%attr(755,root,root) %{_bindir}/disdvi
%attr(755,root,root) %{_bindir}/dt2dv
%attr(755,root,root) %{_bindir}/dv2dt
%attr(755,root,root) %{_bindir}/dvi2tty
%attr(755,root,root) %{_bindir}/dviasm
%attr(755,root,root) %{_bindir}/dvibook
%attr(755,root,root) %{_bindir}/dviconcat
%attr(755,root,root) %{_bindir}/dvidvi
%attr(755,root,root) %{_bindir}/dvigif
%attr(755,root,root) %{_bindir}/dvipdfmx
%attr(755,root,root) %{_bindir}/dvipos
%attr(755,root,root) %{_bindir}/dviselect
%attr(755,root,root) %{_bindir}/dvitodvi
%attr(755,root,root) %{texmfdist}/scripts/dviasm/dviasm*
%{_mandir}/man1/dt2dv.1*
%{_mandir}/man1/dv2dt.1*
%{_mandir}/man1/dvi2tty.1*
%{_mandir}/man1/dvibook.1*
%{_mandir}/man1/dviconcat.1*
%{_mandir}/man1/dvidvi.1*
%{_mandir}/man1/dvigif.1*
%{_mandir}/man1/dvipos.1*
%{_mandir}/man1/dviselect.1*
%{_mandir}/man1/dvitodvi.1*
%{texmf}/dvipdfmx
%{texmf}/fonts/cmap/dvipdfmx
%{texmf}/fonts/map/dvipdfmx

%files psutils
%defattr(644,root,root,755)
%dir %{texmf}/scripts/ps2eps
%doc %{texmfdist}/doc/epspdf
%attr(755,root,root) %{_bindir}/epsffit
%attr(755,root,root) %{_bindir}/epspdf
%attr(755,root,root) %{_bindir}/epspdftk
%attr(755,root,root) %{_bindir}/extractres
%attr(755,root,root) %{_bindir}/fix*ps
%attr(755,root,root) %{_bindir}/getafm
%attr(755,root,root) %{_bindir}/includeres
%attr(755,root,root) %{_bindir}/ps2eps
%attr(755,root,root) %{_bindir}/psbook
%attr(755,root,root) %{_bindir}/psmerge
%attr(755,root,root) %{_bindir}/psnup
%attr(755,root,root) %{_bindir}/psresize
%attr(755,root,root) %{_bindir}/psselect
%attr(755,root,root) %{_bindir}/pst2pdf
%attr(755,root,root) %{_bindir}/pstops
%attr(755,root,root) %{_bindir}/showchar
%attr(755,root,root) %{texmf}/scripts/ps2eps/ps2eps*
%{_mandir}/man1/epsffit.1*
%{_mandir}/man1/extractres.1*
%{_mandir}/man1/fix*ps.1*
%{_mandir}/man1/getafm.1*
%{_mandir}/man1/includeres.1*
%{_mandir}/man1/ps2eps.1*
%{_mandir}/man1/psbook.1*
%{_mandir}/man1/psmerge.1*
%{_mandir}/man1/psnup.1*
%{_mandir}/man1/psresize.1*
%{_mandir}/man1/psselect.1*
%{_mandir}/man1/pstops.1*
%{texmfdist}/scripts/epspdf
%{texmf}/dvips/psutils

%files uncategorized-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/devnag

%files tex4ht
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/tex4ht
%doc %{texmfdist}/doc/generic/tex4ht
%attr(755,root,root) %{_bindir}/ht
%attr(755,root,root) %{_bindir}/htcontext
%attr(755,root,root) %{_bindir}/htlatex
%attr(755,root,root) %{_bindir}/htmex
%attr(755,root,root) %{_bindir}/httex
%attr(755,root,root) %{_bindir}/httexi
%attr(755,root,root) %{_bindir}/htxelatex
%attr(755,root,root) %{_bindir}/htxetex
%attr(755,root,root) %{_bindir}/mk4ht
%attr(755,root,root) %{_bindir}/t4ht
%attr(755,root,root) %{_bindir}/tex4ht
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/ht.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htcontext.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htlatex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htmex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/httex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/httexi.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htxelatex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htxetex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/mk4ht.pl
%{texmfdist}/tex/generic/tex4ht
%{texmfdist}/tex4ht
%{texmf}/scripts/tex4ht

%files xetex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdvipdfmx
%attr(755,root,root) %{_bindir}/xelatex
%attr(755,root,root) %{_bindir}/xetex
%doc %{texmfdist}/doc/generic/ifxetex
%doc %{texmfdist}/doc/generic/xetex-pstricks
%doc %{texmfdist}/doc/xelatex
%doc %{texmfdist}/doc/xetex
%{texmfdist}/scripts/xetex
%{texmfdist}/tex/generic/ifxetex
%{texmfdist}/tex/generic/xetexconfig
%{texmfdist}/tex/latex/latexconfig/xelatex.ini
%{texmfdist}/tex/plain/config/xetex.ini
%{texmfdist}/tex/xelatex
%{texmfdist}/tex/xetex
%{texmf}/fmtutil/format.xetex.cnf
%dir %{fmtdir}/xetex
%{fmtdir}/xetex/xetex.fmt
%{fmtdir}/xetex/xelatex.fmt

%files xmltex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfxmltex
%attr(755,root,root) %{_bindir}/xmltex
%doc %{texmfdist}/doc/xmltex
%{texmfdist}/source/xmltex
%{texmfdist}/tex/xmltex
%{texmf}/fmtutil/format.xmltex.cnf
%{fmtdir}/pdftex/pdfxmltex.fmt
%{fmtdir}/pdftex/xmltex.fmt

%files luatex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/luatex
%attr(755,root,root) %{_bindir}/lualatex
%attr(755,root,root) %{_bindir}/luatex
%attr(755,root,root) %{_bindir}/pdflualatex
%attr(755,root,root) %{_bindir}/pdfluatex
%attr(755,root,root) %{_bindir}/texlua
%attr(755,root,root) %{_bindir}/texluac
%{texmf}/fmtutil/format.luatex.cnf
%{texmfdist}/tex/latex/latexconfig/lualatex.ini
%{texmfdist}/tex/latex/latexconfig/pdflualatex.ini
%dir %{fmtdir}/luatex
%{fmtdir}/luatex/luatex.fmt
%{fmtdir}/luatex/lualatex.fmt
