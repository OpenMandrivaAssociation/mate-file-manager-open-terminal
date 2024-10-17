Summary:	Caja extension for an open terminal shortcut
Name:		mate-file-manager-open-terminal
Version:	1.4.0
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
URL:		https://pub.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-desktop-2.0)

Requires:	mate-conf
Provides:	caja-open-terminal = %{EVRD}

%description
The caja-open-terminal extension provides a right-click "Open
Terminal" option for caja users who prefer that option.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang caja-open-terminal

%files -f caja-open-terminal.lang
%doc AUTHORS ChangeLog COPYING NEWS TODO
%{_sysconfdir}/mateconf/schemas/*
%{_libdir}/caja/extensions-2.0/*.so*



%changelog
* Thu Jun 07 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 803046
- imported package mate-file-manager-open-terminal

