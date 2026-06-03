---
date: '2026-06-03T00:00:00+02:00'
draft: false
title: 'Change Payment Method'
weight: 1
aliases:
  - /akave-o3/billing/change-payment-method
cascade:
  type: docs
---

Akave Cloud lets you choose how your billing account pays invoices. You can use a saved card or bank payment method for automatic charges, or switch to crypto payments and pay invoices manually.

## Prerequisites

- **Akave Cloud account**
  - Sign in to [Akave Cloud](https://console.akave.ai/).
- **Billing account**
  - Your workspace must have billing enabled.
- **Payment method**
  - To use automatic card or bank payments, add at least one payment method.
  - To use crypto payments, you do not need to add a card.

{{< callout type="info" >}}
Payment methods are managed for the billing account connected to your selected team. If multiple teams share the same billing account, changing the payment method can affect billing for those teams too.
{{< /callout >}}

## Open Payment Method Settings

1. In Akave Cloud, open **Billing** from the sidebar.

![Billing page](/images/gui/billing/payment-method/billing-page.png)

2. **Payment method** section.

The section shows saved cards or bank payment methods and the **Crypto payments** option.

![Payment method section](/images/gui/billing/payment-method/payment-method-section.png)

## Add a Card or Bank Payment Method

1. In **Payment method**, click **Add a new payment method**.

![Add payment method button](/images/gui/billing/payment-method/add-payment-method-button.png)

2. In the payment method modal, enter your card or bank details.

Akave Cloud uses Stripe to securely collect and store payment method details. Akave Cloud does not store full card numbers.

![Add payment method modal](/images/gui/billing/payment-method/add-payment-method.png)

3. Confirm the payment method.

When setup succeeds, Akave Cloud closes the modal and shows a success notification.

![Payment method added notification](/images/gui/billing/payment-method/payment-method-added.png)

4. Confirm that the payment method appears in the **Payment method** list.

![Saved payment method](/images/gui/billing/payment-method/saved-payment-method.png)

{{< callout type="info" >}}
Adding a card or bank payment method does not always make it the active billing method. If crypto payments are selected, choose the saved payment method or enable automatic charges to switch back to card or bank billing.
{{< /callout >}}

## Switch to a Card or Bank Payment Method

Use this flow when you want Akave Cloud to charge a saved card or bank payment method automatically.

1. In **Payment method**, find the saved payment method you want to use.

![Saved payment methods](/images/gui/billing/payment-method/saved-payment-methods.png)

2. Select the payment method.

Akave Cloud marks the selected method as the default payment method.

![Default payment method](/images/gui/billing/payment-method/default-payment-method.png)

3. Make sure **I want to get charged automatically** is selected.

![Automatic charge enabled](/images/gui/billing/payment-method/automatic-charge-enabled.png)

When the update succeeds, Akave Cloud shows a success notification. Future billing periods use the selected default payment method.

{{< callout type="info" >}}
If automatic charges are turned on, Akave Cloud charges the selected payment method each billing period.
{{< /callout >}}

## Switch to Crypto Payments

Use this flow when you want to receive invoices and pay manually with crypto.

1. In **Payment method**, select **Crypto payments**.

![Crypto payments option](/images/gui/billing/payment-method/crypto-payment-option.png)

2. Akave Cloud marks **Crypto payments** as the active payment method.

3. Confirm that **I want to get charged automatically** is turned off.

![Automatic charge disabled](/images/gui/billing/payment-method/automatic-charge-disabled.png)

When the update succeeds, Akave Cloud clears the default card or bank payment method for billing and switches invoices to manual payment.

{{< callout type="info" >}}
Switching to crypto payments does not delete saved card or bank payment methods. You can select a saved payment method later to switch back to automatic card or bank billing.
{{< /callout >}}

## Turn Automatic Charges On or Off

You can also update automatic charges with the checkbox under the payment methods.

### Turn Automatic Charges On

1. Select a saved card or bank payment method.
2. Select **I want to get charged automatically**.

![Turn automatic charges on](/images/gui/billing/payment-method/automatic-charge-enabled.png)

Akave Cloud updates your billing account to use the selected payment method automatically.

### Turn Automatic Charges Off

1. Clear **I want to get charged automatically**.

![Turn automatic charges off](/images/gui/billing/payment-method/automatic-charge-disabled.png)

Akave Cloud changes invoices to manual collection.

{{< callout type="info" >}}
Turning automatic charges off with the checkbox changes invoice collection, but it does not delete saved payment methods.
{{< /callout >}}

## Remove a Saved Payment Method

1. In **Payment method**, find the saved card or bank payment method you want to remove.

2. Click the remove action.

![Payment method actions](/images/gui/billing/payment-method/payment-method-remove-button.png)

3. In the confirmation modal, click **Yes, I am sure**.

![Remove payment method modal](/images/gui/billing/payment-method/remove-payment-method-modal.png)

When removal succeeds, Akave Cloud shows a success notification and removes the payment method from the list.

![Payment method removed notification](/images/gui/billing/payment-method/payment-method-removed.png)

{{< callout type="info" >}}
Akave Cloud requires at least one saved payment method to remain when you are using card or bank billing. If you want to stop using card or bank billing, switch to **Crypto payments** instead.
{{< /callout >}}

## Next Steps

After changing your payment method, you can:

- Review your current usage in **Billing**.
- Download invoices from **Payment history**.
- Add another payment method for backup billing.
- Contact support if you need another email added to your billing account.

{{< callout type="info" >}}
For billing account changes that are not available in Akave Cloud, contact [support@akave.io](mailto:support@akave.io).
{{< /callout >}}
