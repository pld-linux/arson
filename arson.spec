#
# TODO:
# Files %{_datadir}/mimelnk/application/{x-cue,x-iso}.desktop
# conflict with files from package k3b-0.7.5-2

%define		_kdever		kde3

Summary:	Tool for CD recording
Summary(pl.UTF-8):	Narzędzie do nagrywania płyt CD
Name:		arson
Version:	0.9.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-%{_kdever}.tar.bz2
# Source0-md5:	baf05d52128dd75d72298b4011e2e353
URL:		http://arson.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.0
Requires:	kdelibs >= 3.0
Requires:	cdrdao
Requires:	cdrtools
Requires:	cdrtools-cdda2wav
Requires:	cdrtools-mkisofs
Requires:	cdparanoia-III
Requires:	mpg123
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Tool for CD recording.

%description -l pl.UTF-8
Narzędzie do nagrywania płyt CD.

%prep
%setup -q -n %{name}-%{version}-%{_kdever}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kdelnkdir=%{_applnkdir}/Utilities/CD-RW

%find_lang	%{name}		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DESCRIPTION FEATURES HELPME NEWS README REQUIREMENTS THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/* # specify excplicit dirs here (to avoid packaging kde dirs)
%{_datadir}/config/*
%{_datadir}/mimelnk/application/*
%{_applnkdir}/Utilities/CD-RW/*
%{_pixmapsdir}/[!l]*/*/*/*
