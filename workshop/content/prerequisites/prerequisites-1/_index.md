+++
copyright = "Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved."
spdx-license-identifier = "CC-BY-SA-4.0"
title = "Account Setup"
date = 2019-09-09T17:42:10+01:00
weight = 10
+++

## Region selection

Use a single region - **US East (N. Virginia)**, also known as **us-east-1**, for the duration of this workshop.
Please select **US East (N. Virginia)** in the top right corner.

![Step 3](/images/c9-step3.png)

## Starting AWS Cloud9 IDE

[AWS Cloud9][cloud9] is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser. It includes a code editor, debugger, and terminal. Cloud9 comes pre-packaged with essential tools for popular programming languages and the AWS Command Line Interface (CLI) pre-installed so you don’t need to install files or configure your laptop for this workshop. 

Your Cloud9 environment will have access to the same AWS resources as the user with which you logged into the AWS Management Console. We strongly recommend using Cloud9 to complete this workshop.

**Step-by-step Instructions**

1. From the AWS Management Console, Select **Services** then select **Cloud9** under Developer Tools. 

![Step 4](/images/c9-step4.png)

2. Select **Create environment**.

3. Enter `%INITIALS%-wildrydes-webapp-development` into **Name** and optionally provide a **Description**. **:warning:** `%INITIALS%-` means prefixing resource name with participant's initials to avoid resources names clashes with other workshop participants.
For example in the picture below participant *Jan Nowak*, with *jn* initials, creates the Cloud9 environment named `jn-wildrydes-webapp-development`.

![Step 5](/images/c9-step5.png)

4. Select **Next step**.

5. In **Environment settings**:
- Set the *Instance type* to **t2.micro (1 GiB RAM + 1 vCPU)**.
- Choose **training | vpc-0f41a5893958f5b6e** as *Network (VPC)*
- Choose **training-public-a** or **training-public-b** as *Subnet*

![Step 6](/images/c9-step6-b.png)

6. Select **Next step**.

7. Review the environment settings and select **Create environment**. It will take a couple of minutes for your Cloud9 environment to be provisioned and prepared.

## Setting up Cloud9 IDE

1. Once ready, your IDE will open to a welcome screen. Below that, you should see a terminal prompt. Close the Welcome tab and drag up the terminal window to give yourself more space to work in. 

![Step 7](/images/c9-step7.png)

- You can run AWS CLI commands in here just like you would on your local computer. Remember for this workshop to run all commands within the Cloud9 terminal window rather than on your local computer.
- Keep your AWS Cloud9 IDE opened in a browser tab throughout this workshop.

2. Verify that your user is logged in by running the command `aws sts get-caller-identity`. Copy and paste the command into the Cloud9 terminal window. 

```console
aws sts get-caller-identity
```

- You'll see output indicating your account and user information:

```json
{
    "Account": "123456789012",
    "UserId": "AKIAIOSFODNN7EXAMPLE",
    "Arn": "arn:aws:iam::123456789012:user/Alice"
}
```
