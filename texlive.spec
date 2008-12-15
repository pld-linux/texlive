# TODO:
# MAIN TODO:
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
# - summary/description correcting (all languages)
# - solve xindy case, it doesn't build with tetext, and probably won't with texlive
#   until larm1000 font found (xindy option)
# - texk/web2c doesn't build (luatex option)
#
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
Release:	0.1
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
Requires:	%{name}-dirs-fonts
Requires:	%{name}-fonts-cm = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-misc = %{epoch}:%{version}-%{release}
Requires:	%{name}-metafont = %{epoch}:%{version}-%{release}
Requires:	awk
Requires:	dialog
Requires:	sed
Requires:	sh-utils
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
Summary(pl.UTF-8):	FAQ Grupy Użytkowników TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-doc-LaTeX-FAQ-francaise
Obsoletes:	tetex-doc-de-tex-faq
Obsoletes:	tetex-doc-uktug-faq

%description doc-tug-faq
TeX User Group FAQ.

%description doc-tug-faq -l pl.UTF-8
FAQ Grupy Użytkowników TeXa.

%package doc-latex
Summary:	Basic LaTeX packages documentation
Summary(pl.UTF-8):	Podstawowa dokumentacja do pakietów LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description doc-latex
Basic LaTeX packages documentation.

%description doc-latex -l pl.UTF-8
Podstawowa dokumentacja do pakietów LaTeXa.

# # libraries #
%package -n kpathsea
Summary:	File name lookup library
Summary(pl.UTF-8):	Biblioteka szukająca nazw plików
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kpathsea
File name lookup library.

%description -n kpathsea -l pl.UTF-8
Biblioteka szukająca nazw plików.

%package -n kpathsea-devel
Summary:	Kpathsea library filename lookup header files and documentation
Summary(es.UTF-8):	Bibliotecas y archivos de inclusión para desarrollo TeX
Summary(pl.UTF-8):	Pliki nagłówkowe oraz dokumetacja kpathsea
Summary(pt_BR.UTF-8):	Bibliotecas e headers para desenvolvimento TeX
Group:		Development/Libraries
Requires:	kpathsea = %{epoch}:%{version}-%{release}

%description -n kpathsea-devel
Kpathsea library filename lookup header files and documentation.

%description -n kpathsea-devel -l es.UTF-8
Bibliotecas, archivos de inclusión, etc, para que puedas desarrollar
aplicaciones TeX.

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
Summary(pl.UTF-8):	Zestaw narzędzi MetaPost
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-matapost

%description metapost
MetaPost.

%description metapost -l pl.UTF-8
Zestaw narzędzi MetaPost.

%package mptopdf
Summary:	MetaPost to PDF converter
Summary(pl.UTF-8):	Konwerter MetaPost do PDF
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-metapost = %{epoch}:%{version}-%{release}

%description mptopdf
MetaPost to PDF converter.

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
Requires:	tetex-fonts-pl = %{epoch}:%{version}-%{release}
Requires:	tetex-plain = %{epoch}:%{version}-%{release}

%description mex
MeX Plain Format basic files.

%description mex -l pl.UTF-8
Podstawowe pliki dla formatu MeX Plain.

%package format-mex
Summary:	MeX Plain Format
Summary(pl.UTF-8):	Format MeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	tetex-mex = %{epoch}:%{version}-%{release}

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
# for misc/eurosym:
Requires:	%{name}-fonts-eurosym = %{epoch}:%{version}-%{release}
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

%package tex-qtx
Summary:	QuasiTimes and TX fonts typesetting support
Summary(pl.UTF-8):	Wsparcie dla składu fontami QuasiTimes i TX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-qtx = %{epoch}:%{version}-%{release}

%description tex-qtx
QuasiTimes and TX fonts typesetting support.

%description tex-qtx -l pl.UTF-8
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
Requires:	%{name}-dirs-fonts

%description fonts-adobe
Adobe fonts.

%description fonts-adobe -l pl.UTF-8
Fonty Adobe.

%package fonts-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Summary(pl.UTF-8):	Wirtualne fonty do plików PDF z fontami CMR o kodowaniu T1
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-ae
Virtual fonts for PDF-files with T1 encoded CMR-fonts.

%description fonts-ae -l pl.UTF-8
Wirtualne fonty do plików PDF z fontami CMR o kodowaniu T1.

%package fonts-ams
Summary:	AMS fonts
Summary(pl.UTF-8):	Fonty AMS
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-ams
AMS fonts.

%description fonts-ams -l pl.UTF-8
Fonty AMS.

%package fonts-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl.UTF-8):	Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-antp
Antykwa Poltawskiego, a Type 1 family of Polish traditional type.

%description fonts-antp -l pl.UTF-8
Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako
Type 1.

%package fonts-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Summary(pl.UTF-8):	Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%description fonts-antt -l pl.UTF-8
Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1.

%package fonts-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Summary(pl.UTF-8):	Tablicowy wariant fontów Computer Modern ze wsparciem dla LaTeXa
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%description fonts-bbm -l pl.UTF-8
Tablicowy wariant fontów Computer Modern ze wsparciem dla LaTeXa.

%package fonts-bbold
Summary:	Sans serif blackboard bold for LaTeX
Summary(pl.UTF-8):	Tablicowy tłusty font sans serif dla LaTeXa
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-bbold
Sans serif blackboard bold for LaTeX.

%description fonts-bbold -l pl.UTF-8
Tablicowy tłusty font sans serif dla LaTeXa.

%package fonts-bh
Summary:	Bold & Heavy Fonts
Summary(pl.UTF-8):	Fonty Bold i Heavy
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-bh
Bold & Heavy Fonts.

%description fonts-bh -l pl.UTF-8
Fonty Bold i Heavy.

%package fonts-bitstream
Summary:	Bitstream fonts
Summary(pl.UTF-8):	Fonty Bitstream
Group:		Fonts
Requires:	%{name}-dirs-fonts
Obsoletes:	tetex-fonts-bitstrea

%description fonts-bitstream
Bitstream fonts.

%description fonts-bitstream -l pl.UTF-8
Fonty Bitstream.

%package fonts-cbgreek
Summary:	Complete set of Greek fonts
Summary(pl.UTF-8):	Pełny zestaw fontów greckich
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-cbgreek
Complete set of Greek fonts.

%description fonts-cbgreek -l pl.UTF-8
Pełny zestaw fontów greckich.

%package fonts-cc-pl
Summary:	Polish version of Computer Concrete fonts
Summary(pl.UTF-8):	Polska wersja fontów Computer Concrete
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-cc-pl
Polish version of Computer Concrete fonts.

%description fonts-cc-pl -l pl.UTF-8
Polska wersja fontów Computer Concrete.

%package fonts-cg
Summary:	Compugraphic fonts
Summary(pl.UTF-8):	Fonty Compugraphic
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-cg
Compugraphic fonts.

%description fonts-cg -l pl.UTF-8
Fonty Compugraphic.

%package fonts-cm
Summary:	Computer Modern fonts
Summary(pl.UTF-8):	Fonty Computer Modern
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-cm
Computer Modern fonts.

%description fonts-cm -l pl.UTF-8
Fonty Computer Modern.

%package fonts-cmbright
Summary:	CM Bright fonts
Summary(pl.UTF-8):	Fonty CM Bright
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-cmbright
CM Bright fonts.

%description fonts-cmbright -l pl.UTF-8
Fonty CM Bright.

%package fonts-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Summary(pl.UTF-8):	Fonty Computer Modern rozszerzone o litery rosyjskie
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-cmcyr
Computer Modern fonts extended with Russian letters.

%description fonts-cmcyr -l pl.UTF-8
Fonty Computer Modern rozszerzone o litery rosyjskie.

%package fonts-cmextra
Summary:	Extra Computer Modern fonts, from the American Mathematical Society
Summary(pl.UTF-8):	Dodatkowe fonty Computer Modern z AMS
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-cmextra
Extra Computer Modern fonts, from the American Mathematical Society.

%description fonts-cmextra -l pl.UTF-8
Dodatkowe fonty Computer Modern z AMS (American Mathematical Society).

%package fonts-concmath
Summary:	Concrete Math fonts
Summary(pl.UTF-8):	Fonty matematyczne Concrete Math
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-concmath
Concrete Math fonts.

%description fonts-concmath -l pl.UTF-8
Fonty matematyczne Concrete Math.

%package fonts-concrete
Summary:	Concrete Roman fonts
Summary(pl.UTF-8):	Fonty Concrete Roman
Group:		Fonts
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

%description fonts-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%description fonts-cs -l pl.UTF-8
Fonty MetaFont Computer Modern zmodyfikowane pod kątem języków
czeskiego i słowackiego.

%package fonts-dstroke
Summary:	Doublestroke font for typesetting the mathematical symbols
Summary(pl.UTF-8):	Podwójnie kreślony font do składania symboli matematycznych
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-dstroke
Doublestroke font for typesetting the mathematical symbols.

%description fonts-dstroke -l pl.UTF-8
Podwójnie kreślony font do składania symboli matematycznych.

%package fonts-ecc
Summary:	Sources for the European Concrete fonts
Summary(pl.UTF-8):	Źródła dla fontów European Concrete
Group:		Fonts
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

%description fonts-gothic
Gothic and ornamental initial fonts by Yannis Haralambous.

%description fonts-gothic -l pl.UTF-8
Początkowe fonty gotyckie i ornamentowe Yannisa Haralambousa.

%package fonts-hoekwater
Summary:	Converted mflogo font
Summary(pl.UTF-8):	Przekonwertowany font mflogo
Group:		Fonts
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

%description fonts-latex
Basic LaTeX fonts.

%description fonts-latex -l pl.UTF-8
Podstawowe fonty dla LaTeXa.

%package fonts-lh
Summary:	Olga Lapko's LH fonts
Summary(pl.UTF-8):	Fonty LH Olgi Lapko
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-lh
The lh fonts for the `T2'/X2 encodings (for cyrillic languages).

%description fonts-lh -l pl.UTF-8
Fonty lh dla kodowań `T2'/X2 (dla języków zapisywanych cyrylicą).

