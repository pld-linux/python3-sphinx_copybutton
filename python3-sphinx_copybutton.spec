#
# Conditional build:
%bcond_with	doc	# Sphinx documentation (some files missing in sdist)

Summary:	Add a copy button to each of your code cells
Summary(pl.UTF-8):	Dodanie przycisku do kopiowania do każdej komórki z kodem
Name:		python3-sphinx_copybutton
Version:	0.5.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-copybutton/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-copybutton/sphinx-copybutton-%{version}.tar.gz
# Source0-md5:	223f26b9ba5397e5554075bc540a3b46
URL:		https://pypi.org/project/sphinx-copybutton/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-ipython
BuildRequires:	python3-myst_nb
BuildRequires:	python3-sphinx_book_theme
BuildRequires:	sphinx-pdg-3 >= 1.8
%endif
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small Sphinx extension to add a "copy" button to code blocks.

%description -l pl.UTF-8
Małe rozszerzenie Sphinksa dodające przycisk kopiujący do fragmentów
kodu.

%prep
%setup -q -n sphinx-copybutton-%{version}

%build
%py3_build

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/sphinx_copybutton
%{py3_sitescriptdir}/sphinx_copybutton-%{version}-py*.egg-info
