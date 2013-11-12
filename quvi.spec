Name:		quvi
Version:	0.9.4
Release:	1
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
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc ChangeLog AUTHORS COPYING README NEWS
%{_bindir}/*
%{_mandir}/man*/%{name}*.*


%changelog
* Tue Mar 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.2-1
+ Revision: 782399
- version update  0.4.2

* Mon Jan 30 2012 Andrey Bondrov <abondrov@mandriva.org> 0.2.19-2
+ Revision: 769743
- Rebuild to fix .la files issue

* Wed Sep 14 2011 Andrey Bondrov <abondrov@mandriva.org> 0.2.19-1
+ Revision: 699729
- New version: 0.2.19

* Fri Jan 21 2011 Funda Wang <fwang@mandriva.org> 0.2.12-1
+ Revision: 631952
- new version 0.2.12

* Wed Aug 25 2010 Funda Wang <fwang@mandriva.org> 0.2.2-1mdv2011.0
+ Revision: 573025
- use configure2_5x

  + Olivier Thauvin <nanardon@mandriva.org>
    - import quvi

