+++
title = "SAM"
disableToc = true
hidden = true
+++

#### 1. Update the AWS SAM template

In your Cloud9 IDE for this workshop, open the SAM template file `wild-rydes-async-messaging/lab-2/template.yaml`. In the **Resources** section, add the definition for an Amazon SQS queue with the name **CustomerAccountingServiceQueue**, the **CustomerAccountingService** will use to consume messages from. You can find the AWS CloudFormation documentation to do so **[here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-queues.html)**.

{{%expand "Cheat Sheet" %}}
```yaml
  CustomerAccountingServiceQueue:
    Type: AWS::SQS::Queue
```
{{% /expand%}}

The next step, before we can define the subscription, is granting our Amazon SNS topic the permissions to publish messages into this Amazon SQS queue. You can find the AWS CloudFormation documentation to do so **[here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html)**.

{{%expand "Cheat Sheet" %}}
```yaml
  CustomerAccountingServiceQueuePolicy:
      Type: AWS::SQS::QueuePolicy
      Properties:
        Queues:
          - !Ref CustomerAccountingServiceQueue
        PolicyDocument:
          Statement:
            Effect: Allow
            Principal: '*'
            Action: sqs:SendMessage
            Resource: '*'
            Condition:
              ArnEquals:
                aws:SourceArn: !Ref RideCompletionTopic
```
{{% /expand%}}

Now we are ready to create the Amazon SNS subscription for the **CustomerAccountingService**. You can find the AWS CloudFormation documentation to do so **[here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html)**.

{{%expand "Cheat Sheet" %}}
```yaml
  CustomerAccountingServiceQueueToRidesTopicSubscription:
      Type: AWS::SNS::Subscription
      Properties:
        Endpoint: !GetAtt CustomerAccountingServiceQueue.Arn
        Protocol: sqs
        RawMessageDelivery: true
        TopicArn: !Ref RideCompletionTopic
```
{{% /expand%}}

The next step is to attache an AWS IAM policy tou our **CustomerAccountingService** AWS Lambda function, which grants permission to access our previously created Amazon SQS queue, to consume the messages. You can find the AWS SAM documentation to do so **[here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template.html#serverless-sam-template-function)** and **[here](https://github.com/awslabs/serverless-application-model/blob/develop/samtranslator/policy_templates_data/policy_templates.json)**.

{{%expand "Cheat Sheet" %}}
```yaml
      Policies:
        - SQSPollerPolicy:
            QueueName: !Ref CustomerAccountingServiceQueue
```
{{% /expand%}}

Last but not least, we have to declare the **CustomerAccountingServiceQueue** as event source for our **CustomerAccountingService**. You can find the AWS SAM documentation to do so **[here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template.html#serverless-sam-template-function)**.

{{%expand "Cheat Sheet" %}}
```yaml
      Events:
        CustomerAccountingServiceJobQueue:
          Type: SQS
          Properties:
            Queue: !GetAtt CustomerAccountingServiceQueue.Arn
            BatchSize: 1
```
{{% /expand%}}


{{%expand "Detailed description" %}}
![Step 1](step-1-sam.png)

![Step 2](step-2-sam.png)
{{% /expand%}}


#### 2. Deploy the updated AWS SAM template

Run the following command to build the lab again, after we have added the Amazon SQS queue and the Amazon SNS subscription:

{{< highlight bash >}}
cd ~/environment/wild-rydes-async-messaging/lab-2
sam build

{{< /highlight >}}


{{< highlight bash >}}
sam deploy \
    --guided \
    --stack-name %INITIALS-wild-rydes-async-msg-2 \
    --capabilities CAPABILITY_IAM
{{< /highlight >}}

In the meantime while your waiting, you may want to have a look at the AWS SAM template to make yourself familiar with the stack we launched. Just click on the **template.yaml** attachment below to see the content.

Because AWS SAM will only deploy/update/delete resources which are changed, it only takes a couple of seconds to deploy the new Amazon SQS queue and the Amazon SNS subscription.
