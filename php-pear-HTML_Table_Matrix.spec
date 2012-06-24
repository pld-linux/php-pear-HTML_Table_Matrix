%include	/usr/lib/rpm/macros.php
%define         _class          HTML
%define         _subclass       Table
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Matrix

Summary:	%{_pearname} - Autofill a table with data
Summary(pl):	%{_pearname} - Automatycznie wype�nianie tabeli danymi
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
HTML_Table_Matrix to rozszerzenie HTML_Table pozwalaj�ce na �atwe
wype�nianie tabel danymi. Cechy pakietu:
- U�ywa klas Filler do okre�lenia sposobu wype�niania tabeli danymi.
  Przy u�yciu w�asnego Fillera mo�na wype�nia� danymi do g�ry, w d�,
  do przodu, do ty�u, po przek�tnej, losowo lub w dowolny inny spos�b.
- Zawiera klasy Filler do wype�niania od lewej do prawej, od g�ry do
  do�u oraz od prawej do lewej, od g�ry do do�u.
- Wyabstrahowane metody Filler pozwalaj� utrzyma� kod czystym i �atwym
  do zrozumienia.
- Wysoko�� lub szeroko�� tabeli mo�e by� pomini�ta, a w�a�ciwy rozmiar
  tabel oparty na dostarczonych danych.
- Zr�cznie integruje si� z klas� Pager tworz�c przyjemne stronnicowane
  tabele, takie jak dla galerii obrazk�w. Wystarczy poda� wysoko�� lub
  szeroko��, klas� Filler i dostarczy� dane zwr�cone przez Pager.
- Tabele mog� by� ograniczane do okre�lonej wysoko�ci lub szeroko�ci,
  a nadmiarowe dane zostan� zignorowane.
- Mo�na poda� offset wype�nienia aby zostawi� miejsce na nag��wek lub
  inne elementy tabeli.
- Jest w ope�ni udokumentowany przy u�yciu PHPDoc.
- Zawiera w pe�ni funkcjonalny kod przyk�adowy.

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
