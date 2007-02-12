Summary:	Dockable clock that only displays Beats
Summary(pl.UTF-8):   Dokowalny zegar wyświetlający tylko Beats
Name:		asbeats
Version:	0.2
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://bohemians.org/~iznogood/asbeats/%{name}-%{version}.tar.gz
# Source0-md5:	b323d177f077818b6d0f93319bee902d
URL:		http://bohemians.org/~iznogood/asbeats/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dockable application that will display the new Internet time from
Swatch called Beats.

%description -l pl.UTF-8
Dokowalna aplikacja wyświetlająca nowy czas internetowy z zegara
nazwanego Beats.

%prep
%setup -q

%build
%{__make} CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install asbeats $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* CHANGES*
%attr(755,root,root) %{_bindir}/asbeats
