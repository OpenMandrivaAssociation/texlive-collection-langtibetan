# revision 14727
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langtibetan
Epoch:		1
Version:	20120224
Release:	2
Summary:	Tibetan
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langtibetan.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-ctib
Requires:	texlive-otibet
Requires:	texlive-collection-basic

%description
Support for typesetting Tibetan.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780456
- Update to latest release.
- Import texlive-collection-langtibetan
- Import texlive-collection-langtibetan

