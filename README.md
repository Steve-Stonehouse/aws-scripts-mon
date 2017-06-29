# AWS Monitoring Scripts

A package built from the AWS [monitoring scripts] to send statistics to Amazon CloudWatch. The scripts support the following:

  - Memory
  - Swap space
  - Root volume disk usage

Data is aggregated by default to the auto-scaling group the instances are in. This can be changed by editing the cronjob at `/etc/cron.d/aws-scripts-mon`. By default, the following command is run every one minute:

```*/1 * * * * root /opt/aws/aws-scripts-mon/mon-put-instance-data.pl --mem-util --mem-used-incl-cache-buff --mem-used --mem-avail --swap-util --swap-used --disk-path=/ --disk-space-avail --disk-space-util --disk-space-used --auto-scaling=only --from-cron```

## Requirements

In order to send data to Amazon CloudWatch, the instance needs to have an IAM profile attached with the following permissions:

  - `cloudwatch:PutMetricData`
  - `cloudwatch:GetMetricStatistics`
  - `cloudwatch:ListMetrics`
  - `ec2:DescribeTags`

## Installation

This package can be installed using your distro package manager.

   [monitoring scripts]: <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html>
