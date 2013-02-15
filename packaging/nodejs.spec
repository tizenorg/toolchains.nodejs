Name:          nodejs
Version:       0.6.14
Release:       1
Summary:       Evented I/O for V8 JavaScript
Group:         System/Servers
Vendor:        openmamba
Distribution:  openmamba
Packager:      Silvan Calarco <silvan.calarco@mambasoft.it>
URL:           http://nodejs.org/
Source:        %{name}-%{version}.tar.gz
License:       MIT
## AUTOBUILDREQ-BEGIN
BuildRequires: glibc-devel
BuildRequires: libgcc
BuildRequires: openssl-devel
BuildRequires: libstdc++-devel
BuildRequires: zlib-devel
BuildRequires: python
## AUTOBUILDREQ-END

%description
Evented I/O for V8 JavaScript.

%prep
%setup -q

%build
./configure \
  --prefix=%{_prefix}

make

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"
make DESTDIR=%{buildroot} install

%clean
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%{_bindir}/node
#%{_bindir}/node-repl
%{_bindir}/node-waf
%{_bindir}/npm
%dir %{_includedir}/node
%{_includedir}/node/*
%dir %{_libdir}/node
%dir %{_libdir}/node/wafadmin
%{_libdir}/node/wafadmin/*
%dir %{_libdir}/node_modules
%{_libdir}/node_modules/npm
%{_mandir}/man1/node.1*
#%{_libdir}/pkgconfig/nodejs.pc
%doc AUTHORS ChangeLog LICENSE

%changelog
* Thu Mar 29 2012 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.6.14-1mamba
- update to 0.6.14

* Mon Jul 25 2011 Automatic Build System <autodist@mambasoft.it> 0.5.0-1mamba
- automatic version update by autodist

* Sun Jun 19 2011 Automatic Build System <autodist@mambasoft.it> 0.4.8-1mamba
- automatic update by autodist

* Fri Apr 01 2011 Automatic Build System <autodist@mambasoft.it> 0.4.4-1mamba
- update to 0.4.4

* Wed Jan 12 2011 Silvan Calarco <silvan.calarco@mambasoft.it> v0.2.6-1mamba
- package created by autospec
