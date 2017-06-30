#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-e1071
Version  : 1.6.8
Release  : 36
URL      : http://cran.r-project.org/src/contrib/e1071_1.6-8.tar.gz
Source0  : http://cran.r-project.org/src/contrib/e1071_1.6-8.tar.gz
Summary  : Misc Functions of the Department of Statistics, Probability
Group    : Development/Tools
License  : GPL-2.0
Requires: R-e1071-lib
Requires: R-SparseM
BuildRequires : R-SparseM
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-e1071 package.
Group: Libraries

%description lib
lib components for the R-e1071 package.


%prep
%setup -q -c -n e1071

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496605880

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1496605880
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library e1071
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library e1071
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library e1071
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library e1071
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/e1071/DESCRIPTION
/usr/lib64/R/library/e1071/INDEX
/usr/lib64/R/library/e1071/Meta/Rd.rds
/usr/lib64/R/library/e1071/Meta/features.rds
/usr/lib64/R/library/e1071/Meta/hsearch.rds
/usr/lib64/R/library/e1071/Meta/links.rds
/usr/lib64/R/library/e1071/Meta/nsInfo.rds
/usr/lib64/R/library/e1071/Meta/package.rds
/usr/lib64/R/library/e1071/Meta/vignette.rds
/usr/lib64/R/library/e1071/NAMESPACE
/usr/lib64/R/library/e1071/NEWS.Rd
/usr/lib64/R/library/e1071/R/e1071
/usr/lib64/R/library/e1071/R/e1071.rdb
/usr/lib64/R/library/e1071/R/e1071.rdx
/usr/lib64/R/library/e1071/doc/index.html
/usr/lib64/R/library/e1071/doc/svmdoc.R
/usr/lib64/R/library/e1071/doc/svmdoc.Rnw
/usr/lib64/R/library/e1071/doc/svmdoc.pdf
/usr/lib64/R/library/e1071/doc/svminternals.Rnw
/usr/lib64/R/library/e1071/doc/svminternals.pdf
/usr/lib64/R/library/e1071/help/AnIndex
/usr/lib64/R/library/e1071/help/aliases.rds
/usr/lib64/R/library/e1071/help/e1071.rdb
/usr/lib64/R/library/e1071/help/e1071.rdx
/usr/lib64/R/library/e1071/help/paths.rds
/usr/lib64/R/library/e1071/html/00Index.html
/usr/lib64/R/library/e1071/html/R.css
/usr/lib64/R/library/e1071/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/e1071/libs/e1071.so
/usr/lib64/R/library/e1071/libs/e1071.so.avx2
/usr/lib64/R/library/e1071/libs/e1071.so.avx512
