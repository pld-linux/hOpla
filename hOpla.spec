Summary:	XML-SQL link
Summary(pl.UTF-8):	Łącze XML-SQL
Name:		hOpla
Version:	1.0.3
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://ftp.gnu.org/gnu/toutdoux/%{name}-%{version}.tar.gz
# Source0-md5:	7ff236581ab80223b5f82931a8f1260c
URL:		http://www.gnu.org/software/toutdoux/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libxml-devel
BuildRequires:	postgresql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
hOpla links XML files and SQL databases. It can change database's
structure (table, field, type). It also can provide datatable for
applications (add, remove or update).

%description -l pl.UTF-8
hOpla łączy pliki XML z bazami danych SQL. Jest w stanie modyfikować
strukturę baz danych (tabele, pola, typy). Umożliwia także
udostępnianie bazy aplikacjom (dodawanie, usuwanie, aktualizacja).

%package devel
Summary:	hOpla print libraries, includes, etc
Summary(pl.UTF-8):	H0pla print - pliki nagłówkowe itp
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for hOpla.

%description devel -l pl.UTF-8
Pliki nagłówkowe itp. do hOpla.

%package static
Summary:	hOpla static libraries
Summary(pl.UTF-8):	Biblioteki statyczne hOpla
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
hOpla static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne z funkcjami hOpla.

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure  \
	--with-gnome \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/hopla
%dir %{_libdir}/hopla/plugins
%attr(755,root,root) %{_libdir}/hopla/plugins/lib*.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/hopla/plugins/lib*.a
%{_libdir}/lib*.a
