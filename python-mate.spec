Summary:	MATE bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek MATE
Name:		python-mate
Version:	1.4.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	dbae06418ac4567ca292d27a33f7b26d
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libmate-devel >= 1.1.0
BuildRequires:	libmatecomponent-devel >= 1.1.0
BuildRequires:	libmatecomponentui-devel >= 1.1.0
BuildRequires:	libmatecanvas-devel >= 1.1.0
BuildRequires:	libmateui-devel >= 1.1.0
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-common
BuildRequires:	mate-conf-devel >= 1.1.0
BuildRequires:	mate-vfs-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-matecorba-devel >= 1.1.0
BuildRequires:	python-pygobject-devel >= 2.17.0
BuildRequires:	python-pygtk-devel >= 2:2.10.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-common = %{version}-%{release}
Requires:	libmate-libs >= 1.1.0
Requires:	python-pygobject >= 2.17.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
MATE bindings for Python.

%description -l pl.UTF-8
Wiązania Pythona do bibliotek MATE.

%package canvas
Summary:	MateCanvas bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki MateCanvas
Group:		Libraries/Python
Requires:	%{name}-common = %{version}-%{release}
Requires:	libmatecanvas >= 1.1.0
Requires:	python-pygobject >= 2.17.0
Requires:	python-pygtk-gtk >= 2:2.10.3

%description canvas
MateCanvas bindings for Python.

%description canvas -l pl.UTF-8
Wiązania Pythona do biblioteki MateCanvas.

%package component
Summary:	MateComponent bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki MateComponent
Group:		Libraries/Python
Requires:	libmatecomponent >= 1.1.0
Requires:	python-matecorba >= 1.1.0
Requires:	python-pygobject >= 2.17.0

%description component
MateComponent bindings for Python.

%description component -l pl.UTF-8
Wiązania Pythona do biblioteki MateComponent.

%package component-ui
Summary:	MateComponent User Interface bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki interfejsu użytkownika MateComponent
Group:		Libraries/Python
Requires:	%{name}-canvas = %{version}-%{release}
Requires:	%{name}-component = %{version}-%{release}
Requires:	libmate-libs >= 1.1.0
Requires:	libmatecomponentui >= 1.1.0
Requires:	python-pygobject >= 2.17.0
Requires:	python-pygtk-gtk >= 2:2.10.3

%description component-ui
MateComponent User Interface bindings for Python.

%description component-ui -l pl.UTF-8
Wiązania Pythona do biblioteki interfejsu użytkownika MateComponent.

%package conf
Summary:	MateConf bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki MateConf
Group:		Libraries/Python
Requires:	%{name}-common = %{version}-%{release}
Requires:	mate-conf-libs >= 1.1.0
Requires:	python-pygobject >= 2.17.0

%description conf
MateConf bindings for Python.

%description conf -l pl.UTF-8
Wiązania Pythona do biblioteki MateConf.

%package ui
Summary:	MATE User Interface bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki interfejsu użytkownika MATE
Group:		Libraries/Python
Requires:	%{name}-canvas = %{version}-%{release}
Requires:	%{name}-component-ui = %{version}-%{release}
Requires:	libmateui >= 1.1.0
Requires:	python-pygobject >= 2.17.0
Requires:	python-pygtk-gtk >= 2:2.10.3

%description ui
MATE User Interface bindings for Python.

%description ui -l pl.UTF-8
Wiązania Pythona do biblioteki interfejsu użytkownika MATE.

%package vfs
Summary:	MateVFS bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki MateVFS
Group:		Libraries/Python
Requires:	%{name}-common = %{version}-%{release}
Requires:	mate-vfs-libs >= 1.1.0
Requires:	python-pygobject >= 2.17.0
# for matevfs.matecomponent and pyvfs bridge
Requires:	libmatecomponent >= 1.1.0
# for matevfs.matecomponent
Requires:	python-matecorba >= 1.1.0

%description vfs
MateVFS bindings for Python.

%description vfs -l pl.UTF-8
Wiązania Pythona do biblioteki MateVFS.

%package common
Summary:	Common files for Python MATE bindings
Summary(pl.UTF-8):	Pliki wspólne wiązań Pythona do MATE
Group:		Libraries/Python
Requires:	python-libs >= 2.2
Requires:	python-pygobject >= 2.17.0

%description common
Common files for Python MATE bindings.

%description common -l pl.UTF-8
Pliki wspólne wiązań Pythona do MATE.

%package devel
Summary:	Development files for Python MATE bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Pythona do MATE
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-canvas = %{version}-%{release}
Requires:	%{name}-component = %{version}-%{release}
Requires:	%{name}-component-ui = %{version}-%{release}
Requires:	%{name}-conf = %{version}-%{release}
Requires:	%{name}-ui = %{version}-%{release}
Requires:	%{name}-vfs = %{version}-%{release}
Requires:	mate-vfs-devel >= 1.1.0
Requires:	python-pygtk-devel >= 2:2.10.3

%description devel
Development files for Python MATE bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Pythona do MATE.

%package apidocs
Summary:	API documentation for Python MATE bindings
Summary(pl.UTF-8):	Dokumentacja API wiązań Pythona do MATE
Group:		Documentation

%description apidocs
API documentation for Python MATE bindings.

%description apidocs -l pl.UTF-8
Dokumentacja API wiązań Pythona do MATE.

%prep
%setup -q

%build
# NOTE: altough configure.ac contains autotools build system deprecation note,
# it's maintained in MATE unlike waf (and there won't be any "future version")
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0{,/mate*}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/mate-vfs-2.0/modules/*.la
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/mate/_mate.so
%{py_sitedir}/gtk-2.0/mate/__init__.py[co]

%files canvas
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/matecanvas.so
%{py_sitedir}/gtk-2.0/mate/canvas.py[co]

%files component
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/matecomponent
%attr(755,root,root) %{py_sitedir}/gtk-2.0/matecomponent/_matecomponent.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/matecomponent/activation.so
%{py_sitedir}/gtk-2.0/matecomponent/__init__.py[co]

%files component-ui
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/matecomponent/ui.so

%files conf
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/mateconf.so

%files ui
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/mate/ui.so

%files vfs
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/matevfs
%attr(755,root,root) %{py_sitedir}/gtk-2.0/matevfs/_matevfs.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/matevfs/matevfsmatecomponent.so
%{py_sitedir}/gtk-2.0/matevfs/__init__.py[co]
%{py_sitedir}/gtk-2.0/mate/vfs.py[co]
%attr(755,root,root) %{_libdir}/mate-vfs-2.0/modules/libpythonmethod.so

%files common
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{py_sitedir}/gtk-2.0/mate

%files devel
%defattr(644,root,root,755)
%{_includedir}/mate-python-2.0
%dir %{_datadir}/pygtk/2.0/argtypes
%{_datadir}/pygtk/2.0/argtypes/matecomponent-arg-types.py*
%{_datadir}/pygtk/2.0/argtypes/mateconf-arg-types.py*
%{pydefsdir}/matecomponent.defs
%{pydefsdir}/matecomponent-types.defs
%{pydefsdir}/matecomponentui.defs
%{pydefsdir}/matecomponentui-types.defs
%{pydefsdir}/mateconf.defs
%dir %{pydefsdir}/mate
%{pydefsdir}/mate/canvas.defs
%{pydefsdir}/mate/mate.defs
%{pydefsdir}/mate/mate-types.defs
%{pydefsdir}/mate/ui.defs
%{_pkgconfigdir}/mate-python-2.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/pymatevfs
