Summary: Dockable clock that only displays Beats
Name: asbeats
Version: 0.2
Release: 2
Source: http://bohemians.org/~iznogood/asbeats/%{name}-%{version}.tar.gz
URL: http://bohemians.org/~iznogood/asbeats/
Copyright: GPL
Group: X11/Utilities
Packager: Karl-Martin Skontorp <karl-ms@online.no>
BuildRoot: /var/tmp/%{name}-%{version}-root

%description
Dockable application that will display the new Internet time from Swatch
called Beats.

%prep
%setup

%build
make

%install
install -d $RPM_BUILD_ROOT/usr/X11R6/bin
install -m755 asbeats $RPM_BUILD_ROOT/usr/X11R6/bin

%files
%defattr(-,root,root)
%doc README README.asclock LICENCE CHANGES
%attr(0755,root,root) /usr/X11R6/bin/asbeats
