%define module precis-i18n
%define oname precis_i18n

Name:		python-precis-i18n
Version:	1.1.2
Release:	1
Summary:	Internationalised Usernames and Passwords
Group:		Development/Python
License:	MIT
URL:		https://pypi.org/project/precis-i18n
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)

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

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%doc README.md
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}*.*-info
