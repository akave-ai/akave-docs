---
date: '2025-06-10T22:51:37-05:00'
draft: false
title: 'Service Level Agreement (SLA)'
weight: 23
cascade:
  type: docs
---

**Policy Date:** 04/16/2025  
**Version:** 1.0

This Akave Service Level Agreement (**"SLA"**) governs the use of Akave's decentralized storage services and applies separately to each customer account. In the event of a conflict between this SLA and the Akave Terms of Service or other governing agreement, this SLA controls solely with respect to such conflict.

Capitalized terms not defined herein will have the meanings assigned to them in the Akave Terms of Service.

## 1. Service Commitment

Akave will use commercially reasonable efforts to ensure:

* A Monthly Uptime Percentage of at least 99.9%, and
* A data durability level of 99.999999999% (11 nines) on an annual basis.

If Akave fails to meet this Service Commitment in a given monthly billing cycle, you may be eligible to receive a **Service Credit**, as described below.

## 2. Definitions

### 2.1. Monthly Uptime Percentage

The percentage of 5-minute intervals in a given monthly billing cycle during which the Akave service was operational and available to the customer. A 5-minute interval is considered unavailable if all requests during that interval fail due to issues with the Akave service. Availability is calculated across all such intervals in the month, excluding Customer Planned Downtime or SLA Exclusions.

**Formula:**

Monthly Uptime % = (Total 5-minute Intervals - Unavailable Intervals) / Total 5-minute Intervals × 100

### 2.2. Error Rate

The percentage of valid storage or retrieval requests that fail due to Akave-side errors (e.g., timeouts, internal errors).

### 2.3. Service Credit

A monetary credit (USD) applied to future Akave invoices, calculated based on the service disruption severity.

### 2.4. Outage Period

The duration during which Akave services were unavailable due to factors under Akave's control.

### 2.5. Customer Planned Downtime

Downtime in minutes expressly specified to Akave by the customer, including, but not limited to, any time for which the customer has requested that service access be suspended from their environment.

### 2.6. Unscheduled Service Outage

An interruption to the Service that was not previously communicated to the customer, and that results in the customer's services being unavailable to its own end users. Unscheduled Service Outages exclude any of the following:

