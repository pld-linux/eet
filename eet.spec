Summary:	Library for speedy data storage, retrieval, and compression
Summary(pl):	Biblioteka do szybkiego zapisywania, odtwarzania i kompresji danych
Name:		eet
Version:	0.9.10
%define	_snap	20050329
Release:	0.%{_snap}.0.1
License:	BSD
Group:		Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{_snap}.tar.gz
# Source0-md5:	d993ba9af4fa5e54f802d4b013a24743
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

%description -l pl
Eet to ma³a biblioteka zaprojektowana do zapisu dowolnego zbioru
porcji danych do pliku i opcjonalnej kompresji ka¿dej porcji (podobnie
do pliku zip) oraz umo¿liwienia pó¼niej szybkiego odczytu pliku ze
swobodnym dostêpem. Nie jest to zip, jako ¿e sam zip jest bardziej
z³o¿ony ni¿ trzeba, a by³o du¿o pro¶ciej zaimplementowaæ to tak, jak
jest.

Biblioteka mo¿e tak¿e kodowaæ i dekodowaæ struktury danych w pamiêci,
a tak¿e dane obrazów do zapisu do plików eet lub wysy³ania po sieci na
inne maszyny, lub po prostu zapisywania do dowolnych plików w
systemie. Wszystkie dane s± kodowane w sposób niezale¿ny od platformy
i mog± byæ zapisywane i odczytywane na dowolnej architekturze.

%package devel
Summary:	Header files for Eet library
Summary(pl):	Pliki nag³ówkowe biblioteki Eet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Eet library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Eet.

%package static
Summary:	Static Eet library
Summary(pl):	Statyczna biblioteka Eet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Eet library.

%description static -l pl
Statyczna biblioteka Eet.

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
%attr(755,root,root) %{_bindir}/eet
%attr(755,root,root) %{_libdir}/libeet.so.*.*.*

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
