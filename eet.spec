Summary:	Library for speedy data storage, retrieval, and compression
Name:		eet
Version:	0.9.9
%define	_snap	20050105
Release:	0.%{_snap}.0.1
License:	BSD
Group:		Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	77334dc6def3684e6ac51cec6189770a
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eet is a tiny library designed to write an arbitary set of chunks of
data to a file and optionally compress each chunk (very much like a
zip file) and allow fast random-access reading of the file later on.
It does not do zip as a zip itself has more complexity than is needed,
and it was much simpler to implement this once here.

It also can encode and decode data structures in memory, as well as
image data for saving to eet files or sending across the network to
other machines, or just writing to arbitary files on the system. All
data is encoded in a platform independant way and can be written and
read by any architecture.

%package devel
Summary:	headers, documentation and test programs
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Headers, static libraries, test programs and documentation for Eet.

%package static
Summary:	Static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries fo Eet.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libeet.so.*
%attr(755,root,root) %{_bindir}/eet

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eet-config
%attr(755,root,root) %{_libdir}/libeet.so
%{_libdir}/libeet.la
%{_pkgconfigdir}/eet.pc
%{_includedir}/Eet*

%files static
%defattr(644,root,root,755)
%{_libdir}/libeet.a
