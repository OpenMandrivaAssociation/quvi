%define name  quvi
%define version 0.2.2
%define release %mkrel 1

%define libname %mklibname %name 0
%define libnamedevel %{_lib}%{name}-devel

Summary: A command line video download tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPLv3
Group: Networking/WWW
Url: http://code.google.com/p/cclive/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: lua-devel >= 5.1
BuildRequires: curl-devel
BuildRequires: libpcre-devel

%description
cclive is a command line video download tool for Youtube and similar websites.
It is a rewrite of the clive software in C++ with a smaller system footprint.
It is not, nor intended to become, an universal flash video download tool.

%package -n %libname
Summary: A command line video download tool
Group: System/Libraries

%description -n %libname
cclive is a command line video download tool for Youtube and similar websites.
It is a rewrite of the clive software in C++ with a smaller system footprint.
It is not, nor intended to become, an universal flash video download tool.

%package -n %libnamedevel
Summary: A command line video download tool
Group: System/Libraries
Requires: %libname = %version-%release

%description -n %libnamedevel
cclive is a command line video download tool for Youtube and similar websites.
It is a rewrite of the clive software in C++ with a smaller system footprint.
It is not, nor intended to become, an universal flash video download tool.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/*
%_datadir/%{name}
%_mandir/man*/%{name}.*
%doc KNOWN_ISSUES ChangeLog README NEWS

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.*

%files -n %libnamedevel
%defattr(-,root,root)
%_includedir/%{name}
%_libdir/*.so
%_libdir/*.a
%_libdir/*.la
%_libdir/pkgconfig/lib%{name}.pc

