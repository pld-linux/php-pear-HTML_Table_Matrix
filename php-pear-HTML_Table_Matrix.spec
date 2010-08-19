%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Table
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Matrix
Summary:	%{_pearname} - autofill a table with data
Summary(pl.UTF-8):	%{_pearname} - automatycznie wypełnianie tabeli danymi
Name:		php-pear-%{_pearname}
Version:	1.0.10
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	563aa076399bcaa6d690bbe24fe90090
URL:		http://pear.php.net/package/HTML_Table_Matrix/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTML_Table
Requires:	php-pear-PEAR-core >= 1:1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Numbers/Words.*)'

%description
HTML_Table_Matrix is an extension to HTML_Table which allows you to
easily fill up a table with data. Features:
- It uses Filler classes to determine how the data gets filled in the
  table. With a custom Filler, you can fill data in up, down, forwards,
  backwards, diagonally, randomly or any other way you like.
- Comes with Fillers to fill left-to-right-top-to-bottom and
  right-to-left-top-to-bottom.
- Abstract Filler methods keep the code clean & easy to understand.
- Table height or width may be omitted, and it will figure out the
  correct table size based on the data you provide.
- It integrates handily with Pager to create pleasant pageable table
  layouts, such as for an image gallery. Just specify a height or width,
  Filler, and feed it the data returned from Pager.
- Table may be constrained to a specific height or width, and excess
  data will be ignored.
- Fill offset may be specified, to leave room for a table header, or
  other elements in the table.
- Fully documented with PHPDoc.
- Includes fully functional example code.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
HTML_Table_Matrix to rozszerzenie HTML_Table pozwalające na łatwe
wypełnianie tabel danymi. Cechy pakietu:
- Używa klas Filler do określenia sposobu wypełniania tabeli danymi.
  Przy użyciu własnego Fillera można wypełniać danymi do góry, w dół, do
  przodu, do tyłu, po przekątnej, losowo lub w dowolny inny sposób.
- Zawiera klasy Filler do wypełniania od lewej do prawej, od góry do
  dołu oraz od prawej do lewej, od góry do dołu.
- Wyabstrahowane metody Filler pozwalają utrzymać kod czystym i łatwym
  do zrozumienia.
- Wysokość lub szerokość tabeli może być pominięta, a właściwy rozmiar
  tabel oparty na dostarczonych danych.
- Zręcznie integruje się z klasą Pager tworząc przyjemne stronnicowane
  tabele, takie jak dla galerii obrazków. Wystarczy podać wysokość lub
  szerokość, klasę Filler i dostarczyć dane zwrócone przez Pager.
- Tabele mogą być ograniczane do określonej wysokości lub szerokości,
  a nadmiarowe dane zostaną zignorowane.
- Można podać offset wypełnienia aby zostawić miejsce na nagłówek lub
  inne elementy tabeli.
- Jest w pełni udokumentowany przy użyciu PHPDoc.
- Zawiera w pełni funkcjonalny kod przykładowy.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# examples fixups
mv ./%{php_pear_dir}/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/Matrix.php
%{php_pear_dir}/%{_class}/%{_subclass}/Matrix

%{_examplesdir}/%{name}-%{version}