* (i) **Customer Planned Downtime;** and/or
* (ii) **Any downtime caused by an SLA exclusion listed in [Section 7.1](#71).**

## 3. Access to Support

### 3.1.

Customers can manage and configure Akave services through the Akave online dashboard and developer portal.

### 3.2.

Akave provides access to a dedicated online support system where customers may: (i) submit SLA Credit Requests or general support tickets; (ii) share diagnostic logs or other relevant data to assist with issue resolution; (iii) track the status of open requests; (iv) view correspondence with Akave support engineers; and (v) access self-service documentation, FAQs, and other technical resources.

### 3.3.

Akave provides direct access to support engineers via email and ticketing for all Priority 1 and Priority 2 issues. Emergency support is available 24/7 for critical service disruptions.

### 3.4.

Additional support information and documentation are available at https://docs.akave.xyz or by contacting support@akave.ai.

## 4. Support Commitment & Issue Severity

Akave provides a single-tier support experience with clearly defined expectations for incident prioritization and response. Please use one of the following methods to request support:

* 🔍 **Review our documentation** for technical details, configuration steps, and FAQs
* 📧 **Email**: Send a message to support@akave.ai with the subject line corresponding to the **priority** of your request
* 🧾 **Ticket**: Submit an issue through our support system at support.akave.xyz

### Response Matrix

| Priority | Description | Response Time |
|----------|-------------|---------------|
| **1 - Urgent** | Complete interruption of production environment affecting all users | Under 4 hours |
| **2 - High** | Major business disruption for a subset of users | Within 8 hours |
| **3 - Normal** | No major impact; issue can be worked around | By next business day |
| **4 - Low** | Informational request, UI issue, enhancement request | Within 7 business days |

## 5. Service Credits

If the Monthly Uptime Percentage falls below the thresholds listed below during a billing cycle, you may be eligible to receive a Service Credit:

| Monthly Uptime Percentage | Service Credit |
|---------------------------|----------------|
| < 99.9% but ≥ 99.0% | 5% of monthly charges |
| < 99.0% but ≥ 95.0% | 10% of monthly charges |
| < 95.0% | 25% of monthly charges |

Service Credits apply only to the portion of your monthly Akave charges directly related to the affected service(s).

### Service Credit Terms and Application

We will apply any Service Credits only against future payments otherwise due from you for Akave services. At our discretion, we may issue the Service Credit to the payment method used for the billing cycle in which Akave did not meet the Service Commitment.

Service Credits will not entitle you to any refund or other monetary reimbursement from Akave. A Service Credit will be applicable and issued only if the total credit amount for the affected monthly billing cycle is greater than one dollar ($1 USD). Service Credits are non-transferable and may not be applied to any other account, organization, or customer.

Unless otherwise agreed in writing, your **sole and exclusive remedy** for any unavailability, non-performance, or failure by Akave to meet the Service Commitment is the receipt of a Service Credit (if eligible), in accordance with the terms of this SLA.

## 6. Credit Request and Payment Procedures

To receive a Service Credit, you must submit a claim by contacting Akave Support via email at support@akave.ai. To be eligible, the credit request must be received **no later than the end of the second billing cycle following the incident** and must include:

1. The subject line: **"SLA Credit Request"**
2. The **billing cycle** and date(s)/time(s) of each incident where the Monthly Uptime Percentage was not met
3. **Logs or supporting documentation** showing that Akave's services did not meet the Service Commitment (confidential information should be redacted or replaced with asterisks)

If the Monthly Uptime Percentage for the specified billing cycle is confirmed by Akave to be below the applicable threshold, a Service Credit will be issued **within one billing cycle** of the confirmed request.

Failure to submit a complete and timely request, or to provide sufficient evidence, will disqualify you from receiving a Service Credit.

## 7. SLA Exclusions

### 7.1.

This SLA does **not** apply to any performance or availability issues that result from:

**(a)** **Events outside of Akave's reasonable control**, including but not limited to:

* (i) Customer's or its end users' hardware, software, or connectivity issues;
* (ii) Corrupted, incomplete, or improperly formatted customer content;
* (iii) Acts or omissions of the customer, its employees, agents, contractors, or third-party vendors;
* (iv) Unauthorized access to the service through misuse of customer credentials, accounts, keys, or devices.

**(b)** Continued use of Akave services after Akave has advised the customer to modify such use, and the customer has not implemented the recommended changes.

**(c)** Any unavailability, degradation, or issue occurring during use of **beta, free-tier, or trial services**, unless otherwise agreed to in writing by Akave.

**(d)** Suspension or termination of access due to violation of the Akave Terms of Service or Acceptable Use Policy.

### 7.2.

If availability is impacted by factors other than those used in calculating the Monthly Uptime Percentage, Akave may, at its sole discretion, issue a Service Credit considering such factors.

## 8. Methodology

### 8.1.

Akave is not responsible for the comprehensive monitoring of customer content, data access logs, or third-party system integrations. The customer is solely responsible for monitoring its own applications and content availability using reasonable industry-standard tools or Akave-provided SDKs, logging endpoints, or APIs.

### 8.2.

Akave will review and consider all supporting data related to a reported **Unscheduled Service Outage**, provided such data is submitted by the customer using a commercially reasonable independent measurement system and includes sufficient technical detail to validate the incident.

### 8.3.

Akave will use all information reasonably available to it to confirm the occurrence and scope of an Unscheduled Service Outage. This may include (but is not limited to) telemetry from Akave's observability infrastructure, node health metrics, and performance data collected immediately before and during the reported Outage Period.
