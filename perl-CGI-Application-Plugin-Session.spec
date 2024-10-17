%define upstream_name    CGI-Application-Plugin-Session
%define upstream_version 1.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Add CGI::Session support to CGI::Application
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CGI/CGI-Application-Plugin-Session-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI::Application)
BuildRequires:	perl(CGI::Session)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
Requires:	perl(CGI::Session)
BuildArch:	noarch

%description
CGI::Application::Plugin::Session seamlessly adds session support to your
the CGI::Application manpage modules by providing a the CGI::Session
manpage object that is accessible from anywhere in the application.

Lazy loading is used to prevent expensive file system or database calls
from being made if the session is not needed during this request. In other
words, the Session object is not created until it is actually needed. Also,
the Session object will act as a singleton by always returning the same
Session object for the duration of the request.

This module aims to be as simple and non obtrusive as possible. By not
requiring any changes to the inheritance tree of your modules, it can be
easily added to existing applications. Think of it as a plugin module that
adds a couple of new methods directly into the CGI::Application namespace
simply by loading the module. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 653392
- rebuild for updated spec-helper

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 405778
- rebuild using %%perl_convert_version

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-2mdv2009.1
+ Revision: 307082
- add missing dependency on CGI::Session

* Fri Oct 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2009.1
+ Revision: 291355
- import perl-CGI-Application-Plugin-Session


* Thu Oct 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2009.1
- initial mdv release, generated with cpan2dist


