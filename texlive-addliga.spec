Name:		texlive-addliga
Version:	50912
Release:	2
Summary:	Access basic ligatures in legacy TrueType fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/addliga
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/addliga.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/addliga.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small and simple package allows LuaLaTeX users to access
basic ligatures (ff, fi, ffi, fl, ffl) in legacy TrueType fonts
(those lacking a liga table) accessed via fontspec.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/addliga
%doc %{_texmfdistdir}/doc/lualatex/addliga

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
