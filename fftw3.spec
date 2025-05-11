# NOTE (for distributors from NEWS file): don't enable too many SIMD variants in
# distribution builds, because it increases planing time; by default enable just
# most popular ones (like SSE, AVX).
# The rest are available by bconds.
#
# TODO: mpi
#
# Conditional build:
%bcond_without	fftwl		# "long" subpackages
%bcond_without	fftwq		# "quad" subpackages
%bcond_without	openmp		# OpenMP support
%bcond_with	avx128fma	# AVX128/FMA instructions (for some AMD machines)
%bcond_with	avx256		# AVX2 256-bit FMA instructions
%bcond_with	avx512		# AVX512 and KCVI [experimental]
#

%ifnarch %{ix86} %{x8664} x32 ia64
%undefine	with_fftwq
%endif

Summary:	Fast Fourier Transform library
Summary(pl.UTF-8):	Biblioteka z funkcjami szybkiej transformaty Fouriera
Summary(pt_BR.UTF-8):	biblioteca fast fourier transform
Name:		fftw3
Version:	3.3.10
Release:	2
License:	GPL v2+
Group:		Libraries
#Source0Download: http://fftw.org/download.html
Source0:	http://fftw.org/fftw-%{version}.tar.gz
# Source0-md5:	8ccbf6a5ea78a16dbc3e1306e234cc5c
Patch0:		%{name}-info.patch
Patch1:		%{name}-flags.patch
Patch2:		fftw-cmake.patch
Patch3:		fftw-cmakedir.patch
URL:		http://www.fftw.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.7
BuildRequires:	gcc-fortran
%ifarch alpha ppc s390 s390x sparc sparcv9
%if %{with fftwl}
# for 128-bit long double support
BuildRequires:	gcc-fortran >= 5:4.1.0-1
BuildRequires:	glibc >= 6:2.4-1
%endif
%endif
%if %{with fftwq}
BuildRequires:	gcc >= 6:4.6.0
BuildRequires:	libquadmath-devel
%endif
%if %{with openmp}
BuildRequires:	gcc >= 6:4.2.0
BuildRequires:	libgomp-devel
%endif
BuildRequires:	libtool
BuildRequires:	rpm-build >= 4.6
BuildRequires:	texinfo
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define builds	single double %{?with_fftwl:long-double} %{?with_fftwq:quad-precision}

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
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-common-devel%{?_isa} = %{version}-%{release}
%{?with_openmp:Requires:	libgomp-devel%{?_isa}}

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
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

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
Requires:	%{name}-common-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-single%{?_isa} = %{version}-%{release}
%{?with_openmp:Requires:	libgomp-devel%{?_isa}}

%description single-devel
This package contains the files you need to develop programs using the
single precision FFTW (fast fourier transform library).

%description single-devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do tworzenia programów używających
biblioteki FFTW (wykonującej szybką transformatę Fouriera) pojedynczej
precyzji.

%package single-static
Summary:	Static fftw single precision libraries
Summary(pl.UTF-8):	Statyczne biblioteki fftw pojedynczej precyzji
Group:		Development/Libraries
Requires:	%{name}-single-devel%{?_isa} = %{version}-%{release}

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
Requires:	%{name}-common-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-long%{?_isa} = %{version}-%{release}
%{?with_openmp:Requires:	libgomp-devel%{?_isa}}

%description long-devel
This package contains the files you need to develop programs using the
long double precision FFTW (fast fourier transform library).

%description long-devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do tworzenia programów używających
biblioteki FFTW (wykonującej szybką transformatę Fouriera)
rozszerzonej precyzji.

%package long-static
Summary:	Static fftw long double precision libraries
Summary(pl.UTF-8):	Statyczne biblioteki fftw rozszerzonej precyzji
Group:		Development/Libraries
Requires:	%{name}-long-devel%{?_isa} = %{version}-%{release}

%description long-static
Static fftw long double precision libraries.

%description long-static -l pl.UTF-8
Statyczne biblioteki fftw rozszerzonej precyzji.

%package quad
Summary:	Fast Fourier Transform library - quad precision
Summary(pl.UTF-8):	Biblioteka z funkcjami szybkiej transformaty Fouriera - poczwórnej precyzji
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}

