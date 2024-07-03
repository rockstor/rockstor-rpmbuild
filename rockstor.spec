Name: rockstor
Version: 5.0.11
Release: 0
Summary: Btrfs Network Attached Storage (NAS) Appliance.
Group: Productivity/Networking/File-Sharing

%define jslibs_version 5.0.11
# Enable source fetch - when default disabled, source dir is /usr/src/packages/SOURCES
%undefine _disable_source_fetch

# https://fedoraproject.org/wiki/Packaging:LicensingGuidelines#Multiple_Licensing_Scenarios
# Source0: (rockstor-core) is GPL-3.0-or-later, Source1: (rockstor-jslibs) has mixed licensing:
License: GPL-3.0-or-later AND (MIT AND Apache-2.0 AND GPL-3.0-or-later AND LGPL-3.0-or-later AND ISC)
URL: https://rockstor.com/
Vendor: YewTreeApps
AutoReqProv: no  #  Turn off automatic dependency processing.
# https://github.com/rockstor/rockstor-core
# https://github.com/rockstor/rockstor-core/archive/refs/tags/4.5.4-0.tar.gz
# Create equivalent of GitHub archive tar.gz locally via:
# mv /opt/rockstor /opt/rockstor-core-4.5.4-0
# tar czf /usr/src/packages/SOURCES/4.5.4-0.tar.gz --directory=/opt rockstor-core-4.5.4-0
# With _disable_source_fetch (default) Sourc* lines use /usr/src/packages/SOURCES/
# i.e. url part will then be ignored.
Source0: https://github.com/rockstor/rockstor-core/archive/refs/tags/%{version}-%{release}.tar.gz
# Patch1: https://github.com/rockstor/rockstor-core/pull/2434.patch
# https://github.com/rockstor/rockstor-jslibs
# GitHub versioned archive has top directory of e.g.: rockstor-jslibs-4.5.2
# N.B. our file names are almost clashing here, rockstor-core has -release.
# rpmbuild downloads these very similarly named tar.gz files and stashes then in the same dir!
# wget -O /usr/src/packages/SOURCES/4.5.4.tar.gz https://github.com/rockstor/rockstor-jslibs/archive/refs/tags/4.5.4.tar.gz
Source1: https://github.com/rockstor/rockstor-jslibs/archive/refs/tags/%{jslibs_version}.tar.gz

Prefix: /opt
# The following (BuildRoot) is available in scriptlets as {buildroot}
# which is in-turn exported as a shell variable of RPM_BUILD_ROOT
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-build

# Generic build requirements: % check requires a Poetry built venv.
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
BuildRequires: git
BuildRequires: dbus-1-devel
BuildRequires: glib2-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: postgresql13
BuildRequires: postgresql13-server
BuildRequires: postgresql13-server-devel
BuildRequires: password-store
# Notes re Poetry for future consideration:
# https://en.opensuse.org/openSUSE:Build_system_recipes#PEP517_style:
# https://github.com/openSUSE/python-rpm-macros/blob/79041e9986dd5427d0bc1f66936092ddfe04533b/README.md#install-macros
# BuildRequires: python-rpm-macros
# BuildRequires: poetry-core

################
# SuSE, openSUSE
################
# https://en.opensuse.org/openSUSE:Packaging_for_Leap#RPM_Distro_Version_Macros
# "suse_version 1500 for the full time life of SLE15 and openSUSE:Leap:15.x"
# https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto

# openSUSE Leap 15.0/15.1/15.2/15.3/15.4/15.5
%if 0%{?suse_version} == 1500
BuildRequires: python311
BuildRequires: python311-devel
BuildRequires: python311-pipx
Requires: python311
Requires: python311-devel
Requires: python311-pipx
Requires: NetworkManager
Requires: nginx
Requires: btrfsprogs
Requires: nfs-kernel-server
Requires: nfs-client
Requires: samba
Requires: samba-winbind
Requires: ypbind
Requires: rpcbind
Requires: realmd
Requires: realmd-lang
Requires: krb5-client
Requires: ntp
Requires: at
Requires: chrony
Requires: systemtap-runtime
Requires: firewalld
Requires: postgresql13
Requires: postgresql13-server
Requires: postgresql13-server-devel
Requires: postgresql13-contrib
Requires: rsync
Requires: smartmontools
Requires: hdparm
Requires: postfix
Requires: cyrus-sasl-plain
Requires: nano
Requires: nut
Requires: nut-drivers-net
Requires: net-snmp
Requires: docker
Requires: cryptsetup
Requires: dnf-yum
Requires: dnf-plugins-core
Requires: python3-python-dateutil
Requires: which
Requires: shellinabox
Requires: avahi
Requires: cronie
Requires: sssd
Requires: sssd-tools
Requires: sssd-ad
Requires: sssd-ldap
Requires: sssd-dbus
Requires: dmraid
Requires: libzmq5
Requires: dbus-1-devel
Requires: glib2-devel
Requires: haveged
Requires: gcc
Requires: gcc-c++
Requires: make
Requires: password-store
%endif

# TUMBLEWEED
# Tumbleweed as of Nov 2022:
# Version unreliable as changes over time !
%if 0%{?suse_version} >= 1599
BuildRequires: python311
BuildRequires: python311-devel
BuildRequires: python311-pipx
Requires: python311
Requires: python311-devel
Requires: python311-pipx
Requires: NetworkManager
Requires: nginx
Requires: btrfsprogs
Requires: nfs-kernel-server
Requires: nfs-client
Requires: samba
Requires: samba-winbind
Requires: ypbind
Requires: rpcbind
Requires: realmd
Requires: realmd-lang
Requires: krb5-client
Requires: ntp
Requires: at
Requires: chrony
Requires: systemtap-runtime
Requires: firewalld
Requires: postgresql13
Requires: postgresql13-server
Requires: postgresql13-server-devel
Requires: postgresql13-contrib
Requires: rsync
Requires: smartmontools
Requires: hdparm
Requires: postfix
Requires: cyrus-sasl-plain
Requires: nano
Requires: nut
Requires: nut-drivers-net
Requires: net-snmp
Requires: docker
Requires: cryptsetup
Requires: dnf-yum
Requires: dnf-plugins-core
Requires: python3-python-dateutil
Requires: which
Requires: shellinabox
Requires: avahi
Requires: cronie
Requires: sssd
Requires: sssd-tools
Requires: sssd-ad
Requires: sssd-ldap
Requires: sssd-dbus
Requires: dmraid
Requires: libzmq5
Requires: dbus-1-devel
Requires: glib2-devel
Requires: haveged
Requires: gcc
Requires: gcc-c++
Requires: make
Requires: password-store
%endif

# rpm build notes (from man rpmbuild):
# "-ba Build binary and source packages (after doing the %prep, %build, and %install stages)."
# rpmbuild -ba --nobuild --define "_sourcedir /opt/rockstor/dist/" --define "_specdir SPECS" -ba SPECS/rockstor.spec
# Default source directory: /usr/src/packages/SOURCES
# rpmbuild -ba -v rockstor.spec
# built rpms can be installed directly via (depending on arch and version):
# zypper --no-gpg-checks in /usr/src/packages/RPMS/x86_64/rockstor-4.5.2-0.x86_64.rpm

%description
Software raid, snapshot capable NAS solution with built-in file integrity protection.
Allows for file sharing between network attached devices.

%prep
# Macro to unpack "Source0:" (Defined in header)
# and cd into the named (-n) tar top-level directory.
# GitHub release archive.tar.gz has eg rockstor-core-4.5.2-0 (reponame-tag)
# -S git use git to manage changes.
# -T avoid unpacking Source0 twice.
# -b 0 Source0:
# -n tar top-level directory name.
# autosetup also applies all patches (if any) in order.
%autosetup -S git -T -b 0 -n %{name}-core-%{version}-%{release}
# Unpack our jslibs (removing it's top directory) into jslibs/js of %{source}
# Make expected extra jslibs location in above source directory
mkdir -p jslibs/js/lib
# our GitHub archive has a containing top directory, strip this off.
tar zxvf %{SOURCE1} --directory jslibs/js/lib --strip-components=1
# PLACE COPY OF JSLIBS TAR.GZ INTO SOURCE ROOT
# Include rockstor-jslibs.tar.gz used in rpm check, and to be re-used during rpm install post scriptlet.
# renamed from GitHub archive Source1 "4.5.2.tar.gz" to rockstor-jslibs.tar.gz for sdist inclusion
# and reuse by build.sh
cp %{SOURCE1} rockstor-jslibs.tar.gz
# generate accompanying sha256 file:
sha256sum rockstor-jslibs.tar.gz > rockstor-jslibs.tar.gz.sha256sum

%build
# Defaults to e.g. '/usr/src/packages/BUILD/rockstor-core-4.5.2-0/
echo "'build' scriptlet PATH=${PATH}"
# Poetry install assumed, as per rockstor-build.service / build.sh.
# Create our poetry source distribution in ./dist/rockstor-4.5.2.tar.gz
poetry build --format sdist
# N.B. above build installs minimal .venv (via poetry.toml) of around 12 MB.
# see contents via: tar tvf ./dist/rockstor-4.5.2.tar.gz
# which shows top embedded directory of "rockstor-4.5.2"

%install
# cwd example: /usr/src/packages/BUILD/rockstor-core-4.5.2-0/, i.e. as per build.
# Current directory will be top level of source, post build. {build}
# Target directory to build our file tree in is {buildroot}
# Must not attempt any chown as rpmbuild is normally run as un-unprivileged user.
# Unpack Poetry created sdist tar.gz into our proposed new location.
install -d -m 0755 %{buildroot}%{prefix}/rockstor
# N.B. sdist tar.gz does not contain 'static' or '.venv' top level directories:
# these will be regenerated post install
tar zxvf ./dist/%{name}-%{version}.tar.gz --directory %{buildroot}%{prefix}/rockstor --strip-components=1
# ADD MISSING opt/rockstor/var/log
# var/log/rockstor_systems_log_dir is included in poetry dist tar.gz
# but when run in rpmbuild build scriptlet environment it is somehow missing.
# Revisit after updating poetry, i.e. once no longer Python 2.7 tethered.
mkdir -p %{buildroot}%{prefix}/rockstor/var/log
touch %{buildroot}%{prefix}/rockstor/var/log/rockstor_systems_log_dir
# SYSTEMD FILE INSTANTIATION
# See: https://en.opensuse.org/openSUSE:Systemd_packaging_guidelines#Unit_files
# _unitdir normally resolves to: /usr/lib/systemd/system
# N.B. we could run a sed here on all our service files to honour prefix.
# Main rocksor* service files.
install -D -m 644 ./conf/rockstor-build.service %{buildroot}%{_unitdir}/%{name}-build.service
install -D -m 644 ./conf/rockstor-pre.service %{buildroot}%{_unitdir}/%{name}-pre.service
install -D -m 644 ./conf/rockstor.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 ./conf/rockstor-bootstrap.service %{buildroot}%{_unitdir}/%{name}-bootstrap.service
# nginx override file
mkdir -p %{buildroot}/etc/systemd/system/nginx.service.d
install -m 644 ./conf/30-rockstor-nginx-override.conf %{buildroot}/etc/systemd/system/nginx.service.d/30-%{name}-nginx-override.conf

