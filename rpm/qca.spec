#global botan 1

%bcond_without qt5
%bcond_with qt6

#global doc 1
%global tests 1

%global __requires_exclude ^libqca-qt5.*$

Name:    opt-qca
Summary: Qt Cryptographic Architecture
Version: 2.3.5
Release: 1%{?dist}

License: LGPLv2+
URL:     https://userbase.kde.org/QCA
Source0: %{name}-%{version}.tar.bz2
# Also generate pkgconfig file for qt6
#Patch0:  qca-qt6-pkgconfig.patch
## upstream patches

## upstreamable patches
%{?opt_qt5_default_filter}

BuildRequires: cmake >= 2.8.12
BuildRequires: gcc-c++
BuildRequires: libgcrypt-devel
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(libpkcs11-helper-1)
#BuildRequires: pkgconfig(libsasl2)


%if 0%{?doc}
# apidocs
# may need to add some tex-related ones too -- rex
BuildRequires: doxygen-latex
BuildRequires: graphviz
%endif


%description
Taking a hint from the similarly-named Java Cryptography Architecture,
QCA aims to provide a straightforward and cross-platform crypto API,
using Qt datatypes and conventions. QCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
lication!


%if %{with qt5}
%package qt5
Summary: Qt5 Cryptographic Architecture
%{?opt_qt5_default_filter}
BuildRequires: opt-qt5-qtbase-devel
# most runtime consumers seem to assume the ossl plugin be present
Recommends: %{name}-qt5-ossl%{?_isa}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
%description qt5
Taking a hint from the similarly-named Java Cryptography Architecture,
QCA aims to provide a straightforward and cross-platform crypto API,
using Qt datatypes and conventions. QCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
application!

%package qt5-devel
Summary: Qt5 Cryptographic Architecture development files
Requires:  %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.

%if 0%{?botan}
%package qt5-botan
Summary: Botan plugin for the Qt5 Cryptographic Architecture
%{?opt_qt5_default_filter}
BuildRequires: pkgconfig(botan-2)
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
%description qt5-botan
%{summary}.
%endif

#package qt5-cyrus-sasl
#Summary: Cyrus-SASL plugin for the Qt5 Cryptographic Architecture
#Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
#description qt5-cyrus-sasl
#{summary}.

%package qt5-gcrypt
Summary: Gcrypt plugin for the Qt5 Cryptographic Architecture
%{?opt_qt5_default_filter}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
%description qt5-gcrypt
%{summary}.

%package qt5-gnupg
Summary: Gnupg plugin for the Qt Cryptographic Architecture
%{?opt_qt5_default_filter}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: gnupg
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
%description qt5-gnupg
%{summary}.

%package qt5-logger
Summary: Logger plugin for the Qt5 Cryptographic Architecture
%{?opt_qt5_default_filter}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
%description qt5-logger
%{summary}.

%package qt5-nss
Summary: Nss plugin for the Qt5 Cryptographic Architecture
%{?opt_qt5_default_filter}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
%description qt5-nss
%{summary}.

%package qt5-ossl
Summary: Openssl plugin for the Qt5 Cryptographic Architecture
%{?opt_qt5_default_filter}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
%description qt5-ossl
%{summary}.

%package qt5-pkcs11
Summary: Pkcs11 plugin for the Qt5 Cryptographic Architecture
%{?opt_qt5_default_filter}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
%description qt5-pkcs11
%{summary}.

%package qt5-softstore
Summary: Pkcs11 plugin for the Qt5 Cryptographic Architecture
%{?opt_qt5_default_filter}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
%description qt5-softstore
%{summary}.
%endif


%if %{with qt6}
%package qt6
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Core5Compat)
Summary: Qt6 Cryptographic Architecture
# most runtime consumers seem to assume the ossl plugin be present
Recommends: %{name}-qt6-ossl%{?_isa}
%description qt6
Taking a hint from the similarly-named Java Cryptography Architecture,
QCA aims to provide a straightforward and cross-platform crypto API,
using Qt datatypes and conventions. QCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
application!

%package qt6-devel
Summary: Qt6 Cryptographic Architecture development files
Requires:  %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-devel
%{summary}.

