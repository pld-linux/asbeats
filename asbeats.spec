Summary:	Dockable clock that only displays Beats
Name:		asbeats
Version:	0.2
Release:	3
URL:		http://bohemians.org/~iznogood/asbeats/
Source:		http://bohemians.org/~iznogood/asbeats/%{name}-%{version}.tar.gz
Copyright:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Dockable application that will display the new Internet time from Swatch
called Beats.

%prep
%setup -q

%build
make

%install
install -d $RPM_BUILD_ROOT/usr/X11R6/bin
install -s asbeats $RPM_BUILD_ROOT/usr/X11R6/bin

gzip -9nf README* CHANGES*

%files
%defattr(644,root,root)
%doc *.gz
%attr(755,root,root) /usr/X11R6/bin/asbeats

%changelog
* Mon May 3 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [0.2-3]
- added -q %setup parameter
- changes for common l&f
- added gzipping documentation
- added stripping binary
- removed LICENCE from %doc (GPL)
- added Group(pl)
