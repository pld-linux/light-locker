Summary:	A simple session-locker for lightdm
Name:		light-locker
Version:	1.9.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://github.com/the-cavalry/light-locker/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d10b85757b02df0c82e42c0ada4f3a9a
URL:		https://github.com/the-cavalry/light-locker
BuildRequires:	ConsoleKit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	glib2-devel >= 1:2.25.6
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	systemd-devel
BuildRequires:	upower-devel
BuildRequires:	xfce4-dev-tools
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires:	glib2 >= 1:2.26.0
Requires:	lightdm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
light-locker is a simple locker (forked from gnome-screensaver) that
aims to have simple, sane, secure defaults and be well integrated with
the desktop while not carrying any desktop-specific dependencies. It
relies on lightdm for locking and unlocking your session via
ConsoleKit/UPower or logind/systemd.

%prep
%setup -q

%build
NOCONFIGURE=1 xdt-autogen
%configure \
	--with-x \
	--with-mit-ext \
	--with-dpms-ext \
	--with-xf86gamma-ext \
	--with-console-kit \
	--with-systemd \
	--with-upower \
	--enable-settings-backend=gsettings \
	--enable-late-locking \
	--enable-lock-on-suspend
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS HACKING NEWS README
/etc/xdg/autostart/light-locker.desktop
%attr(755,root,root) %{_bindir}/light-locker
%attr(755,root,root) %{_bindir}/light-locker-command
%{_datadir}/glib-2.0/schemas/apps.light-locker.gschema.xml
%{_mandir}/man1/light-locker-command.1*
%{_mandir}/man1/light-locker.1*
