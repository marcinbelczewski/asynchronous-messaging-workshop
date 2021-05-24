+++
title = "SAM"

disableToc = true
hidden = true
+++

#### 1. Update the AWS SAM template

In your Cloud9 IDE for this workshop, open the SAM template file `wild-rydes-async-messaging/lab-2/template.yaml`. In the **Resources** section, add the definition for an Amazon SNS topic with the name `%INITIALS%-RideCompletionTopic`. Remember to prefix the topic name with your initials. You can find the AWS CloudFormation documentation to do so **[here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html)**.

{{%expand "Cheat Sheet" %}}
```
  RideCompletionTopic:
    Type: AWS::SNS::Topic
```
{{% /expand%}}

{{%expand "Detailed description" %}}
In the picture below, SNS topic name prefix is for sample user *Jan Nowak* with *jn* as initials.
![Step 1](step-1-sam.png)
{{% /expand%}}


#### 2. Deploy the updated AWS SAM template

Run the following command to build the lab again, after we have added the Amazon SNS topic:

{{< highlight bash >}}
cd ~/environment/wild-rydes-async-messaging/lab-2
sam build

{{< /highlight >}}


Now we are ready to update the application, by running the following command to deploy the change. Remember about your initials prefix in CloudFormation stack name:  

{{< highlight bash >}}
sam deploy \
    --guided \
    --stack-name %INITIALS%-wild-rydes-async-msg-2 \
    --capabilities CAPABILITY_IAM    
{{< /highlight >}}

In the meantime while your waiting, you may want to have a look at the AWS SAM template to make yourself familiar with the stack we launched. Just click on the **template.yaml** attachment below to see the content.

Because AWS SAM will only deploy/update/delete resources which are changed, it only takes a couple of seconds to deploy the new Amazon SNS topic.
