Summary:	Dockable clock that only displays Beats
Name:		asbeats
Version:	0.2
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools                                                                                     
######		Unknown group!
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://bohemians.org/~iznogood/asbeats/%{name}-%{version}.tar.gz
URL:		http://bohemians.org/~iznogood/asbeats/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Dockable application that will display the new Internet time from
Swatch called Beats.

%prep
%setup -q

%build
%{__make} CC="gcc $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -s asbeats $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README* CHANGES*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/asbeats
