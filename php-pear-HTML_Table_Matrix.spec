%include	/usr/lib/rpm/macros.php
%define         _class          HTML
%define         _subclass       Table
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Matrix

Summary:	%{_pearname} - Autofill a table with data
Summary(pl):	%{_pearname} - Automatycznie wype³nianie tabeli danymi
Name:		php-pear-%{_pearname}
Version:	1.0.5
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	69e4f2535a1195afe8694264970354ce
URL:		http://pear.php.net/package/HTML_Table_Matrix/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML_Table_Matrix is an extension to HTML_Table which allows you to
easily fill up a table with data. Features:
- It uses Filler classes to determine how the data gets filled in the
  table. With a custom Filler, you can fill data in up, down,
  forwards, backwards, diagonally, randomly or any other way you like.
- Comes with Fillers to fill left-to-right-top-to-bottom and
  right-to-left-top-to-bottom.
- Abstract Filler methods keep the code clean & easy to understand.
- Table height or width may be omitted, and it will figure out the
  correct table size based on the data you provide.
- It integrates handily with Pager to create pleasant pageable table
  layouts, such as for an image gallery. Just specify a height or
  width, Filler, and feed it the data returned from Pager.
- Table may be constrained to a specific height or width, and excess
  data will be ignored.
- Fill offset may be specified, to leave room for a table header, or
  other elements in the table.
- Fully documented with PHPDoc.
- Includes fully functional example code.

In PEAR status of this package is: %{_status}.

%description -l pl
HTML_Table_Matrix to rozszerzenie HTML_Table pozwalaj±ce na ³atwe
wype³nianie tabel danymi. Cechy pakietu:
- U¿ywa klas Filler do okre¶lenia sposobu wype³niania tabeli danymi.
  Przy u¿yciu w³asnego Fillera mo¿na wype³niaæ danymi do góry, w dó³,
  do przodu, do ty³u, po przek±tnej, losowo lub w dowolny inny sposób.
- Zawiera klasy Filler do wype³niania od lewej do prawej, od góry do
  do³u oraz od prawej do lewej, od góry do do³u.
- Wyabstrahowane metody Filler pozwalaj± utrzymaæ kod czystym i ³atwym
  do zrozumienia.
- Wysoko¶æ lub szeroko¶æ tabeli mo¿e byæ pominiêta, a w³a¶ciwy rozmiar
  tabel oparty na dostarczonych danych.
- Zrêcznie integruje siê z klas± Pager tworz±c przyjemne stronnicowane
  tabele, takie jak dla galerii obrazków. Wystarczy podaæ wysoko¶æ lub
  szeroko¶æ, klasê Filler i dostarczyæ dane zwrócone przez Pager.
- Tabele mog± byæ ograniczane do okre¶lonej wysoko¶ci lub szeroko¶ci,
  a nadmiarowe dane zostan± zignorowane.
- Mo¿na podaæ offset wype³nienia aby zostawiæ miejsce na nag³ówek lub
  inne elementy tabeli.
- Jest w ope³ni udokumentowany przy u¿yciu PHPDoc.
- Zawiera w pe³ni funkcjonalny kod przyk³adowy.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Matrix/Filler

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Matrix/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Matrix
install %{_pearname}-%{version}/Matrix/Filler/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Matrix/Filler

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/%{_subclass}/Matrix.php
%{php_pear_dir}/%{_class}/%{_subclass}/Matrix
