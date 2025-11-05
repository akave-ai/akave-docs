---
date: '2025-04-23T22:48:28-05:00'
draft: false
title: 'Hugging Face'
weight: 32
cascade:
  type: docs
---

[Hugging Face](https://huggingface.co/) is a community based platform for machine learning and deep learning models. It allows you to easily access and share AI datasets, load a dataset in a single line of code, and use powerful data processing and streaming methods to quickly get your dataset ready for training a deep learning model.

[Hugging Face Datasets](https://huggingface.co/docs/datasets/en/index) is a library that allows you to store, version, and access ML datasets with Hugging Face and Akave storage.

## Prerequisites

- **Akave Cloud Credentials**  
These can be requested by contacting Akave at [Akave Cloud Contact](https://www.akave.cloud/contact).

- **Install dependencies** (Requirements: Python 3.9+, pip, s3fs, Hugging Face: datasets)


## Installation

{{< callout type="info" >}}
**Note on Python commands:** Throughout this guide, we provide commands for default Python 3 installations  using `python` and `pip`. For systems where you need to explicitly specify Python 3 you may need to use `python3` and `pip3`. Use the command variation that works for your specific environment.
{{< /callout >}}

### Pip Installation Instructions

Pip comes pre-installed with Python 3.4 and later. If you don't already have Python installed, you can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

You can verify that pip is installed by running the following command:

```bash
pip --version
```

### Hugging Face Datsets Installation Instructions
For detailed datasets installation instructions go to [https://huggingface.co/docs/datasets/installation](https://huggingface.co/docs/datasets/installation)

The simplest way to install the Hugging Face datasets library is to use pip, which can also be used to install s3fs:

```bash
pip install s3fs datasets
```

Run the following command to verify datasets was installed and is working as expected:

```bash
python -c "from datasets import load_dataset; print(load_dataset('rajpurkar/squad', split='train')[0])"
```

Expected Output:
```bash
{'answers': {'answer_start': [515], 'text': ['Saint Bernadette Soubirous']}, 'context': 'Architecturally, the school has a Catholic character. Atop the Main Building\'s gold dome is a golden statue of the Virgin Mary. Immediately in front of the Main Building and facing it, is a copper statue of Christ with arms upraised with the legend "Venite Ad Me Omnes". Next to the Main Building is the Basilica of the Sacred Heart. Immediately behind the basilica is the Grotto, a Marian place of prayer and reflection. It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858. At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary.', 'id': '5733be284776f41900661182', 'question': 'To whom did the Virgin Mary allegedly appear in 1858 in Lourdes France?', 'title': 'University_of_Notre_Dame'}
```

Run the following command to verify s3fs installation:

```bash
pip show s3fs
```

## Usage

The below usage example has simple examples for how to use Hugging Face datasets with Akave O3 storage by using [S3FS](https://s3fs.readthedocs.io/en/latest/). 

Helper scripts have also been created to make it easier to use Hugging Face datasets and S3FS with Akave O3 storage, as well to test the connection to your Akave O3 storage. Both of these scripts can be found in the [configuration](#configuration) section below.


For more information on S3FS usage with Akave see the [S3FS](/akave-o3/solutions-and-integrations/s3fs) Akave O3 documentation.

### Configuration

Start by downloading the helper scripts below by copy/pasting each of them into new `.py` files in your working directory with the same name:

- **[huggingface_s3.py](/huggingface_s3.py)**

- **[huggingface_test.py](/huggingface_test.py)**


Then create a `.env` file in the same directory as your scripts with the following contents:

```
AKAVE_ACCESS_KEY=your_access_key
AKAVE_SECRET_KEY=your_secret_key
AKAVE_ENDPOINT_URL=https://o3-rc2.akave.xyz
AKAVE_BUCKET_NAME=your-bucket-name
```

{{< callout type="info" >}}
**Note:** Make sure to use the endpoint URL for your specific instance and replace the other values with your access key, secret key, and the name of a bucket you've created with those credentials.
{{< /callout >}}


Your directory should now look something like this:

```
.
├── huggingface_s3.py
├── huggingface_test.py
└── .env
```

### Working with Datasets

The `huggingface_s3.py` helper script provides a `HuggingFaceS3` class that simplifies working with Hugging Face datasets on Akave O3 storage. All examples below assume you've initialized the client:

```python
from huggingface_s3 import HuggingFaceS3

hf_s3 = HuggingFaceS3()
```

#### List Available Buckets

The `list_buckets()` method returns all S3 buckets accessible with your credentials. This is useful for verifying your connection and exploring available storage locations.

```python
buckets = hf_s3.list_buckets()
print(buckets)
```

#### Transfer an Existing Hugging Face Dataset to Akave O3

The `transfer_dataset()` method downloads a dataset from the [Hugging Face Hub](https://huggingface.co/datasets) and transfers it directly to your Akave O3 bucket. This is useful when you want to store public datasets in your own storage for faster access or offline use.

**Parameters:**
- `dataset_name` (required): The name of the dataset on [Hugging Face Hub](https://huggingface.co/datasets) (e.g., "mnist", "imdb")
- `output_path` (optional): Custom path within your bucket. Defaults to the dataset name
- `file_format` (optional): Storage format for the dataset. Defaults to "parquet"

**Basic usage:**

```python
output_dir = hf_s3.transfer_dataset("mnist")
```

**Custom path and format:**

```python
output_dir = hf_s3.transfer_dataset("imdb", output_path="text/imdb_dataset")
output_dir = hf_s3.transfer_dataset("squad", file_format="arrow")
```

#### Save a Dataset to Akave O3

The `save_dataset()` method saves any Hugging Face dataset object to your Akave O3 bucket. This is particularly useful after you've processed or transformed a dataset and want to persist the changes.

**Parameters:**
- `dataset` (required): The Hugging Face dataset object to save
- `output_path` (optional): Path within your bucket where the dataset will be stored

**Example workflow:**

```python
from datasets import load_dataset

dataset = load_dataset("imdb", split="train")
save_path = hf_s3.save_dataset(dataset, output_path="processed/imdb_train")
```

#### Load a Dataset from Akave O3

The `load_dataset()` method retrieves a previously saved dataset from your Akave O3 bucket. It returns a standard Hugging Face dataset object that you can use for training, analysis, or further processing.

**Parameters:**
- `path` (required): Path within your bucket where the dataset is stored

**Usage:**

```python
dataset = hf_s3.load_dataset(path="imdb")
print(f"Dataset has {len(dataset)} examples")
print(dataset[0])
```

### Testing

The included `test_huggingface_s3.py` script provides a set of example tests to verify that the Hugging Face S3 integration is working correctly.

There are 7 tests in total:

1. **Custom Dataset** - Creates a custom dataset and saves it to Akave O3.

2. **Dataset Transformations** - Demonstrates how to transform a dataset before saving it to Akave O3.

3. **Transfer MNIST** - Transfers the MNIST dataset to Akave O3.

4. **Dataset Streaming** - Demonstrates how to stream a dataset from Akave O3.

5. **Dataset Versioning** - Demonstrates how to version a dataset.

6. **Dataset Formats** - Demonstrates how to save a dataset in different formats.

7. **Create & Save Dataset** - Demonstrates how to create and save a dataset to Akave O3.
  
To run the tests, use the following command:

```bash
python test_huggingface_s3.py
```

If all tests pass, you should see a message similar to the below at the end of the output:

```bash
=== Test Summary ===
Example 1: Custom Dataset: ✅ Passed
Example 2: Dataset Transformations: ✅ Passed
Example 3: Transfer MNIST: ✅ Passed
Example 4: Dataset Streaming: ✅ Passed
Example 5: Dataset Versioning: ✅ Passed
Example 6: Dataset Formats: ✅ Passed
Example 7: Create & Save Dataset: ✅ Passed
```
