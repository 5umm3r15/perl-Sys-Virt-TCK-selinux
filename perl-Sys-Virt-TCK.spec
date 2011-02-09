# Automatically generated by perl-Sys-Virt-TCK.spec.PL

%define perlvendorlib %(perl -e 'use Config; print $Config{installvendorlib}')
%define perlvendorprefix %(perl -e 'use Config; print $Config{vendorprefix}')
%define perlvendorman1 %{perlvendorprefix}/share/man/man1
%define perlvendorman3 %{perlvendorprefix}/share/man/man3

%define appname Sys-Virt-TCK

Summary: Sys::Virt::TCK - libvirt Technology Compatibility Kit
Name: perl-%{appname}
Version: 0.1.0
Release: 9%{dist}
License: GPLv2 or Artistic
Group: Development/Tools
Source: http://libvirt.org/sources/tck/%{appname}-%{version}.tar.gz
Patch1: %{appname}-%{version}-cleanup-skip.patch
Patch2: %{appname}-%{version}-skip-dom0.patch
Patch3: %{appname}-%{version}-i686-pae-kernels.patch
Patch4: %{appname}-%{version}-clone-api.patch
Url: http://libvirt.org/
BuildRoot: %{_tmppath}/%{appname}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: libvirt >= 0.6.4
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires: perl(accessors)
BuildRequires: perl(App::Prove)
BuildRequires: perl(Config::Record)
BuildRequires: perl(Cwd)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Path)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(IO::String)
BuildRequires: perl(IO::Uncompress::Gunzip)
BuildRequires: perl(IO::Uncompress::Bunzip2)
BuildRequires: perl(Module::Build)
BuildRequires: perl(TAP::Formatter::HTML)
BuildRequires: perl(TAP::Harness)
BuildRequires: perl(TAP::Harness::Archive)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::More)
BuildRequires: perl(Sub::Uplevel)
BuildRequires: perl(Sys::Virt) >= 0.2.1
BuildRequires: perl(XML::Twig)
BuildRequires: perl(XML::Writer)
BuildRequires: perl(XML::XPath)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
# RPM autoprovides misses these 3
Requires: perl(Test::Exception)
Requires: perl(TAP::Formatter::HTML)
Requires: perl(TAP::Harness::Archive)
# Want to force this minimal version, so don't rely on RPM autoprov
Requires: perl(Sys::Virt) >= 0.2.1
BuildArchitectures: noarch

%description
Sys::Virt::TCK provides an integration test suite for validating
correct operation of libvirt drivers with underlying virtualization
technology.

%prep
%setup -q -n %{appname}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0 \
  --install_path conf=%{_sysconfdir}/libvirt-tck \
  --install_path pkgdata=%{_datadir}/libvirt-tck/tests

find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%__install -m 0755 -d $RPM_BUILD_ROOT%{_localstatedir}/cache/libvirt-tck

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
#%doc AUTHORS
%doc LICENSE
%doc README
#%doc INSTALL
%dir %{_sysconfdir}/libvirt-tck
%config(noreplace) %{_sysconfdir}/libvirt-tck/default.cfg
%{_bindir}/libvirt-tck
%dir %{_datadir}/libvirt-tck
%{_datadir}/libvirt-tck/*
%{perlvendorman1}/*
#%{perlvendorman3}/*
%{perlvendorlib}/Sys/Virt/TCK.pm
%{perlvendorlib}/Sys/Virt/TCK/
%dir %{_localstatedir}/cache/libvirt-tck

%changelog
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.1.0-8
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.1.0-7
- Mass rebuild with perl-5.12.0

* Wed Aug 26 2009 Daniel P. Berrange <berrange@redhat.com> - 0.1.0-6
- Skip over Xen dom0 domains
- Use PAE kernel for i686 by default so it works with Xen
- Re-enable cloning test now newer Sys-Virt exists in rawhide

* Wed Aug  5 2009 Daniel P. Berrange <berrange@redhat.com> - 0.1.0-5
- Add missing perl-Test-Exception dep
- Skip cleanup if sanity check fails

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Daniel P. Berrange <berrange@redhat.com> - 0.1.0-3
- Add disttag, remove extrarelease, add Perl module compat, add missing BRs

* Wed Jul 22 2009 Daniel P. Berrange <berrange@redhat.com> - 0.1.0-2
- Fix license field

* Wed Jul 22 2009 Daniel P. Berrange <berrange@redhat.com> - 0.1.0-1
- Initial build
