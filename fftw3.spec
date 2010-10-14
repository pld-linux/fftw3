#
# Conditional build:
%bcond_without	fftwl	# don't build "long" subpackages
#
Summary:	Fast Fourier Transform library
Summary(pl.UTF-8):	Biblioteka z funkcjami szybkiej transformaty Fouriera
Summary(pt_BR.UTF-8):	biblioteca fast fourier transform
Name:		fftw3
Version:	3.2.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	ftp://ftp.fftw.org/pub/fftw/fftw-%{version}.tar.gz
# Source0-md5:	b616e5c91218cc778b5aa735fefb61ae
Patch0:		%{name}-info.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-ac_simd.patch
URL:		http://www.fftw.org/
BuildRequires:	autoconf
BuildRequires:	automake
%ifarch alpha ppc s390 s390x sparc sparcv9
%if %{with fftwl}
# for 128-bit long double support
BuildRequires:	gcc-fortran >= 5:4.1.0-1
BuildRequires:	glibc >= 6:2.4-1
%endif
%endif
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

%description -l pl.UTF-8
FFTW jest zbiorem szybkich funkcji C do obliczania dyskretnych
transformat Fouriera w jednym lub więcej wymiarach. Zawiera również
zespolone, rzeczywiste oraz równoległe transformaty i potrafi wydajnie
radzić sobie z tablicami o dowolnych rozmiarach. Ten pakiet RPM
zawiera wersje FFTW o podwójnej precyzji dla architektur
jednoprocesorowych oraz z obsługą wątków.

%description -l pt_BR.UTF-8
FFTW é uma coleção de rotinas rápidas em C para computar a Discrete
Fourier Transform em uma ou mais dimensões. Incluindo transformações
complexas, reais e paralelas, também pode manipular vetores de tamanho
arbitrário eficientemente. Esse pacote RPM inclui bibliotecas FFTW com
suporte a threads, normal e dupla precisão (Os arquivos de precisão
normal tem um prefixo "s").

%package devel
Summary:	Development files for fftw
Summary(pl.UTF-8):	Pliki programistyczne do fftw
Summary(pt_BR.UTF-8):	Headers e documentação do pacote FFTW
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-common-devel = %{version}-%{release}

%description devel
This package contains the files you need to develop programs using the
FFTW (fast fourier transform library).

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do tworzenia programów używających
biblioteki FFTW (wykonującej szybką transformatę Fouriera).

%description devel -l pt_BR.UTF-8
Este pacote contém documentação e headers adicionais para desenvolver
programas usando a FFTW.

%package static
Summary:	Static fftw libraries
Summary(pl.UTF-8):	Statyczne biblioteki fftw
Summary(pt_BR.UTF-8):	Bibliotecas estáticas do pacote FFTW
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static fftw libraries.

%description static -l pl.UTF-8
Statyczne biblioteki fftw.

%description static -l pt_BR.UTF-8
Este pacote contém as bibliotecas estáticas do pacote FFTW.

%package single
Summary:	Fast Fourier Transform library - single precision
Summary(pl.UTF-8):	Biblioteka z funkcjami szybkiej transformaty Fouriera - pojedynczej precyzji
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}

%description single
FFTW is a collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions. It includes complex,
real, and parallel transforms, and can handle arbitrary array sizes
efficiently. This RPM package includes the single precision FFTW
uniprocessor and threads libraries.

%description single -l pl.UTF-8
FFTW jest zbiorem szybkich funkcji C do obliczania dyskretnych
transformat Fouriera w jednym lub więcej wymiarach. Zawiera również
zespolone, rzeczywiste oraz równoległe transformaty i potrafi wydajnie
radzić sobie z tablicami o dowolnych rozmiarach. Ten pakiet RPM
zawiera wersje FFTW o pojedynczej precyzji dla architektur
jednoprocesorowych oraz z obsługą wątków.

%package single-devel
Summary:	Development files for single precision fftw
Summary(pl.UTF-8):	Pliki programistyczne do fftw pojedynczej precyzji
Group:		Development/Libraries
Requires:	%{name}-common-devel = %{version}-%{release}
Requires:	%{name}-single = %{version}-%{release}

%description single-devel
This package contains the files you need to develop programs using the
single precision FFTW (fast fourier transform library).

%description single-devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do tworzenia programów używających
biblioteki FFTW pojedynczej precyzji (wykonującej szybką transformatę
Fouriera).

%package single-static
Summary:	Static fftw single precision libraries
Summary(pl.UTF-8):	Statyczne biblioteki fftw pojedynczej precyzji
Group:		Development/Libraries
Requires:	%{name}-single-devel = %{version}-%{release}

%description single-static
Static fftw single precision libraries.

%description single-static -l pl.UTF-8
Statyczne biblioteki fftw pojedynczej precyzji.

%package long
Summary:	Fast Fourier Transform library - long double precision
Summary(pl.UTF-8):	Biblioteka z funkcjami szybkiej transformaty Fouriera - rozszerzonej precyzji
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}

