Step 1:

Own a domain in AWS Route 53, for example, pplygygrhq.com
https://console.aws.amazon.com/route53/v2/home

Step 1 verify:

$ dig NS pplygygrhq.com.
pplygygrhq.com. 172800 IN    NS  ns-000.awsdns-00.org.
pplygygrhq.com. 172800 IN    NS  ns-000.awsdns-00.co.uk.
pplygygrhq.com. 172800 IN    NS  ns-000.awsdns-00.com.
pplygygrhq.com. 172800 IN    NS  ns-000.awsdns-00.net.

$ aws route53 list-hosted-zones
{
    "HostedZones": [
        {
            "Id": "/hostedzone/XXXXXXXXXXXXXXXXXXXX",
            "Name": "pplygygrhq.com",
            "CallerReference": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "Config": {
                "Comment": "",
                "PrivateZone": false
            },
            "ResourceRecordSetCount": 2
        }
    ]
}

================================

Step 2:

Create new certificate in AWS Certifiicate Manager
https://console.aws.amazon.com/acm/home?region=us-east-1#/wizard/
region = us-east-1 , other region not works
domain name = *.pplygygrhq.com

Step 2 verify:

$ aws acm --region us-east-1 list-certificates
{
    "CertificateSummaryList": [
        {
            "CertificateArn": "arn:aws:acm:us-east-1:999999999999:certificate/ffffffff-ffff-ffff-fffffffffffffffff",
            "DomainName": "*.pplygygrhq.com"
        }
    ]
}

================================

Step 3:

modify src/serverless.yml, line with [BBPMSLSX]

================================

Step 4:

Deploy code to AWS

$ ./aws-deploy.sh

Verify:

$ curl https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/hello
Hello, World!

$ curl https://xxx.pplygygrhq.com/hello
Hello, World!

================================

Step 5:

Test OAuth
(TBA)

================================

Step 6:

Undeploy code from AWS

$ ./aws-undeploy.sh
