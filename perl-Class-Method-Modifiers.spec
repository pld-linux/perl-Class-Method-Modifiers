#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Class
%define	pnam	Method-Modifiers
Summary:	Class::Method::Modifiers - provides Moose-like method modifiers
Summary(pl.UTF-8):	Class::Method::Modifiers - modyfikatory metod na kształt Moose
Name:		perl-Class-Method-Modifiers
Version:	2.13
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b1398e3682aa2e075b913b9f9000b596
URL:		https://metacpan.org/release/Class-Method-Modifiers
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Needs
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In its most basic form, a method modifier is just a method that calls
$self->SUPER::foo(@_).

Class::Method::Modifiers provides three modifiers: before, around,
and after. before and after are run just before and after the method
they modify, but can not really affect that original method. around
is run in place of the original method, with a hook to easily call
that original method.

%description -l pl.UTF-8
W najprostszej postaci, modyfikator metody to metoda wywołująca
$self->SUPER::foo(@_).

Moduł Class::Method::Modifiers dostarcza trzy modyfikatory: before,
around oraz after. Modyfikatory before oraz after są wywoływane
bezpośrednio przed i bezpośrednio po modyfikowanej metodzie, ale nie
mogą wpływać na oryginalną metodę. Modyfikator around jest wywoływany
zamiast oryginalnej metody z uchwytem do łatwego wywołania tej
oryginalnej metody. 

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/Method/Modifiers.pm
%{_mandir}/man3/Class::Method::Modifiers.3pm*
