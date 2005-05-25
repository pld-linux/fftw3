#
%bcond_without	fftwl	# don't build "long" subpackages
#
%ifarch alpha ppc sparc
# sizeof(double long)==sizeof(double) on these archs
%undefine	with_fftwl
%endif
Summary:	Fast Fourier Transform library
Summary(pl):	Biblioteka z funkcjami szybkiej transformaty Fouriera
Summary(pt_BR):	biblioteca fast fourier transform
Name:		fftw3
Version:	3.0.1
Release:	5
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.fftw.org/pub/fftw/fftw-%{version}.tar.gz
# Source0-md5:	76cd21ecc9a7bed6343566c473c36477
Patch0:		%{name}-info.patch
Patch1:		%{name}-link.patch
Patch2:		fftw-gcc4.patch
Icon:		fftw-logo-thumb.gif
URL:		http://www.fftw.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-g77
BuildRequires:	libtool
BuildRequires:	texinfo
Requires:	%{name}-common = %{version}-%{release}
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
Summary:	Development files for fftw
Summary(pl):	Pliki programistyczne do fftw
Summary(pt_BR):	Headers e documentação do pacote FFTW
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-common-devel = %{version}-%{release}

%description devel
This package contains the files you need to develop programs using the
FFTW (fast fourier transform library).

%description devel -l pl
Ten pakiet zawiera pliki potrzebne do tworzenia programów u¿ywaj±cych
biblioteki FFTW (wykonuj±cej szybk± transformatê Fouriera).

%description devel -l pt_BR
Este pacote contém documentação e headers adicionais para desenvolver
programas usando a FFTW.

%package static
Summary:	Static fftw libraries
Summary(pl):	Statyczne biblioteki fftw
Summary(pt_BR):	Bibliotecas estáticas do pacote FFTW
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static fftw libraries.

%description static -l pl
Statyczne biblioteki fftw.

%description static -l pt_BR
Este pacote contém as bibliotecas estáticas do pacote FFTW.

%package single
Summary:	Fast Fourier Transform library - single precision
Summary(pl):	Biblioteka z funkcjami szybkiej transformaty Fouriera - pojedynczej precyzji
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}

%description single
FFTW is a collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions. It includes complex,
real, and parallel transforms, and can handle arbitrary array sizes
efficiently. This RPM package includes the single precision FFTW
uniprocessor and threads libraries.

%description single -l pl
FFTW jest zbiorem szybkich funkcji C do obliczania dyskretnych
transformat Fouriera w jednym lub wiêcej wymiarach. Zawiera równie¿
zespolone, rzeczywiste oraz równoleg³e transformaty i potrafi wydajnie
radziæ sobie z tablicami o dowolnych rozmiarach. Ten pakiet RPM
zawiera wersje FFTW o pojedynczej precyzji dla architektur
jednoprocesorowych oraz z obs³ug± w±tków.

%package single-devel
Summary:	Development files for single precision fftw
Summary(pl):	Pliki programistyczne do fftw pojedynczej precyzji
Group:		Development/Libraries
Requires:	%{name}-common-devel = %{version}-%{release}
Requires:	%{name}-single = %{version}-%{release}

%description single-devel
This package contains the files you need to develop programs using the
single precision FFTW (fast fourier transform library).

%description single-devel -l pl
Ten pakiet zawiera pliki potrzebne do tworzenia programów u¿ywaj±cych
biblioteki FFTW pojedynczej precyzji (wykonuj±cej szybk± transformatê
Fouriera).

%package single-static
Summary:	Static fftw single precision libraries
Summary(pl):	Statyczne biblioteki fftw pojedynczej precyzji
Group:		Development/Libraries
Requires:	%{name}-single-devel = %{version}-%{release}

%description single-static
Static fftw single precision libraries.

%description single-static -l pl
Statyczne biblioteki fftw pojedynczej precyzji.

%package long
Summary:	Fast Fourier Transform library - long double precision
Summary(pl):	Biblioteka z funkcjami szybkiej transformaty Fouriera - rozszerzonej precyzji
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}

%description long
FFTW is a collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions. It includes complex,
real, and parallel transforms, and can handle arbitrary array sizes
efficiently. This RPM package includes the long double precision FFTW
uniprocessor and threads libraries.

%description long -l pl
FFTW jest zbiorem szybkich funkcji C do obliczania dyskretnych
transformat Fouriera w jednym lub wiêcej wymiarach. Zawiera równie¿
zespolone, rzeczywiste oraz równoleg³e transformaty i potrafi wydajnie
radziæ sobie z tablicami o dowolnych rozmiarach. Ten pakiet RPM
zawiera wersje FFTW o rozszerzonej precyzji dla architektur
jednoprocesorowych oraz z obs³ug± w±tków.

%package long-devel
Summary:	Development files for long double precision fftw
Summary(pl):	Pliki programistyczne do fftw rozszerzonej precyzji
Group:		Development/Libraries
Requires:	%{name}-common-devel = %{version}-%{release}
Requires:	%{name}-long = %{version}-%{release}

%description long-devel
This package contains the files you need to develop programs using the
long double precision FFTW (fast fourier transform library).