%check
# Run tests from inside build directory.
echo "'check' scriptlet PATH=${PATH}"
# Build full project .venv (via poetry.config) - installing all dependencies: 140 MB
env > poetry-install.txt
poetry --version >> poetry-install.txt
# /usr/local/bin/poetry -> /opt/pipx/venvs/poetry
poetry install -vvv --no-interaction --no-ansi >> poetry-install.txt 2>&1

# GNUPG & 'pass' setup assumed, as per rockstor-build.service / build.sh,
# with re-assertion, and key rotation via rockstor-pre.service.
export Environment="PASSWORD_STORE_DIR=/root/.password-store"
export DJANGO_SETTINGS_MODULE=settings
poetry run django-admin collectstatic --no-input --verbosity 1
cd src/rockstor/
poetry run django-admin test

%files
# Define what files shall be owned by the resulting rpm.
# Establish any special file ownership in this section.
# N.B. take care with entire directory entries.
# We don't want to end up owning all other files in that directory.
%defattr(-, root, root)
# e.g. collected from /usr/src/packages/BUILDROOT/rockstor-4.5.2-0.x86_64
/opt/%{name}
# enable owner (root) execute on ./build.sh & ./src/rockstor/scripts/db_upgrade.sh
# TODO: "warning: File listed twice: /opt/rockstor/build.sh"
%attr(744, root, root) /opt/%{name}/build.sh
%attr(744, root, root) /opt/%{name}/src/rockstor/scripts/db_upgrade.sh
# all rockstro* service files from buildroot
%{_unitdir}/%{name}*
# Our nginx override dir and all contents:
/etc/systemd/system/nginx.service.d/30-%{name}-nginx-override.conf
# The rockstor-core README.md details the overall package license,
# along with the included and referenced repositories.
# For a breakdown of the licensing, see License: in README.md
%license /opt/%{name}/README.md
# % license /opt/% {name}/jslibs/js/lib/README.md


# N.B. Package update runs
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#ordering
# view installed package scriptlets via: "rpm -q --scripts rockstor"
#
#- %pretrans of new version (Lua only)
#- %pre of new version
# New package installed.
#- %post of new version
#
#- %preun of old version
# Old package uninstalled
#- %postun of old version
#- %posttrans of new package

