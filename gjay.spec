Name: 	 	gjay
Summary: 	Automated music manager for DJ applications
Version: 	0.2.8.3
Release: 	 %mkrel 3

Source:		%{name}-%{version}.tar.bz2
Patch0:     gjay-0.2.8.3-gcc34.patch.bz2
URL:		http://gjay.sourceforge.net/
License:	GPL
Group:		Sound
BuildRequires:	gtk+1.2-devel libvorbis-devel gsl-devel xmms-devel pkgconfig gtk2-devel
Requires:	mp3info mpg321 vorbis-tools xmms

%description
GJay (Gtk+ DJ) generates playlists across a collection of music (ogg, mp3,
wav) such that each song sounds good following the previous song. It is ideal
for home users who want a non-random way to wander large collections or for
DJs planning a set list. You can generate playlists from within the
application, or run GJay as a standalone command-line utility.

%prep
%setup -q
%patch0 -p0

%build
%make
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
mkdir -p $RPM_BUILD_ROOT/%_datadir/%name/icons
%makeinstall PREFIX=$RPM_BUILD_ROOT/%_prefix INSTALL="%_bindir/install -m"
strip $RPM_BUILD_ROOT/%_bindir/%name

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
	command="%{name}" \
	icon="sound_section.png" \
	needs="x11" \
	title="GJay" \
	longtitle="DJ Collection Manager" \
	section="Multimedia/Sound"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_datadir}/%name
%{_mandir}/man1/*
%{_menudir}/%name

