Summary:	Dockable clock that only displays Beats
Name:		asbeats
Version:	0.2
Release:	3
Copyright:	GPL
Group:		X11/Window Managers/Tools                                                                                     
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source:		http://bohemians.org/~iznogood/asbeats/%{name}-%{version}.tar.gz
URL:		http://bohemians.org/~iznogood/asbeats/
BuildPrereq:	xpm-devel
BuildPrereq:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Dockable application that will display the new Internet time from Swatch
called Beats.

%prep
%setup -q

%build
make CC="gcc $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/bin
install -s asbeats $RPM_BUILD_ROOT/usr/X11R6/bin

gzip -9nf README* CHANGES*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root)
%doc *.gz
%attr(755,root,root) /usr/X11R6/bin/asbeats
