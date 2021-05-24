+++
title = "Console"

disableToc = true
hidden = true
+++

#### 1. Browse to the Amazon SNS console

In your [Amazon SNS console](https://console.aws.amazon.com/sns/v3/home?#/topics), select **Topic** in the left navigation pane and click the **Create topic** button in the top right corner.

{{%expand "Detailed description" %}}
![Step 1](step-1-console.png)
{{% /expand%}}


#### 2. Create the Ride Completion Topic

Choose **Standard** topic type.
Enter the topic name `%INITIALS%-RideCompletionTopic` and leave the default values. 
Remember to prefix the name with your initials.
Scroll to the bottom of the page and click **Create topic**.

{{%expand "Detailed description" %}}
In the picture below SNS topic name prefix is for sample user *Jan Nowak* with *jn* as initials.
![Step 2](step-2-console.png)
{{% /expand%}}
