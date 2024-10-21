### This project aims to delete the ec2 instances which are older than 1 day.

# EC2 Auto-Termination Lambda Function

This repository contains an AWS Lambda function written in Python that automatically terminates EC2 instances that have been running for more than **1 day**. The function is triggered **daily** using a **CloudWatch Event**.

## Overview

- **Functionality**: This Lambda function fetches all EC2 instances in your AWS account and terminates any instance that has been running for more than 1 day.
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
```
### 2. Create the Lambda Function
1. Go to AWS Lambda Console and click Create Function.
2. Choose Author from Scratch.
3. Enter a name for your function .
4. Select Python 3.x as the runtime.
5. Choose the IAM Role you created earlier. Click Create Function.

### 3. Add the Python Code
1. Copy the Python code (lambdaTest.py) into the Lambda function editor.
2. Click Deploy to save the function.

### 4. Create a CloudWatch Event to Trigger the Lambda Daily
1. Go to CloudWatch Console and click Rules under Events.
2. Click Create Rule.
3. Set the Event Source to Schedule.
4. Use the following expression to trigger the function daily at midnight UTC:
   ```
   cron(0 0 * * ? *)
   ```
5. Set the Target to your Lambda function.
6. Give the rule a name. Click Create Rule.

### 5.  Monitor the Logs
1. Go to CloudWatch Logs to monitor the output of the Lambda function. It will log any EC2 instances that were terminated.

## Screenshots

<img width="1317" alt="Screenshot 2024-10-17 at 10 54 07 AM" src="https://github.com/user-attachments/assets/2ed4b462-232f-4583-a193-5fe480c3931c">
<img width="1147" alt="Screenshot 2024-10-17 at 10 44 30 AM" src="https://github.com/user-attachments/assets/5accd13c-f072-4d5d-934a-b1914537d2f9">
<img width="989" alt="Screenshot 2024-10-17 at 10 53 25 AM" src="https://github.com/user-attachments/assets/2952e35e-d5e2-4303-9791-4d92570e48ba">
<img width="1313" alt="Screenshot 2024-10-17 at 10 43 07 AM" src="https://github.com/user-attachments/assets/bed50e51-8852-46c0-bcc4-5f5c3411d7aa">
<img width="1118" alt="Screenshot 2024-10-17 at 10 43 49 AM" src="https://github.com/user-attachments/assets/eea11817-5cc3-4e19-988d-602d9f263821">