%description quad
FFTW is a collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions. It includes complex,
real, and parallel transforms, and can handle arbitrary array sizes
efficiently. This RPM package includes the quad precision FFTW
uniprocessor and threads libraries.

%description quad -l pl.UTF-8
FFTW jest zbiorem szybkich funkcji C do obliczania dyskretnych
transformat Fouriera w jednym lub więcej wymiarach. Zawiera również
zespolone, rzeczywiste oraz równoległe transformaty i potrafi wydajnie
radzić sobie z tablicami o dowolnych rozmiarach. Ten pakiet RPM
zawiera wersje FFTW o poczwórnej precyzji dla architektur
jednoprocesorowych oraz z obsługą wątków.

%package quad-devel
Summary:	Development files for quad precision fftw
Summary(pl.UTF-8):	Pliki programistyczne do fftw poczwórnej precyzji
Group:		Development/Libraries
Requires:	%{name}-common-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-quad%{?_isa} = %{version}-%{release}
%{?with_openmp:Requires:	libgomp-devel%{?_isa}}
Requires:	libquadmath-devel%{?_isa}

%description quad-devel
This package contains the files you need to develop programs using the
quad precision FFTW (fast fourier transform library).

%description quad-devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do tworzenia programów używających
biblioteki FFTW (wykonującej szybką transformatę Fouriera) poczwórnej
precyzji.

%package quad-static
Summary:	Static fftw quad precision libraries
Summary(pl.UTF-8):	Statyczne biblioteki fftw poczwórnej precyzji
Group:		Development/Libraries
Requires:	%{name}-quad-devel%{?_isa} = %{version}-%{release}

%description quad-static
Static fftw quad precision libraries.

%description quad-static -l pl.UTF-8
Statyczne biblioteki fftw poczwórnej precyzji.

%package common
Summary:	Files common for all versions of fftw libraries
Summary(pl.UTF-8):	Pliki wspólne dla wszystkich wersji bibliotek fftw
Group:		Libraries
BuildArch:	noarch

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
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}

# MMX/SSE/etc. seem to be safe because of runtime CPU detection
for ver in %{builds}; do
	OPTS=""
	# SSE,altivec,neon@arm[32] only for single
	if [ "$ver" = "single" ]; then
%ifarch pentium3 athlon
		# for SSE2-aware subarchs SSE for single precision is enabled by --enable-sse2 option
		OPTS="--enable-sse"
%endif
%ifarch armv7l armv7hl armv7hnl armv8l armv8hl armv8hnl armv8hcnl aarch64
		OPTS="--enable-neon"
%endif
%ifarch ppc ppc64
		OPTS="--enable-altivec"
%endif
		: # keep sh happy about syntax on other archs
	fi
%ifarch i686 pentium4 %{x8664} x32
	# SSE/SSE2 and AVX only for single and double
	if [ "$ver" = "double" -o "$ver" = "single" ]; then
		OPTS="$OPTS --enable-sse2 --enable-avx"
%if %{with avx256}
		OPTS="$OPTS --enable-avx2"
%endif
%if %{with avx512}
		OPTS="$OPTS --enable-avx512 --enable-kcvi"
%endif
	fi
%endif
%if %{with avx128fma}
	OPTS="$OPTS --enable-avx128-fma"
%endif
%ifarch aarch64
	OPTS="$OPTS --enable-neon"
%endif
%ifarch ppc ppc64
	OPTS="$OPTS --enable-vsx"
%endif
install -d build-${ver}
cd build-${ver}
../%configure \
	--enable-$ver \
	--enable-debug%{!?debug:=no} \
	--enable-openmp \
	--enable-shared \
	--enable-threads \
	$OPTS

%{__make}
cd ..
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fftw

for b in %{builds} ; do
	%{__make} install -C build-${b} \
		DESTDIR=$RPM_BUILD_ROOT
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	single -p /sbin/ldconfig
%postun	single -p /sbin/ldconfig

%post	long -p /sbin/ldconfig
%postun	long -p /sbin/ldconfig

