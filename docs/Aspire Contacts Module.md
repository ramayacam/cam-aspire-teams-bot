# Contacts Module (Aspire)

System URL: https://cloud.youraspire.com/

*Covers what a contact is, contact types, finding and editing contacts, creating them (including employee contacts with user accounts, and bulk import), attaching contacts to properties, bulk emailing, and certifications. Structure based on the Aspire Academy CRM chapter, enriched with operational depth from the reference documentation.*

---

## CRM, Contacts & Properties

**CRM** (Customer Relationship Management) in Aspire isn't a single module — the functionality lives across **Contacts** and **Properties**, primarily supporting the prospecting and sales process. Both are in the blue side panel: Contacts (contact-card icon) with Properties (building icon) directly below.

- **Contact** = a person you do business with.
- **Property** = a physical location where opportunities are estimated and work is performed (Aspire is property-centric).

⚠️ **Relationship direction:** you can add a **contact to a property**, but you **cannot add a property to a contact**. One contact can be linked to **many** properties (e.g., a property manager overseeing 20 properties).

---

## Contact Types

Aspire defines **five contact types** (the Contact Type field is required):

| Type | Notes |
|---|---|
| **Customer** | Active client. |
| **Prospect** | Potential client (has a Prospect Rating: Hot / Warm / Cold). |
| **Employee** | Your staff. May need a User Account (see Employee Contacts). |
| **Subcontractor (Sub)** | Contractors performing work. |
| **Vendor** | Suppliers. ⚠️ **Vendors import from your accounting software** into a managed list in Administration — vendor records in Contacts are for contact information only. |

⚠️ **Contacts cannot be deleted** once added — mark them **inactive** instead (removes them from default lists but keeps the record).

---

## Finding a Contact

1. Click **Contacts** in the blue side panel (defaults to active contacts).
2. Use a default search (e.g., the employees list) or **filter / display / sort / group** (e.g., drag Company Name to the top to group by company).
3. Type a name in the top search field, press Enter, click a result to open the contact card.

You can also use the universal search bar at the top left.

---

## Key Contact Fields

| Field | Description |
|---|---|
| First / Last Name | **Required.** |
| Contact Type | **Required.** Customer / Prospect / Employee / Sub / Vendor. |
| Email | **Conditionally required:** required if the contact will be an Aspire **user** (email = login username) or an **email contact** for any property. Aspire validates format and **uniqueness** — no sharing across contacts. |
| Job Title | e.g., Property Manager, Board President, Crew Leader. |
| Office / Home / Mobile / Fax Phone | Mobile is used for SMS notifications if configured. |
| Company | Where the contact is employed. |
| Branch | Branch where the contact is located. Controls **visibility** of the contact across modules (e.g., which managers show in route dropdowns). |
| Prospect Rating | Hot / Warm / Cold (for prospects). |
| Owner | Employee who manages the relationship (like an Account Owner at property level). |
| Notes | Internal only. |
| Address | Billing contacts: the mailed-invoice destination. |

On **employee** contacts (with permissions) you'll also see **Payroll**, **Human Resources** (termination, certifications, incidents), and sales **Scorecards** sections.

---

## Creating a New Contact

⚠️ **Aspire allows duplicate contact records** — always **search first** (contact search screen or the left search bar) before creating.