%package fonts-lm
Summary:	Latin Modern family fonts
Summary(pl.UTF-8):	Fonty z rodziny Latin Modern
Group:		Applications/Publishing/TeX
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

%description fonts-mflogo
Logo fonts.

%description fonts-mflogo -l pl.UTF-8
Fonty logo.

%package fonts-misc
Summary:	Miscellaneous fonts
Summary(pl.UTF-8):	Różne fonty
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-misc
Miscellaneous fonts.

%description fonts-misc -l pl.UTF-8
Fonty różne.

%package fonts-monotype
Summary:	Monotype fonts
Summary(pl.UTF-8):	Fonty Monotype
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-monotype
Monotype fonts.

%description fonts-monotype -l pl.UTF-8
Fonty Monotype.

%package fonts-omega
Summary:	Fonts for Omega - extended unicode TeX
Summary(pl.UTF-8):	Fonty dla Omegi - TeXa ze wsparciem dla unikodu
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-omega
Fonts for Omega - extended unicode TeX.

%description fonts-omega -l pl.UTF-8
Fonty dla Omegi - TeXa ze wsparciem dla unikodu.

%package fonts-pazo
Summary:	Pazo fonts
Summary(pl.UTF-8):	Fonty Pazo
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-pazo
Pazo fonts.

%description fonts-pazo -l pl.UTF-8
Fonty Pazo.

%package fonts-pl
Summary:	Polish fonts
Summary(pl.UTF-8):	Polskie fonty
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-pl
Polish fonts.

%description fonts-pl -l pl.UTF-8
Polskie fonty.

%package fonts-px
Summary:	PX fonts
Summary(pl.UTF-8):	Fonty PX
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-px
PX fonts.

%description fonts-px -l pl.UTF-8
Fonty PX.

%package fonts-qfonts
Summary:	Quasi fonts
Summary(pl.UTF-8):	Fonty Quasi
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-qfonts
Quasi fonts.

%description fonts-qfonts -l pl.UTF-8
Fonty Quasi.

%package fonts-qpx
Summary:	Additional fonts for QPX package
Summary(pl.UTF-8):	Dodatkowe fonty dla pakietu QPX
Group:		Fonts
Requires:	%{name}-dirs-fonts
Requires:	%{name}-fonts-px = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-qfonts = %{epoch}:%{version}-%{release}

%description fonts-qpx
Additional fonts for QPX package.

%description fonts-qpx -l pl.UTF-8
Dodatkowe fonty dla pakietu QPX.

%package fonts-qtx
Summary:	Additional fonts for QTX package
Summary(pl.UTF-8):	Dodatkowe fonty dla pakietu QTX
Group:		Fonts
Requires:	%{name}-dirs-fonts
Requires:	%{name}-fonts-qfonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-tx = %{epoch}:%{version}-%{release}

%description fonts-qtx
Additional fonts for QTX package.

%description fonts-qtx -l pl.UTF-8
Dodatkowe fonty dla pakietu QTX.

%package fonts-rsfs
Summary:	Fonts of uppercase script letters for scientific and mathematical typesetting
Summary(pl.UTF-8):	Fonty wielkich liter pisanych do składania dokumentów naukowych i matematycznych
Group:		Fonts
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

%description fonts-stmaryrd
St Mary Road symbols for functional programming.

%description fonts-stmaryrd -l pl.UTF-8
Symbole St Mary Road do programowania funkcyjnego.

%package fonts-tx
Summary:	TX fonts
Summary(pl.UTF-8):	Fonty TX
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-tx
TX fonts.

%description fonts-tx -l pl.UTF-8
Fonty TX.

%package fonts-urw
Summary:	URW fonts
Summary(pl.UTF-8):	Fonty URW
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-urw
URW fonts.

%description fonts-urw -l pl.UTF-8
Fonty URW.

%package fonts-urwvn
Summary:	URWVN fonts
Summary(pl.UTF-8):	Fonty URWVN
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-urwvn
URWVN fonts.

%description fonts-urwvn -l pl.UTF-8
Fonty URWVN.

%package fonts-vnr
Summary:	VNR fonts
Summary(pl.UTF-8):	Fonty VNR
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-vnr
VNR fonts.

%description fonts-vnr -l pl.UTF-8
Fonty VNR.

%package fonts-wasy
Summary:	Waldis symbol fonts
Summary(pl.UTF-8):	Fonty Waldis symbol
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-wasy
Waldis symbol fonts.

%description fonts-wasy -l pl.UTF-8
Fonty Waldis symbol.

%package fonts-xypic
Summary:	Xy-pic fonts
Summary(pl.UTF-8):	Fonty Xy-pic
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-xypic
Xy-pic fonts.

%description fonts-xypic -l pl.UTF-8
Fonty Xy-pic.

%package fonts-yandy
Summary:	European Modern fonts from Y&Y
Summary(pl.UTF-8):	Fonty European Modern od Y&Y
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-yandy
European Modern fonts from Y&Y.

%description fonts-yandy -l pl.UTF-8
Fonty European Modern od Y&Y.

%package fonts-type1-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl.UTF-8):	Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-antp
Antykwa Poltawskiego, a Type 1 family of Polish traditional type.

%description fonts-type1-antp -l pl.UTF-8
Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako
Type 1.

%package fonts-type1-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Summary(pl.UTF-8):	Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%description fonts-type1-antt -l pl.UTF-8
Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1.

%package fonts-type1-belleek
Summary:	Free replacement for basic MathTime fonts
Summary(pl.UTF-8):	Wolnodostępny zamiennik podstawowych fontów MathTime
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-belleek
Free replacement for basic MathTime fonts.

%description fonts-type1-belleek -l pl.UTF-8
Wolnodostępny zamiennik podstawowych fontów MathTime.

%package fonts-type1-bitstream
Summary:	Bitstream fonts
Summary(pl.UTF-8):	Fonty Bitstream
Group:		Fonts
Requires:	%{name}-dirs-fonts
Obsoletes:	tetex-fonts-type1-bitstrea

%description fonts-type1-bitstream
Bitstream fonts.

%description fonts-type1-bitstream -l pl.UTF-8
Fonty Bitstream.

%package fonts-type1-bluesky
Summary:	Computer Modern family fonts
Summary(pl.UTF-8):	Fonty z rodziny Computer Modern
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-bluesky
Computer Modern family fonts.

%description fonts-type1-bluesky -l pl.UTF-8
Fonty z rodzony Computer Modern.

%package fonts-type1-cc-pl
Summary:	Polish version of Computer Concrete fonts
Summary(pl.UTF-8):	Polska wersja fontów Computer Concrete
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-cc-pl
Polish version of Computer Concrete fonts.

%description fonts-type1-cc-pl -l pl.UTF-8
Polska wersja fontów Computer Concrete.

%package fonts-type1-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Summary(pl.UTF-8):	Fonty Computer Modern rozszerzone o litery rosyjskie
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-cmcyr
Computer Modern fonts extended with Russian letters.

%description fonts-type1-cmcyr -l pl.UTF-8
Fonty Computer Modern rozszerzone o litery rosyjskie.

%package fonts-type1-cs
Summary:	Czech/Slovak-tuned MetaFont Computer Modern fonts
Summary(pl.UTF-8):	Fonty MetaFont Computer Modern dla języków czeskiego i słowackiego
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%description fonts-type1-cs -l pl.UTF-8
Fonty MetaFont Computer Modern zmodyfikowane pod kątem języków
czeskiego i słowackiego.

%package fonts-type1-dstroke
Summary:	Doublestroke Type1 font for typesetting the mathematical symbols
Summary(pl.UTF-8):	Podwójnie kreślony font Type1 do składania symboli matematycznych
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-dstroke
Doublestroke Type1 font for typesetting the mathematical symbols.

%description fonts-type1-dstroke -l pl.UTF-8
Podwójnie kreślony font Type1 do składania symboli matematycznych.

%package fonts-type1-eurosym
Summary:	The new European currency symbol for the Euro
Summary(pl.UTF-8):	Symbol nowej europejskiej waluty Euro
Group:		Fonts
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

%description fonts-type1-tt2001
Type1 tt2001 famliy fonts.

%description fonts-type1-tt2001 -l pl.UTF-8
Fonty Type1 z rodziny tt2001.

%package fonts-type1-lm
Summary:	Type1 Latin Modern family fonts
Summary(pl.UTF-8):	Fonty Type1 z rodziny Latin Modern
Group:		Applications/Publishing/TeX
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

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
Requires:	%{name}-dirs-fonts

%description fonts-type1-mathpazo
Pazo Math fonts.

%description fonts-type1-mathpazo -l pl.UTF-8
Fonty matematyczne Pazo Math.

%package fonts-type1-omega
Summary:	Type1 fonts for Omega - extended unicode TeX
Summary(pl.UTF-8):	Fonty Type1 dla Omegi - TeXa ze wsparciem dla unikodu
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-omega
Type1 fonts for Omega - extended unicode TeX.

%description fonts-type1-omega -l pl.UTF-8
Fonty Type1 dla Omegi - TeXa ze wsparciem dla unikodu.

%package fonts-type1-pl
Summary:	Polish fonts
Summary(pl.UTF-8):	Polskie fonty
Group:		Fonts
Requires:	%{name}-dirs-fonts
Requires:	%{name}-fonts-type1-bluesky = %{epoch}:%{version}-%{release}

%description fonts-type1-pl
Polish fonts.

%description fonts-type1-pl -l pl.UTF-8
Polskie fonty.

%package fonts-type1-px
Summary:	PX fonts
Summary(pl.UTF-8):	Fonty PX
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-px
PX fonts.

%description fonts-type1-px -l pl.UTF-8
Fonty PX.

%package fonts-type1-qfonts
Summary:	Quasi fonts
Summary(pl.UTF-8):	Fonty Quasi
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-qfonts
Quasi fonts.

%description fonts-type1-qfonts -l pl.UTF-8
Fonty Quasi.

%package fonts-type1-tx
Summary:	TX fonts
Summary(pl.UTF-8):	Fonty TX
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-tx
TX fonts.

