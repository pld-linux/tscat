Summary:	Simple Filter that adds Timestamps to Stdin
Name:		tscat
Version:	1.0
Release:	0.1
Source0:	http://www.gerg.ca/software/tscat/%{name}-%{version}.tar.gz
# Source0-md5:	1337bd212bbef8f4f9518f1f2d50e088
License:	MIT/X Consortium License
Group:		Applications/Text
URL:		http://www.gerg.ca/software/tscat/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tscat is a simple filter that reads a line from standard input,
prepends a timestamp to each line, and writes to standard output.
Timestamps can be absolute (current time of day), relative to process
start time, or deltas since the previous line (previous timestamp).

%prep
%setup -q

%build
%{__make} \
	PREFIX="%{_prefix}" \
	BIN_DIR="%{_bindir}" \
	MAN_DIR="%{_mandir}/man1" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install tscat $RPM_BUILD_ROOT%{_bindir}/tscat
install tscat.1 $RPM_BUILD_ROOT%{_mandir}/man1/tscat.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/tscat
%doc %{_mandir}/man1/tscat.1*
