%define module	Algorithm-Cluster
%define name	perl-%{module}
%define version	1.43
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl interface to Michiel Jan Laurens de Hoon's C clustering library
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Algorithm/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module is an interface to the C Clustering Library, a general purpose
library implementing functions for hierarchical clustering (pairwise simple,
complete, average, and centroid linkage), along with k-means and k-medians
clustering, and 2D self-organizing maps. The library is distributed along with
Cluster 3.0, an enhanced version of the famous Cluster program originally
written by Michael Eisen while at Stanford University. The C clustering library
was written by Michiel de Hoon.

%prep
%setup -q -n %{module}-%{version}
perl -pi -e 's|^#!/usr/perl/perl580/bin/perl|#!/usr/bin/perl|' perl/examples/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL README perl/examples
%{perl_vendorarch}/Algorithm
%{perl_vendorarch}/auto/Algorithm
%{_mandir}/*/*



