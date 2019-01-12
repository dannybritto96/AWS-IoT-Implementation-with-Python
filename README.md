# Setting up AWS IoT Core to work as message broker and rule engine for you MQTT project with Python and AWS CLI.

Check out more on AWS IoT here https://aws.amazon.com/iot-core/.

Make sure you have Python 3 and PIP installed on your computer.
#### Install AWS CLI using PIP

`
pip3  install awscli
`

Configure your AWS CLI to use your IAM account (https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html ). If you don’t have one already go ahead and create one in the root user account.

#### Create IoT Thing

`
aws iot create-thing –thing-name “TestThing1”
`

##### List things to check if the thing was created successfully.

`
aws iot list-things
`

#### Create Certificates
Now, let’s create certificates for authentication. Be sure to perform this step, or else your AWS IoT Core will exposed to the whole internet.

`
aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile cert.pem --public-key-outfile publicKey.pem --private-key-outfile privkey.pem
`

##### List certificates 

`
aws iot list-certificates
`

> Note the certificateArn value. This will be used later while creating policy.

Download Root certificate. This one is provided by Symantec.

You can download it from here https://www.symantec.com/content/en/us/enterprise/verisign/roots/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem

> Save this file as aws-iot-rootCA.crt

#### Create Policy
Now let’s create policy for this IoT Thing.

Create a JSON file in your current directory. You may call it iotpolicy.json.

Paste the below in your JSON file.

<pre>
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iot:*",
      "Resource": "*"
    }
  ]
}
</pre>

This policy allows all actions from any resource on the thing. For more information on IoT policies head here https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html 

Now to create the policy

`
aws iot create-policy –policy-name “PubSubToAnyTopic” –policy-document file://iotpolicy.json
`

Attach certificate to Policy.

`
aws iot attach-principal-policy –principal <<paste the certificateArn>> --policy-name “PubSubToAnyTopic”
`

Get the end point details using

`
aws iot describe-endpoint
`

> The endpoint URL will be used in the code later.

Now we must attach the generated certificates to the IoT Thing.

`
aws iot attach-thing-principal –thing-name “TestThing1” –principal <<paste certificateArn>>
`

So, now AWS part is setup. All that is left is to modify the code within the script folder to match the thing which we have created now and execute them.
