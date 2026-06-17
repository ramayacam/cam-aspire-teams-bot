# Aspire Platform – Properties Module

Module: Properties | Platform: Aspire Cloud  
Source: guide.youraspire.com/docs/properties

---

## Overview

In Aspire, a **property** is a location where your company performs work. Properties are the foundation of the CRM — they're where you create Opportunities, estimate work, track activity, and manage client relationships.

---

## The Properties Module

The Properties module shows a list of all properties in your system. Use filters, sorts, groups, and saved searches to organize the list.

- Click the **panel icon** to view property details, opportunity metrics, issues, and notes without leaving the list.
- Click the **three-dot menu** to create a new Issue, Task, Email, or Appointment for the property.
- Click **New Property** to add a new property.

---

## Creating a New Property

Go to the Properties module → **New Property**, or use the **Quick Menu**.

**Alternative:** You can also import properties in bulk via Administration → Application → Imports.

### Key Property Fields

| Field | Description |
|---|---|
| Property Name | Required. The name used to identify the property. |
| Property Name Abbreviation | Optional shortened name (20 characters max) used in space-limited displays. |
| Active | Toggle to mark the property as active/inactive. Properties cannot be deleted — mark them inactive to hide them. |
| Branch | Required. The branch the property is associated with. Affects all related Opportunities unless overridden. |
| Property Status | Tracks the sales disposition: Prospect, Customer, Past Customer, Prior Bid, etc. |
| Account Owner | The employee responsible for managing the customer account. |
| Ops Manager | The employee responsible for work performance at the property. |
| Property Group | Groups properties by location (e.g., same campus, HOA, or office park). |
| Tags | Classification tags for filtering and reporting. |
| Tax Jurisdiction | Required before creating an invoice. Set under Administration. |
| Payment Terms | Required before creating an invoice. |
| Lead Source | Where the property came from (e.g., Referral, Website, Cold Call). |
| Annual Budget | Expected annual spending for the property. |
| GEO Perimeter (feet) | Radius from property center within which crews must clock in. Overrides the system-wide default if set. |
| Address | Street address. Google Places autocomplete fills City/State/Zip automatically. |
| Industry | Type of property (e.g., Retail, Residential, HOA, Commercial). |
| Primary Contact | Main contact for the property. |
| Billing Contact | Contact for invoicing. Requires Edit Billing permission to set. |
| Separate Invoice | If checked, a separate invoice is generated per opportunity line in the Invoicing Assistant. |
| Paperless Invoices | If checked, invoices are only sent via email (not printed). |

---

## Notes Types on a Property

| Note Type | Visibility |
|---|---|
| Property Notes | Internal notes visible to office staff only. |
| Operations Notes | Visible to crew leaders in the Mobile App. |
| Snow Notes | Show in Mobile only for work tickets in the Snow division. Replaces Operations Notes for snow jobs. |
| Collection Notes | Internal billing and collections history. Not visible to customers. |

---

## Property Details Screen

When you click on a property, the details screen shows:

| Element | Description |
|---|---|
| Account Owner | Responsible account manager. Click name to see contact details. |
| Primary Contact | Main client contact. |
| Company | Associated company. |
| Earned Revenue | Revenue earned over the past 12 months (excluding current month). Click to view the Property P&L Report. Requires View Revenue permission. |
| Account Balance | Total amount owed. Click to go to Invoicing → Receivables. |
| Previous Site Audit | Date of last Site Audit. Click to view. Click + to start a new one. |
| Gross Margin | Revenue minus direct costs over 12 months, as a percentage. |
| Previous Visit | Most recent Work Ticket date. |
| Next Visit | Next scheduled Work Ticket date. |
| Next Activity | Next scheduled Activity. Click New to create a new one. |
| Attachments | Add or manage files. View All opens the Manage Attachments screen. |
| Map | Static Google Maps view of the property location. |

---

## Sub-tabs on the Property Details Screen

| Tab | What it shows |
|---|---|
| Opportunities | All opportunities for the property. Click New Opportunity to start an estimate. |
| Contacts | Contacts associated with the property. Add existing or create new. |
| Property Issues | Count and chart of open, created, and completed issues. |
| Availability | Days and hours when crews are permitted on the property. |
| Visit Notes | Notes from Work Ticket visits. |
| Notification Log | Log of email/SMS notifications sent for the property. |
| Timeline | Chronological activity history — useful for quickly reviewing property status during a client call. |

---

## Key Behaviors

- **Properties cannot be deleted.** Mark unwanted properties as Inactive to hide them from lists and dropdowns.
- Changing the **Branch** on a property prompts you to update the branch on all associated open/scheduled Work Tickets. Aspire will not change the branch on completed or cancelled Work Tickets.
- If **Require No Open Invoices Check When Changing Jurisdiction** is enabled, Aspire will block a tax jurisdiction change if there are unpaid invoices.
- Changing the **Billing Contact** prompts you to update the billing contact on all related open Opportunities and Invoices.

---

## Frequently Asked Questions

**Q: Can I delete a property?**  
No. Properties cannot be deleted. Mark them as Inactive to remove them from active views.

**Q: What's the difference between Operations Notes and Property Notes?**  
Operations Notes are visible to crew leaders in the Mobile App. Property Notes are only visible to office staff in Aspire.

**Q: What are Snow Notes?**  
Snow Notes replace Operations Notes in the Mobile App when a work ticket is in the Snow division. If no Snow Notes exist, Operations Notes are shown instead.

**Q: When does the GEO Perimeter field matter?**  
It defines the radius within which a crew member must be located to clock in at the property. If set at the property level, it overrides the system-wide setting in Application Configuration.

**Q: What permissions are needed to set Tax Jurisdiction or Billing Contact?**  
You need the **Edit Billing** permission in your user role.

**Q: Can I import properties in bulk?**  
Yes. Go to Administration → Application → Imports to use the Property Import spreadsheet.

**Q: Where do I see all financial activity for a property?**  
Click the Earned Revenue amount on the Property Details screen to open the Property P&L Report.
