Summary:	Python bindings for libcdio
Name:		python-pycdio
Version:	0.19
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://ftp.gnu.org/gnu/libcdio/pycdio-%{version}.tar.gz
# Source0-md5:	3829879fbfc7f8d85a79c753735788f0
URL:		http://www.gnu.org/software/libcdio/
BuildRequires:	libcdio-devel
BuildRequires:	pkg-config
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	swig-python
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for libcdio.

%prep
%setup -qn pycdio-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install	\
	--optimize=2		\
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{py_sitedir}/_pycdio.so
%attr(755,root,root) %{py_sitedir}/_pyiso9660.so
%{py_sitedir}/cdio.py[co]
%{py_sitedir}/iso9660.py[co]

