# TODO:
# - get rid of /etc/cron.daily depencency from base pkg, use /etc/tmpwatch.d instead
# - cache in /var/lib? (move to /var/cache)
# - dep loops:
#error: LOOP:
#error: removing kpathsea-20080816-5.x86_64 "Requires(post): /usr/bin/texhash" from tsort relations.
#error:     kpathsea-20080816-5.x86_64               Requires(post): /usr/bin/texhash
#error: removing texlive-20080816-5.x86_64 "Requires: texconfig = 1:20080816-5" from tsort relations.
#error:     texlive-20080816-5.x86_64                Requires: texconfig = 1:20080816-5
#error: removing texconfig-20080816-5.x86_64 "Requires: texlive-dvips = 1:20080816-5" from tsort relations.
#error:     texconfig-20080816-5.x86_64              Requires: texlive-dvips = 1:20080816-5
#error: removing texlive-dvips-20080816-5.x86_64 "Requires(auto): libkpathsea.so.4()(64bit)" from tsort relations.
#error:     texlive-dvips-20080816-5.x86_64          Requires(auto): libkpathsea.so.4()(64bit)
#Preparing...                ########################################### [100%]
#
# unpackaged files:
#   /usr/bin/repstopdf
#   /usr/share/texmf-dist/scripts/pst-pdf/ps4pdf
#   /var/lib/texmf/web2c/csplain/csplain.fmt
#   /var/lib/texmf/web2c/etex/etex.fmt
#   /var/lib/texmf/web2c/lambda/lambda.fmt
#   /var/lib/texmf/web2c/lamed/lamed.fmt
#   /var/lib/texmf/web2c/latex/latex.fmt
#   /var/lib/texmf/web2c/mex/mex.fmt
#   /var/lib/texmf/web2c/mllatex/mllatex.fmt
#   /var/lib/texmf/web2c/mptopdf/mptopdf.fmt
#   /var/lib/texmf/web2c/pdfcsplain/pdfcsplain.fmt
#   /var/lib/texmf/web2c/pdfetex/pdfetex.fmt
#   /var/lib/texmf/web2c/pdflatex/pdflatex.fmt
#   /var/lib/texmf/web2c/pdftex/aleph.fmt
#   /var/lib/texmf/web2c/pdftex/lambda.fmt
#   /var/lib/texmf/web2c/pdftex/lamed.fmt
#   /var/lib/texmf/web2c/pdftex/omega.fmt
#   /var/lib/texmf/web2c/pdftex/tex.fmt
#   /var/lib/texmf/web2c/pdftex/xelatex.fmt
#   /var/lib/texmf/web2c/pdftex/xetex.fmt
#   /var/lib/texmf/web2c/physe/physe.fmt
#   /var/lib/texmf/web2c/phyzzx/phyzzx.fmt
#   /var/lib/texmf/web2c/texsis/texsis.fmt
#   /var/lib/texmf/web2c/xelatex/xelatex.fmt

# Conditional build:
%bcond_without	bootstrap	# bootstrap build
%bcond_without	xindy		# do not build xindy packages

%if %{with bootstrap}
%undefine	with_xindy
%endif

%include	/usr/lib/rpm/macros.perl

