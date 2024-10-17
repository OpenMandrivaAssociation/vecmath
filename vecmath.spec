%{?_javapackages_macros:%_javapackages_macros}
%global commit 41fddda1a4f430e45bef0154e1fdfe5671025f1e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          vecmath
Version:       1.6.0
Release:       0.1.20130710git41fddda.0%{?dist}
Summary:       The 3D vector math Java package, javax.vecmath

# License is GNU General Public License, version 2, with the Classpath Exception
License:       GPLv2 with exceptions
URL:           https://github.com/hharrison/vecmath
Source0:       https://github.com/hharrison/vecmath/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# Fix link to javadoc
Patch0:        %{name}-%{version}-javadoc-link.patch
BuildArch:     noarch

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: java-devel >= 1:1.6.0
BuildRequires: java-javadoc
BuildRequires: jpackage-utils

Requires:      java >= 1:1.6.0
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

%changelog
* Thu Sep 5 2013 Harvey Harrison <harvey.harrison@gmail.com> - 1.6.0-0.1.20130710git41fddda
- change upstream source to github
- upgrade to 1.6.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 07 2012 gil cattaneo <puntogil@libero.it> 1.5.2-1
- Use tarball from 1.5.2 tag (no change in source code)
- Added maven pom
- Adapt to current guideline
- Added javadoc sub package

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.20090922cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-4.20090922cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.20090922cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 28 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-2.20090922cvs
- Minor review fixes.

* Tue Sep 22 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-1.20090922cvs
- First release.
