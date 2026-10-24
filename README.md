# AWS CloudOps Monitoring & Automation

## Project Overview

This project aims to demonstrate practical AWS CloudOps workflows for infrastructure monitoring, incident detection, alert notifications, and operational automation.

The goal is to build a documented, version-controlled project using AWS services and Terraform.

## Technologies

- Amazon VPC
- AWS IAM
- AWS Lambda
- Amazon CloudWatch
- Amazon SNS
- Terraform
- Git and GitHub

## Planned Features

- Configure a VPC and security groups
- Apply least-privilege IAM permissions
- Monitor infrastructure using CloudWatch metrics, logs, and alarms
- Use Lambda for predefined operational tasks
- Send incident notifications through SNS
- Define infrastructure using Terraform
- Document configuration, testing, and results

## Architecture

EC2 / AWS Infrastructure → CloudWatch Alarm → AWS Lambda → SNS Notification

## Repository Structure

- `docs/` — Architecture and design documentation
- `lambda/` — Lambda documentation and future function code
- `screenshots/` — Project screenshots and evidence
- `terraform/` — Terraform documentation and future infrastructure code