%description long-devel -l pl
Ten pakiet zawiera pliki potrzebne do tworzenia programów u¿ywaj±cych
biblioteki FFTW rozszerzonej precyzji (wykonuj±cej szybk± transformatê
Fouriera).

%package long-static
Summary:	Static fftw long double precision libraries
Summary(pl):	Statyczne biblioteki fftw rozszerzonej precyzji
Group:		Development/Libraries
Requires:	%{name}-long-devel = %{version}-%{release}

%description long-static
Static fftw long double precision libraries.

%description long-static -l pl
Statyczne biblioteki fftw rozszerzonej precyzji.

%package common
Summary:	Files common for all versions of fftw libraries
Summary(pl):	Pliki wspólne dla wszystkich wersji bibliotek fftw
Group:		Libraries

%description common
Files common for all versions of fftw libraries (basic documentation,
fftw-wisdom-to-conf utility).

%description common -l pl
Pliki wspólne dla wszystkich wersji bibliotek fftw (podstawowa
dokumentacja, narzêdzie fftw-wisdom-to-conf).

%package common-devel
Summary:	Development files common for all versions of fftw libraries
Summary(pl):	Pliki programistyczne wspólne dla wszystkich wersji bibliotek fftw
Group:		Development/Libraries
Requires:	%{name}-common = %{version}-%{release}

%description common-devel
Development files common for all versions of fftw libraries (header
files, development documentation).

%description common-devel -l pl
Pliki programistyczne wspólne dla wszystkich wersji bibliotek fftw
(pliki nag³ówkowe, dokumentacja programisty).

%prep
%setup -q -n fftw-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

# prepare three trees (for single, double, long-double precision)
echo * > files.list
install -d single long-double
cp -a `cat files.list` single
cp -a `cat files.list` long-double
ln -sf . double

# MMX/SSE/etc. seem to be safe because of runtime CPU detection
for ver in single double %{?with_fftwl:long-double} ; do
	OPTS=""
	# k7,SSE,3dnow,altivec only for single
	if [ "$ver" = "single" ]; then
%ifarch i586 k6
		OPTS="--enable-3dnow"
%endif
%ifarch i686
		OPTS="--enable-sse"
%endif
%ifarch athlon
		OPTS="--enable-sse" # "--enable-k7" disabled - causes SEGV on athlons
%endif
%ifarch ppc
		OPTS="--enable-altivec"
%endif
%ifnarch i586 i686 k6 athlon ppc
		:	# keep sh happy about syntax
%endif
	fi
%ifarch i686
	# SSE2 only for double
	if [ "$ver" = "double" ]; then
		OPTS="--enable-sse2"
	fi
%endif
cd $ver
%configure \
	--enable-shared \
	--enable-threads \
	--enable-$ver \
	$OPTS \
	--%{!?debug:dis}%{?debug:en}able-debug

%{__make}

cd ..
done

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C single \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with fftwl}
%{__make} install -C long-double\
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post common-devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun common-devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fftw-wisdom
%attr(755,root,root) %{_libdir}/libfftw3.so.*.*.*
%attr(755,root,root) %{_libdir}/libfftw3_threads.so.*.*.*
%{_mandir}/man1/fftw-wisdom.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfftw3.so
%attr(755,root,root) %{_libdir}/libfftw3_threads.so
%{_libdir}/libfftw3.la
%{_libdir}/libfftw3_threads.la
%{_pkgconfigdir}/fftw3.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libfftw3.a
%{_libdir}/libfftw3_threads.a

%files single
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fftwf-wisdom
%attr(755,root,root) %{_libdir}/libfftw3f.so.*.*.*
%attr(755,root,root) %{_libdir}/libfftw3f_threads.so.*.*.*
%{_mandir}/man1/fftwf-wisdom.1*

%files single-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfftw3f.so
%attr(755,root,root) %{_libdir}/libfftw3f_threads.so
%{_libdir}/libfftw3f.la
%{_libdir}/libfftw3f_threads.la
%{_pkgconfigdir}/fftw3f.pc

%files single-static
%defattr(644,root,root,755)
%{_libdir}/libfftw3f.a
%{_libdir}/libfftw3f_threads.a

%if %{with fftwl}
%files long
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fftwl-wisdom
%attr(755,root,root) %{_libdir}/libfftw3l.so.*.*.*
%attr(755,root,root) %{_libdir}/libfftw3l_threads.so.*.*.*
%{_mandir}/man1/fftwl-wisdom.1*

%files long-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfftw3l.so
%attr(755,root,root) %{_libdir}/libfftw3l_threads.so
%{_libdir}/libfftw3l.la
%{_libdir}/libfftw3l_threads.la
%{_pkgconfigdir}/fftw3l.pc

%files long-static
%defattr(644,root,root,755)
%{_libdir}/libfftw3l.a
%{_libdir}/libfftw3l_threads.a
%endif

%files common
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/fftw-wisdom-to-conf
%{_mandir}/man1/fftw-wisdom-to-conf.1*

%files common-devel
%defattr(644,root,root,755)
%doc doc/html doc/FAQ/fftw-faq.html
%{_includedir}/fftw3.*
%{_infodir}/fftw3.info*
