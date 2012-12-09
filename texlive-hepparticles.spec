# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/hepparticles
# catalog-date 2007-02-23 00:16:39 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-hepparticles
Version:	20070223
Release:	2
Summary:	Macros for typesetting high energy physics particle names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hepparticles
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepparticles.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepparticles.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
HEPparticles is a set of macros for typesetting high energy
particle names, to meet the following criteria: 1. The main
particle name is a Roman or Greek symbol, to be typeset in
upright font in normal contexts. 2. Additionally a superscript
and/or subscript may follow the main symbol. 3. Particle
resonances may also have a resonance specifier which is typeset
in parentheses following the main symbol. In general the
parentheses may also be followed by sub- and superscripts. 4.
The particle names are expected to be used both in and out of
mathematical contexts. 5. If the surrounding text is bold or
italic then the particle name should adapt to that context as
best as possible (this may not be possible for Greek symbols).
A consequence of point 5 is that the well-known problems with
boldness of particle names in section titles, headers and
tables of contents automatically disappear if these macros are
used.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hepparticles/hepparticles.sty
%doc %{_texmfdistdir}/doc/latex/hepparticles/README
%doc %{_texmfdistdir}/doc/latex/hepparticles/hepparticles.pdf
%doc %{_texmfdistdir}/doc/latex/hepparticles/hepparticles.tex
%doc %{_texmfdistdir}/doc/latex/hepparticles/testhepparticles.pdf
%doc %{_texmfdistdir}/doc/latex/hepparticles/testhepparticles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070223-2
+ Revision: 752541
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070223-1
+ Revision: 718610
- texlive-hepparticles
- texlive-hepparticles
- texlive-hepparticles
- texlive-hepparticles

