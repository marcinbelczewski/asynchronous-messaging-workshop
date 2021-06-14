+++
title = "Clean up"
weight = 38
pre = "8 "
+++

In this step, we will clean up all resources, we created during this lab, so that no further cost will occur.

#### 1. Delete the AWS SAM template

In your Cloud9 IDE, run the following command to delete the resources we created with our AWS SAM template (assuming your have chosen `%INITIALS%-wild-rydes-async-msg-2` as your stack name):

{{< highlight bash >}}
cd ~/environment/wild-rydes-async-messaging/lab-2
aws cloudformation delete-stack \
    --stack-name %INITIALS%-wild-rydes-async-msg-2

{{< /highlight >}}


#### 2. Delete the AWS Lambda created Amazon CloudWatch Log Group

Follow **[this deep link](https://console.aws.amazon.com/cloudwatch/home?#logs:prefix=/aws/lambda/wild-rydes-async-msg-2)** to list all **Amazon CloudWatch Log Groups** with the prefix `/aws/lambda/%INITIALS%-wild-rydes-async-msg-2` (assuming your have chosen `%INITIALS%-wild-rydes-async-msg-2` as your stack name), AWS Lambda created during this lab. Select all the Amazon CloudWatch Log Group one after each other and choose **Delete log group** from the **Actions** menu.

