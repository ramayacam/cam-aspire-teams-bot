# Aspire Platform – Contacts Module

Module: Contacts | Platform: Aspire Cloud  
Source: guide.youraspire.com/docs/contacts-1

---

## Overview

In Aspire, a **contact** is a person or entity your business interacts with. The Contacts module is the foundation of Aspire's CRM — contacts are linked to properties, opportunities, invoices, and activities throughout the system.

**The four default Contact Types:**

| Contact Type | Description |
|---|---|
| Employee | Someone who works for your business. May or may not use the Aspire platform. |
| Customer | A person or organization your business does work for. |
| Vendor | A person or organization your business buys supplies from. |
| Sub | Short for "subcontractor" — a person or organization your business subcontracts with. |

> Administrators can add custom Contact Types under Administration → Application → Lists → Contact Types.

---

## The Contacts Screen

The Contacts screen shows a list of all contacts added to your Aspire instance. Like other list screens, you can use filter, display, sort, and group actions and save your selections as saved searches.

- Click the **panel icon** to view details and notes about a contact without leaving the list screen.
- Click the **three-dot menu** to create a new Issue, Task, Email, or Appointment related to that contact.
- Click **New Contact** to add a new contact.

### Bulk Actions

The Bulk Actions menu only appears if your role has the **Mass Email Contacts** permission. Select one or more contacts and click Bulk Actions to:

| Action | What it does |
|---|---|
| Bulk Email Contacts | Compose an email to all selected contacts. Emails are sent individually — recipients don't see each other's addresses. |
| Send Customer Portal Invite | Email an invitation to selected contacts to use the Customer Portal. |
| Change Contact Type | Change the selected contacts' type. |
| Change Branch | Change which Branch the contact is assigned to. |
| Change Owner | Change the Contact Owner (mostly used for business/organization contacts). |
| Change Pay Schedule | Set a Pay Schedule for Employee or Sub type contacts. |
| Change Status | Toggle the contact's Active status on or off. |
| Add/Remove Tags | Add or remove classification tags for reporting. |
| Opt-In SMS Notifications | Opt Employee contacts into SMS notifications. |
| Add Certification or Skill | Add a Certification or Skill to Employee or Sub contacts. |

---

## Creating a New Contact

### Ways to create a contact

1. **Quick Menu** → New Contact
2. **Contacts module** → New Contact button
3. **From a Property** → Contacts tab → Add Contact
4. **Bulk import** → Administration → Application → Imports (Contact Import Spreadsheet)

### Key Contact Fields

| Field | Description |
|---|---|
| First Name / Last Name | Required for person contacts. |
| Contact Type | Employee, Customer, Vendor, Sub, or custom type. |
| Email Address | Used as the username for Aspire login for employees. |
| Branch | Branch the contact is associated with. Affects visibility across modules. |
| Primary Address | Physical address. |
| Office Phone / Mobile Phone | Contact phone numbers. |
| Tags | Classification tags for filtering and reporting. |
| Active | Toggle to activate or deactivate. Inactive contacts are hidden from most lists. |

### Attaching a Contact to a Property

1. Open the **Property** record.
2. Go to the **Contacts tab**.
3. Click **Add Contact** and search for an existing contact, or create a new one.
4. Assign the contact **role** on the property:
   - **Primary Contact** — main client contact
   - **Billing Contact** — receives invoices (requires Edit Billing permission to set)
   - **Account Owner** — employee managing the customer relationship
   - **Operations Manager** — employee managing work performance

> Always assign the right contact to the right role. The Billing Contact controls who receives invoices. The Primary Contact is used for bulk email and notification defaults.

---

## Creating an Employee Contact

Employee contacts require a **Contact Record** and, for most employees, a **User Account**.

