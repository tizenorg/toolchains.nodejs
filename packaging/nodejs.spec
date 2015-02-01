Name:          nodejs
Version:       0.10.29
Release:       1
Summary:       Evented I/O for V8 JavaScript
Group:         System/Service
URL:           http://nodejs.org/
Source0:       %{name}-%{version}.tar.gz
Source1:       nodejs.pc
Patch1:	       no-parallel.patch
License:       MIT
BuildRequires: glibc-devel
BuildRequires: openssl-devel
BuildRequires: libstdc++-devel
BuildRequires: zlib-devel
BuildRequires: python
BuildRequires: fdupes
BuildRequires: which

%description
Node.js is a platform built on Chromes JavaScript runtime for easily building fast,
scalable network applications. Node.js uses an event-driven, non-blocking I/O model
that makes it lightweight and efficient, perfect for data-intensive real-time
applications that run across distributed devices.

%package devel
Summary: Development package for nodejs
Group:   Development/Libraries
Requires: %{name} = %{version}

%description devel
dev package

%ifarch %{arm}
%package -n nodejs-x86-arm
Summary: node x86 runtime - speed up building node related packages
Group:   Development/Libraries
Requires: %{name}-devel = %{version}
AutoReqProv: no

%description -n nodejs-x86-arm
node x86 runtime - speed up building node related packages
%endif

%prep
%setup -q

%patch1 -p1

%build

./configure --prefix=%{_prefix} --without-dtrace \
	--shared-openssl \
	--shared-zlib 

make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}/usr/lib/pkgconfig
install -m0644 %SOURCE1 %{buildroot}/usr/lib/pkgconfig

# cleanup leftover cruft
rm -fR %{buildroot}/usr/lib/dtrace
find %{buildroot}/usr/lib/node_modules -name '\.*' -delete

%ifarch %{arm}
mkdir -p %{buildroot}/emul/ia32-linux/usr/bin/
install -m0755 node-x86/node %{buildroot}/emul/ia32-linux/usr/bin/
%endif

%fdupes %{buildroot}/usr/lib/node_modules

%docs_package

%ifarch %{arm}
%post -n nodejs-x86-arm
if test -e /usr/bin/node.orig-arm -a -h /usr/bin/node; then 
    echo "skipping change /usr/bin/node"
else
    mv /usr/bin/node /usr/bin/node.orig-arm
    ln -sf /emul/ia32-linux/usr/bin/node /usr/bin/node
fi
%endif

%files
%defattr(-,root,root)
%{_bindir}/node
%exclude %{_bindir}/npm
%exclude %dir /usr/lib/node_modules
%exclude %dir /usr/lib/node_modules/npm
%exclude /usr/lib/node_modules/npm/*

%files devel
/usr/include/node/*
/usr/lib/pkgconfig/nodejs.pc

%ifarch %{arm}
%files -n nodejs-x86-arm
/emul/ia32-linux/usr/bin/node
%endif
