%define name pyaspects
%define version 0.4.1
%define taglevel 1

%define release %{taglevel}%{?pldistro:.%{pldistro}}%{?date:.%{date}}

Summary: Aspect Oriented programming library for Python
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Development/Libraries
Source0: pyaspects-0.4.1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Packager: PlanetLab <devel@planet-lab.org>
Distribution: PlanetLab %{plrelease}
URL: %{SCMURL}

Requires: python

%description
Aspect Oriented programming library for Python

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT

%install
python setup.py install  --root $RPM_BUILD_ROOT
 
%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,-)
/usr

%changelog
* Mon Jan 24 2011 Thierry Parmentelat <thierry.parmentelat@sophia.inria.fr> - pyaspects-0.4.1-1
- no semantic change - just fixed specfile for git URL

* Mon Jun 14 2010 Baris Metin <Talip-Baris.Metin@sophia.inria.fr> - pyaspects-0.3-2
- dummy tag to test module-tools' git support

* Fri Mar 5 2009 Baris Metin <tmetin@sophia.inria.fr>
- initial package
