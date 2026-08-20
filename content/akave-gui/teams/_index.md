---
date: '2026-06-03T00:00:00+02:00'
draft: false
title: 'Teams'
weight: 5
cascade:
  type: docs
---

Teams give you a **shared workspace** in Akave Cloud. The people on a team
share the same buckets, access keys, usage data, and billing context, so you can
collaborate on data and manage billing together instead of relying on a single
account.

Teams is located in the left sidebar of Akave Cloud.

![Teams page in the sidebar](/images/teams_sidebar.png)

## Prerequisites

- **Akave Cloud account**
  - Sign in to [Akave Cloud](https://console.akave.com/).
- **Admin role**
  - Creating teams, adding or removing members, and changing roles requires the **Admin** role on that team.

## Key Concepts

### The Active Team

At any time, exactly one team is your **active team**. The active team decides what
the rest of Akave Cloud shows you:

- **Buckets & files** you can browse and manage
- **Access keys** (credentials) you can view and create
- **Usage & dashboard** figures
- **Billing** context

When you switch teams, Akave Cloud refreshes to show that team's data.

You always have a personal **Default** workspace to fall back on if you don't have
(or haven't selected) a team.

### Roles

There are two roles on a team:

| Role | What they can do |
| --- | --- |
| **Admin** | Everything a Member can do, plus **create access keys**, invite members, set members' roles, and remove members. |
| **Member** | Belongs to the team and can use its buckets, data, and **the access keys created by Admins** — but cannot create access keys or manage membership. |

The main difference between the two roles is access keys: **Admins create them, and
Members can only use the ones Admins have created.**

The person who creates a team is automatically its **Admin**.

### Owner (Billing)

Ownership is separate from roles. The account that **created and pays for** a team is
its **owner**. Only the owner sees billing details (costs, payment methods, invoices)
for that team. Other members see a notice that billing is available to the team owner.

## Common Tasks

### Create a Team

1. Go to **Teams** in the sidebar.
2. Click **Create team** (or **Create your first team** if you do not have any yet).
3. Enter a **Team name** and confirm.

You are added as the team's **Admin** automatically, and the team becomes available
in your Teams list.

![Create team modal](/images/team_modal.png)

{{< callout type="info" >}}
You can own up to **5 teams**. Team creation is disabled while your billing is overdue.
{{< /callout >}}

### Switch the Active Team

You can switch teams two ways:

- On the **Teams** page, click **Select team** on any team card. The active team shows a
  **Selected** button and an **Active** badge.
- Use the **team switcher** in the top bar (shown once you have more than one workspace).

Switching updates the buckets, access keys, usage, and billing shown across Akave Cloud.

![Team card with Active badge and top-bar switcher](/images/team_switcher.png)

### Add Members

_Admins only._

1. On the **Teams** page, find the team and click **Add members**.
2. Enter one or more **email addresses**, separated by commas.
3. Choose a **Role** — **Member** or **Admin**.
4. Click **Add members**.

![Add team members modal](/images/team_members.png)

{{< callout type="info" >}}
Teams support up to **10 members**.
{{< /callout >}}

### Change a Member's Role

To change a member's role, add them again with the new role selected. Their
existing membership is updated.

### Remove a Member

_Admins only._

1. On a team card, expand **Members: N**.
2. Click **Remove** next to the person you want to remove.

You cannot remove yourself.

![Members list with Remove buttons](/images/team_remove.png)

### View Members

Expand the **Members: N** section on any team card to see each member's email, their
role, and a **You** tag next to your own entry.

## Billing and Access Notes

{{< callout type="info" >}}
**Access keys** can only be **created** by Admins. Members can **use** the keys an
Admin has created for the team, but cannot create their own. If your active team is not
one you own or administer, Akave Cloud prompts you to switch to a team you own.
{{< /callout >}}

{{< callout type="info" >}}
**Billing** details are visible only to the team **owner**. If the active team is not
owned by your account, billing information is hidden until you switch to a team you own.
{{< /callout >}}

## Not Yet Available

The following actions are not available in Akave Cloud today:

- Deleting a team
- Leaving a team
- Renaming a team
- Email notifications for team invitations