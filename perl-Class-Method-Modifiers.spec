#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Method-Modifiers
Summary:	Class::Method::Modifiers - provides Moose-like method modifiers
Summary(pl.UTF-8):	Class::Method::Modifiers - dostarcza modyfikatory metod na kształt Moose
Name:		perl-Class-Method-Modifiers
Version:	1.05
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8f504d4a95b2994835fbe72a3790864e
URL:		http://search.cpan.org/dist/Class-Method-Modifiers/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl-Test-Exception
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
that original method.  See the MODIFIERS section for more details on
how the particular modifiers work.

%description -l pl.UTF-8
Class::Method::Modifiers - dostarcza modyfikatory metod na kształt Moose

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
%{perl_vendorlib}/Class/Method/*.pm
%{_mandir}/man3/*
