#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%define		pdir	Mail
%define		pnam	Box-IMAP4
Summary:	Mail::Transport::IMAP4 - proxy to Mail::IMAPClient
Name:		perl-Mail-Box-IMAP4
Version:	3.003
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e195c24962425a14afb7841b5f2e33ba
URL:		https://metacpan.org/release/Mail-Box-IMAP4/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Mail::Box::Manage::User) >= 3
BuildRequires:	perl(Mail::Box::Net) >= 3
BuildRequires:	perl(Mail::Box::Search) >= 3
BuildRequires:	perl(Mail::Box::Test) >= 3
BuildRequires:	perl(Mail::Message::Head::Delayed) >= 3
BuildRequires:	perl(Mail::Server) >= 3
BuildRequires:	perl(Mail::Transport::Receive) >= 3
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-Mail-IMAPClient
BuildRequires:	perl-Mail-Message >= 3
BuildRequires:	perl-TimeDate
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IMAP4 protocol is quite complicated: it is feature rich and allows
various asynchronous actions. The main document describing IMAP is
rfc3501 (which obsoleted the original specification of protocol 4r1 in
rfc2060 in March 2003).

This package, as part of MailBox, does not implement the actual
protocol itself but uses Mail::IMAPClient to do the work. The task for
this package is to hide as many differences between that module's
interface and the common MailBox folder types. Multiple
Mail::Box::IMAP4 folders can share one Mail::Transport::IMAP4
connection.

The Mail::IMAPClient module is the best IMAP4 implementation for
Perl5, but is not maintained. There are many known problems with the
module, and solving those is outside the scope of MailBox. See
http://rt.cpan.org/Public/Dist/Display.html?Name=Mail-IMAPClient for
all the reported bugs.

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
%doc ChangeLog README
%{perl_vendorlib}/Mail/Box/*.pm
%{perl_vendorlib}/Mail/Box/*.pod
%{perl_vendorlib}/Mail/Box/IMAP4
%{perl_vendorlib}/Mail/Server/IMAP4.pm
%{perl_vendorlib}/Mail/Server/IMAP4.pod
%dir %{perl_vendorlib}/Mail/Server/IMAP4
%{perl_vendorlib}/Mail/Server/IMAP4/*.pm
%{perl_vendorlib}/Mail/Server/IMAP4/*.pod
%{perl_vendorlib}/Mail/Transport/IMAP4.pm
%{perl_vendorlib}/Mail/Transport/IMAP4.pod
%{_mandir}/man3/*
