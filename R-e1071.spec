#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-e1071
Version  : 1.7.13
Release  : 105
URL      : https://cran.r-project.org/src/contrib/e1071_1.7-13.tar.gz
Source0  : https://cran.r-project.org/src/contrib/e1071_1.7-13.tar.gz
Summary  : Misc Functions of the Department of Statistics, Probability
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-e1071-lib = %{version}-%{release}
Requires: R-proxy
BuildRequires : R-proxy
BuildRequires : R-randomForest
BuildRequires : buildreq-R

%description
transform, fuzzy clustering, support vector machines,
	     shortest path computation, bagged clustering, naive Bayes
	     classifier, generalized k-nearest neighbour ...

%package lib
Summary: lib components for the R-e1071 package.
Group: Libraries

%description lib
lib components for the R-e1071 package.


%prep
%setup -q -n e1071
cd %{_builddir}/e1071

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678816636

%install
export SOURCE_DATE_EPOCH=1678816636
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
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/e1071/tests/clustering.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/e1071/libs/e1071.so
/usr/lib64/R/library/e1071/libs/e1071.so.avx2
/usr/lib64/R/library/e1071/libs/e1071.so.avx512
