%global srcname precis_i18n

Name:		python-precis-i18n
Version:	1.0.4
Release:	4
Summary:	Internationalised Usernames and Passwords
Group:		Development/Python
License:	MIT
URL:		https://pypi.python.org/pypi/%{srcname}
Source0:	https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)

%{?python_provide:%python_provide python3-%{srcname}}

%description
The PRECIS framework makes internationalised user names and
passwords safer for use by applications. PRECIS profiles transform
unicode strings into a canonical form, suitable for comparison.

This module implements the PRECIS Framework as described in:
 - PRECIS Framework: Preparation, Enforcement, and Comparison of
   Internationalized Strings in Application Protocols (RFC 8264).
 - Preparation, Enforcement, and Comparison of Internationalized
   Strings Representing Usernames and Passwords (RFC 8265).
 - Preparation, Enforcement, and Comparison of Internationalized
   Strings Representing Nicknames (RFC 8266).


%prep
%setup -q -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%files
%doc README.rst
%{python_sitelib}/%{srcname}/
%{python_sitelib}/%{srcname}*.egg-info
