### This project aims to delete the ec2 instances which are older than 1 day.

# EC2 Auto-Termination Lambda Function

This repository contains an AWS Lambda function written in Python that automatically terminates EC2 instances that have been running for more than **1 minute**. The function is triggered **daily** using a **CloudWatch Event**.

## Overview

- **Functionality**: This Lambda function fetches all EC2 instances in your AWS account and terminates any instance that has been running for more than 1 minute.
- **Trigger**: The function is automatically triggered once a day using a scheduled **CloudWatch Event**.
- **Logs**: Logs are generated in **CloudWatch Logs**, showing which instances were terminated (if any).

## Architecture

1. **Lambda Function**: Contains the Python code to check and terminate EC2 instances.
2. **IAM Role**: Grants the necessary permissions for Lambda to interact with EC2 and CloudWatch.
3. **CloudWatch Event**: Schedules the Lambda function to run daily.

## Prerequisites

1. **AWS Account**: Ensure you have access to an AWS account.
2. **AWS CLI**: (optional) To interact with AWS services from your terminal.
3. **IAM Role**: Create an IAM role with the required permissions for Lambda to terminate EC2 instances.

## Setup Instructions

### 1. Create the IAM Role

Create an IAM role with the following permissions and attach it to the Lambda function.

#### Permissions Policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:TerminateInstances"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}

