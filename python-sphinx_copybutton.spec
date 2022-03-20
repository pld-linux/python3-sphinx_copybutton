#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Add a copy button to each of your code cells
Summary(pl.UTF-8):	Dodanie przycisku do kopiowania do każdej komórki z kodem
Name:		python-sphinx_copybutton
# keep 0.2.6 here for python2 support
Version:	0.2.6
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-copybutton/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-copybutton/sphinx-copybutton-%{version}.tar.gz
# Source0-md5:	0c3380264ff0b7543bdff0f0f154c87f
Patch0:		%{name}-deps.patch
URL:		https://pypi.org/project/sphinx-copybutton/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small Sphinx extension to add a "copy" button to code blocks.

%description -l pl.UTF-8
Małe rozszerzenie Sphinksa dodające przycisk kopiujący do fragmentów
kodu.

%package -n python3-sphinx_copybutton
Summary:	Add a copy button to each of your code cells
Summary(pl.UTF-8):	Dodanie przycisku do kopiowania do każdej komórki z kodem
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sphinx_copybutton
A small Sphinx extension to add a "copy" button to code blocks.

%description -n python3-sphinx_copybutton -l pl.UTF-8
Małe rozszerzenie Sphinksa dodające przycisk kopiujący do fragmentów
kodu.

%prep
%setup -q -n sphinx-copybutton-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/sphinx_copybutton
%{py_sitescriptdir}/sphinx_copybutton-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_copybutton
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/sphinx_copybutton
%{py3_sitescriptdir}/sphinx_copybutton-%{version}-py*.egg-info
%endif
