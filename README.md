# Howto rpmbuild the 'rockstor' package

## Repository contents

This repository [rockstor-rpmbuild](https://github.com/rockstor/rockstor-rpmbuild) contains the rpmbuild spec file,
the repositories license file: `SPDX-License-Identifier: GPL-3.0-or-later`
FSF Free/Libre, & OSI approved according to: [SPDX License List](https://spdx.org/licenses/).
And this README.md: to be formatted according to 
[Semantic Linefeeds](https://rhodesmill.org/brandon/2012/one-sentence-per-line/)
which sites Brian W. Kernighan (1974).
I.e.: For content additions/changes please stick to **one sentence per line**
as this helps with translations and reviews of changes.
Really long sentences may be broken at punctuation points.

## Contributions

As with all 'The Rockstor Projects' repositories, contributions are always welcome.
We depend upon domain experts to assist with our community endeavour.
For contribution guidelines, see:
[Contributing to Rockstor - Developers](https://rockstor.com/docs/contribute/contribute.html#developers).

## Getting started

This repository is aimed at developers/enthusiasts only.
See our [Regular documentation](https://rockstor.com/docs/) for general infomation about Rocksor,
and specifically the [Installation]() subsection for how to install a Rockstor instance.
The rest of this guide assumes such an instance is in use, and has been fully updated.

Using an existing Rockstor install ensures that at least our prior dependencies are in place.
This helps with establishing if any new dependencies are required when making spec file changes.
The rpmbuild process, within the %check scriptlet, also runs all our existing unit tests.
As such a properly configured and running Postgres server is required.
The prior installs rockstor-pre.service (initrock) would have asserted these conditions.
Otherwise the rpmbuild command will fail on the %check scriptlet stage.

### Remove the existing package

See: [Remove the Existing Rockstor RPM install](https://rockstor.com/docs/contribute/contribute.html#remove-the-existing-rockstor-rpm-install)

### Establish rpm spec file

The RPM spec file named **rockstor.spec** is required on the prior installer instance.

#### Via your rockstor-rpmbuild GitHub fork

It is assumed in this section that you have forked the rockstor-rpmbuild GitHub repository,
as per the Developer docs advise for the rockstor-core repository.

```shell
zypper --non-interactive install --no-recommends git
cd /opt
git clone https://github.com/your_github_username/rockstor-rpmbuild.git
cd rockstor-rpmbuild/
git checkout testing  # or stable, or your issue branch
```
For specific git branches re making/submitting back changes see the
[Making changes](https://rockstor.com/docs/contribute/contribute.html#making-changes)
doc section and adapt for this rockstor-rpmbuild repository.

If you are developing a contribution, be sure to include all upstream changes:
in the case of developing against the **testing channel** (normal dev target) use:
```shell
git remote add upstream https://github.com/rockstor/rockstor-rpmbuild.git
# git remote show  # should then indicate all remotes.
git pull --rebase upstream testing
```

#### Via rsync from your development system

Or you could rsync your local copy of the rockstor-rpmbuild repository, over from your development system.

## Install rpmbuild
```shell
zypper install --no-recommends rpm-build
```
**NOTE: Solution 1: deinstallation of busybox-gzip ...**
May be required (replaced by the full gzip).
See: [pre-install gzip to avoid busybox-gzip via dependency](https://github.com/rockstor/rockstor-installer/issues/135)


## Build the RPM/SRPM

Both the regular RPM, and its source variant (SRPM) can be build with a single command.

```shell
# Current dir must be that of the spec file:
rpmbuild -ba -v rockstor.spec
```

The tail end of the resulting output indicates the built RPM and SRPM files, e.g.:
```shell
...
Wrote: /usr/src/packages/SRPMS/rockstor-4.5.7-0.src.rpm
Wrote: /usr/src/packages/RPMS/x86_64/rockstor-4.5.7-0.x86_64.rpm
...
```

Note that currently our arch specific RPMs are built to prove the integrated (%check) tests,
on the intended/target architecture.
Their contents, for now at least, are not actually architecture specific.
But when installed, the resulting RPMs' Poetry build orchestrator,
links/downloads and/or builds what is found to be required,
and places it in the `.venv` subdirectory of `/opt/%{name}`.

## Caveats

### RPM will not be signed.

All official Rockstor packages, and their host repositories, are signed by the project.
As such a hand/custom-built package will have no signature.
Options:
1) The fix is to sign you rpm.
2) The workaround (reasonable for development testing) is to ignoe gpg checks via e.g.:
    ```shell
    zypper --no-gpg-checks /usr/src/packages/RPMS/x86_64/rockstor-4.5.7-0.x86_64.rpm
    ```

### RPM relocation

RPM Relocation; see: "Prefix: /opt" in the spec file, is known to be incompletely implemented:
both here in [rockstor-rpmbuild](https://github.com/rockstor/rockstor-rpmbuild)
and in the [rockstor-core](https://github.com/rockstor/rockstor-core).
Contributions to complete this capability are of course welcome.
But this is not a priority for the project.

### Package renaming

There is a facility within the rpmbuild spec file to rename the resulting package.
This, as per RPM relocation above, is also only partially implemented across our repositories.
And would entail far more work to implement than the relocation capability.
Again this is not a priority for the project.

Both RPM relocation and renaming would benefit from package-name/install-location aware database instances.
