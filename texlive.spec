# TODO:
# MAIN TODO (sort by importnce):
# - need more %dir (poldek says it missed)
# - texlive-format-pdflatex deps
# - check unpackaged files
# - pl updates
# - maybe more splits (e.g. latex subpackages)
# - context: consider more splitting, check dependencies
# - omega: consider more splitting, check dependencies
# - tdphp: is it really useful?
# - allow using Type1 fonts in others applications (symlink to
#   /usr/share/fonts/Type1 ?)
# - fix package removal:
#   /usr/bin/texhash[77]: kpsewhich: not found
#
# FHS TODO:
# - merge rhconfig and texmfsysvar patches
# - texmfsysvar patch: change fmtutil and web2cdir variables instead
#   of creating texmfsys{config,var} variables?
# - move config files to /etc
# - merge all above with configure switch "--enable-fhs" and send it to TE
#
# TeXLive specific TODO:
# - fix broken symlinks in /usr/bin (see line 3564)
# - summary/description correcting (all languages)
# - texk/web2c doesn't build (luatex option)
# - %files latex-bibtex-revtex4
# - Check CEF/cjk!
#
# Subpackages TODO:
# check deps the following subpackages:
# - latex-exam
# - latex-SIunits
#
%include	/usr/lib/rpm/macros.perl
#
%bcond_without	bootstrap
#
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
Release:	0.8.3
Epoch:		1
License:	distributable
Group:		Applications/Publishing/TeX
Source0:	http://tug.org/svn/texlive/branches/branch2008/Master/source/%{name}-%{version}-source.tar.lzma
# Source0-md5:	554287c3e458da776edd684506048d45
Source1:	ftp://tug.org/texlive/historic/2008/%{name}-20080822-texmf.tar.lzma
# Source1-md5:	fa74072e1344e8390eb156bcda61a8b2
Source4:	%{name}.cron
Source5:	xdvi.desktop
Source6:	xdvi.png
Patch0:		%{name}-am.patch
Patch1:		%{name}-20080816-kpathsea-ar.patch
URL:		http://www.tug.org/texlive/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	clisp
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
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	t1lib-devel >= 5.0.2
BuildRequires:	texinfo
%if %{with bootstrap}
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-latex-cyrillic
BuildRequires:	tetex-tex-babel
%else
BuildRequires:	texlive-format-latex
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-latex-cyrillic
BuildRequires:	texlive-tex-babel
# fill with future texlive BR. guesses ones for now
%endif
BuildRequires:	unzip
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel >= 1.2.1
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-cm = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-misc = %{epoch}:%{version}-%{release}
Requires:	%{name}-metafont = %{epoch}:%{version}-%{release}
Requires:	awk
Requires:	dialog
Requires:	kpathsea = %{epoch}:%{version}-%{release}
Requires:	sed
Requires:	sh-utils
Requires:	texconfig = %{epoch}:%{version}-%{release}
Requires:	textutils
Suggests:	tmpwatch
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
Obsoletes:	tetex-latex-vnps
Obsoletes:	tetex-latex-vnr
Obsoletes:	tetex-oxdvi
Obsoletes:	tetex-oxdvi
Obsoletes:	tetex-plain-dvips
Obsoletes:	tetex-plain-dvips
Obsoletes:	tetex-plain-mathtime
Obsoletes:	tetex-plain-mathtime
Obsoletes:	tetex-plain-misc
Obsoletes:	tetex-plain-misc
Obsoletes:	tetex-plain-plnfss
Obsoletes:	tetex-plain-plnfss
Obsoletes:	tetex-tex-hyphen
Obsoletes:	tetex-tex-vietnam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texmf	%{_datadir}/texmf
%define		texmfdist %{texmf}-dist
%define		texmfdoc %{texmf}-doc
%define		fmtdir	/var/lib/texmf/web2c
%define		texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2;
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

%package doc
Summary:	Documentation for TeX Live
Group:		Documentation

%description doc
Assorted useful documentation for TeX Live.

%package doc-bg
Summary:	Bulgarian documentation for TeX Live
Group:		Documentation

%description doc-bg
Assorted useful Bulgarian documentation for TeX Live.

%package doc-cs
Summary:	Czech documentation for TeX Live
Group:		Documentation

%description doc-cs
Assorted useful Czech documentation for TeX Live.

%package doc-de
Summary:	German documentation for TeX Live
Group:		Documentation

%description doc-de
Assorted useful German documentation for TeX Live.

%package doc-el
Summary:	Greek documentation for TeX Live
Group:		Documentation

%description doc-el
Assorted useful Greek documentation for TeX Live.

%package doc-es
Summary:	Spanish documentation for TeX Live
Group:		Documentation

%description doc-es
Assorted useful Spanish documentation for TeX Live.

%package doc-fi
Summary:	Finnish documentation for TeX Live
Group:		Documentation

%description doc-fi
Assorted useful Finnish documentation for TeX Live.

%package doc-fr
Summary:	French documentation for TeX Live
Group:		Documentation

%description doc-fr
Assorted useful French documentation for TeX Live.

%package doc-it
Summary:	Italian documentation for TeX Live
Group:		Documentation

%description doc-it
Assorted useful Italian documentation for TeX Live.

%package doc-ja
Summary:	Japanese documentation for TeX Live
Group:		Documentation

%description doc-ja
Assorted useful Japanese documentation for TeX Live.

%package doc-ko
Summary:	Korean documentation for TeX Live
Group:		Documentation

%description doc-ko
Assorted useful Korean documentation for TeX Live.

%package doc-mn
Summary:	Mongolian documentation for TeX Live
Group:		Documentation

%description doc-mn
Assorted useful Mongolian documentation for TeX Live.

%package doc-nl
Summary:	Dutch documentation for TeX Live
Group:		Documentation

%description doc-nl
Assorted useful Dutch documentation for TeX Live.

%package doc-pl
Summary:	Polish documentation for TeX Live
Group:		Documentation

%description doc-pl
Assorted useful Polish documentation for TeX Live.

%package doc-pt
Summary:	Portuguese documentation for TeX Live
Group:		Documentation

%description doc-pt
Assorted useful Portuguese documentation for TeX Live.

%package doc-ru
Summary:	Russian documentation for TeX Live
Group:		Documentation

%description doc-ru
Assorted useful Russian documentation for TeX Live.

%package doc-sk
Summary:	Slovak documentation for TeX Live
Group:		Documentation

%description doc-sk
Assorted useful Slovak documentation for TeX Live.

%package doc-sl
Summary:	Slovenian documentation for TeX Live
Group:		Documentation

%description doc-sl
Assorted useful Slovenian documentation for TeX Live.

%package doc-th
Summary:	Thai documentation for TeX Live
Group:		Documentation

%description doc-th
Assorted useful Thai documentation for TeX Live.

%package doc-tr
Summary:	Turkish documentation for TeX Live
Group:		Documentation

%description doc-tr
Assorted useful Turkish documentation for TeX Live.

%package doc-uk
Summary:	Ukrainian documentation for TeX Live
Group:		Documentation

%description doc-uk
Assorted useful Ukrainian documentation for TeX Live.

%package doc-vi
Summary:	Vietnamese documentation for TeX Live
Group:		Documentation

%description doc-vi
Assorted useful Vietnamese documentation for TeX Live.

%package doc-zh_CN
Summary:	Chinese documentation for TeX Live
Group:		Documentation

%description doc-zh_CN
Assorted useful Chinese documentation for TeX Live.

%package doc-Catalogue
Summary:	TeX Catalogue
Summary(pl.UTF-8):	Katalog TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description doc-Catalogue
TeX Catalogue.

%description doc-Catalogue -l pl.UTF-8
Katalog TeXa.

%package doc-tug-faq
Summary:	TeX User Group FAQ
Summary(hu.UTF-8):	TeX felhasználók FAQ-ja
Summary(pl.UTF-8):	FAQ Grupy Użytkowników TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-doc-LaTeX-FAQ-francaise
Obsoletes:	tetex-doc-de-tex-faq
Obsoletes:	tetex-doc-uktug-faq

%description doc-tug-faq
TeX User Group FAQ.

%description doc-tug-faq -l hu.UTF8
TeX felhasználók FAQ-ja.

%description doc-tug-faq -l pl.UTF-8
FAQ Grupy Użytkowników TeXa.

%package doc-latex
Summary:	Basic LaTeX packages documentation
Summary(hu.UTF-8):	Az alap LaTeX csomagok dokumentációja
Summary(pl.UTF-8):	Podstawowa dokumentacja do pakietów LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

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

%package metafont
Summary:	MetaFont
Summary(hu.UTF-8):	MetaFont
Summary(pl.UTF-8):	Zestaw narzędzi MetaFont
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description metafont
MetaFont.

%description metafont -l pl.UTF-8
Zestaw narzędzi MetaFont.

%package metapost
Summary:	MetaPost
Summary(hu.UTF-8):	MetaPost
Summary(pl.UTF-8):	Zestaw narzędzi MetaPost
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-matapost

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
Requires:	%{name}-metafont = %{epoch}:%{version}-%{release}
Requires:	xdvi = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-texconfig

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
Requires:	%{name}-metafont = %{epoch}:%{version}-%{release}
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
Summary(hu.UTF-8):	Xindy vietnám nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-vietnamese
Xindy vietnamese language

%description -n xindy-vietnamese -l hu.UTF-8
Xindy vietnám nyelv


%package pdftex
Summary:	TeX generating PDF files instead DVI
Summary(pl.UTF-8):	TeX generujący pliki PDF zamiast DVI
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-type1-bluesky = %{epoch}:%{version}-%{release}

%description pdftex
TeX generating PDF files instead DVI.

%description pdftex -l pl.UTF-8
TeX generujący pliki PDF zamiast DVI.

%package omega
Summary:	Extended unicode TeX
Summary(pl.UTF-8):	Omega - TeX ze wsparciem dla unikodu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-omega = %{epoch}:%{version}-%{release}
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}

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

%description plain
Plain TeX format basic files.

%description plain -l pl.UTF-8
Podstawowe pliki dla formatu Plain TeX.

%package format-plain
Summary:	TeX Plain format
Summary(pl.UTF-8):	Format TeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}

%description format-plain
TeX Plain format.

%description format-plain -l pl.UTF-8
Format TeX Plain.

%package format-pdftex
Summary:	PDFTeX Plain format
Summary(pl.UTF-8):	Format PDFTeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
# for epstopdf to work
Requires:	fonts-Type1-urw
Requires:	ghostscript

%description format-pdftex
PDFTeX Plain format.

%description format-pdftex -l pl.UTF-8
Format PDFTeX Plain.

%package format-pdfetex
Summary:	PDFTeX EPlain format
Summary(pl.UTF-8):	Format PDFTeX EPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}

%description format-pdfetex
PDFTeX EPlain format.

%description format-pdfetex -l pl.UTF-8
Format PDFTeX EPlain.

# MeX Plain format

%package mex
Summary:	MeX Plain Format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla format MeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	texlive-fonts-pl = %{epoch}:%{version}-%{release}
Requires:	texlive-plain = %{epoch}:%{version}-%{release}

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
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-ams
Obsoletes:	tetex-plain-amsfonts

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
Obsoletes:	tetex-ams

%description format-amstex
American Mathematical Society macros for Plain TeX.

%description format-amstex -l pl.UTF-8
Makra AMS (American Mathematical Society) dla formatu Plain TeX.

%package format-pdfamstex
Summary:	AMS macros for PDFTeX
Summary(pl.UTF-8):	Makra AMS dla formatu PDFTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-amstex = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}

%description format-pdfamstex
American Mathematical Society macros for PDFTeX.

%description format-pdfamstex -l pl.UTF-8
Makra AMS (American Mathematical Society) dla formatu PDFTeX.

# CSPlain format

%package csplain
Summary:	TeX CSPlain format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla formatu TeX CSPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-cs = %{epoch}:%{version}-%{release}
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}

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

%description format-pdfcslatex
PDF CSLaTeX format.

%description format-pdfcslatex -l pl.UTF-8
Format PDF CSLaTeX.

# Cyrillic Plain format

%package cyrplain
Summary:	Cyrillic Plain format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla formatu Cyrillic Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}

%description cyrplain
Cyrillic Plain format basic files.

%description cyrplain -l pl.UTF-8
Podstawowe pliki dla formatu Cyrillic Plain.

%package format-cyrplain
Summary:	Cyrillic Plain format
Summary(pl.UTF-8):	Format Cyrillic Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-cyrplain = %{epoch}:%{version}-%{release}

%description format-cyrplain
Cyrillic Plain format.

%description format-cyrplain -l pl.UTF-8
Format Cyrillic Plain.

%package format-cyramstex
Summary:	Cyrillic AMSTeX format
Summary(pl.UTF-8):	Format Cyrillic AMSTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-cyramstex

%description format-cyramstex
Cyrillic AMSTeX format.

%description format-cyramstex -l pl.UTF-8
Format Cyrillic AMSTeX.

%package format-cyrtexinfo
Summary:	Cyrillic TeXInfo format
Summary(pl.UTF-8):	Format Cyrillic TeXInfo
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-cyrtexinfo

%description format-cyrtexinfo
Cyrillic TeXInfo format.

%description format-cyrtexinfo -l pl.UTF-8
Format Cyrillic TeXInfo.

# EPlain format

%package eplain
Summary:	EPlain format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla formatu EPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
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
Requires:	%{name}-eplain = %{epoch}:%{version}-%{release}

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
Obsoletes:	tetex-latex-context

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
Suggests:	%{name}-latex-ucs = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-koma-script
Obsoletes:	tetex-latex-SIunits
Obsoletes:	tetex-latex-caption
Obsoletes:	tetex-latex-curves
Obsoletes:	tetex-latex-dinbrief
Obsoletes:	tetex-latex-draftcopy
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
Obsoletes:	tetex-latex-pstriks
Obsoletes:	tetex-latex-revtex4
Obsoletes:	tetex-latex-seminar
Obsoletes:	tetex-latex-t2
Obsoletes:	tetex-latex-titlesec
Obsoletes:	tetex-latex-tools
Obsoletes:	tetex-latex-units
Obsoletes:	tetex-mwcls
Obsoletes:	tetex-revtex4

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

%package latex-12many
Summary:	Generalising mathematical index sets
Summary(hu.UTF-8):	A matematikai halmazok indexelésének általánosítása
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-12many
Generalising mathematical index sets.

%description latex-12many -l hu.UTF-8
A matematikai halmazok indexelésének általánosítása.

%package latex-abstract
Summary:	Control the typesetting of the abstract environment
Summary(hu.UTF-8):	Az "abstract" környezet szedésének irányítása
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-abstract
Control the typesetting of the abstract environment.

%description latex-abstract -l hu.UTF-8
Az "abstract" környezet szedésének irányítása.

%package latex-accfonts
Summary:	Utilities to derive new fonts from existing ones
Summary(hu.UTF-8):	Eszközök új betűtípusok származtatására már létezőkből
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description latex-accfonts
Utilities to derive new fonts from existing ones.

%description latex-accfonts -l hu.UTF-8
Eszközök új betűtípusok származtatására már létezőkből.

%package latex-adrconv
Summary:	BibTeX styles to implement an address database
Summary(hu.UTF-8):	BibTeX stílusok cím-adatbázis megvalósításához
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-adrconv
BibTeX styles to implement an address database.

%description latex-adrconv -l hu.UTF-8
BibTeX stílusok cím-adatbázis megvalósításához.


%package latex-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Summary(pl.UTF-8):	Wirtualne fonty dla plików PDF z fontami CMR o kodowaniu T1
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-ae = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

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
Obsoletes:	tetex-latex-amscls
Obsoletes:	tetex-latex-amsfonts
Obsoletes:	tetex-latex-amsmath

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
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-appendix
Extra control of appendices.

%description latex-appendix -l hu.UTF-8
Az appendixek nagyobb irányítása.

%package latex-backgammon
Summary:	LaTeX package to documenting backgammon games
Summary(hu.UTF-8):	LaTeX csomag backgammon játékok dokumentálására
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-backgammon
LaTeX package to documenting backgammon games.

%description latex-backgammon -l hu.UTF-8
LaTeX csomag backgammon játékok dokumentálására

%package latex-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Summary(pl.UTF-8):	Tablicowy wariant fontów Computer Modern z obsługą LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-bbm = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%description latex-bbm -l pl.UTF-8
Tablicowy wariant fontów Computer Modern z obsługą LaTeXa.

%package latex-bardiag
Summary:	LateX package for drawing bar diagrams
Summary(pl.UTF-8):	LaTeX csomag oszlopdiagramok rajzolására
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description latex-bardiag
LateX package for drawing bar diagrams.

%description latex-bardiag -l hu.UTF-8
LaTeX csomag oszlopdiagramok rajzolására.

%package latex-bbold
Summary:	Sans serif blackboard bold for LaTeX
Summary(pl.UTF-8):	Tablicowy tłusty font sans serif dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-bbold = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

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
Obsoletes:	tetex-bibtex
Obsoletes:	tetex-natbib
Obsoletes:	tetex-rubibtex

%description latex-bibtex
Bibliography management for LaTeX.

%description latex-bibtex -l pl.UTF-8
Zarządzanie bibliografią dla LaTeXa.

%package latex-beamer
Summary:	A LaTeX class for producing presentations and slides
Summary(hu.UTF-8):	LaTeX dokumentumosztály prezentációk és fóliák készítéséhez
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-beamer
A LaTeX class for producing presentations and slides.

%description latex-beamer -l hu.UTF-8
LaTeX dokumentumosztály prezentációk és fóliák készítéséhez.

%package latex-bezos
Summary:	Packages by Javier Bezos (additional math tools)
Summary(hu.UTF-8):	Javier Bezos csomagjai (további matematikai eszközök)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-bezos
Packages by Javier Bezos (additional math tools).

%description latex-bezos
Javier Bezos csomagjai (további matematikai eszközök).

%package latex-bibtex-ams
Summary:	BibTeX style files for American Mathematical Society publications
Summary(pl.UTF-8):	Pliki stylów BibTeXa do publikacji American Mathematical Society
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-ams = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-ams

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

%package latex-bibtex-nor
Summary:	Norwegian variants of the standard BibTeX styles
Summary(pl.UTF-8):	Norweskie warianty standardowych stylów BibTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}

%description latex-bibtex-nor
Norwegian variants of the standard BibTeX styles.

%description latex-bibtex-nor -l pl.UTF-8
Norweskie warianty standardowych stylów BibTeXa.

%package latex-bibtex-pl
Summary:	Polish bibliography management for LaTeX
Summary(pl.UTF-8):	Polska wersja zarządzania bibliografią dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-plbib

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
Obsoletes:	tetex-bibtex-germbib

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
Obsoletes:	tetex-bibtex-revtex4

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
Obsoletes:	tetex-bibtex-jurabib

