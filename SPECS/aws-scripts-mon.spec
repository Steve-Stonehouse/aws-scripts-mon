Summary: Amazon CloudWatch Monitoring Scripts for Linux
Name: aws-scripts-mon
Version: 1.0
Release: 1w1%{dist}
License: ASL 2.0
Group: Applications/System
URL: http://aws.amazon.com/code/8720044071969977
Source: aws-scripts-mon-%{version}.zip
Patch: mon-put-instance-data.inode.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: perl(LWP::Protocol::https)
BuildRequires: unzip
BuildArch: noarch

%description
The Amazon CloudWatch Monitoring Scripts for Linux are scripts
for monitoring memory and disk space utilization on Amazon EC2
instances running Linux.

%prep
%setup -q -n aws-scripts-mon
%patch -p0

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}/opt/aws/aws-scripts-mon
%__mkdir_p %{buildroot}/etc/cron.d
%__install -m 755 *.pl %{buildroot}/opt/aws/aws-scripts-mon/
%__install -m 644 *.pm %{buildroot}/opt/aws/aws-scripts-mon/
%__install -m 644 *.cron %{buildroot}/etc/cron.d/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc awscreds.template LICENSE.txt NOTICE.txt
/opt/aws/aws-scripts-mon
/etc/cron.d

%changelog
* Fri May 19 2017 Yonekawa Susumu <yone@webtech.co.jp>
- 1.2.1-1w1

* Tue Apr 26 2016 Yonekawa Susumu <yone@webtech.co.jp>
- 1.1.0-1w1
- add --disk-inode-* options

* Mon Feb 22 2016 Yonekawa Susumu <yone@webtech.co.jp>
- 1.1.0-1
