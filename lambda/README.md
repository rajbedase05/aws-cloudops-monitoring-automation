# AWS Lambda Automation

## Purpose

AWS Lambda will execute predefined tasks when a CloudWatch alarm detects an infrastructure issue.

## Planned Responsibilities

- Receive an event from a CloudWatch alarm workflow.
- Process the event and record useful information in logs.
- Perform a predefined, safe operational action.
- Support troubleshooting and incident response.

## Security

The Lambda function will use an IAM execution role with only the permissions it requires.

## Testing

The function will be tested with sample events before any production-style