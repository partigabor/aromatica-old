% https://academic.oup.com/dsh/pages/General_Instructions % all wrong

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{dsh}[Digital Scolarship in the Humanities]

% Load class as base
\newif\ifinitial
\DeclareOption{initial}{\initialtrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[12pt]{article}

\usepackage[a4paper, margin=3cm]{geometry}
\usepackage[style=british]{csquotes}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage[dvipsnames]{xcolor} % Color names

\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=RoyalBlue,
    anchorcolor=black,
    citecolor=RoyalBlue,
    filecolor=black,
    menucolor=black,
    runcolor=black,
    urlcolor=RoyalBlue}
\hypersetup{breaklinks=true}
\usepackage{url}

\usepackage{blindtext}
\usepackage{soul} %strikethrough \st{} and highlight \hl{}
\usepackage{authblk}
\usepackage{endnotes}

\usepackage{epigraph}
\setlength\epigraphwidth{\textwidth}
\setlength\epigraphrule{0pt}
\renewcommand{\epigraphflush}{center}
\renewcommand{\sourceflush}{flushleft}
\renewcommand{\epigraphsize}{\small}
\setlength\afterepigraphskip{-1\baselineskip}

\usepackage{titlesec}
\titleformat{\section}{\bfseries\Large}{\thesection.}{0.5em}{}
\titleformat{\subsection}{}{\thesubsection}{1em}{\itshape}

% Languages, scripts, and fonts

% Font packages
% \usepackage{libertine} % Latin, Greek, Cyrillic, Hebrew

% Fontspec
% \usepackage{fontspec}
% \setmainfont{Times New Roman}
% \defaultfontfeatures{Ligatures={TeX}}

% Language settings
% \usepackage[main=english, bidi=basic]{babel}

% % Automatic typesetting of certain writing systems
% \babelprovide[import=he, onchar=ids fonts]{hebrew}
% \babelprovide[import=ar, onchar=ids fonts]{arabic}
% \babelprovide[import=sa-Deva, onchar=ids fonts]{sanskrit-devanagari}

% % Define fonts (https://tug.org/FontCatalogue/)
% \babelfont{rm}{Linux Libertine}
% \babelfont{sf}{Linux Biolinum}
% \babelfont{tt}{Inconsolata}

% \babelfont[*arabic]{rm}{Amiri} % Noto Naskh Arabic
% \babelfont[*hebrew]{rm}{Linux Libertine} % Noto Serif Hebrew
% \babelfont[*devanagari]{rm}[Renderer=Harfbuzz]{Noto Serif Devanagari} 
% % Settigs: Scale=MatchUppercase; Scale=MatchLowercase; Scale=1.0; Language=Default

% % East Asian scripts
% \usepackage{kotex} % Support for KR, JP, some TC (not SC).
% % \setmainhangulfont{Noto Serif CJK KR} % Only on Overleaf
% \setmainhangulfont[
%     Path=./fonts/,
%     Extension = .otf,
%     UprightFont=*-Medium,
%     BoldFont=*-Bold
%     ]{NotoSerifKR}

% \newfontfamily{\traditionalchinesefont}[
%     Path=./fonts/,
%     Extension = .otf,
%     UprightFont=*-Medium,
%     BoldFont=*-Bold
%     ]{NotoSerifTC}
% \newfontfamily{\simplifiedchinesefont}[
%     Path=./fonts/,
%     Extension = .otf,
%     UprightFont=*-Medium,
%     BoldFont=*-Bold,
%     ]{NotoSerifSC}

% % Other scripts
% \newfontfamily{\tibetanfont}[Script=Tibetan]{Noto Serif Tibetan}

% % Commands to use scripts
% \newcommand{\bo}[1]{\tibetanfont{#1}\rmfamily}
% \newcommand{\tc}[1]{\traditionalchinesefont{#1}\rmfamily}
% \newcommand{\zh}[1]{\simplifiedchinesefont{#1}\rmfamily}


% Bibliography information processing
\usepackage[
    backend=biber,
    style=apa,
    autocite=inline,
    sorting=nyt,
    sortcites=true,
    backref=false,
    backrefstyle=three,
    abbreviate=true,
    block=space,
]{biblatex}
% \DefineBibliographyStrings{american}{
%     backrefpage={Cited on p.},
%     backrefpages={Cited on pp.}
% }
\defbibheading{bibintoc}[\bibname]{
    \chapter*{#1\markboth{#1}{#1}}
    \addcontentsline{toc}{chapter}{#1}
}
\apptocmd{\sloppy}{\hbadness 10000\relax}{}{}
\appto{\bibsetup}{\sloppy}
\DeclareFieldFormat{apacase}{#1} % Title casing in APA
% \AtBeginBibliography{\small} % Can make the font in bibliography smaller

\addbibresource{../static/bibliography/parti.bib} % Replace with your .bib file

% Bibliography attempts
% \usepackage[
%     style=authoryear,
%     backend=biber,
%     % giveninits=true,
%     isbn=false,
%     ]{biblatex}
% \addbibresource{parti.bib} % Replace with your .bib file

% \usepackage[
%     style=oxyear,
%     backend=biber,
%     isbn=false,
%     url=false,
%     doi=false,
%     giveninits=false,
%     ]{biblatex}
% \addbibresource{parti.bib} % Replace with your .bib file

% % Customize journal entry
% \DeclareFieldFormat
%   [article,inbook,incollection,inproceedings,patent,thesis,unpublished]
%   {title}{\mkbibquote{#1}\addcomma}

% \DeclareFieldFormat
%   [article,inbook,incollection,inproceedings,patent,thesis,unpublished]
%   {journaltitle}{\emph{#1}\addcomma}

% % Remove pp. before pages
% \DeclareFieldFormat[article]{pages}{#1}

% % Customize book entry
% \DeclareFieldFormat
%   [book, article,inbook,incollection,inproceedings,patent,thesis,unpublished]
%   {year}{\mkbibparens{#1}\addspace}

% \DeclareBibliographyDriver{book}{%
%   \printnames{author}%
%   \newunit{\addperiod}\newblock
%   \printfield{year}%
%   \newblock
%   \printfield{title}%
%   \newunit{\addperiod}
%   \printlist{location}%
%   \newunit{\addcolon}
%   \printlist{publisher}%
%   \newunit
%   \finentry}

% % Remove dot after year
% \DeclareDelimFormat[bib]{nametitledelim}{\addspace}



% Keywords command
\providecommand{\keywords}[1]
{
\small	
\noindent\textbf{\textit{Keywords ---}} #1
}

% ORCiD
\definecolor{orcid}{HTML}{A6CE39}
\usepackage{academicons}
\newcommand{\orcid}[1]{\href{https://orcid.org/#1}{\textcolor{orcid}{\aiOrcid}}}