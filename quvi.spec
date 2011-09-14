%define name  quvi
%define version 0.2.19
%define release %mkrel 1

%define libname %mklibname %{name} 6
%define libnamedevel %mklibname -d %{name}

Summary: A command line tool originally created to aid the development of libquvi
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
License: GPLv3
Group: Networking/WWW
Url: http://quvi.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: lua-devel >= 5.1
BuildRequires: curl-devel

%description
A libquvi-in-a-command-line-tool. It was originally created
to aid the development of libquvi.

Features:
- Fast and low system footprint
- Basic JSON and XML output

%package -n %{libname}
Summary: A small C library that can be used to parse flash media stream URLs
Group: System/Libraries

%description -n %{libname}
A small C library that can be used to parse flash media stream URLs. 
It originates from the idea of working around the flash requirement 
found on many media hosting websites (e.g. YouTube).

Features:
- Parses additional media details (e.g. media title, media ID)
- Supported platforms include Linux, *BSD systems
- C library: Fast and low system footprint
- Easy to extend: uses lua for scripting
- Supports 40+ websites
- C API is simple to use

%package -n %{libnamedevel}
Summary: A small C library that can be used to parse flash media stream URLs
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{libnamedevel}
Development files (headers etc) needed to develop software with %{libname}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man*/%{name}.*
%doc ChangeLog AUTHORS COPYING README NEWS

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lua/

%files -n %{libnamedevel}
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/lib%{name}.pc