| Employee Type | Contact Record | User Account |
|---|---|---|
| Crew Member | ✅ Required | ❌ Not required (uses PIN on Crew Leader's device) |
| Crew Leader / All other employees | ✅ Required | ✅ Required |

### Required Permissions
- **Add Contact** — to create contact records
- **Edit My Contacts / Edit All Contacts** — to edit after creation
- **HR Admin** + Edit Contacts — to view/edit payroll fields
- **System Admin or Branch Admin** — to access Administration for user management

### Steps to Create an Employee Contact

1. Hover over the **Quick Menu** → **New Contact**
2. Fill in First Name, Last Name, Title
3. Set **Contact Type** to Employee
4. Enter work email address *(used as Aspire login username)*
5. Select the employee's **Branch**
6. Enter address and phone information
7. Click the **three-dot menu** → **Create User** (skip for Crew Members — just Save)

### Creating the User Account

1. Enter a **PIN** and **Password** (can be the same; no minimum length)
   > ⚠️ PINs must be unique per employee — duplicate PINs cause Clock In and Time Entry issues.
2. Select **Branch Access** — the branches this user can see and interact with in Aspire
3. Add any attachments if needed
4. Select the user's **Role** (defines system permissions)
5. Press **Save**

### Payroll Fields (appear after User Account is created)

| Field | Description |
|---|---|
| Pay Schedule | Set under Administration → Application → Lists → Pay Schedule |
| Default Workers Comp Code | Used when exporting employee time for payroll integration |
| Employee Number | From your company's payroll system |
| PIN | Crew Members use this to log in on a mobile device |
| Pay Rates | Set Effective Date, Base Rate, and Burden % |
| Certifications | Add required certifications with expiration dates |
| Incidents | Log employee incidents |

> **Note on Effective Date for pay rates:** Should be the Sunday before the start of the work week for a new hire.

### Branch Assignment vs. Branch Access — Key Distinction

| Setting | Location | What it controls |
|---|---|---|
| **Branch (on Contact Record)** | Contact record → Branch field | Visibility of the contact across Aspire modules (e.g., which managers appear in route dropdowns) |
| **Branch Access (on User Record)** | User Details screen | What data the employee can see and interact with in Aspire |

> Assigning a Branch to the contact record ≠ giving the user access to that branch's data. Use the User Details screen Branch Access setting for security and data visibility.

---

## Bulk Emailing Customers

Aspire supports two methods of bulk emailing from the Contacts module:

### Method 1: Bulk Email from the Contacts List

1. Go to the **Contacts** module
2. Filter and select the contacts you want to email (checkbox to select all)
3. Click **Bulk Actions** → **Bulk Email Contacts**
4. Compose the email — the **To** field is pre-populated
5. Use the 🔍 icon to insert tokens (e.g., contact name, property name) in the subject line
6. Click **Send**

> Emails are sent individually — recipients do not see each other's addresses.  
> Requires: **Mass Email Contacts** permission

### Method 2: Bulk Email from the Work Ticket List

Used to send work-ticket-specific notifications to property contacts.

1. Go to **Work Tickets** module and filter for the relevant tickets
2. Check the boxes next to the tickets
3. Click **Bulk Actions** → **Email**
4. Set the **To** field: Primary Contact, Billing Contact, or All Property Contacts
5. Optionally filter by contact Tags, attach a Work Ticket report (PDF), and compose the message
6. Click **Send**

> Each selected ticket generates a separate email per recipient.  
> Requires: **Ticket Bulk Email** permission  
> Recommendation: Send in batches of 50–100 to avoid email queue delays.

---

## Certifications & Skills

Adding certifications and skills to Employee or Sub contacts helps you:
- Source the right crew for specialized jobs
- Track recertification and renewal dates
- Validate availability against job requirements

### Adding a Certification or Skill

From a contact record: scroll to the **Certifications** section → click **New**  
Or from the Contacts list: select contacts → **Bulk Actions** → **Add Certification or Skill**

Certifications can also be validated against scheduling requirements — Aspire can surface warnings when a scheduled employee lacks a required certification for a job.

---

## Contact Best Practices

- **Check for duplicates before creating** — search for the name in Contacts before creating a new record.
- **Use consistent naming conventions** for employee PINs and passwords (e.g., first 2 letters of first name + first 4 of last name).
- **Inactive vs. Delete** — contacts cannot be deleted. Mark unwanted contacts as Inactive to hide them.
- **Email address accuracy matters** — for employees who need email/calendar sync with Aspire, use their real email address. For others, any unique email format works as a username.
- **Tags** — use them consistently so bulk actions and reports filter correctly.

---

## Frequently Asked Questions

**Q: Can I delete a contact?**  
No. Contacts cannot be deleted. Mark them as Inactive to remove them from active views.

**Q: What's the difference between Branch (on contact) and Branch Access (on user)?**  
Branch on the contact record controls visibility in module dropdowns (e.g., which managers appear on a route). Branch Access on the user record controls what data the employee can see and interact with across Aspire.

**Q: Does the email address on an employee contact have to be a real email?**  
Only if they need email/calendar sync with Aspire. Otherwise, any unique email-format string works as a login username.

**Q: What permission do I need to set or change a Billing Contact on a property?**  
You need the **Edit Billing** permission in your user role.

**Q: Why does a new employee contact not appear in a route's Manager dropdown?**  
The Manager dropdown is filtered by Branch on the contact record. Make sure the employee's contact record has the correct Branch assigned — not just Branch Access on their user record.

**Q: Can I import contacts in bulk?**  
Yes. Go to Administration → Application → Imports → use the Contact Import Spreadsheet.
