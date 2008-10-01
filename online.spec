### RPM cms online CMSSW_2_1_9_ONLINE1
## IMPORT configurations 

Provides: /bin/zsh
Provides: /bin/ksh
Provides: /bin/sed
Provides: /usr/bin/awk
Provides: /usr/bin/python
Provides: perl(Date::Format)
Provides: perl(Term::ReadKey)
Provides: perl(full)
Provides: perl(LWP::UserAgent)
Provides: perl(Template)

Requires: online-tool-conf python

%define cmssw_release   %(perl -e '$_="%v"; s/_ONLINE1//; print;')
%define cvsprojuc       %(echo %n | sed -e "s|-debug||"| tr 'a-z' 'A-Z')
%define cvsprojlc       %(echo %cvsprojuc | tr 'A-Z' 'a-z')
%define cvsdir          %cvsprojuc
%define cvsserver       %cvsprojlc
%define useCmsTC        1
%define buildtarget     release-build
%define saveDeps        yes

#Defines for file containing list of packages for checkout and build:
%define buildsetrepo    CMSDIST
%define buildsetfile    online_build_set.file
%define buildsetvers    buildset_V2_9

%define patchsrc2	perl -p -i -e ' s!(<classpath.*/test\\+.*>)!!;' config/BuildFile.xml
%define patchsrc3       perl -p -i -e ' s!(<use name=root>)!$1\\n<use name=Foundation/PluginManager>!;' src/DQM/L1TMonitorClient/BuildFile
%define patchsrc4       perl -p -i -e ' s!(<use name=boost>)!$1\\n<use name=EventFilter/Utilities>!;' src/DQM/SiPixelMonitorClient/BuildFile

## IMPORT cms-scram-build
## IMPORT partial-build
## IMPORT scramv1-build
