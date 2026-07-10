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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small and simple package allows LuaLaTeX users to access basic
ligatures (ff, fi, ffi, fl, ffl) in legacy TrueType fonts (those lacking
a liga table) accessed via fontspec.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/lualatex
%dir %{_datadir}/texmf-dist/tex/lualatex
%dir %{_datadir}/texmf-dist/doc/lualatex/addliga
%dir %{_datadir}/texmf-dist/tex/lualatex/addliga
%doc %{_datadir}/texmf-dist/doc/lualatex/addliga/README
%doc %{_datadir}/texmf-dist/doc/lualatex/addliga/addliga.pdf
%doc %{_datadir}/texmf-dist/doc/lualatex/addliga/addliga.tex
%{_datadir}/texmf-dist/tex/lualatex/addliga/addliga.sty