%description long
FFTW is a collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions. It includes complex,
real, and parallel transforms, and can handle arbitrary array sizes
efficiently. This RPM package includes the long double precision FFTW
uniprocessor and threads libraries.

%description long -l pl.UTF-8
FFTW jest zbiorem szybkich funkcji C do obliczania dyskretnych
transformat Fouriera w jednym lub więcej wymiarach. Zawiera również
zespolone, rzeczywiste oraz równoległe transformaty i potrafi wydajnie
radzić sobie z tablicami o dowolnych rozmiarach. Ten pakiet RPM
zawiera wersje FFTW o rozszerzonej precyzji dla architektur
jednoprocesorowych oraz z obsługą wątków.

%package long-devel
Summary:	Development files for long double precision fftw
Summary(pl.UTF-8):	Pliki programistyczne do fftw rozszerzonej precyzji
Group:		Development/Libraries
Requires:	%{name}-common-devel = %{version}-%{release}
Requires:	%{name}-long = %{version}-%{release}

%description long-devel
This package contains the files you need to develop programs using the
long double precision FFTW (fast fourier transform library).

%description long-devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do tworzenia programów używających
biblioteki FFTW rozszerzonej precyzji (wykonującej szybką transformatę
Fouriera).

%package long-static
Summary:	Static fftw long double precision libraries
Summary(pl.UTF-8):	Statyczne biblioteki fftw rozszerzonej precyzji
Group:		Development/Libraries
Requires:	%{name}-long-devel = %{version}-%{release}

%description long-static
Static fftw long double precision libraries.

%description long-static -l pl.UTF-8
Statyczne biblioteki fftw rozszerzonej precyzji.

%package common
Summary:	Files common for all versions of fftw libraries
Summary(pl.UTF-8):	Pliki wspólne dla wszystkich wersji bibliotek fftw
Group:		Libraries

%description common
Files common for all versions of fftw libraries (basic documentation,
fftw-wisdom-to-conf utility).

%description common -l pl.UTF-8
Pliki wspólne dla wszystkich wersji bibliotek fftw (podstawowa
dokumentacja, narzędzie fftw-wisdom-to-conf).

%package common-devel
Summary:	Development files common for all versions of fftw libraries
Summary(pl.UTF-8):	Pliki programistyczne wspólne dla wszystkich wersji bibliotek fftw
Group:		Development/Libraries
Requires:	%{name}-common = %{version}-%{release}

%description common-devel
Development files common for all versions of fftw libraries (header
files, development documentation).

%description common-devel -l pl.UTF-8
Pliki programistyczne wspólne dla wszystkich wersji bibliotek fftw
(pliki nagłówkowe, dokumentacja programisty).

%prep
%setup -q -n fftw-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}

# MMX/SSE/etc. seem to be safe because of runtime CPU detection
for ver in single double %{?with_fftwl:long-double}; do
	OPTS=""
	# k7,SSE,3dnow,altivec only for single
	if [ "$ver" = "single" ]; then
%ifarch i686
		OPTS="--enable-sse"
%endif
%ifarch athlon
		OPTS="--enable-sse" # no "--enable-k7" - conflicts with shared, SEGV on athlons
%endif
%ifarch ppc
		OPTS="--enable-altivec"
%endif
%ifnarch i686 k6 athlon ppc
		:	# keep sh happy about syntax
%endif
	fi
%ifarch i686
	# SSE2 only for double
	if [ "$ver" = "double" ]; then
		OPTS="--enable-sse2"
	fi
%endif
install -d build-${ver}
cd build-${ver}
../%configure \
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
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fftw

%{__make} install -C build-single \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C build-double \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with fftwl}
%{__make} install -C build-long-double \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	single -p /sbin/ldconfig
%postun	single -p /sbin/ldconfig

%post	long -p /sbin/ldconfig
%postun	long -p /sbin/ldconfig

%post	common-devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	common-devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fftw-wisdom
%attr(755,root,root) %{_libdir}/libfftw3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3.so.3
%attr(755,root,root) %{_libdir}/libfftw3_threads.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3_threads.so.3
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
%attr(755,root,root) %ghost %{_libdir}/libfftw3f.so.3
%attr(755,root,root) %{_libdir}/libfftw3f_threads.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3f_threads.so.3
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
%attr(755,root,root) %ghost %{_libdir}/libfftw3l.so.3
%attr(755,root,root) %{_libdir}/libfftw3l_threads.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3l_threads.so.3
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
%dir %{_sysconfdir}/fftw
%attr(755,root,root) %{_bindir}/fftw-wisdom-to-conf
%{_mandir}/man1/fftw-wisdom-to-conf.1*

%files common-devel
%defattr(644,root,root,755)
%doc doc/html doc/FAQ/fftw-faq.html
%{_includedir}/fftw3.f
%{_includedir}/fftw3.h
%{_infodir}/fftw3.info*
