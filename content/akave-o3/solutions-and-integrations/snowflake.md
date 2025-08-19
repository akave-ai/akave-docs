---
date: '2025-06-11T19:23:35-07:00'
draft: false
title: 'Snowflake'
weight: 28
cascade:
  type: docs
---

Akave O3 is a fully S3 compatible decentralized storage solution that integrates seamlessly with Snowflake, allowing you to leverage decentralized storage for your data warehousing needs.

**Below is a short video demo for using Akave O3 with Snowflake:**

{{< youtube jFCd_snG0D0 >}}

## Prerequisites

- **A Snowflake account**
  - Snowflake has all *akave.xyz* endpoints enabled by default starting in the 9.10 release
- **Akave Cloud Credentials**
  - If you do not already have these, please reach out to us for access to [Akave Cloud](https://www.akave.cloud/contact)
- **[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)**
  - Install the AWS CLI using the instructions for your operating system
  - Once successfully installed use the `aws configure` command to set your Akave credentials:
    - **access_key:** Provided by Akave
    - **secret_key:** Provided by Akave
    - **region:** akave-network

> **Note:** All commands pointing to Akave should use one of the custom endpoints listed in the [Akave Environment](/akave-o3/introduction/akave-environment) documentation. 

## Setup Guide

### O3 API

The following section is a quick start guide to using Akave with the AWS CLI for basic Snowflake setup requirements. For more information and usage instructions on using Akave O3, refer to the [Akave O3 documentation](/akave-o3/introduction/what-is-akave-o3).

#### 1. Test that your credentials are valid
Ensure your credentials are valid by listing buckets in your account:

```bash
aws s3api list-buckets \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Expected output:**
> The output should include an empty buckets array if you haven’t created any buckets in Akave yet:
```json
{
    "Buckets": [],
    "Owner": {
        "DisplayName": "ServiceAccount-123...xyz",
        "ID": "abc...789"
    },
    "Prefix": ""
}
```

#### 2. Create a bucket
Then, create a bucket using the AWS CLI and your Akave credentials:

```bash
aws s3 mb s3://my-snowflake-bucket \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Expected output:**
```
make_bucket: my-snowflake-bucket
```

#### 3. Test uploading an object
Finally, test uploading an object to your bucket:
```bash
aws s3 cp ./myfile.txt s3://my-snowflake-bucket/myfile.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Expected output:**
```
upload: ./myfile.txt to s3://my-snowflake-bucket/myfile.txt
```

### Snowflake Configuration

#### 1. Create a stage in Snowflake
Start by creating a stage in your account by running the below command for the bucket you created in the last section:

```sql
CREATE STAGE my_akave_stage
  URL = 's3compat://my-snowflake-bucket/'
  ENDPOINT = 'o3-rc2.akave.xyz'
  CREDENTIALS = (AWS_KEY_ID = '1a2b3c...' AWS_SECRET_KEY = '4x5y6z...')
  DIRECTORY = ( ENABLE = true );
```

**Expected output:**
```
Stage area MY_AKAVE_STAGE successfully created.
```

#### 2. Copy data from Snowflake into Akave

```sql
COPY INTO @my_akave_stage/nation_data/
FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.NATION
FILE_FORMAT = (
  TYPE = CSV
  COMPRESSION = GZIP
  FIELD_OPTIONALLY_ENCLOSED_BY = '"'
);
```

> For this example we use TPCH_SF1.NATION from the SNOWFLAKE_SAMPLE_DATA database, a 4KB table with only 25 rows and 4 columns. 

**Expected output:**
![Snowflake Copy Output](/images/snowflake_copy_output.png)

#### 3. Define a CSV file format
```sql
CREATE OR REPLACE FILE FORMAT my_csv_format
  TYPE = CSV
  COMPRESSION = GZIP
  FIELD_OPTIONALLY_ENCLOSED_BY = '"'
  SKIP_HEADER = 0;
```

**Expected output:**
```
File format MY_CSV_FORMAT successfully created.
```

#### 4. Create an external table in Akave

```sql
CREATE OR REPLACE EXTERNAL TABLE ext_akave_table (
  N_NATIONKEY NUMBER AS (VALUE:c1::NUMBER),
  N_NAME STRING AS (VALUE:c2::STRING),
  N_REGIONKEY NUMBER AS (VALUE:c3::NUMBER),
  N_COMMENT STRING AS (VALUE:c4::STRING)
)
LOCATION = @my_akave_stage/nation_data/
FILE_FORMAT = my_csv_format
PATTERN = '.*\.csv\.gz'
AUTO_REFRESH = FALSE
REFRESH_ON_CREATE = TRUE;
```

> AUTO_REFRESH must be set to false because this feature is not supported for S3 Compatible Storage on Snowflake and without being explicitly set the table will not be created

**Expected Output:**
```
Table EXT_AKAVE_TABLE successfully created.
```

#### 5. Query data directly from Akave's decentralized storage

```sql
SELECT * FROM ext_akave_table;
```

**Expected output:**

![Snowflake Query Output](/images/snowflake_query_output.png)

#### 6. Retrieve data stored in Akave from Snowflake
You can retrieve the data stored in Akave from Snowflake by synchronizing the raw data from your bucket/folder to a directory:

```bash
aws s3 sync s3://my-snowflake-bucket/nation_data ./local-directory \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Expected output:**
```
download: s3://my-snowflake-bucket/nation_data/data_0_0_0.csv.gz to local-directory/data_0_0_0.csv.gz
```

## Links to Additional Resources

Below are some additional resources from Snowflake, AWS, and Akave that may be helpful:

- **Snowflake**
  - [Snowflake S3 compatible storage docs](https://docs.snowflake.com/en/user-guide/data-load-s3-compatible-storage)
- **Akave**
  - [Akave O3 docs](/akave-o3/)
- **AWS**
  - [Installing the CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
