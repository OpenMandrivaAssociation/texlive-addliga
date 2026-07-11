%global tl_name addliga
%global tl_revision 78793

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Access basic ligatures in legacy TrueType fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/addliga
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/addliga.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/addliga.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small and simple package allows LuaLaTeX users to access basic
ligatures (ff, fi, ffi, fl, ffl) in legacy TrueType fonts (those lacking
a liga table) accessed via fontspec.

