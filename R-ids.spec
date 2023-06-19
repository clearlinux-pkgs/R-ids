#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ids
Version  : 1.0.1
Release  : 11
URL      : https://cran.r-project.org/src/contrib/ids_1.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ids_1.0.1.tar.gz
Summary  : Generate Random Identifiers
Group    : Development/Tools
License  : MIT
Requires: R-openssl
Requires: R-uuid
BuildRequires : R-openssl
BuildRequires : R-uuid
BuildRequires : buildreq-R

%description
# ids
[![Project Status: Active - The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Linux Build Status](https://travis-ci.org/richfitz/ids.svg?branch=master)](https://travis-ci.org/richfitz/ids)
[![codecov.io](https://codecov.io/github/richfitz/ids/coverage.svg?branch=master)](https://codecov.io/github/richfitz/ids?branch=master)
[![](https://www.r-pkg.org/badges/version/ids)](https://cran.r-project.org/package=ids)

%prep
%setup -q -c -n ids
cd %{_builddir}/ids

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641035502

%install
export SOURCE_DATE_EPOCH=1641035502
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ids
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ids
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ids
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ids || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ids/DESCRIPTION
/usr/lib64/R/library/ids/INDEX
/usr/lib64/R/library/ids/LICENSE
/usr/lib64/R/library/ids/Meta/Rd.rds
/usr/lib64/R/library/ids/Meta/features.rds
/usr/lib64/R/library/ids/Meta/hsearch.rds
/usr/lib64/R/library/ids/Meta/links.rds
/usr/lib64/R/library/ids/Meta/nsInfo.rds
/usr/lib64/R/library/ids/Meta/package.rds
/usr/lib64/R/library/ids/Meta/vignette.rds
/usr/lib64/R/library/ids/NAMESPACE
/usr/lib64/R/library/ids/NEWS.md
/usr/lib64/R/library/ids/R/ids
/usr/lib64/R/library/ids/R/ids.rdb
/usr/lib64/R/library/ids/R/ids.rdx
/usr/lib64/R/library/ids/R/sysdata.rdb
/usr/lib64/R/library/ids/R/sysdata.rdx
/usr/lib64/R/library/ids/doc/ids.R
/usr/lib64/R/library/ids/doc/ids.Rmd
/usr/lib64/R/library/ids/doc/ids.html
/usr/lib64/R/library/ids/doc/index.html
/usr/lib64/R/library/ids/help/AnIndex
/usr/lib64/R/library/ids/help/aliases.rds
/usr/lib64/R/library/ids/help/ids.rdb
/usr/lib64/R/library/ids/help/ids.rdx
/usr/lib64/R/library/ids/help/paths.rds
/usr/lib64/R/library/ids/html/00Index.html
/usr/lib64/R/library/ids/html/R.css
/usr/lib64/R/library/ids/tests/testthat.R
/usr/lib64/R/library/ids/tests/testthat/test-adjective-animal.R
/usr/lib64/R/library/ids/tests/testthat/test-case.R
/usr/lib64/R/library/ids/tests/testthat/test-ids.R
/usr/lib64/R/library/ids/tests/testthat/test-proquint.R
/usr/lib64/R/library/ids/tests/testthat/test-random.R
/usr/lib64/R/library/ids/tests/testthat/test-sentence.R
/usr/lib64/R/library/ids/tests/testthat/test-uuid.R
