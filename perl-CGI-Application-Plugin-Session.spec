%define module   CGI-Application-Plugin-Session
%define version    1.03
%define release    %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Add CGI::Session support to CGI::Application
Source:     http://www.cpan.org/modules/by-module/CGI/%{module}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{module}
BuildRequires: perl(CGI::Application)
BuildRequires: perl(CGI::Session)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
Requires:      perl(CGI::Session)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