%description latex-bibtex-jurabib
Extended BibTeX citation support for the humanities and legal texts.

%description latex-bibtex-jurabib -l pl.UTF-8
Rozszerzona obsługa cytowania BibTeXa do tekstów humanistycznych i
prawniczych.

%package latex-bibtex-styles
Summary:	Various BibTeX styles
Summary(hu.UTF-8):	Vegyes BibTeX stílusok
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}

%description latex-bibtex-styles
Various BibTeX styles.

%description latex-bibtex-styles -l hu.UTF-8
Vegyes BibTeX stílusok.

%package latex-bibtex-vancouver
Summary:	Bibliographic style file for Biomedical Journals
Summary(hu.UTF-8):	Irodalomjegyzék-stílus a Biomedical Journal-hoz
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}

%description latex-bibtex-vancouver
Bibliographic style file for Biomedical Journals.

%description latex-bibtex-vancouver -l hu.UTF-8
Irodalomjegyzék-stílus a Biomedical Journal-hoz.

%package latex-booktabs
Summary:	Publication quality tables in LaTeX
Summary(hu.UTF-8):	Nyomdai minőségű táblázatok LaTeX-ben
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-booktabs
Publication quality tables in LaTeX.

%description latex-booktabs -l hu.UTF-8
Nyomdai minőségű táblázatok LaTeX-ben.


%package latex-caption
Summary:	Customising captions in floating environments
Summary(hu.UTF-8):	Feliratok testreszabása úszó környezetekben
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-caption
Customising captions in floating environments.

%description latex-caption -l hu.UTF-8
Feliratok testreszabása úszó környezetekben.

%package latex-carlisle
Summary:	Miscellaneous small packages by David Carlisle
Summary(pl.UTF-8):	Różne małe pakiety autorstwa Davida Carlisle
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

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
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-comment
Selectively include/excludes portions of text.

%description latex-comment -l hu.UTF-8
A szöveg részeinek beillesztése/kihagyása.

%package latex-concmath
Summary:	LaTeX package and font definition files to access the Concrete math fonts
Summary(pl.UTF-8):	Pakiet LaTeXa i pliki definicji fontów udostępniające fonty matematyczne Concrete
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-concmath = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

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
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-currvita
Typeset a curriculum vitae.

%description latex-currvita -l hu.UTF-8
Önéletrajzok írása.

%package latex-curves
Summary:	Curves for LaTeX picture environment
Summary(hu.UTF-8):	Görbék LaTeX picture környezetébe
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-curves
Curves for LaTeX picture environment.

%description latex-curves -l hu.UTF-8
Görbék LaTeX picture környezetébe.

%package latex-custom-bib
Summary:	Customized BibTeX styles for LaTeX
Summary(pl.UTF-8):	Dostosowywanie stylów BibTeXa dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

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

%description latex-cyrillic
LaTeX Cyrillic support.

%description latex-cyrillic -l pl.UTF-8
Obsługa cyrylicy dla LaTeXa.

%package latex-dstroke
Summary:	LaTeX doublestroke font
Summary(pl.UTF-8):	Podwójnie kreślony font dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-dstroke = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-dstroke
Doublestroke font for typesetting the mathematical symbols for the
natural numbers, whole numbers, rational numbers, real numbers and
complex numbers.

%description latex-dstroke -l pl.UTF-8
Podwójnie kreślony font do składania symboli matematycznych liczb
naturalnych, całkowitych, wymiernych, rzeczywistych i zespolonych.

%package latex-enumitem
Summary:	A package to customize the three basic lists
Summary(hu.UTF-8):	Egy csomag, amivel testreszabhatod a három alapvető listát
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-enumitem
A package to customize the three basic lists (enumerate, itemize and
description).

%description latex-enumitem
Egy csomag, amivel testreszabhatod a három alapvető listakörnyezetet
(enumerate, itemize, description).

%package latex-exam
Summary:	The exam document class attempts to make it easy for even a LaTeX novice to prepare exams
Summary(hu.UTF-8):	Az exam dokumentumosztály segítségével könnyűvé válik LaTeX-ben a feladatsorok készítése
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-exam
The exam document class attempts to make it easy for even a LaTeX
novice to prepare exams.

%description latex-exam -l hu.UTF-8
Az exam dokumentumosztály segítségével könnyűvé válik LaTeX-ben a
feladatsorok készítése.

%package latex-gbrief
Summary:	Letter document class
Summary(hu.UTF-8):	Levél dokumentumosztály
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-gbrief
Letter document class.

%description latex-gbrief -l hu.UTF-8
Levél dokumentumosztály.


%package latex-jknappen
Summary:	Miscellaneous packages by Joerg Knappen
Summary(pl.UTF-8):	Różne pakiety autorstwa Joerga Knappena
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-jknappen = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-jknappen
Miscellaneous macros, mostly for making use of extra fonts, by Joerg
Knappen, including sgmlcmpt.

%description latex-jknappen -l pl.UTF-8
Różne makra, głównie do używania dodatkowych fontów autorstwa Joerga
Knappena. Zawiera sgmlcmpt.

%package latex-leftidx
Summary:	Left and right subscripts and superscripts in math mode
Summary(hu.UTF-8):	Bal és jobboldali alsó és felső indexek matematikai módban
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-leftidx
Left and right subscripts and superscripts in math mode.

%description latex-leftidx -l hu.UTF-8
Bal és jobboldali alsó és felső indexek matematikai módban.

%package latex-lm
Summary:	LaTeX styles for Latin Modern family fonts
Summary(pl.UTF-8):	Style LaTeXa dla fontów z rodziny Latin Modern
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-lm = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

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
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description latex-lastpage
Reference last page for Page N of M type footers.

%description latex-lastpage -l hu.UTF-8
Az utolsó oldalra hivatkozás "N/M. oldal" típusú lábfejekhez.

%package latex-lineno
Summary:	Line numbers on paragraphs
Summary(pl.UTF-8):	Numery linii dla paragrafów
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

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

%package latex-microtype
Summary:	An interface to the micro-typographic extensions of pdfTeX
Summary(pl.UTF-8):	Interfejs do rozszerzeń mikrotypograficznych pdfTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

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
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-musictex
Typesetting music with TeX.

%description latex-musictex -l hu.UTF-8
Zenék szedése TeX-hel.

%package latex-lucidabr
Summary:	Package to make Lucida Bright fonts usable with LaTeX
Summary(pl.UTF-8):	Pakiet umożliwiający używanie fontów Lucida Bright w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

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

%package latex-mathpple
Summary:	Use PostScript Palatino for typesetting maths
Summary(pl.UTF-8):	Używanie postscriptowych fontów Palatino do składania wzorów matematycznych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-adobe = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-mathpple
The package defines the PostScript font family `Palatino' (ppl) as the
default roman font and then uses the `mathpple' fonts for typesetting
math. These virtual fonts have been created for typesetting math in a
style that suits the Palatino text fonts. The AMS fonts, when used
additionally, will be scaled to fit Palatino.

%description latex-mathpple -l pl.UTF-8
Pakiet definiuje rodzinę fontów postscriptowych Palatino (ppl) jako
domyślny font roman i używa fontów mathpple do składania wzorów
matematycznych. Te wirtualne fonty zostały stworzone do składania
wzorów matematycznych w stylu pasującym do fontów tekstowych Palatino.
Fonty AMS, jeśli są dodatkowo używane, zostaną przeskalowane tak, by
pasować do Palatino.

%package latex-mathtime
Summary:	Mathtime fonts for LaTeX
Summary(pl.UTF-8):	Fonty Mathtime dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-mathtime
The Mathtime fonts have a number of characters remapped to positions
different from the ones normally used by the corresponding TeX
CM-fonts. For the symbol font ``operators'' the corresponding mathtime
style files use the Times Roman font (often called something like:
ptmr or ptmr7t or ptmrq).

%description latex-mathtime -l pl.UTF-8
Fonty Mathtime zawierają wiele znaków przemapowanych na pozycje
różniące się od tych normalnie używanych w odpowiadających im TeXowych
fontach CM. Dla fontu symboli "operators" odpowiadający styl mathtime
używa fontu Times Roman (zazwyczaj nazywanego w stylu ptmr, ptmr7t lub
ptmrq).

%package latex-mflogo
Summary:	LaTeX support for MetaFont and logo fonts
Summary(pl.UTF-8):	Obsługa LaTeXa dla MetaFonta i fontów logo
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-mflogo = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

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

%description latex-mltex
Support for MLTeX, the multilingual TeX extension from Michael J.
Ferguson.

%description latex-mltex -l pl.UTF-8
Wsparcie dla MLTeXa - rozszerzenia TeXa z obsługą wielu języków,
autorstwa Michaela J. Fergusona.

%package latex-multienum
Summary:	Multi-column enumerated lists
Summary(hu.UTF-8):	Többoszlopos számozott listák
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-multienum
Multi-column enumerated lists.

%description latex-multienum -l hu.UTF-8
Többoszlopos számozott listák.


%package latex-moreverb
Summary:	Extended verbatim
Summary(hu.UTF-8):	Kiterjesztett verbatim
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-moreverb
Extended verbatim.

%description latex-moreverb -l hu.UTF-8
Kiterjesztett verbatim.

%package latex-ntheorem
Summary:	Enhanced theorem environment
Summary(hu.UTF-8):	Bővített tétel környezet
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-ntheorem
Enhanced theorem environment.

%description latex-ntheorem -l hu.UTF-8
Bővített tétel környezet

%package latex-palatcm
Summary:	Palatino + Computer Modern math fonts for LaTeX
Summary(pl.UTF-8):	Fonty matematyczne Palatino i Computer Modern dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-palatcm
Palatino + Computer Modern math fonts for LaTeX.

%description latex-palatcm -l pl.UTF-8
Fonty matematyczne Palatino i Computer Modern dla LaTeXa.

%package latex-pgf
Summary:	The TeX Portable Graphic Format
Summary(hu.UTF-8):	TeX Portable Graphic Formátum
Summary(pl.UTF-8):	Przenośny format grafiki dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-xcolor = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-pgf

%description latex-pgf
A macro package for creating graphics directly in TeX and LaTeX.

%description latex-pgf -l hu.UTF-8
Makró csomag rajzok készítéséhez közvetlenül TeX-ben és LaTeX-ben.

%description latex-pgf -l pl.UTF-8
Pakiet makr do tworzenia grafiki bezpośrednio z TeXa i LaTeXa.

%package latex-psnfss
Summary:	LaTeX font support for common PostScript fonts
Summary(pl.UTF-8):	Obsługa popularnych fontów postscriptowych w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-adobe = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-mathptm
Obsoletes:	tetex-latex-mathptmx

%description latex-psnfss
LaTeX font definition files, macros and font metrics for common
PostScript fonts.

%description latex-psnfss -l pl.UTF-8
LaTeXowe pliki definicji fontów, makra i metryki fontów dla
popularnych fontów postscriptowych.

%package latex-pxfonts
Summary:	PX fonts LaTeX support
Summary(pl.UTF-8):	Obsługa fontów PX w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-px = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-pxfonts
PX fonts LaTeX support.

%description latex-pxfonts -l pl.UTF-8
Obsługa fontów PX w LaTeXu.

%package latex-qfonts
Summary:	A collection of PostScript (Adobe Type 1) fonts in QX layout
Summary(pl.UTF-8):	Zestaw fontów postscriptowych (Adobe Type 1) w układzie QX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-qfonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-qfonts
A collection of Type 1 fonts; include QuasiBookman, QuasiChancery,
QuasiCourier, QuasiPalatino, QuasiSwiss, QuasiSwissCondensed, and
QuasiTimes (regular, italic, bold and bold italic), based on URW++
fonts distributed with Ghostscript. The fonts are encoded according to
QX layout which facilitates multilingual and technical typesetting
using TeX, preserving usability in Windows applications.

%description latex-qfonts -l pl.UTF-8
Zestaw fontów Type 1; zawiera QuasiBookman, QuasiChancery,
QuasiCourier, QuasiPalatino, QuasiSwiss, QuasiSwissCondensed oraz
QuasiTimes (zwykłe, pochyłe, tłuste i tłuste pochyłe), oparte na
fontach URW++ rozpowszechnianych z Ghostscriptem. Fonty są kodowane
zgodnie z układem QX, który ułatwia skład wielojęzyczny i techniczny w
TeXu, zachowując przydatność dla aplikacji windowsowych.

%package latex-SIstyle
Summary:	Package to typeset SI units, numbers and angles
Summary(hu.UTF-8):	Csomag SI egységek, számok és szögek szedésére
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex-ams = %{epoch}:%{version}-%{release}

%description latex-SIstyle
Package to typeset SI units, numbers and angles.

%description latex-SIstyle -l hu.UTF-8
Csomag SI egységek, számok és szögek szedésére.

%package latex-SIunits
Summary:	The SIunits package can be used to standardise the use of units in your writings
Summary(hu.UTF-8):	Az SIunits csomag a mennyiségek egységes írásában nyújt segítséget
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex-ams = %{epoch}:%{version}-%{release}

%description latex-SIunits
The SIunits package can be used to standardise the use of units in
your writings.

%description latex-SIunits -l hu.UTF-8
Az SIunits csomag a mennyiségek egységes írásában nyújt segítséget.

%package latex-Tabbing
Summary:	Tabbing with accented letters
Summary(hu.UTF-8):	Tabbing környezet ékezetes betűk használatával
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description latex-Tabbing
Tabbing with accented letters.

%description latex-Tabbing -l hu.UTF-8
Tabbing környezet ékezetes betűk használatával.

%package latex-urwvn
Summary:	URWVN fonts
Summary(pl.UTF-8):	Fonty URWVN
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-urwvn = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-urwvn
URWVN fonts.

%description latex-urwvn -l pl.UTF-8
Fonty URWVN.

%package latex-txfonts
Summary:	TX fonts LaTeX support
Summary(pl.UTF-8):	Obsługa fontów TX w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-tx = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-txfonts
TX fonts LaTeX support.

%description latex-txfonts -l pl.UTF-8
Obsługa fontów TX w LaTeXu.

%package latex-ucs
Summary:	This package contains support for using UTF-8 as input encoding in LaTeX documents
Summary(hu.UTF-8):	Ez a csomag lehetővé teszi UTF-8 kódolást a LaTeX dokumentumokban
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-ucs
This package contains support for using UTF-8 as input encoding in
LaTeX documents.

%description latex-ucs -l hu.UTF-8
Ez a csomag lehetővé teszi UTF-8 kódolást a LaTeX dokumentumokban.

%package latex-umlaute
Summary:	An interface to inputenc for using alternate input encodings
Summary(pl.UTF-8):	Interfejs inputenc do używania alternatywnych kodowań wejściowych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

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
Obsoletes:	tetex-latex-xcolor

%description
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

%package format-latex
Summary:	LaTeX macro package
Summary(pl.UTF-8):	Pakiet makr LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	hugelatex

%description format-latex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains LaTeX format.

%description format-latex -l pl.UTF-8
LaTeX jest frontendem do systemu formatującego tekst TeX. Jest
łatwiejszy w użyciu niż TeX. Jest właściwie zestawem makr TeXowych,
dających użytkownikom wygodne, predefiniowane formaty dokumentów.

Ten pakiet zawiera format LaTeX.

%package format-pdflatex
Summary:	PDF LaTeX macro package
Summary(pl.UTF-8):	Pakiet makr PDF LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-jknappen = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-psnfss = %{epoch}:%{version}-%{release}
Requires:	%{name}-metafont = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}

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

# PLaTeX format

%package platex
Summary:	PLaTeX format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla formatu PLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-pl = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description platex
PLaTeX format basic files.

%description platex -l pl.UTF-8
Podstawowe pliki dla formatu PLaTeX.

%package format-platex
Summary:	PLaTeX format
Summary(pl.UTF-8):	Format PLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-platex = %{epoch}:%{version}-%{release}

%description format-platex
PLaTeX format.

%description format-platex -l pl.UTF-8
Format PLaTeX.

%package format-pdfplatex
Summary:	PDF PLaTeX format
Summary(pl.UTF-8):	Format PDF PLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-type1-pl = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Requires:	%{name}-platex = %{epoch}:%{version}-%{release}

%description format-pdfplatex
PDF PLaTeX format.

%description format-pdfplatex -l pl.UTF-8
Format PDF PLaTeX.

# # TeX generic macros #

%package tex-babel
Summary:	Multilingual support for TeX
Summary(pl.UTF-8):	Obsługa wielu języków dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

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

%description tex-german
Supports the new German orthography (neue deutsche Rechtschreibung).

%description tex-german -l pl.UTF-8
Obsługa nowej ortografii niemieckiej (neue deutsche Rechtschreibung).

%package tex-mfpic
Summary:	Macros which generate Metafont or Metapost for drawing pictures
Summary(pl.UTF-8):	Makra generujące Metafont lub Metapost do rysowania obrazków
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

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
Obsoletes:	tetex-tex-eijkhout

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

%description tex-pictex
Picture drawing macros for TeX and LaTeX.

%description tex-pictex -l pl.UTF-8
Makra do rysowania obrazków dla TeXa i LaTeXa.

%package tex-pstricks
Summary:	PostScript macros for TeX
Summary(pl.UTF-8):	Makra postscriptowe dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

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

%package tex-qpx
Summary:	QuasiPalatino and PX fonts typesetting support
Summary(pl.UTF-8):	Wsparcie dla składu fontami QuasiPalatino i PX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-qpx = %{epoch}:%{version}-%{release}

%description tex-qpx
QuasiPalatino and PX fonts typesetting support.

%description tex-qpx -l pl.UTF-8
Wsparcie dla składu fontami QuasiPalatino i PX.

%package tex-qpxqtx
Summary:	QuasiTimes and TX fonts typesetting support
Summary(pl.UTF-8):	Wsparcie dla składu fontami QuasiTimes i TX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-qpxqtx = %{epoch}:%{version}-%{release}

%description tex-qpxqtx
QuasiTimes and TX fonts typesetting support.

%description tex-qpxqtx -l pl.UTF-8
Wsparcie dla składu fontami QuasiTimes i TX.

%package tex-ruhyphen
Summary:	Russian hyphenation
Summary(pl.UTF-8):	Rosyjskie reguły przenoszenia wyrazów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

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
Obsoletes:	tetex-tex-spanishb

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

%package latex-vietnam
Summary:	Vietnamese language support
Summary(pl.UTF-8):	Wsparcie dla języka wietnamskiego
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-vietnam

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

%description tex-xkeyval
Extension to keyval package.

%description tex-xkeyval -l pl.UTF-8
Rozszerzenie do pakietu keyval.

%package dirs-fonts
Summary:	TeX font directories
Summary(pl.UTF-8):	Katalogi fontów TeXa
Group:		Fonts

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

%description fonts-adobe
Adobe fonts.

%description fonts-adobe -l pl.UTF-8
Fonty Adobe.

