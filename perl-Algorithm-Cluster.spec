%define upstream_name	 Algorithm-Cluster
%define upstream_version 1.50

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Perl interface to Michiel Jan Laurens de Hoon's C clustering library
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module is an interface to the C Clustering Library, a general purpose
library implementing functions for hierarchical clustering (pairwise simple,
complete, average, and centroid linkage), along with k-means and k-medians
clustering, and 2D self-organizing maps. The library is distributed along with
Cluster 3.0, an enhanced version of the famous Cluster program originally
written by Michael Eisen while at Stanford University. The C clustering library
was written by Michiel de Hoon.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
