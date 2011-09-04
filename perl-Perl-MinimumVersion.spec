Name:           perl-Perl-MinimumVersion
Version:        1.20
Release:        3%{?dist}
Summary:        Find a minimum required version of perl for Perl code
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Perl-MinimumVersion/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Perl-MinimumVersion-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires: perl(List::Util) >= 1.19
BuildRequires: perl(PPI) >= 1.118
BuildRequires: perl(Test::Script) >= 1.02
BuildRequires: perl(version)
BuildRequires: perl(File::Find::Rule) >= 0.30
BuildRequires: perl(File::Find::Rule::Perl) >= 1.04
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(Test::More) >= 0.47

# For improved tests
BuildRequires: perl(Test::Pod) >= 1.00
BuildRequires: perl(Test::CPAN::Meta) >= 0.12
# n/a in Fedora
# BuildRequires: perl(Pod::Simple) >= 3.07
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Test::MinimumVersion) >= 0.008


%description
Find a minimum required version of perl for Perl code

%prep
%setup -q -n Perl-MinimumVersion-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test AUTOMATED_TESTING=1

%files
%defattr(-,root,root,-)
%doc Changes LICENSE
%{_bindir}/*
%{perl_vendorlib}/Perl
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.20-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 26 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.20-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 16 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.19-1
- Upstream update.

* Mon Aug 25 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.18-1
- Upstream update.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.15-5
- Rebuild for perl 5.10 (again)

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.15-4
- correct List::Util version, perl 5.10.0 has 1.19

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.15-3
- rebuild for new perl

* Thu Jan 10 2008 Ralf Corsépius <rc040203@freenet.de> - 0.15.2
- Use unversioned BR: perl(version) to circumvent perl vs. rpm versioning 
  conflicts

* Tue Nov 20 2007 Ralf Corsépius <rc040203@freenet.de> - 0.15-1
- Initial version.
