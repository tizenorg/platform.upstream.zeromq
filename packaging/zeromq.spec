Name:          zeromq
Version:       3.2.2
Release:       1
Summary:       The ZeroMQ messaging library
Group:         System/Libraries
License:       LGPL-3.0+
URL:           http://www.zeromq.org/
Source:        http://download.zeromq.org/%{name}-%{version}.tar.gz
Source1001:    %name.manifest
BuildRequires: libuuid-devel
Requires:      libuuid

# Build pgm only on supported archs
%ifarch %ix86 x86_64
BuildRequires: python, perl
%endif

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the ZeroMQ shared library.


%package -n libzmq
Summary:    The ZeroMQ messaging library
%description -n libzmq
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the ZeroMQ shared library.

%package devel
Summary:  Development files and static library for the ZeroMQ library
Group:    Development/Libraries
Requires: libzmq = %{version}-%{release}
Requires: pkgconfig

%description devel
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains ZeroMQ related development libraries and header files.

%prep
%setup -q
cp %{SOURCE1001} .
%build
%configure

%{__make} %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig -n libzmq

%postun -p /sbin/ldconfig -n libzmq


%files -n libzmq
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING COPYING.LESSER
%{_libdir}/libzmq.so.3
%{_libdir}/libzmq.so.3.0.0

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/zmq.h
%{_includedir}/zmq_utils.h
%{_libdir}/pkgconfig/libzmq.pc
%{_libdir}/libzmq.so