%if 0%{?botan}
%package qt6-botan
Summary: Botan plugin for the Qt6 Cryptographic Architecture
BuildRequires: pkgconfig(botan-2)
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-botan
%{summary}.
%endif

%package qt6-cyrus-sasl
Summary: Cyrus-SASL plugin for the Qt6 Cryptographic Architecture
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-cyrus-sasl
%{summary}.

%package qt6-gcrypt
Summary: Gcrypt plugin for the Qt6 Cryptographic Architecture
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-gcrypt
%{summary}.

%package qt6-gnupg
Summary: Gnupg plugin for the Qt Cryptographic Architecture
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Requires: gnupg
%description qt6-gnupg
%{summary}.

%package qt6-logger
Summary: Logger plugin for the Qt6 Cryptographic Architecture
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-logger
%{summary}.

%package qt6-nss
Summary: Nss plugin for the Qt6 Cryptographic Architecture
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-nss
%{summary}.

%package qt6-ossl
Summary: Openssl plugin for the Qt6 Cryptographic Architecture
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-ossl
%{summary}.

%package qt6-pkcs11
Summary: Pkcs11 plugin for the Qt6 Cryptographic Architecture
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-pkcs11
%{summary}.

%package qt6-softstore
Summary: Pkcs11 plugin for the Qt6 Cryptographic Architecture
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-softstore
%{summary}.

%endif


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
export CMAKE_PREFIX_PATH=%{_opt_qt5_prefix}
export CMAKE_INCLUDE_PATH=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

cmake_opts="-Wno-dev \
  -DBUILD_TESTS:BOOL=%{?tests:ON}%{!?tests:OFF} \
  -DQCA_INSTALL_IN_QT_PREFIX:BOOL=ON \
  -DQCA_BINARY_INSTALL_DIR:STRING=%{_opt_qt5_bindir} \
  -DQCA_MAN_INSTALL_DIR:PATH=%{_mandir} \
  -DWITH_botan_PLUGIN:BOOL=%{?botan:ON}%{?!botan:OFF}"
%if %{with qt5}
%define _vpath_builddir %{_target_platform}-qt5
%cmake $cmake_opts \
  -DQCA_INCLUDE_INSTALL_DIR:PATH=%{_opt_qt5_headerdir} \
  -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{_opt_qt5_headerdir} \
  ..

%make_build
%endif


%if %{with qt6}
%define _vpath_builddir %{_target_platform}-qt6
%cmake $cmake_opts \
  -DQT6=ON \
  -DQCA_INCLUDE_INSTALL_DIR:PATH=%{_qt6_headerdir} \
  -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{_qt6_headerdir} \
  ..

%make_build
%endif

%if 0%{?doc}
%cmake_build --target doc
%endif

popd

%install
pushd build

%define _vpath_builddir %{_target_platform}-qt5
make DESTDIR=%{buildroot} install

%if %{with qt6}
%define _vpath_builddir %{_target_platform}-qt6
make DESTDIR=%{buildroot} install
%endif

%if 0%{?doc}
# no make install target for docs yet
mkdir -p %{buildroot}%{_docdir}/qca
cp -a %{_target_platform}/apidocs/html/ \
      %{buildroot}%{_docdir}/qca/
%endif

popd

%check
%if %{with qt5}
%if 0%{?test}
%define _vpath_builddir %{_target_platform}-qt5
export CTEST_OUTPUT_ON_FAILURE=1
export PKG_CONFIG_PATH=%{buildroot}%{_opt_qt5_libdir}/pkgconfig
# skip slow archs
%ifnarch %{arm} ppc64 s390x
test "$(pkg-config --modversion qca2-qt5)" = "%{version}"
%ctest --timeout 180
%endif
%endif
%endif

%if %{with qt6}
%if 0%{?test}
%define _vpath_builddir %{_target_platform}-qt6
export CTEST_OUTPUT_ON_FAILURE=1
export PKG_CONFIG_PATH=%{buildroot}%{_opt_qt5_libdir}/pkgconfig
# skip slow archs
%ifnarch %{arm} ppc64 s390x
test "$(pkg-config --modversion qca2-qt6)" = "%{version}"
%ctest --timeout 180
%endif
%endif
%endif


