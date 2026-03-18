---
date: '2025-06-11T19:23:35-07:00'
draft: false
title: 'Acronis'
weight: 25
cascade:
  type: docs
---

[Acronis](https://www.acronis.com/) is a backup and recovery solution that can integrate with Akave storage for secure data protection. 

## Prerequisites

- **Acronis Account**
  - If you do not already have an Acronis account, please create one at [Acronis](https://www.acronis.com/)
- **Akave Cloud Credentials**
  - If you do not already have these, please create them on [Akave Cloud](https://console.akave.com/)
- **AWS Account (for Backup Gateway option)**
  - User must have access to the AWS Marketplace and EC2, sign up at [aws.amazon.com](https://aws.amazon.com/)

## Acronis Setup

To get started with Akave and Acronis, make sure you have access to your Akave:
- Access Key ID
- Secret Access Key
- Endpoint URL

As well as a bucket in Akave to store your data. More information on how to create a bucket can be found in the [Bucket Management](/akave-o3/bucket-management/create-list-delete-buckets/) section of these docs.

Akave O3 can be used with Acronis in two common ways:

- **Acronis Cyber Protect Cloud**: Configure an S3-compatible backup location directly in the Acronis SaaS console.
- **Acronis Cyber Infrastructure (Backup Gateway)**: Run an Acronis-managed gateway (for example via AWS Marketplace) that exposes S3-compatible storage configuration through a self-managed service.

In both cases, you'll use your Akave S3-compatible credentials (access key, secret key, and endpoint) and an Akave bucket. If you need to validate your Akave bucket and credentials first, reference the other S3-compatible integrations in this folder (for example [Snowflake](/akave-o3/solutions-and-integrations/snowflake/) and [S3FS](/akave-o3/solutions-and-integrations/s3fs/)).

### Acronis Cyber Protect Cloud

This option is best when you want the simplest setup and prefer a fully managed Acronis control plane.

1. Create an account for [Acronis Cyber Protect](https://www.acronis.com/en/products/cyber-protect/components/).
2. Use the Acronis console to set up a Management Agent on the device you want to back up by going to **Devices** → **Add** then select the device you want to backup from and follow the installation instructions provided.

![Acronis Add](/images/acronis_add.png)
![Acronis Add 2](/images/acronis_add2.png)

3. In the [Acronis console](https://us-cloud.acronis.com/ui/#/), add Akave as an S3-compatible backup location:
   1. Go to **Backup Storage** → **Backups** → **Locations** → **Add location** → **Public Cloud** → **S3 Compatible**
   
![Acronis Menu](/images/acronis_menu.png)
![Acronis Menu 2](/images/acronis_menu2.png)

4. Click "Connect" and enter your Akave credentials:
   - Endpoint URL
   - Access Key ID
   - Secret Access Key
   - Select the "AuthV4" authentication protocol

**Note**: In the menu below, the "Management Agent" option is the device you set up in Step 2.

![Acronis Configuration](/images/acronis_config.png)

Then select the bucket you would like to use for backups (you should have already created this bucket using the same credentials used above).

![Acronis Configuration 2](/images/acronis_config2.png)

5. Once you have installed the Management Agent, you can create a backup plan for the device by selecting the device from the console then selecting **Protect** → **Create Plan** → **Protection** and then configuring the backup settings as needed. Just make sure to select "S3 compatible location" which you set up in the previous steps for the "Where to back up" option. 

![Acronis Plan](/images/acronis_plan.png)

6. You can now run backups and restore data as needed. To test that the backup is working correctly, select "Run now" on the backup plan you created in the last step.

![Acronis Run](/images/acronis_run.png)

You should see a folder similar to the following in the bucket you selected for your backups:

![Acronis Backup](/images/acronis_backup.png)

This directory contains the backup data for your device stored in a binary format Acronis uses to reconstruct the backup.

### Acronis Cyber Infrastructure (Backup Gateway)

This option is best when you want a dedicated gateway you control (deployment region, networking/VPC, instance sizing) while still using Akave for the underlying S3-compatible storage target.

**Note:** Acronis has a [reference guide](https://dl.acronis.com/u/software-defined/html/AcronisCyberInfrastructure_5_4_abgw_quick_start_guide_for_amazon_s3_ec2_en-US/) for using Amazon S3 storage with Acronis Backup Gateway deployed on EC2. The Akave setup is similar and requires a minor configuration change in the "[Setting up Backup Gateway](https://dl.acronis.com/u/software-defined/html/AcronisCyberInfrastructure_5_4_abgw_quick_start_guide_for_amazon_s3_ec2_en-US/#setting-up-backup-gateway.html)" section, and the below instructions closely follow their setup process.


#### Launching the Gateway

1. From AWS Marketplace, open **Acronis Backup Gateway**:
   - https://us-east-1.console.aws.amazon.com/marketplace/search/listing/prodview-3m6req74uapzo/procurement/procure/?productId=4d1b528c-1949-405d-9bc7-b6a4aea266a4&redirectUrl=%2Fmarketplace%2Fsearch%2Flisting%2Fprodview-3m6req74uapzo
2. Subscribe to the software (free) and launch the software using the "Launch your software" button.

For the instance configuration select the following options:
- **Service**: Amazon EC2
- **Launch Method**: One-click launch from AWS Marketplace
- **Version**: Latest stable
- **Region**: Preferred region (example: `US East (N. Virginia)`)
- **Instances**: 1
- **Instance type**: `t2.large`
- Choose a VPC, subnet, security group, and key pair. Instructions for creating these can be found in the AWS documentation:
  - [Creating a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html)
  - [Creating a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html)
  - [Creating a security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-security-group.html)
  - [Creating a key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html)

![Acronis Launch](/images/acronis_launch.png)

You're now ready to launch the instance!

#### Connecting to the Gateway

1. After launching, you'll see the button which says "View instance on EC2" which you can click to view the instance in a new tab, and then click "Connect" to view the various connection instructions.

First click "View instance on EC2":
![Acronis Launch 2](/images/acronis_launch2.png)

Then click "Connect":
![Acronis Launch 3](/images/acronis_launch3.png)

We'll be connecting to the instance using SSH and the key file created in the previous step (e.g., `name.pem`):

```bash
chmod 400 name.pem
ssh -i "name.pem" cloud-user@ec2-54-237-90-228.compute-1.amazonaws.com
```

{{< callout type="info" >}}
Make sure to replace `name.pem` with the name of your key file and `ec2-54-237-90-228.compute-1.amazonaws.com` with the public DNS of your EC2 instance. This public DNS will be different **each time** an instance is launched.
{{< /callout >}}

2. Once you've successfully connected to your instance, retrieve the initial admin password:

```bash
cat /.initial-admin-password
```

3. Login to the web portal using the password from the previous step and the `8888` port for your instance.
   - Example: `https://ec2-54-237-90-228.compute-1.amazonaws.com:8888/`
   - **username:** `admin`
   - **password:** value from `/.initial-admin-password`

![Acronis Login](/images/acronis_login.png)

#### Configuring the Gateway

Create and configure the Backup Gateway:

   1. Go to **Infrastructure** → **Networks** and ensure the network(s) you will use include:
      - **ABGW private** traffic type
      - **ABGW public** traffic type
   ![Acronis 1](/images/acronis_1.png)
   2. In the left sidebar, click **Storage services** → **Backup storage**, then click **Create Backup Storage**.
   ![Acronis 2](/images/acronis_2.png)
   3. Select **Public Cloud** as the storage type.
   ![Acronis 3](/images/acronis_3.png)
   4. Select the node(s) that will run the gateway services, then click **Next**.
   ![Acronis 4](/images/acronis_4.png)
   5. On the **Public cloud** page, select **AuthV4 compatible (S3)** and fill out the S3 parameters using your Akave:
      - Endpoint URL
      - Region
      - Bucket name
      - Access Key ID
      - Secret Access Key
   ![Acronis 5](/images/acronis_5.png)
   6. On **Storage policy**, leave defaults unless you have specific redundancy requirements.
   ![Acronis 6](/images/acronis_6.png)
   7. On **DNS configuration**, add the domain name you want to use for the gateway (e.g., `backup.example.com`) and make sure it has a DNS record pointing to the gateway IP address.
   ![Acronis 7](/images/acronis_7.png)
   8. On **Acronis account**, enter the URL of the cloud management portal (e.g., `https://cloud.acronis.com`), or the hostname/IP address and port of the local management server (e.g., `http://192.168.1.2:9877`) along with your credentials.
   ![Acronis 8](/images/acronis_8.png)
   9. Review the configuration and click **Create** to finalize the gateway setup.
   ![Acronis 9](/images/acronis_9.png)

<!-- #### Using the Gateway

Once the Backup Gateway is configured and connected to Akave storage, you can use it with Acronis Cyber Backup to perform backups and restores.

1. **Register backup agents**: Install Acronis Cyber Backup agents on the machines you want to protect. During installation or configuration, point them to the Backup Gateway you just created.

2. **Create backup plans**: In your Acronis management console (either Acronis Cyber Backup Cloud or a local management server), create backup plans that target the gateway storage location.
   - Select the machines/resources to back up
   - Configure backup schedule and retention policies
   - Choose the Backup Gateway as the destination

3. **Run backups**: Execute backup jobs according to your configured schedule or run them manually. The data will be sent to the Backup Gateway, which will then store it in your Akave bucket.

4. **Monitor and verify**: Check the Acronis console to verify backups are completing successfully. You can also verify the backup data in your Akave bucket using the AWS CLI:

```bash
aws s3 ls s3://your-bucket-name/ \
  --endpoint-url <YOUR_ENDPOINT_URL> \
  --recursive
```

5. **Restore data**: When needed, use the Acronis console to restore files, folders, or entire systems from the backups stored in Akave through the gateway.

{{< callout type="info" >}}
The Backup Gateway acts as a bridge between Acronis Cyber Backup and Akave storage, handling data transfer, deduplication, and compression. All backup data is stored in your Akave bucket in Acronis's proprietary format.
{{< /callout >}}

For detailed information on using Acronis Cyber Backup with the gateway, refer to the [Acronis Cyber Backup documentation](https://www.acronis.com/en-us/support/documentation/BackupService/). -->