%description fonts-type1-tx -l pl.UTF-8
Fonty TX.

%package fonts-type1-urw
Summary:	URW fonts
Summary(pl.UTF-8):	Fonty URW
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-urw
URW fonts.

%description fonts-type1-urw -l pl.UTF-8
Fonty URW.

%package fonts-type1-vnr
Summary:	Type1 VNR fonts
Summary(pl.UTF-8):	Fonty Type1 VNR
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-vnr
Type1 VNR fonts.

%description fonts-type1-vnr -l pl.UTF-8
Fonty Type1 VNR.

%package fonts-type1-xypic
Summary:	Xy-pic fonts
Summary(pl.UTF-8):	Fonty Xy-pic
Group:		Fonts
Requires:	%{name}-dirs-fonts

%description fonts-type1-xypic
Xy-pic fonts.

%description fonts-type1-xypic -l pl.UTF-8
Fonty Xy-pic.

%prep
%setup -q -c -T -n %{name}-%{version}-source
lzma -dc %{SOURCE0} | tar xf - -C ..
lzma -dc %{SOURCE1} | tar xf - -C .
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
	--with-texmf-dir=../../texmf \
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
	$RPM_BUILD_ROOT/etc/sysconfig/tetex-updmap

# commented out because of following (non-fatal) error:
# Can't open texmf/web2c/texmf.cnf: No such file or directory.
#perl -pi \
#	-e "s|\.\./\.\./texmf|$RPM_BUILD_ROOT%{texmf}|g;" \
#	-e "s|/var/cache/fonts|$RPM_BUILD_ROOT/var/cache/fonts|g;" \
#	texmf/web2c/texmf.cnf

