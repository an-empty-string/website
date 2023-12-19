---
title: Using CloudFormation to create Athena tables
posted_on: 2022-11-07
---

## Background

If you use [Amazon Athena](https://aws.amazon.com/athena/) to query data stored in [Amazon S3](https://aws.amazon.com/s3/) (for example, log files, or large datasets used for analysis), you may find yourself wanting to version-control table definitions using [AWS CloudFormation](https://aws.amazon.com/cloudformation/). Since Athena uses the [AWS Glue](https://aws.amazon.com/glue/) data catalog underneath, you can create [Glue tables](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html) to populate your Athena databases.

(You should note that, with a bit of effort, you can likely adapt this information to e.g. [Terraform's Glue table resource](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/glue_catalog_table).)

## Simple example

Using the [CloudFront Logs example](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) table, here's a resource definition suitable for a CloudFormation YAML template:

```yaml
CloudfrontLogsTable:
  Type: "AWS::Glue::Table"
  Properties:
    CatalogId: !Ref "AWS::AccountId"
    DatabaseName: default
    TableInput:
      Name: cloudfront_logs
      TableType: EXTERNAL_TABLE
      StorageDescriptor:
        Location: "s3://athena-examples-us-east-1/cloudfront/plaintext/"
        StoredAsSubDirectories: true

        InputFormat: org.apache.hadoop.mapred.TextInputFormat
        OutputFormat: IgnoreKeyTextOutputFormat

        SerdeInfo:
          SerializationLibrary: org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe
          Parameters:
            field.delim: "\t"
            serialization.format: "\t"

        Columns:
          - Name: Date
            Type: date
          - Name: Time
            Type: string
          - Name: Location
            Type: string
          - Name: Bytes
            Type: int
          - Name: RequestIP
            Type: string
          - Name: Method
            Type: string
          - Name: Host
            Type: string
          - Name: Uri
            Type: string
          - Name: Status
            Type: int
          - Name: Referrer
            Type: string
          - Name: ClientInfo
            Type: string
```

## Defining partition projection

[Partition projection](https://docs.aws.amazon.com/athena/latest/ug/partition-projection.html) is supported here too. For example, on a CloudTrail logs table with partition projection:

```yaml
CloudtrailLogsTable:
  Properties:
    TableInput:
      Parameters:
        projection.enabled: "true"
        projection.timestamp.type: "date"
        projection.timestamp.format: "yyyy/MM/dd"
        projection.timestamp.interval: "1"
        projection.timestamp.interval.unit: "DAYS"
        projection.awsregion.type: "enum"
        projection.awsregion.values: "us-east-1,us-east-2"
        storage.location.template: !Sub "s3://my-cloudtrail-logs/AWSLogs/${AWS::AccountId}/CloudTrail/${!awsregion}/${!timestamp}"

      PartitionKeys:
        - Name: awsregion
          Type: string

        - Name: timestamp
          Type: string
```
