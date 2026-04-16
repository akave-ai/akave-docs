---
date: '2025-04-23T22:48:28-05:00'
draft: false
title: 'Akavelink REST API — Reference & Examples'
linkTitle: 'Akavelink API'
description: 'Akavelink REST API reference: endpoints, authentication, bucket and file operations, Docker setup, and JavaScript SDK examples for Akave integration.'
weight: 11
cascade:
  type: docs
schema_json: |
  {
    "@context": "https://schema.org",
    "@type": "HowTo",
    "name": "Get Started with the Akavelink REST API",
    "description": "Set up and call the Akavelink REST API to interact with Akave sovereign cloud storage from any language or environment.",
    "step": [
      { "@type": "HowToStep", "text": "Follow the instructions on this page." }
    ]
  }
---
Welcome to the Akave Link API! This API wrapper enables seamless integration with Akave's decentralized storage network. Below, you’ll find quick setup steps, examples of how to use each API endpoint with JavaScript, and equivalent `curl` commands.

- **GitHub repo for reference:** [https://github.com/akave-ai/akavelink](https://github.com/akave-ai/akavelink)
- **Installing Docker:** [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)


## Getting Started

### Step 1: Pull the Docker Image

To start, pull the Akave Link Docker image:

```bash
docker pull akave/akavelink:latest
```

### Step 2: Get a Wallet Address and Request Funds
- Visit [https://faucet.akave.ai](https://faucet.akave.ai) to obtain a wallet address and add the Akave chain to MetaMask.
- Request funds from the faucet to start experimenting with the Akave Link API.

![Akave Faucet](/images/faucet.gif)

**Blockchain Explorer:** [http://explorer.akave.ai](http://explorer.akave.ai)

### Step 3: Run the Akave Link Container

Run the container and specify the `PRIVATE_KEY` environment variable and the `NODE_ADDRESS` public endpoint.

The Node Address (`NODE_ADDRESS`) is ➔ `connect.akave.ai:5500`

The private key is the private key of an EVM wallet address. For steps on how to access this private key see this example using [Metamask](https://support.metamask.io/configure/accounts/how-to-export-an-accounts-private-key/).

{{< callout type="warning" >}}
  **Always be careful when dealing with your private key. Double-check that you’re hard-coding it anywhere and not committing it to Git.**

  **Remember: Anyone with access to your private key has complete control over your funds.**

  Ensure you’re not reusing a private key that’s been deployed on other EVM chains. Each blockchain has its own attack vectors, and reusing keys across chains exposes you to cross-chain vulnerabilities. Keep separate keys to maintain isolation and protect your assets.
{{< /callout >}}

### Run the Akave Link Docker Container

```bash
docker run -d \
  -p 8000:3000 \
  -e NODE_ADDRESS="public_node_address" \
  -e PRIVATE_KEY="your_private_key" \
  akave/akavelink:latest
```

The API will now be running locally at [http://localhost:8000](http://localhost:8000).


## Setting Up the JavaScript Wrapper

Here's a quick setup to interact with the Akave API using JavaScript:

```javascript
const axios = require('axios');

const API_BASE_URL = 'http://localhost:8000';

async function apiRequest(method, endpoint, data = null) {
  try {
    const response = await axios({
      method,
      url: `${API_BASE_URL}${endpoint}`,
      data,
    });
    console.log(response.data);
  } catch (error) {
    console.error(error.response ? error.response.data : error.message);
  }
}
```

## Example Usage

Each section below demonstrates API calls using this wrapper, alongside the `curl` equivalent.

### Bucket Operations

#### 1. Create a Bucket

Create a new storage bucket.

**JavaScript Example:**

```javascript
apiRequest('POST', '/buckets', { bucketName: 'myBucket' });
```

**curl Command:**

```bash
curl -X POST http://localhost:8000/buckets -H "Content-Type: application/json" -d '{"bucketName": "myBucket"}'
```

#### 2. List Buckets

Retrieve all existing buckets.

**JavaScript Example:**

```javascript
apiRequest('GET', '/buckets');
```

**curl Command:**

```bash
curl -X GET http://localhost:8000/buckets
```

#### 3. View Bucket Details

Retrieve details of a specific bucket.

**JavaScript Example:**

```javascript
apiRequest('GET', '/buckets/myBucket');
```

**curl Command:**

```bash
curl -X GET http://localhost:8000/buckets/myBucket
```

#### 4. Delete a Bucket

Delete a specific bucket.

**JavaScript Example:**

```javascript
apiRequest('DELETE', '/buckets/myBucket');
```

**curl Command:**

```bash
curl -X DELETE http://localhost:8000/buckets/myBucket
```

### File Operations

#### 1. List Files in a Bucket

Retrieve a list of files within a bucket.

**JavaScript Example:**

```javascript
apiRequest('GET', '/buckets/myBucket/files');
```

**curl Command:**

```bash
curl -X GET http://localhost:8000/buckets/myBucket/files
```

#### 2. Get File Info

Fetch metadata about a specific file.

**JavaScript Example:**

```javascript
apiRequest('GET', '/buckets/myBucket/files/myFile.txt');
```

**curl Command:**

```bash
curl -X GET http://localhost:8000/buckets/myBucket/files/myFile.txt
```

#### 3. Upload a File

Upload a file to a bucket.

{{< callout type="info" >}}
 The maximum file size for upload is 5GB. For larger files please use Multipart Uploads with the [Akave O3 API](/akave-o3/multipart-uploads/best-practices-for-large-files/)
{{< /callout >}}

**JavaScript Example (using FormData):**

```javascript
const FormData = require('form-data');
const fs = require('fs');

async function uploadFile(bucketName, filePath) {
  const form = new FormData();
  form.append('file', fs.createReadStream(filePath));
  
  try {
    const response = await axios.post(`${API_BASE_URL}/buckets/${bucketName}/files`, form, {
      headers: form.getHeaders(),
    });
    console.log(response.data);
  } catch (error) {
    console.error(error.response ? error.response.data : error.message);
  }
}

uploadFile('myBucket', './path/to/file.txt');
```

**curl Command:**

```bash
curl -X POST http://localhost:8000/buckets/myBucket/files -F file=@/path/to/file.txt
```

#### 4. Download a File

Download a file from a bucket.

**JavaScript Example:**

```javascript
async function downloadFile(bucketName, fileName, outputDir) {
  const fs = require('fs');
  try {
    const response = await axios.get(`${API_BASE_URL}/buckets/${bucketName}/files/${fileName}/download`, {
      responseType: 'blob',
    });
    console.log(`File downloaded: ${fileName}`);
    fs.writeFileSync(`./${outputDir}/${fileName}`, response.data);
  } catch (error) {
    console.error(error.response ? error.response.data : error.message);
  }
}
```

You can download the file directly in your browser or provide a download URL with a publicly hosted API by using:

```bash
http(s)://ip-or-dns-name/buckets/:BucketName/files/:FileName/download
```

**curl Command:**

```bash
curl -X GET http://localhost:8000/buckets/myBucket/files/myFile.txt/download -o myFile.txt
```
Output file extension should be the same as the requested file.

## Error Handling

All endpoints return errors in the following format:

```json
{
    "success": false,
    "error": "error message"
}
```

Ensure you handle these responses in your code to capture and process errors effectively.