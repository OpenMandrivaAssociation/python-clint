Name:		python-clint
Version:	0.5.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/c/clint/clint-%{version}.tar.gz
Summary:	Python Command Line Interface Tools
URL:		https://pypi.org/project/clint/
License:	ISC
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Python Command Line Interface Tools

%files
%{py_sitedir}/clint
%{py_sitedir}/clint-*.*-info