%pre
# Before install/update (run from new/incoming package version)
# $1 == 1 is before an install
# $1 == 2 is before an update
#
# Stop all main rockstor services, irrespective of origin.
/usr/bin/systemctl stop rockstor-bootstrap.service rockstor.service rockstor-pre.service rockstor-build.service
#
# Backup all static/config-backups contents; to be restored in posttrans scriptlet.
if [ -d "%{prefix}/%{name}/static/config-backups" ]
then
    echo "Copying contents of static/config-backups to config-backups-rpmsave."
    [ ! -d "%{prefix}/%{name}/config-backups-rpmsave" ] && mkdir %{prefix}/%{name}/config-backups-rpmsave
    cp --preserve=all %{prefix}/%{name}/static/config-backups/* %{prefix}/%{name}/config-backups-rpmsave
else
    echo "No static/config-backups directory found."
fi
#
# remove all pyc files (Python interpreter generated)
find %{prefix}/%{name}/src -name '*.pyc' -delete
# Before we install, remove non-packaged rockstor legacy/development files:
rm --force /etc/systemd/system/rockstor*
systemctl daemon-reload
# remove legacy bin develop-eggs & eggs directories
rm --force --recursive %{prefix}/%{name}/bin
rm --force --recursive %{prefix}/%{name}/develop-eggs
rm --force --recursive %{prefix}/%{name}/eggs
# https://en.opensuse.org/openSUSE:Systemd_packaging_guidelines#Unit_files
# See: /usr/lib/rpm/macros.d/macros.systemd from systemd-rpm-macros
# rpm --eval macro-name-here
%service_add_pre rockstor-build.service rockstor-pre.service rockstor.service rockstor-bootstrap.service
exit 0

%post
# After install/update (run from new/incoming package version)
# $1 == 1 is after an install
# $1 == 2 is after an update
#
if [ "$1" = "2" ]; then  # update
    # Remove jslibs dir so build.sh (posttrans) will refresh from new rpm rockstor-jslibs.tar.gz
    rm -rf %{prefix}/%{name}/jslibs
    # Remove collectstatic generated static dir as build.sh (posttrans) will regenerate.
    rm -rf %{prefix}/%{name}/static
    # Remove our prior versions .venv dir as build.sh (posttrans) will regenerate.
    rm -rf %{prefix}/%{name}/.venv
fi
# Enforce, via manual alternatives configuration, our target postgresql & pipx versions.
# We do this on install & update to avoid base OS defaults exceeding our compatibility.
# Compatibility concerns:
# - Postgresql: Django's secondary dependency of psycopg which we pin.
# - Pipx: We install and manage Poetry via OS supplied python3.##-pipx packages.
update-alternatives --set postgresql /usr/lib/postgresql13
update-alternatives --set pipx /usr/bin/pipx-3.11
# enable/disable our units by default on package installation,
# enforcing distribution, spin or administrator preset policy.
# See: https://build.opensuse.org/package/show/home:rockstor:branches:Base:System/systemd-presets-branding-rockstor
%service_add_post rockstor-build.service rockstor-pre.service rockstor.service rockstor-bootstrap.service
exit 0

%preun
# Before uninstall/update (run from old/outgoing package version)
# $1 == 0 is before an uninstall
# $1 == 1 is before an update
#
# If uninstall, the following service macro disables and stops our services.
%service_del_preun rockstor-build.service rockstor-pre.service rockstor.service rockstor-bootstrap.service
exit 0

%postun
# After uninstall/update (run from old/outgoing package version)
# $1 == 0 is after an uninstall
# $1 == 1 is after an update
#
# During package update, % service_del_postun restarts units.

# If units are not to be restarted, use % service_del_postun_without_restart
# On uninstall the following service macro deletes our services, then does a 'systemctl daemon-reload'
%service_del_postun_without_restart rockstor-build.service rockstor-pre.service rockstor.service rockstor-bootstrap.service

# Post uninstall we need to restart the nginx service as we removed our nginx override file.
if [ "$1" = "0" ]; then  # uninstall so clean up build.sh generated files and other dynamic files.
    systemctl restart nginx
    # Remove jslibs directory from rockstor-jslibs.tar.gz
    rm -rf %{prefix}/%{name}/jslibs
    # remove collectstatic generated static dir
    rm -rf %{prefix}/%{name}/static
    # remove Poetry installed .venv directory.
    rm -rf %{prefix}/%{name}/.venv
    # remove poetry-install.txt
    rm -rf %{prefix}/%{name}/poetry-install.txt
    # remove all pyc files (Python interpreter generated)
    find %{prefix}/%{name}/src -name '*.pyc' -delete
    # remove all empty directories
    find %{prefix}/%{name}/src -type d -empty -delete
    # remove Huey db file:
    rm %{prefix}/%{name}/rockstor-tasks-huey.db
    # remove top level directory but only if empty
    rmdir %{prefix}/%{name}
fi
exit 0

%posttrans
# From: https://en.opensuse.org/openSUSE:Packaging_scriptlet_snippets
# the posttrans scriptlet is available from rpm version 4.4 onwards.
#
# Last scriptlet to execute from old or new package versions.
# Executed from new package version during install & upgrade similarly.
#
# Ensure Postgres DB format is sufficiently upgraded prior to systemd services start.
# Requires matching postgresqlXX-* dependencies to target format requested.
# If a system currently uses an older DB format, the associated binaries are assumed.
# "10 13" prepares Leap 15.3 4.1.0-0 installs, dup'ed to 15.4 4.6.1-0, for > 5.0.5-0.
%{prefix}/%{name}/src/rockstor/scripts/db_upgrade.sh 10 13
#
# Restore 'pre' scriptlet's config-backup-rpmsave files to static.
if [ -d "%{prefix}/%{name}/config-backups-rpmsave" ]
then
    echo "Restoring config-backups-rpmsave contents to static/config-backups."
    [ ! -d "%{prefix}/%{name}/static/config-backups" ] && mkdir %{prefix}/%{name}/static/config-backups
    cp --preserve=all %{prefix}/%{name}/config-backups-rpmsave/* %{prefix}/%{name}/static/config-backups
else
    echo "No config-backups-rpmsave directory found."
fi
exit 0


# remove and reformat to rockstor.changes file as per:
# https://en.opensuse.org/openSUSE:Creating_a_changes_file_(RPM)
# https://github.com/openSUSE/obs-build/blob/master/changelog2spec
%changelog
* Wed Jul 03 2024 The Rockstor Project <support@rockstor.com> - 5.0.11-0
-Bump versions to a 5.0.11 base - testing branch #2859 @phillxnet 
-Routine update of dependencies #2861 @phillxnet 
-Leap 15.6: SFTP share error - library paths changed #2856 @Hooverdan96 @phillxnet @FroggyFlox  
-5.0.9-0 & 5.0.10-0 lsblk whitespace only values - not enough values to unpack #2853 @phillxnet 
* Mon Jun 17 2024 The Rockstor Project <support@rockstor.com> - 5.0.10-0
-Bump versions to a 5.0.10 base - testing branch #2848 @phillxnet 
-Routine update of dependencies #2849 @phillxnet 
-5.0.6-0 to 5.0.9-0 Configuration Backup file upload fails #2846 @Hooverdan96 @FroggyFlox @phillxnet 
* Fri Apr 19 2024 The Rockstor Project <support@rockstor.com> - 5.0.9-0
-Bump versions to a 5.0.9 base - testing branch #2837 @phillxnet @FroggyFlox 
-DRF, Django LTS, and Gunicorn maintenance updates #2820 @phillxnet @FroggyFlox 
-Un special-case system drive btrfs-in-partition treatment #2824 @phillxnet 
-Unit test improvements re Disk miss-attribution to ROOT pool #2828 @phillxnet 
-Modernise scan_disks() - no functional change intended #2826 @phillxnet 
-Adapt net interface delete to 'rockstor' service null config #2819 @phillxnet 
-Change Quota Status Display Wording #2810 @Hooverdan96 
-TypeError when deleting unused Rocknet #2814 @phillxnet @FroggyFlox 
-[t] Add Group with custom GID fails with type error #2807 @phillxnet @Hooverdan96 
-Scheduled shutdown task fails due to type issue #2805 @phillxnet @Hooverdan96 
-Replace raw_input() with input() #2803 @Hooverdan96 
* Mon Feb 12 2024 The Rockstor Project <support@rockstor.com> - 5.0.8-0
-Bump versions to a 5.0.8 base - testing branch #2800 @phillxnet 
-(t) Samba shares not accessible - 5.0.6-0 & 5.0.7-0 #2794 @phillxnet @FroggyFlox @Hooverdan96 
-Add rockstor-build systemd service #2793 @phillxnet 
* Mon Jan 29 2024 The Rockstor Project <support@rockstor.com> - 5.0.7-0
-Bump versions to a 5.0.7 base - testing branch #2791 @phillxnet 
-Failure to re-create venv - pre 5.0.3-0 updating to 5.0.6-0 rpm #2788 @phillxnet 
-Establish Postgres database format upgrade #2780 @phillxnet 
-Failure to remove legacy poetry version in 5.0.6-0 rpm #2782 @phillxnet 
* Tue Jan 16 2024 The Rockstor Project <support@rockstor.com> - 5.0.6-0
-Bump versions to a 5.0.6 base (Testing) - testing branch #2778 @phillxnet 
-(t) replication spawn error #2766 @phillxnet 
-Account for eventual double slahes in the conversion from legacy to poetry paths #2757 @FroggyFlox 
-Replication secret encrypted in Web-UI #2759 @phillxnet 
-Make explicit to systemd our NetworkManager dependency #2685 @phillxnet 
-Adopt dedicated secrets management library #2728 @phillxnet 
-Add/Update help icon linking to docs #2720 @FroggyFlox 
-Update Poetry build system & normalise on Python 3.11 #2703 @phillxnet @FroggyFlox
-update to latest psycopg 3 #2740 @phillxnet 
-Update Django to latest 4.2 LTS #2750 @phillxnet @Hooverdan96 @FroggyFlox 
-Update pyzmq dependency to latest #2746 @phillxnet 
-Update dbus python dependency to latest #2744 @phillxnet 
-Update Django-rest-framework to latest #2738 @phillxnet 
-Update Huey task queue library #2731 @phillxnet 
-Update Django to next LTS #2734 @phillxnet 
-Ease database diagnosis via local IP access configuration #2730 @phillxnet 
-Update django-oauth-toolkit #2710 @phillxnet 
-Address redundancy re database setup #2729 @phillxnet 
-SyntaxWarning: "is not" with a literal #2713 @phillxnet 
-Use regular expressions to validate tailscale hostname #2714 @FroggyFlox @Hooverdan96 
-Fix mocking insufficiencies in system.network.py #2717 @FroggyFlox 
* Thu Oct 19 2023 The Rockstor Project <support@rockstor.com> - 5.0.5-0
-Bump versions to a 5.0.5 base (Testing) - testing branch #2715 @phillxnet 
-Implement Tailscale service #2679 @FroggyFlox 
-remove django-braces dependency #2709 @phillxnet 
-Use single https session to retrieve all rock-on definitions #2707 @phillxnet 
-Update gunicorn to latest - use gthread - discrete config file #2702 @phillxnet 
-Update Requests library to latest #2704 @phillxnet 
-Update python-socketio & python-engineio to latest #2591 @phillxnet @Hooverdan96 
-Update Django REST Framework within Django version constraint #2695 @phillxnet 
-Update django-pipeline to latest #2689 @phillxnet 
-Update Python dependency to 3.9 #2691 @phillxnet 
-Provisional Django 2.2 LTS update #2625 @phillxnet 
-Add PyCharm rock-tests run config #2686 @phillxnet 
-Don't throw exception when getting supervisord service status #2681 @FroggyFlox 
* Fri Sep 15 2023 The Rockstor Project <support@rockstor.com> - 5.0.4-0
-Bump versions to a 5.0.4 base (Testing) - testing branch #2675 @phillxnet 
-Catch DBusException to not throw error on LDAP group lookup #2673 @FroggyFlox 
-Explicitly set REALM when querying workgroup #2671 @FroggyFlox 
-surface Distro Version to breadcrumb bar #2668 @Hooverdan96 
-Set `Meta.base_manager_name` on 'storageadmin.Disk' #2666 @FroggyFlox 
-Use user.is_authenticated as an attribute #2664 @FroggyFlox 
-Migrate to New Middleware style #2662 @FroggyFlox 
* Sat Aug 19 2023 The Rockstor Project <support@rockstor.com> - 5.0.3-0
-Save and Restore config back-up files during rpm update #2660 @Hooverdan96 @phillxnet @FroggyFlox 
-(t) Update django-pipeline to 1.7.0 #2646 @FroggyFlox 
-Improve rockstor.service re robustness #2657 @phillxnet 
-Improve Web-UI update re systemd service management #2651 @phillxnet 
-Enhance development ease #2653 @phillxnet 
-Web-UI update fails to recreate venv #2652 @FroggyFlox @phillxnet 
-Establish on_delete for ForeignKey re Django update #2645 @phillxnet 
-Address compression cosmetics #2640 @StephenBrown2 
-Update .gitignore with Rockstor build artifacts #2644 @StephenBrown2 
* Wed Aug 02 2023 The Rockstor Project <support@rockstor.com> - 5.0.2-0
-resolve indeterminate or inappropriate postgresql alternative conf #2632 @phillxnet 
-Add option for ZSTD compression #2618 @StephenBrown2 
-Improve OS independence re unit tests #2633 @phillxnet 
-user admin enable without password change not internal error #2635 @phillxnet 
* Mon Jul 24 2023 The Rockstor Project <support@rockstor.com> - 5.0.1-0
-venv not updating re python version change #2626 @phillxnet 
-(t) Failure to check for updates in locales other than en_US #2627 @phillxnet 
* Fri Jul 21 2023 The Rockstor Project <support@rockstor.com> - 5.0.0-0
-WARNING -- RENEWED TESTING PHASE 5.0.0-0 -- (DEVELOPERS ONLY) #2610 @phillxnet 
-Update specifics of Python version in pyproject.toml etc #2620 @phillxnet 
-Update unit tests re recent SSL Cert update changes #2611 @phillxnet 
-update use of python distro module re 1.7.0+ changes #2426 @phillxnet 
-Disposition of pytz package #2590 @phillxnet 
-SSL Certificate update doesn't reload nginx #2606 @phillxnet 
-Testing counterpart Revise Stable Updates activation re legacy shop removal #2603 @phillxnet 
-Add GitHub Action to trigger post-release updates across repositories #2600  @FroggyFlox 
-Restore config backup functionality #2569 @FroggyFlox 
-Py3.6 Update certifi, urllib3, idna #2588 @phillxnet 
-Restore Logs Manager - Logs Readers functions #2568 @FroggyFlox 
-Py3.6 Scheduled tasks import paths fix, snapshot & scub #2570 @phillxnet 
-Py3.6 test_user.py fail re string interpretation #2582 @phillxnet 
-Save network usage processed data as List object #2577 @FroggyFlox 
-Py3.6 test_shares.py & test_snapshot.py re boolean type #2580 @phillxnet 
-Py3.6 ModuleNotFoundError: 'crontabwindow', 'nfsd_calls' - tests #2578 @phillxnet 
-Py3.6 ModuleNotFoundError: No module named 'mock' - tests #2575 @phillxnet 
-Py3.6 update test_btrfs.py and use built-in mock #2571 @phillxnet 
-Preliminary python 3.6 port - development #2564 @phillxnet 
* Tue May 30 2023 Philip Guyton <philip@yewtreeapps.com> - 4.6.0-0
-Merge testing branch into master #2529 @phillxnet
-Bump versions to a 4.6.0 base (RC7) #2561 @phillxnet
-Allow delete of un-mounted/un-mountable pool #2395 @phillxnet
-Improve permissions on crontabs created by rockstor #2556 @FroggyFlox
-migrate hard wired config paths re poetry build #2540 @FroggyFlox
-Account for Tumbleweed sshd config changes #2501 @phillxnet @Hooverdan96 @FroggyFlox
-Cleanup json2.js reference #2550 @Hooverdan96
-Make rockon-delete compatible with duplicate RockOn model entries #2549 @FroggyFlox @Hooverdan96
-use cryptsetup to retrieve container uuid #2545 @phillxnet
* Sat Apr 29 2023 Philip Guyton <philip@yewtreeapps.com> - 4.5.9-1
-Update indirect greenlet dependency to latest version #2543 @phillxnet
-Bump versions to a 4.5.9 base (RC6) #2541 @phillxnet
-Replace 'SHOP' with 'OPEN COLLECTIVE' in header menu #2538 @phillxnet
-Enhance Pool size calculation re new raid levels #2525 @phillxnet
-[Active Directory] Failure to set an AD user as Samba admin_user until Rockstor service restart #2526 @FroggyFlox
-RockOn Installation: the environment form has no scrollbar when there are many vars defined #2533 @kanecko
-Add mixed raid levels #2520 @phillxnet
-improve behaviour on missing /dev/disk/by-id directory #2401 @phillxnet
-Scheduled tasks of type "Reboot" fail to run #2514 @FroggyFlox
* Tue Mar 07 2023 Philip Guyton <philip@yewtreeapps.com> - 4.5.8-0
-Bump versions to a 4.5.8 base (RC5) #2510 @phillxnet
-Convert pool ID in backup file to the one in the database #2508 @FroggyFlox
-alt arch causing false positive update available #2468 @phillxnet
-drop qgroupid in share create when quotas are disabled #2506 @Hooverdan96 @phillxnet
-Convert share ID during snapshot task restore #2355 @FroggyFlox
-Improve 'Maintenance required' advice #2394 @phillxnet
-Remove raid0 dev restriction & tidy pool dev fencing code #2385 @phillxnet
* Fri Feb 17 2023 Philip Guyton <philip@yewtreeapps.com> - 4.5.7-0
-Bump versions to a 4.5.7 base (RC4) #2496 @phillxnet
-Improve README.md re package licensing, project goals etc #2489 @phillxnet
-Web-UI update to start rockstor-bootstrap.service #2488 @phillxnet @kanecko
-Refactor scrub status parsing to enhance/enable testing #2342 @phillxnet
-Pending 'missing' case issue re btrfs fi show #2311 @phillxnet
-Move Rock-on url default definitions to runtime #2305 @FroggyFlox
* Wed Jan 25 2023 Philip Guyton <philip@yewtreeapps.com> - 4.5.6-0
-Bump versions to a 4.5.6 base (RC3) #2486 @phillxnet
-Upload rockstor config fails #2483 @kanecko @FroggyFlox
-Don't load non-json rockon config files? #2473 @kanecko @Stitch10925
-Add form validation for share selected multiple times #2064 @FroggyFlox
* Thu Jan 19 2023 Philip Guyton <philip@yewtreeapps.com> - 4.5.5-0
-Spelling typo in password reset text #2474 @slowhand93
-(t) legacy binary path in some scripts/functions #2470 @FroggyFlox @phillxnet
-(t) 4.5.4-0 Samba shares fail #2471 @FroggyFlox @phillxnet
* Sat Jan 14 2023 Philip Guyton <philip@yewtreeapps.com> - 4.5.4-0
-NGINX SSL directive should be aligned to new format #2275 @Hooverdan96 @phillxnet
-(t) WARNING - update fails - needs cli follow-up "zypper in -f rockstor" #2463 @phillxnet
-move to multi-arch repos from leap 15.4 onwards #2458 @phillxnet
-Remove now redundant rockstor-fstrim service and timer #2442 @phillxnet
-Add the fields attribute to RockOnDeviceSerializer #2457 @FroggyFlox
-Correct license anomalies in newly added pyproject.toml #2447 @phillxnet
-remove redundant cubism.v1.js - rockstor-jslibs related #2455 @phillxnet
-remove unused jquery.sparkline.min.js - rockstor-jslibs related #2453 @phillxnet
-remove redundant json2.js - rockstor-jslibs related #2451 @phillxnet
-Remove redundant jquery.flot - rockstor-jslibs related #2448 @phillxnet
-Resolve Python 3.6 Poetry issue re char \u2022: (bullet) #2445 @phillxnet
-normalise on underscore.js in setup.html & base.html #2443 @phillxnet
-source rockstor-jslibs directly from GitHub releases #2440 @phillxnet
-relocate our systemd service files #2437 @phillxnet @FroggyFlox
-Rename our nginx drop-in override systemd file #2436 @phillxnet
-Replace Buildout with Poetry #2432 @phillxnet @FroggyFlox
-Inadvertent sssd related calls in Leap 15.4 #2429 @phillxnet @FroggyFlox
-Embed and update more dependencies - removed as rpm dependencies #2424 @phillxnet
* Wed Nov 09 2022 Philip Guyton <philip@yewtreeapps.com> - 4.5.0-0
-WARNING --EARLY TESTING CHANNEL-- KNOWN BROKEN - DEVELOPERS ONLY #2362 @phillxnet
-Update psutil to the latest version #2421 @phillxnet
-Improve initrock re db setup/tune & systemd service setup #2076 @phillxnet
-(t) resolve outstanding test discrepancy #2408 @phillxnet
-(t) unknown internal balance state inferior to regular balance state #2409 @phillxnet
-(t) upgrade psycopg2 within current constrains - move to PostgreSQL 13 #2406 @phillxnet
-(t) resolve multiple leaf nodes in db migration graph #2404 @phillxnet
-(t) initrock fails to assert changes in Django launch file #2402 @phillxnet
-(t) update tests #2384 @phillxnet @FroggyFlox
-Add balance status reporting for cli initiated balance operations #2393 @phillxnet
-API http post on balance status fails serialisation #2396 @phillxnet
-Scrub UI - Integer Out of Range #2397 @Hooverdan96
-Abstract pool balance command construction #2390 @phillxnet
-Improve disk removal error message formatting re pool free space #2388 @phillxnet
-(t) avoid recalculating pool free #2386 @phillxnet
-(t) Test fixtures non functional #2382 @FroggyFlox
-(t) request.DATA NotImplementedError #2379 @phillxnet
-(t) Services, Replication-Send_Receive, and Tasks pages fail #2370 @FroggyFlox @Hooverdan96
-Fake apply 0002_08_updates migration for oauth2_provider only if not applied #2376 @FroggyFlox
-Prevent duplicate localdomain entry in generic map #2373 @parthjoshi-pc
-(t) data-collector (Dashboard backend) fails to start #2368 @phillxnet @FroggyFlox
-(t) 'true' value must be either True or False." in network.py #2366 @phillxnet
-Update Django within current Python 2 constrains #2254 @phillxnet @FroggyFlox @Hooverdan96
-Increase minimum disk size to 5GiB and define at run-time #2308 @phillxnet
* Mon Jan 10 2022 Philip Guyton <philip@yewtreeapps.com> - 4.1.0-0
-Remove neglected/redundant AUTHORS file #2328 @phillxnet
-Reject null serial disk entries from database #2344 @phillxnet
-Centralise device serial rejection system #2330 @phillxnet
-Sender issues re notification emails #2339 @phillxnet
-Postfix hash format is deprecated in Leap 15.3 #2324 @phillxnet @FroggyFlox
-Mock ifp_get_groupname() instead of grp.getgrid() #2327 @FroggyFlox
-Refactor restore_service() logic to assume the service is OFF #2334 @FroggyFlox
-initrock via rockstor-pre fails on non-existent /etc/issue #2335 @phillxnet
-NUT timed shutdown has file path bug #2331 @phillxnet
-Remove special treatment for the deprecated discourse rock-on #2033 @phillxnet
-Remove coverage library as unused and now requires Python 3 #2325 @phillxnet @FroggyFlox
* Sun Sep 26 2021 Philip Guyton <philip@yewtreeapps.com> - 4.0.9-0
-Add another JMS567 controller serial obfuscation detection #2318 @azilber @phillxnet
-Logs Archive 'Click to download' link broken #2317 @harryhuk @phillxnet
-Replace Yum logs with Zypper history in Logs Manager #2314 @Hooverdan96 @FroggyFlox
* Tue Aug 17 2021 Philip Guyton <philip@yewtreeapps.com> - 4.0.8-0
-Re-enable IPv6 at kernel level (Reboot Required) #2309 @phillxnet
-rpm_build_info: 'rockstor' hardcoded in error #2306 @chrstphrchvz
-Change rock-ons default url to https #2304 @korg
* Sun May 09 2021 Philip Guyton <philip@yewtreeapps.com> - 4.0.7-0
-Fake Product UUID Case Sensitivity Incorrect on Rockstor 4 #2290 @phillxnet
-Fetch Group management setting and add it to payload #2294 @FroggyFlox
-Retrieve dmesg logs using journald #2281 @FroggyFlox
* Mon Mar 08 2021 Philip Guyton <philip@yewtreeapps.com> - 4.0.6-0
-Replace orphaned django-ztask with Huey #2276 @phillxnet
-Retrieve remote groups information using SSSD InfoPipe #2240 @FroggyFlox
-Implement automatic Samba workgroup configuration from AD server #2241 @FroggyFlox
-Update link to rock-on networking section of documentation #2263 @FroggyFlox
-repeated log errors on disabled quotas #2236 @phillxnet
-Add system-wide subvol exclusion mechanism #2223 @phillxnet
-Fix forum title encoding re auto support topic creation link #2150 @phillxnet
-Specify --lines=0 when running systemctl status #2267 @chrstphrchvz
-Remove donate menu item and update legacy paypal mechanism #2260 @phillxnet
-Fix spelling of systemctl in code comments #2266 @chrstphrchvz
-Fix detection of rock-on host networking #2242 @FroggyFlox
-Update Readme.md and add paypal.me donate link #2250 @phillxnet @StephenBrown2
-Deprecate update_rockons routine from data_collector.py #2255 @FroggyFlox
-Improve handling of rock-on-related functions when Rock-ons service is OFF #2239 @FroggyFlox
-remove legacy kernel version maintenance #2246 @phillxnet
-Correct typo in field label #2244 @FroggyFlox
-Unit test maintenance re legacy disparity. #2243 @phillxnet
* Sat Jan 02 2021 Philip Guyton <philip@yewtreeapps.com> - 4.0.5-0
-Implement SSSD-based enrollment into Active Directory or LDAP domains. Fixes #2235 @FroggyFlox
-Implement docker networks. Fixes #1982 @FroggyFlox
* Sun Oct 18 2020 Philip Guyton <philip@yewtreeapps.com> - 4.0.4-0
-Stable updates regression Rockstor 4 release candidate. Fixes #2227 @phillxnet @FroggyFlox
* Fri Oct 09 2020 Philip Guyton <philip@yewtreeapps.com> - 4.0.3-0
-minor optimisation of smb share add - "Admin user" option. Fixes #2220 @phillxnet
-remove redundant chkconfig use. Fixes #1986 @phillxnet
-NIS regression re Rockstor 4 release candidates. Fixes #2216 @phillxnet
* Mon Sep 14 2020 Philip Guyton <philip@yewtreeapps.com> - 4.0.2-0
-[NG] - Authorized_keys doesn't allow public key ssh login. Fixes #2212 @phillxnet
-9000 user limit within NIS breaks Web-UI for larger user sets. Fixes #2211 @phillxnet
* Sun Aug 02 2020 Philip Guyton <philip@yewtreeapps.com> - 4.0.1-0
-Project-wide Black formatting. Fixes #2195 @FroggyFlox
* Sun Jul 19 2020 Philip Guyton <philip@yewtreeapps.com> - 4.0.0-0
-hide non functional auto update button until post re-launch fix. Fixes #2196 @phillxnet
-avoid referencing incompatible subdir by-id device names. Fixes #2126 @phillxnet
-add recognition of system disk & pool when on SD or MicroSD card. Fixes #2192 @phillxnet
* Thu Jun 25 2020 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-60
-add architecture aware repo configuration. Fixes #2188 @phillxnet
-add arm64-efi system pool subvol exclusion. Fixes #2186 @phillxnet
-failure to remove detached disks via pool resize. Fixes #2099 @phillxnet
-ssh: use correct ld-linux for chroot on arm64. Fixes #2183 @mcbridematt
* Sun Jun 07 2020 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-59
-establish new rpm/repo/project signing key ready for relaunch. Fixes #2176 @phillxnet
-Delete 90-default.preset. Fixes #2178 @FroggyFlox
-Configure SFTP server at buildtime and update customization settings. Fixes #2168 @FroggyFlox
* Wed May 20 2020 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-58
-[NG] ROOT pool user share not displayed on page refresh. Fixes #2156 @phillxnet
-Update libraries needed for Rsync over SFTP. Fixes #2155 @FroggyFlox
-improve share rollback robustness re missing qgroup. Fixes #2171 @phillxnet
-improve pool import robustness re recently observed quota states. Fixes #2163 @phillxnet
-BTRFS SCRUB status reporting enhancements. Fixes #2162 @ubenmackin @FroggyFlox
-[openSUSE] Refer to full name of nfs-server.service. Fixes #2160 @FroggyFlox
-inadvertent use of internal -1/-1 pool quote group flag. Fixes #2158 @phillxnet
* Sun Apr 19 2020 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-57
-remark out all currently failing unit tests. Fixes #2137 @phillxnet
-improve password handling during config restore. Fixes #2151 @phillxnet
* Wed Apr 1 2020 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-56
-Deprecate Netatalk/AFP. Fixes #2146 @FroggyFlox
-update known non unique product uuids. Fixes #2143 @phillxnet
* Tue Mar 10 2020 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-55
-Enable Time Machine support via Samba. Fixes #1910 @FroggyFlox
-[openSUSE] adapt to shellinabox package differences. Fixes #2006 @phillxnet
* Mon Feb 24 2020 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-54
-Source package default smb.service in "Built on openSUSE" variants. Fixes #2127 @FroggyFlox
-[openSUSE] fix postfix config re ipv4, tlsmgr, & CA file settings. Fixes #2132 @phillxnet
* Tue Feb 11 2020 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-53
-support longer device names. Fixes #2026 @phillxnet
-Enabling samba doesn't always trigger initial configuration dialog. Fixes #2108 @defmonk0 @FroggyFlox
-Changed 'E-mail' to 'Email'. Fixes #2122 @jonpwilson
-Remove 'latest' from the Rockstor version message. Fixes #2115 @jonpwilson
-Support upload of non-gzipped files during config backup upload. Fixes #1953 @FroggyFlox
-Configure Service page corrections. Fixes #2120 @jonpwilson
-File sharing initialism inconsistencies. Fixes #2117 @jonpwilson
-Minor spelling corrections and consistency. Fixes #2116 @jonpwilson
-failure to build on Tumbleweed for master tag 3.9.2-52. Fixes #2113 @phillxnet
* Tue Jan 28 2020 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-52
-[Config Backup & Restore] Implement backup and restore of rock-ons. Fixes #2065 @FroggyFlox
-improve/add update channel/appman related text and doc links. Fixes #2106 @phillxnet
-revise donate menu item within Web-UI. Fixes #2104 @phillxnet @FroggyFlox
-pin django-braces to restore django version compatibility. Fixes #2102 @phillxnet
* Wed Dec 04 2019 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-51
-[openSUSE] replace legacy yum with dnf-yum. Fixes #2092 @phillxnet
-[openSUSE] NUT could not be configured. Fixes #2095 @phillxnet
-[openSUSE] configure docker daemon using json configuration file. Fixes #2032 #2088 @FroggyFlox
-[Config Backup/Restore] Restore Service status. Fixes #2087 @FroggyFlox
-[openSUSE] use zypper for package installs. Fixes #2071 @phillxnet
-Allow multiple versions for a docker image. Fixes #2017 @FroggyFlox
-Add support for scheduled tasks to the config backup/restore feature. Fixes #2058 @FroggyFlox
-Scheduled tasks: add feature to scan for network devices before shutting down. Fixes #2038 @p-betula-pendula
* Sun Oct 06 2019 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-50
-[openSUSE] Fix smartd config location in Rockstor-NG. Fixes #2070 @FroggyFlox
-update broken support link. Fixes #2060 @magicalyak
-pin python-engineio to 2.3.2 as recent 3.0.0 update breaks gevent. Fixes #1995 @phillxnet
* Sun Sep 22 2019 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-49
-[openSUSE] improve JeOS compatibility re ROOT label. Fixes #2062 @phillxnet
-changelog fails on version lines. Fixes #2054 @phillxnet
-Fix restore of samba share export. Fixes #2051 #2053 @FroggyFlox
-Source docker.service configuration from package in openSUSE. Fixes #2044 @FroggyFlox
-Add unit testing for core network functions. Fixes #2043 @FroggyFlox
-add known non unique product_uuid on GIADA N70E-DR. Fixes #2036 @phillxnet
-Fix ENV display in RockonInstall_summary-table. Fixes #2029 @FroggyFlox
-Fix size sorting on snapshots / shares pages. Fixes #1368 #1878 @Psykar
-honour tag element within rock-on json. Fixes #2014 @phillxnet
-pool resize disk removal unknown internal error and no UI counterpart. Fixes #1722 @phillxnet
-[openSUSE] don't rely on PGDATA env var. Fixes #2041 @phillxnet
* Sun Feb 24 2019 Philip Guyton <philip@yewtreeapps.com> - 3.9.2-48
-Skip empty label fields. Fixes #2018 @FroggyFlox
-Implement Add Labels feature for already-installed Rock-Ons. Fixes #1998 @FroggyFlox
-regression in unit tests - environment outdated since 3.9.2-46. Fixes #1993 @phillxnet
* Sun Feb 03 2019 Suman Chakravartula <suman@rockstor.com> - 3.9.2-47
-add non legacy distro aware repo configuration. Fixes #1991 @phillxnet
* Sun Feb 03 2019 Suman Chakravartula <suman@rockstor.com> - 3.9.2-46
-fix non legacy build/docker issues plus dev to rpm install mechanism. Fixes #1989 @phillxnet
* Thu Nov 15 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-44
-improve pool import with disabled or indeterminate quota state. Fixes #1987 @phillxnet
* Sat Nov 10 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-43
-regression - source build fails to fully initialise db. Fixes #1983 @phillxnet
* Thu Nov 01 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-42
-regression in dashboard disk activity widget. Fixes #1978 @phillxnet
* Fri Oct 05 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-41
-Implement a delete missing disk in pool UI #1700 @phillxnet
-As a user I'd like to replace failed drives in a RAID with new ones #737 @phillxnet
-Rockstor does not handle drive/pool errors with Grace or Recognition #1199 @phillxnet
* Tue Sep 25 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-40
-Add Support for Docker run command arguments. Fixes #1967 @FroggyFlox
* Sat Sep 22 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-39
-Add support for mounting devices to Rockons. Fixes #1957 @FroggyFlox
* Wed Sep 19 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-38
-update and fix fake product_uuid entries. Fixes #1964 @phillxnet
* Wed Sep 05 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-35
-Show warn on dashboard if errors occurs on IO or fs. Fixes #1532 @phillxnet
* Fri Aug 31 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-34
-remove grubby dependency for kernel version reporting. Fixes #1955 @phillxnet
* Fri Aug 17 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-33
-regression - nvme system disk not identified. Fixes #1951 @phillxnet
* Mon Aug 13 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-32
-add system pool auto label and enhance associated db mechanisms. Fixes #1947 @phillxnet
* Mon Jul 16 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-31
-disk serial=none or fake-serial re sda[a-z] dev names. Fixes #1925 @phillxnet
-disk serial is null #1834
* Wed Jul 11 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-30
-missing validation - megaraid custom smart option raid dev target. Fixes #1942 @phillxnet
* Tue Jul 10 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-29
-Fix Rockon unknown state due to multi-line docker inspect. Fixes #1933 @sgissi
* Thu Jun 21 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-28
-improve by-id device name retrieval. Fixes #1936 @phillxnet
* Thu Jun 14 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-27
-add root subvol exclusion mechanism. Fixes #1931 @phillxnet
* Fri Jun 01 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-26
-remove redundant rc.local cleanup. Fixes #1929 @phillxnet
* Fri Jun 01 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-25
-remove --stdin option use for passwd. Fixes #1927 @phillxnet
* Tue May 22 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-24
-improve subvol mount code robustness. Fixes #1923 @phillxnet
-check on quota updates re share rollback #1880 @phillxnet
* Mon Apr 16 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-23
-Issues with afp share name #1347 @fva-dev @phillxnet
* Mon Apr 09 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-22
-On GUI only 5000 user show up. Fixes #1915 @phillxnet
* Tue Apr 03 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-21
-Standardise error text format and move to string.format part-1. Fixes #1913 @phillxnet
-root pool edit message formatting type error #1847 @phillxnet
* Sun Mar 18 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-20
-unmounted pool with prior balance record has broken details page. Fixes #1837 @phillxnet
* Mon Mar 12 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-19
-surface pool missing disk info in UI. Fixes #1897 @phillxnet
* Sat Mar 10 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-18
-Add option to disable BTRFS quota-qgroups. Fixes #1592 #1785 @phillxnet
* Sat Mar 10 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-17
-empty compression setting on imported pools blocks extra mount options. Fixes #1896 @phillxnet
* Sun Mar 04 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-16
-inconsistent balance behaviour on single raid pool. Fixes #1894 @phillxnet
* Tue Feb 13 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-15
-allow import of ro,degraded cli mounted pool. Fixes #1890 @phillxnet
* Tue Feb 13 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-14
-deleting stale pincard holding users fails. Fixes #1891 @phillxnet
* Mon Jan 29 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.12-13
-Fix replication regression re share api change. Fixes #1853 @phillxnet
* Sun Jan 28 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-12
-remove immutable flag prior to share delete. Fixes #1882 @phillxnet
* Sat Jan 20 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-11
-fix clone auto mount on creation. Fixes #1836 @phillxnet
* Sat Jan 20 2018 Suman Chakravartula <suman@rockstor.com> - 3.9.2-10
-Catch all exceptions for backwards compatibility (continued). #1854 @schakrava
-improve user messaging re system disk no serial. Fixes #1866 @phillxnet
* Thu Dec 28 2017 Suman Chakravartula <suman@rockstor.com> - 3.9.2-9
-Catch all exceptions for backwards compatibility. #1854 @schakrava
* Thu Dec 21 2017 Suman Chakravartula <suman@rockstor.com> - 3.9.2-8
-improve quotas not enabled behaviour. Fixes #1869 @phillxnet
* Mon Dec 18 2017 Suman Chakravartula <suman@rockstor.com> - 3.9.2-7
-rock-ons-root host pool quota disabled by docker-ce. Fixes #1872 @phillxnet
* Mon Dec 18 2017 Suman Chakravartula <suman@rockstor.com> - 3.9.2-6
-version and date incorrectly reported re update info. Fixes #1870 @phillxnet
* Mon Dec 11 2017 Suman Chakravartula <suman@rockstor.com> - 3.9.2-5
-don't raise exception on quota not enabled. Fixes #1867 @phillxnet
* Sat Dec 9 2017 Suman Chakravartula <suman@rockstor.com> - 3.9.2-4
-share name blank in edit schedule snapshot page. Fixes #1863 @phillxnet
* Sat Dec 9 2017 Suman Chakravartula <suman@rockstor.com> - 3.9.2-3
-Move from docker-engine to docker-ce #1860 @schakrava
* Tue Dec 05 2017 Suman Chakravartula <suman@rockstor.com> - 3.9.2-2
-suspected 3.9.2-1 scheduled snapshot UI regression #1857 @schakrava
* Mon Nov 13 2017 Suman Chakravartula <suman@rockstor.com> - 3.9.2-1
-Schedules broken after update to 3.9.2-0 #1851 @schakrava

* Mon Nov 06 2017 Suman Chakravartula <suman@rockstor.com>
failed to start rockstor hdparm settings #1752 @phillxnet
no drive name on custom smart options page #1756 @phillxnet
mark whole disk LVM members as unusable #1710 @phillxnet
Scheduled scrub throws error #1759 @phillxnet
rogue share.pqgroup db field fails share mounts #1769 @phillxnet
improve mount status reporting capability #1763 @phillxnet
Config backup restore error: exception: isdir() takes exactly 1 argument (0 given) #1765 @phillxnet
useradd error upon config restore #1774 @phillxnet
regression on user create with existing non managed group #1780 @phillxnet
improve scrub status reporting resolution #1786 @phillxnet
SCRUB fails to end / fails to restart after shutdown #1640 @phillxnet
fix portability bug in fs unit tests #1787 @phillxnet
regression in 'force' option - scrub and balance #1790 @phillxnet
Change chosen plugin to bootstrap-select or select2 plugin #1270 @priyaganti
improve rebooted dialog message #1584 @phillxnet
Kernel update #1732 @schakrava
Update Chart.js libs for better ticks & labels sliding #1469 @MFlyer
scheduled scrub blocked by halted, conn-reset, and cancelled states #1800 @phillxnet
scrub task end time incorrect #1802 @phillxnet
share and snapshot api endpoints must be by id and not by name #1807 @schakrava
fix scrub in progress message format regression #1776 @phillxnet
Improve messaging re SMART refresh button #1435 @phillxnet
improve share mount re ro,degraded pool options #1804 @phillxnet
snapshot scheduled task regression re 3.9.1-9 API change #1809 @phillxnet
Unable to create Samba export #1813 @phillxnet
Scrub feedback feature #1243 @phillxnet
scrubs 'show entries' selector ineffectual #1799 @phillxnet
rock-on UI fails to reflect removed container #1795 @schakrava
Sysctl.conf optimizations should go into separate file #1598 @schakrava
failure in share import prep re duplicate name and usage #1828 @phillxnet
share link regression on snapshots page #1829 @phillxnet
[BUGS] Default ulimit setting too low #1656 @schakrava
abstract by-id device path in a function #1839 @KaiRo-at
add share detail links to export tables #1830 @phillxnet
Don't print stack trace for update subscription authorization error #1843 @schakrava

* Sun Jul 02 2017 Suman Chakravartula <suman@rockstor.com>
Support full disk LUKS #550 @phillxnet
Schedule power down/up of the system #735 @MFlyer
Graceful shutdown with cron job #1306 @MFlyer
UI Shares view incorrect sort on size #1673 @MFlyer
Rockstor Translations #1643 @MFlyer
Systemd warns that "rockstor-hdparm.service is marked world-inaccessible" #1493 @schakrava
Importing an unlabeled btrfs RAID5 pool fails #1342 @schakrava
single pool metadata level is single not dup #1409 @phillxnet
Samba Custom configuration UI glitch #1691 @MFlyer
rockstor update doesn't fail if db migration fails #1332 @schakrava
Add Yum capabilities to System updates #1619 @MFlyer
Turn off debug logs in Rockstor built by rpm(prod/testing builds) #1478 @schakrava
update nginx and /etc/issue if mgmt interface config changes #1701 @schakrava
Muting gulp tasks over buildout process #1708 @MFlyer
nbd devices do not support S.M.A.R.T. #1705 @KaiRo-at
fix 'for' attributes on user_create_template labels #1706 @KaiRo-at
create SHA256 certs so browser devtools don't complain all the time #1707 @KaiRo-at
overflow of disk.role db field #1709 @phillxnet
Non integer threshold value in SMART data blocks reporting #1725 @phillxnet
support ro rw degraded and skip_balance mount options #1728 @phillxnet
Support Jumbo frames config in the UI #1044 @schakrava
Extra button adding storage to a Rock-On #1341 @priyaganti
Don't check for Rock-ons metadata when the service is disabled #1286 @schakrava
AFP export doesn't expand when underneath share (subvolume in btrfs) expands #614 @schakrava
insufficient use of btrfs device scan #1547 @phillxnet
Rock-on bad behaviour when starting with no configuration #1579 @priyaganti
add cli initiated config backup #1382 @daniel-illi
change Pool API to use ids instead of names #1741 @schakrava
detached disks used in mount command #1422 @phillxnet
Display client-side error differently #1743 @priyaganti
change disk api to use ids instead of names #1746 @schakrava
propagate user errors properly in user management #1748 @schakrava
minor disk api regression follow up #1750 @phillxnet

* Thu Mar 16 2017 Suman Chakravartula <suman@rockstor.com>
Issue: Non-ASCII password on user creation leads to 'User(...) already exists' #1555 @ansemjo
[Enhancement] data_collector move from Django ORM to CRUD operations (on db writes) #1567 @MFlyer
Dashboard widget resizing is glitchy in Chrome on Mac #1530 @MFlyer
[Bug] Disks widget console errors #1596 @MFlyer
cosmetic issue: create snapshot label appears twice in share details view #1564 @MFlyer
SMART edit icon tooltip text in disks table view not fully visible #1565 @MFlyer
More documentation on services page! #1168 @priyaganti
cleanup dependencies and add build status badge to readme #1604 @schakrava
root and home shares offer delete button #1583 @MFlyer
fs unit tests settings issue #1609 @phillxnet
work around failure of udev to observe btrfs device add #1606 @phillxnet
Flake8 satisfying style improvements and cleanup #1615 @schakrava
Sector Size empty for 512e drives #1590 @phillxnet
Fixing Jenkins Flake8 regressions #1626 @MFlyer
enhance disk role/management subsystem #1494 @phillxnet
balance cancel requested 'unit test' false alarm #1627 @phillxnet
Share usage not reported correctly while pool usage is #1412 @MFlyer
improve state column clarity in network device tables #1633 @phillxnet
keyerror in samba config restore #1585 @MFlyer
"Comment" field not filled when editing Samba share #1647 @MFlyer
inconsistent redirect role validator message and bug #1651 @phillxnet
[Rockstor Devel Feature] Add Gulp file testing #1632 @MFlyer
Rock-on share columns reversed #1581 @schakrava
Remove python downgrade workaround #1587 @schakrava
[Flake8] Unused import over initrock.py script #1663 @MFlyer
Small UI bug while installing rock-ons #1660 @MFlyer
fix replication regression from django 1.8 update #1667 @schakrava
Make software update non-disruptive #1188 @schakrava
Updating Font Awesome to latest 4.7 #1669 @MFlyer

* Tue Dec 13 2016 Suman Chakravartula <suman@rockstor.com>
Improve Dashboard pool usage widget #1426 @sfranzen
Improve pool usage reporting #1460 @sfranzen
Linked to #1379 - writable snapshots #1482 @MFlyer
Show up Rockstor as a Server in AFP Shares #1485 @MFlyer
Ajax-Loader.gif does not dissappear #623 @MFlyer
Increase widget animation timing to grant a better smoothing #1487 @MFlyer
NUT timed shutdown option #982 @phillxnet
improve NUT port config usability #1458 @phillxnet
Fix time comparison failing #1479 @MFlyer
null value in column "details" when parsing SMART error log #1498 @phillxnet
Remove flash websocket files #848 @MFlyer
Glitch in SMART error log UI #1001 @phillxnet
SMART parsing issue shell script helper #1507 @phillxnet
Small Samba regression #1495 @MFlyer
Move from gevent-socketio python-socketio #1503 @MFlyer
Make services configure forms as modals #1278 @MFlyer
remove gateway requirements for manual interface configuration #1520 @tomtom13
Improve Pool delete UX #1195 @gkadillak
use chattr to make parent dirs of mount points immutable #1414 @schakrava
Missing favicon on login page #1535 @MFlyer
failure to submit on modal service dialogs #1537 @MFlyer
support pool compression inline edit in pool details view #1464 @priyaganti
Update Django #1190 @schakrava
Improved handling of spawned functions in socket server #1524 @MFlyer
Samba configuration enhancements #1540 @MFlyer
incorrect space calculation on disk removal #1553 @phillxnet
Wrong Samba AD closing line #1548 @MFlyer
unsaved related object fix #1551 @phillxnet
Resize UI bug #1194 @priyaganti
Fix loading while edit scheduled tasks #1561 @MFlyer
Snapshots & scrubs scheduled tasks not working - double issue #1560 @schakrava
data_collector changes for django >= 1.7 #1556 @MFlyer
add datatables feature to users view #1370 @MFlyer
add datatables feature to pool srub and rebalance tables #1369 @MFlyer
Pool creation succeeds but refresh icon(ajax-loader) still exists #1563 @MFlyer

* Tue Nov 01 2016 Suman Chakravartula <suman@rockstor.com>
Overhaul pagination, sort and search on UI using DataTables. #1138 @priyaganti
Revise internal use and format of device names. #1320 @phillxnet
Support customizing web-ui port. #983 @schakrava
Improvements to password recovery system. #1290 @MFlyer
Remove smb service dependency on rockstor-bootstrap. #1241 @schakrava @phillxnet
add raid56 warning. #1372 @phillxnet
Fix Samba regression from 3.8-14.03 #1385 @phillxnet
Add local/current time on the UI. #1362 @MFlyer
Update postfix config when hostname is changed. #1392 @MFlyer
Edit user page - bad render for username and uid. #1389 @MFlyer
Support Console access from the Web-UI with Shell In a Box. #518 @MFlyer
Allow force removal of Rock-on metadata. #1124 @schakrava
improve nvme compatibility for system disk. #1397 @phillxnet
Fix Services page bottleneck on Active Directory status. #1391 @MFlyer
Improve test e-mail notification. #978 @MFlyer @schakrava
Field validation in e-mail setup. #1340 @MFlyer @schakrava
GMail detects Rockstor as a Less Secure application. #1083 @MFlyer
single to raid1 pool resize not reflected in Web-UI. #1406 @grebnek
Email Alerts page missing dependency. #1410 @MFlyer
Docker journald logging. #1420 @sfranzen
Adjust share usage reporting. #1415 @sfranzen
add samba shadow localtime param. #1252 @MFlyer
Improve Dashboard pool usage widget. #1426 @sfranzen
Fix: argument to docker run should still be -d. #1423 @sfranzen
Fix DataTables error on AFP shares view. #1442 @sfranzen
Bootstrap inline edit with X-editable js library. #1356 @priyaganti
Inline edit - pool compression in Pools view. #1401 @priyaganti
Web-UI initiated balance status not updated during execution. #1405 @phillxnet
improve dashboard disk activity widget for by-id names. #1366 @phillxnet
Allow scheduling of read-only snapshot creation. #1379 @tomtom13 @schakrava
Improve how smb.conf is updated. #1453 @MFlyer
Fix: Dashboard crashes if left open for a long time #998 @MFlyer
add the second knowns fake uuid to exception list. #1461 @schakrava
fs unittests part 1. #1443 @phillxnet
dashboard crashes if opened long - Memory Widget - Part 3. #998 @MFlyer
dashboard crashes if opened long - Cpu Widget - Part 1 Final. #998 @MFlyer
dashboard crashes if opened long - Network Widget - Part 2. #998 @MFlyer
dashboard crashes if opened long - Top Shares Widget - Part 4. #998 @MFlyer
dashboard crashes if opened long - Pool Usage Widget - Part 5. #998 @MFlyer
dashboard crashes if opened long - Storage Metrics Widget - Part 6. #998 @MFlyer
dashboard crashes if opened long - Disks Widget - Part 7. #998 @MFlyer
New progressbars height, tested over 10+ shares. #1476 @MFlyer
support long nutanix device names. #1471 @phillxnet

* Sun Jun 19 2016 Suman Chakravartula <suman@rockstor.com>
Add anacron like feature to task scheduling. #1233 @MFlyer
Add support for policy driven powering down of HDDs from the UI. #885 @phillxnet
Add the feature to browse and download various log files from the UI. #762 @MFlyer
Significantly improve UI templates part 2. #1287 @priyaganti
Significantly improve UI templates part 3. #1304 @priyaganti
Significantly improve UI templates part 4. #1307 @priyaganti
Add different support flows for stable and testing channel users. #1339 @schakrava
Improve Active Directory info popup. #1284 @ScarabMonkey
Improve multiple disk selection during resize. #1196 @priyaganti
Show correct screens in add/remove disks during resize. #811 @priyaganti
Fix power menu alignment. #1192 @priyaganti
Use chardet to properly encode/decode user/group names. #1283 @demount
Add Active Directory rfc2307 support. #1263 @MFlyer
Sort Shares by name in the UI. #973 @maxhq
Fix a regression in scheduled tasks. #1296 @MFlyer
Fix Total capacity widget resize bug. #1225 @MFlyer
Fix deprecated volume removal bug in rock-on update. #1294 @phillxnet
Fix transfer rate column in replication history. #1279 @priyaganti
Improve NTP check in Active Directory service. #1301 @ScarabMonkey
Enhance Rock-on service config UX. #1202 @priyaganti
Properly update mdraid member status. #1214 @phillxnet
Add pagination support to replication tasks. #1305 @priyaganti
Improve snmp config UI. #1240 @schakrava
Humanize replication transfer rate display. #1317 @priyaganti
Fix bug in Pool disk removal wizard. #1325 @phillxnet
Fix a bug in scheduled tasks. #1327 @MFlyer
Add support for nossd mount option. #1313 @priyaganti
Fix regression in network widget. #1302 @MFlyer
Show system users shell info. #1335 @MFlyer
Add the ability of add/remove drives to/from single profile pools. #1337 @bskrtich
Fix a bug in userdel. #1343 @MFlyer
Make Appliance UUID persistent through reinstalls. #1348 @schakrava
Add better error handling to network connection refresh. #1350 @schakrava
Fix handlebar helper in replication. #1352 @priyaganti

* Wed Apr 20 2016 Suman Chakravartula <suman@rockstor.com>
Add Network Teaming and Bonding support. #560 @schakrava @priyaganti
Support user supplied custom S.M.A.R.T parameters. #1079 @phillxnet
Redesign Services page. #796 @priyaganti
Advice user to use nmtui in case of install without network. #1268 @ScarabMonkey
Allow Rock-on metadata update on failed installation. #1259 @schakrava
Add optional smtp authentication to e-mail notification setup. #1228 @MFlyer
Handlebars template improvements in samba UI. #1176 @priyaganti
Add support to sort services by status in the UI. #1201 @MFlyer
Improve storage unmount logic. #1242 @schakrava
Make adding storage to Rock-ons more intuitive. #1178 @priyaganti
Improve tooltip display. #1198 @priyaganti
Make favicon access secure. #1055 @priyaganti
Fix compression UI bug. #1245 @priyaganti @MFlyer
Improve Rock-on install state transition logic. #1216 @schakrava
Mount by-label consistently as first preference. #1181 @schakrava
Fix Samba UI pagination. #1224 @schakrava
Improve scheduled Snapshot management. #1227 @MFlyer
Add more frequency choices for scheduled tasks. #1226 @MFlyer
Automatically map /etc/localtime to Rock-ons. #809 @schakrava
Fix dashboard by locking backend library versions. #1215 @schakrava
Improve S.M.A.R.T self test log parsing. #1207 @phillxnet
Improve S.M.A.R.T behaviour on root drive. #1206 @phillxnet
Fix snapshot name prefix bug. #1186 @schakrava

* Thu Feb 25 2016 Suman Chakravartula <suman@rockstor.com>
Added support for hostname configuration. #896 @Mchakravartula
Improved S.M.A.R.T support for more types drives. #1107 @phillxnet
Improved tooltip design. #1110 @Mchakravartula
Redesigned Pool creation UI to handle large number of drives better. #693 @priyaganti
Improved Share size reporting. #669 @schakrava
Added support for dynamic root Pool name retrieval. #921 @schakrava
Made rockstor-pre service more robust. #1128 @schakrava
Fixed bug in updating nginx on ip changes. #1101 @schakrava
Improved disk information handling of system disk(s). #1116 @phillxnet
Improved AD integration via winbind. #1024 @schakrava
Improved Share deletion UX and warnings. #979 @priyaganti
Improved bulk Snapshot deletion UX. #988 @priyaganti
Fixed a bug in schedule task history display. #1129 @Mchakravartula
Improved bios raid handling on system disk. #1151 @phillxnet
Fixed version display bug in the UI. #1119 @schakrava
Improved Rock-On app profile updates. #1131 @schakrava
Improved support for mdraid root disk setup. #1164 @phillxnet
Change font and color of banner elements. #1165 @gkadillak
Improved Rock-On restart policy. #1132 @schakrava
Fixed a bug in group creation. #1161 @schakrava
Fixed a bug in AD join. #1122 @schakrava
Added support for force removal of Shares. #1125 @schakrava
Added support for custom port in e-mail alerts setup. #837 @schakrava
Fixed a UI bug in Rock-On restart. #1175 @nicolaslt
Fixed a templating bug in Samba exports UI. #1176 @schakrava
Improved design of Services view. #796 @priyaganti @schakrava

* Fri Jan 22 2016 Suman Chakravartula <suman@rockstor.com>
Significantly improved Rock-Ons functionality. #858 @schakrava
Overhauled and optimized frontend with better temlating using Handlebars. #1019 @priyaganti @schakrava
Improved disk scan to handle duplicate names and offline disks better. #937 @phillxnet
Updated django-auth-toolkit and improved the Access Key functionality. #1017 @schakrava
Fixed a bug in S.M.A.R.T monitoring functionality. #1060 @phillxnet
Simplified Rock-on app profile management. #842 @schakrava
Enhanced custom config implementation in Rock-on install wizard. #918 @schakrava
Added support for bigger SSL certs of size up to 12K. #1067 @schakrava
Enhanced state refresh for Shares and Pools when underlying disks drop. #930 @schakrava
Added better support for drive name changes. #897 @schakrava
Fixed admin host related bug in NFS management. #959 @schakrava
Added better handling for md block drives. #1063 @phillxnet
Made Rock-ons framework more robust and simpler. #858 @schakrava
Added S.M.A.R.T support for MSA70 enclosures. #997 @phillxnet
Fixed minor regression in fake serial ui logic. #1086 @phillxnet
Added support for retaining only last 5 kernels. #1068 @schakrava
Made Access Key API a bit more robust. #1080 @Mchakravartula
Fixed a regression with raw S.M.A.R.T error log display. #1084 @phillxnet
Fixed a UI bug in schedule task display. #1058 @Mchakravartula
Improved config ownership management of NUT. #1073 @phillxnet
Fixed a regression in NUT service configuration in the UI. #1094 @phillxnet
Fixed a Share ACL display bug in the UI. #1100 @phillxnet
Improved README. #1104 @Mazo
Improved messaging for S.M.A.R.T self tests on the UI. #1097 @phillxnet

* Fri Dec 11 2015 Suman Chakravartula <suman@rockstor.com>
Rolled out a redesigned Rockstor-Rockstor Share replication feature. #886 @schakrava
Improved functional test coverage. part 1 #992 @Mchakravartula
Improved alerts on the UI #989 @priyaganti
CSS cleanup in the UI #1003 @grogi
Fixed advanced-nfs exports bug. #991 @schakrava
Improved functional test coverage. part 2. #1008 @Mchakravartula
Redesigned switches on the UI. #1013 @priyaganti
Improved functional test coverage. part 3. #1014 @Mchakravartula
Fixed SFTP service toggle bug. #1027 @phillxnet
Fixed AD service status bug. #1029 @phillxnet
Improved rockstor-bootstrap service. #1026 @schakrava
More switch redesign updates on the UI. #1021 @priyaganti
Fixed a bug in network config. #1039 @schakrava

* Wed Oct 28 2015 Suman Chakravartula <suman@rockstor.com>
Improved service orchestration by leveraging Systemd more. #904 @schakrava
Fixed Web-UI to dynamically refresh management interface IP. #917 @schakrava
Fixed a Web-UI issue with network interface management. #915 @schakrava
Clarify password reset instructions. #890 @phillxnet
Refresh Pool state automatically after delete. #859 @schakrava
Improved logic to update /etc/issue with Web-UI link. #924 @phillxnet
Improved certificate labeling on the Web-UI. 938 @phillxnet
Fixed and improved Active Directory integration support. #860 @schakrava
Simplified Reboot/Shutdown functionality. #943 @phillxnet
Sort services alphabetically by default. #907 @schakrava
Improve test coverage for Snapshot functionality. #945 @Mchakravartula
Clean up Web-UI for OS Pool. #926 @Mchakravartula
Improve test coverage for Network interface management. #954 @Mchakravartula
Fixed broken S.M.A.R.T data collection for some HDDs. #657 @phillxnet
Fixed Web-UI bug that prevented Cloning writable Snapshots. #939 @schakrava
Fixed a small regression in /etc/issue update. #961 @phillxnet
Fixed the submit button in Rock-ons install wizard. #975 maxhq
Improved e-mail notifications by properly setting send address. #970 @phillxnet
Improved overall functional test coverage. #967 @Mchakravartula
Removed qgroup rescan work around. #950 @schakrava

* Sat Oct 03 2015 Suman Chakravartula <suman@rockstor.com>
Added support for UPS. #595 @phillxnet
Added Shadow Copy support for Windows Samba clients. #715 @schakrava @priyaganti
Improved Network management #799 @schakrava
Improved User management functional test coverage #856 @Mchakravartula
Improved NFS functional test coverage #876 @Mchakravartula @schakrava
Improved AFP functional test coverage #877 @Mchakravartula
Improved SFTP functional test coverage #878 @Mchakravartula
Made development side of supervisor processes consistent with production. #852 @phillxnet
Improved UI for mobile #869 @snamstorm
Made forms on the UI better and consistent. #891 @priyaganti
Added Stable and Testing updates channels. #899 @schakrava

* Tue Sep 01 2015 Suman Chakravartula <suman@rockstor.com>
Added more functional tests. #828 @Mchakravartula
Improved styling of the login page. #815 @snamstorm
Made ssh access stricter and fixed a sftp related bug. #838 @schakrava
Improved display of contributions during update. #845 @priyaganti
Improved top menu bar in the UI. #832 @snamstorm
Added support to use system timezone. #712 @schakrava
Improved sidebar menu in the UI. #840 @snamstorm
Cleaned up Share detail page in the UI. #814 @Mchakravartula
Add quota support for imported pools and shares. #687 @schakrava

* Mon Aug 24 2015 Suman Chakravartula <suman@rockstor.com>
Enhanced the auto software update process. #695 @schakrava
Improved disk serial number identification logic. #757 @phillxnet
Added support for Rock-on installation using Firefox browser. #744 @priyaganti
Made Rock-on service state persistent after reboot. #721 @schakrava @phillxnet
Fixed buggy NFS export management #713 @schakrava
Improved functional test coverage #733 @Mchakravartula
Fixed S.M.A.R.T service configuration management. #741 @schakrava @phillxnet
Fixed NTP service for it's state to be persistent after reboot. #768 @schakrava
Improved e-mail notification setup. #793 @phillxnet
Improved wording #792 @phillxnet
Fixed a minor UI bug to refresh properly after a disk wipe. #635 @schakrava
Improved tooltips #802 @priyaganti

* Fri Aug 14 2015 Suman Chakravartula <suman@rockstor.com>
Reworked the data-collector service and removed dashboard polling. Both server and client side performance is significantly improved and all unnecessary IO is eliminated. #763 @gkadillak @schakrava
Fixed buggy behavior with display and deletion of Clones. #727 @schakrava
Added support for e-mail setup for receiving notifications and alerts. #633 @Mchakravartula @schakrava
Fixed broken UI during Share rollback. #774 @schakrava
Fixed Samba export field display on edit. #767 @Mchakravartula
Added support to set Samba workgroup from the UI. #678 @schakrava
Enhanced Share ownership edit form to display sorted users and correct pre-select values. #775 @Mchakravartula
Reworked Pool resize logic to be simpler and more robust. #580 @schakrava

* Fri Jul 31 2015 Suman Chakravartula <suman@rockstor.com>
Added support for config(system state like users, exports etc..) backup and restoration. #392 @schakrava @gkadillak
Fixed task scheduling. #728 @gkadillak @schakrava
Fixed units drop down in Share resize form #745 @Mchakravartula
Fixed advanced nfs exports feature #754 @schakrava
Fixed wrong kernel warning message #746 @gkadillak
Fixed scrub status parsing #752 @schakrava

* Wed Jul 15 2015 Suman Chakravartula <suman@rockstor.com>
Optimize Rockstor for usb flash drive and ssd deployments. #724 @schakrava @phillxnet
Improve Rock-on logging with syslog. #723 @schakrava
Revive and enhance websocket framework and the WebUI. #706 @gkadillak @phillxnet
Make service state changes persist across reboot. #660 @schakrava @phillxnet`

* Mon Jul 06 2015 Suman Chakravartula <suman@rockstor.com>
Significantly improved the Rock-ons framework. #697 @schakrava @gkadillak @phillxnet
Added a new exciting Rock-on: OwnCloud. #697 Thanks @schakrava @gkadillak @phillxnet
Overhauled look and feel of the UI by upgrading Bootstrap. #670 @gkadillak
Dynamically update raid level changes from the system. #650 @schakrava
Improved test coverage for Samba API. #679 @Mchakravartula
Improved test coverage for User API. #688 @Mchakravartula

* Wed Jun 17 2015 Suman Chakravartula <suman@rockstor.com>
Added support to Auto import BTRFS data from previous install or a different Rockstor system. Issue #534
Added more functional tests and improved test coverage. Issue #676
Enhanced disk scan logic to better support KVM. Issue #673

* Sun Jun 07 2015 Suman Chakravartula <suman@rockstor.com>
Improved Rock-ons code over all and added Syncthing, Transmission and BTSync. Issue #665
Added functional tests to improve coverage by about 10%. Issue #648
Fixed samba password reset issue. Issue #617

* Wed May 20 2015 Suman Chakravartula <suman@rockstor.com>
Improved user management to be consistent with system state. Issue #613
Improved HDD wipe functionality for non-btrfs filesystems. Issue #572
Fixed misc bugs related to S.M.A.R.T support.

* Mon May 18 2015 Suman Chakravartula <suman@rockstor.com>
Added S.M.A.R.T support for monitoring HDDs. You can now proactively monitor the health of your Hard Drives. Issue #498
Improved the core API by upgraded to Django Rest Framework(DRF) 3.1. Issue #637
Improved automated testing with new functional tests for Pool related featureset. Issue #639

* Wed Apr 29 2015 Suman Chakravartula <suman@rockstor.com>
Fixed a minor bug in replication code that was causing problems if appliance id starts with a number. Issue #616
Optimized service monitor to do minimal IO. The new code is significantly better and especially helpful to those users running Rockstor from Flash. Issue #585
Added a new Snapshots screen at the top level in the Storage Tab. All snapshots on the system can now be managed from one screen. Issue #573

* Sat Apr 18 2015 Suman Chakravartula <suman@rockstor.com>
Enhanced shutdown/reboot such that web-ui refresh doesn't repeat itself. Issue #612
Enhanced web-ui validation so users are clearly prohibited from choosing share, snapshot etc.. names with spaces in them. Issue #622

* Tue Apr 14 2015 Suman Chakravartula <suman@rockstor.com>
New feature -- Rockons. Added framework support with limited release of Rockons. Issue #542
Added support for custom TLS certificate. Users can add a custom certificate for the web-ui. Issue #570

* Sat Mar 07 2015 Suman Chakravartula <suman@rockstor.com>
Added support for automatic scheduled updates. Once enabled, Rockstor checks for updates once a day. Issue #604
Added wizard support to pool resize to properly guide the user. Issue #577

* Tue Feb 17 2015 Suman Chakravartula <suman@rockstor.com>
Added support for Share creation on the root disk. Now you get a bonus pool called rockstor_rockstor. Consume it responsibly. Issue#600
Fixed a bug that forced create mask on samba exports. Now you can override the default(744) via custom configuration. Issue#587
Added a web-ui goodie. The logged in user will be displayed on the web-ui. Issue#576

* Mon Feb 09 2015 Suman Chakravartula <suman@rockstor.com>
Enhanced Rockstor to Rockstor Share replication. This is a significant feature that can be used to keep your Shares automatically synced between two Rockstor appliances. Issue#574
Fixed a bug in Raid5/6 pool creation. Raid5/6 is still actively being tested, but this bug caused error on creation. Issue#579
Enhanced oauth token generation for api access and made it more efficient. Issue#590

* Tue Jan 20 2015 Suman Chakravartula <suman@rockstor.com>
Added Pool raid level migration. Disks can be added and raid level can be changed. Disks can also be removed from Pools. Issue#517
Added support for providing custom Samba configuration during Share export. Issue#555
Added support to kick of a Pool balance process to redistribute Pool data among it's disks. Issue #510
Fix a bug that prevented Samba exports to be deleted. Issue #566

* Wed Jan 07 2015 Suman Chakravartula <suman@rockstor.com>
Updated kernel to 3.18.1 and fixed a minor bug related to it. Issue #557
Enhanced compression support. Issue #559
Improved snapshot scheduled task management. Issue #475

* Wed Dec 24 2014 Suman Chakravartula <suman@rockstor.com>
Added support for compression. It can be enabled both at the Pool level or at individual Share level. Issue #468
Redesigned snapshots to manage them more cleanly. Issue #536
Simplified SMB and AFP share discovery. Issue #536
Enhanced scheduled task functionality. You can set a number of Snapshots to retain and older snapshots will be deleted according to this policy. Issue #513

* Wed Dec 10 2014 Suman Chakravartula <suman@rockstor.com>
Enhanced support for multiple network interfaces. Issue #521
Fixed Pool scrub bug and improved it overall. Issue #516
Better handling of Disks without serial numbers. Issue #545
Fixed bug resulting from disk name changes triggered by replacement etc.. Issue #546

* Sun Nov 23 2014 Suman Chakravartula <suman@rockstor.com>
Fixed snapshot clone delete bug. Issue #520
Enhanced ui input validation. Issue #541
Enhanced pool creation UX. Issue #434
Misc UI improvements. Issue #537 and #538

* Sat Nov 15 2014 Suman Chakravartula <suman@rockstor.com>
Added SNMP support. Issue #469
Fixed minor snapshot rollback bug. Issue #511
Enhanced user/group management. Issue #401
Enhanced Memory widget in the dashboard. Issue #371

* Thu Nov 06 2014 Suman Chakravartula <suman@rockstor.com>
Fixed Samba guest access. Issue #515
Enhanced Pool resize functionality. Issue #299
Added a few minor UI enhancements. Issue #522

* Sat Oct 25 2014 Suman Chakravartula <suman@rockstor.com>
Added AFP support. Shares can be exported via AFP protocol and Rockstor can be used as a Time Machine server. Issue #323
Added a new widget to show overall capacity and usage information of the system. Issue #429
Added support to identify drives physically and replace them easily if necessary. Issue #499
Fixed a SFTP related bug that could cause sshd service to terminate. Issue #505

* Fri Oct 24 2014 Suman Chakravartula <suman@rockstor.com>
Added AFP support. Shares can be exported via AFP protocol and Rockstor can be used as a Time Machine server. Issue #323
Added a new widget to show overall capacity and usage information of the system. Issue #429
Added support to identify drives physically and replace them easily if necessary. Issue #499
Fixed a SFTP related bug that could cause sshd service to terminate. Issue #505

* Wed Oct 15 2014 Suman Chakravartula <suman@rockstor.com>
Added shutdown/reboot feature in the web-ui. Issue #466
Fixed snapshot rollback bug. Issue #492
Enhanced nfs service display and switch on the web-ui. Issue #483

* Thu Oct 09 2014 Suman Chakravartula <suman@rockstor.com>
Enabled edit functionality for samba exports and enhanced the interface. Issue #481 and #467
Fixed a bug and made service monitoring more stable. Issue #476

* Wed Oct 01 2014 Suman Chakravartula <suman@rockstor.com>
!!!!SPECIAL NOTE!!! This particular update may cause the web-ui to wait for ever. Manually refresh your browser after few minutes.
Enhanced Share create form and Pool usage display on the web-ui. Issue #418
Fixed TLS cert generation so it happens on user's Rockstor box and self-signed by the user. Issue #485

* Sat Sep 27 2014 Suman Chakravartula <suman@rockstor.com>
Fixed device scan issue that created issues after reboot. Issue #465
Misc ui enhancements. Issue #452, #450, #480

* Thu Sep 18 2014 Suman Chakravartula <suman@rockstor.com>
Fixed minor SFTP related bugs. Issue #394
Added ssh pub key as an optional input during user creation. Issue #463

* Mon Sep 01 2014 Suman Chakravartula <suman@rockstor.com>
Fresh new Rockstor 3.0 rpm that's installed along with the OS.


