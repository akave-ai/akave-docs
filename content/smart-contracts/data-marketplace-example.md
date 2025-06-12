---
date: '2025-06-10T22:51:37-05:00'
draft: true
title: 'Data Marketplace Smart Contract Example'
weight: 24
cascade:
  type: docs
---

Below is an example of how you might use our [data marketplace policy smart contract](https://github.com/akave-ai/policy-guide/blob/main/data-marketplace-policy/contracts/MarketplacePolicy.sol) for time based access to data for a data marketplace application.

For this use case we assume you would like users to pay for access to data in your marketplace, automatically expiring access if payments are not made after one month.

The below example meets the following criteria for use:
- Allows users to charge for their unique data sets on Akave by setting the price for data and subscription length
- Data is only retrievable by the users who paid for it
- Buyers can extend their access to the data (defaults to 30 days)
- If users stop paying to subscribe to the data set they lose access

## Installation

### Requirements

1. **Clone the policy-guide repository**:

```bash
git clone https://github.com/akave-ai/policy-guide.git
cd policy-guide
```
2. **Install Dependencies** (Requirements: Node.js, Hardhat)
  - **Node.js:** For all OS installation instructions visit https://nodejs.org/en/download (LTS Version recommended)
  - **Hardhat:** For all package manager installation instruction visit https://hardhat.org/hardhat-runner/docs/getting-started#installation
  
### Mac OS Node.js install example

If you don't already have Node.js installed you can install it by running:
```sh
brew install node
```

This will install the latest version of Node.js and npm (Node Package Manager), which is bundled with Node.js.

**Verify Installation:** After installation, verify that Node.js and npm were successfully installed by checking their versions:
```sh
node -v
npm -v
```

This should display the installed versions of both Node.js and npm.

#### Important Note on Node Version Compatibility:
Hardhat only supports _even_ versions of Node.js with a release status of: Current, Active LTS or Maintenance. If the latest version of Node.js is currently _odd_ install an _even_ version using the node version manager. See the Troubleshooting section at the bottom for more information on how to resolve

### Hardhat npm install example

Hardhat requires a certain directory structure, which the [akave-ai/policy-guide repository](https://github.com/akave-ai/policy-guide) already holds and can be customized for your use.

For our example today start by moving into the data-marketplace-policy folder

```sh
cd data-marketplace-policy
```
It should contain the following folders and files at this stage (if you don't see these make sure to your version of the repository is up to date using "git pull" from the parent directory, [akave-ai/policy-guide](https://github.com/akave-ai/policy-guide)):
```
data-marketplace-policy/
├── contracts/        # Smart contracts
├── test/             # Test files
├── ignition/         # Deployment automation (Hardhat Ignition)
├── setPrice.ts       # Sets the price of a deployed data marketplace contract
├── .env.example      # Example .env file for using a private key
├── hardhat.config.ts # Hardhat configuration
├── package.json      # Project dependencies
├── tsconfig.json     # TypeScript configuration
├── README.md         # Project documentation
```

To install Hardhat as a development dependency, run the below command from the data-marketplace-policy folder:

```sh
npm install --save-dev hardhat 
```

## Deploy Smart Contracts to localhost

Once the above dependencies have been installed, you can then start a **local Hardhat network** to test that your development environment is set up correctly:

```sh
npx hardhat node
```

This command will spin up a local Ethereum network for testing.

With the Hardhat node running, open a **new terminal window** and execute the following command:

```sh
npx hardhat ignition deploy ./ignition/modules/MarketplacePolicy.ts --network localhost
```

This will deploy the `MarketplacePolicy` contract using [Hardhat Ignition](https://hardhat.org/ignition/docs/getting-started#overview).

#### **Expected Deployment Output**

If everything is set up correctly, the output should look similar to:

```sh
Hardhat Ignition 🚀

Deploying [ MarketplacePolicyModule ]

Batch #1
  Executed MarketplacePolicyModule#MarketplacePolicy
  Executed call: initialize()
  Executed call: setSubscriptionPrice(1 ETH)

[ MarketplacePolicyModule ] successfully deployed 🚀

Deployed Addresses

MarketplacePolicyModule#MarketplacePolicy - 0x5FbDB...
```

The deployed address (`0x5FbDB...`) will be **different each time** you deploy.

After deploying the contract, you can run the test suite to validate its functionality using the below command:

```sh
npx hardhat test
```

or, if you want a more detailed output:

```sh
npx hardhat test --verbose
```

#### **Expected Test Output**

If all tests pass, you should see an output similar to this:

```sh
   MarketplacePolicy
       ✔ Should deploy and check initial state
       ✔ Should allow owner to set subscription price
       ✔ Should allow users to subscribe, verification returns true for subscribed users
       ✔ Should revert if once subscribed user lost access due to subscription expiration
       ✔ Subscription can be prolonged
       ✔ Non-subscribed users do not have access


     6 passing
```

If a test **fails**, the error message will indicate **why** the test didn't pass.

#### **Summary of Deployment & Testing Steps**

To ensure your development environment is configured correctly, make sure that the following commands show their expected output before moving on to deploy contracts to the Akave Network

| **Step**                                            | **Command**                                                                                    | **Expected Output**                                                                                                                                                                                                                                           |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Start Hardhat Node**<br/>[for local testing only] | `npx hardhat node`                                                                             | Hardhat network starts running.                                                                                                                                                                                                                               |
| **Deploy Contract**                                 | `npx hardhat ignition deploy ./ignition/modules/MarketplacePolicy.ts --network localhost` | Contract deployed with its address to local test network. |
| **Run Tests**                                       | `npx hardhat test`                                                                             | All tests should pass (`✓ 6 passing`).                                                                                                                                                                                                                        |

If all the outputs look correct, you're ready to start creating your own smart contracts to use with Akave! 🚀

## Customize and Use Your Data Marketplace Contract

This section surfaces how to change modify and interact with your marketplace contract to so that it's ready to start being used. 

We'll cover how to: 
- Change the number of days a data subscription lasts (before deployment)
- Set the subscription price for your data (after deployment)

### Change the number of days a data subscription lasts
This first step is one that requires modifying your contract before deployment and can be done by simply modifying the line where the duration is defined in the MarketplacePolicy.sol contract.

You may use this static variable change as an example of how to add to or modify other aspects of the contract before deployment.

In your codebase go to contracts/MarketplacePolicy.sol and find where the SUBSCRIPTION_DURATION variable is defined ([line 11](https://github.com/akave-ai/policy-guide/blob/main/data-marketplace-policy/contracts/MarketplacePolicy.sol#L11) if using the contract as defined in the policy-guide repo)

```solidity
uint256 constant SUBSCRIPTION_DURATION = 30 days;
```
`SUBSCRIPTION_DURATION`: Defines the **length of a subscription period** (default is 30 days).

If you'd like to modify the subscription duration simply change the value from 30 days to another time frame. Solidity allows you to use time units like:
- seconds
- minutes
- hours
- days
- weeks

Here, 30 days is automatically converted by the compiler to the equivalent number of seconds (30 * 24 * 60 * 60 = 2,592,000 seconds). Remember that these are **integer** values, so if you want the subscription period to be half a day, you would use 12 hours, **not** 0.5 days

Now that you've updated the contract you can redeploy it using the commands from the **Deploy Smart Contracts to localhost** section above. However you first need to cleanly restart the local hardhat network if it's still runnning. 

- On MacOS you can do this using Ctrl+C, **not** Ctrl+Z which will create a zombie process (see troubleshooting section below for more information). 

Once the existing network has been cleanly exited, start it back up:

```sh
npx hardhat node
```

Then redeploy your modified contract:

```sh
npx hardhat ignition deploy ./ignition/modules/MarketplacePolicy.ts --network localhost
```

#### Optional: Update Tests

If you want to retest the behavior of the contract, the test script will no longer work! This is because it is checking for the default subscription length of **30 days**. 

To test that all the behavior still works as expected after changing the subscription length value, you can update the following sections in [marketplace-policy.test.ts](https://github.com/akave-ai/policy-guide/blob/main/data-marketplace-policy/test/marketplace-policy.test.ts)


**[Should revert if once subscribed user lost access due to subscription expiration](https://github.com/akave-ai/policy-guide/blob/main/data-marketplace-policy/test/marketplace-policy.test.ts#L52)**
- Change the values here to the number of seconds it should take for a user subscription to expire
  - For example if you are using "3 days" as your SUBSCRIPTION_DURATION value you can change this line to the below to represent 4 days

```solidity
await time.increase(60 * 60 * 24 * 4);
```

**[Subscription can be prolonged](https://github.com/akave-ai/policy-guide/blob/main/data-marketplace-policy/test/marketplace-policy.test.ts#L61)**
- Modify the [first time increase](https://github.com/akave-ai/policy-guide/blob/main/data-marketplace-policy/test/marketplace-policy.test.ts#L74) to be just less than 3x your SUBSCRIPTION_DURATION
  - For example if your subscription should expire after 3 days, increase this value to 8 days

```solidity
await time.increase(60 * 60 * 24 * 8);
```

- Also modify the [second time increase ](https://github.com/akave-ai/policy-guide/blob/main/data-marketplace-policy/test/marketplace-policy.test.ts#L82) to make sense with an increased length that **should** expire access
  - In our example 2 days is enough time so that access should expire after 3 subscription durations have been paid

```solidity
await time.increase(60 * 60 * 24 * 2); // 2 days
```

### Set the subscription price for your data

For this step we'll be interacting with our deployed contract! For now you can continue to use the localhost deployment for testing, we'll deploy our contract to the Akave Network in the following section

First, make sure that you have a succesfully deployed Marketplace Policy contract with an address which you can find at the end of the output after the "npx hardhat ignition deploy" command:

```sh
MarketplacePolicyModule#MarketplacePolicy - 0x5FbDB2315678afecb367f032d93F642f64180aa3
```

**Note:** This contract address will change every time you redeploy the contract, so make sure you have the latest one that you want to work with.

Now run setPrice.ts to change the price of your subscription for your deployed contract

```sh
npx hardhat run setPrice.ts --network localhost
```

It requires 2 inputs:
- The contract address from the previous step
- Your new subscription price

If successful the output will return a transaction hash (different every time) and your new subscription price

```solidity
Transaction sent. Hash: 0x3ebf891751e6fd5926f3e49943052049e303a2f277aab1c783dcde4b9218de2b
✅ Subscription price set to: 0.5 ETH
```

## Deploy your contract to Akave 
Now that we've successfully launched and tested our contracts locally it's time to deploy the to Akave!

To start, you’ll need an Akave wallet address. Visit [https://faucet.akave.ai](https://faucet.akave.ai), where you can connect, add the Akave chain to MetaMask, and request funds from the faucet.

![Akave Faucet](/images/faucet.gif)

Now that you have funds in your wallet, export your newly created key. Here is an example for how to do so using MetaMask: 
[How to Export an Accounts Private Key](https://support.metamask.io/configure/accounts/how-to-export-an-accounts-private-key/)

Then, duplicate the .env.example file and add your private key and a valid Akave RPC URL:
```sh
    PRIVATE_KEY="replace-with-your-private-key"
    RPC_URL="akave-rpc-url"
```
For the current testnet you can use this RPC URL for the Akave Network:
https://n1-us.akave.ai/ext/bc/2JMWNmZbYvWcJRPPy1siaDBZaDGTDAaqXoY5UBKh4YrhNFzEce/rpc

Rename the file with your private key to _".env"_

{{< callout type="warning" >}}
  **Always be careful when dealing with your private key. Double-check that you’re not hardcoding it anywhere or committing it to Git. Remember: anyone with access to your private key has complete control over your funds.**

  Ensure you’re not reusing a private key that’s been deployed on other EVM chains. Each blockchain has its own attack vectors, and reusing keys across chains exposes you to cross-chain vulnerabilities. Keep separate keys to maintain isolation and protect your assets.
{{< /callout >}}

Then run the below command to deploy your contract to the Akave network:

```sh
npx hardhat ignition deploy ./ignition/modules/MarketplacePolicy.ts --network akaveNetwork
```

After this you're live! You can visit the [Akave Blockchain Explorer](http://explorer.akave.ai/) and look for transactions from your **public** wallet address. You should see one that looks like this on the Akave Network:

![Explorer Transaction](/images/explorertx.png)

Now when you want to modify the contract, for example to change the price, make sure to use akaveFuji network flag in your commands and ensure your wallet holds enough Akave Tokens to interact with the blockchain (you can always use the [Akave Faucet](https://faucet.akave.ai) to get more.

```sh
npx hardhat run setPrice.ts --network akaveNetwork
```

### Define where your data lives

🚨 TO ADD 🚨


## Troubleshooting
This section contains a list of common errors and details on how to resolve them, although it is **not** comprehensive.

### Incompatible Hardhat and Node Version
- **Commands:** All npx hardhat commands (npx hardhat node, npx hardhat ignition deploy, npx hard test, etc.)
- **Error Message:** WARNING: You are currently using Node.js v23.11.0, which is not supported by Hardhat. This can lead to unexpected behavior. See https://hardhat.org/nodejs-versions
- **Explanation:** This error occurs because Hardhat only supports _even_ versions of Node.js with a release status of: Current, Active LTS or Maintenance. If the latest version of Node.js is currently _odd_ install an _even_ version using the node version manager

#### Resolution Steps
If not already installed, install node version manager using Homebrew:

```sh
brew install nvm
```

Then install an even version of Node.js with a Current, Active LTS or Maintenance status (you can check the status of a version by checking the [nodejs/Release page](https://github.com/nodejs/Release))

```sh
nvm install v22
```

And switch to that version using nvm

```sh
nvm use v22
```

Now when running npx hardhat commands this warning will go away, and your deployment behavior should avoid unneccesary errors.

### Incompatible Hardhat and Node Version
- **Command:** "npx hardhat node"
- **Error Message:** Error: listen EADDRINUSE: address already in use 127.0.0.1:8545
- **Explanation:** This error occurs when the port used by Hardhat (typically 8545) wasn't restarted cleanly and is still holding on to the port.

#### Resolution Steps
First, find what's using the port (8545 in this example):

```sh
lsof -i :8545
```

Example output:

```sh
COMMAND   PID   USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
node    12345  you    22u  IPv4 0x1234567890      0t0  TCP *:8545 (LISTEN)
```

Then kill the process (replace 12345 with the actual number you see under PID in the output above)

```sh
kill -9 12345
```

Now you should be able to relaunch your local ETH test network with Hardhat!
