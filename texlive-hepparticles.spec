Name:		texlive-hepparticles
Version:	2.0
Release:	3
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
%{_texmfdistdir}/tex/latex/hepparticles
%doc %{_texmfdistdir}/doc/latex/hepparticles

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
