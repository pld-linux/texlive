# TODO:
# - get rid of /etc/cron.daily dependency from base pkg, use systemd-tmpfiles
#   instead; also drop the Suggests: tmpwatch
# - dep loop: kpathsea -> texhash -> texlive -> texconfig -> dvips -> libkpathsea
#   mitigated by [ ! -x texhash ] guard in scriptlets; cosmetic rpm warning only
# - switch to out-of-source build (remove --enable-build-in-source-tree);
#   aleph is disabled (--disable-aleph) so the omegafonts blocker may be gone,
#   needs re-testing
# Conditional build:
%bcond_with	xindy		# do not build xindy packages
%bcond_with	luajittex	# LuaJITTeX (system luajit lacks lua_rawlen compat)


%define		year	2026
%define		monthday	0301
%define		texmfversion 20260301
Summary:	TeX typesetting system and MetaFont font formatter
Summary(de.UTF-8):	TeX-Satzherstellungssystem und MetaFont-Formatierung
Summary(es.UTF-8):	Sistema de typesetting TeX y formateador de fuentes MetaFont
Summary(fr.UTF-8):	Système de composition TeX et formatteur de MetaFontes
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
Source0:	https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/%{year}/%{name}-%{version}-source.tar.xz
# Source0-md5:	734e2521173e8ef6a4c04f70d1285124
Source4:	%{name}.cron
Source5:	xdvi.desktop
Source6:	xdvi.png
# Source6-md5:	1e412b0d19d41353a7966bbeba70be8d
URL:		https://www.tug.org/texlive/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
%if %{with xindy}
#BuildRequires:	clisp
%endif
BuildRequires:	cairo-devel
BuildRequires:	ed
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gd-devel
BuildRequires:	gmp-devel
BuildRequires:	graphite2-devel
BuildRequires:	harfbuzz-devel >= 2.6
BuildRequires:	harfbuzz-icu-devel
BuildRequires:	libpaper-devel
BuildRequires:	libpng-devel >= 1.2.8
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRequires:	lua53-devel
%{?with_luajittex:BuildRequires:	luajit-devel}
BuildRequires:	mpfi-devel
BuildRequires:	mpfr-devel
BuildRequires:	ncurses-devel
BuildRequires:	poppler-devel >= 22.0
BuildRequires:	pango-devel
BuildRequires:	potrace-devel
BuildRequires:	readline-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	unzip
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel >= 1.2.1
BuildRequires:	zziplib-devel >= 0.12
# Old texlive-dirs-fonts/fonts-misc/fonts-cm are now in texlive-texmf
# (texlive-cm and per-package subpackages)
Requires:	awk
Requires:	coreutils
Requires:	kpathsea = %{epoch}:%{version}-%{release}
Requires:	sed
Requires(post):	%{name}-texlive-scripts
Requires(post):	texlive-kpathsea
Suggests:	tmpwatch
Provides:	tetex = %{epoch}:%{version}-%{release}
Provides:	tetex-format-pdfetex = %{epoch}:%{version}-%{release}
Provides:	tetex-metafont
# Provides for packages needed by other PLD packages (xmlto, docbook-utils)
Provides:	xmltex = %{epoch}:%{version}-%{release}
Provides:	jadetex = %{epoch}:%{version}-%{release}
Provides:	passivetex = %{epoch}:%{version}-%{release}
# Provides for old subpackages now in texlive-texmf
Provides:	texlive-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-dirs-fonts = %{epoch}:%{version}-%{release}
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
Obsoletes:	tetex-fonts-cbgreek
Obsoletes:	tetex-fonts-dstroke
Obsoletes:	tetex-fonts-pazo
Obsoletes:	tetex-fonts-type1-dstroke
Obsoletes:	tetex-fonts-type1-qfonts
Obsoletes:	tetex-fonts-type1-tt2001
Obsoletes:	tetex-qfonts
# Packages removed in TL 2026
Obsoletes:	texlive-omega-basic < %{epoch}:%{version}
Obsoletes:	texlive-texdoctk < %{epoch}:%{version}
Obsoletes:	texlive-format-context-de < %{epoch}:%{version}
Obsoletes:	texlive-format-context-en < %{epoch}:%{version}
Obsoletes:	texlive-format-context-nl < %{epoch}:%{version}
Obsoletes:	texlive-tlmgr < %{epoch}:%{version}
Obsoletes:	texlive-cefutils < %{epoch}:%{version}
# Old zombie subpackages (moved to texlive-texmf or removed)
Obsoletes:	texconfig < %{epoch}:%{version}
Obsoletes:	texlive-latex-presentation-bin < %{epoch}:%{version}
Obsoletes:	texlive-metapost-other < %{epoch}:%{version}
Obsoletes:	texlive-other-utils-doc < %{epoch}:%{version}
# tetex compat from zombie subpackages
Obsoletes:	tetex-context
Obsoletes:	tetex-csplain
Obsoletes:	tetex-cyrplain
Obsoletes:	tetex-eplain
Obsoletes:	tetex-etex
Obsoletes:	tetex-format-amstex
Obsoletes:	tetex-format-cslatex
Obsoletes:	tetex-format-csplain
Obsoletes:	tetex-format-cyrplain
Obsoletes:	tetex-format-cyramstex
Obsoletes:	tetex-format-eplain
Obsoletes:	tetex-format-mex
Obsoletes:	tetex-format-pdfcslatex
Obsoletes:	tetex-format-pdfcsplain
Obsoletes:	tetex-format-pdfmex
Obsoletes:	tetex-format-plain
Obsoletes:	tetex-format-utf8mex
Obsoletes:	tetex-mex
Obsoletes:	tetex-mptopdf
Obsoletes:	tetex-plain
Obsoletes:	tetex-tex-babel
Obsoletes:	tetex-tex-thumbpdf
Provides:	tetex-context
Provides:	tetex-csplain
Provides:	tetex-format-plain
Provides:	tetex-plain
Provides:	tetex-tex-babel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texmf	%{_datadir}/texmf
%define		texmfdist %{texmf}-dist
%define		fmtdir	/var/lib/texmf/web2c
%define		texhash	umask 022; [ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2;
%define		_localstatedir	/var/lib/texmf
%define		fixinfodir [ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 ;

%define		_noautoreq 'perl(path_tre)'
%define		skip_post_check_so libptexenc.so.1

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
Summary:	Miscellaneous TeX Live utilities
Summary(pl.UTF-8):	Różne narzędzia TeX Live
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-format-cyrtexinfo

%description other-utils
Miscellaneous TeX Live utilities not categorized elsewhere, including
font manipulation and conversion tools, CJK encoding converters, and
source-output synchronization.

%description other-utils -l pl.UTF-8
Różne narzędzia TeX Live nie skategoryzowane gdzie indziej, w tym
narzędzia do manipulacji i konwersji fontów, konwertery kodowań CJK
oraz synchronizacja źródła z wyjściem.

%package -n kpathsea
Summary:	Path searching library for TeX-related files
Summary(hu.UTF-8):	Útvonal-kereső könyvtár TeX-hez kapcsolódó fájlokhoz
Summary(pl.UTF-8):	Biblioteka wyszukiwania ścieżek do plików związanych z TeXem
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kpathsea
Kpathsea is a library for path searching used by TeX and related
programs (METAFONT, BibTeX, dvips, etc.) to locate fonts, macros,
and other TeX-related files in the texmf directory trees.

%description -n kpathsea -l hu.UTF-8
A Kpathsea egy útvonal-kereső könyvtár, amelyet a TeX és kapcsolódó
programok (METAFONT, BibTeX, dvips stb.) használnak a fontok, makrók
és egyéb TeX-hez kapcsolódó fájlok megtalálásához a texmf
könyvtárfákban.

%description -n kpathsea -l pl.UTF-8
Kpathsea to biblioteka wyszukiwania ścieżek używana przez TeXa i
powiązane programy (METAFONT, BibTeX, dvips itp.) do lokalizowania
fontów, makr i innych plików związanych z TeXem w drzewach
katalogów texmf.

%package -n kpathsea-devel
Summary:	Kpathsea library filename lookup header files and documentation
Summary(es.UTF-8):	Bibliotecas y archivos de inclusión para desarrollo TeX
Summary(hu.UTF-8):	Kpathsea fájlnév-kereső könyvtár header fájljai és dokumentációja
Summary(pl.UTF-8):	Pliki nagłówkowe oraz dokumentacja kpathsea
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

%package dvips-basic
Summary:	DVI to PostScript converter
Summary(de.UTF-8):	dvi-Postscript-Konvertierungsprogramm
Summary(es.UTF-8):	Convertidor dvi para postscript
Summary(fr.UTF-8):	Convertisseur dvi vers PostScript
Summary(hu.UTF-8):	DVI-ből PostScript-be konvertáló
Summary(pl.UTF-8):	Konwerter plików DVI do PostScriptu
Summary(pt_BR.UTF-8):	Conversor dvi para postscript
Summary(tr.UTF-8):	dvi'dan postscript'e dönüştürücü
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description dvips-basic
The program dvips takes a DVI file file[.dvi] produced by TeX (or by
some other processor such as GFtoDVI) and converts it to PostScript,
normally sending the result directly to the laserprinter.

%description dvips-basic -l de.UTF-8
Das dvips-Programm nimmt eine dvi-Datei ([.dvi]), die von TeX bzw.
durch einen anderen Prozessor wie GFtoDVI) erzeugt wurde, und
konvertiert diese in PostScript, wobei das Ergebnis in der Regel
direkt an einen Laserdrucker gesandt wird.

%description dvips-basic -l es.UTF-8
El programa dvips coge un archivo DVI (.dvi) producido por TeX (o por
otro procesador como GFtoDVI) y lo convierte a PostScript, normalmente
enviando el resultado directamente a la impresora láser.

%description dvips-basic -l fr.UTF-8
Le programme dvips convertit les fichiers DVI en PostScript, en
envoyant normalement le résultat directement sur une imprimante Laser.

%description dvips-basic -l hu.UTF-8
A dvips program egy TeX által készített DVI-fájlból PostScript
állományt készít, amelyet a legtöbb esetben közvetlenül a
lézernyomtatóra küldhetsz.

%description dvips-basic -l pl.UTF-8
Program dvips bierze plik DVI wygenerowany przez TeXa (lub jakiś inny
program, jak na przykład GFtoDVI) i konwertuje go do PostScriptu.
Domyślnie wynik jest wysyłany bezpośrednio do drukarki.

%description dvips-basic -l pt_BR.UTF-8
O programa dvips toma um arquivo DVI (.dvi) produzido pelo TeX (ou por
outro processador como o GFtoDVI) e o converte para PostScript,
normalmente enviando o resultado diretamente para a impressora laser.

%description dvips-basic -l tr.UTF-8
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
Summary:	MetaPost - a tool for creating technical diagrams and figures
Summary(hu.UTF-8):	MetaPost - műszaki ábrák és diagramok készítéséhez
Summary(pl.UTF-8):	MetaPost - narzędzie do tworzenia diagramów i rysunków technicznych
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-metapost-data >= %{epoch}:%{texmfversion}
Obsoletes:	tetex-metapost

%description metapost
MetaPost is a programming language for creating technical diagrams and
figures. It uses a system of equations to describe geometric
relationships and produces PostScript or SVG output suitable for
inclusion in TeX documents.

%description metapost -l hu.UTF-8
A MetaPost egy programozási nyelv műszaki ábrák és diagramok
készítéséhez. Egyenletrendszerekkel írja le a geometriai
összefüggéseket, és PostScript vagy SVG kimenetet készít, amely
beilleszthető TeX dokumentumokba.

%description metapost -l pl.UTF-8
MetaPost to język programowania do tworzenia diagramów i rysunków
technicznych. Używa układu równań do opisu zależności geometrycznych
i generuje pliki PostScript lub SVG, które można włączać do
dokumentów TeXowych.

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
Summary(pl.UTF-8):	Xindy - tworzenie posortowanego i otagowanego indeksu z surowego indeksu
Group:		Applications/Publishing/TeX

%description -n xindy
Xindy creates sorted and tagged index from raw index.

%description -n xindy -l hu.UTF-8
Xindy rendezett és cimkézett indexet készít nyers indexekből.

%description -n xindy -l pl.UTF-8
Xindy tworzy posortowany i otagowany indeks z surowego indeksu.

%package -n xindy-albanian
Summary:	Xindy albanian language
Summary(hu.UTF-8):	Xindy albán nyelv
Summary(pl.UTF-8):	Xindy - język albański
Group:		Applications/Publishing/TeX

%description -n xindy-albanian
Xindy albanian language

%description -n xindy-albanian -l hu.UTF-8
Xindy albán nyelv

%description -n xindy-albanian -l pl.UTF-8
Xindy - język albański.

%package -n xindy-belarusian
Summary:	Xindy belarusian language
Summary(hu.UTF-8):	Xindy belorusz nyelv
Summary(pl.UTF-8):	Xindy - język białoruski
Group:		Applications/Publishing/TeX

%description -n xindy-belarusian
Xindy belarusian language

%description -n xindy-belarusian -l hu.UTF-8
Xindy belorusz nyelv

%description -n xindy-belarusian -l pl.UTF-8
Xindy - język białoruski.

%package -n xindy-bulgarian
Summary:	Xindy bulgarian language
Summary(hu.UTF-8):	Xindy bolgár nyelv
Summary(pl.UTF-8):	Xindy - język bułgarski
Group:		Applications/Publishing/TeX

%description -n xindy-bulgarian
Xindy bulgarian language

%description -n xindy-bulgarian -l hu.UTF-8
Xindy bolgár nyelv

%description -n xindy-bulgarian -l pl.UTF-8
Xindy - język bułgarski.

%package -n xindy-croatian
Summary:	Xindy croatian language
Summary(hu.UTF-8):	Xindy horvát nyelv
Summary(pl.UTF-8):	Xindy - język chorwacki
Group:		Applications/Publishing/TeX

%description -n xindy-croatian
Xindy croatian language

%description -n xindy-croatian -l hu.UTF-8
Xindy horvát nyelv

%description -n xindy-croatian -l pl.UTF-8
Xindy - język chorwacki.

%package -n xindy-czech
Summary:	Xindy czech language
Summary(hu.UTF-8):	Xindy cseh nyelv
Summary(pl.UTF-8):	Xindy - język czeski
Group:		Applications/Publishing/TeX

%description -n xindy-czech
Xindy czech language

%description -n xindy-czech -l hu.UTF-8
Xindy cseh nyelv

%description -n xindy-czech -l pl.UTF-8
Xindy - język czeski.

%package -n xindy-danish
Summary:	Xindy danish language
Summary(hu.UTF-8):	Xindy dán nyelv
Summary(pl.UTF-8):	Xindy - język duński
Group:		Applications/Publishing/TeX

%description -n xindy-danish
Xindy danish language

%description -n xindy-danish -l hu.UTF-8
Xindy dán nyelv

%description -n xindy-danish -l pl.UTF-8
Xindy - język duński.

%package -n xindy-dutch
Summary:	Xindy dutch language
Summary(hu.UTF-8):	Xindy holland nyelv
Summary(pl.UTF-8):	Xindy - język holenderski
Group:		Applications/Publishing/TeX

%description -n xindy-dutch
Xindy dutch language

%description -n xindy-dutch -l hu.UTF-8
Xindy holland nyelv

%description -n xindy-dutch -l pl.UTF-8
Xindy - język holenderski.

%package -n xindy-english
Summary:	Xindy english language
Summary(hu.UTF-8):	Xindy angol nyelv
Summary(pl.UTF-8):	Xindy - język angielski
Group:		Applications/Publishing/TeX

%description -n xindy-english
Xindy english language

%description -n xindy-english -l hu.UTF-8
Xindy angol nyelv

%description -n xindy-english -l pl.UTF-8
Xindy - język angielski.

%package -n xindy-esperanto
Summary:	Xindy esperanto language
Summary(hu.UTF-8):	Xindy eszperantó nyelv
Summary(pl.UTF-8):	Xindy - język esperanto
Group:		Applications/Publishing/TeX

%description -n xindy-esperanto
Xindy esperanto language

%description -n xindy-esperanto -l hu.UTF-8
Xindy eszperantó nyelv

%description -n xindy-esperanto -l pl.UTF-8
Xindy - język esperanto.

%package -n xindy-estonian
Summary:	Xindy estonian language
Summary(hu.UTF-8):	Xindy észt nyelv
Summary(pl.UTF-8):	Xindy - język estoński
Group:		Applications/Publishing/TeX

%description -n xindy-estonian
Xindy estonian language

%description -n xindy-estonian -l hu.UTF-8
Xindy észt nyelv

%description -n xindy-estonian -l pl.UTF-8
Xindy - język estoński.

%package -n xindy-finnish
Summary:	Xindy finnish language
Summary(hu.UTF-8):	Xindy finn nyelv
Summary(pl.UTF-8):	Xindy - język fiński
Group:		Applications/Publishing/TeX

%description -n xindy-finnish
Xindy finnish language

%description -n xindy-finnish -l hu.UTF-8
Xindy finn nyelv

%description -n xindy-finnish -l pl.UTF-8
Xindy - język fiński.

%package -n xindy-french
Summary:	Xindy french language
Summary(hu.UTF-8):	Xindy francia nyelv
Summary(pl.UTF-8):	Xindy - język francuski
Group:		Applications/Publishing/TeX

%description -n xindy-french
Xindy french language

%description -n xindy-french -l hu.UTF-8
Xindy francia nyelv

%description -n xindy-french -l pl.UTF-8
Xindy - język francuski.

%package -n xindy-general
Summary:	Xindy general language
Summary(hu.UTF-8):	Xindy általános nyelv
Summary(pl.UTF-8):	Xindy - obsługa ogólna
Group:		Applications/Publishing/TeX

%description -n xindy-general
Xindy general language

%description -n xindy-general -l hu.UTF-8
Xindy általános nyelv

%description -n xindy-general -l pl.UTF-8
Xindy - obsługa ogólna.

%package -n xindy-georgian
Summary:	Xindy georgian language
Summary(hu.UTF-8):	Xindy georgian nyelv
Summary(pl.UTF-8):	Xindy - język gruziński
Group:		Applications/Publishing/TeX

%description -n xindy-georgian
Xindy georgian language

%description -n xindy-georgian -l hu.UTF-8
Xindy georgian nyelv

%description -n xindy-georgian -l pl.UTF-8
Xindy - język gruziński.

%package -n xindy-german
Summary:	Xindy german language
Summary(hu.UTF-8):	Xindy német nyelv
Summary(pl.UTF-8):	Xindy - język niemiecki
Group:		Applications/Publishing/TeX

%description -n xindy-german
Xindy german language

%description -n xindy-german -l hu.UTF-8
Xindy német nyelv

%description -n xindy-german -l pl.UTF-8
Xindy - język niemiecki.

%package -n xindy-greek
Summary:	Xindy greek language
Summary(hu.UTF-8):	Xindy görög nyelv
Summary(pl.UTF-8):	Xindy - język grecki
Group:		Applications/Publishing/TeX

%description -n xindy-greek
Xindy greek language

%description -n xindy-greek -l hu.UTF-8
Xindy görög nyelv

%description -n xindy-greek -l pl.UTF-8
Xindy - język grecki.

%package -n xindy-gypsy
Summary:	Xindy gypsy language
Summary(hu.UTF-8):	Xindy cigány nyelv
Summary(pl.UTF-8):	Xindy - język cygański
Group:		Applications/Publishing/TeX

%description -n xindy-gypsy
Xindy gypsy language

%description -n xindy-gypsy -l hu.UTF-8
Xindy cigány nyelv

%description -n xindy-gypsy -l pl.UTF-8
Xindy - język cygański.

%package -n xindy-hausa
Summary:	Xindy hausa language
Summary(hu.UTF-8):	Xindy hausa nyelv
Summary(pl.UTF-8):	Xindy - język hausa
Group:		Applications/Publishing/TeX

%description -n xindy-hausa
Xindy hausa language

%description -n xindy-hausa -l hu.UTF-8
Xindy hausa nyelv

%description -n xindy-hausa -l pl.UTF-8
Xindy - język hausa.

%package -n xindy-hebrew
Summary:	Xindy hebrew language
Summary(hu.UTF-8):	Xindy héber nyelv
Summary(pl.UTF-8):	Xindy - język hebrajski
Group:		Applications/Publishing/TeX

%description -n xindy-hebrew
Xindy hebrew language

%description -n xindy-hebrew -l hu.UTF-8
Xindy héber nyelv

%description -n xindy-hebrew -l pl.UTF-8
Xindy - język hebrajski.

%package -n xindy-hungarian
Summary:	Xindy hungarian language
Summary(hu.UTF-8):	Xindy magyar nyelv
Summary(pl.UTF-8):	Xindy - język węgierski
Group:		Applications/Publishing/TeX

%description -n xindy-hungarian
Xindy hungarian language

%description -n xindy-hungarian -l hu.UTF-8
Xindy magyar nyelv

%description -n xindy-hungarian -l pl.UTF-8
Xindy - język węgierski.

%package -n xindy-icelandic
Summary:	Xindy icelandic language
Summary(hu.UTF-8):	Xindy izlandi nyelv
Summary(pl.UTF-8):	Xindy - język islandzki
Group:		Applications/Publishing/TeX

%description -n xindy-icelandic
Xindy icelandic language

%description -n xindy-icelandic -l hu.UTF-8
Xindy izlandi nyelv

%description -n xindy-icelandic -l pl.UTF-8
Xindy - język islandzki.

%package -n xindy-italian
Summary:	Xindy italian language
Summary(hu.UTF-8):	Xindy olasz nyelv
Summary(pl.UTF-8):	Xindy - język włoski
Group:		Applications/Publishing/TeX

%description -n xindy-italian
Xindy italian language

%description -n xindy-italian -l hu.UTF-8
Xindy olasz nyelv

%description -n xindy-italian -l pl.UTF-8
Xindy - język włoski.

%package -n xindy-klingon
Summary:	Xindy klingon language
Summary(hu.UTF-8):	Xindy klingon nyelv
Summary(pl.UTF-8):	Xindy - język klingoński
Group:		Applications/Publishing/TeX

%description -n xindy-klingon
Xindy klingon language

%description -n xindy-klingon -l hu.UTF-8
Xindy klingon nyelv

%description -n xindy-klingon -l pl.UTF-8
Xindy - język klingoński.

%package -n xindy-kurdish
Summary:	Xindy kurdish language
Summary(hu.UTF-8):	Xindy kurd nyelv
Summary(pl.UTF-8):	Xindy - język kurdyjski
Group:		Applications/Publishing/TeX

%description -n xindy-kurdish
Xindy kurdish language

%description -n xindy-kurdish -l hu.UTF-8
Xindy kurd nyelv

%description -n xindy-kurdish -l pl.UTF-8
Xindy - język kurdyjski.

%package -n xindy-latin
Summary:	Xindy latin language
Summary(hu.UTF-8):	Xindy latin nyelv
Summary(pl.UTF-8):	Xindy - język łaciński
Group:		Applications/Publishing/TeX

%description -n xindy-latin
Xindy latin language

%description -n xindy-latin -l hu.UTF-8
Xindy latin nyelv

%description -n xindy-latin -l pl.UTF-8
Xindy - język łaciński.

%package -n xindy-latvian
Summary:	Xindy latvian language
Summary(hu.UTF-8):	Xindy lett nyelv
Summary(pl.UTF-8):	Xindy - język łotewski
Group:		Applications/Publishing/TeX

%description -n xindy-latvian
Xindy latvian language

%description -n xindy-latvian -l hu.UTF-8
Xindy lett nyelv

%description -n xindy-latvian -l pl.UTF-8
Xindy - język łotewski.

%package -n xindy-lithuanian
Summary:	Xindy lithuanian language
Summary(hu.UTF-8):	Xindy litván nyelv
Summary(pl.UTF-8):	Xindy - język litewski
Group:		Applications/Publishing/TeX

%description -n xindy-lithuanian
Xindy lithuanian language

%description -n xindy-lithuanian -l hu.UTF-8
Xindy litván nyelv

%description -n xindy-lithuanian -l pl.UTF-8
Xindy - język litewski.

%package -n xindy-lower-sorbian
Summary:	Xindy lower-sorbian language
Summary(hu.UTF-8):	Xindy lower-sorbian nyelv
Summary(pl.UTF-8):	Xindy - język dolnołużycki
Group:		Applications/Publishing/TeX

%description -n xindy-lower-sorbian
Xindy lower-sorbian language

%description -n xindy-lower-sorbian -l hu.UTF-8
Xindy lower-sorbian nyelv

%description -n xindy-lower-sorbian -l pl.UTF-8
Xindy - język dolnołużycki.

%package -n xindy-macedonian
Summary:	Xindy macedonian language
Summary(hu.UTF-8):	Xindy macedón nyelv
Summary(pl.UTF-8):	Xindy - język macedoński
Group:		Applications/Publishing/TeX

%description -n xindy-macedonian
Xindy macedonian language

%description -n xindy-macedonian -l hu.UTF-8
Xindy macedón nyelv

%description -n xindy-macedonian -l pl.UTF-8
Xindy - język macedoński.

%package -n xindy-mongolian
Summary:	Xindy mongolian language
Summary(hu.UTF-8):	Xindy mongol nyelv
Summary(pl.UTF-8):	Xindy - język mongolski
Group:		Applications/Publishing/TeX

%description -n xindy-mongolian
Xindy mongolian language

%description -n xindy-mongolian -l hu.UTF-8
Xindy mongol nyelv

%description -n xindy-mongolian -l pl.UTF-8
Xindy - język mongolski.

%package -n xindy-norwegian
Summary:	Xindy norwegian language
Summary(hu.UTF-8):	Xindy norvég nyelv
Summary(pl.UTF-8):	Xindy - język norweski
Group:		Applications/Publishing/TeX

%description -n xindy-norwegian
Xindy norwegian language

%description -n xindy-norwegian -l hu.UTF-8
Xindy norvég nyelv

%description -n xindy-norwegian -l pl.UTF-8
Xindy - język norweski.

%package -n xindy-polish
Summary:	Xindy polish language
Summary(hu.UTF-8):	Xindy lengyel nyelv
Summary(pl.UTF-8):	Xindy - język polski
Group:		Applications/Publishing/TeX

%description -n xindy-polish
Xindy polish language

%description -n xindy-polish -l hu.UTF-8
Xindy lengyel nyelv

%description -n xindy-polish -l pl.UTF-8
Xindy - język polski.

%package -n xindy-portuguese
Summary:	Xindy portuguese language
Summary(hu.UTF-8):	Xindy portugál nyelv
Summary(pl.UTF-8):	Xindy - język portugalski
Group:		Applications/Publishing/TeX

%description -n xindy-portuguese
Xindy portuguese language

%description -n xindy-portuguese -l hu.UTF-8
Xindy portugál nyelv

%description -n xindy-portuguese -l pl.UTF-8
Xindy - język portugalski.

%package -n xindy-romanian
Summary:	Xindy romanian language
Summary(hu.UTF-8):	Xindy román nyelv
Summary(pl.UTF-8):	Xindy - język rumuński
Group:		Applications/Publishing/TeX

%description -n xindy-romanian
Xindy romanian language

%description -n xindy-romanian -l hu.UTF-8
Xindy román nyelv

%description -n xindy-romanian -l pl.UTF-8
Xindy - język rumuński.

%package -n xindy-russian
Summary:	Xindy russian language
Summary(hu.UTF-8):	Xindy orosz nyelv
Summary(pl.UTF-8):	Xindy - język rosyjski
Group:		Applications/Publishing/TeX

%description -n xindy-russian
Xindy russian language

%description -n xindy-russian -l hu.UTF-8
Xindy orosz nyelv

%description -n xindy-russian -l pl.UTF-8
Xindy - język rosyjski.

%package -n xindy-serbian
Summary:	Xindy serbian language
Summary(hu.UTF-8):	Xindy szerb nyelv
Summary(pl.UTF-8):	Xindy - język serbski
Group:		Applications/Publishing/TeX

%description -n xindy-serbian
Xindy serbian language

%description -n xindy-serbian -l hu.UTF-8
Xindy szerb nyelv

%description -n xindy-serbian -l pl.UTF-8
Xindy - język serbski.

%package -n xindy-slovak
Summary:	Xindy slovak language
Summary(hu.UTF-8):	Xindy szlovák nyelv
Summary(pl.UTF-8):	Xindy - język słowacki
Group:		Applications/Publishing/TeX

%description -n xindy-slovak
Xindy slovak language

%description -n xindy-slovak -l hu.UTF-8
Xindy szlovák nyelv

%description -n xindy-slovak -l pl.UTF-8
Xindy - język słowacki.

%package -n xindy-slovenian
Summary:	Xindy slovenian language
Summary(hu.UTF-8):	Xindy szlovén nyelv
Summary(pl.UTF-8):	Xindy - język słoweński
Group:		Applications/Publishing/TeX

%description -n xindy-slovenian
Xindy slovenian language

%description -n xindy-slovenian -l hu.UTF-8
Xindy szlovén nyelv

%description -n xindy-slovenian -l pl.UTF-8
Xindy - język słoweński.

%package -n xindy-spanish
Summary:	Xindy spanish language
Summary(hu.UTF-8):	Xindy spanyol nyelv
Summary(pl.UTF-8):	Xindy - język hiszpański
Group:		Applications/Publishing/TeX

%description -n xindy-spanish
Xindy spanish language

%description -n xindy-spanish -l hu.UTF-8
Xindy spanyol nyelv

%description -n xindy-spanish -l pl.UTF-8
Xindy - język hiszpański.

%package -n xindy-swedish
Summary:	Xindy swedish language
Summary(hu.UTF-8):	Xindy svéd nyelv
Summary(pl.UTF-8):	Xindy - język szwedzki
Group:		Applications/Publishing/TeX

%description -n xindy-swedish
Xindy swedish language

%description -n xindy-swedish -l hu.UTF-8
Xindy svéd nyelv

%description -n xindy-swedish -l pl.UTF-8
Xindy - język szwedzki.

%package -n xindy-turkish
Summary:	Xindy turkish language
Summary(hu.UTF-8):	Xindy török nyelv
Summary(pl.UTF-8):	Xindy - język turecki
Group:		Applications/Publishing/TeX

%description -n xindy-turkish
Xindy turkish language

%description -n xindy-turkish -l hu.UTF-8
Xindy török nyelv

%description -n xindy-turkish -l pl.UTF-8
Xindy - język turecki.

%package -n xindy-ukrainian
Summary:	Xindy ukrainian language
Summary(hu.UTF-8):	Xindy ukrán nyelv
Summary(pl.UTF-8):	Xindy - język ukraiński
Group:		Applications/Publishing/TeX

%description -n xindy-ukrainian
Xindy ukrainian language

%description -n xindy-ukrainian -l hu.UTF-8
Xindy ukrán nyelv

%description -n xindy-ukrainian -l pl.UTF-8
Xindy - język ukraiński.

%package -n xindy-upper-sorbian
Summary:	Xindy upper-sorbian language
Summary(hu.UTF-8):	Xindy upper-sorbian nyelv
Summary(pl.UTF-8):	Xindy - język górnołużycki
Group:		Applications/Publishing/TeX

%description -n xindy-upper-sorbian
Xindy upper-sorbian language

%description -n xindy-upper-sorbian -l hu.UTF-8
Xindy upper-sorbian nyelv

%description -n xindy-upper-sorbian -l pl.UTF-8
Xindy - język górnołużycki.

%package -n xindy-vietnamese
Summary:	Xindy vietnamese language
Summary(hu.UTF-8):	Xindy vietnámi nyelv
Summary(pl.UTF-8):	Xindy - język wietnamski
Group:		Applications/Publishing/TeX

%description -n xindy-vietnamese
Xindy vietnamese language

%description -n xindy-vietnamese -l hu.UTF-8
Xindy vietnám nyelv

%description -n xindy-vietnamese -l pl.UTF-8
Xindy - język wietnamski.

%package pdftex
Summary:	pdfTeX - TeX engine with direct PDF output
Summary(hu.UTF-8):	pdfTeX - TeX motor közvetlen PDF kimenettel
Summary(pl.UTF-8):	pdfTeX - silnik TeX z bezpośrednim wyjściem PDF
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex-data >= %{epoch}:%{texmfversion}
Requires(post):	%{name}-texlive-scripts
Requires(post):	texlive-kpathsea
# ams provides bluesky fonts
Requires:	%{name}-amsfonts >= %{epoch}:%{texmfversion}
Requires:	ghostscript
Provides:	tetex-format-pdftex = %{epoch}:%{version}-%{release}
Provides:	tetex-pdftex
Obsoletes:	tetex-format-pdftex
Obsoletes:	tetex-pdftex

%description pdftex
pdfTeX is an extension of TeX that can create PDF output directly
(instead of DVI), including support for microtypographic extensions,
PDF hyperlinks, and inclusion of JPEG, PNG, and PDF images.

%description pdftex -l pl.UTF-8
pdfTeX to rozszerzenie TeXa, które potrafi bezpośrednio tworzyć pliki
PDF (zamiast DVI), z obsługą rozszerzeń mikrotypograficznych,
hiperłączy PDF oraz włączania obrazów JPEG, PNG i PDF.

%package psutils
Summary:	PostScript Utilities
Summary(hu.UTF-8):	PostScript eszközök
Summary(pl.UTF-8):	Narzędzia do PostScriptu
Group:		Applications/Printing
Requires:	%{name}-psutils-data
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

%package latex
Summary:	LaTeX macro package basic files
Summary(pl.UTF-8):	Podstawowe pliki pakietu makr LaTeX
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-data >= %{epoch}:%{texmfversion}
Requires(post):	%{name}-texlive-scripts
Requires(post):	texlive-kpathsea
# for misc/eurosym:
Requires:	%{name}-pdftex
Suggests:	%{name}-jknapltx
Suggests:	%{name}-ucs
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
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-bibtex
Obsoletes:	tetex-bibtex
Obsoletes:	tetex-latex-bibtex
Obsoletes:	tetex-natbib
Obsoletes:	tetex-rubibtex

%description latex-bibtex
Bibliography management for LaTeX.

%description latex-bibtex -l pl.UTF-8
Zarządzanie bibliografią dla LaTeXa.

%package format-pdflatex
Summary:	PDF LaTeX macro package
Summary(pl.UTF-8):	Pakiet makr PDF LaTeX
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-jknapltx
Requires:	%{name}-collection-fontsrecommended
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Provides:	tetex-format-pdflatex
Obsoletes:	tetex-format-pdflatex
# Force arch transition from old noarch to x86_64
Obsoletes:	texlive-format-pdflatex < %{epoch}:%{version}
Requires(post):	%{name}-texlive-scripts

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
Summary:	TeX Live helper scripts
Summary(hu.UTF-8):	TeX Live segédszkriptek
Summary(pl.UTF-8):	Skrypty pomocnicze TeX Live
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description scripts
TeX Live helper scripts for font pre-generation, format conversion,
and font installation support.

%description scripts -l hu.UTF-8
TeX Live segédszkriptek fontok előgenerálásához, formátumkonverzióhoz
és fonttelepítéshez.

%description scripts -l pl.UTF-8
Skrypty pomocnicze TeX Live do wstępnego generowania fontów, konwersji
formatów i wspomagania instalacji fontów.

%package font-utils
Summary:	Type1 and TrueType font utilities
Summary(pl.UTF-8):	Narzędzia do fontów Type1 i TrueType
Group:		Fonts

%description font-utils
Utilities for manipulating Type1 and TrueType fonts, including
PFB/PFA conversion tools and TrueType font table inspection.

%description font-utils -l pl.UTF-8
Narzędzia do manipulacji fontami Type1 i TrueType, w tym narzędzia do
konwersji PFB/PFA oraz inspekcji tabel fontów TrueType.

%package bbox
Summary:	bbox prints the bounding box of images
Summary(pl.UTF-8):	bbox wypisuje bounding box obrazów
Group:		Applications/Publishing/TeX

%description bbox
bbox reads a rawppm or rawpbm file and prints out the bounding box of
the image.

%description bbox -l pl.UTF-8
bbox czyta plik rawppm lub rawpbm i wypisuje bounding box obrazu.

%package detex
Summary:	A filter to strip TeX commands from a .tex file
Summary(hu.UTF-8):	Egy szűrő, amely .tex fájlokból szűri ki a TeX parancsokat
Summary(pl.UTF-8):	Filtr usuwający polecenia TeXa z pliku .tex
Group:		Applications/Publishing/TeX
Requires:	%{name}-detex-data

%description detex
A filter to strip TeX commands from a .tex file.

%description detex -l hu.UTF-8
Egy szűrő, amely .tex fájlokból szűri ki a TeX parancsokat.

%description detex -l pl.UTF-8
Filtr usuwający polecenia TeXa z pliku .tex.

%package dviutils
Summary:	Various DVI utils
Summary(hu.UTF-8):	Vegyes DVI eszközök
Summary(pl.UTF-8):	Różne narzędzia DVI
Group:		Applications/Publishing/TeX
Provides:	dvi2tty
Obsoletes:	dvi2tty

%description dviutils
Utilities for manipulating DVI files: conversion to text, rearranging
pages, concatenating files, converting to PDF/GIF, and other DVI
transformations.

%description dviutils -l hu.UTF-8
DVI fájlok kezelésére szolgáló eszközök: szöveggé konvertálás, oldalak
átrendezése, fájlok összefűzése, PDF/GIF konverzió és egyéb DVI
átalakítások.

%description dviutils -l pl.UTF-8
Narzędzia do manipulacji plikami DVI: konwersja na tekst,
zmiana kolejności stron, łączenie plików, konwersja do PDF/GIF i inne
przekształcenia DVI.

%package uncategorized-utils
Summary:	Additional TeX Live utilities
Summary(pl.UTF-8):	Dodatkowe narzędzia TeX Live
Group:		Applications/Publishing/TeX

%description uncategorized-utils
Additional TeX Live utilities not fitting in other subpackages.

%description uncategorized-utils -l pl.UTF-8
Dodatkowe narzędzia TeX Live nie pasujące do innych podpakietów.

%package tex4ht
Summary:	LaTeX and TeX for hypertext
Summary(pl.UTF-8):	LaTeX i TeX do hipertekstu
Group:		Applications/Publishing/TeX
Requires:	%{name}-tex4ht-data

%description tex4ht
A converter from TeX and LaTeX to hypertext (HTML, XML, etc.),
providing a configurable (La)TeX-based authoring system for hypertext.
When converting to XML, you can use MathML instead of images for
equation representation.

%description tex4ht -l pl.UTF-8
Konwerter z TeXa i LaTeXa do hipertekstu (HTML, XML itp.),
udostępniający konfigurowalny system autorski oparty na (La)TeXu.
Przy konwersji do XML można użyć MathML zamiast obrazów do
reprezentacji równań.

%package xetex
Summary:	Extended TeX / LaTeX version for unicode
Summary(pl.UTF-8):	Rozszerzona wersja TeXa/LaTeXa z obsługą Unicode
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-xetex-data >= %{epoch}:%{texmfversion}
Requires(post):	%{name}-texlive-scripts
Requires(post):	texlive-kpathsea
Requires(post,postun):	/usr/bin/texhash

%description xetex
XeTeX extends the TeX typesetting system (and macro packages such as
LaTeX and ConTeXt) to have native support for the Unicode character
set, including complex Asian scripts, and for OpenType and TrueType
fonts.

%description xetex -l pl.UTF-8
XeTeX rozszerza system składu TeX (oraz pakiety makr takie jak LaTeX
i ConTeXt) o natywną obsługę zestawu znaków Unicode, w tym złożonych
pism azjatyckich, oraz fontów OpenType i TrueType.

%package luatex
Summary:	LuaTeX - TeX engine with embedded Lua scripting
Summary(pl.UTF-8):	LuaTeX - silnik TeX z wbudowanym skryptowaniem Lua
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-luatex-data >= %{epoch}:%{texmfversion}
Requires(post):	%{name}-texlive-scripts
Requires(post):	texlive-kpathsea
Requires:	kpathsea = %{epoch}:%{version}-%{release}

%description luatex
LuaTeX is an extended version of pdfTeX using Lua as an embedded
scripting language. It provides access to the internals of the TeX
engine, allowing programmatic control of typesetting. LuaHBTeX adds
HarfBuzz support for OpenType font shaping.

%description luatex -l pl.UTF-8
LuaTeX to rozszerzona wersja pdfTeX z wbudowanym językiem
skryptowym Lua. Zapewnia dostęp do mechanizmów silnika TeX,
pozwalając na programistyczną kontrolę składu. LuaHBTeX dodaje
obsługę HarfBuzz do kształtowania fontów OpenType.

%prep
%setup -q -n %{name}-%{version}-source

%build
%{__sed} -i 's@"extend/\(.*\)"@<\1>@' texk/ttf2pk2/*.c

# Set texmf paths in kpathsea's texmf.cnf to match PLD filesystem layout
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
# clisp (used by xindy) needs unlimited stack on ppc/ppc64
ulimit -s unlimited
%endif

export CPPFLAGS="%{rpmcppflags} -DHAVE_PROTOTYPES"

%configure \
	--enable-build-in-source-tree \
	%{__enable_disable xindy} \
	--enable-shared \
	--disable-native-texlive-build \
	--disable-static \
	--enable-ipc \
	--enable-luatex \
	--enable-luahbtex \
	%{!?with_luajittex:--disable-luajittex} \
	%{!?with_luajittex:--disable-luajithbtex} \
	%{?with_luajittex:--with-system-luajit} \
	--enable-uptex \
	--disable-aleph \
	--disable-t1utils \
	--disable-texdoctk \
	--with-system-freetype2 \
	--with-system-gd \
	--with-system-libpng \
	--with-system-zlib \
	--with-system-harfbuzz \
	--with-system-icu \
	--with-system-graphite2 \
	--with-system-zziplib \
	--with-system-poppler \
	--with-system-cairo \
	--with-system-pixman \
	--with-system-mpfr \
	--with-system-gmp \
	--with-system-mpfi \
	--with-system-lua \
	--with-system-libpaper \
	--with-system-potrace \
	--with-xdvi-x-toolkit=xaw
%{__make}

# Ensure generated/intermediate sources exist for debuginfo extraction.
# debuginfo runs from the source dir; paths are relative to there.
for f in \
	libs/luajit/buildvm_x86.dasc \
	texk/cjkutils/cjkutils-src/Bg5conv/bg5conv.w \
	texk/cjkutils/cjkutils-src/CEFconv/cef5conv.w \
	texk/cjkutils/cjkutils-src/CEFconv/cefconv.w \
	texk/cjkutils/cjkutils-src/CEFconv/cefsconv.w \
	texk/cjkutils/cjkutils-src/SJISconv/sjisconv.w \
	texk/cjkutils/cjkutils-src/extconv/extconv.w \
	texk/cjkutils/cjkutils-src/hbf2gf/hbf2gf.w \
	texk/gregorio/gabc/gabc-notes-determination-l.c \
	texk/gregorio/gabc/gabc-notes-determination.l \
	texk/gregorio/gabc/gabc-score-determination-l.c \
	texk/gregorio/gabc/gabc-score-determination-l.h \
	texk/gregorio/gabc/gabc-score-determination-y.c \
	texk/gregorio/gabc/gabc-score-determination.l \
	texk/gregorio/gabc/gabc-score-determination.y \
	texk/gregorio/vowel/vowel-rules-l.c \
	texk/gregorio/vowel/vowel-rules-y.c \
	texk/gregorio/vowel/vowel-rules.l \
	texk/gregorio/vowel/vowel-rules.y \
	texk/tex4htk/tex4ht-c.tex \
	texk/tex4htk/tex4ht-t4ht.tex \
	texk/web2c/format.w \
	texk/web2c/hiparser.h \
	texk/web2c/lexer.c \
	texk/web2c/lexer.l \
	texk/web2c/omegafonts/pl-lexer.c \
	texk/web2c/parser.c \
	utils/vlna/vlna.w \
	; do
	[ -f "$f" ] || { install -d "$(dirname "$f")" && touch "$f"; }
done

%install
install -d $RPM_BUILD_ROOT%{_datadir} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_mandir}/man5 \
	$RPM_BUILD_ROOT/var/cache/fonts \
	$RPM_BUILD_ROOT/etc/cron.daily\
	$RPM_BUILD_ROOT%{_localstatedir}/fonts/map\
	$RPM_BUILD_ROOT%{fmtdir}/pdftex

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}; export LD_LIBRARY_PATH
PATH=$RPM_BUILD_ROOT%{_bindir}:$PATH; export PATH

# TL's build system doesn't fully support DESTDIR; override paths explicitly
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
	texmfsysconfig=$RPM_BUILD_ROOT%{texmf} \
	encdir=$RPM_BUILD_ROOT%{texmfdist}/fonts/enc/dvips/base \
	glyphlistdir=$RPM_BUILD_ROOT%{texmfdist}/fonts/map/glyphlist


# Engine symlinks (ELF binary aliases)
cd $RPM_BUILD_ROOT%{_bindir}
ln -s pdftex latex
ln -s pdftex pdflatex
ln -s luahbtex lualatex
ln -s xetex xelatex
cd -

# Script-based tool symlinks (/usr/bin/foo -> scripts/foo.pl) are created
# by the texlive-texmf package, not here. Each texlive-texmf subpackage
# owns both the script and its /usr/bin symlink.
# Remove the ones installed by make install (linked_scripts mechanism).
for link in $RPM_BUILD_ROOT%{_bindir}/*; do
	[ -L "$link" ] || continue
	target=$(readlink "$link")
	case "$target" in
		*texmf-dist/scripts/*) rm "$link" ;;
	esac
done
# Binary-to-binary aliases (texhash->mktexlsr etc.) are also created by
# linked_scripts. Remove them - texlive-texmf creates them in its %install.
rm $RPM_BUILD_ROOT%{_bindir}/texhash
rm $RPM_BUILD_ROOT%{_bindir}/mktexfmt
rm $RPM_BUILD_ROOT%{_bindir}/allec
rm $RPM_BUILD_ROOT%{_bindir}/ebb
rm $RPM_BUILD_ROOT%{_bindir}/kpsexpand
rm $RPM_BUILD_ROOT%{_bindir}/kpsepath
rm $RPM_BUILD_ROOT%{_bindir}/rpdfcrop
rm $RPM_BUILD_ROOT%{_bindir}/cllualatex
rm $RPM_BUILD_ROOT%{_bindir}/clxelatex
rm $RPM_BUILD_ROOT%{_bindir}/latexdef
rm $RPM_BUILD_ROOT%{_bindir}/repstopdf
# Also remove man pages for aliases (owned by texlive-texmf)
rm $RPM_BUILD_ROOT%{_mandir}/man1/texhash.1
rm $RPM_BUILD_ROOT%{_mandir}/man1/mktexfmt.1
rm $RPM_BUILD_ROOT%{_mandir}/man1/allec.1
rm $RPM_BUILD_ROOT%{_mandir}/man1/kpsexpand.1
rm $RPM_BUILD_ROOT%{_mandir}/man1/kpsepath.1
rm -r $RPM_BUILD_ROOT%{texmfdist}/scripts

install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.daily/texlive

install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE6} $RPM_BUILD_ROOT%{_pixmapsdir}


# Fix #!/usr/bin/env shebangs in compiled script wrappers (PLD policy)
grep -rl '/usr/bin/env ' $RPM_BUILD_ROOT%{_bindir} 2>/dev/null | \
	xargs %{__sed} -i \
	-e '1s,^#!\s*/usr/bin/env\s\+perl,#!/usr/bin/perl,' \
	-e '1s,^#!\s*/usr/bin/env\s\+python,#!/usr/bin/python3,' \
	2>/dev/null || :

# Remove install artifacts not belonging to any package
rm $RPM_BUILD_ROOT%{_infodir}/dir
rm $RPM_BUILD_ROOT%{_infodir}/dvipng.info*

# Remove .la files (not needed, shared libs are used)
rm $RPM_BUILD_ROOT%{_libdir}/libkpathsea.la
rm $RPM_BUILD_ROOT%{_libdir}/libptexenc.la
rm $RPM_BUILD_ROOT%{_libdir}/libsynctex.la
rm $RPM_BUILD_ROOT%{_libdir}/libtexlua53.la

%if %{without luajittex}
# libtexluajit/mfluajit are built even with --disable-luajittex
# (the library is shared, only the engine binaries are skipped)
rm $RPM_BUILD_ROOT%{_bindir}/mfluajit
rm $RPM_BUILD_ROOT%{_bindir}/mfluajit-nowin
rm $RPM_BUILD_ROOT%{_mandir}/man1/luajittex.1
rm $RPM_BUILD_ROOT%{_libdir}/libtexluajit.la
rm $RPM_BUILD_ROOT%{_libdir}/libtexluajit.so*
rm $RPM_BUILD_ROOT%{_libdir}/pkgconfig/texluajit.pc
rm -r $RPM_BUILD_ROOT%{_includedir}/texluajit
%endif

# Remove texmf-dist data installed by make install that belongs to
# the texlive-texmf package (docs, configs, font tools data)
rm -r $RPM_BUILD_ROOT%{texmfdist}/bibtex
rm -r $RPM_BUILD_ROOT%{texmfdist}/chktex
rm -r $RPM_BUILD_ROOT%{texmfdist}/doc
rm -r $RPM_BUILD_ROOT%{texmfdist}/dvipdfmx
rm -r $RPM_BUILD_ROOT%{texmfdist}/dvips
rm -r $RPM_BUILD_ROOT%{texmfdist}/fonts
rm -r $RPM_BUILD_ROOT%{texmfdist}/hbf2gf
rm -r $RPM_BUILD_ROOT%{texmfdist}/psutils
rm -r $RPM_BUILD_ROOT%{texmfdist}/source
rm -r $RPM_BUILD_ROOT%{texmfdist}/texconfig
rm -r $RPM_BUILD_ROOT%{texmfdist}/ttf2pk
rm -r $RPM_BUILD_ROOT%{texmfdist}/web2c
rm -r $RPM_BUILD_ROOT%{texmfdist}/xdvi
rm $RPM_BUILD_ROOT%{_mandir}/man1/texconfig.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/texconfig-sys.1*

# Install TeXLive Perl modules needed by fmtutil/updmap at runtime.
# These come from texlive.infra upstream but we only need TLUtils + TLConfig.
install -d $RPM_BUILD_ROOT%{_datadir}/tlpkg/TeXLive
install -m 644 texk/tests/TeXLive/TLUtils.pm $RPM_BUILD_ROOT%{_datadir}/tlpkg/TeXLive/
install -m 644 texk/tests/TeXLive/TLConfig.pm $RPM_BUILD_ROOT%{_datadir}/tlpkg/TeXLive/

%clean
rm -rf $RPM_BUILD_ROOT

%post
%fixinfodir
%texhash
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt mf 1>&2
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt tex 1>&2

%postun
%fixinfodir
# Only run texhash on upgrade ("1"), not on full removal ("0") -
# the texmf trees are gone at that point
if [ "$1" = "1" ]; then
	%texhash
fi

%post other-utils
%texhash

%postun other-utils
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

%post dvips-basic
%fixinfodir
%texhash

%postun dvips-basic
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

%post -n xdvi
%texhash

%postun -n xdvi
%texhash

%post pdftex
%texhash
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt pdftex 1>&2
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt etex 1>&2

%postun pdftex
%texhash

%post latex
%fixinfodir
%texhash
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt latex 1>&2

%postun latex
%fixinfodir
%texhash

%post latex-bibtex
%texhash

%postun latex-bibtex
%texhash

%post format-pdflatex
%texhash
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt pdflatex 1>&2

%postun format-pdflatex
%texhash

%post xetex
%texhash
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt xetex 1>&2
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt xelatex 1>&2

%postun xetex
%texhash

%post luatex
%texhash
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt luatex 1>&2
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt luahbtex 1>&2
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt lualatex 1>&2
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt dviluatex 1>&2
umask 022; [ ! -x %{_bindir}/fmtutil-sys ] || %{_bindir}/fmtutil-sys --no-strict --byfmt dvilualatex 1>&2

%postun luatex
%texhash

%files
%defattr(644,root,root,755)

# ***********
# executables
# ***********
%attr(755,root,root) %{_bindir}/afm2tfm
%attr(755,root,root) %{_bindir}/afm2pl
%attr(755,root,root) %{_bindir}/ctangle
%attr(755,root,root) %{_bindir}/ctie
%attr(755,root,root) %{_bindir}/cweave
%attr(755,root,root) %{_bindir}/dvipng
%attr(755,root,root) %{_bindir}/gftodvi
%attr(755,root,root) %{_bindir}/gftopk
%attr(755,root,root) %{_bindir}/gftype
%attr(755,root,root) %{_bindir}/gsftopk
%attr(755,root,root) %{_bindir}/inimf
%attr(755,root,root) %{_bindir}/initex
%attr(755,root,root) %{_bindir}/kpseaccess
%attr(755,root,root) %{_bindir}/kpsereadlink
%attr(755,root,root) %{_bindir}/mag
%attr(755,root,root) %{_bindir}/mf
%attr(755,root,root) %{_bindir}/mf-nowin
%attr(755,root,root) %{_bindir}/mft
%attr(755,root,root) %{_bindir}/patgen
%attr(755,root,root) %{_bindir}/pfb2pfa
%attr(755,root,root) %{_bindir}/pk2bm
%attr(755,root,root) %{_bindir}/pktogf
%attr(755,root,root) %{_bindir}/pktype
%attr(755,root,root) %{_bindir}/pltotf
%attr(755,root,root) %{_bindir}/pooltype
%attr(755,root,root) %{_bindir}/ps2pk
%attr(755,root,root) %{_bindir}/tangle
%attr(755,root,root) %{_bindir}/tex
%attr(755,root,root) %{_bindir}/tftopl
%attr(755,root,root) %{_bindir}/tie
%attr(755,root,root) %{_bindir}/ttf2afm
%attr(755,root,root) %{_bindir}/vftovp
%attr(755,root,root) %{_bindir}/vptovf
%attr(755,root,root) %{_bindir}/weave


%config(noreplace,missingok) %verify(not md5 mtime size) %attr(750,root,root) /etc/cron.daily/texlive

# fmtutil.cnf and texmf.cnf are owned by texlive-texmf (texlive-kpathsea)

%attr(1777,root,root) /var/cache/fonts

%{_infodir}/web2c.info*

# TeXLive Perl modules (needed by fmtutil/updmap)
%dir %{_datadir}/tlpkg
%dir %{_datadir}/tlpkg/TeXLive
%{_datadir}/tlpkg/TeXLive/TLConfig.pm
%{_datadir}/tlpkg/TeXLive/TLUtils.pm

# ***********
# Directories
# ***********
%attr(1777,root,root) %dir %{_localstatedir}
%attr(1777,root,root) %dir %{_localstatedir}/fonts
%attr(1777,root,root) %dir %{_localstatedir}/fonts/map
%dir %{fmtdir}

# New TL 2026 compiled binaries
%attr(755,root,root) %{_bindir}/autosp
%attr(755,root,root) %{_bindir}/axohelp
%attr(755,root,root) %{_bindir}/chkdvifont
%attr(755,root,root) %{_bindir}/chktex
%attr(755,root,root) %{_bindir}/ctwill
%attr(755,root,root) %{_bindir}/ctwill-proofsort
%attr(755,root,root) %{_bindir}/ctwill-refsort
%attr(755,root,root) %{_bindir}/ctwill-twinx
%attr(755,root,root) %{_bindir}/dvispc
%attr(755,root,root) %{_bindir}/eptex
%attr(755,root,root) %{_bindir}/euptex
%attr(755,root,root) %{_bindir}/gregorio
%attr(755,root,root) %{_bindir}/hishrink
%attr(755,root,root) %{_bindir}/histretch
%attr(755,root,root) %{_bindir}/hitex
%attr(755,root,root) %{_bindir}/makejvf
%attr(755,root,root) %{_bindir}/mendex
%attr(755,root,root) %{_bindir}/mflua
%attr(755,root,root) %{_bindir}/mflua-nowin
%attr(755,root,root) %{_bindir}/mfplain
%attr(755,root,root) %{_bindir}/mkocp
%attr(755,root,root) %{_bindir}/mkofm
%attr(755,root,root) %{_bindir}/msxlint
%attr(755,root,root) %{_bindir}/odvicopy
%attr(755,root,root) %{_bindir}/odvitype
%attr(755,root,root) %{_bindir}/omfonts
%attr(755,root,root) %{_bindir}/opl2ofm
%attr(755,root,root) %{_bindir}/otangle
%attr(755,root,root) %{_bindir}/otp2ocp
%attr(755,root,root) %{_bindir}/outocp
%attr(755,root,root) %{_bindir}/ovf2ovp
%attr(755,root,root) %{_bindir}/ovp2ovf
%attr(755,root,root) %{_bindir}/pbibtex
%attr(755,root,root) %{_bindir}/pdvitomp
%attr(755,root,root) %{_bindir}/pdvitype
%attr(755,root,root) %{_bindir}/pmpost
%attr(755,root,root) %{_bindir}/pmxab
%attr(755,root,root) %{_bindir}/ppltotf
%attr(755,root,root) %{_bindir}/prepmx
%attr(755,root,root) %{_bindir}/ptekf
%attr(755,root,root) %{_bindir}/ptftopl
%attr(755,root,root) %{_bindir}/r-mpost
%attr(755,root,root) %{_bindir}/r-pmpost
%attr(755,root,root) %{_bindir}/r-upmpost
%attr(755,root,root) %{_bindir}/scor2prt
%attr(755,root,root) %{_bindir}/tex2aspc
%attr(755,root,root) %{_bindir}/texprof
%attr(755,root,root) %{_bindir}/texprofile
%attr(755,root,root) %{_bindir}/twill
%attr(755,root,root) %{_bindir}/twill-refsort
%attr(755,root,root) %{_bindir}/upbibtex
%attr(755,root,root) %{_bindir}/updvitomp
%attr(755,root,root) %{_bindir}/updvitype
%attr(755,root,root) %{_bindir}/upmendex
%attr(755,root,root) %{_bindir}/upmpost
%attr(755,root,root) %{_bindir}/uppltotf
%attr(755,root,root) %{_bindir}/uptex
%attr(755,root,root) %{_bindir}/uptftopl
%attr(755,root,root) %{_bindir}/wofm2opl
%attr(755,root,root) %{_bindir}/wopl2ofm
%attr(755,root,root) %{_bindir}/wovf2ovp
%attr(755,root,root) %{_bindir}/wovp2ovf
%attr(755,root,root) %{_bindir}/xdvipsk
%attr(755,root,root) %{_bindir}/xml2pmx

# Libraries
%attr(755,root,root) %{_libdir}/libptexenc.so.*
%attr(755,root,root) %{_libdir}/libsynctex.so.*
%attr(755,root,root) %{_libdir}/libtexlua53.so.*

%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/afm2pl.1*
%{_mandir}/man1/allcm.1*
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
%{_mandir}/man1/mf.1*
%{_mandir}/man1/mf-nowin.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*
%{_mandir}/man1/mktexlsr.1*
%{_mandir}/man1/patgen.1*
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

%files cef-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bg5+latex
%attr(755,root,root) %{_bindir}/bg5+pdflatex
%attr(755,root,root) %{_bindir}/bg5conv
%attr(755,root,root) %{_bindir}/bg5latex
%attr(755,root,root) %{_bindir}/bg5pdflatex
%attr(755,root,root) %{_bindir}/cef*
%{_mandir}/man1/bg5conv.1*
%{_mandir}/man1/cef?conv.1*

%files other-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bibtex8
%attr(755,root,root) %{_bindir}/cfftot1
%attr(755,root,root) %{_bindir}/extconv
%attr(755,root,root) %{_bindir}/gbklatex
%attr(755,root,root) %{_bindir}/gbkpdflatex
%attr(755,root,root) %{_bindir}/hbf2gf
%attr(755,root,root) %{_bindir}/mmafm
%attr(755,root,root) %{_bindir}/mmpfb
%attr(755,root,root) %{_bindir}/ofm2opl
%attr(755,root,root) %{_bindir}/otfinfo
%attr(755,root,root) %{_bindir}/otftotfm
%attr(755,root,root) %{_bindir}/pdfclose
%attr(755,root,root) %{_bindir}/pdfopen
%attr(755,root,root) %{_bindir}/pdftosrc
%attr(755,root,root) %{_bindir}/teckit_compile
%attr(755,root,root) %{_bindir}/sjisconv
%attr(755,root,root) %{_bindir}/sjislatex
%attr(755,root,root) %{_bindir}/sjispdflatex
%attr(755,root,root) %{_bindir}/synctex
%attr(755,root,root) %{_bindir}/ttf2pk
%attr(755,root,root) %{_bindir}/ttf2tfm
%attr(755,root,root) %{_bindir}/ttftotype42
%attr(755,root,root) %{_bindir}/vlna
%{_mandir}/man1/cfftot1.1*
%{_mandir}/man1/hbf2gf.1*
%{_mandir}/man1/mmafm.1*
%{_mandir}/man1/mmpfb.1*
%{_mandir}/man1/otfinfo.1*
%{_mandir}/man1/otftotfm.1*
%{_mandir}/man1/pdfclose.1*
%{_mandir}/man1/pdfopen.1*
%{_mandir}/man1/pdftosrc.1*
%{_mandir}/man1/synctex.1*
%{_mandir}/man1/ttf2pk.1*
%{_mandir}/man1/ttf2tfm.1*
%{_mandir}/man1/ttftotype42.1*
%{_mandir}/man1/vlna.1*
%{_mandir}/man5/synctex.5*
# New TL 2026 man pages
%{_mandir}/man1/amstex.1*
%{_mandir}/man1/autosp.1*
%{_mandir}/man1/axohelp.1*
%{_mandir}/man1/bibtex8.1*
%{_mandir}/man1/bibtexu.1*
%{_mandir}/man1/cefconv.1*
%{_mandir}/man1/chkdvifont.1*
%{_mandir}/man1/chktex.1*
%{_mandir}/man1/chkweb.1*
%{_mandir}/man1/ctwill.1*
%{_mandir}/man1/ctwill-proofsort.1*
%{_mandir}/man1/ctwill-refsort.1*
%{_mandir}/man1/ctwill-twinx.1*
%{_mandir}/man1/devnag.1*
%{_mandir}/man1/deweb.1*
%{_mandir}/man1/disdvi.1*
%{_mandir}/man1/dvilualatex-dev.1*
%{_mandir}/man1/dvispc.1*
%{_mandir}/man1/eptex.1*
%{_mandir}/man1/euptex.1*
%{_mandir}/man1/extconv.1*
%{_mandir}/man1/inimf.1*
%{_mandir}/man1/initex.1*
%{_mandir}/man1/latex-dev.1*
%{_mandir}/man1/lualatex-dev.1*
%{_mandir}/man1/makejvf.1*
%{_mandir}/man1/mendex.1*
%{_mandir}/man1/mkocp.1*
%{_mandir}/man1/mkofm.1*
%{_mandir}/man1/msxlint.1*
%{_mandir}/man1/odvicopy.1*
%{_mandir}/man1/odvitype.1*
%{_mandir}/man1/ofm2opl.1*
%{_mandir}/man1/opl2ofm.1*
%{_mandir}/man1/otangle.1*
%{_mandir}/man1/otp2ocp.1*
%{_mandir}/man1/outocp.1*
%{_mandir}/man1/ovf2ovp.1*
%{_mandir}/man1/ovp2ovf.1*
%{_mandir}/man1/pbibtex.1*
%{_mandir}/man1/pdflatex-dev.1*
%{_mandir}/man1/platex-dev.1*
%{_mandir}/man1/pmxab.1*
%{_mandir}/man1/ppltotf.1*
%{_mandir}/man1/prepmx.1*
%{_mandir}/man1/ptekf.1*
%{_mandir}/man1/ptex.1*
%{_mandir}/man1/ptftopl.1*
%{_mandir}/man1/scor2prt.1*
%{_mandir}/man1/sjisconv.1*
%{_mandir}/man1/tex2aspc.1*
%{_mandir}/man1/texprof.1*
%{_mandir}/man1/texprofile.1*
%{_mandir}/man1/twill.1*
%{_mandir}/man1/twill-refsort.1*
%{_mandir}/man1/upbibtex.1*
%{_mandir}/man1/uplatex-dev.1*
%{_mandir}/man1/uppltotf.1*
%{_mandir}/man1/uptex.1*
%{_mandir}/man1/uptftopl.1*
%{_mandir}/man1/xdvipsk.1*
%{_mandir}/man1/xml2pmx.1*


%files font-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/t1*
%attr(755,root,root) %{_bindir}/ttfdump
%{_mandir}/man1/t1*.1*
%{_mandir}/man1/ttfdump.1*

%files -n kpathsea
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpsestat
%attr(755,root,root) %{_bindir}/kpsewhich
%attr(755,root,root) %{_libdir}/libkpathsea.so.*
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsetool.1*
%{_mandir}/man1/kpsewhich.1*

%files -n kpathsea-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkpathsea.so
%attr(755,root,root) %{_libdir}/libptexenc.so
%attr(755,root,root) %{_libdir}/libsynctex.so
%attr(755,root,root) %{_libdir}/libtexlua53.so
%{_includedir}/kpathsea
%{_includedir}/ptexenc
%{_includedir}/synctex
%{_includedir}/texlua53
%{_infodir}/kpathsea.info*
%{_infodir}/tlbuild.info*
%{_libdir}/pkgconfig/kpathsea.pc
%{_libdir}/pkgconfig/ptexenc.pc
%{_libdir}/pkgconfig/synctex.pc
%{_libdir}/pkgconfig/texlua53.pc

%files dvips-basic
%defattr(644,root,root,755)
# dvi2fax requires ghostscript
%attr(755,root,root) %{_bindir}/dvicopy
%attr(755,root,root) %{_bindir}/dvipdfm
%attr(755,root,root) %{_bindir}/dvipdft
%attr(755,root,root) %{_bindir}/dvips
%attr(755,root,root) %{_bindir}/dvitomp
%attr(755,root,root) %{_bindir}/dvisvgm
%attr(755,root,root) %{_bindir}/dvitype
%{_infodir}/dvips.info*
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvicopy.1*
%{_mandir}/man1/dvips.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/dvitype.1*
%{_mandir}/man1/dvipdfm.1*
%{_mandir}/man1/dvipdfmx.1*
%{_mandir}/man1/dvipdft.1*
%{_mandir}/man1/dvisvgm.1*
%{_mandir}/man1/extractbb.1*

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
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/mkindex.1*
%{_mandir}/man1/rumakeindex.1*

%files scripts
%defattr(644,root,root,755)
%{_mandir}/man1/e2pall.1*

%files metapost
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpost
%{_mandir}/man1/mpost.1*


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

%files pdftex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdftex
%attr(755,root,root) %{_bindir}/tpic2pdftex
%dir %{fmtdir}/pdftex
%{_mandir}/man1/pdftex.1*
%{_mandir}/man1/tpic2pdftex.1*

%files latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lacheck
%attr(755,root,root) %{_bindir}/latex

%{_mandir}/man1/lacheck.1*
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pslatex.1*

%files latex-bibtex
%defattr(644,root,root,755)
%{_mandir}/man1/bibtex.1*
%{_mandir}/man1/rubibtex.1*

%attr(755,root,root) %{_bindir}/bibtex
%attr(755,root,root) %{_bindir}/bibtexu
 
%files format-pdflatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdflatex
%{_mandir}/man1/pdflatex.1*
 
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
%attr(755,root,root) %{_bindir}/disdvi
%attr(755,root,root) %{_bindir}/dt2dv
%attr(755,root,root) %{_bindir}/dv2dt
%attr(755,root,root) %{_bindir}/dvi2tty
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

%files psutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/epsffit
%attr(755,root,root) %{_bindir}/psbook
%attr(755,root,root) %{_bindir}/psnup
%attr(755,root,root) %{_bindir}/psresize
%attr(755,root,root) %{_bindir}/psselect
%attr(755,root,root) %{_bindir}/pstops
%{_mandir}/man1/epsffit*
%{_mandir}/man1/extractres*
%{_mandir}/man1/includeres*
%{_mandir}/man1/ps2eps.1*
%{_mandir}/man1/psbook*
%{_mandir}/man1/psjoin*
%{_mandir}/man1/psnup*
%{_mandir}/man1/psresize*
%{_mandir}/man1/psselect*
%{_mandir}/man1/pstops*
%{_mandir}/man1/psutils*

%files uncategorized-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/devnag

%files tex4ht
%defattr(644,root,root,755)
# htcontext removed in TL 2026
%attr(755,root,root) %{_bindir}/t4ht
%attr(755,root,root) %{_bindir}/tex4ht
# htcontext.sh removed in TL 2026

%files xetex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdvipdfmx
%attr(755,root,root) %{_bindir}/xelatex
%attr(755,root,root) %{_bindir}/xetex
%{_mandir}/man1/xdvipdfmx.1*
%{_mandir}/man1/xetex.1*
%{_mandir}/man1/xelatex-dev.1*

%files luatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/luatex
%attr(755,root,root) %{_bindir}/luahbtex
%attr(755,root,root) %{_bindir}/texlua
%attr(755,root,root) %{_bindir}/texluac
%attr(755,root,root) %{_bindir}/lualatex
%{_mandir}/man1/luatex.1*
%{_mandir}/man1/luahbtex.1*
%{_mandir}/man1/texlua.1*
%{_mandir}/man1/texluac.1*
%{_mandir}/man1/dviluatex.1*
