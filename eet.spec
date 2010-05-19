#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library for speedy data storage, retrieval, and compression
Summary(pl.UTF-8):	Biblioteka do szybkiego zapisywania, odtwarzania i kompresji danych
Name:		eet
Version:	1.1.0
Release:	4
License:	BSD
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	c9f1fd90c3f9886cebd5d38ff9cd0ccf
URL:		http://enlightenment.org/p.php?p=about/efl/eet
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

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

%description -l pl.UTF-8
Eet to mała biblioteka zaprojektowana do zapisu dowolnego zbioru
porcji danych do pliku i opcjonalnej kompresji każdej porcji (podobnie
do pliku zip) oraz umożliwienia później szybkiego odczytu pliku ze
swobodnym dostępem. Nie jest to zip, jako że sam zip jest bardziej
złożony niż trzeba, a było dużo prościej zaimplementować to tak, jak
jest.

Biblioteka może także kodować i dekodować struktury danych w pamięci,
a także dane obrazów do zapisu do plików eet lub wysyłania po sieci na
inne maszyny, lub po prostu zapisywania do dowolnych plików w
systemie. Wszystkie dane są kodowane w sposób niezależny od platformy
i mogą być zapisywane i odczytywane na dowolnej architekturze.

%package devel
Summary:	Header files for Eet library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Eet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	zlib-devel

%description devel
Header files for Eet library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Eet.

%package static
Summary:	Static Eet library
Summary(pl.UTF-8):	Statyczna biblioteka Eet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Eet library.

%description static -l pl.UTF-8
Statyczna biblioteka Eet.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
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
%doc AUTHORS COPYING COPYING-PLAIN README
%attr(755,root,root) %{_bindir}/eet
%attr(755,root,root) %{_libdir}/libeet.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeet.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeet.so
%{_libdir}/libeet.la
%{_pkgconfigdir}/eet.pc
%{_includedir}/Eet.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libeet.a
%endif
