+++
title = "Configure AWS Cloud9"
weight = 12
pre = ""
+++

{{% notice note %}}
Ad blockers, javascript disabler, and tracking blockers should be disabled for
the cloud9 domain, or connecting to the workspace might be impacted.
Cloud9 requires third-party-cookies. You can whitelist the [specific domains]( https://docs.aws.amazon.com/cloud9/latest/user-guide/troubleshooting.html#troubleshooting-env-loading).
{{% /notice %}}

### 1. Configure your AWS Cloud9 development environment

In your AWS Cloud9 IDE (find yours by your initials prefix), you can close the welcome tab. Run the following command in the **bash** tab (at the bottom of the IDE):

{{< highlight bash >}}
git clone https://github.com/marcinbelczewski/asynchronous-messaging-workshop.git ~/environment/wild-rydes-async-messaging
mv ~/environment/wild-rydes-async-messaging/code/lab-* ~/environment/wild-rydes-async-messaging
rm -fr ~/environment/wild-rydes-async-messaging/workshop/
rm -fr ~/environment/wild-rydes-async-messaging/code/
{{< /highlight >}}

![Get Started](magic.gif)

**You are now ready to get started!!!**
