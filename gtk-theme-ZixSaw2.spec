Summary:	ZixSaw2 theme
Summary(pl):	Temat ZixSaw2
Name:		gtk-theme-ZixSaw2
Version:	1.2
Release:	1
License:	GPL
Group:		Themes/Gtk
Source0:	http://download.freshmeat.net/themes/zixsaw2/zixsaw2-1.2.x.tar.gz
URL:		http://themes.freshmeat.net/projects/zixsaw2/?topic_id=923%2C951
Requires:	gtk-engines
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Flat theme without distracting stuff.

%description -l pl
P³aski temat bez zbêdnych drobiazgów.

%prep
%setup  -q -n ZixSaw2

%build
rm -f missing

%install
rm -rf $RPM_BUILD_ROOT

install -d "$RPM_BUILD_ROOT%{_datadir}/themes/ZixSaw2"

cp -pR * $RPM_BUILD_ROOT%{_datadir}/themes/ZixSaw2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/ZixSaw2