**Required fields:** first name, last name, contact type, and email (if they'll receive emailed invoices or be a user).

**Four ways to create a contact:**
1. **Quick Menu** (blue side panel) → New Contact.
2. **Contacts module** → New Contact (top right).
3. **From a property record** → Contact section → New.
4. **From Edit Property** (three-dot → Edit Property) → add a new primary/billing contact via the white circle with the blue **+**, or pick an existing contact from the dropdown.

---

## Attaching a Contact to a Property

⚠️ **Per property: one primary contact and one billing contact only.** Assigning a new primary/billing contact **silently removes** the previous one from that role — confirm intent. You *can* set **multiple** contacts to receive emailed invoices.

**Steps:**
1. Properties (blue side panel) → search and open the property.
2. Scroll to the **Contact** section → **New** → **Add Existing Contact** (or create new).
3. Set as **primary** and/or **billing**, and choose to email/mail the invoice once generated.
4. **Save** (saving here means you don't also need to save at the top right).

Reminder: you can add a contact to a property, but not a property to a contact.

---

## Creating an Employee Contact

Employee contacts require a **Contact Record** and, for most employees, a **User Account.**

| Employee Type | Contact Record | User Account |
|---|---|---|
| **Crew Member** | ✅ Required | ❌ Not required (uses a PIN on the Crew Leader's device) |
| **Crew Leader / all other employees** | ✅ Required | ✅ Required |

### Required permissions
- **Add Contact** — create contact records.
- **Edit My Contacts / Edit All Contacts** — edit after creation.
- **HR Admin** + Edit Contacts — view/edit payroll fields.
- **System Admin or Branch Admin** — access Administration for user management.

### Steps to create an employee contact
1. Quick Menu → **New Contact**.
2. Fill First Name, Last Name, Title.
3. Set **Contact Type = Employee**.
4. Enter the **work email** (used as the Aspire login username).
5. Select the employee's **Branch**.
6. Enter address and phone.
7. Three-dot menu → **Create User** (skip for Crew Members — just Save).

### Creating the User Account
1. Enter a **PIN** and **Password** (can be the same; no minimum length). ⚠️ **PINs must be unique per employee** — duplicate PINs cause Clock In and Time Entry issues.
2. Select **Branch Access** — the branches this user can see and interact with.
3. Add attachments if needed.
4. Select the user's **Role** (defines system permissions).
5. **Save.**

### Payroll fields (appear after the User Account is created)

| Field | Description |
|---|---|
| Pay Schedule | Set under Administration → Application → Lists → Pay Schedule. |
| Default Workers Comp Code | Used when exporting employee time for payroll integration. |
| Employee Number | From your payroll system. |
| PIN | Crew Members use this to log in on a mobile device. |
| Pay Rates | Effective Date, Base Rate, Burden %. |
| Certifications | Add required certifications with expiration dates. |
| Incidents | Log employee incidents. |

> **Effective Date for pay rates:** should be the Sunday before the start of the work week for a new hire.

### Branch Assignment vs. Branch Access — key distinction

| Setting | Location | What it controls |
|---|---|---|
| **Branch (on Contact Record)** | Contact record → Branch field | **Visibility** of the contact across modules (e.g., which managers appear in route dropdowns). |
| **Branch Access (on User Record)** | User Details screen | What **data** the employee can see and interact with. |

> Assigning a Branch to the contact record ≠ giving the user access to that branch's data. Use the User Details **Branch Access** setting for security and data visibility.

---

## Bulk Import (Contact Import Spreadsheet)

Bulk-create contact records via Administration → **Application** → **Imports** → Import Type = **Contact** → Download Example / Upload. Requires System Admin.

> ⚠️ **Critical sequencing rule: import contacts (including employees) FIRST, before importing properties.** Properties reference contacts by name (Account Owner, Ops Manager, Primary/Billing Contact), so contacts must exist first.

**Rules:** Columns A–C required. Any field with defined options (Contact Type, Prospect Rating, etc.) must have those options added in Admin first — you can't create them via import. Email must be unique.

**Columns:** A Contact Type*, B Contact First*, C Contact Last*, D Salutation (Mr./Mrs./Ms./Dr.), E Job Title, F Office Phone, G Home Phone, H Mobile Phone (SMS), I Fax, J Contact Email (unique), K Address1, L Address2, M City, N State, O Zip, P Company, Q Branch, R Prospect Rating (Hot/Warm/Cold), S Notes, T Owner, U Website.

---

## Editing Contacts & Bulk Actions

**Edit:** open the contact card → edit fields → Save. **Best practice: edit one at a time**; reserve bulk actions until you're certain of the filter.

**Bulk Actions** (Contacts list → filter → check → Bulk Actions): Bulk Email Contacts, Add Certification or Skill, and others. ⚠️ Bulk changes hit every selected contact — verify the filter first.

---

## Bulk Emailing Customers

Two methods:

### Method 1 — from the Contacts List
1. Contacts module → filter and select contacts (checkbox to select all).
2. Bulk Actions → **Bulk Email Contacts**.
3. Compose — the **To** field is pre-populated.
4. Use the 🔍 icon to insert tokens (contact name, property name) into the subject.
5. Send.

> Emails send individually — recipients don't see each other's addresses. Requires **Mass Email Contacts** permission.

### Method 2 — from the Work Ticket List (ticket-specific notifications)
1. Work Tickets module → filter for the relevant tickets → check them.
2. Bulk Actions → **Email**.
3. Set **To**: Primary Contact, Billing Contact, or All Property Contacts.
4. Optionally filter by contact Tags, attach a Work Ticket report (PDF), compose.
5. Send.

> Each ticket generates a separate email per recipient. Requires **Ticket Bulk Email** permission. Send in batches of 50–100 to avoid queue delays.

---

## Certifications & Skills

Adding certifications/skills to Employee or Sub contacts helps you source the right crew for specialized jobs, track recertification/renewal dates, and validate availability against job requirements.

**Add:** from a contact record → **Certifications** section → New. Or from the Contacts list → select → Bulk Actions → **Add Certification or Skill**.

Aspire can surface warnings when a scheduled employee lacks a certification required for a job.

---

## Required Permissions

| Action | Permission |
|--------|-----------|
| Create contacts | Add Contact |
| Edit contacts | Edit My Contacts / Edit All Contacts |
| View/edit payroll fields | HR Admin + Edit Contacts |
| User management (create users) | System Admin or Branch Admin |
| Bulk email from Contacts | Mass Email Contacts |
| Bulk email from Work Tickets | Ticket Bulk Email |
| Import contacts | System Admin |

---

## Best Practices

- **Search before creating** — Aspire allows duplicates, so always check first.
- **Consistent PIN/password conventions** for employees (e.g., first 2 letters of first name + first 4 of last).
- **Inactive, not delete** — contacts can't be deleted; mark Inactive to hide.
- **Email accuracy** — for employees needing email/calendar sync, use their real email; for others any unique email works as a username.
- **Use Tags consistently** so bulk actions and reports filter correctly.

---

## Related (see other modules)

- **Attaching contacts / primary & billing on a property** → also covered in Properties module.
- **Billing contact changes and the "property shows twice" behavior** → Invoicing / Properties.
- **User roles & permissions setup, vendor list, import options** → Administration.

---

## Frequently Asked Questions

**Q: What's the difference between a contact and a property?**
A contact is a person you do business with; a property is a physical location where work is performed. You add contacts to properties, not the other way around, and one contact can be on many properties.

**Q: What are the five contact types?**
Customer, Prospect, Employee, Subcontractor, and Vendor.

**Q: Can I delete a contact?**
No — contacts can't be deleted. Mark them Inactive to remove them from default lists.

**Q: Is email required on a contact?**
Only conditionally — it's required if the contact will be an Aspire user (email = username) or an email-invoice contact for a property. It must be unique.

**Q: Does Aspire prevent duplicate contacts?**
No — Aspire allows duplicates, so always search before creating a new contact.

**Q: How do I create a contact?**
Four ways: Quick Menu → New Contact; Contacts module → New Contact; from a property's Contact section; or from Edit Property when adding a primary/billing contact.

**Q: How many primary and billing contacts can a property have?**
One primary and one billing each. Assigning a new one removes the previous from that role. You can, however, set multiple contacts to receive emailed invoices.

**Q: Does a crew member need a user account?**
No — crew members only need a Contact Record and use a PIN on the Crew Leader's device. Crew Leaders and all other employees need a full User Account.

**Q: My employee's clock-in / time entry is glitching — what should I check?**
Confirm the employee's PIN is unique. Duplicate PINs cause Clock In and Time Entry issues.

**Q: What's the difference between the Branch on the contact record and Branch Access on the user?**
The contact-record Branch controls where the contact is visible across modules; Branch Access on the user record controls what data the employee can actually see and interact with.

**Q: How do I email a group of customers at once?**
Contacts module → filter/select → Bulk Actions → Bulk Email Contacts (requires Mass Email Contacts permission). Emails send individually so recipients don't see each other.

**Q: In what order do I import contacts and properties?**
Contacts (and employees) first, then properties — properties reference contacts by name, so the contacts must already exist.
