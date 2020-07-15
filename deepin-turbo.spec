%bcond_with check



######deepin-turbo-0.0.3.orig.tar.xz

Name:          deepin-turbo
Version:       0.0.3
Release:       1
Summary:       deepin-trubo is a deepin project that derives from Applauncherd.

License:       GPLv3
URL:           https://uos-packages.deepin.com/uos/pool/main/d/deepin-turbo/
Source0:       %{name}-%{version}.orig.tar.xz

BuildRequires: cmake
BuildRequires: qt5-qtbase-devel
BuildRequires: dbus-devel
BuildRequires: systemd-devel

%description
deepin-trubo is a deepin project that derives from Applauncherd.

%package devel
Summary:    %{summary}
%description devel

%prep
%setup

%build
cmake .
make

%install
%make_install
mkdir -p %{?buildroot}%{_libdir}
mkdir -p %{?buildroot}%{_bindir}
mkdir -p %{?buildroot}%{_includedir}
mv %{?buildroot}/usr/local/lib/* %{?buildroot}%{_libdir}/
mv %{?buildroot}/usr/local/bin/* %{?buildroot}%{_bindir}/
mv %{?buildroot}/usr/local/include/%{name}/ %{?buildroot}%{_includedir}/

%files
%{_libdir}/*.so
%{_bindir}/*
/usr/lib/systemd/user/deepin-turbo-booster-dtkwidget.service
%{_libdir}/deepin-turbo/booster-dtkwidget
%doc README.md

%files devel
%{_libdir}/*.so
%{_bindir}/*
%{_includedir}/*
%doc README.md


%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.22.2-9
- Switch to %%ldconfig_scriptlets

* Wed Nov 22 2017 Troy Dawson <tdawson@redhat.com> - 1.22.2-8
- Fix spec file conditionals

* Thu Sep 28 2017 mosquito <sensor.wen@gmail.com> - 1.22.2-7
- Add GL_ARB_shader_texture_lod and copy_sub_image support (#1421055)
- Add pkgconfig(egl) BReq for rawhide
- Move BReqs to pkgconfig

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 17 2017 Owen Taylor <otaylor@redhat.com> - 1.22.2-4
- Add Requires: %%{name} = %%{version}-%%{release} to the tests subpackage

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 11 2016 Adam Jackson <ajax@redhat.com> - 1.22.2-2
- Prefer eglGetPlatformDisplay to eglGetDisplay

* Fri Aug 26 2016 Kalev Lember <klember@redhat.com> - 1.22.2-1
- Update to 1.22.2
- Don't set group tags

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 21 2015 Ray Strode <rstrode@redhat.com> 1.22.0-2
- Fix black login screen
  Resolves: #1272737

* Wed Sep 16 2015 Kalev Lember <klember@redhat.com> - 1.22.0-1
- Update to 1.22.0

* Fri Aug 21 2015 Kalev Lember <klember@redhat.com> - 1.21.2-2
- Re-enable parallel make

* Fri Aug 21 2015 Kalev Lember <klember@redhat.com> - 1.21.2-1
- Update to 1.21.2
- Use make_install macro
- Mark COPYING as %%license
- Drop large ChangeLog file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Ray Strode <rstrode@redhat.com> 1.20.0-3
- Update to upstreamed version of mgag200 fix

* Wed Mar 11 2015 Ray Strode <rstrode@redhat.com> 1.20.0-2
- Try to fix wayland on mgag200

* Mon Feb 23 2015 Kalev Lember <kalevlember@gmail.com> - 1.20.0-1
- Update to 1.20.0

* Tue Jan 20 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.18.2-10
- Enable tests subpackage (rhbz 1163429)

* Sun Nov 16 2014 Kalev Lember <kalevlember@gmail.com> - 1.18.2-9
- Obsolete compat-cogl116 from rhughes-f20-gnome-3-12 copr

* Thu Nov 13 2014 Kalev Lember <kalevlember@gmail.com> - 1.18.2-8
- Disable cogl-gst as long as we don't have clutter-gst3 (#1158676)

* Sat Nov 01 2014 Richard Hughes <rhughes@redhat.com> - 1.18.2-7
- Fix compile on RHEL, harder

* Mon Oct 27 2014 Richard Hughes <rhughes@redhat.com> - 1.18.2-6
- Fix compile on RHEL

* Fri Aug 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.18.2-5
- Remove lib64 rpaths (#1132876)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.18.2-3
- Rebuilt for gobject-introspection 1.41.4

* Fri Jul 11 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.18.2-2
- Run make check but don't fail build on it

* Fri Jul 04 2014 Kalev Lember <kalevlember@gmail.com> - 1.18.2-1
- Update to 1.18.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Kalev Lember <kalevlember@gmail.com> - 1.18.0-3
- Backport an upstream fix for a totem crash

* Thu May 08 2014 Adam Jackson <ajax@redhat.com>
- Add optional installed-tests subpackage

* Mon Apr 28 2014 Richard Hughes <rhughes@redhat.com> - 1.18.0-2
- Build with --enable-cogl-gst

* Fri Mar 21 2014 Kalev Lember <kalevlember@gmail.com> - 1.18.0-1
- Update to 1.18.0

* Fri Mar 21 2014 Kalev Lember <kalevlember@gmail.com> - 1.17.5-1.gitbb10532
- Update to 1.17.5 git snapshot

* Fri Feb 21 2014 Kalev Lember <kalevlember@gmail.com> - 1.17.4-2
- Drop compat-libcogl19

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 1.17.4-1
- Update to 1.17.4, which includes soname bump
- Build a temporary compat-libcogl19 subpackage to ease the rebuilds

* Wed Feb 05 2014 Richard Hughes <rhughes@redhat.com> - 1.17.2-1
- Update to 1.17.2

* Tue Jan 21 2014 Richard Hughes <rhughes@redhat.com> - 1.16.2-1
- Update to 1.16.2

* Wed Sep 25 2013 Dan Horák <dan[at]danny.cz> - 1.16.0-2
- fix build on big endians (#1011893)

* Tue Sep 24 2013 Kalev Lember <kalevlember@gmail.com> - 1.16.0-1
- Update to 1.16.0

* Thu Sep 12 2013 Kalev Lember <kalevlember@gmail.com> - 1.15.10-3
- More configure options for enabling the gnome-shell Wayland compositor
- Enable parallel build

* Tue Sep 10 2013 Matthias Clasen <mclasen@redhat.com> - 1.15.10-2
- Add configure options that are needed to enable the gnome-shell
  Wayland compositor

* Mon Sep 02 2013 Kalev Lember <kalevlember@gmail.com> - 1.15.10-1
- Update to 1.15.10

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 1.15.8-1
- Update to 1.15.8

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 1.15.4-1
- Update to 1.15.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Kalev Lember <kalevlember@gmail.com> 1.14.0-3
- Rebuilt

* Wed May 22 2013 Adam Jackson <ajax@redhat.com> 1.14.0-2
- cogl-1.14.0-21-ge26464f.patch: Sync with 1.14 branch for a crash fix.

* Mon Mar 25 2013 Kalev Lember <kalevlember@gmail.com> 1.14.0-1
- Update to 1.14.0

* Wed Mar 13 2013 Matthias Clasen <mclasen@redhat.com> 1.13.4-2
- Enable wayland backend

* Thu Feb 21 2013 Bastien Nocera <bnocera@redhat.com> 1.13.4-1
- Update to 1.13.4

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.13.2-1
- Update to 1.13.2

* Mon Jan  7 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.12.2-1
- Update to 1.12.2

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 1.12.0-1
- Update to 1.12.0

* Tue Sep 18 2012 Kalev Lember <kalevlember@gmail.com> - 1.11.6-1
- Update to 1.11.6
- Drop upstreamed cogl-1.11.4-mesa-strings.patch

* Mon Sep 17 2012 Adam Jackson <ajax@redhat.com> 1.11.4-2
- cogl-1.11.4-mesa-strings.patch: Update match strings for Mesa.

* Mon Sep  3 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.11.4-1
- Update to 1.11.4

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 1.11.2-1
- Update to 1.11.2

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Kalev Lember <kalevlember@gmail.com> - 1.10.4-1
- Update to 1.10.4
- Dropped no-framebuffer-blit patch which is included in the release

* Thu Apr 19 2012 Adel Gadllah <adel.gadllah@gmail.com> - 1.10.2-1
- Update to 1.10.2

* Tue Mar 20 2012 Kalev Lember <kalevlember@gmail.com> - 1.10.0-1
- Update to 1.10.0

* Sat Mar 10 2012 Matthias Clasen <mclasen@redhat.com> - 1.9.8-1
- Update to 1.9.8

* Sat Feb 25 2012 Matthias Clasen <mclasen@redhat.com> - 1.9.6-1
- Update to 1.9.6

* Tue Jan 17 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.9.4-1
- Update to 1.9.4
- http://ftp.gnome.org/pub/GNOME/sources/cogl/1.9/cogl-1.9.4.news

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Matthias Clasen <mclasen@redhat.com> 1.9.2-1
- Update to 1.9.2

* Thu Nov 03 2011 Adam Jackson <ajax@redhat.com> 1.8.2-4
- cogl-1.8.2-lp-no-framebuffer-blit.patch: Disable the subbuffer blit code
  when running on llvmpipe until it's unbroken.

* Tue Nov 01 2011 Adam Jackson <ajax@redhat.com> 1.8.2-3
- cogl-1.8.2-no-drm-hax.patch: Don't try insane direct DRM vblank wait.

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for glibc bug#747377

* Mon Oct 17 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.8.2-1
- 1.8.2 stable release
- http://ftp.gnome.org/pub/GNOME/sources/cogl/1.8/cogl-1.8.2.news
- Enable gdk-pixbuf2 support - Fixes RHBZ # 738092

* Mon Sep 19 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.8.0-1
- 1.8.0 stable release
- http://ftp.gnome.org/pub/GNOME/sources/cogl/1.8/cogl-1.8.0.news

* Mon Sep  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.8-1
- Update to 1.7.8

* Thu Aug 18 2011 Matthias Clasen <mclasen@redhat.com> - 1.7.6-1
- Update to 1.7.6

* Tue Jul 26 2011 Matthias Clasen <mclasen@redhat.com> - 1.7.4-1
- Update to 1.7.4

* Mon Jul  4 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2

* Thu Jun 16 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.0-3
- Update spec for review feedback

* Thu Jun 16 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.0-2
- Update spec for review feedback

* Wed Jun 15 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.0-1
- Initial Package
