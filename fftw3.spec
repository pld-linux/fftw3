# TODO: move single and long-double libs to subpackages
Summary:	Fast Fourier transform library
Summary(pl):	Biblioteka z funkacjami szybkiej transformaty Fouriera
Summary(pt_BR):	biblioteca fast fourier transform
Name:		fftw3
Version:	3.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.fftw.org/pub/fftw/fftw-%{version}.tar.gz
# Source0-md5:	6b09e3b141a9f1aae8b3a1d64fff6982
Patch0:		%{name}-info.patch
Icon:		fftw-logo-thumb.gif
URL:		http://www.fftw.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FFTW is a collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions. It includes complex,
real, and parallel transforms, and can handle arbitrary array sizes
efficiently. This RPM package includes the double precision FFTW
uniprocessor and threads libraries.

%description -l pl
FFTW jest zbiorem szybkich funkcji C do obliczania dyskretnych
transformat Fouriera w jednym lub wiêcej wymiarach. Zawiera równie¿
zespolone, rzeczywiste oraz równoleg³e transformaty i potrafi wydajnie
radziæ sobie z tablicami o dowolnych rozmiarach. Ten pakiet RPM
zawiera wersje FFTW o podwójnej precyzji dla architektur
jednoprocesorowych oraz z obs³ug± w±tków.

%description -l pt_BR
FFTW é uma coleção de rotinas rápidas em C para computar a Discrete
Fourier Transform em uma ou mais dimensões. Incluindo transformações
complexas, reais e paralelas, também pode manipular vetores de tamanho
arbitrário eficientemente. Esse pacote RPM inclui bibliotecas FFTW com
suporte a threads, normal e dupla precisão (Os arquivos de precisão
normal tem um prefixo "s").

%package devel
Summary:	Header files and documentation for fftw
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja do fftw
Summary(pt_BR):	Headers e documentação do pacote FFTW
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains the header files and documentation you need to
develop programs using the FFTW (fast fourier transform library).

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe oraz dokumetacjê potrzebne do
tworzenia programów u¿ywaj±cych biblioteki FFTW (wykonuj±cej szybk±
transformatê Fouriera).

%description devel -l pt_BR
Este pacote contém documentação e headers adicionais para desenvolver
programas usando a FFTW.

%package static
Summary:	Static fftw libraries
Summary(pl):	Statyczne biblioteki fftw
Summary(pt_BR):	Bibliotecas estáticas do pacote FFTW
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static fftw libraries.

%description static -l pl
Statyczne biblioteki fftw.

%description static -l pt_BR
Este pacote contém as bibliotecas estáticas do pacote FFTW.

%prep
%setup -q -n fftw-%{version}
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
# it seems to be safe because of runtime CPU detection
for ver in single double long-double ; do
	OPTS=""
	# k7,SSE,3dnow,altivec only for single
	if [ "$ver" = "single" ]; then
		OPTS="
%ifarch athlon
		--enable-k7
%endif
%ifarch i686 athlon
	--enable-sse
%endif
%ifarch i586 k6
	--enable-3dnow
%endif
%ifarch ppc
	--enable-altivec
%endif
		"
	fi
%ifarch i686
	# SSE2 only for double
	if [ "$ver" = "double" ]; then
		OPTS="--enable-sse2"
	endif
%endif
%configure \
	--enable-shared \
	--enable-threads \
	--enable-$ver \
	$OPTS \
	--%{!?debug:dis}%{?debug:en}able-debug

%{__make}
%{__make} install DESTDIR=`pwd`/inst-$ver
	if [ "$ver" != "long-double" ]; then
%{__make} clean
	fi
done

# remake docs removed by make clean
%{__make} fftw-faq.html -C doc/FAQ

%install
rm -rf $RPM_BUILD_ROOT

# this installs last configured version (long-double)
%{__make} install DESTDIR=$RPM_BUILD_ROOT

# duplicates
rm -rf inst-*{%{_bindir}/fftw-wisdom-to-conf,%{_includedir}} \
	inst-*{%{_infodir},%{_mandir}/man1/fftw-wisdom-to-conf.1}

# install prepared remaining versions
tar cf - -C inst-single . | tar xf - -C $RPM_BUILD_ROOT
tar cf - -C inst-double . | tar xf - -C $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/fftw*-wisdom*
%attr(755,root,root) %{_libdir}/libfftw3*.so.*.*.*
%{_mandir}/man1/fftw*-wisdom*.1*

%files devel
%defattr(644,root,root,755)
%doc doc/html doc/FAQ/fftw-faq.html
%attr(755,root,root) %{_libdir}/libfftw3*.so
%{_libdir}/libfftw3*.la
%{_includedir}/fftw3.*
%{_infodir}/fftw3.info*
%{_pkgconfigdir}/fftw3*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libfftw3*.a
