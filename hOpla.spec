Summary:	XML-SQL link
Summary(pl):	£±cze XML-SQL
Name:		hOpla
Version:	1.0.3
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://hopla.sourceforge.net/dl/%{name}-%{version}.tar.gz
URL:		http://hopla.sourceforge.net/
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libxml-devel
BuildRequires:	postgresql-devel
BuildRequires:	bison
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
hOpla links XML files and SQL databases. It can change database's
structure (table, field, type). It also can provide datatable for
applications (add, remove or update).

%description -l pl
hOpla ³±czy pliki XML z bazami danych SQL. Jest w stanie modyfikowaæ
strukturê baz danych (tabele, pola, typy). Umo¿liwia tak¿e
udostêpnianie bazy aplikacjom (dodawanie, usuwanie, aktualizacja).

%package devel
Summary:	hOpla print libraries, includes, etc
Summary(pl):	H0pla print - pliki nag³ówkowe itp
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for hOpla.

%description devel -l pl
Pliki nag³ówkowe itp. do hOpla.

%package static
Summary:	hOpla static libraries
Summary(pl):	Biblioteki statyczne hOpla
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
hOpla static libraries.

%description static -l pl
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

%{__make} DESTDIR=$RPM_BUILD_ROOT install

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
