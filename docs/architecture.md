# AWS CloudOps Monitoring and Automation

## 1. Project Purpose

The purpose of this project is to demonstrate AWS CloudOps monitoring, incident detection, alerting, and automation.

## 2. Architecture Flow

1. Amazon EC2 runs a sample workload.
2. Amazon CloudWatch monitors EC2 metrics.
3. A CloudWatch alarm detects a defined threshold breach.
4. AWS Lambda performs a predefined operational action.
5. Amazon SNS sends an email notification to the CloudOps engineer.

## 3. AWS Services

- **Amazon VPC:** Provides network isolation and configuration.
- **AWS IAM:** Controls access using least-privilege permissions.
- **Amazon EC2:** Provides a sample server to monitor.
- **Amazon CloudWatch:** Collects metrics, logs, and alarm information.
- **AWS Lambda:** Runs operational automation.
- **Amazon SNS:** Delivers notifications.
- **Terraform:** Defines infrastructure as code.

## 4. Version Control

Git and GitHub are used to manage source code, documentation, and project changes