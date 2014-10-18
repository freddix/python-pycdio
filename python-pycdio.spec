Summary:	Python bindings for libcdio
Name:		python-pycdio
Version:	0.20
Release:	2
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://ftp.gnu.org/gnu/libcdio/pycdio-%{version}.tar.gz
# Source0-md5:	3f075574f661f49f4ede89aff9ff0cda
URL:		http://www.gnu.org/software/libcdio/
BuildRequires:	libcdio-devel >= 0.90
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
%{py_sitedir}/pycdio.py[co]
%{py_sitedir}/iso9660.py[co]
%{py_sitedir}/pyiso9660.py[co]