%post	quad -p /sbin/ldconfig
%postun	quad -p /sbin/ldconfig

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
%if %{with openmp}
%attr(755,root,root) %{_libdir}/libfftw3_omp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3_omp.so.3
%endif
%{_mandir}/man1/fftw-wisdom.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfftw3.so
%attr(755,root,root) %{_libdir}/libfftw3_threads.so
%{_libdir}/libfftw3.la
%{_libdir}/libfftw3_threads.la
%if %{with openmp}
%attr(755,root,root) %{_libdir}/libfftw3_omp.so
%{_libdir}/libfftw3_omp.la
%endif
%{_pkgconfigdir}/fftw3.pc
%{_libdir}/cmake/fftw3

%files static
%defattr(644,root,root,755)
%{_libdir}/libfftw3.a
%{_libdir}/libfftw3_threads.a
%if %{with openmp}
%{_libdir}/libfftw3_omp.a
%endif

%files single
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fftwf-wisdom
%attr(755,root,root) %{_libdir}/libfftw3f.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3f.so.3
%attr(755,root,root) %{_libdir}/libfftw3f_threads.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3f_threads.so.3
%if %{with openmp}
%attr(755,root,root) %{_libdir}/libfftw3f_omp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3f_omp.so.3
%endif
%{_mandir}/man1/fftwf-wisdom.1*

%files single-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfftw3f.so
%attr(755,root,root) %{_libdir}/libfftw3f_threads.so
%{_libdir}/libfftw3f.la
%{_libdir}/libfftw3f_threads.la
%if %{with openmp}
%attr(755,root,root) %{_libdir}/libfftw3f_omp.so
%{_libdir}/libfftw3f_omp.la
%endif
%{_pkgconfigdir}/fftw3f.pc
%{_libdir}/cmake/fftw3f

%files single-static
%defattr(644,root,root,755)
%{_libdir}/libfftw3f.a
%{_libdir}/libfftw3f_threads.a
%if %{with openmp}
%{_libdir}/libfftw3f_omp.a
%endif

%if %{with fftwl}
%files long
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fftwl-wisdom
%attr(755,root,root) %{_libdir}/libfftw3l.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3l.so.3
%attr(755,root,root) %{_libdir}/libfftw3l_threads.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3l_threads.so.3
%if %{with openmp}
%attr(755,root,root) %{_libdir}/libfftw3l_omp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3l_omp.so.3
%endif
%{_mandir}/man1/fftwl-wisdom.1*

%files long-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfftw3l.so
%attr(755,root,root) %{_libdir}/libfftw3l_threads.so
%{_libdir}/libfftw3l.la
%{_libdir}/libfftw3l_threads.la
%if %{with openmp}
%attr(755,root,root) %{_libdir}/libfftw3l_omp.so
%{_libdir}/libfftw3l_omp.la
%endif
%{_includedir}/fftw3l.f03
%{_pkgconfigdir}/fftw3l.pc
%{_libdir}/cmake/fftw3l

%files long-static
%defattr(644,root,root,755)
%{_libdir}/libfftw3l.a
%{_libdir}/libfftw3l_threads.a
%if %{with openmp}
%{_libdir}/libfftw3l_omp.a
%endif
%endif

%if %{with fftwq}
%files quad
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fftwq-wisdom
%attr(755,root,root) %{_libdir}/libfftw3q.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3q.so.3
%attr(755,root,root) %{_libdir}/libfftw3q_threads.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3q_threads.so.3
%if %{with openmp}
%attr(755,root,root) %{_libdir}/libfftw3q_omp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfftw3q_omp.so.3
%endif
%{_mandir}/man1/fftwq-wisdom.1*

%files quad-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfftw3q.so
%attr(755,root,root) %{_libdir}/libfftw3q_threads.so
%{_libdir}/libfftw3q.la
%{_libdir}/libfftw3q_threads.la
%if %{with openmp}
%attr(755,root,root) %{_libdir}/libfftw3q_omp.so
%{_libdir}/libfftw3q_omp.la
%endif
%{_includedir}/fftw3q.f03
%{_pkgconfigdir}/fftw3q.pc
%{_libdir}/cmake/fftw3q

%files quad-static
%defattr(644,root,root,755)
%{_libdir}/libfftw3q.a
%{_libdir}/libfftw3q_threads.a
%if %{with openmp}
%{_libdir}/libfftw3q_omp.a
%endif
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
%{_includedir}/fftw3.f03
%{_includedir}/fftw3.h
%{_infodir}/fftw3.info*