%package fonts-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Summary(pl.UTF-8):	Wirtualne fonty do plików PDF z fontami CMR o kodowaniu T1
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-ae
Virtual fonts for PDF-files with T1 encoded CMR-fonts.

%description fonts-ae -l pl.UTF-8
Wirtualne fonty do plików PDF z fontami CMR o kodowaniu T1.

%package fonts-ams
Summary:	AMS fonts
Summary(pl.UTF-8):	Fonty AMS
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-ams
AMS fonts.

%description fonts-ams -l pl.UTF-8
Fonty AMS.

%package fonts-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl.UTF-8):	Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

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

%description fonts-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%description fonts-antt -l pl.UTF-8
Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1.

%package fonts-arphic
Summary:	Arphic fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-arphic
Arphic fonts.

%package fonts-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Summary(pl.UTF-8):	Tablicowy wariant fontów Computer Modern ze wsparciem dla LaTeXa
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%description fonts-bbm -l pl.UTF-8
Tablicowy wariant fontów Computer Modern ze wsparciem dla LaTeXa.

%package fonts-bbold
Summary:	Sans serif blackboard bold for LaTeX
Summary(pl.UTF-8):	Tablicowy tłusty font sans serif dla LaTeXa
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-bbold
Sans serif blackboard bold for LaTeX.

%description fonts-bbold -l pl.UTF-8
Tablicowy tłusty font sans serif dla LaTeXa.

%package fonts-bh
Summary:	Bold & Heavy Fonts
Summary(pl.UTF-8):	Fonty Bold i Heavy
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-bh
Bold & Heavy Fonts.

%description fonts-bh -l pl.UTF-8
Fonty Bold i Heavy.

%package fonts-bitstream
Summary:	Bitstream fonts
Summary(pl.UTF-8):	Fonty Bitstream
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-bitstrea

%description fonts-bitstream
Bitstream fonts.

%description fonts-bitstream -l pl.UTF-8
Fonty Bitstream.

%package fonts-cbgreek
Summary:	Complete set of Greek fonts
Summary(pl.UTF-8):	Pełny zestaw fontów greckich
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-cbgreek
Complete set of Greek fonts.

%description fonts-cbgreek -l pl.UTF-8
Pełny zestaw fontów greckich.

%package fonts-cc-pl
Summary:	Polish version of Computer Concrete fonts
Summary(pl.UTF-8):	Polska wersja fontów Computer Concrete
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-cc-pl
Polish version of Computer Concrete fonts.

%description fonts-cc-pl -l pl.UTF-8
Polska wersja fontów Computer Concrete.

%package fonts-cg
Summary:	Compugraphic fonts
Summary(pl.UTF-8):	Fonty Compugraphic
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-cg
Compugraphic fonts.

%description fonts-cg -l pl.UTF-8
Fonty Compugraphic.

%package fonts-cm
Summary:	Computer Modern fonts
Summary(pl.UTF-8):	Fonty Computer Modern
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-cm
Computer Modern fonts.

%description fonts-cm -l pl.UTF-8
Fonty Computer Modern.

%package fonts-cmbright
Summary:	CM Bright fonts
Summary(pl.UTF-8):	Fonty CM Bright
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-cmbright
CM Bright fonts.

%description fonts-cmbright -l pl.UTF-8
Fonty CM Bright.

%package fonts-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Summary(pl.UTF-8):	Fonty Computer Modern rozszerzone o litery rosyjskie
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-cmcyr
Computer Modern fonts extended with Russian letters.

%description fonts-cmcyr -l pl.UTF-8
Fonty Computer Modern rozszerzone o litery rosyjskie.

%package fonts-cmextra
Summary:	Extra Computer Modern fonts, from the American Mathematical Society
Summary(pl.UTF-8):	Dodatkowe fonty Computer Modern z AMS
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-cmextra
Extra Computer Modern fonts, from the American Mathematical Society.

%description fonts-cmextra -l pl.UTF-8
Dodatkowe fonty Computer Modern z AMS (American Mathematical Society).

%package fonts-concmath
Summary:	Concrete Math fonts
Summary(pl.UTF-8):	Fonty matematyczne Concrete Math
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-concmath
Concrete Math fonts.

%description fonts-concmath -l pl.UTF-8
Fonty matematyczne Concrete Math.

%package fonts-concrete
Summary:	Concrete Roman fonts
Summary(pl.UTF-8):	Fonty Concrete Roman
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

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

%description fonts-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%description fonts-cs -l pl.UTF-8
Fonty MetaFont Computer Modern zmodyfikowane pod kątem języków
czeskiego i słowackiego.

%package fonts-dstroke
Summary:	Doublestroke font for typesetting the mathematical symbols
Summary(pl.UTF-8):	Podwójnie kreślony font do składania symboli matematycznych
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-dstroke
Doublestroke font for typesetting the mathematical symbols.

%description fonts-dstroke -l pl.UTF-8
Podwójnie kreślony font do składania symboli matematycznych.

%package fonts-ecc
Summary:	Sources for the European Concrete fonts
Summary(pl.UTF-8):	Źródła dla fontów European Concrete
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

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

%description fonts-gothic
Gothic and ornamental initial fonts by Yannis Haralambous.

%description fonts-gothic -l pl.UTF-8
Początkowe fonty gotyckie i ornamentowe Yannisa Haralambousa.

%package fonts-hoekwater
Summary:	Converted mflogo font
Summary(pl.UTF-8):	Przekonwertowany font mflogo
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

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

%description fonts-jknappen
Miscellaneous macros, mostly for making use of extra fonts, by Joerg
Knappen, including sgmlcmpt.

%description fonts-jknappen -l pl.UTF-8
Różne makra, głównie do używania dodatkowych fontów autorstwa Joerga
Knappena. Zawiera sgmlcmpt.

%package fonts-latex
Summary:	Basic LaTeX fonts
Summary(pl.UTF-8):	Podstawowe fonty dla LaTeXa
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-latex
Basic LaTeX fonts.

%description fonts-latex -l pl.UTF-8
Podstawowe fonty dla LaTeXa.

%package fonts-lh
Summary:	Olga Lapko's LH fonts
Summary(pl.UTF-8):	Fonty LH Olgi Lapko
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-lh
The lh fonts for the `T2'/X2 encodings (for cyrillic languages).

%description fonts-lh -l pl.UTF-8
Fonty lh dla kodowań `T2'/X2 (dla języków zapisywanych cyrylicą).

%package fonts-lm
Summary:	Latin Modern family fonts
Summary(pl.UTF-8):	Fonty z rodziny Latin Modern
Group:		Applications/Publishing/TeX
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

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

%description fonts-mflogo
Logo fonts.

%description fonts-mflogo -l pl.UTF-8
Fonty logo.

%package fonts-misc
Summary:	Miscellaneous fonts
Summary(pl.UTF-8):	Różne fonty
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-misc
Miscellaneous fonts.

%description fonts-misc -l pl.UTF-8
Fonty różne.

%package fonts-monotype
Summary:	Monotype fonts
Summary(pl.UTF-8):	Fonty Monotype
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-monotype
Monotype fonts.

%description fonts-monotype -l pl.UTF-8
Fonty Monotype.

%package fonts-omega
Summary:	Fonts for Omega - extended unicode TeX
Summary(pl.UTF-8):	Fonty dla Omegi - TeXa ze wsparciem dla unikodu
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-omega
Fonts for Omega - extended unicode TeX.

%description fonts-omega -l pl.UTF-8
Fonty dla Omegi - TeXa ze wsparciem dla unikodu.

%package fonts-pazo
Summary:	Pazo fonts
Summary(pl.UTF-8):	Fonty Pazo
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-pazo
Pazo fonts.

%description fonts-pazo -l pl.UTF-8
Fonty Pazo.

%package fonts-pl
Summary:	Polish fonts
Summary(pl.UTF-8):	Polskie fonty
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-pl
Polish fonts.

%description fonts-pl -l pl.UTF-8
Polskie fonty.

%package fonts-px
Summary:	PX fonts
Summary(pl.UTF-8):	Fonty PX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-px
PX fonts.

%description fonts-px -l pl.UTF-8
Fonty PX.

%package fonts-qfonts
Summary:	Quasi fonts
Summary(pl.UTF-8):	Fonty Quasi
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-qfonts
Quasi fonts.

%description fonts-qfonts -l pl.UTF-8
Fonty Quasi.

%package fonts-qpx
Summary:	Additional fonts for QPX package
Summary(pl.UTF-8):	Dodatkowe fonty dla pakietu QPX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-px = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-qfonts = %{epoch}:%{version}-%{release}

%description fonts-qpx
Additional fonts for QPX package.

%description fonts-qpx -l pl.UTF-8
Dodatkowe fonty dla pakietu QPX.

%package fonts-qpxqtx
Summary:	Additional fonts for QTX package
Summary(pl.UTF-8):	Dodatkowe fonty dla pakietu QTX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-qfonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-tx = %{epoch}:%{version}-%{release}

%description fonts-qpxqtx
Additional fonts for QTX package.

%description fonts-qpxqtx -l pl.UTF-8
Dodatkowe fonty dla pakietu QTX.

%package fonts-rsfs
Summary:	Fonts of uppercase script letters for scientific and mathematical typesetting
Summary(pl.UTF-8):	Fonty wielkich liter pisanych do składania dokumentów naukowych i matematycznych
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

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

%description fonts-stmaryrd
St Mary Road symbols for functional programming.

%description fonts-stmaryrd -l pl.UTF-8
Symbole St Mary Road do programowania funkcyjnego.

%package fonts-tx
Summary:	TX fonts
Summary(pl.UTF-8):	Fonty TX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-tx
TX fonts.

%description fonts-tx -l pl.UTF-8
Fonty TX.

%package fonts-uhc
Summary:	UHC fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-uhc
UHC fonts.

%package fonts-urw
Summary:	URW fonts
Summary(pl.UTF-8):	Fonty URW
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-urw
URW fonts.

%description fonts-urw -l pl.UTF-8
Fonty URW.

%package fonts-urwvn
Summary:	URWVN fonts
Summary(pl.UTF-8):	Fonty URWVN
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-urwvn
URWVN fonts.

%description fonts-urwvn -l pl.UTF-8
Fonty URWVN.

%package fonts-vnr
Summary:	VNR fonts
Summary(pl.UTF-8):	Fonty VNR
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-vnr
VNR fonts.

%description fonts-vnr -l pl.UTF-8
Fonty VNR.

%package fonts-wadalab
Summary:	Wadalab fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-wadalab
Wadalab fonts.

%package fonts-wasy
Summary:	Waldis symbol fonts
Summary(pl.UTF-8):	Fonty Waldis symbol
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-wasy
Waldis symbol fonts.

%description fonts-wasy -l pl.UTF-8
Fonty Waldis symbol.

%package fonts-xypic
Summary:	Xy-pic fonts
Summary(pl.UTF-8):	Fonty Xy-pic
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-xypic
Xy-pic fonts.

%description fonts-xypic -l pl.UTF-8
Fonty Xy-pic.

%package fonts-yandy
Summary:	European Modern fonts from Y&Y
Summary(pl.UTF-8):	Fonty European Modern od Y&Y
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-yandy
European Modern fonts from Y&Y.

%description fonts-yandy -l pl.UTF-8
Fonty European Modern od Y&Y.

%package fonts-type1-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl.UTF-8):	Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

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

%description fonts-type1-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%description fonts-type1-antt -l pl.UTF-8
Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1.

%package fonts-type1-arphic
Summary:	Type1 Arphic fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-arphic
Type1 Arphic fonts.

%package fonts-type1-belleek
Summary:	Free replacement for basic MathTime fonts
Summary(pl.UTF-8):	Wolnodostępny zamiennik podstawowych fontów MathTime
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-belleek
Free replacement for basic MathTime fonts.

%description fonts-type1-belleek -l pl.UTF-8
Wolnodostępny zamiennik podstawowych fontów MathTime.

%package fonts-type1-bitstream
Summary:	Bitstream fonts
Summary(pl.UTF-8):	Fonty Bitstream
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-bitstrea

%description fonts-type1-bitstream
Bitstream fonts.

%description fonts-type1-bitstream -l pl.UTF-8
Fonty Bitstream.

%package fonts-type1-bluesky
Summary:	Computer Modern family fonts
Summary(pl.UTF-8):	Fonty z rodziny Computer Modern
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-bluesky
Computer Modern family fonts.

%description fonts-type1-bluesky -l pl.UTF-8
Fonty z rodzony Computer Modern.

%package fonts-type1-cc-pl
Summary:	Polish version of Computer Concrete fonts
Summary(pl.UTF-8):	Polska wersja fontów Computer Concrete
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-cc-pl
Polish version of Computer Concrete fonts.

%description fonts-type1-cc-pl -l pl.UTF-8
Polska wersja fontów Computer Concrete.

%package fonts-type1-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Summary(pl.UTF-8):	Fonty Computer Modern rozszerzone o litery rosyjskie
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-cmcyr
Computer Modern fonts extended with Russian letters.

%description fonts-type1-cmcyr -l pl.UTF-8
Fonty Computer Modern rozszerzone o litery rosyjskie.

%package fonts-type1-cs
Summary:	Czech/Slovak-tuned MetaFont Computer Modern fonts
Summary(pl.UTF-8):	Fonty MetaFont Computer Modern dla języków czeskiego i słowackiego
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%description fonts-type1-cs -l pl.UTF-8
Fonty MetaFont Computer Modern zmodyfikowane pod kątem języków
czeskiego i słowackiego.

%package fonts-type1-dstroke
Summary:	Doublestroke Type1 font for typesetting the mathematical symbols
Summary(pl.UTF-8):	Podwójnie kreślony font Type1 do składania symboli matematycznych
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-dstroke
Doublestroke Type1 font for typesetting the mathematical symbols.

%description fonts-type1-dstroke -l pl.UTF-8
Podwójnie kreślony font Type1 do składania symboli matematycznych.

%package fonts-type1-eurosym
Summary:	The new European currency symbol for the Euro
Summary(pl.UTF-8):	Symbol nowej europejskiej waluty Euro
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-eurosym
The new European currency symbol for the Euro implemented in Metafont,
using the official European Commission dimensions, and providing
several shapes (normal, slanted, bold, outline).

%description fonts-type1-eurosym -l pl.UTF-8
Symbol nowej europejskiej waluty Euro, zaimplementowany w Metafoncie,
z użyciem oficjalnych wymiarów wg Komisji Europejskiej, dostarczający
różnych kształtów (normalnego, pochylonego, tłustego, szkicowanego).

%package fonts-type1-hoekwater
Summary:	Converted mflogo font
Summary(pl.UTF-8):	Przekonwertowany font mflogo
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-hoekwater
Fonts originally created in MetaFont, transformed to PostScript by
Taco Hoekwater; includes logo, manfnt, rsfs, stmaryrd, wasy, wasy2,
xipa.

%description fonts-type1-hoekwater -l pl.UTF-8
Fonty oryginalnie stworzone w MetaFoncie, przekształcone do
PostScriptu przez Taco Hoekwatera; zawierają: logo, manfnt, rsfs,
stmaryrd, wasy, wasy2, xipa.

%package fonts-type1-fpl
Summary:	SC/OsF fonts for URW Palladio L
Summary(pl.UTF-8):	Fonty SC/OsF dla URW Palladio L
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

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

%package fonts-type1-tt2001
Summary:	Type1 tt2001 family fonts
Summary(pl.UTF-8):	Fonty Type1 z rodziny tt2001
Group:		Applications/Publishing/TeX
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-tt2001
Type1 tt2001 famliy fonts.

%description fonts-type1-tt2001 -l pl.UTF-8
Fonty Type1 z rodziny tt2001.

%package fonts-type1-lm
Summary:	Type1 Latin Modern family fonts
Summary(pl.UTF-8):	Fonty Type1 z rodziny Latin Modern
Group:		Applications/Publishing/TeX
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

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

%description fonts-type1-mathpazo
Pazo Math fonts.

%description fonts-type1-mathpazo -l pl.UTF-8
Fonty matematyczne Pazo Math.

%package fonts-type1-omega
Summary:	Type1 fonts for Omega - extended unicode TeX
Summary(pl.UTF-8):	Fonty Type1 dla Omegi - TeXa ze wsparciem dla unikodu
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

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

%description fonts-type1-pl
Polish fonts.

%description fonts-type1-pl -l pl.UTF-8
Polskie fonty.

%package fonts-type1-px
Summary:	PX fonts
Summary(pl.UTF-8):	Fonty PX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-px
PX fonts.

%description fonts-type1-px -l pl.UTF-8
Fonty PX.

%package fonts-type1-qfonts
Summary:	Quasi fonts
Summary(pl.UTF-8):	Fonty Quasi
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-qfonts
Quasi fonts.

%description fonts-type1-qfonts -l pl.UTF-8
Fonty Quasi.

%package fonts-type1-tx
Summary:	TX fonts
Summary(pl.UTF-8):	Fonty TX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-tx
TX fonts.

%description fonts-type1-tx -l pl.UTF-8
Fonty TX.

%package fonts-type1-uhc
Summary:	Type1 UHC fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-uhc
Type1 UHC fonts.

%package fonts-type1-urw
Summary:	URW fonts
Summary(pl.UTF-8):	Fonty URW
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-urw
URW fonts.

%description fonts-type1-urw -l pl.UTF-8
Fonty URW.

%package fonts-type1-vnr
Summary:	Type1 VNR fonts
Summary(pl.UTF-8):	Fonty Type1 VNR
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-vnr
Type1 VNR fonts.

%description fonts-type1-vnr -l pl.UTF-8
Fonty Type1 VNR.

%package fonts-type1-wadalab
Summary:	Type1 Wadalab fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-wadalab
Type1 Wadalab fonts.

%package fonts-type1-xypic
Summary:	Xy-pic fonts
Summary(pl.UTF-8):	Fonty Xy-pic
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-xypic
Xy-pic fonts.

%description fonts-type1-xypic -l pl.UTF-8
Fonty Xy-pic.


# TeXLive-specific packages - there wasn't before...
%package afm2pl
Summary:	Convert an Adobe font metric file to a TeX font property list
Group:		Fonts

%description afm2pl
Convert an Adobe font metric file to a TeX font property list.


%package bbox
Summary:	bbox prints the bounding box of images
Group:		Applications/Publishing/TeX

%description bbox
bbox reads a rawppm or rawpbm file and prints out the bounding box of
the image.

%package cefutils
Summary:	In cefutils there are CEF-compatible utils
Group:		Applications/Publishing/TeX

%description cefutils
In cefutils there are CEF-compatible (Chinese Encoding Framework)
utils.

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

%description dviutils
This package contains various DVI utils.

%description dviutils -l hu.UTF-8
Ez a csomag mindenféle DVI eszközt tartalmaz.

%package epsutils
Summary:	Various EPS utils
Group:		Applications/Publishing/TeX

