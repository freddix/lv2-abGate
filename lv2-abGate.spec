%define		rname	abGate

Summary:	LV2 Noise Gate
Name:		lv2-abGate
Version:	1.1.6
Release:	1
License:	GPL v3
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/project/abgate/abGate-source/%{rname}-%{version}.tar.gz
# Source0-md5:	1c8aea03d44ef023cef3451a9fb16c91
BuildRequires:	gtkmm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -qn %{rname}-%{version}

%{__sed} -i -e "s/g++/%{__cxx}/g" \
	-e "s/-O3/%{rpmcxxflags}/g" Makefile

%ifarch %{x8664}
%{__sed} -i -e "s|/usr/lib|%{_libdir}|" plugin_configuration.h
%endif

%build
%{__make} \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_libdir}/lv2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_libdir}/lv2/%{rname}.lv2
%attr(755,root,root) %{_libdir}/lv2/%{rname}.lv2/*.so
%{_libdir}/lv2/%{rname}.lv2/*.png
%{_libdir}/lv2/%{rname}.lv2/*.ttl

