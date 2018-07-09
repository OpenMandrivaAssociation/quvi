Name:		quvi
Version:	0.9.5
Release:	5
Summary:	A command line tool originally created to aid the development of libquvi
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
License:	GPLv3
Group:		Networking/WWW
Url:		http://quvi.sourceforge.net/
BuildRequires:	lua-devel >= 5.1
BuildRequires:	curl-devel
BuildRequires:	pkgconfig(libquvi-0.9)

%description
A libquvi-in-a-command-line-tool. It was originally created
to aid the development of libquvi.

Features:
- Fast and low system footprint
- Basic JSON and XML output

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%doc ChangeLog AUTHORS COPYING README NEWS
%{_bindir}/*
%{_mandir}/man*/%{name}*.*