%description epsutils
Various EPS (Encapsulated PostScript) utils.


%package filters
Summary:	Various filters
Group:		Applications/Publishing/TeX

%description filters
Various filters.


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
Requires:	%{name}-fonts-misc = %{epoch}:%{version}-%{release}

%description xetex
XeTeX extends the TeX typesetting system (and macro packages such as
LaTeX and ConTeXt) to have native support for the Unicode character
set, including complex Asian scripts, and for OpenType and TrueType
fonts.

%package xmltex
Summary:	TeX package for processing XML files
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description xmltex
XMLTeX is a non-validating, namespace-aware XML parser written in TeX.
It allows TeX to directly process XML files.

%prep
%setup -q -c -T -n %{name}-%{version}-source
lzma -dc %{SOURCE0} | tar xf - -C ..
%patch0 -p1
%patch1 -p1

cd libs/teckit
cat ax*.m4 > acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%build
find . -name "config.sub" -exec cp /usr/share/automake/config.sub '{}' ';'
%{__sed} -i 's@"extend/\(.*\)"@<\1>@' texk/ttf2pk/*.c
cd texk/kpathsea
%{__sed} -i 's@^TEXMFMAIN =.*@TEXMFMAIN = %{texmf}@' texmf.cnf
%{__sed} -i 's@^TEXMFDIST =.*@TEXMFDIST = %{texmfdist}@' texmf.cnf
%{__sed} -i 's@^TEXMFLOCAL =.*@TEXMFLOCAL = %{texmf}@' texmf.cnf
%{__sed} -i 's@^TEXMFSYSVAR =.*@TEXMFSYSVAR = %{_localstatedir}@' texmf.cnf
%{__sed} -i 's@^TEXMFSYSCONFIG =.*@TEXMFSYSCONFIG = %{_sysconfdir}/%{name}@' texmf.cnf
%{__sed} -i 's@^TEXMFVAR =.*@TEXMFVAR = %{_localstatedir}@' texmf.cnf
cd ../..

%configure \
%if %{with bootstrap}
	--without-xindy \
	--without-luatex \
%endif
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
	$RPM_BUILD_ROOT%{fmtdir}

lzma -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_datadir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf/texmf $RPM_BUILD_ROOT%{texmf}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf/texmf-dist $RPM_BUILD_ROOT%{texmfdist}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf/texmf-doc $RPM_BUILD_ROOT%{texmfdoc}
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

# install -d $RPM_BUILD_ROOT%{texmf} $RPM_BUILD_ROOT%{texmfdist} $RPM_BUILD_ROOT%{texmfdoc}
# %{__cp} -a texlive-20080822-texmf/texmf/* $RPM_BUILD_ROOT%{texmf}
# %{__cp} -a texlive-20080822-texmf/texmf-dist/* $RPM_BUILD_ROOT%{texmfdist}
# %{__cp} -a texlive-20080822-texmf/texmf-doc/* $RPM_BUILD_ROOT%{texmfdoc}

install -d $RPM_BUILD_ROOT%{texmf}/fonts/opentype/public

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}; export LD_LIBRARY_PATH

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

# Fix broken symlinks
# CURDIR=$(pwd)
# cd $RPM_BUILD_ROOT%{_bindir}
# for file in $(file * | grep broken | awk -F ":" {'print $1'}); do
# ln -sf $(readlink $file | %{__sed} "s@\.\.@%{_datadir}@") $file
# done
# cd $CURDIR

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

perl -pi \
	-e "s|$RPM_BUILD_ROOT||g;" \
	$RPM_BUILD_ROOT%{texmf}/web2c/texmf.cnf

install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.daily/texlive

install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE6} $RPM_BUILD_ROOT%{_pixmapsdir}

# bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# in separate spec
# rm -rf $RPM_BUILD_ROOT%{texmf}/tex/latex/{pgf,xcolor}
# rm -rf $RPM_BUILD_ROOT%{texmf}/doc/latex/{pgf,xcolor}

# not included in package
rm -f $RPM_BUILD_ROOT%{texmf}/doc/fonts/oldgerman/COPYING
rm -f $RPM_BUILD_ROOT%{texmf}/doc/Makefile
rm -f $RPM_BUILD_ROOT%{texmf}/doc/programs/texinfo.*
rm -f $RPM_BUILD_ROOT%{texmf}/doc/helpfile
rm -f $RPM_BUILD_ROOT%{texmf}/doc/helpindex.html
rm -f $RPM_BUILD_ROOT%{texmf}/fonts/pk/ljfour/lh/lh-lcy/*.600pk
rm -f $RPM_BUILD_ROOT%{texmf}/release-tetex-{src,texmf}.txt
rm -f $RPM_BUILD_ROOT%{texmf}/scripts/uniqleaf/uniqleaf.pl
rm -f $RPM_BUILD_ROOT%{texmf}/doc/help/Catalogue-upd.sh
rm -f $RPM_BUILD_ROOT%{texmf}/doc/help/faq/uktug-faq-upd.sh
rm -f $RPM_BUILD_ROOT%{texmf}/doc/mkhtml*
rm -f $RPM_BUILD_ROOT%{texmf}/doc/index.html
rm -f $RPM_BUILD_ROOT%{texmf}/doc/index.php
rm -f $RPM_BUILD_ROOT%{_infodir}/dir.gz
rm -f $RPM_BUILD_ROOT%{_mandir}/{README.*,hu/man1/readlink.1*}
rm -f $RPM_BUILD_ROOT%{_datadir}/texinfo/html/texi2html.html

# move format logs to BUILD, so $RPM_BUILD_ROOT is not polluted
# and we can still analyze them
# install -d format-logs
# mv -fv $RPM_BUILD_ROOT%{fmtdir}/*.log format-logs

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

%post doc-Catalogue
%texhash

%postun doc-Catalogue
%texhash

%post doc-tug-faq
%texhash

%postun doc-tug-faq
%texhash

%post -n kpathsea
/sbin/ldconfig
%fixinfodir
%texhash

%postun -n kpathsea
/sbin/ldconfig
%fixinfodir
%texhash

%post -n kpathsea-devel
%texhash

%postun -n kpathsea-devel
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

%post metafont
%texhash

%postun metafont
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

%post omega
%texhash

%postun omega
%texhash

%post plain
%texhash

%postun plain
%texhash

%post format-plain
%texhash

%postun format-plain
%texhash

%post format-pdftex
%texhash

%postun format-pdftex
%texhash

%post format-pdfetex
%texhash

%postun format-pdfetex
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

%post format-pdfamstex
%texhash

%postun format-pdfamstex
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

%post cyrplain
%texhash

%postun cyrplain
%texhash

%post format-cyrplain
%texhash

%postun format-cyrplain
%texhash

%post format-cyramstex
%texhash

%postun format-cyramstex
%texhash

%post format-cyrtexinfo
%texhash

%postun format-cyrtexinfo
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

# LaTeX format.

%post latex
%fixinfodir
%texhash

%postun latex
%fixinfodir
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

%post latex-backgammon
%texhash

%postun latex-backgammon
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

# %post latex-dstroke
# %texhash

# %postun latex-dstroke
# %texhash

%post latex-enumitem
%texhash

%postun latex-enumitem
%texhash

%post latex-exam
%texhash

%postun latex-exam
%texhash

%post latex-gbrief
%texhash

%postun latex-gbrief
%texhash

%post latex-jknappen
%texhash

%postun latex-jknappen
%texhash

%post latex-leftidx
%texhash

%postun latex-leftidx
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

%post latex-mathpple
%texhash

%postun latex-mathpple
%texhash

%post latex-mathtime
%texhash

%postun latex-mathtime
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

%post latex-palatcm
%texhash

%postun latex-palatcm
%texhash

%post latex-pgf
%texhash

%postun latex-pgf
%texhash

%post latex-psnfss
%texhash

%postun latex-psnfss
%texhash

%post latex-pxfonts
%texhash

%postun latex-pxfonts
%texhash

%post latex-qfonts
%texhash

%postun latex-qfonts
%texhash

%post latex-SIstyle
%texhash

%postun latex-SIstyle
%texhash

%post latex-SIunits
%texhash

%postun latex-SIunits
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

%post latex-wasysym
%texhash

%postun latex-wasysym
%texhash

%post latex-xcolor
%texhash

%postun latex-xcolor
%texhash

%post format-latex
%texhash

%postun format-latex
%texhash

%post format-pdflatex
%texhash

%postun format-pdflatex
%texhash

%post platex
%texhash

%postun platex
%texhash

%post format-platex
%texhash

%postun format-platex
%texhash

%post format-pdfplatex
%texhash

%postun format-pdfplatex
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

%post tex-pstricks
%texhash

%postun tex-pstricks
%texhash

%post tex-qpx
%texhash

%postun tex-qpx
%texhash

%post tex-qpxqtx
%texhash

%postun tex-qpxqtx
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

%post tex-xypic
%texhash

%postun tex-xypic
%texhash

%post fonts-adobe
%texhash

%postun fonts-adobe
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

%post fonts-bh
%texhash

%postun fonts-bh
%texhash

%post fonts-bitstream
%texhash

%postun fonts-bitstream
%texhash

%post fonts-cbgreek
%texhash

%postun fonts-cbgreek
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

%post fonts-dstroke
%texhash

%postun fonts-dstroke
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

%post fonts-pazo
%texhash

%postun fonts-pazo
%texhash

%post fonts-pl
%texhash

%postun fonts-pl
%texhash

%post fonts-px
%texhash

%postun fonts-px
%texhash

%post fonts-qfonts
%texhash

%postun fonts-qfonts
%texhash

%post fonts-qpx
%texhash

%postun fonts-qpx
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

%post fonts-type1-dstroke
%texhash

%postun fonts-type1-dstroke
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

%post fonts-type1-qfonts
%texhash

%postun fonts-type1-qfonts
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

# Check the commented lines!!!

%files
%defattr(644,root,root,755)
# %doc %{texmf}/LICENSE.texmf
# %doc %{texmf}/ChangeLog
# %doc %{texmf}/doc/README.knuth
# There isn't doc/fonts directory
# %dir %{texmf}/doc/fonts
# %doc %{texmf}/doc/fonts/fontname
# %dir %{texmf}/doc/fonts/polish
# %dir %{texmf}/doc/help
# %doc %{texmf}/doc/help/csname.txt
# %doc %{texmf}/doc/help/ctan
# %doc %{texmf}/doc/help/tds.dvi
# %doc %{texmf}/doc/help/unixtex.ftp
# %dir %{texmf}/doc/help/faq
# %doc %{texmf}/doc/images
# %dir %{texmf}/doc/polish
# %doc %{texmf}/doc/polish/*.html
# %dir %{texmf}/doc/programs
# %doc %{texmf}/doc/programs/web2c*
# %doc %{texmf}/doc/programs/cwebman.dvi
# %doc %{texmf}/doc/programs/dvipng.*
# %doc %{texmf}/doc/knuth
#%attr(755,root,root) %{_bindir}/MakeTeXPK
#%attr(755,root,root) %{_bindir}/access

# ***********
# executables
# ***********
%attr(755,root,root) %{_bindir}/a2ping
%attr(755,root,root) %{_bindir}/afm2tfm
%attr(755,root,root) %{_bindir}/allcm
%attr(755,root,root) %{_bindir}/allec
%attr(755,root,root) %{_bindir}/allneeded
%attr(755,root,root) %{_bindir}/cweave
%attr(755,root,root) %{_bindir}/ctangle
%attr(755,root,root) %{_bindir}/ctie
%attr(755,root,root) %{_bindir}/dmp
%attr(755,root,root) %{_bindir}/dvipng
%attr(755,root,root) %{_bindir}/e2pall
%attr(755,root,root) %{_bindir}/ebb
# %attr(755,root,root) %{_bindir}/fdf2tan
%attr(755,root,root) %{_bindir}/fmtutil
%attr(755,root,root) %{_bindir}/fmtutil-sys
#%attr(755,root,root) %{_bindir}/fontexport
#%attr(755,root,root) %{_bindir}/fontimport
%attr(755,root,root) %{_bindir}/fontinst
%attr(755,root,root) %{_bindir}/gftodvi
%attr(755,root,root) %{_bindir}/gftopk
%attr(755,root,root) %{_bindir}/gftype
%attr(755,root,root) %{_bindir}/gsftopk
#%attr(755,root,root) %{_bindir}/initex
%attr(755,root,root) %{_bindir}/kpseaccess
%attr(755,root,root) %{_bindir}/kpsereadlink
%attr(755,root,root) %{_bindir}/kpsewhere
%attr(755,root,root) %{_bindir}/mag
%attr(755,root,root) %{_bindir}/makempx
#%attr(755,root,root) %{_bindir}/mkfontdesc
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
# TODO: move this file to correct subpackage ?
%attr(755,root,root) %{_bindir}/ps4pdf
#%attr(755,root,root) %{_bindir}/t1mapper
%attr(755,root,root) %{_bindir}/tangle
#%attr(755,root,root) %{_bindir}/tetex-updmap
%attr(755,root,root) %{_bindir}/tex
%attr(755,root,root) %{_bindir}/texdoc
%attr(755,root,root) %{_bindir}/texhash
# %attr(755,root,root) %{_bindir}/texi2html
%attr(755,root,root) %{_bindir}/texlinks
%attr(755,root,root) %{_bindir}/tftopl
%attr(755,root,root) %{_bindir}/tie
%attr(755,root,root) %{_bindir}/ttf2afm
%attr(755,root,root) %{_bindir}/updmap
%attr(755,root,root) %{_bindir}/updmap-sys
%attr(755,root,root) %{_bindir}/vftovp
#%attr(755,root,root) %{_bindir}/virtex
%attr(755,root,root) %{_bindir}/vptovf
%attr(755,root,root) %{_bindir}/weave

%attr(755,root,root) %{texmf}/web2c/mktexnam
%attr(755,root,root) %{texmf}/web2c/mktexdir
%attr(755,root,root) %{texmf}/web2c/mktexupd

%attr(750,root,root) /etc/cron.daily/texlive

#%dir /etc/sysconfig/tetex-updmap
#%verify(not md5 mtime size) %config(noreplace) /etc/sysconfig/tetex-updmap/maps.lst

%ghost %{texmf}/ls-R
%ghost %{texmfdist}/ls-R
# %ghost %{_localstatedir}/ls-R

%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/cslatex/base/fonttext.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.dat
%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/latex/base/fontmath.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/latex/base/fonttext.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/latex/base/preload.cfg

%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/fmtutil.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktex.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktex.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktexdir.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktexnam.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/texmf.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/updmap.cfg

%attr(1777,root,root) /var/cache/fonts

%{_datadir}/info/web2c.info*
# %{_datadir}/info/texi2html.info*
# %{_datadir}/texi2html
#%{texmf}/updates.dat

# %{texmf}/aliases
# %{texmf}/tex/generic/bghyph
# %doc %{texmf}/doc/generic/hyphen
#%{texmf}/tex/generic/letterspacing

# ***********
# Directories
# ***********
%attr(1777,root,root) %dir %{_localstatedir}
%attr(1777,root,root) %dir %{_localstatedir}/fonts
%attr(1777,root,root) %dir %{_localstatedir}/fonts/map
%attr(1777,root,root) %dir %{fmtdir}

%dir %{texmfdist}
%doc %{texmfdist}/README
%dir %{texmf}

%dir %{texmfdist}/doc
%dir %{texmfdist}/doc/generic
%dir %{texmfdist}/doc/generic/enctex
%dir %{texmfdist}/doc/latex
%dir %{texmfdist}/doc/latex/localloc
%dir %{texmf}/doc
%dir %{texmf}/doc/generic
%dir %{texmf}/doc/tetex

%dir %{texmfdist}/tex
%dir %{texmfdist}/tex/cslatex
%dir %{texmfdist}/tex/cslatex/base
%dir %{texmfdist}/tex/generic
%dir %{texmfdist}/tex/generic/dehyph-exptl
%dir %{texmfdist}/tex/generic/enctex
%dir %{texmfdist}/tex/generic/genmisc
%dir %{texmfdist}/tex/generic/hyph-utf8
%dir %{texmfdist}/tex/generic/misc
%dir %{texmfdist}/tex/latex
%dir %{texmfdist}/tex/latex/base
%dir %{texmf}/dvips
%dir %{texmf}/dvips/config
%dir %{texmf}/dvips/tetex
%dir %{texmf}/fonts/enc
%dir %{texmf}/fonts/enc/dvips
%dir %{texmf}/fonts/enc/dvips/tetex
%dir %{texmf}/fonts/map/dvips/updmap
%dir %{texmf}/fonts/map
%dir %{texmf}/fonts/map/dvips
%dir %{texmf}/fonts/map/dvips/tetex
%dir %{texmf}/scripts
%dir %{texmf}/tex
%dir %{texmf}/tex/generic
%dir %{texmf}/tex/generic/config
%dir %{texmf}/web2c

# Docs
# %doc %{texmf}/doc/README
%doc %{texmf}/doc/tetex/TETEXDOC.*
%doc %{texmf}/doc/tetex/teTeX-FAQ

# %{texmf}/fonts/map/dvips/tetex/contnav.map
# %{texmf}/fonts/map/dvips/tetex/lumath-o.map
%{texmfdist}/fonts/map/dvips/vntex/urwvn.map
%{texmfdist}/fonts/enc/dvips/vntex/t5.enc

# Main fonts from TeTeX
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

%{texmfdist}/tex/generic/dehyph-exptl/*
%{texmfdist}/tex/generic/encodings
%{texmfdist}/tex/generic/epsf
%{texmfdist}/tex/generic/hyph-utf8/*
%{texmfdist}/tex/generic/genmisc/random.tex
%{texmfdist}/tex/generic/misc/null*
%{texmfdist}/tex/generic/misc/texnames.sty
%{texmfdist}/tex/generic/tap
%{texmfdist}/tex/generic/tex-ps
%{texmfdist}/tex/texinfo
%{texmf}/tex/fontinst
%{texmf}/tex/generic/hyphen

# %{fmtdir}/metafun.mem
#%{texmf}/web2c/tex-pl.pool
# %{texmf}/web2c/tex.pool
%{texmf}/fonts/map/dvips/updmap/*

%{texmf}/web2c/*.tcx

# %lang(fi) %{_mandir}/fi/man1/afm2tfm.1*
# %lang(fi) %{_mandir}/fi/man1/allcm.1*
# %lang(fi) %{_mandir}/fi/man1/allneeded.1*
# %lang(fr) %{_mandir}/fr/man1/access.1*
# %lang(hu) %{_mandir}/hu/man1/access.1*
# %lang(hu) %{_mandir}/hu/man1/newer.1*
# %lang(pl) %{_mandir}/pl/man1/access.1*
# %lang(pl) %{_mandir}/pl/man1/newer.1*
#%{_mandir}/man1/MakeTeXPK.1*
#%{_mandir}/man1/access.1*
#%{_mandir}/man1/fontexport.1*
#%{_mandir}/man1/fontimport.1*
#%{_mandir}/man1/initex.1*
#%{_mandir}/man1/t1mapper.1*
#%{_mandir}/man1/texdoc.1*
#%{_mandir}/man1/texi2html.1*
#%{_mandir}/man1/virtex.1*
#%{_mandir}/man8/fmtutil.8*
#%{_mandir}/man8/mkfontdesc.8*
#%{_mandir}/man8/texlinks.8*

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
%{_mandir}/man1/e2pall.1*
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


%files dirs-fonts
%defattr(644,root,root,755)
%dir %{texmfdist}/doc/latex/marvosym/mac/oztex/tex-font
%dir %{texmfdist}/fonts
%dir %{texmfdist}/fonts/afm
%dir %{texmfdist}/fonts/afm/public
%dir %{texmfdist}/fonts/afm/vntex
%dir %{texmfdist}/fonts/enc
%dir %{texmfdist}/fonts/enc/dvips
%dir %{texmfdist}/fonts/enc/dvips/vntex
%dir %{texmfdist}/fonts/map
%dir %{texmfdist}/fonts/map/dvipdfm
%dir %{texmfdist}/fonts/map/dvips
%dir %{texmfdist}/fonts/map/dvips/vntex
%dir %{texmfdist}/fonts/map/fontname
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
%dir %{texmfdist}/fonts/type1
%dir %{texmfdist}/fonts/type1/public
%dir %{texmfdist}/fonts/type1/vntex
%dir %{texmfdist}/fonts/vf
%dir %{texmfdist}/fonts/vf/public
%dir %{texmfdist}/fonts/vf/vntex
%dir %{texmfdist}/source
%dir %{texmfdist}/source/fonts
%dir %{texmfdist}/source/latex
%dir %{texmf}/fonts
%dir %{texmf}/fonts/opentype
%dir %{texmf}/fonts/opentype/public

%files doc
%defattr(644,root,root,755)
%{texmfdoc}/doc/english

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

# %files doc-Catalogue
# %defattr(644,root,root,755)
# %{texmf}/doc/help/Catalogue

# %files doc-tug-faq
# %defattr(644,root,root,755)
# %{texmf}/doc/help/faq/uktug-faq


%files doc-latex
%defattr(644,root,root,755)
# %{texmfdist}/doc/latex/bar
# %{texmfdist}/doc/latex/eclbip
# %{texmfdist}/doc/latex/eo
# %{texmfdist}/doc/latex/floatflt
# %{texmfdist}/doc/latex/general
# %{texmfdist}/doc/latex/germbib
# %{texmfdist}/doc/latex/images
# %{texmfdist}/doc/latex/mathcomp
# %{texmfdist}/doc/latex/mt11p
# %{texmfdist}/doc/latex/picins
# %{texmfdist}/doc/latex/ps4pdf
# %{texmfdist}/doc/latex/pslatex
# %{texmfdist}/doc/latex/shapepar
# %{texmfdist}/doc/latex/supertab
# %{texmfdist}/doc/latex/tex-refs
# %{texmfdist}/doc/latex/textmerg
# %{texmfdist}/doc/latex/treesvr
%{texmfdist}/doc/latex/acronym
%{texmfdist}/doc/latex/aeguill
%{texmfdist}/doc/latex/anysize
%{texmfdist}/doc/latex/base
%{texmfdist}/doc/latex/beton
%{texmfdist}/doc/latex/carlisle
%{texmfdist}/doc/latex/ccaption
%{texmfdist}/doc/latex/changebar
%{texmfdist}/doc/latex/chappg
%{texmfdist}/doc/latex/concmath
%{texmfdist}/doc/latex/crop
%{texmfdist}/doc/latex/dinbrief
%{texmfdist}/doc/latex/draftcopy
%{texmfdist}/doc/latex/eepic
%{texmfdist}/doc/latex/endfloat
%{texmfdist}/doc/latex/esint
%{texmfdist}/doc/latex/eso-pic
%{texmfdist}/doc/latex/euler
%{texmfdist}/doc/latex/eulervm
%{texmfdist}/doc/latex/extsizes
%{texmfdist}/doc/latex/fancybox
%{texmfdist}/doc/latex/fancyhdr
%{texmfdist}/doc/latex/fancyvrb
%{texmfdist}/doc/latex/filecontents
%{texmfdist}/doc/latex/float
%{texmfdist}/doc/latex/footmisc
%{texmfdist}/doc/latex/footnpag
%{texmfdist}/doc/latex/fp
%{texmfdist}/doc/latex/geometry
%{texmfdist}/doc/latex/graphics
%{texmfdist}/doc/latex/hyperref
%{texmfdist}/doc/latex/hyphenat
%{texmfdist}/doc/latex/index
%{texmfdist}/doc/latex/koma-script
%{texmfdist}/doc/latex/labels
%{texmfdist}/doc/latex/layouts
%{texmfdist}/doc/latex/lettrine
%{texmfdist}/doc/latex/listings
%{texmfdist}/doc/latex/ltabptch
%{texmfdist}/doc/latex/mdwtools
%{texmfdist}/doc/latex/memoir
%{texmfdist}/doc/latex/mh
%{texmfdist}/doc/latex/mparhack
%{texmfdist}/doc/latex/ms
%{texmfdist}/doc/latex/multibib
%{texmfdist}/doc/latex/mwcls
%{texmfdist}/doc/latex/natbib
%{texmfdist}/doc/latex/nomencl
%{texmfdist}/doc/latex/ntgclass
%{texmfdist}/doc/latex/oberdiek
%{texmfdist}/doc/latex/overpic
%{texmfdist}/doc/latex/paralist
%{texmfdist}/doc/latex/pb-diagram
%{texmfdist}/doc/latex/pdfpages
%{texmfdist}/doc/latex/picinpar
%{texmfdist}/doc/latex/pict2e
%{texmfdist}/doc/latex/placeins
%{texmfdist}/doc/latex/preprint
%{texmfdist}/doc/latex/preview
%{texmfdist}/doc/latex/program
%{texmfdist}/doc/latex/psfrag
%{texmfdist}/doc/latex/revtex
%{texmfdist}/doc/latex/rotating
%{texmfdist}/doc/latex/rotfloat
%{texmfdist}/doc/latex/scale
%{texmfdist}/doc/latex/sectsty
%{texmfdist}/doc/latex/seminar
%{texmfdist}/doc/latex/showlabels
%{texmfdist}/doc/latex/sidecap
%{texmfdist}/doc/latex/slashbox
%{texmfdist}/doc/latex/soul
%{texmfdist}/doc/latex/stdclsdv
%{texmfdist}/doc/latex/subfig
%{texmfdist}/doc/latex/subfigure
%{texmfdist}/doc/latex/textfit
%{texmfdist}/doc/latex/textpos
%{texmfdist}/doc/latex/titlesec
%{texmfdist}/doc/latex/tocbibind
%{texmfdist}/doc/latex/tocloft
%{texmfdist}/doc/latex/tools
%{texmfdist}/doc/latex/totpages
%{texmfdist}/doc/latex/type1cm
%{texmfdist}/doc/latex/units
%{texmfdist}/doc/latex/vmargin
%{texmfdist}/doc/latex/was
%{texmfdist}/doc/latex/wrapfig
%{texmfdist}/doc/latex/xtab
%{texmfdist}/doc/latex/yfonts

%files -n kpathsea
%defattr(644,root,root,755)
%dir %{texmf}/doc/kpathsea
%doc %{texmf}/doc/kpathsea/kpathsea.pdf
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
# %doc %{texmf}/doc/programs/dvips.dvi
# %doc %{texmf}/doc/programs/dvipdfm.dvi
# %doc %{texmf}/doc/latex/psnfssx
# %lang(fi) %{_mandir}/fi/man1/dvips.1*
# %{texmf}/dvips/misc
# %{texmf}/dvips/config/config.generic
# %{texmf}/fonts/map/dvips/misc
# %{texmf}/fonts/map/dvips/tetex/bsr-interpolated.map
# %{texmf}/fonts/map/dvips/tetex/bsr.map
# %{_localstatedir}/fonts/map/dvipdfm
# %{_localstatedir}/fonts/map/dvips
%dir %{texmfdist}/fonts/map/dvips/cmex
%dir %{texmf}/dvipdfm
%docdir %{texmf}/doc/dvips
%docdir %{texmf}/doc/dvipdfm
%attr(755,root,root) %{_bindir}/dvips
%attr(755,root,root) %{_bindir}/dvired
%attr(755,root,root) %{_bindir}/dvitomp
%attr(755,root,root) %{_bindir}/dvitype
%attr(755,root,root) %{_bindir}/dvicopy
%attr(755,root,root) %{_bindir}/dvipdfm
%attr(755,root,root) %{_bindir}/dvipdft
# dvi2fax requires ghostscript
%attr(755,root,root) %{_bindir}/dvi2fax
%{_infodir}/dvips.info*
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvicopy.1*
%{_mandir}/man1/dvipdfm.1*
%{_mandir}/man1/dvips.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/dvitype.1*
%{texmf}/dvips/base
%{texmf}/dvips/gsftopk
%{texmfdist}/dvips/psfrag
%config(noreplace) %verify(not md5 mtime size) %{texmf}/dvips/config/config.ps
%{texmfdist}/fonts/enc/dvips/base
%{texmfdist}/fonts/map/dvips/allrunes
%{texmfdist}/fonts/map/dvips/cmex/ttcmex.map
%{texmf}/dvipdfm/config
%{texmf}/dvips/tetex/config.*
%{texmf}/fonts/enc/dvips/tetex/mtex.enc
# %{texmf}/fonts/map
%dir %{texmf}/fonts/map/dvipdfm
%dir %{texmf}/fonts/map/dvips
%dir %{texmf}/fonts/map/dvips/tetex
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
%attr(755,root,root) %{_bindir}/mkindex
%attr(755,root,root) %{_bindir}/makeindex
%attr(755,root,root) %{_bindir}/rumakeindex
%{texmfdist}/makeindex
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/mkindex.1*
%{_mandir}/man1/rumakeindex.1*

%files metafont
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/mfw
#%attr(755,root,root) %{_bindir}/virmf
#%attr(755,root,root) %{_bindir}/inimf
#%{texmf}/mft/cmbase.mft
# %{texmf}/mft/e.mft
# %{texmf}/mft/pl.mft
# %{fmtdir}/mf.base
#%{texmf}/web2c/mf-nowin.base
# %{texmf}/web2c/mf.pool
#%{texmf}/web2c/mfw.base
#%{_mandir}/man1/inimf.1*
#%{_mandir}/man1/virmf.1*
%dir %{texmfdist}/mft
%dir %{texmfdist}/mft/base
%attr(755,root,root) %{_bindir}/mf
%attr(755,root,root) %{_bindir}/mf-nowin
%attr(755,root,root) %{_bindir}/mft
%attr(755,root,root) %{_bindir}/mktexmf
%attr(755,root,root) %{_bindir}/mktexpk
%attr(755,root,root) %{_bindir}/mktextfm
%{texmfdist}/metafont
%{texmfdist}/mft/base/mplain.mft
%{texmfdist}/mft/base/plain.mft
%{_mandir}/man1/mf.1*
%{_mandir}/man1/mf-nowin.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*

%files metapost
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/virmpost
#%attr(755,root,root) %{_bindir}/inimpost
# %{texmf}/web2c/mp.pool
# %{fmtdir}/mpost.mem
#%{_mandir}/man1/inimpost.1*
#%{_mandir}/man1/virmpost.1*
%dir %{texmfdist}/metapost
%doc %{texmfdist}/doc/metapost
%attr(755,root,root) %{_bindir}/mpost
%attr(755,root,root) %{_bindir}/mpto
%{texmfdist}/metapost/base
%{texmfdist}/metapost/config
%{texmfdist}/metapost/mfpic
%{texmfdist}/metapost/misc
%{texmfdist}/metapost/support
%{_mandir}/man1/mpost.1*
%{_mandir}/man1/mpto.1*

%files mptopdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mptopdf
%{_mandir}/man1/mptopdf.1*
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/mptopdf.fmt

%files texdoctk
%defattr(644,root,root,755)
# %doc %{texmf}/doc/texdoctk
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

%files -n xindy
%defattr(644,root,root,755)
%doc %{texmf}/doc/xindy
%dir %{texmf}/xindy
%dir %{texmf}/xindy/lang
%{texmf}/xindy/base
%{texmf}/xindy/class
%{texmf}/xindy/ord
%{texmf}/xindy/rules
%{texmf}/xindy/styles
%{texmf}/xindy/tex

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

%files -n xdvi
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/xdvi-motif.bin
# %attr(755,root,root) %{_bindir}/xdvizilla
# %{_mandir}/man1/xdvizilla.1*
%attr(755,root,root) %{_bindir}/xdvi-xaw
%attr(755,root,root) %{_bindir}/xdvi
%{_mandir}/man1/xdvi.1*
%{_desktopdir}/xdvi.desktop
%{_pixmapsdir}/xdvi.png
%{texmf}/xdvi

%files pdftex
%defattr(644,root,root,755)
# %doc %{texmf}/doc/programs/pdfcrop.txt
# %attr(755,root,root) %{_bindir}/pdfxtex
# %{_localstatedir}/fonts/map/pdftex
# %dir %{texmf}/fonts/map/pdftex
# %dir %{texmf}/fonts/map/pdftex/cmttf
# %{texmf}/fonts/map/pdftex/cmttf/cmttf.map
# %{texmf}/web2c/pdfetex-pl.pool
# %{texmf}/web2c/pdfetex.pool
# %{texmf}/web2c/pdfxtex.pool
# %{_mandir}/man1/pdfxtex.1*
%docdir %{texmfdist}/doc/pdftex
%attr(755,root,root) %{_bindir}/epstopdf
%attr(755,root,root) %{_bindir}/pdfcrop
%attr(755,root,root) %{_bindir}/pdftex
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/pdftexconfig.tex
%{texmfdist}/scripts/pdfcrop
%{_mandir}/man1/epstopdf.1*
%{_mandir}/man1/pdftex.1*

%files omega
%defattr(644,root,root,755)
# %{texmf}/web2c/omega.pool
# %{texmf}/web2c/aleph.pool
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/aleph.fmt
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/lambda.fmt
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/lamed.fmt
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/omega.fmt
%doc %{texmfdist}/doc/omega
%dir %{texmfdist}/omega
%dir %{texmfdist}/dvips/omega
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
%{texmfdist}/dvips/omega/config.omega
%{texmfdist}/dvips/omega/omega.cfg
%{texmfdist}/fonts/map/dvips/omega
%{texmfdist}/omega/ocp
%{texmfdist}/omega/otp
%{texmfdist}/tex/lambda
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

%files plain
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/plain
%{texmfdist}/tex/plain
%exclude %{texmfdist}/tex/plain/config/xetex.ini
#%{texmf}/web2c/plain.mem
#%{texmf}/web2c/plain.base

# %files format-plain
# %defattr(644,root,root,755)
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/tex.fmt
#%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/plain.fmt

# %files format-pdftex
# %defattr(644,root,root,755)
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdftex.fmt

# %files format-pdfetex
# %defattr(644,root,root,755)
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdfetex.fmt

%files mex
%defattr(644,root,root,755)
# %doc %{texmf}/doc/polish/mex
%dir %{texmfdist}/tex/mex
%dir %{texmfdist}/tex/mex/base
%{texmfdist}/tex/mex/base/mex1.tex
%{texmfdist}/tex/mex/base/mex2.tex
%{texmfdist}/tex/mex/base/mex.tex
%dir %{texmfdist}/tex/mex/config
%{texmfdist}/tex/mex/base/mexconf.tex

%files format-mex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mex
%{texmfdist}/tex/mex/config/mex.ini
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/mex.fmt

%files format-pdfmex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfmex
%{texmfdist}/tex/mex/config/pdfmex.ini
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdfmex.fmt

%files format-utf8mex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/utf8mex
%doc %{texmfdist}/doc/mex/utf8mex
%{texmfdist}/tex/mex/utf8mex
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/utf8mex.fmt

%files amstex
%defattr(644,root,root,755)
%dir %{texmfdist}/tex/amstex
%{texmfdist}/tex/amstex/base
%{texmfdist}/tex/amstex/config
%{texmfdist}/tex/plain/amsfonts

%files format-amstex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/amstex
%{texmfdist}/tex/amstex
%attr(755,root,root) %{_bindir}/amstex
%{_mandir}/man1/amstex.1*
# %lang(fi) %{_mandir}/fi/man1/amstex.1*
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/amstex.fmt

# %files format-pdfamstex
# %defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/pdfamstex
#%{texmf}/pdftex/amstex
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdfamstex.fmt

%files csplain
%defattr(644,root,root,755)
%dir %{texmfdist}/doc/cslatex/base
%doc %{texmfdist}/doc/cslatex/base/README-cspsfont
%doc %{texmfdist}/doc/cslatex/base/cs-fonts.doc
%doc %{texmfdist}/doc/cslatex/base/cscorr.tab
%doc %{texmfdist}/doc/cslatex/base/csplain.doc
%doc %{texmfdist}/doc/cslatex/base/parpozn.tex
%doc %{texmfdist}/doc/cslatex/base/test8z.tex
%doc %{texmfdist}/doc/cslatex/base/testlat.tex
%attr(755,root,root) %{_bindir}/csplain
%{texmfdist}/tex/csplain

%files format-csplain
%defattr(644,root,root,755)
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/csplain.fmt

%files format-pdfcsplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfcsplain
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdfcsplain.fmt

%files cslatex
%defattr(644,root,root,755)
# %doc %{texmf}/doc/cstex/INSTALL.cslatex
# %doc %{texmf}/doc/cstex/README.cslatex
%{texmfdist}/tex/cslatex
%{texmfdist}/tex/latex/cslatex

%files format-cslatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cslatex
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cslatex.fmt

%files format-pdfcslatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfcslatex
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdfcslatex.fmt

# %files cyrplain
# %defattr(644,root,root,755)
# %doc %{texmf}/doc/cyrplain
# %{texmf}/tex/cyrplain

# %files format-cyrplain
# %defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/cyrtex
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cyrtex.fmt

# %files format-cyramstex
# %defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/cyramstex
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cyramstex.fmt

# %files format-cyrtexinfo
# %defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/cyrtexinfo
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cyrtexinfo.fmt

%files eplain
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/etex
%doc %{texmfdist}/doc/eplain
%{texmfdist}/tex/plain/etex
%{texmfdist}/tex/eplain

%files format-eplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eplain
%attr(755,root,root) %{_bindir}/etex
%{_mandir}/man1/eplain.1*
%{_mandir}/man1/etex.1*
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/eplain.fmt
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/etex.fmt

%files context
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/context
# %doc %{texmf}/doc/polish/context
%attr(755,root,root) %{_bindir}/context
%attr(755,root,root) %{_bindir}/ctxtools
%attr(755,root,root) %{_bindir}/exatools
%attr(755,root,root) %{_bindir}/luatools
%attr(755,root,root) %{_bindir}/makempy
%attr(755,root,root) %{_bindir}/mpstools
%attr(755,root,root) %{_bindir}/mtxrun
%attr(755,root,root) %{_bindir}/mtxtools
%attr(755,root,root) %{_bindir}/pdfthumb
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
# %{_mandir}/man1/fdf2tex.1*
%{_mandir}/man1/ctxtools.1*
%{_mandir}/man1/pdftools.1*
%{_mandir}/man1/pstopdf.1*
%{_mandir}/man1/texfind.1*
%{_mandir}/man1/texfont.1*
%{_mandir}/man1/texmfstart.1*
%{_mandir}/man1/textools.1*
%{_mandir}/man1/texutil.1*
# %{_mandir}/man1/texshow.1*
%{texmfdist}/context
%{texmfdist}/fonts/enc/dvips/context
# %{texmfdist}/fonts/map/dvips/context
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

# no fmt, so commented out
#%files format-context-cz
#%defattr(644,root,root,755)
#%%{texmf}/tex/context/config/cont-cz.ini
# does not build with beta 20021025
#%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cont-cz.efmt

%files format-context-de
%defattr(644,root,root,755)
%{texmfdist}/tex/context/config/cont-de.ini
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cont-de.fmt
#%{_mandir}/man1/cont-de.1*

%files format-context-en
%defattr(644,root,root,755)
%{texmfdist}/tex/context/config/cont-en.ini
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cont-en.fmt
#%{_mandir}/man1/cont-en.1*
# what is the difference betwen uk and en in this particular situation?
%{texmfdist}/tex/context/config/cont-uk.ini
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cont-uk.fmt

# no fmt, so commented out
#%files format-context-it
#%defattr(644,root,root,755)
#%%{texmf}/tex/context/config/cont-it.ini

%files format-context-nl
%defattr(644,root,root,755)
%{texmfdist}/tex/context/config/cont-nl.ini
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cont-nl.fmt
#%{_mandir}/man1/cont-nl.1*

# no fmt, so commented out
#%files format-context-ro
#%defattr(644,root,root,755)
#%%{texmf}/tex/context/config/cont-ro.ini


%files latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/latex
%attr(755,root,root) %{_bindir}/pslatex
# %lang(fi) %{_mandir}/fi/man1/latex.1*
# %lang(pl) %{_mandir}/pl/man1/latex.1*
# %{_infodir}/latex.info*
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pslatex.1*

%dir %{texmfdist}/scripts
%dir %{texmfdist}/scripts/pst-pdf
%dir %{texmfdist}/source/generic
%dir %{texmfdist}/tex/latex
%dir %{texmfdist}/tex/plain
%dir %{texmf}/tex/latex

# %{texmfdist}/tex/latex/citesort
# %{texmfdist}/tex/latex/dvilj
# %{texmfdist}/tex/latex/eclbip
# %{texmfdist}/tex/latex/eo
# %{texmfdist}/tex/latex/example
# %{texmfdist}/tex/latex/fguill
# %{texmfdist}/tex/latex/floatflt
# %{texmfdist}/tex/latex/gletter
# %{texmfdist}/tex/latex/here
# %{texmfdist}/tex/latex/mt11p
# %{texmfdist}/tex/latex/relsize
# %{texmfdist}/tex/latex/selectp
# %{texmfdist}/tex/latex/shadow
# %{texmfdist}/tex/latex/showtags
# %{texmfdist}/tex/latex/tabls
# %{texmfdist}/tex/latex/texmacs
# %{texmfdist}/tex/latex/threeparttable
# %{texmfdist}/tex/latex/treesvr
# %{texmfdist}/tex/latex/ulem
# %{texmfdist}/tex/latex/url
# %{texmf}/tex/latex/version
# %{texmf}/tex/latex/vpage
%{texmfdist}/scripts/pst-pdf/ps4pdf
%{texmfdist}/tex/generic/pstricks
%{texmfdist}/tex/generic/shapepar
%{texmfdist}/tex/generic/textmerg
%{texmfdist}/tex/latex/12many
%{texmfdist}/tex/latex/AkkTeX
%{texmfdist}/tex/latex/ESIEEcv
%{texmfdist}/tex/latex/GuIT
%{texmfdist}/tex/latex/HA-prosper
%{texmfdist}/tex/latex/IEEEconf
%{texmfdist}/tex/latex/IEEEtran
%{texmfdist}/tex/latex/SIstyle
%{texmfdist}/tex/latex/Tabbing
%{texmfdist}/tex/latex/a0poster
%{texmfdist}/tex/latex/aastex
%{texmfdist}/tex/latex/abc
%{texmfdist}/tex/latex/achemso
%{texmfdist}/tex/latex/acmconf
%{texmfdist}/tex/latex/acmtrans
%{texmfdist}/tex/latex/acronym
%{texmfdist}/tex/latex/active-conf
%{texmfdist}/tex/latex/addlines
%{texmfdist}/tex/latex/adrlist
%{texmfdist}/tex/latex/aeguill
%{texmfdist}/tex/latex/afthesis
%{texmfdist}/tex/latex/aguplus
%{texmfdist}/tex/latex/aiaa
%{texmfdist}/tex/latex/akletter
%{texmfdist}/tex/latex/alg
%{texmfdist}/tex/latex/algorithm2e
%{texmfdist}/tex/latex/algorithmicx
%{texmfdist}/tex/latex/allrunes
%{texmfdist}/tex/latex/alnumsec
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
%{texmfdist}/tex/latex/apacite
%{texmfdist}/tex/latex/apl
%{texmfdist}/tex/latex/ar
%{texmfdist}/tex/latex/arabi
%{texmfdist}/tex/latex/arabtex
%{texmfdist}/tex/latex/archaic
%{texmfdist}/tex/latex/arcs
%{texmfdist}/tex/latex/arev
%{texmfdist}/tex/latex/armenian
%{texmfdist}/tex/latex/arydshln
%{texmfdist}/tex/latex/asaetr
%{texmfdist}/tex/latex/ascelike
%{texmfdist}/tex/latex/ascii
%{texmfdist}/tex/latex/assignment
%{texmfdist}/tex/latex/attachfile
%{texmfdist}/tex/latex/augie
%{texmfdist}/tex/latex/auncial-new
%{texmfdist}/tex/latex/aurical
%{texmfdist}/tex/latex/authoraftertitle
%{texmfdist}/tex/latex/authorindex
%{texmfdist}/tex/latex/auto-pst-pdf
%{texmfdist}/tex/latex/autoarea
%{texmfdist}/tex/latex/autotab
%{texmfdist}/tex/latex/avantgar
%{texmfdist}/tex/latex/babelbib
%{texmfdist}/tex/latex/bangtex
%{texmfdist}/tex/latex/barcodes
%{texmfdist}/tex/latex/base
%{texmfdist}/tex/latex/bayer
%{texmfdist}/tex/latex/bbding
%{texmfdist}/tex/latex/bbm-macros
%{texmfdist}/tex/latex/begriff
%{texmfdist}/tex/latex/bengali
%{texmfdist}/tex/latex/bera
%{texmfdist}/tex/latex/betababel
%{texmfdist}/tex/latex/beton
%{texmfdist}/tex/latex/bez123
%{texmfdist}/tex/latex/bibarts
%{texmfdist}/tex/latex/bibleref
%{texmfdist}/tex/latex/biblist
%{texmfdist}/tex/latex/bibtopicprefix
%{texmfdist}/tex/latex/bigfoot
%{texmfdist}/tex/latex/binomexp
%{texmfdist}/tex/latex/biocon
%{texmfdist}/tex/latex/bizcard
%{texmfdist}/tex/latex/blacklettert1
%{texmfdist}/tex/latex/blindtext
%{texmfdist}/tex/latex/blowup
%{texmfdist}/tex/latex/boisik
%{texmfdist}/tex/latex/boites
%{texmfdist}/tex/latex/boldtensors
%{texmfdist}/tex/latex/bookest
%{texmfdist}/tex/latex/bookhands
%{texmfdist}/tex/latex/booklet
%{texmfdist}/tex/latex/bookman
%{texmfdist}/tex/latex/bophook
%{texmfdist}/tex/latex/boxhandler
%{texmfdist}/tex/latex/bpchem
%{texmfdist}/tex/latex/braille
%{texmfdist}/tex/latex/breakurl
%{texmfdist}/tex/latex/bridge
%{texmfdist}/tex/latex/brushscr
%{texmfdist}/tex/latex/bullcntr
%{texmfdist}/tex/latex/burmese
%{texmfdist}/tex/latex/bussproofs
%{texmfdist}/tex/latex/bytefield
%{texmfdist}/tex/latex/calrsfs
%{texmfdist}/tex/latex/calxxxx
%{texmfdist}/tex/latex/captcont
%{texmfdist}/tex/latex/casyl
%{texmfdist}/tex/latex/catechis
%{texmfdist}/tex/latex/cbcoptic
%{texmfdist}/tex/latex/cbfonts
%{texmfdist}/tex/latex/ccaption
%{texmfdist}/tex/latex/cchess
%{texmfdist}/tex/latex/cclicenses
%{texmfdist}/tex/latex/cd-cover
%{texmfdist}/tex/latex/cd
%{texmfdist}/tex/latex/cdpbundl
%{texmfdist}/tex/latex/cellspace
%{texmfdist}/tex/latex/changebar
%{texmfdist}/tex/latex/changepage
%{texmfdist}/tex/latex/changes
%{texmfdist}/tex/latex/chappg
%{texmfdist}/tex/latex/chapterfolder
%{texmfdist}/tex/latex/chemarrow
%{texmfdist}/tex/latex/chemcompounds
%{texmfdist}/tex/latex/chemcono
%{texmfdist}/tex/latex/chemstyle
%{texmfdist}/tex/latex/cherokee
%{texmfdist}/tex/latex/chess
%{texmfdist}/tex/latex/chessboard
%{texmfdist}/tex/latex/chessfss
%{texmfdist}/tex/latex/chicago
%{texmfdist}/tex/latex/china2e
%{texmfdist}/tex/latex/chletter
%{texmfdist}/tex/latex/circ
%{texmfdist}/tex/latex/citeref
%{texmfdist}/tex/latex/cjhebrew
%{texmfdist}/tex/latex/cjk
%{texmfdist}/tex/latex/cjw
%{texmfdist}/tex/latex/classicthesis
%{texmfdist}/tex/latex/clefval
%{texmfdist}/tex/latex/cleveref
%{texmfdist}/tex/latex/clock
%{texmfdist}/tex/latex/clrscode
%{texmfdist}/tex/latex/cm-lgc
%{texmfdist}/tex/latex/cm-super
%{texmfdist}/tex/latex/cmap
%{texmfdist}/tex/latex/cmcyralt
%{texmfdist}/tex/latex/cmdstring
%{texmfdist}/tex/latex/cmdtrack
%{texmfdist}/tex/latex/cmll
%{texmfdist}/tex/latex/cmsd
%{texmfdist}/tex/latex/codepage
%{texmfdist}/tex/latex/colorinfo
%{texmfdist}/tex/latex/colortab
%{texmfdist}/tex/latex/colortbl
%{texmfdist}/tex/latex/colorwav
%{texmfdist}/tex/latex/combine
%{texmfdist}/tex/latex/commath
%{texmfdist}/tex/latex/compactbib
%{texmfdist}/tex/latex/complexity
%{texmfdist}/tex/latex/computational-complexity
%{texmfdist}/tex/latex/concprog
%{texmfdist}/tex/latex/confproc
%{texmfdist}/tex/latex/constants
%{texmfdist}/tex/latex/contour
%{texmfdist}/tex/latex/cooking
%{texmfdist}/tex/latex/cool
%{texmfdist}/tex/latex/coollist
%{texmfdist}/tex/latex/coolstr
%{texmfdist}/tex/latex/cooltooltips
%{texmfdist}/tex/latex/coordsys
%{texmfdist}/tex/latex/courier-scaled
%{texmfdist}/tex/latex/courier
%{texmfdist}/tex/latex/courseoutline
%{texmfdist}/tex/latex/coursepaper
%{texmfdist}/tex/latex/coverpage
%{texmfdist}/tex/latex/covington
%{texmfdist}/tex/latex/crop
%{texmfdist}/tex/latex/crossreference
%{texmfdist}/tex/latex/crosswrd
%{texmfdist}/tex/latex/csbulletin
%{texmfdist}/tex/latex/csquotes
%{texmfdist}/tex/latex/csvtools
%{texmfdist}/tex/latex/ctable
%{texmfdist}/tex/latex/ctib
%{texmfdist}/tex/latex/cuisine
%{texmfdist}/tex/latex/cursor
%{texmfdist}/tex/latex/curve
%{texmfdist}/tex/latex/curve2e
%{texmfdist}/tex/latex/cv
%{texmfdist}/tex/latex/cweb-latex
%{texmfdist}/tex/latex/cwpuzzle
%{texmfdist}/tex/latex/cyklop
%{texmfdist}/tex/latex/dashbox
%{texmfdist}/tex/latex/dashrule
%{texmfdist}/tex/latex/datatool
%{texmfdist}/tex/latex/dateiliste
%{texmfdist}/tex/latex/datenumber
%{texmfdist}/tex/latex/datetime
%{texmfdist}/tex/latex/dcpic
%{texmfdist}/tex/latex/decimal
%{texmfdist}/tex/latex/delimtxt
%{texmfdist}/tex/latex/diagnose
%{texmfdist}/tex/latex/dialogl
%{texmfdist}/tex/latex/dichokey
%{texmfdist}/tex/latex/dictsym
%{texmfdist}/tex/latex/digiconfigs
%{texmfdist}/tex/latex/dinbrief
%{texmfdist}/tex/latex/dingbat
%{texmfdist}/tex/latex/directory
%{texmfdist}/tex/latex/disser
%{texmfdist}/tex/latex/dlfltxb
%{texmfdist}/tex/latex/dnaseq
%{texmfdist}/tex/latex/docmfp
%{texmfdist}/tex/latex/doi
%{texmfdist}/tex/latex/doipubmed
%{texmfdist}/tex/latex/dotarrow
%{texmfdist}/tex/latex/dotseqn
%{texmfdist}/tex/latex/dottex
%{texmfdist}/tex/latex/doublestroke
%{texmfdist}/tex/latex/dpfloat
%{texmfdist}/tex/latex/dprogress
%{texmfdist}/tex/latex/drac
%{texmfdist}/tex/latex/draftcopy
%{texmfdist}/tex/latex/draftwatermark
%{texmfdist}/tex/latex/dramatist
%{texmfdist}/tex/latex/dtk
%{texmfdist}/tex/latex/duerer-latex
%{texmfdist}/tex/latex/dvdcoll
%{texmfdist}/tex/latex/dvipdfmx-def
%{texmfdist}/tex/latex/dyntree
%{texmfdist}/tex/latex/eCards
%{texmfdist}/tex/latex/ean13isbn
%{texmfdist}/tex/latex/easy
%{texmfdist}/tex/latex/ebezier
%{texmfdist}/tex/latex/ebsthesis
%{texmfdist}/tex/latex/ecclesiastic
%{texmfdist}/tex/latex/ecltree
%{texmfdist}/tex/latex/eco
%{texmfdist}/tex/latex/economic
%{texmfdist}/tex/latex/ecv
%{texmfdist}/tex/latex/ed
%{texmfdist}/tex/latex/edmargin
%{texmfdist}/tex/latex/ednotes
%{texmfdist}/tex/latex/eemeir
%{texmfdist}/tex/latex/eepic
%{texmfdist}/tex/latex/egameps
%{texmfdist}/tex/latex/egplot
%{texmfdist}/tex/latex/eiad
%{texmfdist}/tex/latex/ellipsis
%{texmfdist}/tex/latex/elmath
%{texmfdist}/tex/latex/elpres
%{texmfdist}/tex/latex/elsarticle
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
%{texmfdist}/tex/latex/environ
%{texmfdist}/tex/latex/envlab
%{texmfdist}/tex/latex/epigrafica
%{texmfdist}/tex/latex/epigraph
%{texmfdist}/tex/latex/epiolmec
%{texmfdist}/tex/latex/epsdice
%{texmfdist}/tex/latex/epspdfconversion
%{texmfdist}/tex/latex/eqlist
%{texmfdist}/tex/latex/eqname
%{texmfdist}/tex/latex/eqnarray
%{texmfdist}/tex/latex/eqparbox
%{texmfdist}/tex/latex/errata
%{texmfdist}/tex/latex/esdiff
%{texmfdist}/tex/latex/esint
%{texmfdist}/tex/latex/eskd
%{texmfdist}/tex/latex/eskdx
%{texmfdist}/tex/latex/eso-pic
%{texmfdist}/tex/latex/esvect
%{texmfdist}/tex/latex/etaremune
%{texmfdist}/tex/latex/etex-pkg
%{texmfdist}/tex/latex/ethiop
%{texmfdist}/tex/latex/etoolbox
%{texmfdist}/tex/latex/eukdate
%{texmfdist}/tex/latex/euler
%{texmfdist}/tex/latex/eulervm
%{texmfdist}/tex/latex/euproposal
%{texmfdist}/tex/latex/euro
%{texmfdist}/tex/latex/eurofont
%{texmfdist}/tex/latex/europecv
%{texmfdist}/tex/latex/eurosans
%{texmfdist}/tex/latex/eurosym
%{texmfdist}/tex/latex/everypage
%{texmfdist}/tex/latex/examdesign
%{texmfdist}/tex/latex/examplep
%{texmfdist}/tex/latex/exceltex
%{texmfdist}/tex/latex/exercise
%{texmfdist}/tex/latex/expdlist
%{texmfdist}/tex/latex/expl3
%{texmfdist}/tex/latex/export
%{texmfdist}/tex/latex/extarrows
%{texmfdist}/tex/latex/extpfeil
%{texmfdist}/tex/latex/extract
%{texmfdist}/tex/latex/extsizes
%{texmfdist}/tex/latex/facsimile
%{texmfdist}/tex/latex/faktor
%{texmfdist}/tex/latex/fancybox
%{texmfdist}/tex/latex/fancyhdr
%{texmfdist}/tex/latex/fancynum
%{texmfdist}/tex/latex/fancyref
%{texmfdist}/tex/latex/fancytooltips
%{texmfdist}/tex/latex/fancyvrb
%{texmfdist}/tex/latex/fax
%{texmfdist}/tex/latex/fc
%{texmfdist}/tex/latex/feyn
%{texmfdist}/tex/latex/feynmf
%{texmfdist}/tex/latex/fge
%{texmfdist}/tex/latex/figbib
%{texmfdist}/tex/latex/figsize
%{texmfdist}/tex/latex/filecontents
%{texmfdist}/tex/latex/fink
%{texmfdist}/tex/latex/fixfoot
%{texmfdist}/tex/latex/fixme
%{texmfdist}/tex/latex/flabels
%{texmfdist}/tex/latex/flacards
%{texmfdist}/tex/latex/flagderiv
%{texmfdist}/tex/latex/flashcards
%{texmfdist}/tex/latex/flippdf
%{texmfdist}/tex/latex/float
%{texmfdist}/tex/latex/floatrow
%{texmfdist}/tex/latex/flowfram
%{texmfdist}/tex/latex/fmp
%{texmfdist}/tex/latex/fmtcount
%{texmfdist}/tex/latex/fnbreak
%{texmfdist}/tex/latex/fncychap
%{texmfdist}/tex/latex/foekfont
%{texmfdist}/tex/latex/foilhtml
%{texmfdist}/tex/latex/fonetika
%{texmfdist}/tex/latex/fontinst
%{texmfdist}/tex/latex/fonttable
%{texmfdist}/tex/latex/footmisc
%{texmfdist}/tex/latex/footnpag
%{texmfdist}/tex/latex/forarray
%{texmfdist}/tex/latex/forloop
%{texmfdist}/tex/latex/formlett
%{texmfdist}/tex/latex/formula
%{texmfdist}/tex/latex/formular
%{texmfdist}/tex/latex/fouridx
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
%{texmfdist}/tex/latex/functan
%{texmfdist}/tex/latex/fundus
%{texmfdist}/tex/latex/gaceta
%{texmfdist}/tex/latex/galois
%{texmfdist}/tex/latex/gastex
%{texmfdist}/tex/latex/gatech-thesis
%{texmfdist}/tex/latex/gauss
%{texmfdist}/tex/latex/gb4e
%{texmfdist}/tex/latex/gcard
%{texmfdist}/tex/latex/gcite
%{texmfdist}/tex/latex/genmpage
%{texmfdist}/tex/latex/geometry
%{texmfdist}/tex/latex/geomsty
%{texmfdist}/tex/latex/germbib
%{texmfdist}/tex/latex/gfsartemisia
%{texmfdist}/tex/latex/gfsbaskerville
%{texmfdist}/tex/latex/gfsbodoni
%{texmfdist}/tex/latex/gfscomplutum
%{texmfdist}/tex/latex/gfsdidot
%{texmfdist}/tex/latex/gfsneohellenic
%{texmfdist}/tex/latex/gfsporson
%{texmfdist}/tex/latex/gfssolomos
%{texmfdist}/tex/latex/ginpenc
%{texmfdist}/tex/latex/gloss
%{texmfdist}/tex/latex/glossaries
%{texmfdist}/tex/latex/gmdoc
%{texmfdist}/tex/latex/gmeometric
%{texmfdist}/tex/latex/gmiflink
%{texmfdist}/tex/latex/gmutils
%{texmfdist}/tex/latex/gmverb
%{texmfdist}/tex/latex/gnuplottex
%{texmfdist}/tex/latex/go
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
%{texmfdist}/tex/latex/guitar
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
%{texmfdist}/tex/latex/hhtensor
%{texmfdist}/tex/latex/hilowres
%{texmfdist}/tex/latex/histogr
%{texmfdist}/tex/latex/hitec
%{texmfdist}/tex/latex/hpsdiss
%{texmfdist}/tex/latex/hrlatex
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
%{texmfdist}/tex/latex/inversepath
%{texmfdist}/tex/latex/invoice
%{texmfdist}/tex/latex/ipa
%{texmfdist}/tex/latex/iso
%{texmfdist}/tex/latex/iso10303
%{texmfdist}/tex/latex/isodate
%{texmfdist}/tex/latex/isodoc
%{texmfdist}/tex/latex/isonums
%{texmfdist}/tex/latex/isorot
%{texmfdist}/tex/latex/isotope
%{texmfdist}/tex/latex/itnumpar
%{texmfdist}/tex/latex/itrans
%{texmfdist}/tex/latex/iwona
%{texmfdist}/tex/latex/jeopardy
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
%dir %{texmfdist}/tex/latex/latexconfig
%{texmfdist}/tex/latex/latexconfig/latex.ini
%{texmfdist}/tex/latex/latexconfig/lualatex.ini
%{texmfdist}/tex/latex/latexconfig/mllatex.ini
%{texmfdist}/tex/latex/latexconfig/pdflatex.ini
%{texmfdist}/tex/latex/latexconfig/pdflualatex.ini
%{texmfdist}/tex/latex/layouts
%{texmfdist}/tex/latex/lettrine
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
%{texmfdist}/tex/latex/natbib
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
%{texmfdist}/tex/latex/oberdiek
%{texmfdist}/tex/latex/overpic
%{texmfdist}/tex/latex/paralist
%{texmfdist}/tex/latex/pb-diagram
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
%{texmfdist}/tex/latex/wrapfig
%{texmfdist}/tex/latex/wsuipa
%{texmfdist}/tex/latex/xargs
%{texmfdist}/tex/latex/xcolor
%{texmfdist}/tex/latex/xdoc
%{texmfdist}/tex/latex/xfor
%{texmfdist}/tex/latex/xifthen
%{texmfdist}/tex/latex/xkeyval
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
%{texmfdist}/tex/plain/etex
%{texmf}/tex/latex/config
%{texmf}/tex/latex/dvipdfm

%files latex-12many
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/12many
%{texmfdist}/source/latex/12many

%files latex-abstract
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/abstract
%{texmfdist}/tex/latex/abstract

%files latex-accfonts
%defattr(644,root,root,755)
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
%doc %{texmfdist}/doc/latex/amscls
%doc %{texmfdist}/doc/latex/amsmath
%doc %{texmfdist}/doc/latex/onlyamsmath
%{texmfdist}/tex/latex/amscls
%{texmfdist}/tex/latex/amsmath
%{texmfdist}/tex/latex/amsfonts
%{texmfdist}/tex/latex/onlyamsmath
%{texmfdist}/source/latex/onlyamsmath

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

%files latex-backgammon
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/backgammon
%{texmfdist}/tex/latex/backgammon

%files latex-bardiag
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bardiag
%{texmfdist}/tex/latex/bardiag

%files latex-bbm
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/bbm
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
%doc %{texmfdist}/doc/bibtex/base
%doc %{texmfdist}/doc/latex/adrconv
%doc %{texmfdist}/doc/latex/bibtopic
%doc %{texmfdist}/doc/latex/bibunits
%doc %{texmfdist}/doc/latex/natbib
%doc %{texmfdist}/doc/latex/footbib
%dir %{texmfdist}/doc/bibtex
%dir %{texmfdist}/bibtex
%dir %{texmfdist}/bibtex/bib
%dir %{texmfdist}/bibtex/bst
%dir %{texmfdist}/bibtex/csf

%attr(755,root,root) %{_bindir}/bibtex
%attr(755,root,root) %{_bindir}/rubibtex

%{texmfdist}/bibtex/bst/base
%{texmfdist}/bibtex/csf/base
%{texmfdist}/bibtex/bib/base
%{texmfdist}/bibtex/bst/adrconv
%{texmfdist}/bibtex/bib/adrconv
%{texmfdist}/source/latex/adrconv
%{texmfdist}/tex/latex/adrconv
# %{texmf}/bibtex/bst/misc
%{texmfdist}/bibtex/bst/natbib
%{texmfdist}/tex/latex/natbib
%{texmfdist}/tex/latex/bibtopic
%{texmfdist}/source/latex/bibunits
%{texmfdist}/tex/latex/bibunits
%{texmfdist}/source/latex/footbib
%{texmfdist}/tex/latex/footbib

%{_mandir}/man1/bibtex.1*
%{_mandir}/man1/rubibtex.1*

%files latex-bibtex-ams
%defattr(644,root,root,755)
%{texmfdist}/bibtex/bst/ams
%{texmfdist}/bibtex/bib/ams

%files latex-bibtex-pl
%defattr(644,root,root,755)
%{texmfdist}/bibtex/bib/gustlib/plbib.bib

%files latex-bibtex-german
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/bibtex/germbib
%{texmfdist}/bibtex/bst/germbib
%{texmfdist}/tex/latex/germbib

%files latex-bibtex-revtex4
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/revtex/revtex4.pdf
%{texmfdist}/source/latex/revtex/revtex4.dtx
%{texmfdist}/source/latex/revtex/revtex4.ins
%{texmfdist}/tex/latex/revtex/revtex4.cls

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

# %files latex-bibtex-nor
# %defattr(644,root,root,755)
# %{texmf}/bibtex/bst/norbib

%files latex-bibtex-styles
%defattr(644,root,root,755)
%{texmfdist}/bibtex/bib/IEEEtran
%{texmfdist}/bibtex/bib/abstyles
%{texmfdist}/bibtex/bib/achemso
%{texmfdist}/bibtex/bib/acmtrans
%{texmfdist}/bibtex/bib/aiaa
%{texmfdist}/bibtex/bib/apacite
%{texmfdist}/bibtex/bib/asaetr
%{texmfdist}/bibtex/bib/ascelike
%{texmfdist}/bibtex/bib/beebe
%{texmfdist}/bibtex/bib/bibhtml
%{texmfdist}/bibtex/bib/bibtopic
%{texmfdist}/bibtex/bib/biocon
%{texmfdist}/bibtex/bib/computational-complexity
%{texmfdist}/bibtex/bib/din1505
%{texmfdist}/bibtex/bib/directory
%{texmfdist}/bibtex/bib/dtk
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
%{texmfdist}/bibtex/bib/philosophersimprint
%{texmfdist}/bibtex/bib/revtex
%{texmfdist}/bibtex/bib/spie
%{texmfdist}/bibtex/bib/urlbst
%{texmfdist}/bibtex/bst/IEEEtran
%{texmfdist}/bibtex/bst/abstyles
%{texmfdist}/bibtex/bst/achemso
%{texmfdist}/bibtex/bst/acmtrans
%{texmfdist}/bibtex/bst/afthesis
%{texmfdist}/bibtex/bst/aguplus
%{texmfdist}/bibtex/bst/aiaa
%{texmfdist}/bibtex/bst/aichej
%{texmfdist}/bibtex/bst/ametsoc
%{texmfdist}/bibtex/bst/apacite
%{texmfdist}/bibtex/bst/asaetr
%{texmfdist}/bibtex/bst/ascelike
%{texmfdist}/bibtex/bst/babelbib
%{texmfdist}/bibtex/bst/beebe
%{texmfdist}/bibtex/bst/bibhtml
%{texmfdist}/bibtex/bst/chem-journal
%{texmfdist}/bibtex/bst/chicago
%{texmfdist}/bibtex/bst/computational-complexity
%{texmfdist}/bibtex/bst/confproc
%{texmfdist}/bibtex/bst/datatool
%{texmfdist}/bibtex/bst/din1505
%{texmfdist}/bibtex/bst/dinat
%{texmfdist}/bibtex/bst/directory
%{texmfdist}/bibtex/bst/dtk
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
%{texmfdist}/bibtex/bst/mciteplus
%{texmfdist}/bibtex/bst/mslapa
%{texmfdist}/bibtex/bst/multibib
%{texmfdist}/bibtex/bst/munich
%{texmfdist}/bibtex/bst/nature
%{texmfdist}/bibtex/bst/nddiss
%{texmfdist}/bibtex/bst/opcit
%{texmfdist}/bibtex/bst/perception
%{texmfdist}/bibtex/bst/revtex
%{texmfdist}/bibtex/bst/rsc
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
%doc %{texmfdist}/doc/bibtex/abstyles
%doc %{texmfdist}/doc/bibtex/bibhtml
%doc %{texmfdist}/doc/bibtex/dinat
%doc %{texmfdist}/doc/bibtex/economic
%doc %{texmfdist}/doc/bibtex/elsevier-bib
%doc %{texmfdist}/doc/bibtex/gost
%doc %{texmfdist}/doc/bibtex/ijqc
%doc %{texmfdist}/doc/bibtex/iopart-num
%doc %{texmfdist}/doc/generic/t2%{_sysconfdir}/rubibtex
%doc %{texmfdist}/doc/latex/IEEEtran
%{texmfdist}/source/bibtex/gost

%files latex-bibtex-vancouver
%defattr(644,root,root,755)
%dir %{texmfdist}/bibtex/bib/vancouver
%{texmfdist}/bibtex/bib/vancouver/vancouver.bib
%{texmfdist}/bibtex/bst/vancouver/vancouver.bst
%doc %{texmfdist}/doc/bibtex/vancouver/README
%doc %{texmfdist}/doc/bibtex/vancouver/vancouver.pdf
%doc %{texmfdist}/doc/bibtex/vancouver/vancouver.tex

%files latex-booktabs
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/booktabs
%{texmfdist}/tex/latex/booktabs

%files latex-caption
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/caption
%{texmfdist}/tex/latex/caption

%files latex-carlisle
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/carlisle
%{texmfdist}/tex/latex/carlisle

%files latex-ccfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ccfonts
%{texmfdist}/tex/latex/ccfonts

%files latex-cite
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/cite

%files latex-cmbright
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/cmbright
%{texmfdist}/tex/latex/cmbright

%files latex-comment
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/comment
%{texmfdist}/tex/latex/comment

%files latex-concmath
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/concmath

%files latex-currvita
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/currvita
%{texmfdist}/tex/latex/currvita

%files latex-curves
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/curves
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

# %files latex-dstroke
# %defattr(644,root,root,755)
# %{texmf}/tex/latex/dstroke

%files latex-enumitem
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/enumitem
%{texmfdist}/tex/latex/enumitem

%files latex-exam
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/exam
%{texmfdist}/tex/latex/exam

%files latex-gbrief
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/g-brief
%{texmfdist}/tex/latex/g-brief

%files latex-jknappen
%defattr(644,root,root,755)
%doc %{texmfdist}/fonts/source/jknappen
%{texmfdist}/fonts/tfm/jknappen

%files latex-lastpage
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lastpage
%{texmfdist}/tex/latex/lastpage

%files latex-leftidx
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/leftidx
%{texmfdist}/tex/latex/leftidx

%files latex-lm
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/lm
%{texmfdist}/tex/latex/lm
%{texmfdist}/fonts/afm/public/lm
%{texmfdist}/fonts/enc/dvips/lm
%{texmfdist}/fonts/map/dvips/lm
%{texmfdist}/fonts/map/dvipdfm/lm
%{texmfdist}/fonts/opentype/public/lm
%{texmfdist}/fonts/tfm/public/lm
%{texmfdist}/source/fonts/lm

%files latex-lucidabr
%defattr(644,root,root,755)
%{texmfdist}/vtex/config/lucidabr-k.ali
%{texmfdist}/vtex/config/lucidabr.ali

%files latex-lineno
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lineno
%{texmfdist}/tex/latex/lineno


%files latex-marvosym
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/marvosym

#%files latex-mathpple
#%defattr(644,root,root,755)

#%files latex-mathtime
#%defattr(644,root,root,755)

%files latex-microtype
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/microtype
%{texmfdist}/source/latex/microtype
%{texmfdist}/tex/latex/microtype

%files latex-mflogo
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/mflogo
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

%files latex-moreverb
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/moreverb
%{texmfdist}/tex/latex/moreverb

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
%{texmfdist}/tex/latex/ntheorem
%doc %{texmfdist}/doc/latex/ntheorem

# %files latex-palatcm
# %defattr(644,root,root,755)
# %{texmf}/tex/latex/palatcm

%files latex-pgf
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pgf
%{texmfdist}/tex/generic/pgf
%{texmfdist}/tex/generic/pgfplots
%{texmfdist}/tex/latex/pgf
%{texmfdist}/tex/latex/pgfopts
%{texmfdist}/tex/latex/pgfplots

%files latex-psnfss
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/psnfss
%{texmfdist}/fonts/map/dvips/psnfss
%{texmfdist}/source/latex/psnfss
%{texmfdist}/source/latex/latex-tds/tex/psnfss2e.drv
%{texmfdist}/tex/latex/psnfss


%files latex-pxfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/pxfonts
%{texmfdist}/tex/latex/pxfonts
%{texmfdist}/fonts/type1/public/pxfonts
%{texmfdist}/fonts/afm/public/pxfonts
%{texmfdist}/fonts/tfm/public/pxfonts
%{texmfdist}/fonts/vf/public/pxfonts
%{texmfdist}/fonts/map/dvips/pxfonts

#%files latex-qfonts
#%defattr(644,root,root,755)

%files latex-SIstyle
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/SIstyle
%{texmfdist}/source/latex/SIstyle

%files latex-SIunits
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/SIunits
%{texmfdist}/tex/latex/SIunits
%{texmfdist}/source/latex/SIunits

%files latex-Tabbing
%defattr(644,root,root,755)
%{texmfdist}/source/latex/Tabbing
%{texmfdist}/doc/latex/Tabbing

%files latex-txfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/txfonts
%{texmfdist}/fonts/type1/public/txfonts
%{texmfdist}/fonts/afm/public/txfonts
%{texmfdist}/fonts/enc/dvips/txfonts
%{texmfdist}/fonts/tfm/public/txfonts
%{texmfdist}/fonts/vf/public/txfonts
%{texmfdist}/fonts/map/dvips/txfonts
%{texmfdist}/tex/latex/txfonts

%files latex-ucs
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ucs
%{texmfdist}/tex/latex/ucs

%files latex-umlaute
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/umlaute

# %files latex-urwvn
# %defattr(644,root,root,755)

%files latex-wasysym
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/wasysym
%{texmfdist}/tex/latex/wasysym
%{texmfdist}/source/latex/wasysym

%files latex-xcolor
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/xcolor
%{texmfdist}/dvips/xcolor/xcolor.pro
%{texmfdist}/source/latex/xcolor

# %files format-latex
# %defattr(644,root,root,755)
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/latex.fmt

%files format-pdflatex
%defattr(644,root,root,755)
#%{texmf}/pdftex/latex/config
# %dir %{texmf}/pdftex/latex
%attr(755,root,root) %{_bindir}/pdflatex
%{_mandir}/man1/pdflatex.1*
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdflatex.fmt

# %files platex
# %defattr(644,root,root,755)
# %doc %{texmf}/doc/latex/platex
# %dir %{texmf}/tex/platex
# %{texmf}/tex/platex/config
# %{texmf}/tex/latex/platex

# %files format-platex
# %defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/platex
#%attr(755,root,root) %{_bindir}/platex-pl
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/platex.fmt
#%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/platex-pl.fmt

# %files format-pdfplatex
# %defattr(644,root,root,755)
#%dir %{texmf}/pdftex/platex
#%{texmf}/pdftex/platex/config
# %attr(755,root,root) %{_bindir}/pdfplatex
# %config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdfplatex.fmt

%files tex-babel
%defattr(644,root,root,755)
%dir %{texmfdist}/source/generic/babel
%doc %{texmfdist}/doc/generic/babel
%{texmfdist}/tex/generic/babel

%files tex-german
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/german
%{texmfdist}/tex/generic/german

%files tex-mfpic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/mfpic
%{texmfdist}/tex/generic/mfpic

%files tex-misc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/localloc
%doc %{texmfdist}/doc/generic/multido
%doc %{texmfdist}/doc/generic/tap

%{texmfdist}/tex/generic/eijkhout
%{texmfdist}/tex/generic/multido
%{texmfdist}/tex/generic/misc

%files tex-pictex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pictex
%{texmfdist}/tex/generic/pictex

%files tex-pstricks
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pstricks
%{texmfdist}/dvips/pstricks
%{texmfdist}/tex/generic/pstricks

# %files tex-qpx
# %defattr(644,root,root,755)
# %doc %{texmf}/doc/fonts/polish/qpx
# %{texmf}/tex/generic/qpx

%files tex-qpxqtx
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/qpxqtx
%{texmfdist}/fonts/tfm/public/qpxqtx
%{texmfdist}/fonts/vf/public/qpxqtx
%{texmfdist}/tex/generic/qpxqtx

%files tex-ruhyphen
%defattr(644,root,root,755)
%{texmfdist}/tex/generic/ruhyphen
%{texmfdist}/source/generic/ruhyphen

%files tex-spanish
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/spanish-mx
%dir %{texmfdist}/source/latex/mapcodes
%dir %{texmfdist}/source/latex/polyglot/langs
%dir %{texmfdist}/tex/latex/apacite
%dir %{texmfdist}/tex/latex/babelbib
%dir %{texmfdist}/tex/latex/dvdcoll/dcl
%dir %{texmfdist}/tex/texsis/base
%{texmfdist}/source/generic/babel/spanish.ins
%{texmfdist}/source/generic/babel/spanish.dtx
%{texmfdist}/source/latex/polyglot/langs/spanish.ld
%{texmfdist}/source/latex/polyglot/langs/spanish.ot1
%{texmfdist}/source/latex/mapcodes/spanish.map
%{texmfdist}/source/latex/mapcodes/spanish.dtx
%{texmfdist}/tex/texsis/base/Spanish.txs
%{texmfdist}/tex/generic/babel/spanish.sty
%{texmfdist}/tex/generic/babel/spanish.ldf
%{texmfdist}/tex/latex/spanish-mx
%{texmfdist}/tex/latex/custom-bib/spanish.mbs
%{texmfdist}/tex/latex/babelbib/spanish.bdf
%{texmfdist}/tex/latex/apacite/spanish.apc
%{texmfdist}/tex/latex/dvdcoll/dcl/spanish.dcl

%files tex-texdraw
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/texdraw
%{texmfdist}/tex/generic/texdraw

%files tex-thumbpdf
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/thumbpdf
%attr(755,root,root) %{_bindir}/thumbpdf
%{texmfdist}/tex/generic/thumbpdf
%{texmfdist}/scripts/thumbpdf
%{_mandir}/man1/thumbpdf.1*

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

%files fonts-ae
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/ae
%{texmfdist}/fonts/tfm/public/ae
%{texmfdist}/fonts/vf/public/ae
%{texmfdist}/source/fonts/ae

%files fonts-ams
%defattr(644,root,root,755)
%{texmfdist}/bibtex/bst/ams
%{texmfdist}/bibtex/bib/ams
%{texmfdist}/dvips/ams
%{texmfdist}/fonts/source/public/ams
%{texmfdist}/fonts/type1/bluesky/ams
%{texmfdist}/fonts/afm/bluesky/ams
%{texmfdist}/fonts/tfm/public/ams
%{texmfdist}/fonts/map/dvips/ams

%files fonts-antp
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/antp
%{texmfdist}/fonts/enc/dvips/antp
%{texmfdist}/fonts/map/dvips/antp
%{texmfdist}/fonts/afm/public/antp
%{texmfdist}/fonts/tfm/public/antp
%{texmfdist}/dvips/antp

%files fonts-antt
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/antt
%{texmfdist}/fonts/afm/public/antt
%{texmfdist}/fonts/opentype/public/antt
%{texmfdist}/fonts/enc/dvips/antt
%{texmfdist}/fonts/tfm/public/antt
%{texmfdist}/fonts/map/dvips/antt
%{texmfdist}/tex/plain/antt
%{texmfdist}/tex/latex/antt

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
%{texmfdist}/source/latex/bbm
%{texmfdist}/tex/latex/bbm

%files fonts-bbold
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/bbold
%{texmfdist}/fonts/tfm/public/bbold

# %files fonts-bh
# %defattr(644,root,root,755)
# %doc %{texmf}/doc/fonts/bh
# %{texmf}/fonts/tfm/bh
# %{texmf}/fonts/vf/bh

%files fonts-bitstream
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/bitstrea
%{texmfdist}/fonts/tfm/bitstrea
%{texmfdist}/fonts/vf/bitstrea

#%files fonts-cbgreek
#%defattr(644,root,root,755)

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
%doc %{texmfdist}/doc/fonts/cm
%dir %{texmfdist}/doc/fonts
%dir %{texmfdist}/dvips
%dir %{texmfdist}/fonts/afm/bluesky
%dir %{texmfdist}/fonts/map/dvips
%dir %{texmfdist}/fonts/pk/ljfour/public
%{texmfdist}/dvips/cm
%{texmfdist}/fonts/source/public/cm
%{texmfdist}/fonts/afm/bluesky/cm
%{texmfdist}/fonts/tfm/public/cm
%{texmfdist}/fonts/pk/ljfour/public/cm
%{texmfdist}/fonts/map/dvips/cm

%files fonts-cmbright
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/cmbright
%{texmfdist}/fonts/source/public/cmbright
%{texmfdist}/fonts/tfm/public/cmbright
%{texmfdist}/source/latex/cmbright
%{texmfdist}/tex/latex/cmbright

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

%files fonts-concmath
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/concmath
%doc %{texmfdist}/doc/latex/concmath
%{texmfdist}/fonts/source/public/concmath
%{texmfdist}/fonts/tfm/public/concmath
%{texmfdist}/source/latex/concmath
%{texmfdist}/tex/latex/concmath

%files fonts-concrete
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/concrete
%{texmfdist}/fonts/source/public/concrete
%{texmfdist}/fonts/tfm/public/concrete

%files fonts-cs
%defattr(644,root,root,755)
%{texmfdist}/dvips/cs
%{texmfdist}/fonts/source/public/cs
%{texmfdist}/fonts/enc/dvips/cs
%{texmfdist}/fonts/tfm/public/cs
%{texmfdist}/fonts/map/dvips/cs

#%files fonts-dstroke
#%defattr(644,root,root,755)

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
%doc %{texmfdist}/doc/latex/eulervm
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
%{texmfdist}/doc/fonts/gothic
%{texmfdist}/dvips/gothic
%{texmfdist}/fonts/source/public/gothic
%{texmfdist}/fonts/type1/public/gothic
%{texmfdist}/fonts/afm/public/gothic
%{texmfdist}/fonts/tfm/public/gothic
%{texmfdist}/fonts/vf/public/gothic
%{texmfdist}/fonts/map/dvips/gothic

%files fonts-hoekwater
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/hoekwater
%{texmfdist}/fonts/tfm/hoekwater
%{texmfdist}/fonts/truetype/hoekwater

%files fonts-jknappen
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/jknappen
%{texmfdist}/fonts/tfm/jknappen

%files fonts-latex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/esint
%dir %{texmfdist}/fonts/source/public/latex-fonts
%dir %{texmfdist}/fonts/type1/bluesky/latex-fonts
%dir %{texmfdist}/fonts/afm/bluesky/latex-fonts
%dir %{texmfdist}/fonts/tfm/public/latex-fonts
%dir %{texmfdist}/fonts/map/dvips/latex-fonts
%{texmfdist}/fonts/source/public/esint
%{texmfdist}/fonts/tfm/public/esint
%{texmfdist}/source/latex/esint
%{texmfdist}/tex/latex/esint
%{texmfdist}/fonts/source/public/latex-fonts/*
%{texmfdist}/fonts/type1/bluesky/latex-fonts/*
%{texmfdist}/fonts/afm/bluesky/latex-fonts/*
%{texmfdist}/fonts/tfm/public/latex-fonts/*
%{texmfdist}/fonts/map/dvips/latex-fonts/*

%files fonts-lh
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/lh
%{texmfdist}/fonts/source/lh
%{texmfdist}/metapost/support/charlib/LH
%{texmfdist}/source/fonts/lh
%{texmfdist}/source/latex/lh

%files fonts-lm
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/lm
%{texmfdist}/fonts/type1/public/lm
%{texmfdist}/fonts/afm/public/lm
%{texmfdist}/fonts/opentype/public/lm
%{texmfdist}/fonts/enc/dvips/lm
%{texmfdist}/fonts/tfm/public/lm
%{texmfdist}/fonts/map/dvips/lm
%{texmfdist}/fonts/map/dvipdfm/lm
%{texmfdist}/source/fonts/lm
%{texmfdist}/tex/latex/lm

%files fonts-marvosym
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/marvosym
%dir %{texmfdist}/source/fonts/eurofont
%dir %{texmfdist}/source/fonts/eurofont/marvosym
%dir %{texmfdist}/tex/latex
%{texmfdist}/fonts/type1/public/marvosym
%{texmfdist}/fonts/afm/public/marvosym
%{texmfdist}/fonts/tfm/public/marvosym
%{texmfdist}/fonts/map/dvips/marvosym
%{texmfdist}/source/fonts/eurofont/marvosym/*
%{texmfdist}/tex/latex/marvosym

%files fonts-mflogo
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/mflogo
%{texmfdist}/fonts/source/public/mflogo
%{texmfdist}/fonts/type1/hoekwater/mflogo
%{texmfdist}/fonts/afm/hoekwater/mflogo
%{texmfdist}/fonts/tfm/public/mflogo
%{texmfdist}/fonts/map/dvips/mflogo
%{texmfdist}/source/latex/mflogo
%{texmfdist}/tex/latex/mflogo

%files fonts-misc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/marvosym/mac/oztex/tex-font/misc
%{texmfdist}/fonts/source/public/misc
%{texmfdist}/fonts/tfm/public/misc
%{texmfdist}/fonts/misc

%files fonts-monotype
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/monotype
%{texmfdist}/fonts/vf/monotype

%files fonts-omega
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/omega
%dir %{texmfdist}/omega
%dir %{texmfdist}/omega/otp
%dir %{texmfdist}/omega/ocp
%{texmfdist}/dvips/omega
%{texmfdist}/fonts/ofm/public/omega
%{texmfdist}/fonts/type1/public/omega
%{texmfdist}/fonts/afm/public/omega
%{texmfdist}/fonts/ovp/public/omega
%{texmfdist}/fonts/tfm/public/omega
%{texmfdist}/fonts/ovf/public/omega
%{texmfdist}/fonts/map/dvips/omega
%{texmfdist}/omega/ocp/omega
%{texmfdist}/omega/otp/omega
%{texmfdist}/tex/plain/omega

#%files fonts-pazo
#%defattr(644,root,root,755)

%files fonts-pl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/pl
%{texmfdist}/dvips/pl
%{texmfdist}/fonts/source/public/pl
%{texmfdist}/fonts/type1/public/pl
%{texmfdist}/fonts/afm/public/pl
%{texmfdist}/fonts/enc/dvips/pl
%{texmfdist}/fonts/tfm/public/pl
%{texmfdist}/fonts/map/dvips/pl
%{texmf}/scripts/texlive/tlmgrgui/lang/pl

%files fonts-px
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/pxfonts
# %doc %{texmf}/doc/doc/english/free-math-font-survey/source/pxfonts.tex
# %doc %{texmf}/doc/doc/english/free-math-font-survey/images/pxfonts.png
%dir %{texmfdist}/fonts/map/dvips/pxfonts
%dir %{texmfdist}/tex/latex/pxfonts
%{texmfdist}/fonts/map/dvips/pxfonts/pxfonts.map
%{texmfdist}/fonts/afm/public/pxfonts
%{texmfdist}/fonts/tfm/public/pxfonts
%{texmfdist}/fonts/type1/public/pxfonts
%{texmfdist}/fonts/vf/public/pxfonts
%{texmfdist}/tex/latex/pxfonts/pxfonts.sty

#%files fonts-qfonts
#%defattr(644,root,root,755)
# %doc %{texmf}/doc/fonts/polish/qfonts
# %{texmf}/fonts/enc/dvips/qfonts
# %{texmf}/fonts/map/dvips/qfonts
# %{texmf}/dvips/qfonts
# %{texmf}/fonts/afm/public/qfonts
# %{texmf}/fonts/tfm/public/qfonts

# %files fonts-qpx
# %defattr(644,root,root,755)
# %{texmf}/fonts/tfm/public/qpx
# %{texmf}/fonts/vf/public/qpx

%files fonts-qpxqtx
%defattr(644,root,root,755)
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
%{texmfdist}/fonts/map/dvips/txfonts/txfonts.map
%{texmfdist}/fonts/afm/public/txfonts
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
%{texmfdist}/fonts/tfm/vntex/urwvn
%{texmfdist}/fonts/type1/vntex/urwvn
%{texmfdist}/fonts/vf/vntex/urwvn

%files fonts-vnr
%defattr(644,root,root,755)
%{texmfdist}/fonts/map/dvips/vntex
%{texmfdist}/fonts/source/vntex/vnr
%{texmfdist}/fonts/tfm/vntex/vnr

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
# %{texmfdist}/fonts/afm/public/xypic
%{texmfdist}/fonts/source/public/xypic
%{texmfdist}/fonts/tfm/public/xypic

%files fonts-yandy
%defattr(644,root,root,755)
# %{texmf}/fonts/afm/yandy
%{texmfdist}/source/fonts/eurofont/marvosym/tfmfiles/yandy
# %{texmf}/fonts/tfm/yandy
# %{texmf}/fonts/vf/yandy

%files fonts-type1-antp
%defattr(644,root,root,755)
%{texmfdist}/dvips/antp
%{texmfdist}/fonts/type1/public/antp

%files fonts-type1-antt
%defattr(644,root,root,755)
# %{texmf}/dvips/antt
%{texmfdist}/fonts/type1/public/antt

%files fonts-type1-arphic
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/arphic

%files fonts-type1-belleek
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/belleek
%{texmfdist}/fonts/type1/public/belleek

%files fonts-type1-bitstream
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/bitstrea

%files fonts-type1-bluesky
%defattr(644,root,root,755)
# %doc %{texmf}/doc/fonts/bluesky
# %{texmf}/dvips/bluesky
%{texmfdist}/fonts/type1/bluesky

%files fonts-type1-cc-pl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/cc-pl
%{texmfdist}/fonts/type1/public/cc-pl

%files fonts-type1-cmcyr
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/cmcyr

%files fonts-type1-cs
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/cs

# %files fonts-type1-dstroke
# %defattr(644,root,root,755)
# %{texmf}/fonts/type1/public/dstroke

%files fonts-type1-eurosym
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/eurosym

%files fonts-type1-hoekwater
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/hoekwater

%files fonts-type1-fpl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/fpl
%{texmfdist}/fonts/afm/public/fpl
%{texmfdist}/fonts/type1/public/fpl

%files fonts-type1-lm
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/public/lm
%{texmfdist}/fonts/type1/public/lm

%files fonts-type1-marvosym
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/marvosym

%files fonts-type1-mathpazo
%defattr(644,root,root,755)
# %doc %{texmf}/doc/fonts/mathpazo
%{texmfdist}/fonts/afm/public/mathpazo
%{texmfdist}/fonts/type1/public/mathpazo

%files fonts-type1-omega
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/omega

%files fonts-type1-pl
%defattr(644,root,root,755)
# %doc %{texmf}/doc/fonts/polish/plpsfont
%{texmfdist}/fonts/type1/public/pl

%files fonts-type1-px
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/pxfonts

# %files fonts-type1-qfonts
# %defattr(644,root,root,755)
# %{texmfdist}/fonts/type1/public/qfonts

%files fonts-type1-tx
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/txfonts

# %files fonts-type1-tt2001
# %defattr(644,root,root,755)
# %{texmf}/fonts/type1/public/tt2001

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

# TeXLive-specific

%files afm2pl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afm2pl
%{_mandir}/man1/afm2pl*

%files bbox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bbox
%{_mandir}/man1/bbox*

%files cefutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cef*
%dir %{texmfdist}/tex/latex/cjk
%dir %{texmfdist}/doc/latex/cjk
%dir %{texmfdist}/source/latex/cjk
%dir %{texmfdist}/source/latex/cjk/utils
%{texmfdist}/tex/latex/cjk/CEF
%doc %{texmfdist}/doc/latex/cjk/doc
%doc %{texmfdist}/doc/latex/cjk/examples
%{texmfdist}/source/latex/cjk/utils/CEFconv

%files detex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/detex
%{_mandir}/man1/detex*


%files dviutils
%defattr(644,root,root,755)
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

%files epsutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/epsffit
%attr(755,root,root) %{_bindir}/epspdf
%attr(755,root,root) %{_bindir}/epspdftk
%{texmfdist}/scripts/epspdf
%{_mandir}/man1/epsffit*
%doc %{texmfdist}/doc/epspdf

%files filters
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fix*
%{_mandir}/man1/fix*

%files uncategorized-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/devnag
%attr(755,root,root) %{_bindir}/disdvi

%files tex4ht
%defattr(644,root,root,755)
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
%{texmf}/scripts/tex4ht
%{texmfdist}/tex/generic/tex4ht
%dir %{texmfdist}/scripts/tex4ht
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/ht.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htcontext.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htlatex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htmex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/httex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/httexi.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htxelatex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htxetex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/mk4ht.pl
%{texmfdist}/tex4ht

%files xetex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdvipdfmx
%attr(755,root,root) %{_bindir}/xelatex
%attr(755,root,root) %{_bindir}/xetex
%{texmf}/fmtutil/format.xetex.cnf
%doc %{texmfdist}/doc/xelatex
%doc %{texmfdist}/doc/xetex
%{texmfdist}/scripts/xetex
%{texmfdist}/tex/generic/ifxetex
%{texmfdist}/tex/generic/xetexconfig
%{texmfdist}/tex/latex/latexconfig/xelatex.ini
%{texmfdist}/tex/plain/config/xetex.ini
%{texmfdist}/tex/xelatex
%{texmfdist}/tex/xetex

%files xmltex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/xmltex
%attr(755,root,root) %{_bindir}/pdfxmltex
%attr(755,root,root) %{_bindir}/xmltex
%{texmfdist}/tex/xmltex
%{texmf}/fmtutil/format.xmltex.cnf
