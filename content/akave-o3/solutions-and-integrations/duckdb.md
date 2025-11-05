---
date: '2025-06-24T22:07:18-07:00'
draft: false
title: 'DuckDB'
weight: 26
cascade:
  type: docs
---

[DuckDB](https://duckdb.org/) is an in-memory, SQL query engine that enables data analytics directly on data stored in Akave.

## Pre-requisites

1. **Akave O3 Credentials**
These can be requested by contacting Akave at [Akave Cloud Contact](https://www.akave.cloud/contact).

2. **Install dependencies** (Requirements: DuckDB)

### DuckDB Installation Guide
For all latest OS installation instructions go to [https://duckdb.org/docs/installation/](https://duckdb.org/docs/installation/)

#### Mac OS DuckDB install example

**If you don’t already have DuckDB installed, you can add it with:**
```bash
brew install duckdb
```
**If DuckDB is installed and you need to upgrade it use:**
```bash
brew upgrade duckdb
```
**After installing or upgrading, confirm it's installed using:**
```bash
duckdb --version
```

#### Linux DuckDB install example

**DuckDB has a simple install script that will install the latest version of duckdb.**

```bash
curl https://install.duckdb.org | sh
```

**After installing or upgrading, confirm it's installed using:**
```bash
duckdb --version
```

## Configuration
Configure DuckDB to use Akave's S3 compatible API, Akave O3. For more information on DuckDB S3 configuration, see [DuckDB S3 API Support](https://duckdb.org/docs/stable/core_extensions/httpfs/s3api).

### Akave O3 Configuration

1. **Open the DuckDB CLI by running the following command in your terminal:**
```bash
duckdb
```
> **Note:** Running DuckDB without a database file will cause the session to be reset every time you close the CLI. Run the command with a database name such as `duckdb mydatabase.duckdb` when launching DuckDB to create or open a persistent database which will be stored locally in the active directory.

2. **To load a Parquet file from S3, the httpfs extension is required. This can be installed using the INSTALL SQL command:**
```sql
INSTALL httpfs;
```
> This only needs to be run once.

3. **Load the httpfs extension using:**
```sql
LOAD httpfs;
```

4. **Define the credentials, region, and endpoint:**
```sql
CREATE OR REPLACE PERSISTENT SECRET akave_secret (
    TYPE s3,
    PROVIDER config,
    KEY_ID '<your-access-key>',
    SECRET '<your-secret-key>',
    REGION 'akave-network',
    ENDPOINT 'o3-rc2.akave.xyz'
);
```
- Select the endpoint corresponding to your credentials from the options provided here: [Akave Environment](/akave-o3/introduction/akave-environment)
  - **Note:** Make sure to exclude `https://` from the endpoint as DuckDB automatically adds it
- Secrets are not saved between sessions by default. The `PERSISTENT` flag will save the secret between sessions. For more information on managing secrets within DuckDB see [Secrets Manager](https://duckdb.org/docs/stable/configuration/secrets_manager.html)

### (Optional) Attach Akave as a database

If you have an existing DuckDB database, you can attach Akave as a database.

First, move the database file into an Akave bucket. In this example using the AWS CLI:
```bash
aws s3 cp database.duckdb s3://bucket/database.duckdb \
  --endpoint-url https://o3-rc2.akave.xyz
```
> For more information on object management using the AWS CLI with Akave see [Upload, Download, Delete Objects](/akave-o3/object-management/upload-download-delete-objects).

Then, attach the .duckdb file as a database:
```sql
ATTACH 's3://bucket/database.duckdb' AS akave;
```

This will allow you to query Akave as a database using the following command:
```sql
SELECT * FROM akave.table_name;
```
> Here `table_name` is the name of an existing table within the .duckdb database.

## Query Examples
{{< callout type="info" >}}
Akave currently supports a read only connection with DuckDB.
{{< /callout >}}

- **Read files from Akave using the following command:**
```sql
SELECT * FROM 's3://bucket/file.extension';
```
> DuckDB supports csv, parquet, xlsx, and json files though it is recommended to use parquet for performance.

- **Read parquet files from Akave using the following command:**
```sql
SELECT * FROM read_parquet('s3://bucket/file.parquet');
```
> The Parquet file will be processed in parallel. Filters will be automatically pushed down into the Parquet scan, and only the relevant columns will be read automatically.

- **Read multiple parquet files at once:**
```sql
SELECT *
  FROM read_parquet([ 
  's3://bucket/file1.parquet',
  's3://bucket/file2.parquet'
  ]);
```

- **Read from all files with a .parquet extension:**
```sql
SELECT *
FROM read_parquet('s3://bucket/*.parquet');
```

### Partial Reading

DuckDB also supports partial reading of parquet files which allows:

- **Counting the number of rows in a parquet file**
```sql
SELECT count(*)
FROM 's3://bucket/file.parquet';
```

- **Selecting specific columns**
```sql
SELECT column1, column2
FROM 's3://bucket/file.parquet';
```