%if 0%{?doc}
%files doc
%{_docdir}/qca/html/
%endif


%if %{with qt5}
%files qt5
%doc README TODO
%license COPYING
%{_opt_qt5_bindir}/mozcerts-qt5
%{_opt_qt5_bindir}/qcatool-qt5
%{_mandir}/man1/qcatool-qt5.1*
%{_opt_qt5_libdir}/libqca-qt5.so.2*
%dir %{_opt_qt5_plugindir}/crypto/

%files qt5-devel
%{_opt_qt5_headerdir}/QtCrypto
%{_opt_qt5_libdir}/libqca-qt5.so
%{_opt_qt5_libdir}/pkgconfig/qca2-qt5.pc
%{_opt_qt5_libdir}/cmake/Qca-qt5/
%{_opt_qt5_archdatadir}/mkspecs/features/crypto.prf

%if 0%{?botan}
%files qt5-botan
%doc plugins/qca-botan/README
%{_opt_qt5_plugindir}/crypto/libqca-botan.so
%endif

#files qt5-cyrus-sasl
#doc plugins/qca-gcrypt/README
#{_opt_qt5_plugindir}/crypto/libqca-cyrus-sasl.so

%files qt5-gcrypt
%{_opt_qt5_plugindir}/crypto/libqca-gcrypt.so

%files qt5-gnupg
%doc plugins/qca-cyrus-sasl/README
%{_opt_qt5_plugindir}/crypto/libqca-gnupg.so

%files qt5-logger
%doc plugins/qca-logger/README
%{_opt_qt5_plugindir}/crypto/libqca-logger.so

%files qt5-nss
%doc plugins/qca-nss/README
%{_opt_qt5_plugindir}/crypto/libqca-nss.so

%files qt5-ossl
%doc plugins/qca-ossl/README
%{_opt_qt5_plugindir}/crypto/libqca-ossl.so

%files qt5-pkcs11
%doc plugins/qca-pkcs11/README
%{_opt_qt5_plugindir}/crypto/libqca-pkcs11.so

%files qt5-softstore
%doc plugins/qca-softstore/README
%{_opt_qt5_plugindir}/crypto/libqca-softstore.so
%endif


%if %{with qt6}
%files qt6
%doc README TODO
%license COPYING
%{_opt_qt5_bindir}/mozcerts-qt6
%{_opt_qt5_bindir}/qcatool-qt6
%{_mandir}/man1/qcatool-qt6.1*
%{_qt6_libdir}/libqca-qt6.so.2*
%dir %{_qt6_plugindir}/crypto/

%files qt6-devel
%{_qt6_headerdir}/QtCrypto
%{_qt6_libdir}/libqca-qt6.so
%{_opt_qt5_libdir}/pkgconfig/qca2-qt6.pc
%{_opt_qt5_libdir}/cmake/Qca-qt6/

%if 0%{?botan}
%files qt6-botan
%doc plugins/qca-botan/README
%{_qt6_plugindir}/crypto/libqca-botan.so
%endif

%files qt6-cyrus-sasl
%doc plugins/qca-gcrypt/README
%{_qt6_plugindir}/crypto/libqca-cyrus-sasl.so

%files qt6-gcrypt
%{_qt6_plugindir}/crypto/libqca-gcrypt.so

%files qt6-gnupg
%doc plugins/qca-cyrus-sasl/README
%{_qt6_plugindir}/crypto/libqca-gnupg.so

%files qt6-logger
%doc plugins/qca-logger/README
%{_qt6_plugindir}/crypto/libqca-logger.so

%files qt6-nss
%doc plugins/qca-nss/README
%{_qt6_plugindir}/crypto/libqca-nss.so

%files qt6-ossl
%doc plugins/qca-ossl/README
%{_qt6_plugindir}/crypto/libqca-ossl.so

%files qt6-pkcs11
%doc plugins/qca-pkcs11/README
%{_qt6_plugindir}/crypto/libqca-pkcs11.so

%files qt6-softstore
%doc plugins/qca-softstore/README
%{_qt6_plugindir}/crypto/libqca-softstore.so
%endif

