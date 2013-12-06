%global commit 41fddda1a4f430e45bef0154e1fdfe5671025f1e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          vecmath
Version:       1.6.0
Release:       0.1.20130710git41fddda%{?dist}
Summary:       The 3D vector math Java package, javax.vecmath

# License is GNU General Public License, version 2, with the Classpath Exception
License:       GPLv2 with exceptions
URL:           http://github.com/hharrison/vecmath
Source0:       https://github.com/hharrison/vecmath/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# Fix link to javadoc
Patch0:        %{name}-%{version}-javadoc-link.patch
BuildArch:     noarch

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: java-devel
BuildRequires: java-javadoc
BuildRequires: java-rpmbuild
BuildRequires: jpackage-utils

Requires:      java
Requires:      jpackage-utils

%description
The 3D vector math Java package, javax.vecmath.

%package javadoc

Summary:       Javadoc for %{name}
Requires:      jpackage-utils

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -qn %{name}-%{commit}
%patch0 -p0

%build
%ant jar docs

%install
install -D -p -m 644 build/jars/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc docs/api-changes* COPYRIGHT.txt LICENSE.txt LICENSE-SPEC.html
%{_javadir}/%{name}.jar

%files javadoc
%doc COPYRIGHT.txt LICENSE.txt LICENSE-SPEC.html
%{_javadocdir}/%{name}