install -d $RPM_BUILD_ROOT%{texmf}/{dist,doc}
cp -a texlive-20080822-texmf/texmf/* $RPM_BUILD_ROOT%{texmf}
# cp -a texlive-20080822-texmf/texmf-dist/fonts/* $RPM_BUILD_ROOT%{texmf}/fonts
cp -a texlive-20080822-texmf/texmf-dist/dvips $RPM_BUILD_ROOT%{texmf}
cp -a texlive-20080822-texmf/texmf-dist/tex $RPM_BUILD_ROOT%{texmf}
cp -a texlive-20080822-texmf/texmf-dist/* $RPM_BUILD_ROOT%{texmf}/dist
cp -a texlive-20080822-texmf/texmf-doc/* $RPM_BUILD_ROOT%{texmf}/doc

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

#install %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}
#touch $RPM_BUILD_ROOT/etc/sysconfig/tetex-updmap/maps.lst

#%{__make} init \
#	prefix=$RPM_BUILD_ROOT%{_prefix} \
#	bindir=$RPM_BUILD_ROOT%{_bindir} \
#	mandir=$RPM_BUILD_ROOT%{_mandir} \
#	libdir=$RPM_BUILD_ROOT%{_libdir} \
#	datadir=$RPM_BUILD_ROOT%{_datadir} \
#	infodir=$RPM_BUILD_ROOT%{_infodir} \
#	includedir=$RPM_BUILD_ROOT%{_includedir} \
#	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
#	texmf=$RPM_BUILD_ROOT%{texmf}

perl -pi \
	-e "s|$RPM_BUILD_ROOT||g;" \
	$RPM_BUILD_ROOT%{texmf}/web2c/texmf.cnf

install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.daily/tetex

install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE6} $RPM_BUILD_ROOT%{_pixmapsdir}

# bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# in separate spec
rm -rf $RPM_BUILD_ROOT%{texmf}/tex/latex/{beamer,pgf,xcolor}
rm -rf $RPM_BUILD_ROOT%{texmf}/doc/latex/{beamer,pgf,xcolor}

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

%post latex-bbm
%texhash

%postun latex-bbm
%texhash

%post latex-bbold
%texhash

%postun latex-bbold
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

%post latex-concmath
%texhash

%postun latex-concmath
%texhash

%post latex-custom-bib
%texhash

%postun latex-custom-bib
%texhash

%post latex-cyrillic
%texhash

%postun latex-cyrillic
%texhash

%post latex-dstroke
%texhash

%postun latex-dstroke
%texhash

%post latex-jknappen
%texhash

%postun latex-jknappen
%texhash

%post latex-lm
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

%post latex-palatcm
%texhash

%postun latex-palatcm
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

%post latex-txfonts
%texhash

%postun latex-txfonts
%texhash

%post latex-umlaute
%texhash

%postun latex-umlaute
%texhash

%post latex-wasysym
%texhash

%postun latex-wasysym
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

%post tex-qtx
%texhash

%postun tex-qtx
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

%post fonts-qtx
%texhash

%postun fonts-qtx
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

%files
%defattr(644,root,root,755)
%docdir %{texmf}/doc
%dir %{texmf}/doc
%doc %{texmf}/LICENSE.texmf
%doc %{texmf}/ChangeLog
%doc %{texmf}/doc/README
%doc %{texmf}/doc/README.knuth
%dir %{texmf}/doc/tetex
%doc %{texmf}/doc/tetex/eurotex98-te.pdf
%doc %{texmf}/doc/tetex/TETEXDOC.*
%doc %{texmf}/doc/tetex/teTeX-FAQ
%doc %{texmf}/doc/tetex.gif
%doc %{texmf}/doc/tetex.png
%dir %{texmf}/doc/cstex
%doc %{texmf}/doc/fontinst
# There isn't doc/fonts directory
# %dir %{texmf}/doc/fonts
# %doc %{texmf}/doc/fonts/fontname
# %dir %{texmf}/doc/fonts/polish
%dir %{texmf}/doc/generic
%doc %{texmf}/doc/generic/nohyph
%doc %{texmf}/doc/generic/tex-ps
%dir %{texmf}/doc/help
%doc %{texmf}/doc/help/csname.txt
%doc %{texmf}/doc/help/ctan
%doc %{texmf}/doc/help/tds.dvi
%doc %{texmf}/doc/help/unixtex.ftp
%dir %{texmf}/doc/help/faq
%doc %{texmf}/doc/images
%dir %{texmf}/doc/latex
%dir %{texmf}/doc/polish
%doc %{texmf}/doc/polish/*.html
%dir %{texmf}/doc/programs
%doc %{texmf}/doc/programs/web2c*
%doc %{texmf}/doc/programs/cwebman.dvi
%doc %{texmf}/doc/programs/dvipng.*
%doc %{texmf}/doc/knuth

#%attr(755,root,root) %{_bindir}/MakeTeXPK
#%attr(755,root,root) %{_bindir}/access
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
%attr(755,root,root) %{_bindir}/fdf2tan
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
%attr(755,root,root) %{_bindir}/makempy
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
%attr(755,root,root) %{_bindir}/texexec
%attr(755,root,root) %{_bindir}/texhash
%attr(755,root,root) %{_bindir}/texi2html
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

%attr(750,root,root) /etc/cron.daily/tetex

#%dir /etc/sysconfig/tetex-updmap
#%verify(not md5 mtime size) %config(noreplace) /etc/sysconfig/tetex-updmap/maps.lst

%ghost %{texmf}/ls-R
%dir %{_localstatedir}
%dir %{_localstatedir}/fonts
%dir %{_localstatedir}/fonts/map
%ghost %{_localstatedir}/ls-R

%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/fmtutil.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktex.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktex.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktexdir.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktexnam.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/texmf.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/updmap.cfg

%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/fontmath.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/fonttext.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.dat
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/preload.cfg

%dir %{texmf}/dvips
%dir %{texmf}/dvips/config
%dir %{texmf}/dvips/tetex

%attr(1777,root,root) /var/cache/fonts

%{_datadir}/info/web2c.info*
%{_datadir}/info/texi2html.info*
%{_datadir}/texi2html
#%{texmf}/updates.dat

%{texmf}/aliases
%dir %{texmf}/scripts
%dir %{texmf}/tex
%{texmf}/tex/fontinst
%dir %{texmf}/tex/generic
%{texmf}/tex/generic/bghyph
%dir %{texmf}/tex/generic/config
%{texmf}/tex/generic/encodings
%doc %{texmf}/doc/generic/enctex
%{texmf}/tex/generic/enctex
%{texmf}/tex/generic/epsf
%doc %{texmf}/doc/generic/hyphen
%{texmf}/tex/generic/hyphen
#%{texmf}/tex/generic/letterspacing
%{texmf}/tex/generic/localloc
%{texmf}/tex/generic/null
%{texmf}/tex/generic/path
%{texmf}/tex/generic/random
%{texmf}/tex/generic/tap
%{texmf}/tex/generic/tex-ps
%{texmf}/tex/generic/texnames
%{texmf}/tex/texinfo
%dir %{texmf}/web2c
%{texmf}/web2c/*.tcx
%dir %{fmtdir}
%{fmtdir}/metafun.mem
#%{texmf}/web2c/tex-pl.pool
%{texmf}/web2c/tex.pool
%dir %{texmf}/fonts/map
%dir %{texmf}/fonts/map/dvips
#%{texmf}/fonts/map/dvips/updmap/ps2pk.map
%dir %{texmf}/fonts/map/dvips/tetex
%{texmf}/fonts/map/dvips/tetex/ps2pk35.map
%{texmf}/fonts/map/fontname
%dir %{texmf}/fonts/enc
%dir %{texmf}/fonts/enc/dvips
%dir %{texmf}/fonts/enc/dvips/tetex
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

%dir %{texmf}/fonts/enc/dvips/vntex
%{texmf}/fonts/enc/dvips/vntex/t5.enc

%{texmf}/fonts/map/dvips/tetex/contnav.map
%{texmf}/fonts/map/dvips/tetex/lumath-o.map
%dir %{texmf}/fonts/map/dvips/urwvn
%{texmf}/fonts/map/dvips/urwvn/urwvn.map

%lang(fi) %{_mandir}/fi/man1/afm2tfm.1*
%lang(fi) %{_mandir}/fi/man1/allcm.1*
%lang(fi) %{_mandir}/fi/man1/allneeded.1*
%lang(fr) %{_mandir}/fr/man1/access.1*
%lang(hu) %{_mandir}/hu/man1/access.1*
%lang(hu) %{_mandir}/hu/man1/newer.1*
%lang(pl) %{_mandir}/pl/man1/access.1*
%lang(pl) %{_mandir}/pl/man1/newer.1*
#%{_mandir}/man1/MakeTeXPK.1*
#%{_mandir}/man1/access.1*
#%{_mandir}/man1/fontexport.1*
#%{_mandir}/man1/fontimport.1*
#%{_mandir}/man1/initex.1*
#%{_mandir}/man1/t1mapper.1*
#%{_mandir}/man1/virtex.1*
#%{_mandir}/man8/mkfontdesc.8*
%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/allcm.1*
#%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*
%{_mandir}/man1/ctie.1*
%{_mandir}/man1/cweb.1*
%{_mandir}/man1/dmp.1*
%{_mandir}/man1/dvipdft.1*
%{_mandir}/man1/dvipng.1*
%{_mandir}/man1/e2pall.1*
%{_mandir}/man1/ebb.1*
%{_mandir}/man1/fmtutil.1*
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
#%{_mandir}/man1/mktexfmt.1*
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
%{_mandir}/man1/texdoc.1*
%{_mandir}/man1/texexec.1*
%{_mandir}/man1/texlinks.1*
#%{_mandir}/man1/texhash.1*
%{_mandir}/man1/texi2html.1*
%{_mandir}/man1/tftopl.1*
%{_mandir}/man1/ttf2afm.1*
%{_mandir}/man1/tie.1*
%{_mandir}/man1/updmap.1*
%{_mandir}/man1/vftovp.1*
%{_mandir}/man1/vptovf.1*
%{_mandir}/man1/weave.1*
%{_mandir}/man5/fmtutil.cnf.5*
#%{_mandir}/man8/fmtutil.8*
#%{_mandir}/man8/texlinks.8*

%files dirs-fonts
%defattr(644,root,root,755)
%dir %{texmf}
%dir %{texmf}/fonts
%dir %{texmf}/fonts/afm
%dir %{texmf}/fonts/afm/public
%dir %{texmf}/fonts/opentype
%dir %{texmf}/fonts/opentype/public
%dir %{texmf}/fonts/pk
%dir %{texmf}/fonts/source
%dir %{texmf}/fonts/source/public
%dir %{texmf}/fonts/tfm
%dir %{texmf}/fonts/tfm/public
%dir %{texmf}/fonts/type1
%dir %{texmf}/fonts/type1/public
%dir %{texmf}/fonts/vf
%dir %{texmf}/fonts/vf/public

%files doc-Catalogue
%defattr(644,root,root,755)
%{texmf}/doc/help/Catalogue

%files doc-tug-faq
%defattr(644,root,root,755)
%{texmf}/doc/help/faq/uktug-faq

%files doc-latex
%defattr(644,root,root,755)
%{texmf}/doc/latex/abstract
%{texmf}/doc/latex/acronym
%{texmf}/doc/latex/adrconv
%{texmf}/doc/latex/aeguill
%{texmf}/doc/latex/anysize
%{texmf}/doc/latex/appendix
%{texmf}/doc/latex/bar
%{texmf}/doc/latex/base
%{texmf}/doc/latex/beton
%{texmf}/doc/latex/bezos
%{texmf}/doc/latex/booktabs
%{texmf}/doc/latex/caption
%{texmf}/doc/latex/carlisle
%{texmf}/doc/latex/ccaption
%{texmf}/doc/latex/changebar
%{texmf}/doc/latex/chappg
%{texmf}/doc/latex/comment
%{texmf}/doc/latex/concmath
%{texmf}/doc/latex/crop
%{texmf}/doc/latex/currvita
%{texmf}/doc/latex/curves
%{texmf}/doc/latex/dinbrief
%{texmf}/doc/latex/draftcopy
%{texmf}/doc/latex/eclbip
%{texmf}/doc/latex/eepic
%{texmf}/doc/latex/endfloat
%{texmf}/doc/latex/enumitem
%{texmf}/doc/latex/eo
%{texmf}/doc/latex/esint
%{texmf}/doc/latex/eso-pic
%{texmf}/doc/latex/euler
%{texmf}/doc/latex/eulervm
%{texmf}/doc/latex/exam
%{texmf}/doc/latex/extsizes
%{texmf}/doc/latex/fancybox
%{texmf}/doc/latex/fancyhdr
%{texmf}/doc/latex/fancyvrb
%{texmf}/doc/latex/filecontents
%{texmf}/doc/latex/float
%{texmf}/doc/latex/floatflt
%{texmf}/doc/latex/footmisc
%{texmf}/doc/latex/footnpag
%{texmf}/doc/latex/fp
%{texmf}/doc/latex/g-brief
%{texmf}/doc/latex/general
%{texmf}/doc/latex/geometry
%{texmf}/doc/latex/germbib
%{texmf}/doc/latex/graphics
%{texmf}/doc/latex/hyperref
%{texmf}/doc/latex/hyphenat
%{texmf}/doc/latex/images
%{texmf}/doc/latex/index
%{texmf}/doc/latex/koma-script
%{texmf}/doc/latex/labels
%{texmf}/doc/latex/lastpage
%{texmf}/doc/latex/layouts
%{texmf}/doc/latex/leftidx
%{texmf}/doc/latex/lettrine
%{texmf}/doc/latex/listings
%{texmf}/doc/latex/ltabptch
%{texmf}/doc/latex/mathcomp
%{texmf}/doc/latex/mdwtools
%{texmf}/doc/latex/memoir
%{texmf}/doc/latex/mh
%{texmf}/doc/latex/moreverb
%{texmf}/doc/latex/mparhack
%{texmf}/doc/latex/ms
%{texmf}/doc/latex/mt11p
%{texmf}/doc/latex/multibib
%{texmf}/doc/latex/mwcls
%{texmf}/doc/latex/natbib
%{texmf}/doc/latex/nomencl
%{texmf}/doc/latex/ntgclass
%{texmf}/doc/latex/ntheorem
%{texmf}/doc/latex/oberdiek
%{texmf}/doc/latex/overpic
%{texmf}/doc/latex/paralist
%{texmf}/doc/latex/pb-diagram
%{texmf}/doc/latex/pdfpages
%{texmf}/doc/latex/picinpar
%{texmf}/doc/latex/picins
%{texmf}/doc/latex/pict2e
%{texmf}/doc/latex/placeins
%{texmf}/doc/latex/preprint
%{texmf}/doc/latex/preview
%{texmf}/doc/latex/program
%{texmf}/doc/latex/ps4pdf
%{texmf}/doc/latex/psfrag
%{texmf}/doc/latex/pslatex
%{texmf}/doc/latex/revtex4
%{texmf}/doc/latex/rotating
%{texmf}/doc/latex/rotfloat
%{texmf}/doc/latex/scale
%{texmf}/doc/latex/sectsty
%{texmf}/doc/latex/seminar
%{texmf}/doc/latex/shapepar
%{texmf}/doc/latex/showlabels
%{texmf}/doc/latex/sidecap
%{texmf}/doc/latex/SIunits
%{texmf}/doc/latex/slashbox
%{texmf}/doc/latex/soul
%{texmf}/doc/latex/stdclsdv
%{texmf}/doc/latex/subfig
%{texmf}/doc/latex/subfigure
%{texmf}/doc/latex/supertab
%{texmf}/doc/latex/tex-refs
%{texmf}/doc/latex/textfit
%{texmf}/doc/latex/textmerg
%{texmf}/doc/latex/textpos
%{texmf}/doc/latex/titlesec
%{texmf}/doc/latex/tocbibind
%{texmf}/doc/latex/tocloft
%{texmf}/doc/latex/tools
%{texmf}/doc/latex/totpages
%{texmf}/doc/latex/treesvr
%{texmf}/doc/latex/type1cm
%{texmf}/doc/latex/units
%{texmf}/doc/latex/vmargin
%{texmf}/doc/latex/was
%{texmf}/doc/latex/wrapfig
%{texmf}/doc/latex/xtab
%{texmf}/doc/latex/yfonts

%files -n kpathsea
%defattr(644,root,root,755)
%doc %{texmf}/doc/programs/kpathsea.dvi
%doc %{texmf}/doc/programs/kpathsea.pdf
%attr(755,root,root) %{_bindir}/kpsepath
%attr(755,root,root) %{_bindir}/kpsestat
%attr(755,root,root) %{_bindir}/kpsetool
%attr(755,root,root) %{_bindir}/kpsewhich
%attr(755,root,root) %{_bindir}/kpsexpand
%attr(755,root,root) %{_libdir}/libkpathsea.so.*
%{_libdir}/libkpathsea.la
#%{_mandir}/man1/kpsepath.1*
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsetool.1*
%{_mandir}/man1/kpsewhich.1*
#%{_mandir}/man1/kpsexpand.1*

%files -n kpathsea-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkpathsea.so
%{_includedir}/kpathsea
%{_infodir}/kpathsea.info*

%files dvips
%defattr(644,root,root,755)
%doc %{texmf}/doc/programs/dvips.dvi
%doc %{texmf}/doc/programs/dvips.pdf
%doc %{texmf}/doc/programs/dvipdfm.dvi
%doc %{texmf}/doc/programs/dvipdfm.pdf
%doc %{texmf}/doc/latex/psnfssx
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
%lang(fi) %{_mandir}/fi/man1/dvips.1*
%{texmf}/dvips/base
%{texmf}/dvips/misc
%{texmf}/dvips/gsftopk
%{texmf}/dvips/psfrag

%config(noreplace) %verify(not md5 mtime size) %{texmf}/dvips/config/config.ps
%{texmf}/dvips/config/config.generic
%{texmf}/dvips/tetex/config.*

%{texmf}/fonts/enc/dvips/base
%{texmf}/fonts/enc/dvips/tetex/mtex.enc
%{texmf}/fonts/map/dvipdfm
%{texmf}/fonts/map/dvips/misc
%{texmf}/fonts/map/dvips/tetex/bsr-interpolated.map
%{texmf}/fonts/map/dvips/tetex/bsr.map
%{texmf}/fonts/map/dvips/tetex/dvipdfm35.map
%{texmf}/fonts/map/dvips/tetex/dvips35.map
%{texmf}/fonts/map/dvips/tetex/mathpple.map
%{texmf}/fonts/map/dvips/tetex/mt-belleek.map
%{texmf}/fonts/map/dvips/tetex/mt-plus.map
%{texmf}/fonts/map/dvips/tetex/mt-yy.map
%{texmf}/fonts/map/dvips/tetex/pdftex35.map
%{texmf}/fonts/map/dvips/tetex/ttcmex.map
%{_localstatedir}/fonts/map/dvipdfm
%{_localstatedir}/fonts/map/dvips

%dir %{texmf}/dvipdfm
%{texmf}/dvipdfm/config

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

%files makeindex
%defattr(644,root,root,755)
%doc %{texmf}/doc/makeindex

%attr(755,root,root) %{_bindir}/mkindex
%attr(755,root,root) %{_bindir}/makeindex
%attr(755,root,root) %{_bindir}/rumakeindex

%{texmf}/makeindex

%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/mkindex.1*
%{_mandir}/man1/rumakeindex.1*

%files metafont
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mf
%attr(755,root,root) %{_bindir}/mf-nowin
%attr(755,root,root) %{_bindir}/mft
#%attr(755,root,root) %{_bindir}/mfw
#%attr(755,root,root) %{_bindir}/virmf
#%attr(755,root,root) %{_bindir}/inimf
%attr(755,root,root) %{_bindir}/mktexmf
%attr(755,root,root) %{_bindir}/mktexpk
%attr(755,root,root) %{_bindir}/mktextfm
%{texmf}/metafont
%dir %{texmf}/mft
%{texmf}/mft/cmbase.mft
%{texmf}/mft/e.mft
%{texmf}/mft/mplain.mft
%{texmf}/mft/plain.mft
%{texmf}/mft/pl.mft
%{fmtdir}/mf.base
#%{texmf}/web2c/mf-nowin.base
%{texmf}/web2c/mf.pool
#%{texmf}/web2c/mfw.base

%{_mandir}/man1/mf.1*
%{_mandir}/man1/mft.1*
#%{_mandir}/man1/inimf.1*
#%{_mandir}/man1/virmf.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*

%files metapost
%defattr(644,root,root,755)
%doc %{texmf}/doc/metapost
%attr(755,root,root) %{_bindir}/mpost
%attr(755,root,root) %{_bindir}/mpto
#%attr(755,root,root) %{_bindir}/virmpost
#%attr(755,root,root) %{_bindir}/inimpost
%dir %{texmf}/metapost
%{texmf}/metapost/base
%{texmf}/metapost/config
%{texmf}/metapost/mfpic
%{texmf}/metapost/misc
%{texmf}/metapost/support
%{texmf}/web2c/mp.pool
%{fmtdir}/mpost.mem
%{_mandir}/man1/mpost.1*
%{_mandir}/man1/mpto.1*
#%{_mandir}/man1/inimpost.1*
#%{_mandir}/man1/virmpost.1*

%files mptopdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mptopdf
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/mptopdf.fmt

%files texdoctk
%defattr(644,root,root,755)
%doc %{texmf}/doc/texdoctk
%attr(755,root,root) %{_bindir}/texdoctk
%{texmf}/texdoctk

%{_mandir}/man1/texdoctk.1*

%files -n texconfig
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/texconfig
%attr(755,root,root) %{_bindir}/texconfig-dialog
%attr(755,root,root) %{_bindir}/texconfig-sys
%attr(755,root,root) %{texmf}/texconfig/tcfmgr
%{_mandir}/man1/texconfig.1*
%dir %{texmf}/texconfig
%{texmf}/texconfig/tcfmgr.map
%{texmf}/texconfig/generic
%doc %{texmf}/texconfig/README
%{texmf}/texconfig/v
%{texmf}/texconfig/g
%{texmf}/texconfig/x

%files -n xdvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdvi
%attr(755,root,root) %{_bindir}/xdvi-xaw.bin
#%attr(755,root,root) %{_bindir}/xdvi-motif.bin
%attr(755,root,root) %{_bindir}/xdvizilla
%{_mandir}/man1/xdvi.1*
%{_mandir}/man1/xdvizilla.1*
%{_desktopdir}/xdvi.desktop
%{_pixmapsdir}/xdvi.png
%{texmf}/xdvi

%files pdftex
%defattr(644,root,root,755)
%doc %{texmf}/doc/pdftex
%doc %{texmf}/doc/programs/pdfcrop.txt
%attr(755,root,root) %{_bindir}/epstopdf
%attr(755,root,root) %{_bindir}/pdftex
%attr(755,root,root) %{_bindir}/pdfxtex
%attr(755,root,root) %{_bindir}/pdfcrop
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/pdftexconfig.tex
%{_localstatedir}/fonts/map/pdftex
%dir %{texmf}/fonts/map/pdftex
%dir %{texmf}/fonts/map/pdftex/cmttf
%{texmf}/fonts/map/pdftex/cmttf/cmttf.map
%{texmf}/web2c/pdfetex-pl.pool
%{texmf}/web2c/pdfetex.pool
%{texmf}/web2c/pdfxtex.pool
%{texmf}/scripts/pdfcrop
%{_mandir}/man1/epstopdf.1*
%{_mandir}/man1/pdftex.1*
%{_mandir}/man1/pdfxtex.1*

%files omega
%defattr(644,root,root,755)
%doc %{texmf}/doc/omega
%dir %{texmf}/omega
%dir %{texmf}/dvips/omega
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
%{texmf}/dvips/omega/config.omega
%{texmf}/dvips/omega/omega.cfg
%{texmf}/fonts/map/dvips/omega
%{texmf}/tex/lambda
%{texmf}/omega/ocp
%{texmf}/omega/otp
%{texmf}/web2c/omega.pool
%{texmf}/web2c/aleph.pool
#%{_mandir}/man1/lambda.1*
%{_mandir}/man1/mkocp.1*
%{_mandir}/man1/mkofm.1*
%{_mandir}/man1/omega.1*
%{_mandir}/man1/ofm2opl.1*
%{_mandir}/man1/opl2ofm.1*
%{_mandir}/man1/otp2ocp.1*
%{_mandir}/man1/outocp.1*
%{_mandir}/man1/ovf2ovp.1*
%{_mandir}/man1/ovp2ovf.1*

%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/aleph.fmt
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/lambda.fmt
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/lamed.fmt
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/omega.fmt

%files plain
%defattr(644,root,root,755)
%doc %{texmf}/doc/plain
%{texmf}/tex/plain
#%{texmf}/web2c/plain.mem
#%{texmf}/web2c/plain.base

%files format-plain
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/tex.fmt
#%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/plain.fmt

%files format-pdftex
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdftex.fmt

%files format-pdfetex
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdfetex.fmt

%files mex
%defattr(644,root,root,755)
%doc %{texmf}/doc/polish/mex
%dir %{texmf}/tex/mex
%dir %{texmf}/tex/mex/base
%{texmf}/tex/mex/base/mex1.tex
%{texmf}/tex/mex/base/mex2.tex
%{texmf}/tex/mex/base/mex.tex
%dir %{texmf}/tex/mex/config
%{texmf}/tex/mex/config/mexconf.tex

%files format-mex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mex
%{texmf}/tex/mex/config/mex.ini
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/mex.fmt

%files format-pdfmex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfmex
%{texmf}/tex/mex/config/pdfmex.ini
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdfmex.fmt

%files format-utf8mex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/utf8mex
#%doc %{texmf}/doc/mex/utf8mex
%{texmf}/tex/mex/utf8mex
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/utf8mex.fmt

%files amstex
%defattr(644,root,root,755)
%dir %{texmf}/tex/amstex
%{texmf}/tex/amstex/base
%{texmf}/tex/amstex/config
%{texmf}/tex/plain/amsfonts

%files format-amstex
%defattr(644,root,root,755)
%doc %{texmf}/doc/amstex
%attr(755,root,root) %{_bindir}/amstex
%{_mandir}/man1/amstex.1*
%lang(fi) %{_mandir}/fi/man1/amstex.1*
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/amstex.fmt

%files format-pdfamstex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfamstex
#%{texmf}/pdftex/amstex
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdfamstex.fmt

%files csplain
%defattr(644,root,root,755)
%doc %{texmf}/doc/cstex/README-cspsfont
%doc %{texmf}/doc/cstex/cs-fonts.doc
%doc %{texmf}/doc/cstex/cscorr.tab
%doc %{texmf}/doc/cstex/csplain.doc
%doc %{texmf}/doc/cstex/parpozn.tex
%doc %{texmf}/doc/cstex/test8z.tex
%doc %{texmf}/doc/cstex/testlat.tex
%attr(755,root,root) %{_bindir}/csplain
%{texmf}/tex/csplain
%{texmf}/tex/generic/csplain

%files format-csplain
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/csplain.fmt

%files format-pdfcsplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfcsplain
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdfcsplain.fmt

%files cslatex
%defattr(644,root,root,755)
%doc %{texmf}/doc/cstex/INSTALL.cslatex
%doc %{texmf}/doc/cstex/README.cslatex
%{texmf}/tex/cslatex
%{texmf}/tex/latex/cslatex

%files format-cslatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cslatex
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cslatex.fmt

%files format-pdfcslatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfcslatex
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdfcslatex.fmt

%files cyrplain
%defattr(644,root,root,755)
%doc %{texmf}/doc/cyrplain
%{texmf}/tex/cyrplain

%files format-cyrplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cyrtex
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cyrtex.fmt

%files format-cyramstex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cyramstex
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cyramstex.fmt

%files format-cyrtexinfo
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cyrtexinfo
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cyrtexinfo.fmt

%files eplain
%defattr(644,root,root,755)
%doc %{texmf}/doc/etex
%doc %{texmf}/doc/eplain
%{texmf}/tex/plain/etex
%{texmf}/tex/eplain

%files format-eplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eplain
%attr(755,root,root) %{_bindir}/etex
%{_mandir}/man1/eplain.1*
%{_mandir}/man1/etex.1*
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/eplain.fmt
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/etex.fmt

%files context
%defattr(644,root,root,755)
%doc %{texmf}/doc/context
%doc %{texmf}/doc/polish/context
%dir %{texmf}/context
%dir %{texmf}/context/config
%dir %{texmf}/tex/context
%dir %{texmf}/tex/context/config
%attr(755,root,root) %{_bindir}/texfind
%attr(755,root,root) %{_bindir}/texfont
%attr(755,root,root) %{_bindir}/texshow
%attr(755,root,root) %{_bindir}/texutil
%{_mandir}/man1/fdf2tex.1*
%{_mandir}/man1/texfind.1*
%{_mandir}/man1/texfont.1*
%{_mandir}/man1/texutil.1*
%{_mandir}/man1/texshow.1*
%{texmf}/context/config/texexec.ini
%{texmf}/context/config/texexec.rme
%{texmf}/context/data
%{texmf}/fonts/enc/dvips/context
%{texmf}/fonts/map/dvips/context
%{texmf}/metapost/context
%{texmf}/scripts/context
%{texmf}/tex/latex/context
%{texmf}/tex/context/base
%{texmf}/tex/context/bib
%{texmf}/tex/context/config/cont-usr.tex
%{texmf}/tex/context/extra
%{texmf}/tex/context/foxet
%{texmf}/tex/context/interface
%{texmf}/tex/context/maths
%{texmf}/tex/context/sample
%{texmf}/tex/context/user
%{texmf}/tex/generic/context
%{texmf}/bibtex/bst/context

# no fmt, so commented out
#%files format-context-cz
#%defattr(644,root,root,755)
#%%{texmf}/tex/context/config/cont-cz.ini
# does not build with beta 20021025
#%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cont-cz.efmt

%files format-context-de
%defattr(644,root,root,755)
%{texmf}/tex/context/config/cont-de.ini
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cont-de.fmt
#%{_mandir}/man1/cont-de.1*

%files format-context-en
%defattr(644,root,root,755)
%{texmf}/tex/context/config/cont-en.ini
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cont-en.fmt
#%{_mandir}/man1/cont-en.1*
# what is the difference betwen uk and en in this particular situation?
%{texmf}/tex/context/config/cont-uk.ini
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cont-uk.fmt

# no fmt, so commented out
#%files format-context-it
#%defattr(644,root,root,755)
#%%{texmf}/tex/context/config/cont-it.ini

%files format-context-nl
%defattr(644,root,root,755)
%{texmf}/tex/context/config/cont-nl.ini
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/cont-nl.fmt
#%{_mandir}/man1/cont-nl.1*

# no fmt, so commented out
#%files format-context-ro
#%defattr(644,root,root,755)
#%%{texmf}/tex/context/config/cont-ro.ini

%files latex
%defattr(644,root,root,755)
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pslatex.1*
%lang(fi) %{_mandir}/fi/man1/latex.1*
%lang(pl) %{_mandir}/pl/man1/latex.1*
%{_infodir}/latex.info*

%dir %{texmf}/tex/latex

%{texmf}/tex/latex/SIunits
%{texmf}/tex/latex/a4wide
%{texmf}/tex/latex/abstract
%{texmf}/tex/latex/acronym
%{texmf}/tex/latex/adrconv
%{texmf}/tex/latex/aeguill
%{texmf}/tex/latex/anysize
%{texmf}/tex/latex/appendix
%{texmf}/tex/latex/bar
%{texmf}/tex/latex/base
%{texmf}/tex/latex/beton
%{texmf}/tex/latex/bezos
%{texmf}/tex/latex/bold-extra
%{texmf}/tex/latex/booktabs
%{texmf}/tex/latex/boxedminipage
%{texmf}/tex/latex/calrsfs
%{texmf}/tex/latex/cancel
%{texmf}/tex/latex/capt-of
%{texmf}/tex/latex/caption
%{texmf}/tex/latex/ccaption
%{texmf}/tex/latex/changebar
%{texmf}/tex/latex/chappg
%{texmf}/tex/latex/chngpage
%{texmf}/tex/latex/citesort
%{texmf}/tex/latex/cmap
%{texmf}/tex/latex/comment
%{texmf}/tex/latex/concrete
%{texmf}/tex/latex/config
%{texmf}/tex/latex/crop
%{texmf}/tex/latex/currvita
%{texmf}/tex/latex/curves
%{texmf}/tex/latex/dinbrief
%{texmf}/tex/latex/draftcopy
%{texmf}/tex/latex/dvilj
%{texmf}/tex/latex/dvipdfm
%{texmf}/tex/latex/eclbip
%{texmf}/tex/latex/eepic
%{texmf}/tex/latex/endfloat
%{texmf}/tex/latex/endnotes
%{texmf}/tex/latex/enumitem
%{texmf}/tex/latex/eo
%{texmf}/tex/latex/eso-pic
%{texmf}/tex/latex/etex
%{texmf}/tex/latex/esint
%{texmf}/tex/latex/euler
%{texmf}/tex/latex/eulervm
%{texmf}/tex/latex/eurosym
%{texmf}/tex/latex/exam
%{texmf}/tex/latex/example
%{texmf}/tex/latex/extsizes
%{texmf}/tex/latex/fancybox
%{texmf}/tex/latex/fancyhdr
%{texmf}/tex/latex/fancyheadings
%{texmf}/tex/latex/fancyvrb
%{texmf}/tex/latex/fguill
%{texmf}/tex/latex/filecontents
%{texmf}/tex/latex/float
%{texmf}/tex/latex/floatflt
%{texmf}/tex/latex/fnpara
%{texmf}/tex/latex/fontinst
%{texmf}/tex/latex/footmisc
%{texmf}/tex/latex/footnpag
%{texmf}/tex/latex/fp
%{texmf}/tex/latex/framed
%{texmf}/tex/latex/g-brief
%{texmf}/tex/latex/geometry
%{texmf}/tex/latex/germbib
%{texmf}/tex/latex/gletter
%{texmf}/tex/latex/graphics
%{texmf}/tex/latex/greek
%{texmf}/tex/latex/hangcaption
%{texmf}/tex/latex/here
%{texmf}/tex/latex/hyperref
%{texmf}/tex/latex/hyphenat
%{texmf}/tex/latex/import
%{texmf}/tex/latex/index
%{texmf}/tex/latex/koma-script
%{texmf}/tex/latex/labels
%{texmf}/tex/latex/lastpage
%{texmf}/tex/latex/layouts
%{texmf}/tex/latex/leftidx
%{texmf}/tex/latex/lettrine
%{texmf}/tex/latex/listings
%{texmf}/tex/latex/ltabptch
%{texmf}/tex/latex/mathcomp
%{texmf}/tex/latex/mdwtools
%{texmf}/tex/latex/memoir
%{texmf}/tex/latex/mh
%{texmf}/tex/latex/moreverb
%{texmf}/tex/latex/mparhack
%{texmf}/tex/latex/ms
%{texmf}/tex/latex/mt11p
%{texmf}/tex/latex/multibib
%{texmf}/tex/latex/multibox
%{texmf}/tex/latex/multind
%{texmf}/tex/latex/multirow
%{texmf}/tex/latex/mwcls
%{texmf}/tex/latex/natbib
%{texmf}/tex/latex/nextpage
%{texmf}/tex/latex/ntheorem
%{texmf}/tex/latex/nomencl
%{texmf}/tex/latex/ntgclass
%{texmf}/tex/latex/oberdiek
%{texmf}/tex/latex/optional
%{texmf}/tex/latex/overpic
%{texmf}/tex/latex/paralist
%{texmf}/tex/latex/parskip
%{texmf}/tex/latex/pb-diagram
%{texmf}/tex/latex/pdfpages
%{texmf}/tex/latex/picinpar
%{texmf}/tex/latex/picins
%{texmf}/tex/latex/pict2e
%{texmf}/tex/latex/placeins
%{texmf}/tex/latex/portland
%{texmf}/tex/latex/preprint
%{texmf}/tex/latex/preview
%{texmf}/tex/latex/program
%{texmf}/tex/latex/ps4pdf
%{texmf}/tex/latex/psboxit
%{texmf}/tex/latex/psfrag
%{texmf}/tex/latex/pslatex
%{texmf}/tex/latex/pstricks
%{texmf}/tex/latex/relsize
%{texmf}/tex/latex/revtex4
%{texmf}/tex/latex/rotating
%{texmf}/tex/latex/rotfloat
%{texmf}/tex/latex/scale
%{texmf}/tex/latex/sectsty
%{texmf}/tex/latex/selectp
%{texmf}/tex/latex/seminar
%{texmf}/tex/latex/setspace
%{texmf}/tex/latex/shadow
%{texmf}/tex/latex/shapepar
%{texmf}/tex/latex/showdim
%{texmf}/tex/latex/showlabels
%{texmf}/tex/latex/showtags
%{texmf}/tex/latex/sidecap
%{texmf}/tex/latex/slashbox
%{texmf}/tex/latex/soul
%{texmf}/tex/latex/stdclsdv
%{texmf}/tex/latex/stmaryrd
%{texmf}/tex/latex/subfig
%{texmf}/tex/latex/subfigure
%{texmf}/tex/latex/supertabular
%{texmf}/tex/latex/t2
%{texmf}/tex/latex/tabls
%{texmf}/tex/latex/texmacs
%{texmf}/tex/latex/textfit
%{texmf}/tex/latex/textmerg
%{texmf}/tex/latex/textpos
%{texmf}/tex/latex/threeparttable
%{texmf}/tex/latex/titlesec
%{texmf}/tex/latex/tocbibind
%{texmf}/tex/latex/tocloft
%{texmf}/tex/latex/tools
%{texmf}/tex/latex/totpages
%{texmf}/tex/latex/treesvr
%{texmf}/tex/latex/type1cm
%{texmf}/tex/latex/ulem
%{texmf}/tex/latex/units
%{texmf}/tex/latex/upquote
%{texmf}/tex/latex/url
%{texmf}/tex/latex/vmargin
%{texmf}/tex/latex/vpage
%{texmf}/tex/latex/was
%{texmf}/tex/latex/wrapfig
%{texmf}/tex/latex/xkeyval
%{texmf}/tex/latex/xtab
%{texmf}/tex/latex/yfonts
%{texmf}/tex/latex/version

%files latex-algorithms
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/algorithms
%{texmf}/tex/latex/algorithms

%files latex-ae
%defattr(644,root,root,755)
%{texmf}/tex/latex/ae

%files latex-ams
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/amscls
%doc %{texmf}/doc/latex/amsmath
%doc %{texmf}/doc/latex/amsfonts
%doc %{texmf}/doc/latex/onlyamsmath
%{texmf}/tex/latex/amscls
%{texmf}/tex/latex/amsmath
%{texmf}/tex/latex/amsfonts
%{texmf}/tex/latex/onlyamsmath

%files latex-antp
%defattr(644,root,root,755)
%{texmf}/tex/latex/antp

%files latex-antt
%defattr(644,root,root,755)
%{texmf}/tex/latex/antt

%files latex-bbm
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/bbm
%{texmf}/tex/latex/bbm

%files latex-bbold
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/bbold
%{texmf}/tex/latex/bbold

%files latex-bibtex
%defattr(644,root,root,755)
%doc %{texmf}/doc/bibtex/base
%doc %{texmf}/bibtex/bib/README
%doc %{texmf}/doc/latex/bibtopic
%doc %{texmf}/doc/latex/bibunits
%doc %{texmf}/doc/latex/footbib
%dir %{texmf}/doc/bibtex
%dir %{texmf}/bibtex
%dir %{texmf}/bibtex/bib
%dir %{texmf}/bibtex/bst

%attr(755,root,root) %{_bindir}/bibtex
%attr(755,root,root) %{_bindir}/rubibtex

%{texmf}/bibtex/bib/base
%{texmf}/bibtex/bst/adrconv
%{texmf}/bibtex/bst/base
%{texmf}/bibtex/bst/misc
%{texmf}/bibtex/bst/natbib
%{texmf}/tex/latex/bibtopic
%{texmf}/tex/latex/bibunits
%{texmf}/tex/latex/footbib

%{_mandir}/man1/bibtex.1*
%{_mandir}/man1/rubibtex.1*

%files latex-bibtex-ams
%defattr(644,root,root,755)
%{texmf}/bibtex/bib/ams
%{texmf}/bibtex/bst/ams

%files latex-bibtex-pl
%defattr(644,root,root,755)
%{texmf}/bibtex/bib/plbib
%{texmf}/bibtex/bst/plbib

%files latex-bibtex-german
%defattr(644,root,root,755)
%doc %{texmf}/doc/bibtex/bibgerm
%{texmf}/bibtex/bst/germbib

%files latex-bibtex-revtex4
%defattr(644,root,root,755)
%{texmf}/bibtex/bst/revtex4

%files latex-bibtex-jurabib
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/jurabib
%{texmf}/bibtex/bst/jurabib
%{texmf}/tex/latex/jurabib

%files latex-bibtex-dk
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/dk-bib
%{texmf}/bibtex/bst/dk-bib
%{texmf}/tex/latex/dk-bib

%files latex-bibtex-nor
%defattr(644,root,root,755)
%{texmf}/bibtex/bst/norbib

%files latex-carlisle
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/carlisle
%{texmf}/tex/latex/carlisle

%files latex-ccfonts
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/ccfonts
%{texmf}/tex/latex/ccfonts

%files latex-cite
%defattr(644,root,root,755)
%{texmf}/tex/latex/cite

%files latex-cmbright
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/cmbright
%{texmf}/tex/latex/cmbright

%files latex-concmath
%defattr(644,root,root,755)
%{texmf}/tex/latex/concmath

%files latex-custom-bib
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/custom-bib
%{texmf}/tex/latex/custom-bib

%files latex-cyrillic
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/cyrillic
%{texmf}/tex/latex/cyrillic

%files latex-dstroke
%defattr(644,root,root,755)
%{texmf}/tex/latex/dstroke

%files latex-jknappen
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/jknappen
%doc %{texmf}/doc/fonts/ec
%{texmf}/tex/latex/jknappen

%files latex-lm
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/lm
%{texmf}/tex/latex/lm
%{texmf}/fonts/enc/dvips/lm
%{texmf}/fonts/map/dvips/lm

%files latex-lucidabr
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/lucida
%{texmf}/fonts/map/dvips/lucida
%{texmf}/fonts/map/dvips/tetex/lucidabr-o.map
%{texmf}/tex/latex/lucidabr
%{texmf}/tex/latex/lucida

%files latex-lineno
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/lineno
%{texmf}/tex/latex/lineno

%files latex-marvosym
%defattr(644,root,root,755)
%{texmf}/tex/latex/marvosym

%files latex-mathpple
%defattr(644,root,root,755)
%{texmf}/tex/latex/mathpple

%files latex-mathtime
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mathtime
%doc %{texmf}/doc/fonts/mathtime
%{texmf}/tex/latex/mathtime

%files latex-microtype
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/microtype
%{texmf}/tex/latex/microtype

%files latex-mflogo
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mflogo
%{texmf}/tex/latex/mflogo

%files latex-mfnfss
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mfnfss
%{texmf}/tex/latex/mfnfss

%files latex-minitoc
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/minitoc
%{texmf}/tex/latex/minitoc

%files latex-mltex
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mltex
%{texmf}/tex/latex/mltex

%files latex-palatcm
%defattr(644,root,root,755)
%{texmf}/tex/latex/palatcm

%files latex-psnfss
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/psnfss
%{texmf}/fonts/enc/dvips/psnfss
%{texmf}/fonts/enc/dvips/psnfssx
%{texmf}/fonts/map/dvips/psnfss
%{texmf}/fonts/map/dvips/psnfssx
%{texmf}/tex/latex/psnfss
%{texmf}/tex/latex/psnfssx

%files latex-pxfonts
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/pxfonts
%{texmf}/tex/latex/pxfonts

%files latex-qfonts
%defattr(644,root,root,755)
%{texmf}/tex/latex/qfonts

%files latex-txfonts
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/txfonts
%{texmf}/tex/latex/txfonts

%files latex-umlaute
%defattr(644,root,root,755)
%{texmf}/tex/latex/umlaute

%files latex-urwvn
%defattr(644,root,root,755)
%{texmf}/tex/latex/urwvn

%files latex-wasysym
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/wasysym
%{texmf}/tex/latex/wasysym

%files format-latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/latex
%attr(755,root,root) %{_bindir}/pslatex
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/latex.fmt

%files format-pdflatex
%defattr(644,root,root,755)
#%{texmf}/pdftex/latex/config
#%dir %{texmf}/pdftex/latex
%attr(755,root,root) %{_bindir}/pdflatex
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdflatex.fmt
#%{_mandir}/man1/pdflatex.1*

%files platex
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/platex
%dir %{texmf}/tex/platex
%{texmf}/tex/platex/config
%{texmf}/tex/latex/platex

%files format-platex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/platex
#%attr(755,root,root) %{_bindir}/platex-pl
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/platex.fmt
#%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/platex-pl.fmt

%files format-pdfplatex
%defattr(644,root,root,755)
#%dir %{texmf}/pdftex/platex
#%{texmf}/pdftex/platex/config
%attr(755,root,root) %{_bindir}/pdfplatex
%config(noreplace) %verify(not md5 mtime size) %{fmtdir}/pdfplatex.fmt

%files tex-babel
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/babel
%{texmf}/tex/generic/babel

%files tex-german
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/german
%{texmf}/tex/generic/german

%files tex-mfpic
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/mfpic
%{texmf}/tex/generic/mfpic

%files tex-misc
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/localloc
%doc %{texmf}/doc/generic/multido
%doc %{texmf}/doc/generic/tap

%{texmf}/tex/generic/eijkhout
%{texmf}/tex/generic/multido
#%{texmf}/tex/generic/misc

%files tex-pictex
%defattr(644,root,root,755)
%{texmf}/tex/generic/pictex

%files tex-pstricks
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/pstricks
%{texmf}/dvips/pstricks
%{texmf}/tex/generic/pstricks

%files tex-qpx
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/qpx
%{texmf}/tex/generic/qpx

%files tex-qtx
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/qtx
%{texmf}/tex/generic/qtx

%files tex-ruhyphen
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/ruhyphen
%{texmf}/tex/generic/ruhyphen

%files tex-spanish
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/spanish
%{texmf}/tex/generic/spanishb

%files tex-texdraw
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/texdraw
%{texmf}/tex/generic/texdraw

%files tex-thumbpdf
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/thumbpdf
%attr(755,root,root) %{_bindir}/thumbpdf
%{texmf}/tex/generic/thumbpdf
%{texmf}/scripts/thumbpdf
%{_mandir}/man1/thumbpdf.1*

%files tex-ukrhyph
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/ukrhyph
%{texmf}/tex/generic/ukrhyph

%files latex-vietnam
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/vntex
%{texmf}/tex/latex/vietnam

%files tex-xypic
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/xypic
%{texmf}/tex/generic/xypic

%files tex-xkeyval
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/xkeyval
%{texmf}/tex/generic/xkeyval

%files fonts-adobe
%defattr(644,root,root,755)
%{texmf}/fonts/afm/adobe
%{texmf}/fonts/tfm/adobe
%{texmf}/fonts/vf/adobe

%files fonts-ae
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/ae
%{texmf}/fonts/tfm/public/ae
%{texmf}/fonts/vf/public/ae

%files fonts-ams
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/amsfonts
%{texmf}/fonts/map/dvips/ams
%{texmf}/fonts/source/ams
%{texmf}/fonts/tfm/ams

%files fonts-antp
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/antp
%{texmf}/fonts/enc/dvips/antp
%{texmf}/fonts/map/dvips/antp
%{texmf}/fonts/afm/public/antp
%{texmf}/fonts/tfm/public/antp

%files fonts-antt
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/antt
%{texmf}/fonts/enc/dvips/antt
%{texmf}/fonts/map/dvips/antt
%{texmf}/fonts/afm/public/antt
%{texmf}/fonts/tfm/public/antt

%files fonts-bbm
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/bbm
%{texmf}/fonts/tfm/public/bbm

%files fonts-bbold
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/bbold
%{texmf}/fonts/tfm/public/bbold

%files fonts-bh
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/bh
%{texmf}/fonts/tfm/bh
%{texmf}/fonts/vf/bh

%files fonts-bitstream
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/charter
%{texmf}/fonts/afm/bitstrea
%{texmf}/fonts/tfm/bitstrea
%{texmf}/fonts/vf/bitstrea

%files fonts-cbgreek
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/cbgreek
%{texmf}/fonts/source/public/cbgreek

%files fonts-cc-pl
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/cc-pl
%{texmf}/fonts/enc/dvips/cc-pl
%{texmf}/fonts/map/dvips/cc-pl
%{texmf}/fonts/source/public/cc-pl
%{texmf}/fonts/tfm/public/cc-pl

%files fonts-cg
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/cg
%{texmf}/fonts/vf/cg

%files fonts-cm
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/cm
%{texmf}/fonts/source/public/cm
%{texmf}/fonts/tfm/public/cm
%{texmf}/fonts/source/public/cm-bold

%files fonts-cmbright
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/cmbright
%{texmf}/fonts/tfm/public/cmbright

%files fonts-cmcyr
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/cmcyr
%{texmf}/fonts/vf/public/cmcyr

%files fonts-cmextra
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/cmextra
%{texmf}/fonts/tfm/public/cmextra

%files fonts-concmath
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/concmath
%{texmf}/fonts/tfm/public/concmath

%files fonts-concrete
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/concrete
%{texmf}/fonts/tfm/public/concrete

%files fonts-cs
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/cs
%{texmf}/fonts/source/public/cs
%{texmf}/fonts/tfm/public/cs

%files fonts-dstroke
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/dstroke
%{texmf}/fonts/source/public/dstroke
%{texmf}/fonts/tfm/public/dstroke

%files fonts-ecc
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/ecc
%{texmf}/fonts/source/public/ecc
%{texmf}/fonts/tfm/public/ecc

%files fonts-eurosym
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/eurosym
%{texmf}/fonts/source/public/eurosym
%{texmf}/fonts/tfm/public/eurosym

%files fonts-eulervm
%defattr(644,root,root,755)
#%doc %{texmf}/doc/fonts/eulervm
%{texmf}/fonts/tfm/public/eulervm
%{texmf}/fonts/vf/public/eulervm

%files fonts-euxm
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/euxm
%{texmf}/fonts/tfm/public/euxm

%files fonts-gothic
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/gothic
%{texmf}/fonts/tfm/public/gothic

%files fonts-hoekwater
%defattr(644,root,root,755)
# %doc %{texmf}/dist/doc/fonts/hoekwater
%{texmf}/dist/fonts/tfm/hoekwater
%{texmf}/dist/fonts/map/dvips/tetex/hoekwater.map

%files fonts-jknappen
%defattr(644,root,root,755)
%{texmf}/fonts/source/jknappen
%{texmf}/fonts/tfm/jknappen

%files fonts-latex
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/latex
%{texmf}/fonts/tfm/public/latex
%{texmf}/fonts/source/public/esint

%files fonts-lh
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/lh
%{texmf}/fonts/source/lh
#%{texmf}/fonts/tfm/lh

%files fonts-lm
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/lm

%files fonts-marvosym
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/marvosym
%{texmf}/fonts/afm/public/marvosym
%{texmf}/fonts/tfm/public/marvosym

%files fonts-mflogo
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/mflogo
%{texmf}/fonts/tfm/public/mflogo

%files fonts-misc
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/misc
%{texmf}/fonts/tfm/public/misc

%files fonts-monotype
%defattr(644,root,root,755)
#%{texmf}/fonts/tfm/monotype
#%{texmf}/fonts/vf/monotype

%files fonts-omega
%defattr(644,root,root,755)
#%dir %{texmf}/fonts/ocp
#%dir %{texmf}/fonts/ocp/public
#%{texmf}/fonts/ocp/public/oinuit
%dir %{texmf}/fonts/ofm
%dir %{texmf}/fonts/ofm/public
%{texmf}/fonts/ofm/public/*
%dir %{texmf}/fonts/ovf
%dir %{texmf}/fonts/ovf/public
%{texmf}/fonts/ovf/public/*
%dir %{texmf}/fonts/ovp
%dir %{texmf}/fonts/ovp/public
%{texmf}/fonts/ovp/public/*
%{texmf}/fonts/afm/public/omega
%{texmf}/fonts/tfm/public/omega

%files fonts-pazo
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/pazo
%{texmf}/fonts/vf/public/pazo

%files fonts-pl
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/pl
%{texmf}/dvips/pl
%{texmf}/fonts/enc/dvips/pl
%{texmf}/fonts/map/dvips/pl
%{texmf}/fonts/source/public/pl
%{texmf}/fonts/afm/public/pl
%{texmf}/fonts/tfm/public/pl

%files fonts-px
%defattr(644,root,root,755)
%{texmf}/fonts/map/dvips/tetex/pxfonts.map
%{texmf}/fonts/afm/public/pxfonts
%{texmf}/fonts/tfm/public/pxfonts
%{texmf}/fonts/vf/public/pxfonts

%files fonts-qfonts
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/qfonts
%{texmf}/fonts/enc/dvips/qfonts
%{texmf}/fonts/map/dvips/qfonts
%{texmf}/dvips/qfonts
%{texmf}/fonts/afm/public/qfonts
%{texmf}/fonts/tfm/public/qfonts

%files fonts-qpx
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/qpx
%{texmf}/fonts/vf/public/qpx

%files fonts-qtx
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/qtx
%{texmf}/fonts/vf/public/qtx

%files fonts-rsfs
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/rsfs
%{texmf}/fonts/tfm/public/rsfs

%files fonts-stmaryrd
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/stmaryrd
%{texmf}/fonts/source/public/stmaryrd
%{texmf}/fonts/tfm/public/stmaryrd

%files fonts-tx
%defattr(644,root,root,755)
%{texmf}/fonts/map/dvips/tetex/txfonts.map
%{texmf}/fonts/afm/public/txfonts
%{texmf}/fonts/tfm/public/txfonts
%{texmf}/fonts/vf/public/txfonts

%files fonts-urw
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/urw
%{texmf}/fonts/afm/urw

%files fonts-urwvn
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/urwvn
%{texmf}/fonts/type1/public/urwvn
%{texmf}/fonts/vf/public/urwvn

%files fonts-vnr
%defattr(644,root,root,755)
%{texmf}/fonts/map/dvips/vntex
%{texmf}/fonts/source/public/vnr
%{texmf}/fonts/tfm/public/vnr

%files fonts-wasy
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/wasy
%{texmf}/fonts/tfm/public/wasy

%files fonts-xypic
%defattr(644,root,root,755)
%{texmf}/fonts/map/dvips/xypic
%{texmf}/fonts/afm/public/xypic
%{texmf}/fonts/source/public/xypic
%{texmf}/fonts/tfm/public/xypic

%files fonts-yandy
%defattr(644,root,root,755)
%{texmf}/fonts/afm/yandy
%{texmf}/fonts/source/yandy
%{texmf}/fonts/tfm/yandy
%{texmf}/fonts/vf/yandy

%files fonts-type1-antp
%defattr(644,root,root,755)
%{texmf}/dvips/antp
%{texmf}/fonts/type1/public/antp

%files fonts-type1-antt
%defattr(644,root,root,755)
%{texmf}/dvips/antt
%{texmf}/fonts/type1/public/antt

%files fonts-type1-belleek
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/belleek
%{texmf}/fonts/type1/public/belleek

%files fonts-type1-bitstream
%defattr(644,root,root,755)
%{texmf}/fonts/type1/bitstrea

%files fonts-type1-bluesky
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/bluesky
%{texmf}/dvips/bluesky
%{texmf}/fonts/type1/bluesky

%files fonts-type1-cc-pl
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/cc-plps
%{texmf}/fonts/type1/public/cc-pl

%files fonts-type1-cmcyr
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/cmcyr

%files fonts-type1-cs
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/cs

%files fonts-type1-dstroke
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/dstroke

%files fonts-type1-eurosym
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/eurosym

%files fonts-type1-hoekwater
%defattr(644,root,root,755)
%{texmf}/dist/fonts/type1/hoekwater

%files fonts-type1-fpl
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/fpl
%{texmf}/fonts/afm/public/fpl
%{texmf}/fonts/type1/public/fpl

%files fonts-type1-lm
%defattr(644,root,root,755)
%{texmf}/fonts/afm/public/lm
%{texmf}/fonts/type1/public/lm

%files fonts-type1-marvosym
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/marvosym

%files fonts-type1-mathpazo
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/mathpazo
%{texmf}/dist/fonts/afm/public/mathpazo
%{texmf}/dist/fonts/type1/public/mathpazo

%files fonts-type1-omega
%defattr(644,root,root,755)
%{texmf}/dist/fonts/type1/public/omega

%files fonts-type1-pl
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/plpsfont
%{texmf}/dist/fonts/type1/public/pl

%files fonts-type1-px
%defattr(644,root,root,755)
%{texmf}/dist/fonts/type1/public/pxfonts

%files fonts-type1-qfonts
%defattr(644,root,root,755)
%{texmf}/dist/fonts/type1/public/qfonts

%files fonts-type1-tx
%defattr(644,root,root,755)
%{texmf}/dist/fonts/type1/public/txfonts

%files fonts-type1-tt2001
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/tt2001

%files fonts-type1-urw
%defattr(644,root,root,755)
%{texmf}/dist/fonts/type1/urw

%files fonts-type1-vnr
%defattr(644,root,root,755)
%{texmf}/dist/fonts/type1/public/vnr

%files fonts-type1-xypic
%defattr(644,root,root,755)
%{texmf}/dvips/xypic
%{texmf}/dist/fonts/type1/public/xypic