%define		year	2012
%define		monthday	0701
%define		texmfversion 20120701
Summary:	TeX typesetting system and MetaFont font formatter
Summary(de.UTF-8):	TeX-Satzherstellungssystem und MetaFont-Formatierung
Summary(es.UTF-8):	Sistema de typesetting TeX y formateador de fuentes MetaFont
Summary(fr.UTF-8):	Systéme de compostion TeX et formatteur de MetaFontes
Summary(hu.UTF-8):	TeX szövegszedő rendszer és MetaFont font formázó
Summary(pl.UTF-8):	System składu publikacji TeX oraz formater fontów MetaFont
Summary(pt_BR.UTF-8):	Sistema de typesetting TeX e formatador de fontes MetaFont
Summary(tr.UTF-8):	TeX dizgi sistemi ve MetaFont yazıtipi biçimlendiricisi
Name:		texlive
Version:	%{year}%{monthday}
Release:	0.1
Epoch:		1
License:	distributable
Group:		Applications/Publishing/TeX
Source0:	ftp://tug.org/historic/systems/texlive/%{year}/%{name}-%{version}-source.tar.xz
# Source0-md5:	1d38be7dac26440fd022a4708f454a2b
Source4:	%{name}.cron
Source5:	xdvi.desktop
Source6:	xdvi.png
Patch0:		%{name}-am.patch
Patch1:		%{name}-20080816-kpathsea-ar.patch
Patch2:		%{name}-gcc44.patch
Patch3:		%{name}-getline.patch
Patch4:		%{name}-stdio.patch
Patch5:		%{name}-aclocal.patch
Patch6:		%{name}-libpng.patch
Patch7:		icuinfo.patch
URL:		http://www.tug.org/texlive/
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
BuildRequires:	libpng-devel >= 1.2.8
BuildRequires:	libtool
# should this be somewhere in clisp?
BuildRequires:	libsigsegv
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	t1lib-devel >= 5.0.2
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
%if %{without bootstrap}
### BuildRequires:	%{name}-context
### BuildRequires:	%{name}-csplain
### BuildRequires:	%{name}-fonts-cmsuper
### #BuildRequires:	%{name}-format-amstex
### #BuildRequires:	%{name}-format-cslatex
### BuildRequires:	%{name}-format-eplain
### BuildRequires:	%{name}-format-mex
### BuildRequires:	%{name}-format-pdflatex
### BuildRequires:	%{name}-latex
### BuildRequires:	%{name}-latex-cyrillic
### BuildRequires:	%{name}-metapost
### BuildRequires:	%{name}-mex
### BuildRequires:	%{name}-omega
### BuildRequires:	%{name}-other-utils
### BuildRequires:	%{name}-pdftex
### BuildRequires:	%{name}-phyzzx
### BuildRequires:	%{name}-plain
### BuildRequires:	%{name}-tex-babel
### BuildRequires:	%{name}-tex-physe
### BuildRequires:	%{name}-xetex
### BuildRequires:	%{name}-xmltex
# fill with future texlive BR. guesses ones for now
%endif
BuildRequires:	unzip
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel >= 1.2.1
Requires:	%{name}-dirs-fonts
Requires:	%{name}-fonts-cm
Requires:	%{name}-fonts-misc
Requires:	awk
Requires:	dialog
Requires:	kpathsea = %{epoch}:%{version}-%{release}
Requires:	sed
Requires:	sh-utils
Requires:	texconfig = %{epoch}:%{version}-%{release}
Requires:	textutils
Suggests:	tmpwatch
Provides:	tetex = %{epoch}:%{version}-%{release}
Provides:	tetex-format-pdfetex = %{epoch}:%{version}-%{release}
Provides:	tetex-metafont
Obsoletes:	tetex
Obsoletes:	tetex-afm
Obsoletes:	tetex-doc
Obsoletes:	tetex-doc-latex2e-html
Obsoletes:	tetex-fontinst
Obsoletes:	tetex-fontname
Obsoletes:	tetex-fonts
Obsoletes:	tetex-fonts-pandora
Obsoletes:	tetex-fonts-vcm
Obsoletes:	tetex-format-elatex
Obsoletes:	tetex-format-pdfelatex
Obsoletes:	tetex-format-pdfemex
Obsoletes:	tetex-format-pdfetex
Obsoletes:	tetex-latex-vnps
Obsoletes:	tetex-latex-vnr
Obsoletes:	tetex-metafont
Obsoletes:	tetex-oxdvi
Obsoletes:	tetex-plain-dvips
Obsoletes:	tetex-plain-mathtime
Obsoletes:	tetex-plain-misc
Obsoletes:	tetex-plain-plnfss
Obsoletes:	tetex-tex-hyphen
Obsoletes:	tetex-tex-vietnam
Obsoletes:	texlive-metafont
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texmf	%{_datadir}/texmf
%define		texmfdist %{texmf}-dist
%define		texmfdoc %{texmf}-doc
%define		fmtdir	/var/lib/texmf/web2c
%define		texhash	umask 022; [ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2;
%define		_localstatedir	/var/lib/texmf
%define		fixinfodir [ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 ;
%define		fmtutil(f:) [ ! \\\( -f %{_localstatedir}/web2c/%{-f*}.fmt.rpmnew -o -f %{_localstatedir}/web2c/%{-f*}.efmt.rpmnew \\\) ] || %{_bindir}/fmtutil-sys --byfmt %{-f*} >/dev/null 2>/dev/null || echo "Regenerating %{-f*} failed. See %{_localstatedir}/web2c/%{-f*}.log for details" 1>&2 && exit 0 ;

%define		_noautoreq 'perl(path_tre)'
%define		skip_post_check_so libptexenc.so.1.1.1

%description
TeX Live is an implementation of TeX for Linux or UNIX systems. TeX
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
TeX Live a TeX egy implementációja Linux és UNIX rendszerekre. TeX egy
egyszerű szövegfájlt fogad bemenetként, és formázó parancsok
segítségével a szövegszedő egy független .dvi (DeVice Independent)
fájlt készít. A TeX-et leginkább magasabb szintű formázó parancsokkal
kiegészítve használják, mint pl. LaTeX-hel vagy PlainTeX-hel, mivel a
TeX önmaga nem túlzottan "felhasználóbarát".

%description -l pl.UTF-8
TeX Live to implementacja TeXa dla systemów Linux i UNIX. TeX to system
składu przyjmujący na wejściu tekst oraz polecenia formatujące i
tworzący niezależny od urządzenia plik wynikowy (tzw. DVI -- skrót od
DeVice Independent). Zwykle TeX jest używany w połączeniu z pakietem
formatującym wyższego poziomu, jak LaTeX lub PlainTeX, jako że sam TeX
nie jest zbyt przyjazny dla użytkownika.

%description -l pt_BR.UTF-8
Tex formata arquivos de texto e comandos para uma saída independente
de dispositivo (chamado DVI - DeVice Independent). As capacidades e a
linguagem TeX são descritas no The TeXbook, de Knuth.

%description -l tr.UTF-8
TeX, içinde metin ve komutların yer aldığı bir dosyayı okur ve dizgi
aygıtından bağımsız bir çıktı (DeVice Independent - DVI) oluşturur.
TeX'in becerileri ve dizgi dili, dili geliştiren Knuth'un 'The
TeXbook' başlıklı kitabında anlatılmaktadır.

%package jadetex
Summary:	LaTeX macros for converting Jade TeX output into DVI/PS/PDF
Summary(pl.UTF-8):	Makra LaTeXa do konwersji Jade TeXa do DVI/PS/PDF
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Provides:	jadetex = %{epoch}:%{version}-%{release}
Obsoletes:	jadetex

%description jadetex
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as LaTeX files.

%description jadetex -l pl.UTF-8
JadeTeX zawiera dodatkowe makra LaTeXa potrzebne do konwersji plików
otrzymanych z Jade TeXa i przetworzenia ich jako plików LaTeXa.

%package cef-utils
Summary:	Utils for CEF (Chinese Encoding Framework)
Summary(pl.UTF-8):	Narzędzia dla środowiska CEF (Chinese Encoding Framework)
Group:		Applications/Publishing/TeX

%description cef-utils
Utils for CEF (Chinese Encoding Framework).

%description cef-utils -l pl.UTF-8
Narzędzia dla środowiska CEF (Chinese Encoding Framework) służącego do
kodowania języka chińskiego.

%package other-utils
Summary:	Other TeX Live utilities
Summary(pl.UTF-8):	Pozostałe narzędzia z systemu TeX Live
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-format-cyrtexinfo

%description other-utils
Other TeX Live utilities.

%description other-utils -l pl.UTF-8
Pozostałe narzędzia z systemu TeX Live.

%package other-utils-doc
Summary:	Other utilities documentation
Summary(pl.UTF-8):	Dokumentacja do narzędzi z pakietu %{name}-other-utils-doc
Group:		Applications/Publishing/TeX

%description other-utils-doc
Other utilities documentation.

%description other-utils-doc -l pl.UTF-8
Dokumentacja do narzędzi z pakietu %{name}-other-utils-doc.

%package -n kpathsea
Summary:	File name lookup library
Summary(hu.UTF-8):	Fájlnév-kereső könyvtár
Summary(pl.UTF-8):	Biblioteka szukająca nazw plików
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

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
Requires:	%{name}-dvips-data >= %{texmfversion}
Provides:	tetex-dvips = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-dvips

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
Obsoletes:	tetex-dvilj

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
Requires:	%{name}-makeindex-data
Provides:	tetex-makeindex
Obsoletes:	tetex-makeindex
Obsoletes:	tetex-rumakeindex

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

%package metapost
Summary:	MetaPost
Summary(hu.UTF-8):	MetaPost
Summary(pl.UTF-8):	Zestaw narzędzi MetaPost
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-metapost-data >= %{texmfversion}
Obsoletes:	tetex-metapost

%description metapost
MetaPost.

%description metapost -l hu.UTF-8
MetaPost.

%description metapost -l pl.UTF-8
Zestaw narzędzi MetaPost.

%package mptopdf
Summary:	MetaPost to PDF converter
Summary(hu.UTF-8):	MetaPost-ból PDF-be konvertáló
Summary(pl.UTF-8):	Konwerter MetaPost do PDF
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-metapost = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-mptopdf

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
Obsoletes:	tetex-texdoctk

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
Summary(hu.UTF-8):	TeX szövegszedő rendszer beállítása
Summary(pl.UTF-8):	Konfigurator systemu składu TeX
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-dvips = %{epoch}:%{version}-%{release}
Requires:	xdvi = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-texconfig

%description -n texconfig
TeX typesetting system configurator.

%description -n texconfig -l hu.UTF-8
TeX szövegszedő rendszer beállítása.

%description -n texconfig -l pl.UTF-8
Konfigurator systemu składu TeX.

%package -n xdvi
Summary:	X11 previewer
Summary(de.UTF-8):	X11-Previewer
Summary(es.UTF-8):	Visualizador TeX X11
Summary(fr.UTF-8):	Prévisualisateur X11
Summary(hu.UTF-8):	X11 előnézet
Summary(pl.UTF-8):	Przeglądarka DVI dla X11
Summary(pt_BR.UTF-8):	Visualizador TeX X11
Summary(tr.UTF-8):	X11 öngörüntüleyici
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Suggests:	%{name}-dvips
Obsoletes:	tetex-xdvi

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

%description -n xdvi -l hu.UTF-8
xdvi egyprogram, amely az X Window rendszeren fut. DVI fájlok
előnézetére használjuk, amelyet tex és latex készít.

%description -n xdvi -l pl.UTF-8
Xdvi jest programem (działającym w X Window System) do przeglądania
plików DVI, produkowanych przez TeXa i LaTeXa.

%description -n xdvi -l pt_BR.UTF-8
xdvi é um programa que roda no sistema X Window. É usado para
visualizar arquivos dvi, como os produzidos por tex e latex.

%package -n xindy
Summary:	Xindy creates sorted and tagged index from raw index
Summary(hu.UTF-8):	Xindy rendezett és cimkézett indexet készít nyers indexekből
Group:		Applications/Publishing/TeX

%description -n xindy
Xindy creates sorted and tagged index from raw index.

%description -n xindy -l hu.UTF-8
Xindy rendezett és cimkézett indexet készít nyers indexekből.

%package -n xindy-albanian
Summary:	Xindy albanian language
Summary(hu.UTF-8):	Xindy albán nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-albanian
Xindy albanian language

%description -n xindy-albanian -l hu.UTF-8
Xindy albán nyelv

%package -n xindy-belarusian
Summary:	Xindy belarusian language
Summary(hu.UTF-8):	Xindy belorusz nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-belarusian
Xindy belarusian language

%description -n xindy-belarusian -l hu.UTF-8
Xindy belorusz nyelv

%package -n xindy-bulgarian
Summary:	Xindy bulgarian language
Summary(hu.UTF-8):	Xindy bolgár nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-bulgarian
Xindy bulgarian language

%description -n xindy-bulgarian -l hu.UTF-8
Xindy bolgár nyelv

%package -n xindy-croatian
Summary:	Xindy croatian language
Summary(hu.UTF-8):	Xindy horvát nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-croatian
Xindy croatian language

%description -n xindy-croatian -l hu.UTF-8
Xindy horvát nyelv

%package -n xindy-czech
Summary:	Xindy czech language
Summary(hu.UTF-8):	Xindy cseh nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-czech
Xindy czech language

%description -n xindy-czech -l hu.UTF-8
Xindy cseh nyelv

%package -n xindy-danish
Summary:	Xindy danish language
Summary(hu.UTF-8):	Xindy dán nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-danish
Xindy danish language

%description -n xindy-danish -l hu.UTF-8
Xindy dán nyelv

%package -n xindy-dutch
Summary:	Xindy dutch language
Summary(hu.UTF-8):	Xindy holland nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-dutch
Xindy dutch language

%description -n xindy-dutch -l hu.UTF-8
Xindy holland nyelv

%package -n xindy-english
Summary:	Xindy english language
Summary(hu.UTF-8):	Xindy angol nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-english
Xindy english language

%description -n xindy-english -l hu.UTF-8
Xindy angol nyelv

%package -n xindy-esperanto
Summary:	Xindy esperanto language
Summary(hu.UTF-8):	Xindy eszperantó nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-esperanto
Xindy esperanto language

%description -n xindy-esperanto -l hu.UTF-8
Xindy eszperantó nyelv

%package -n xindy-estonian
Summary:	Xindy estonian language
Summary(hu.UTF-8):	Xindy észt nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-estonian
Xindy estonian language

%description -n xindy-estonian -l hu.UTF-8
Xindy észt nyelv

%package -n xindy-finnish
Summary:	Xindy finnish language
Summary(hu.UTF-8):	Xindy finn nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-finnish
Xindy finnish language

%description -n xindy-finnish -l hu.UTF-8
Xindy finn nyelv

%package -n xindy-french
Summary:	Xindy french language
Summary(hu.UTF-8):	Xindy francia nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-french
Xindy french language

%description -n xindy-french -l hu.UTF-8
Xindy francia nyelv

%package -n xindy-general
Summary:	Xindy general language
Summary(hu.UTF-8):	Xindy általános nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-general
Xindy general language

%description -n xindy-general -l hu.UTF-8
Xindy általános nyelv

%package -n xindy-georgian
Summary:	Xindy georgian language
Summary(hu.UTF-8):	Xindy georgian nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-georgian
Xindy georgian language

%description -n xindy-georgian -l hu.UTF-8
Xindy georgian nyelv

%package -n xindy-german
Summary:	Xindy german language
Summary(hu.UTF-8):	Xindy német nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-german
Xindy german language

%description -n xindy-german -l hu.UTF-8
Xindy német nyelv

%package -n xindy-greek
Summary:	Xindy greek language
Summary(hu.UTF-8):	Xindy görög nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-greek
Xindy greek language

%description -n xindy-greek -l hu.UTF-8
Xindy görög nyelv

%package -n xindy-gypsy
Summary:	Xindy gypsy language
Summary(hu.UTF-8):	Xindy cigány nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-gypsy
Xindy gypsy language

%description -n xindy-gypsy -l hu.UTF-8
Xindy cigány nyelv

%package -n xindy-hausa
Summary:	Xindy hausa language
Summary(hu.UTF-8):	Xindy hausa nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-hausa
Xindy hausa language

%description -n xindy-hausa -l hu.UTF-8
Xindy hausa nyelv

%package -n xindy-hebrew
Summary:	Xindy hebrew language
Summary(hu.UTF-8):	Xindy héber nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-hebrew
Xindy hebrew language

%description -n xindy-hebrew -l hu.UTF-8
Xindy héber nyelv

%package -n xindy-hungarian
Summary:	Xindy hungarian language
Summary(hu.UTF-8):	Xindy magyar nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-hungarian
Xindy hungarian language

%description -n xindy-hungarian -l hu.UTF-8
Xindy magyar nyelv

%package -n xindy-icelandic
Summary:	Xindy icelandic language
Summary(hu.UTF-8):	Xindy izlandi nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-icelandic
Xindy icelandic language

%description -n xindy-icelandic -l hu.UTF-8
Xindy izlandi nyelv

%package -n xindy-italian
Summary:	Xindy italian language
Summary(hu.UTF-8):	Xindy olasz nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-italian
Xindy italian language

%description -n xindy-italian -l hu.UTF-8
Xindy olasz nyelv

%package -n xindy-klingon
Summary:	Xindy klingon language
Summary(hu.UTF-8):	Xindy klingon nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-klingon
Xindy klingon language

%description -n xindy-klingon -l hu.UTF-8
Xindy klingon nyelv

%package -n xindy-kurdish
Summary:	Xindy kurdish language
Summary(hu.UTF-8):	Xindy kurd nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-kurdish
Xindy kurdish language

%description -n xindy-kurdish -l hu.UTF-8
Xindy kurd nyelv

%package -n xindy-latin
Summary:	Xindy latin language
Summary(hu.UTF-8):	Xindy latin nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-latin
Xindy latin language

%description -n xindy-latin -l hu.UTF-8
Xindy latin nyelv

%package -n xindy-latvian
Summary:	Xindy latvian language
Summary(hu.UTF-8):	Xindy lett nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-latvian
Xindy latvian language

%description -n xindy-latvian -l hu.UTF-8
Xindy lett nyelv

%package -n xindy-lithuanian
Summary:	Xindy lithuanian language
Summary(hu.UTF-8):	Xindy litván nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-lithuanian
Xindy lithuanian language

%description -n xindy-lithuanian -l hu.UTF-8
Xindy litván nyelv

%package -n xindy-lower-sorbian
Summary:	Xindy lower-sorbian language
Summary(hu.UTF-8):	Xindy lower-sorbian nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-lower-sorbian
Xindy lower-sorbian language

%description -n xindy-lower-sorbian -l hu.UTF-8
Xindy lower-sorbian nyelv

%package -n xindy-macedonian
Summary:	Xindy macedonian language
Summary(hu.UTF-8):	Xindy macedón nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-macedonian
Xindy macedonian language

%description -n xindy-macedonian -l hu.UTF-8
Xindy macedón nyelv

%package -n xindy-mongolian
Summary:	Xindy mongolian language
Summary(hu.UTF-8):	Xindy mongol nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-mongolian
Xindy mongolian language

%description -n xindy-mongolian -l hu.UTF-8
Xindy mongol nyelv

%package -n xindy-norwegian
Summary:	Xindy norwegian language
Summary(hu.UTF-8):	Xindy norvég nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-norwegian
Xindy norwegian language

%description -n xindy-norwegian -l hu.UTF-8
Xindy norvég nyelv

%package -n xindy-polish
Summary:	Xindy polish language
Summary(hu.UTF-8):	Xindy lengyel nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-polish
Xindy polish language

%description -n xindy-polish -l hu.UTF-8
Xindy lengyel nyelv

%package -n xindy-portuguese
Summary:	Xindy portuguese language
Summary(hu.UTF-8):	Xindy portugál nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-portuguese
Xindy portuguese language

%description -n xindy-portuguese -l hu.UTF-8
Xindy portugál nyelv

%package -n xindy-romanian
Summary:	Xindy romanian language
Summary(hu.UTF-8):	Xindy román nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-romanian
Xindy romanian language

%description -n xindy-romanian -l hu.UTF-8
Xindy román nyelv

%package -n xindy-russian
Summary:	Xindy russian language
Summary(hu.UTF-8):	Xindy orosz nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-russian
Xindy russian language

%description -n xindy-russian -l hu.UTF-8
Xindy orosz nyelv

%package -n xindy-serbian
Summary:	Xindy serbian language
Summary(hu.UTF-8):	Xindy szerb nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-serbian
Xindy serbian language

%description -n xindy-serbian -l hu.UTF-8
Xindy szerb nyelv

%package -n xindy-slovak
Summary:	Xindy slovak language
Summary(hu.UTF-8):	Xindy szlovák nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-slovak
Xindy slovak language

%description -n xindy-slovak -l hu.UTF-8
Xindy szlovák nyelv

%package -n xindy-slovenian
Summary:	Xindy slovenian language
Summary(hu.UTF-8):	Xindy szlovén nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-slovenian
Xindy slovenian language

%description -n xindy-slovenian -l hu.UTF-8
Xindy szlovén nyelv

%package -n xindy-spanish
Summary:	Xindy spanish language
Summary(hu.UTF-8):	Xindy spanyol nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-spanish
Xindy spanish language

%description -n xindy-spanish -l hu.UTF-8
Xindy spanyol nyelv

%package -n xindy-swedish
Summary:	Xindy swedish language
Summary(hu.UTF-8):	Xindy svéd nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-swedish
Xindy swedish language

%description -n xindy-swedish -l hu.UTF-8
Xindy svéd nyelv

%package -n xindy-turkish
Summary:	Xindy turkish language
Summary(hu.UTF-8):	Xindy török nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-turkish
Xindy turkish language

%description -n xindy-turkish -l hu.UTF-8
Xindy török nyelv

%package -n xindy-ukrainian
Summary:	Xindy ukrainian language
Summary(hu.UTF-8):	Xindy ukrán nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-ukrainian
Xindy ukrainian language

%description -n xindy-ukrainian -l hu.UTF-8
Xindy ukrán nyelv

%package -n xindy-upper-sorbian
Summary:	Xindy upper-sorbian language
Summary(hu.UTF-8):	Xindy upper-sorbian nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-upper-sorbian
Xindy upper-sorbian language

%description -n xindy-upper-sorbian -l hu.UTF-8
Xindy upper-sorbian nyelv

%package -n xindy-vietnamese
Summary:	Xindy vietnamese language
Summary(hu.UTF-8):	Xindy vietnámi nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-vietnamese
Xindy vietnamese language

%description -n xindy-vietnamese -l hu.UTF-8
Xindy vietnám nyelv

%package pdftex
Summary:	TeX generating PDF files instead DVI
Summary(hu.UTF-8):	PDF fájlok készítése DVI helyett TeX-ből
Summary(pl.UTF-8):	TeX generujący pliki PDF zamiast DVI
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
# ams provides bluesky fonts
Requires:	%{name}-fonts-ams >= %{texmfversion}
Requires:	ghostscript
Provides:	tetex-format-pdftex = %{epoch}:%{version}-%{release}
Provides:	tetex-pdftex
Obsoletes:	tetex-format-pdftex
Obsoletes:	tetex-pdftex

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
Obsoletes:	psutils
Obsoletes:	texlive-epsutils
Obsoletes:	texlive-filters

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
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description phyzzx
A TeX format for physicists.

%description phyzzx -l hu.UTF-8
TeX formátum fizikusoknak.

%package omega
Summary:	Extended unicode TeX
Summary(pl.UTF-8):	Omega - TeX ze wsparciem dla unikodu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-omega >= %{texmfversion}
Requires:	%{name}-omega-data >= %{texmfversion}
Requires:	%{name}-plain >= %{texmfversion}
Obsoletes:	tetex-omega

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
Obsoletes:	tetex-cyrplain
Obsoletes:	tetex-format-cyrplain
Obsoletes:	tetex-format-plain
Obsoletes:	tetex-plain

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
Requires:	%{name}-fonts-pl >= %{texmfversion}
Requires:	%{name}-plain >= %{texmfversion}
Obsoletes:	tetex-mex

%description mex
MeX Plain Format basic files.

%description mex -l pl.UTF-8
Podstawowe pliki dla formatu MeX Plain.

%package format-mex
Summary:	MeX Plain Format
Summary(pl.UTF-8):	Format MeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-mex >= %{texmfversion}
Obsoletes:	tetex-format-mex

%description format-mex
MeX Plain Format.

%description format-mex -l pl.UTF-8
Format MeX Plain.

%package format-pdfmex
Summary:	PDFMeX Plain Format
Summary(pl.UTF-8):	Format PDFMeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-mex >= %{texmfversion}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-pdfmex

%description format-pdfmex
PDFMeX Plain Format.

%description format-pdfmex -l pl.UTF-8
Format PDFMeX Plain.

%package format-utf8mex
Summary:	MeX Plain Format with UTF-8 encoded source files
Summary(pl.UTF-8):	Format MeX Plain z plikami źródłowymi kodowanymi UTF-8
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-mex >= %{texmfversion}
Obsoletes:	tetex-format-utf8mex

%description format-utf8mex
MeX Plain Format with UTF-8 encoded source files.

%description format-utf8mex -l pl.UTF-8
Format MeX Plain z plikami źródłowymi kodowanymi UTF-8.

%package format-amstex
Summary:	AMS macros for Plain TeX
Summary(pl.UTF-8):	Makra AMS dla formatu Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-amstex >= %{texmfversion}
Obsoletes:	tetex-format-amstex
Obsoletes:	tetex-format-cyramstex

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
Requires:	%{name}-fonts-cs >= %{texmfversion}
Requires:	%{name}-plain >= %{texmfversion}
Provides:	tetex-csplain
Obsoletes:	tetex-csplain

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
Obsoletes:	tetex-format-csplain

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
Obsoletes:	tetex-format-pdfcsplain

%description format-pdfcsplain
PDFTeX CSPlain format.

%description format-pdfcsplain -l pl.UTF-8
Format PDFTeX CSPlain.

%package format-cslatex
Summary:	CSLaTeX format
Summary(pl.UTF-8):	Format CSLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-cslatex >= %{texmfversion}
Obsoletes:	tetex-format-cslatex

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
Obsoletes:	tetex-format-pdfcslatex

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
Requires:	%{name}-plain >= %{texmfversion}
Obsoletes:	tetex-eplain
Obsoletes:	tetex-etex

%description eplain
EPlain format basic files.

%description eplain -l pl.UTF-8
Podstawowe pliki dla formatu EPlain.

%package format-eplain
Summary:	EPlain format
Summary(pl.UTF-8):	Format EPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-eplain >= %{texmfversion}
Obsoletes:	tetex-format-eplain

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
Requires:	%{name}-context-data >= %{texmfversion}
Provides:	tetex-context
Obsoletes:	tetex-context

%define		_noautoreq	'perl(path_tre)'

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
Obsoletes:	tetex-format-context-de

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
Obsoletes:	tetex-format-context-en

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
Obsoletes:	tetex-format-context-nl

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
Requires:	%{name}-fonts-latex
Requires:	%{name}-tex-ruhyphen
Requires:	%{name}-tex-ukrhyph
# for misc/eurosym:
Requires:	%{name}-fonts-eurosym
Requires:	%{name}-latex-data
Requires:	%{name}-pdftex
Requires:	%{name}-tex-babel
Requires:	%{name}-tex-pstricks
Suggests:	%{name}-fonts-jknappen
Suggests:	%{name}-latex-ucs
# Provides:	tetex-format-latex = %{epoch}:%{version}-%{release}
# Provides:	tetex-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-koma-script
# Can't install texlive-latex-data, so must delete
# Obsoletes:	tetex-format-latex
# Obsoletes:	tetex-latex
Obsoletes:	tetex-latex-SIunits
Obsoletes:	tetex-latex-caption
Obsoletes:	tetex-latex-curves
Obsoletes:	tetex-latex-dinbrief
Obsoletes:	tetex-latex-draftcopy
Obsoletes:	tetex-latex-dstroke
Obsoletes:	tetex-latex-dvilj
Obsoletes:	tetex-latex-eepic
Obsoletes:	tetex-latex-endfloat
Obsoletes:	tetex-latex-fancyhdr
Obsoletes:	tetex-latex-fancyheadings
Obsoletes:	tetex-latex-fancyvrb
Obsoletes:	tetex-latex-fp
Obsoletes:	tetex-latex-graphics
Obsoletes:	tetex-latex-hyperref
Obsoletes:	tetex-latex-koma-script
Obsoletes:	tetex-latex-labels
Obsoletes:	tetex-latex-listings
Obsoletes:	tetex-latex-misc
Obsoletes:	tetex-latex-ms
Obsoletes:	tetex-latex-multirow
Obsoletes:	tetex-latex-mwcls
Obsoletes:	tetex-latex-mwdtools
Obsoletes:	tetex-latex-natbib
Obsoletes:	tetex-latex-ntgclass
Obsoletes:	tetex-latex-oberdiek
Obsoletes:	tetex-latex-pb-diagram
Obsoletes:	tetex-latex-pstricks
Obsoletes:	tetex-latex-qfonts
Obsoletes:	tetex-latex-revtex4
Obsoletes:	tetex-latex-seminar
Obsoletes:	tetex-latex-t2
Obsoletes:	tetex-latex-titlesec
Obsoletes:	tetex-latex-tools
Obsoletes:	tetex-latex-units
Obsoletes:	tetex-mwcls
Obsoletes:	tetex-revtex4

%define		skip_post_check_so		libptexenc.so.1.2.0

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

%package latex-bibtex
Summary:	Bibliography management for LaTeX
Summary(pl.UTF-8):	Zarządzenie bibliografią dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-bibtex-data >= %{texmfversion}
Provides:	tetex-latex-bibtex
Obsoletes:	tetex-bibtex
Obsoletes:	tetex-latex-bibtex
Obsoletes:	tetex-natbib
Obsoletes:	tetex-rubibtex

%description latex-bibtex
Bibliography management for LaTeX.

%description latex-bibtex -l pl.UTF-8
Zarządzanie bibliografią dla LaTeXa.

%package latex-presentation-bin
Summary:	Presentations in LaTeX
Summary(hu.UTF-8):	Prezentációk LaTeX-ben
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-foiltex >= %{texmfversion}
Requires:	luatex
Suggests:	%{name}-latex-prosper = %{epoch}:%{version}-%{release}

%description latex-presentation-bin
This package contains:
- powerdot: a presentation class.
- ppower4: a postprocessor for PDF presentations.
- sciposter: make posters of ISO A3 size and larger.
- tpslifonts: a LaTeX package for configuring presentation fonts.

%description latex-presentation-bin -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- powerdot: egy prezentáció osztály
- ppower4: egy postprocesszor PDF prezentációkhoz
- sciposter: poszterek készítése A3-as és nagyobb méretben
- tpslifonts: a LaTeX package for configuring presentation fonts.

%package format-pdflatex
Summary:	PDF LaTeX macro package
Summary(pl.UTF-8):	Pakiet makr PDF LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-jknappen
Requires:	%{name}-fonts-type1-urw
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-psnfss
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Provides:	tetex-format-pdflatex
Obsoletes:	tetex-format-pdflatex

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
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description scripts
Various scripts.

%description scripts -l hu.UTF-8
Néhány szkript.

%package tlmgr
Summary:	TeXLive manager
Summary(hu.UTF-8):	TeXLive manager
Group:		Applications/Publishing/TeX

%description tlmgr
tlmgr manages an existing TeX Live installation, both packages and
configuration options. It performs many of the same actions as
texconfig, and more besides.

%description tlmgr -l hu.UTF-8
tlmgr egy létező TeX Live telepítést tart karban, csomag és beállítás
tekintetében is. Hasonló műveleteket végez, mint a texconfig, sőt,
többet is.

# # TeX generic macros #

%package tex-babel
Summary:	Multilingual support for TeX
Summary(pl.UTF-8):	Obsługa wielu języków dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-babel
Obsoletes:	tetex-tex-babel

%description tex-babel
Multilingual support for TeX.

%description tex-babel -l pl.UTF-8
Obsługa wielu języków dla TeXa.

%package tex-thumbpdf
Summary:	Thumbnails for PDFTeX and dvips/ps2pdf
Summary(pl.UTF-8):	Ikonki dla PDFTeXa i dvips/ps2pdf
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-thumbpdf

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

%package dirs-fonts
Summary:	TeX font directories
Summary(pl.UTF-8):	Katalogi fontów TeXa
Group:		Fonts
Provides:	tetex-dirs-fonts
Obsoletes:	tetex-dirs-fonts

%description dirs-fonts
TeX font directories.

%description dirs-fonts -l pl.UTF-8
Katalogi fontów TeXa.

%package font-utils
Summary:	Font utilities
Group:		Fonts

%description font-utils
Font utilities.

# # Fonts packages #

%package fonts-other
Summary:	Other fonts
Summary(hu.UTF-8):	További betűtípusok
Group:		Fonts
Requires:	%{name}-dirs-fonts >= %{texmfversion}
Obsoletes:	tetex-fonts-cbgreek
Obsoletes:	tetex-fonts-dstroke
Obsoletes:	tetex-fonts-pazo
Obsoletes:	tetex-fonts-type1-dstroke
Obsoletes:	tetex-fonts-type1-qfonts
Obsoletes:	tetex-fonts-type1-tt2001
Obsoletes:	tetex-qfonts

%description fonts-other
Other fonts.

%description fonts-other -l hu.UTF-8
További betűtípusok.

%package bbox
Summary:	bbox prints the bounding box of images
Group:		Applications/Publishing/TeX

%description bbox
bbox reads a rawppm or rawpbm file and prints out the bounding box of
the image.

%package detex
Summary:	A filter to strip TeX commands from a .tex file
Summary(hu.UTF-8):	Egy szűrő, amely .tex fájlokból szűri ki a TeX parancsokat
Group:		Applications/Publishing/TeX

%description detex
A filter to strip TeX commands from a .tex file.

%description detex -l hu.UTF-8
Egy szűrő, amely .tex fájlokból szűri ki a TeX parancsokat.

%package dviutils
Summary:	Various DVI utils
Summary(hu.UTF-8):	Vegyes DVI eszközök
Group:		Applications/Publishing/TeX
Provides:	dvi2tty
Obsoletes:	dvi2tty

%description dviutils
This package contains various DVI utils.

%description dviutils -l hu.UTF-8
Ez a csomag mindenféle DVI eszközt tartalmaz.

%package uncategorized-utils
Summary:	Uncategorized utils
Group:		Applications/Publishing/TeX

%description uncategorized-utils
Uncategorized utilities. Needs check and categorizing.

%package tex4ht
Summary:	LaTeX and TeX for hypertext
Group:		Applications/Publishing/TeX

%description tex4ht
A converter from TeX and LaTeX to hypertext (HTML, XML, etc.),
providing a configurable (La)TeX-based authoring system for hypertext.
When converting to XML, you can use MathML instead of images for
equation representation.

%package xetex
Summary:	Extended TeX / LaTeX version for unicode
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-misc >= %{texmfversion}

%description xetex
XeTeX extends the TeX typesetting system (and macro packages such as
LaTeX and ConTeXt) to have native support for the Unicode character
set, including complex Asian scripts, and for OpenType and TrueType
fonts.

%package xmltex
Summary:	TeX package for processing XML files
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Provides:	passivetex = 1.26
Provides:	xmltex
Obsoletes:	passivetex
Obsoletes:	xmltex

%description xmltex
XMLTeX is a non-validating, namespace-aware XML parser written in TeX.
It allows TeX to directly process XML files.

%package luatex
Summary:	LuaTeX uses Lua scripting both as an extension to the TeX macro language and as an extension to the typesetting engine itself
Group:		Applications/Publishing/TeX

%description luatex
LuaTeX uses Lua scripting both as an extension to the TeX macro
language and as an extension to the typesetting engine itself.

%prep
%setup -q -n %{name}-%{version}-source
# %patch0 -p1
# %patch1 -p1
# %patch2 -p1
# %patch3 -p1
# %patch4 -p1
# %patch5 -p1
# %patch6 -p1
# %patch7 -p1

%build
# find . -name "config.sub" -exec cp /usr/share/automake/config.sub '{}' ';'
%{__sed} -i 's@"extend/\(.*\)"@<\1>@' texk/ttf2pk/*.c
cd texk/kpathsea
%{__sed} -i 's@^TEXMFMAIN =.*@TEXMFMAIN = %{texmf}@' texmf.cnf
%{__sed} -i 's@^TEXMFDIST =.*@TEXMFDIST = %{texmfdist}@' texmf.cnf
%{__sed} -i 's@^TEXMFLOCAL =.*@TEXMFLOCAL = %{texmf}@' texmf.cnf
%{__sed} -i 's@^TEXMFSYSVAR =.*@TEXMFSYSVAR = %{_localstatedir}@' texmf.cnf
%{__sed} -i 's@^TEXMFSYSCONFIG =.*@TEXMFSYSCONFIG = %{_sysconfdir}/%{name}@' texmf.cnf
%{__sed} -i 's@^TEXMFVAR =.*@TEXMFVAR = %{_localstatedir}@' texmf.cnf
%{__sed} -i 's@^trie_size.*@trie_size = 1262000@' texmf.cnf
cd ../..

%ifarch ppc ppc64
# clisp does not work properly on forge
ulimit -s unlimited
%endif

export CPPFLAGS="%{rpmcppflags} -DHAVE_PROTOTYPES"
%configure \
	--prefix=%{_prefix} \
	--with%{!?with_xindy:out}-xindy \
	--enable-shared \
	--disable-native-texlive-build \
	--without-luatex \
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
	--with-freetype-includes=/usr/include/freetype \
	--with-system-freetype2 \
	--with-system-gd \
	--with-system-ncurses \
	--with-system-pnglib \
	--with-system-t1lib \
	--with-system-zlib \
	--with-xdvi-x-toolkit=xaw \
	--without-dialog \
	--without-t1utils \
	--without-texinfo \
 	--enable-build-in-source-tree
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_mandir}/man5 \
	$RPM_BUILD_ROOT/var/cache/fonts \
	$RPM_BUILD_ROOT/etc/cron.daily\
	$RPM_BUILD_ROOT/etc/sysconfig/tetex-updmap\
	$RPM_BUILD_ROOT%{_localstatedir}/fonts/map\
	$RPM_BUILD_ROOT%{fmtdir}/pdftex
# 	$RPM_BUILD_ROOT%{texmfdist}/source/generic \
# 	$RPM_BUILD_ROOT%{texmfdist}/tex/generic \
# 	$RPM_BUILD_ROOT%{texmfdist}/tex/plain \
# 	$RPM_BUILD_ROOT%{texmf}/tex

#    %{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf/texmf $RPM_BUILD_ROOT%{texmf}
#    %{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf/texmf-dist $RPM_BUILD_ROOT%{texmfdist}
#    %{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf/texmf-doc $RPM_BUILD_ROOT%{texmfdoc}
#    %{__mv} $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pgfplots/* $RPM_BUILD_ROOT%{texmfdist}/doc/latex/pgfplots
#    rmdir $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pgfplots
#    # imho it is unneeded
#    %{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/doc/fonts/{ec,fc,utopia}
#    %{__rm} -r $RPM_BUILD_ROOT%{texmf}/doc/cefconv
#
#    # This is an empty directory
#    %{__rm} -r $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf
#    # Useless binary
#    %{__rm} $RPM_BUILD_ROOT%{_datadir}/texmf-dist/doc/latex/splitindex/splitindex{.exe,-Linux-i386,-OpenBSD-i386}
#
# commented out because of following (non-fatal) error:
# Can't open texmf/web2c/texmf.cnf: No such file or directory.
#perl -pi \
#	-e "s|\.\./\.\./texmf|$RPM_BUILD_ROOT%{texmf}|g;" \
#	-e "s|/var/cache/fonts|$RPM_BUILD_ROOT/var/cache/fonts|g;" \
#	texmf/web2c/texmf.cnf

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}; export LD_LIBRARY_PATH
PATH=$RPM_BUILD_ROOT%{_bindir}:$PATH; export PATH


%{__make} install \
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

# requires wdiff but we don't have
%{__rm} -rf $RPM_BUILD_ROOT%{texmfdist}/scripts/texdiff
%{__rm} -rf $RPM_BUILD_ROOT%{_bindir}/texdiff
%{__rm} -rf $RPM_BUILD_ROOT%{_bindir}/man

install -d \
	$RPM_BUILD_ROOT%{texmfdist}/doc/generic \
	$RPM_BUILD_ROOT%{texmfdist}/doc \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/afm/public \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/afm/vntex \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/afm \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/enc/dvips/vntex \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/ofm/public \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/ofm \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/opentype/public \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/opentype \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/ovf/public \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/ovf \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/ovp/public \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/ovp \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/pk/ljfour \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/pk \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/source/public \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/source/vntex \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/source \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/tfm/public \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/tfm/vntex \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/truetype \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/type1/public \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/type1/vntex \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/vf/public \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/vf/vntex \
	$RPM_BUILD_ROOT%{texmfdist}/fonts/vf \
	$RPM_BUILD_ROOT%{texmfdist}/source/fonts \
	$RPM_BUILD_ROOT%{texmfdist}/source/generic \
	$RPM_BUILD_ROOT%{texmfdist}/source \
	$RPM_BUILD_ROOT%{texmfdist}/tex/generic \
	$RPM_BUILD_ROOT%{texmfdist}/tex/plain \
	$RPM_BUILD_ROOT%{texmfdist}/tex \
	$RPM_BUILD_ROOT%{texmf}/fonts/opentype/public \
	$RPM_BUILD_ROOT%{texmf}/fonts/opentype \
	$RPM_BUILD_ROOT%{texmf}/tex

CURDIR=$(pwd)
cd $RPM_BUILD_ROOT%{_bindir}

ln -sf pdftex latex
ln -sf xetex xelatex
ln -sf pdftex pdflatex


ln -sf ../share/texmf-dist/scripts/fontools/afm2afm afm2afm
ln -sf ../share/texmf-dist/scripts/fontools/autoinst autoinst
ln -sf ../share/texmf-dist/scripts/cachepic/cachepic.tlu cachepic
ln -sf ../share/texmf-dist/scripts/fontools/cmap2enc cmap2enc
ln -sf ../share/texmf-dist/scripts/epstopdf/epstopdf.pl epstopdf
# ln -sf ../share/texmf-dist/scripts/context/stubs/unix/exatools exatools
ln -sf ../share/texmf-dist/scripts/fig4latex/fig4latex fig4latex
ln -sf ../share/texmf-dist/scripts/findhyph/findhyph findhyph
ln -sf ../share/texmf-dist/scripts/fontools/font2afm font2afm
ln -sf ../share/texmf-dist/scripts/fragmaster/fragmaster.pl fragmaster
# ln -sf ../share/texmf-dist/scripts/texlive/getnonfreefonts.pl getnonfreefonts
# ln -sf ../share/texmf-dist/scripts/texlive/getnonfreefonts.pl getnonfreefonts-sys
ln -sf ../share/texmf-dist/scripts/latex2man/latex2man latex2man
ln -sf ../share/texmf-dist/scripts/latexmk/latexmk.pl latexmk
ln -sf ../share/texmf-dist/scripts/listings-ext/listings-ext.sh listings-ext.sh
ln -sf ../share/texmf-dist/scripts/mkgrkindex/mkgrkindex mkgrkindex
ln -sf ../share/texmf-dist/scripts/accfonts/mkt1font mkt1font
# ln -sf ../share/texmf-dist/scripts/context/stubs/unix/mtxrun mtxrun
ln -sf ../share/texmf-dist/scripts/fontools/ot2kpx ot2kpx
ln -sf ../share/texmf-dist/scripts/pax/pdfannotextractor.pl pdfannotextractor
ln -sf ../share/texmf-dist/scripts/ppower4/pdfthumb.texlua pdfthumb
# ln -sf ../share/texmf-dist/scripts/context/stubs/unix/pdftrimwhite pdftrimwhite
ln -sf ../share/texmf-dist/scripts/perltex/perltex.pl perltex
ln -sf ../share/texmf-dist/scripts/fontools/pfm2kpx pfm2kpx
ln -sf ../share/texmf-dist/scripts/pkfix/pkfix.pl pkfix
ln -sf ../share/texmf-dist/scripts/pkfix-helper/pkfix-helper pkfix-helper
ln -sf ../share/texmf-dist/scripts/ppower4/ppower4.texlua ppower4
ln -sf ../share/texmf-dist/scripts/ps2eps/ps2eps.pl ps2eps
ln -sf ../share/texmf-dist/scripts/purifyeps/purifyeps purifyeps
ln -sf ../share/texmf-dist/scripts/fontools/showglyphs showglyphs
ln -sf ../share/texmf-dist/scripts/splitindex/perl/splitindex.pl splitindex
ln -sf ../share/texmf-dist/scripts/svn-multi/svn-multi.pl svn-multi
ln -sf ../share/texmf-dist/scripts/texcount/TeXcount.pl texcount
ln -sf ../share/texmf-dist/scripts/texdirflatten/texdirflatten texdirflatten
# ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texfind texfind
ln -sf ../share/texmf-dist/scripts/texloganalyser/texloganalyser texloganalyser
# ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texshow texshow
ln -sf ../share/texmf-dist/scripts/ulqda/ulqda.pl ulqda
ln -sf ../share/texmf-dist/scripts/accfonts/vpl2ovp vpl2ovp
ln -sf ../share/texmf-dist/scripts/accfonts/vpl2vpl vpl2vpl

ln -sf ../share/texmf/scripts/a2ping/a2ping.pl a2ping
# ln -sf ../share/texmf-dist/scripts/context/stubs/unix/context context
# ln -sf ../share/texmf-dist/scripts/context/stubs/unix/ctxtools ctxtools
ln -sf ../share/texmf-dist/scripts/dviasm/dviasm.py dviasm
ln -sf ../share/texmf/scripts/tetex/e2pall.pl e2pall
ln -sf ../share/texmf-dist/scripts/bengali/ebong.py ebong
ln -sf ../share/texmf-dist/scripts/epspdf/epspdf epspdf
ln -sf ../share/texmf-dist/scripts/epspdf/epspdftk epspdftk
ln -sf ../share/texmf-dist/scripts/epstopdf/epstopdf.pl epstopdf
# ln -sf ../share/texmf-dist/scripts/context/stubs/unix/exatools exatools
# ln -sf ../share/texmf/scripts/getnonfreefonts/getnonfreefonts.pl getnonfreefonts
# ln -sf ../share/texmf/scripts/getnonfreefonts/getnonfreefonts.pl getnonfreefonts-sys
ln -sf ../share/texmf-dist/scripts/tex4ht/ht.sh ht
ln -sf ../share/texmf-dist/scripts/tex4ht/htcontext.sh htcontext
ln -sf ../share/texmf-dist/scripts/tex4ht/htlatex.sh htlatex
ln -sf ../share/texmf-dist/scripts/tex4ht/htmex.sh htmex
ln -sf ../share/texmf-dist/scripts/tex4ht/httex.sh httex
ln -sf ../share/texmf-dist/scripts/tex4ht/httexi.sh httexi
ln -sf ../share/texmf-dist/scripts/tex4ht/htxelatex.sh htxelatex
ln -sf ../share/texmf-dist/scripts/tex4ht/htxetex.sh htxetex
# ln -sf ../share/texmf-dist/scripts/context/lua/luatools.lua luatools
ln -sf ../share/texmf-dist/scripts/glossaries/makeglossaries makeglossaries
# ln -sf ../share/texmf-dist/scripts/context/stubs/unix/makempy makempy
ln -sf ../share/texmf-dist/scripts/tex4ht/mk4ht.pl mk4ht
ln -sf ../share/texmf-dist/scripts/mkjobtexmf/mkjobtexmf.pl mkjobtexmf
# ln -sf ../share/texmf-dist/scripts/context/stubs/unix/mpstools mpstools
# ln -sf ../share/texmf-dist/scripts/context/stubs/unix/mptopdf mptopdf
# ln -sf ../share/texmf-dist/scripts/context/lua/mtxrun.lua mtxrun
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/mtxtools mtxtools
ln -sf ../share/texmf-dist/scripts/oberdiek/pdfatfi.pl pdfatfi
ln -sf ../share/texmf-dist/scripts/pdfcrop/pdfcrop.pl pdfcrop
ln -sf ../share/texmf-dist/scripts/ppower4/pdfthumb.tlu pdfthumb
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/pdftools pdftools
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/pdftrimwhite pdftrimwhite
ln -sf ../share/texmf-dist/scripts/perltex/perltex perltex
ln -sf ../share/texmf-dist/scripts/pkfix/pkfix.pl pkfix
ln -sf ../share/texmf-dist/scripts/ppower4/ppower4.tlu ppower4
ln -sf ../share/texmf/scripts/ps2eps/ps2eps.pl ps2eps
ln -sf ../share/texmf-dist/scripts/pst-pdf/ps4pdf ps4pdf
ln -sf ../share/texmf-dist/scripts/pst2pdf/pst2pdf.pl pst2pdf
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/pstopdf pstopdf
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/rlxtools rlxtools
ln -sf ../share/texmf/scripts/texlive/rungs.tlu rungs
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/runtools runtools
ln -sf ../share/texmf/scripts/simpdftex/simpdftex simpdftex
ln -sf ../share/texmf-dist/scripts/texcount/texcount.pl texcount
ln -sf ../share/texmf/scripts/texdoc/texdoc.tlu texdoc
ln -sf ../share/texmf/scripts/tetex/texdoctk.pl texdoctk
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texexec texexec
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texfind texfind
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texfont texfont
# ln -sf ../share/texmf-dist/scripts/context/ruby/texmfstart.rb texmfstart
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texshow texshow
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/textools textools
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texutil texutil
ln -sf ../share/texmf-dist/scripts/thumbpdf/thumbpdf.pl thumbpdf
ln -sf ../share/texmf/scripts/texlive/tlmgr.pl tlmgr
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/tmftools tmftools
ln -sf ../share/texmf-dist/scripts/vpe/vpe.pl vpe
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/xmltools xmltools

cd $CURDIR

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

# We don't need it
# %{__rm} -r $RPM_BUILD_ROOT%{texmf}/doc/man
# %{__rm} -r $RPM_BUILD_ROOT%{texmfdoc}/source

perl -pi \
	-e "s|$RPM_BUILD_ROOT||g;" \
	$RPM_BUILD_ROOT%{texmf}/web2c/texmf.cnf

install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.daily/texlive

install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE6} $RPM_BUILD_ROOT%{_pixmapsdir}

# not included in package
rm -f $RPM_BUILD_ROOT%{_datadir}/texinfo/html/texi2html.html
rm -f $RPM_BUILD_ROOT%{_infodir}/dir*
rm -f $RPM_BUILD_ROOT%{_infodir}/dvipng*
rm -f $RPM_BUILD_ROOT%{_mandir}/{README.*,hu/man1/readlink.1*}
rm -f $RPM_BUILD_ROOT%{texmf}/doc/Makefile
rm -f $RPM_BUILD_ROOT%{texmf}/doc/fonts/oldgerman/COPYING
rm -f $RPM_BUILD_ROOT%{texmf}/doc/help/Catalogue-upd.sh
rm -f $RPM_BUILD_ROOT%{texmf}/doc/help/faq/uktug-faq-upd.sh
rm -f $RPM_BUILD_ROOT%{texmf}/doc/helpfile
rm -f $RPM_BUILD_ROOT%{texmf}/doc/helpindex.html
rm -f $RPM_BUILD_ROOT%{texmf}/doc/index.html
rm -f $RPM_BUILD_ROOT%{texmf}/doc/index.php
rm -f $RPM_BUILD_ROOT%{texmf}/doc/mkhtml*
rm -f $RPM_BUILD_ROOT%{texmf}/doc/programs/texinfo.*
rm -rf $RPM_BUILD_ROOT%{texmf}/doc/tetex
rm -f $RPM_BUILD_ROOT%{texmf}/fonts/pk/ljfour/lh/lh-lcy/*.600pk
rm -f $RPM_BUILD_ROOT%{texmf}/generic/config/pdftex-dvi.tex
rm -f $RPM_BUILD_ROOT%{texmf}/release-tetex-{src,texmf}.txt
rm -f $RPM_BUILD_ROOT%{texmf}/scripts/uniqleaf/uniqleaf.pl
rm -f $RPM_BUILD_ROOT%{texmf}/tex/generic/pdftex/glyphtounicode.tex
rm -rf $RPM_BUILD_ROOT%{_datadir}/lcdf-typetools
rm -rf $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pdf-trans
rm -rf $RPM_BUILD_ROOT%{texmfdist}/source/generic/hyph-utf8
rm -rf $RPM_BUILD_ROOT%{texmfdist}/source/generic/patch
rm -rf $RPM_BUILD_ROOT%{texmfdist}/source/plain/plgraph
rm -rf $RPM_BUILD_ROOT%{texmfdist}/tex/generic/pdf-trans
rm -rf $RPM_BUILD_ROOT%{texmfdist}/tex/generic/xecyr

# move format logs to BUILD, so $RPM_BUILD_ROOT is not polluted
# and we can still analyze them
# install -d format-logs
# mv -fv $RPM_BUILD_ROOT%{fmtdir}/*.log format-logs

# xindy files are in %%{texmf}
rm -rf $RPM_BUILD_ROOT%{_datadir}/xindy
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

# Create format files
for format in \
	aleph \
	csplain \
	etex \
	lambda \
	lamed \
	latex \
	mex \
	mllatex \
	mptopdf \
	omega \
	pdfcsplain \
	pdfetex \
	pdflatex \
	pdftex \
	physe \
	phyzzx \
	tex \
	texsis \
	xetex \
	xelatex; do
# pdfxmltex \
# xmltex; do

%if %{with bootstrap}
	install -d $RPM_BUILD_ROOT%{fmtdir}/${format}
	touch $RPM_BUILD_ROOT%{fmtdir}/${format}/${format}.fmt
	touch $RPM_BUILD_ROOT%{fmtdir}/pdftex/${format}.fmt
%else
#######
#	fmtutil --fmtdir $RPM_BUILD_ROOT%{fmtdir} --byfmt=${format}
#######
%endif
done

%if %{with bootstrap}
touch $RPM_BUILD_ROOT%{fmtdir}/xetex/xelatex.fmt
%endif
# We don't need the log files
rm -f $(find $RPM_BUILD_ROOT%{fmtdir} -name "*.log")

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

%post -n kpathsea
/sbin/ldconfig
%texhash

%postun -n kpathsea
/sbin/ldconfig
%texhash

%post -n kpathsea-devel
%fixinfodir
%texhash

%postun -n kpathsea-devel
%fixinfodir
%texhash

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

%post metapost
%texhash

%postun metapost
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

%post latex-bibtex
%texhash

%postun latex-bibtex
%texhash

%post latex-presentation-bin
%texhash

%postun latex-presentation-bin
%texhash

%post format-pdflatex
%texhash

%postun format-pdflatex
%texhash

%post tex-babel
%texhash

%postun tex-babel
%texhash

%post tex-thumbpdf
%texhash

%postun tex-thumbpdf
%texhash

%post fonts-other
%texhash

%postun fonts-other
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

%files
%defattr(644,root,root,755)

# ***********
# executables
# ***********
%attr(755,root,root) %{_bindir}/afm2tfm
%attr(755,root,root) %{_bindir}/allcm
%attr(755,root,root) %{_bindir}/allec
%attr(755,root,root) %{_bindir}/allneeded
%attr(755,root,root) %{_bindir}/arlatex
%attr(755,root,root) %{_bindir}/bundledoc
%attr(755,root,root) %{_bindir}/cweave
%attr(755,root,root) %{_bindir}/ctangle
%attr(755,root,root) %{_bindir}/ctie
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
%attr(755,root,root) %{_bindir}/mf
%attr(755,root,root) %{_bindir}/mf-nowin
%attr(755,root,root) %{_bindir}/mft
%attr(755,root,root) %{_bindir}/mktexmf
%attr(755,root,root) %{_bindir}/mktexpk
%attr(755,root,root) %{_bindir}/mktextfm
%attr(755,root,root) %{_bindir}/mktexfmt
%attr(755,root,root) %{_bindir}/mktexlsr
%attr(755,root,root) %{_bindir}/patgen
%attr(755,root,root) %{_bindir}/pfb2pfa
%attr(755,root,root) %{_bindir}/pk2bm
%attr(755,root,root) %{_bindir}/pktogf
%attr(755,root,root) %{_bindir}/pktype
%attr(755,root,root) %{_bindir}/pltotf
%attr(755,root,root) %{_bindir}/pooltype
%attr(755,root,root) %{_bindir}/ps2frag
%attr(755,root,root) %{_bindir}/ps2pk
# TODO: move this file to correct subpackage ?
%attr(755,root,root) %{_bindir}/ps4pdf
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

%config(noreplace,missingok) %verify(not md5 mtime size) %attr(750,root,root) /etc/cron.daily/texlive

%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/fmtutil.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktex.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktexdir.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktexnam.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/texmf.cnf

%attr(1777,root,root) /var/cache/fonts

%{_datadir}/info/web2c.info*

# ***********
# Directories
# ***********
%attr(1777,root,root) %dir %{_localstatedir}
%attr(1777,root,root) %dir %{_localstatedir}/fonts
%attr(1777,root,root) %dir %{_localstatedir}/fonts/map

%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/allcm.1*
%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*
%{_mandir}/man1/ctangle.1*
%{_mandir}/man1/ctie.1*
%{_mandir}/man1/cweave.1*
%{_mandir}/man1/cweb.1*
%{_mandir}/man1/dvipng.1*
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
# %{_mandir}/man1/makempy.1*
%{_mandir}/man1/mf.1*
%{_mandir}/man1/mf-nowin.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*
%{_mandir}/man1/mktexfmt.1*
%{_mandir}/man1/mktexlsr.1*
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
%{fmtdir}/pdftex/pdfetex.fmt
# %{fmtdir}/pdfetex
%dir %{fmtdir}/tex
%{fmtdir}/tex/tex.fmt
# %{fmtdir}/pdftex/tex.fmt

# %files jadetex
# %defattr(644,root,root,755)
# %dir %{texmfdist}/doc/jadetex
# %doc %{texmfdist}/doc/jadetex/base
# %doc %{texmfdist}/source/jadetex/base/ChangeLog*
# %attr(755,root,root) %{_bindir}/jadetex
# %attr(755,root,root) %{_bindir}/pdfjadetex
# %{texmfdist}/source/jadetex
# %exclude %{texmfdist}/source/jadetex/base/ChangeLog*
# %{texmfdist}/tex/jadetex
# %{texmf}/fmtutil/format.jadetex.cnf

%files cef-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cef*

%files other-utils
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/mkjobtexmf
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
%attr(755,root,root) %{_bindir}/hbf2gf
%attr(755,root,root) %{_bindir}/makeglossaries
%attr(755,root,root) %{_bindir}/mkjobtexmf
%attr(755,root,root) %{texmfdist}/scripts/mkjobtexmf/mkjobtexmf.pl
%attr(755,root,root) %{_bindir}/mmafm
%attr(755,root,root) %{_bindir}/mmpfb
%attr(755,root,root) %{_bindir}/musixflx
%attr(755,root,root) %{_bindir}/ofm2opl
%attr(755,root,root) %{_bindir}/otfinfo
%attr(755,root,root) %{_bindir}/otftotfm
%dir %{texmfdist}/scripts/oberdiek
%attr(755,root,root) %{texmfdist}/scripts/oberdiek/pdfatfi.pl
%attr(755,root,root) %{_bindir}/pdfatfi
%dir %{texmfdist}/scripts/pax
%attr(755,root,root) %{texmfdist}/scripts/pax/pdfannotextractor.pl
%attr(755,root,root) %{_bindir}/pdfannotextractor
%attr(755,root,root) %{_bindir}/pdfclose
%attr(755,root,root) %{_bindir}/pdfopen
%attr(755,root,root) %{_bindir}/pdftosrc
%{__perl}tex
%dir %{texmfdist}/scripts/pkfix
%attr(755,root,root) %{texmfdist}/scripts/pkfix/pkfix.pl
%attr(755,root,root) %{_bindir}/pkfix
%dir %{texmfdist}/scripts/pkfix-helper
%attr(755,root,root) %{texmfdist}/scripts/pkfix-helper/pkfix-helper
%attr(755,root,root) %{_bindir}/pkfix-helper
%attr(755,root,root) %{_bindir}/teckit_compile
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
%attr(755,root,root) %{_bindir}/ttf2pk
%attr(755,root,root) %{_bindir}/ttf2tfm
%attr(755,root,root) %{_bindir}/ttftotype42
%dir %{texmfdist}/scripts/ulqda
%attr(755,root,root) %{texmfdist}/scripts/ulqda/ulqda.pl
%attr(755,root,root) %{_bindir}/ulqda
%attr(755,root,root) %{_bindir}/vlna
%attr(755,root,root) %{_bindir}/vpe
%{_mandir}/man1/cfftot1.1*
%{_mandir}/man1/hbf2gf.1*
# %{_mandir}/man1/mkjobtexmf.1*
%{_mandir}/man1/mmafm.1*
%{_mandir}/man1/mmpfb.1*
%{_mandir}/man1/otfinfo.1*
%{_mandir}/man1/otftotfm.1*
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
%{fmtdir}/pdftex/texsis.fmt
# %{fmtdir}/texsis



%files font-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afm*
%attr(755,root,root) %{_bindir}/autoinst
%attr(755,root,root) %{_bindir}/cmap2enc
%attr(755,root,root) %{_bindir}/font2afm
# %attr(755,root,root) %{_bindir}/getnonfreefonts*
%attr(755,root,root) %{_bindir}/mkt1font
%attr(755,root,root) %{_bindir}/ot2kpx
%attr(755,root,root) %{_bindir}/pfm2kpx
%attr(755,root,root) %{_bindir}/showglyphs
%attr(755,root,root) %{_bindir}/t1*
%attr(755,root,root) %{_bindir}/ttfdump
%attr(755,root,root) %{_bindir}/vpl*
%dir %{texmfdist}/scripts/accfonts
%attr(755,root,root) %{texmfdist}/scripts/accfonts/*
%dir %{texmfdist}/scripts/fontools
%attr(755,root,root) %{texmfdist}/scripts/fontools/*
# %dir %{texmf}/scripts/getnonfreefonts
# %attr(755,root,root) %{texmf}/scripts/getnonfreefonts/*
%{_mandir}/man1/afm2pl.1*
# %{_mandir}/man1/getnonfreefonts-sys.1
# %{_mandir}/man1/getnonfreefonts.1*
%{_mandir}/man1/t1*.1*
%{_mandir}/man1/ttfdump.1*

%files -n kpathsea
%defattr(644,root,root,755)
# %doc %{texmf}/doc/kpathsea
%attr(755,root,root) %{_bindir}/kpsepath
%attr(755,root,root) %{_bindir}/kpsestat
%attr(755,root,root) %{_bindir}/kpsetool
%attr(755,root,root) %{_bindir}/kpsewhich
%attr(755,root,root) %{_bindir}/kpsexpand
%attr(755,root,root) %{_libdir}/libkpathsea.so.*
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
# %dir %{texmfdist}/fonts/map/dvips/cmex
# %dir %{texmf}/dvipdfm
# %dir %{texmf}/fonts/map/dvipdfm
# %dir %{texmf}/fonts/map/dvips
# %dir %{texmf}/fonts/map/dvips/tetex
# %doc %{texmf}/doc/dvips
# %doc %{texmf}/doc/dvipdfm
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
# %{_mandir}/man1/dvipdfm.1*
%{_mandir}/man1/dvips.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/dvitype.1*
%{texmf}/dvips/base
# %{texmf}/dvips/config
# %{texmf}/dvips/getafm
%{texmf}/dvips/gsftopk
%{texmfdist}/fonts/enc/dvips/base
# %{texmfdist}/fonts/map/dvips/allrunes
# %{texmfdist}/fonts/map/dvips/cmex/ttcmex.map
# %{texmfdist}/tex/generic/dvips
# %{texmfdist}/dvips
# %{texmf}/dvipdfm/config
# %{texmf}/dvips/tetex/config.*
# %{texmf}/fonts/enc/dvips/tetex/mtex.enc
# %{texmf}/fonts/enc/dvips/afm2pl
# %{texmf}/fonts/map/dvipdfm/updmap
# %{texmf}/fonts/map/dvipdfm/dvipdfmx

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
%attr(755,root,root) %{_bindir}/makeindex
%attr(755,root,root) %{_bindir}/mkindex
%attr(755,root,root) %{_bindir}/mkgrkindex
%attr(755,root,root) %{_bindir}/rumakeindex
%attr(755,root,root) %{_bindir}/splitindex
%dir %{texmfdist}/scripts/splitindex
%dir %{texmfdist}/scripts/splitindex/perl
%attr(755,root,root) %{texmfdist}/scripts/splitindex/perl/splitindex.pl
%dir %{texmfdist}/scripts/mkgrkindex
%attr(755,root,root) %{texmfdist}/scripts/mkgrkindex/mkgrkindex
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/mkindex.1*
%{_mandir}/man1/rumakeindex.1*

%files tlmgr
%defattr(644,root,root,755)
%dir %{texmf}/scripts/texlive
%attr(755,root,root) %{texmf}/scripts/texlive/*.pl
%attr(755,root,root) %{_bindir}/tlmgr
# %dir %{texmf}/scripts/texlive/gswin32
# %dir %{texmf}/scripts/texlive/lua
# %dir %{texmf}/scripts/texlive/lua/texlive
# %dir %{texmf}/scripts/texlive/tlmgrgui
# %attr(755,root,root) %{texmf}/scripts/texlive/*.pl
# %attr(755,root,root) %{texmf}/scripts/texlive/gswin32/*
# %attr(755,root,root) %{texmf}/scripts/texlive/lua/texlive/*
# %attr(755,root,root) %{texmf}/scripts/texlive/tlmgrgui/*.pl
# %{texmf}/scripts/texlive/tlmgrgui/lang

%files scripts
%defattr(644,root,root,755)
# %dir %{texmfdist}/scripts/bengali
%dir %{texmfdist}/scripts/glossaries
%dir %{texmfdist}/scripts/perltex
# %dir %{texmfdist}/scripts/pgfplots
%dir %{texmfdist}/scripts/pst2pdf
# %dir %{texmfdist}/scripts/shipunov
%dir %{texmfdist}/scripts/texcount
%dir %{texmfdist}/scripts/vpe
%dir %{texmf}/scripts/a2ping
# %dir %{texmf}/scripts/pkfix
%dir %{texmf}/scripts/simpdftex
%dir %{texmf}/scripts/tetex
# %attr(755,root,root) %{texmfdist}/scripts/bengali/*
%attr(755,root,root) %{texmfdist}/scripts/glossaries/*
%attr(755,root,root) %{texmfdist}/scripts/perltex/perltex*
# %attr(755,root,root) %{texmfdist}/scripts/pgfplots/*
%attr(755,root,root) %{texmfdist}/scripts/pst2pdf/pst2pdf*
# %attr(755,root,root) %{texmfdist}/scripts/shipunov/*
%attr(755,root,root) %{texmfdist}/scripts/texcount/*
%attr(755,root,root) %{texmfdist}/scripts/vpe/vpe.pl
%attr(755,root,root) %{texmf}/scripts/a2ping/a2ping*
# %attr(755,root,root) %{texmf}/scripts/pkfix/pkfix*
%attr(755,root,root) %{texmf}/scripts/simpdftex/simpdftex*
%attr(755,root,root) %{texmf}/scripts/tetex/*
%attr(755,root,root) %{_bindir}/a2ping
%attr(755,root,root) %{_bindir}/e2pall
%dir %{texmfdist}/scripts/findhyph
%attr(755,root,root) %{texmfdist}/scripts/findhyph/findhyph
%attr(755,root,root) %{_bindir}/findhyph
%dir %{texmfdist}/scripts/listings-ext
%attr(755,root,root) %{texmfdist}/scripts/listings-ext/listings-ext.sh
%attr(755,root,root) %{_bindir}/listings-ext.sh
%dir %{texmfdist}/scripts/texdirflatten
%attr(755,root,root) %{texmfdist}/scripts/texdirflatten/texdirflatten
%attr(755,root,root) %{_bindir}/texdirflatten
%{_mandir}/man1/e2pall.1*
# %dir %{texmf}/texdoc
# %doc %{texmf}/doc/texdoc
# %config(noreplace) %verify(not md5 mtime size) %{texmf}/texdoc/texdoc.cnf

%files metapost
%defattr(644,root,root,755)
# %dir %{texmfdist}/metapost
# %doc %{texmfdist}/doc/metapost
%attr(755,root,root) %{_bindir}/mpost
# %attr(755,root,root) %{_bindir}/mpto
# %{texmfdist}/metapost/base
# %{texmfdist}/metapost/config
# %{texmfdist}/metapost/mfpic
# %{texmfdist}/metapost/misc
# %{texmfdist}/metapost/support
# %{texmfdist}/source/metapost
%{_mandir}/man1/mpost.1*
# %{_mandir}/man1/mpto.1*
# %{texmf}/fmtutil/format.metapost.cnf

%files mptopdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mptopdf
%{_mandir}/man1/mptopdf.1*
# %{texmfdist}/tex/mptopdf
%{fmtdir}/pdftex/mptopdf.fmt
# %{fmtdir}/mptopdf

%files texdoctk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/texdoctk
# %{texmf}/texdoctk
%{_mandir}/man1/texdoctk.1*

%files -n texconfig
%defattr(644,root,root,755)
%dir %{texmf}/texconfig
%attr(755,root,root) %{_bindir}/texconfig
%attr(755,root,root) %{_bindir}/texconfig-dialog
%attr(755,root,root) %{_bindir}/texconfig-sys
%attr(755,root,root) %{texmf}/texconfig/tcfmgr
%{_mandir}/man1/texconfig.1*
%{_mandir}/man1/texconfig-sys.1*
%{texmf}/texconfig/tcfmgr.map

%if %{with xindy}
%files -n xindy
%defattr(644,root,root,755)
%doc %{texmf}/doc/xindy
%dir %{texmf}/xindy
%dir %{texmf}/xindy/lang
%dir %{texmf}/scripts/xindy
%attr(755,root,root) %{texmf}/scripts/xindy/*
%attr(755,root,root) %{_bindir}/tex2xindy
%attr(755,root,root) %{_bindir}/xindy
%attr(755,root,root) %{_bindir}/texindy
%{_libdir}/xindy
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
%{texmf}/xindy/lang/vietnamese/
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
# %config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/pdftexconfig.tex
# %dir %{texmfdist}/doc/support
# %dir %{texmf}/fonts/map/pdftex
# %doc %{texmfdist}/doc/pdftex
# %doc %{texmfdist}/doc/support/pdfcrop
%dir %{texmfdist}/scripts/pdfcrop
%attr(755,root,root) %{texmfdist}/scripts/pdfcrop/pdfcrop.pl
%attr(755,root,root) %{_bindir}/pdfcrop
%attr(755,root,root) %{_bindir}/rpdfcrop
%attr(755,root,root) %{_bindir}/pdftex
%attr(755,root,root) %{_bindir}/tpic2pdftex
%dir %{fmtdir}/pdftex
# %{_mandir}/man1/epstopdf.1*
%{_mandir}/man1/pdftex.1*
%{_mandir}/man1/tpic2pdftex.1*
# %{texmfdist}/fonts/enc/pdftex
# %{texmfdist}/fonts/map/pdftex
# %{texmf}/fmtutil/format.pdftex.cnf
# %{texmf}/fonts/map/pdftex/updmap
%{fmtdir}/pdftex/pdftex.fmt

%files phyzzx
%defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/phyzzx
# %dir %{texmfdist}/doc/phyzzx
# %dir %{texmfdist}/tex/phyzzx
# %doc %{texmfdist}/doc/phyzzx/base
# %{texmfdist}/tex/phyzzx/base
# %{texmfdist}/tex/phyzzx/config
# %{texmf}/fmtutil/format.phyzzx.cnf
%{fmtdir}/pdftex/phyzzx.fmt
# %{fmtdir}/phyzzx

%files omega
%defattr(644,root,root,755)
# %doc %{texmfdist}/doc/aleph
# %doc %{texmfdist}/doc/omega
# %doc %{texmfdist}/doc/lambda
# %dir %{texmfdist}/omega
# %dir %{texmfdist}/dvips/omega
%attr(755,root,root) %{_bindir}/aleph
# %attr(755,root,root) %{_bindir}/lambda
%attr(755,root,root) %{_bindir}/mkocp
%attr(755,root,root) %{_bindir}/mkofm
%attr(755,root,root) %{_bindir}/odvicopy
# %attr(755,root,root) %{_bindir}/odvips
%attr(755,root,root) %{_bindir}/odvitype
# %attr(755,root,root) %{_bindir}/omega
%attr(755,root,root) %{_bindir}/omfonts
%attr(755,root,root) %{_bindir}/opl2ofm
%attr(755,root,root) %{_bindir}/otangle
%attr(755,root,root) %{_bindir}/otp2ocp
%attr(755,root,root) %{_bindir}/outocp
%attr(755,root,root) %{_bindir}/ovf2ovp
%attr(755,root,root) %{_bindir}/ovp2ovf
# %{texmfdist}/dvips/omega/config.omega
# %{texmfdist}/dvips/omega/omega.cfg
# %{texmfdist}/fonts/map/dvips/omega
# %{texmfdist}/tex/generic/omegahyph
# %{texmfdist}/omega/ocp
# %{texmfdist}/omega/otp
# %{texmfdist}/tex/lambda
# %{texmfdist}/source/lambda
# %{texmf}/fmtutil/format.omega.cnf
# %{texmf}/fmtutil/format.aleph.cnf
%{_mandir}/man1/aleph.1*
# %{_mandir}/man1/lambda.1*
%{_mandir}/man1/mkocp.1*
%{_mandir}/man1/mkofm.1*
# %{_mandir}/man1/omega.1*
%{_mandir}/man1/odvicopy.1*
# %{_mandir}/man1/odvips.1*
%{_mandir}/man1/odvitype.1*
%{_mandir}/man1/ofm2opl.1*
%{_mandir}/man1/opl2ofm.1*
%{_mandir}/man1/otp2ocp.1*
%{_mandir}/man1/outocp.1*
%{_mandir}/man1/ovf2ovp.1*
%{_mandir}/man1/ovp2ovf.1*
%{fmtdir}/aleph
%{fmtdir}/omega
# %{fmtdir}/lambda
# %{fmtdir}/lamed
# %{fmtdir}/pdftex/aleph.fmt
# %{fmtdir}/pdftex/lambda.fmt
# %{fmtdir}/pdftex/lamed.fmt
# %{fmtdir}/pdftex/omega.fmt

%files format-mex
%defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/mex
# %{texmfdist}/tex/mex/config/mex.ini
%{fmtdir}/pdftex/mex.fmt
# %{fmtdir}/mex

%files format-amstex
%defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/amstex
# %doc %{texmfdist}/doc/amstex
# %{texmfdist}/tex/amstex
# %{texmf}/fmtutil/format.amstex.cnf
# %{texmf}/fmtutil/format.cyramstex.cnf
%{_mandir}/man1/amstex.1*

# %files csplain
# %defattr(644,root,root,755)
# %dir %{texmfdist}/doc/cslatex
# %doc %{texmfdist}/doc/cslatex/base
# %attr(755,root,root) %{_bindir}/csplain
# %{texmfdist}/tex/csplain
# %{texmf}/fmtutil/format.csplain.cnf

%files format-csplain
%defattr(644,root,root,755)
%{fmtdir}/pdftex/csplain.fmt
# %{fmtdir}/csplain

%files format-pdfcsplain
%defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/pdfcsplain
%{fmtdir}/pdftex/pdfcsplain.fmt
# %{fmtdir}/pdfcsplain

%files format-eplain
%defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/eplain
# %attr(755,root,root) %{_bindir}/etex
%{_mandir}/man1/eplain.1*
# %{_mandir}/man1/etex.1*
# %{texmf}/fmtutil/format.eplain.cnf
%{fmtdir}/pdftex/etex.fmt
# %{fmtdir}/etex

%files context
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/context
# %dir %{texmfdist}/scripts/context/ruby
# %dir %{texmfdist}/scripts/context/stubs
# %dir %{texmfdist}/scripts/context/stubs/unix
# %attr(755,root,root) %{texmfdist}/scripts/context/stubs/unix/*
%attr(755,root,root) %{_bindir}/context
%attr(755,root,root) %{_bindir}/ctxtools
%attr(755,root,root) %{_bindir}/convbkmk
# %attr(755,root,root) %{_bindir}/exatools
%attr(755,root,root) %{_bindir}/luatools
# %attr(755,root,root) %{_bindir}/makempy
# %attr(755,root,root) %{_bindir}/mpstools
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
# %attr(755,root,root) %{texmfdist}/scripts/context/ruby/texmfstart.rb
%attr(755,root,root) %{_bindir}/texmfstart
%attr(755,root,root) %{_bindir}/texshow
%attr(755,root,root) %{_bindir}/textools
%attr(755,root,root) %{_bindir}/texutil
%attr(755,root,root) %{_bindir}/tmftools
%attr(755,root,root) %{_bindir}/xmltools
%{_mandir}/man1/ctxtools.1*
# %{_mandir}/man1/pdftools.1*
%{_mandir}/man1/pstopdf.1*
# %{_mandir}/man1/texfind.1*
# %{_mandir}/man1/texfont.1*
%{_mandir}/man1/texmfstart.1*
# %{_mandir}/man1/textools.1*
# %{_mandir}/man1/texutil.1*
# %{texmfdist}/context
# %{texmfdist}/fonts/enc/dvips/context
# %{texmfdist}/metapost/context
# %{texmfdist}/tex/context
# %exclude %{texmfdist}/tex/context/config/cont-de.ini
# %exclude %{texmfdist}/tex/context/config/cont-en.ini
# %exclude %{texmfdist}/tex/context/config/cont-nl.ini
# %exclude %{texmfdist}/tex/context/config/cont-uk.ini
# %{texmfdist}/tex/generic/context
# %{texmfdist}/tex/latex/context
# %{texmfdist}/bibtex/bst/context
# %{texmf}/fmtutil/format.context.cnf
# %{texmf}/fmtutil/format.luatex.cnf
# %{texmf}/web2c/context.cnf

%files latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lacheck
%attr(755,root,root) %{_bindir}/latex
%attr(755,root,root) %{_bindir}/pslatex

%dir %{texmfdist}/scripts/latexmk
%attr(755,root,root) %{texmfdist}/scripts/latexmk/latexmk.pl
%attr(755,root,root) %{_bindir}/latexmk
%dir %{texmfdist}/scripts/latex2man
%attr(755,root,root) %{texmfdist}/scripts/latex2man/latex2man
%attr(755,root,root) %{_bindir}/latex2man
%dir %{texmfdist}/scripts/svn-multi
%attr(755,root,root) %{texmfdist}/scripts/svn-multi/svn-multi.pl
%attr(755,root,root) %{_bindir}/svn-multi
%dir %{texmfdist}/scripts/texloganalyser
%attr(755,root,root) %{texmfdist}/scripts/texloganalyser/texloganalyser
%attr(755,root,root) %{_bindir}/texloganalyser
%dir %{texmfdist}/scripts/fig4latex
%attr(755,root,root) %{texmfdist}/scripts/fig4latex/fig4latex
%attr(755,root,root) %{_bindir}/fig4latex
%{_mandir}/man1/lacheck.1*
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pslatex.1*
%{fmtdir}/pdftex/latex.fmt
%{fmtdir}/pdftex/mllatex.fmt

%files latex-bibtex
%defattr(644,root,root,755)
%dir %{texmfdist}/bibtex
# %dir %{texmfdist}/bibtex/bib
# %dir %{texmfdist}/bibtex/bst
%dir %{texmfdist}/bibtex/csf
# %dir %{texmfdist}/doc/bibtex
# %dir %{texmf}/bibtex
# %doc %{texmfdist}/doc/bibtex/base
# %doc %{texmfdist}/doc/latex/bibtopic
# %doc %{texmfdist}/doc/latex/bibunits
# %doc %{texmfdist}/doc/latex/footbib
# %doc %{texmfdist}/doc/latex/natbib
%doc %{texmf}/doc/bibtex8
%{_mandir}/man1/bibtex.1*
%{_mandir}/man1/rubibtex.1*

%attr(755,root,root) %{_bindir}/authorindex
%attr(755,root,root) %{_bindir}/biber
%attr(755,root,root) %{_bindir}/bibexport
%attr(755,root,root) %{_bindir}/bibtex
%attr(755,root,root) %{_bindir}/bibtexu
%attr(755,root,root) %{_bindir}/checkcites
%attr(755,root,root) %{_bindir}/rubibtex
%{texmfdist}/bibtex/csf/base
 
%files latex-presentation-bin
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppower4
%attr(755,root,root) %{_bindir}/pdfthumb

%files format-pdflatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdflatex
# %{fmtdir}/pdflatex
%{fmtdir}/pdftex/pdflatex.fmt
%{_mandir}/man1/pdflatex.1*
 
%files tex-thumbpdf
%defattr(644,root,root,755)
# %doc %{texmfdist}/doc/generic/thumbpdf
%attr(755,root,root) %{_bindir}/thumbpdf
%{_mandir}/man1/thumbpdf.1*
# %{texmfdist}/tex/generic/thumbpdf
%{texmfdist}/scripts/thumbpdf

%files fonts-other
%defattr(644,root,root,755)
%{texmfdist}/fonts/map/glyphlist

%files bbox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bbox
%{_mandir}/man1/bbox*

%files detex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/detex
%{_mandir}/man1/detex*

%files dviutils
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/dviasm
%dir %{texmf}/fonts/cmap
# %doc %{texmf}/fonts/cmap/README
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
%{_mandir}/man1/dt2dv*
%{_mandir}/man1/dv2dt*
%{_mandir}/man1/dvi2tty*
%{_mandir}/man1/dvibook*
%{_mandir}/man1/dviconcat*
%{_mandir}/man1/dvidvi*
%{_mandir}/man1/dvigif*
%{_mandir}/man1/dvipos*
%{_mandir}/man1/dviselect*
%{_mandir}/man1/dvitodvi*
%{texmf}/dvipdfmx
%{texmf}/fonts/cmap/dvipdfmx
# %{texmf}/fonts/map/dvipdfmx

%files psutils
%defattr(644,root,root,755)
# %dir %{texmf}/scripts/ps2eps
# %doc %{texmfdist}/doc/epspdf
%attr(755,root,root) %{_bindir}/epsffit
%attr(755,root,root) %{_bindir}/epspdf
%attr(755,root,root) %{_bindir}/epspdftk
%attr(755,root,root) %{_bindir}/extractres
%dir %{texmfdist}/scripts/fragmaster
%attr(755,root,root) %{texmfdist}/scripts/fragmaster/fragmaster.pl
%attr(755,root,root) %{_bindir}/fragmaster
%attr(755,root,root) %{_bindir}/fix*
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
%dir %{texmfdist}/scripts/epstopdf
%attr(755,root,root) %{texmfdist}/scripts/epstopdf/epstopdf.pl
%attr(755,root,root) %{_bindir}/epstopdf
%dir %{texmfdist}/scripts/purifyeps
%attr(755,root,root) %{texmfdist}/scripts/purifyeps/purifyeps
%attr(755,root,root) %{_bindir}/purifyeps
# %attr(755,root,root) %{texmf}/scripts/ps2eps/ps2eps*
%{_mandir}/man1/epsffit*
%{_mandir}/man1/extractres*
%{_mandir}/man1/fix*
%{_mandir}/man1/getafm*
%{_mandir}/man1/includeres*
%{_mandir}/man1/ps2eps.1*
%{_mandir}/man1/psbook*
%{_mandir}/man1/psmerge*
%{_mandir}/man1/psnup*
%{_mandir}/man1/psresize*
%{_mandir}/man1/psselect*
%{_mandir}/man1/pstops*
%{texmfdist}/scripts/epspdf
# %{texmf}/dvips/psutils

%files uncategorized-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/devnag

%files tex4ht
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/tex4ht
# %doc %{texmfdist}/doc/generic/tex4ht
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
# %{texmfdist}/tex/generic/tex4ht
# %{texmfdist}/tex4ht
# %{texmf}/scripts/tex4ht

%files xetex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdvipdfmx
%attr(755,root,root) %{_bindir}/xelatex
%attr(755,root,root) %{_bindir}/xetex
%dir %{fmtdir}/xetex
# %doc %{texmfdist}/doc/generic/ifxetex
# %doc %{texmfdist}/doc/generic/xetex-pstricks
# %doc %{texmfdist}/doc/xelatex
# %doc %{texmfdist}/doc/xetex
# %{texmfdist}/scripts/xetex
# %{texmfdist}/tex/generic/ifxetex
# %{texmfdist}/tex/generic/xetexconfig
# %{texmfdist}/tex/latex/latexconfig/xelatex.ini
# %{texmfdist}/tex/plain/config/xetex.ini
# %{texmfdist}/tex/xelatex
# %{texmfdist}/tex/xetex
# %{texmf}/fmtutil/format.xetex.cnf
%{fmtdir}/xetex/xetex.fmt
%{fmtdir}/xetex/xelatex.fmt
# %{fmtdir}/pdftex/xelatex.fmt
# %{fmtdir}/pdftex/xetex.fmt
# %{fmtdir}/xelatex

%files xmltex
%defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/pdfxmltex
# %attr(755,root,root) %{_bindir}/xmltex
# %doc %{texmfdist}/doc/xmltex
# %{texmfdist}/source/xmltex
# %{texmfdist}/tex/xmltex
# %{texmf}/fmtutil/format.xmltex.cnf
# %{fmtdir}/pdftex/pdfxmltex.fmt
# %{fmtdir}/pdftex/xmltex.fmt
# %{fmtdir}/pdfxmltex
# %{fmtdir}/xmltex

%files luatex
# %dir %{texmfdist}/scripts/context/lua
%attr(755,root,root) %{_bindir}/luatex
# %attr(755,root,root) %{_bindir}/luatangle
%attr(755,root,root) %{_bindir}/texlua
%attr(755,root,root) %{_bindir}/texluac
%attr(755,root,root) %{texmfdist}/scripts/cachepic/cachepic.tlu
%attr(755,root,root) %{_bindir}/cachepic
# %attr(755,root,root) %{texmfdist}/scripts/context/lua/*
%attr(755,root,root) %{_bindir}/luatools
%attr(755,root,root) %{_bindir}/mtxrun
%attr(755,root,root) %{texmf}/scripts/texlive/rungs.tlu
%attr(755,root,root) %{_bindir}/rungs
%attr(755,root,root) %{_bindir}/texdoc
%attr(755,root,root) %{texmf}/scripts/texdoc/texdoc.tlu
%{_mandir}/man1/luatex.1*
