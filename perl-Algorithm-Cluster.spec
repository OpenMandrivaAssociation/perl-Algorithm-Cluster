%define upstream_name	 Algorithm-Cluster
%define upstream_version 1.52

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl interface to Michiel Jan Laurens de Hoon's C clustering library
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Algorithm/Algorithm-Cluster-%{upstream_version}.tar.gz

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.500.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.500.0-2
+ Revision: 680444
- mass rebuild

* Wed Dec 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.500.0-1mdv2011.0
+ Revision: 625947
- update to new version 1.50

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.490.0-2mdv2011.0
+ Revision: 555218
- rebuild

* Tue Apr 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.490.0-1mdv2010.1
+ Revision: 536957
- update to 1.49
- update to 1.48
- update to 1.47

* Sun Sep 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.470.0-1mdv2010.0
+ Revision: 438652
- update to new version 1.47

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.460.0-1mdv2010.0
+ Revision: 402091
- rebuild using %%perl_convert_version

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.46-1mdv2010.0
+ Revision: 383471
- update to new version 1.46

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.45-1mdv2010.0
+ Revision: 370006
- update to new version 1.45

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.43-1mdv2009.1
+ Revision: 291999
- update to new version 1.43
- update to new version 1.42

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.41-1mdv2009.0
+ Revision: 277939
- update to new version 1.41

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.40-1mdv2009.0
+ Revision: 270334
- update to new version 1.40

* Tue Jul 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.39-1mdv2009.0
+ Revision: 232707
- update to new version 1.39

* Sun Mar 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.38-1mdv2008.1
+ Revision: 183107
- update to new version 1.38

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 1.37-2mdv2008.1
+ Revision: 151803
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Nov 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.37-1mdv2008.1
+ Revision: 110889
- update to new version 1.37

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.36-1mdv2008.0
+ Revision: 46308
- update to new version 1.36


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.35-1mdv2007.0
+ Revision: 133729
- new version

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - import perl-Algorithm-Cluster-1.33-1mdv2007.0

* Fri Sep 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.33-1mdv2007.0
- New version 1.33

* Thu Jun 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.32-1mdv2007.0
- New version 1.32
- better source URL
- use standard optimisations

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.31-2mdk
- Fix BuildRequires Using perl Policies
	- Source URL 
- use mkrel

* Wed Mar 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.31-1mdk
- New release 1.31

* Wed Nov 02 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-1mdk
- New release 1.30

* Wed Jun 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.29-2mdk 
- make test only once in %%check
- spec cleanup
- fix examples shellbang

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.29-1mdk
- 1.29

* Wed Mar 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.28-1mdk
- 1.28
- add tests

* Mon Nov 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.27-2mdk 
- rebuild for new perl

* Wed Sep 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.27-1mdk 
- first mdk release


