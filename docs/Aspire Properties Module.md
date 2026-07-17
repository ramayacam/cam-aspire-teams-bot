# Properties Module (Aspire)

System URL: https://cloud.youraspire.com/

*Covers what a property is, finding and editing properties, creating new ones (including bulk import and indirect properties), the property record and its sub-tabs, note types, key behaviors, and Site Audits. Structure based on the Aspire Academy CRM chapter, enriched with operational depth from the reference documentation.*

---

## What is a Property?

In Aspire, a **property** is a physical location where your company performs work. Properties are the foundation of the CRM — they're where you create Opportunities, estimate work, track activity, schedule visits, and manage the client relationship. Accurate properties produce accurate opportunities.

⚠️ **Properties cannot be deleted.** To remove one from active views, mark it **Inactive** (yellow slide button) — records stay in Aspire but drop out of default lists and dropdowns.

---

## Finding a Property

Two ways to search:
- **Search Aspire** (universal search bar): prefix with **`P`** then the name to limit results to properties.
- **Properties module** (most common): defaults to searching by property name, company, primary contact, and primary contact mobile. Use filters, sorts, groups, and saved searches to organize the list.

In the Properties list: click the **panel icon** to preview details/metrics/issues/notes without leaving the list; click the **three-dot menu** to create an Issue, Task, Email, or Appointment; click **New Property** to add one.

---

## Creating a New Property

⚠️ **Search first to avoid duplicates** — a prior manager may have requested a bid years ago. Edit the existing property rather than create a new one.

**Two ways to create:**
1. **Quick Menu** (blue side panel) → New Property; **or**
2. **Properties module** → blue **New Property** button (upper right).

**Steps:**
1. Enter **Property Name** and **Branch** (the only required fields).
2. Recommended even though optional: Property Status (e.g., Prospect), Tax Jurisdiction, Payment Terms, Address, Industry — these matter for won opportunities and targeted marketing.
3. Optionally add Property / Operation / Snow notes.
4. Scroll down to set **Primary** and **Billing** contacts (can be pre-selected or new; they need not be the same).
5. **Save** (green, upper right) — lands on the property record, ready for opportunities.

**Bulk import alternative:** Administration → Application → Imports → Property Import spreadsheet (see "Bulk Import" below).

### Key Property Fields

| Field | Description |
|---|---|
| Property Name | **Required.** Identifies the property. |
| Property Name Abbreviation | Optional; **20-character** limit. Shown on schedule board, visit plaques, and Aspire Mobile (crew-facing). |
| Active | Toggle active/inactive. Properties **cannot be deleted** — mark inactive to hide. |
| Branch | **Required.** Affects all related opportunities unless overridden. |
| Property Status | Sales disposition: Prospect, Customer, Past Customer, Prior Bid, etc. |
| Account Owner | Employee responsible for managing the customer account. |
| Ops Manager | Employee responsible for work performance at the property. |
| Property Group | Groups connected properties (same campus, HOA, office park). |
| Tags | Classification tags for filtering and reporting. |
| Tax Jurisdiction | **Required before invoicing.** Set under Administration. |
| Payment Terms | **Required before invoicing.** |
| Lead Source | Where the property came from (Referral, Website, Cold Call). |
| Annual Budget | Expected annual spending. |
| GEO Perimeter (feet) | Radius from property center within which crews must clock in. Overrides the system-wide default if set. |
| Address | Street address. Google Places autocomplete fills City/State/Zip. |
| Industry | Retail, Residential, HOA, Commercial, etc. |
| Primary Contact | Main contact for the property. |
| Billing Contact | Contact for invoicing. **Requires Edit Billing permission** to set. |
| Separate Invoices | If checked, generates a **separate invoice per invoice type** available for the property (driven by opportunity invoice type — a property can have opportunities of different types, so each invoice type lands on its own invoice). |
| Paperless Invoices | If checked, Aspire does not include a printed copy in the printable batch. Does **not** by itself email invoices — emailing is set on the property's contacts. |
| Custom Fields | Editable with permission, but **created/deleted only by a System Admin.** |

---

## Note Types on a Property

| Note Type | Visibility |
|---|---|
| **Property Notes** | Internal / office-only. |
| **Operation Notes** | Visible to crew leaders in Aspire Mobile for all scheduled services (e.g., "close the back gate"). |
| **Snow Ops Notes** | Snow-specific field reminders; shown in Mobile only for Snow-division tickets. Replaces Operation Notes for snow jobs (if none exist, Operation Notes show instead). |
| **Collection Notes** | Internal billing/collections history. Not visible to customers. |

⚠️ Property Notes (internal) vs. Operation Notes (field-visible) is a common point of confusion — keep them straight.

---

## The Property Record (Overview / Details Screen)

Opening a property shows an **overview** with name, address, account owner, primary contact, and rolling-12-month metrics.

| Element | Description |
|---|---|
| Account Owner | Responsible account manager (click name for contact details). |
| Primary Contact | Main client contact. |
| Company | Associated company. |
| Earned Revenue | Revenue earned over the past 12 months (excluding current month). Click for the Property P&L Report. **Requires View Revenue permission.** |
| Account Balance | Total owed. Click to go to Invoicing → Receivables. |
| Previous Site Audit | Date of last site audit. Click to view; click **+** to start a new one. |
| Gross Margin | Revenue minus direct costs over 12 months, as a percentage. |
| Previous Visit | Most recent work ticket date. |
| Next Visit | Next scheduled work ticket date. |
| Next Activity | Next scheduled activity (click New to create). |
| Attachments | Add/manage files. |
| Map | Static Google Maps view of the location. |

Also on the overview: opportunities, contacts, and property issues (created/completed in the last 30 days).

**Three-dot menu (top right)** → property-specific links: P&L, transactions (invoices/payments), client budget tool, visit notes, takeoffs, property wizard, or **Edit Property**.

### Sub-tabs on the property record

| Tab | What it shows |
|---|---|
| Opportunities | All opportunities for the property (New Opportunity to start an estimate). |
| Contacts | Contacts associated with the property (add existing or create new). |
| Property Issues | Count and chart of open/created/completed issues. |
| Availability | Days and hours crews are permitted on the property. |
| Visit Notes | Notes from work-ticket visits. |
| Notification Log | Log of email/SMS notifications sent for the property. |
| Timeline | Chronological activity history — useful during a client call to review status quickly. |

---

## Editing a Property

1. Properties → search → open the property.
2. Three-dot menu → **Edit Property**.
3. Edit fields (name, abbreviation, branch, separate/paperless checkboxes, tax jurisdiction, payment terms, address, industry, notes, primary & billing contacts, custom fields) → **Save** (green, top right).

**Best practice:** edit properties **one at a time**; reserve bulk actions until you're experienced and certain of the filter.

### Bulk actions (e.g., reassign account owner)
1. In the property search screen, filter to the target set (e.g., all properties owned by a departing employee).
2. Check the top-row checkbox to select all matches.
3. **Bulk Actions** (top right) → **Change Account Owner** → choose the new owner → **Save**.

Other bulk actions follow the same pattern. ⚠️ Bulk changes affect every selected property — double-check the filter first.

---

## Key Behaviors

- **Properties cannot be deleted** — mark Inactive to hide.
- **Changing the Branch** prompts you to update the branch on all associated **open/scheduled** work tickets. Aspire will **not** change the branch on completed or cancelled tickets.
- **Changing the Tax Jurisdiction:** if "Require No Open Invoices Check When Changing Jurisdiction" is enabled, Aspire blocks the change while unpaid invoices exist.
- **Changing the Billing Contact** prompts you to update the billing contact on all related open opportunities and invoices. ⚠️ If you don't confirm this, the property can appear **twice** in Receivables (old contact holds the old balance, new contact holds new invoices).

---

## Bulk Import (Property Import Spreadsheet)

Bulk-create property records via Administration → **Application** → **Imports** → Import Type = **Property** → Download Example / Upload. Requires System Admin.

> ⚠️ **Critical sequencing rule: import contacts (including employees) FIRST, before importing properties.** Account Owner, Ops Manager, Primary Contact, and Billing Contact all reference contacts that must already exist in Aspire.

**Spreadsheet rules:**
- Columns **A–D are required** — never leave empty.
- Don't remove or change columns (the load fails). No blank/skipped rows. No copyright/™ symbols.
- Any field with defined options (Status, Industry, Property Type, Group, Tax Jurisdiction, Competitor, Lead Source, Locality) must have those options **added in Admin first**.
- Availability windows (columns AF–AS): one window per day of week; times in format like `12:00PM`, `15:00`, `08:30AM`. **Only works when importing NEW properties** — add more later via the property edit page.

**Key columns:** A Property Name*, B Property Name Abbreviation* (20-char display), C Branch Name*, D Property Status*, E Account Owner, F Ops Manager, G–K Address, L Industry, M Property Type, N Property Group, O Property Notes, P Operation Notes, Q Snow Operation Notes, R Primary Contact, S Billing Contact, T Email Invoice Contact, U Paperless Invoices (1/0), V Separate Invoice (1/0), W Payment Terms, X Tax Jurisdiction, Y Competitor, Z Lead Source, AA Locality, AB Website, AC Budget, AD Geo Perimeter (feet), AE Integration Identifier, AF–AS Availability windows.

---

## Indirect Properties

**Indirect properties** exist so overhead/indirect employee time (internal training, office admin) can be recorded — time **not** directly costed to a customer job. Because the **Internal Property field is required to set up a branch**, you must create an indirect property **for each branch.**

**Overall workflow:** (1) Create Indirect Properties → (2) Review/Create Indirect Services → (3) Create Indirect Opportunities. (Steps 2–3 live in the Opportunities module → Indirect Opportunities.)

**Create an indirect property:**
1. Properties module → **New Property** → name it "Indirect - [Branch]" (e.g., Indirect - Chesterfield); keep Branch = **Main** for now; enter the branch's physical address → **Save**.
2. **Create the branch record:** profile icon → Administration → Organization → **Branches** → New → set the **Internal Property** dropdown to the indirect property you just created → fill known fields → Save.
3. **Link branch back to the property:** Properties → open the indirect property → three-dot → **Edit Property** → set **Branch** to the new branch → Save.
4. Repeat for each additional branch.

⚠️ Indirect properties are for **indirect services only** — not shop maintenance or other services/opportunities.

---

## Site Audits

A **Site Audit** evaluates, scores, and documents a property's condition and communicates it to the client. Audits combine notes + photos, scored on a universal scale for objectivity, and can be done on desktop and mobile, sent to clients, and turned into Issues or Opportunities.

### Types vs. Categories
- **Site Audit Type** = the name/reason for the inspection (what an auditor sees at a property). Examples: Commercial Clean, Quality Inspection by Room/Area, Post-Construction Cleaning, Health & Safety Compliance.
- **Site Audit Category** = an individual scored consideration within an audit (cleanliness, safety, compliance; or by room/surface). Categories are assigned to types (as many as desired; if none specified, available to all types), can be tied to a service, given a display order, notes/instructions, and predefined **tags** (quick-select responses).

### Why companies use site audits
Check quality after a customer issue; review new-hire work in training; find upsell opportunities beyond current services; evaluate cleaning-procedure compliance; ensure hygiene/safety benchmarks. **Business benefits:** stronger sales pitch (show a prospect where a competitor falls short), quality control (score → photo → internal Issue → optionally notify client), additional sales opportunities, and employee education/retention.

### Permissions required

| Permission (grouping) | Needed for |
|---|---|
| **System Admin** (Admin) | Setting up site audits in Admin. Super-user — grant to only 1–2 roles / a few users. |
| **Edit My Properties** or **Edit All Properties** (Properties) | Performing audits on customer properties. |
| **Edit Site Audits** (Properties) | May also be required to perform audits. |
| **View Drill Down Reports - Site Audits** (Reports) | Viewing audits in the drill-down report. |

*After updating roles, affected users must log out and back in.*

### Setting up site audits
- **Configuration (attachment size):** Administration → Configuration → Application → far-left column, bottom → **Default Attachment Upload Size** (Small / Medium / Large / Actual Size). Consider an AspireCare layout-revision request to match the chosen size.
- **Create a Type:** Administration → **Site Audits** tab → New → name it and select a scale (1–10, Pass/Fail, Green/Yellow/Red, 1–5, A–F, or no scale).
- **Create a Category:** Site Audits tab → New → name it; assign to relevant types (or none = all types); optionally tie to a service; set display order; add notes/instructions and tags.

⚠️ Unused categories can be **deleted**; categories already used in audits can only be **inactivated**.

---

## Required Permissions

| Action | Permission |
|--------|-----------|
| Set Tax Jurisdiction or Billing Contact | Edit Billing |
| View Earned Revenue / P&L | View Revenue |
| Edit properties | Edit My Properties / Edit All Properties |
| Perform site audits | Edit My/All Properties (+ Edit Site Audits) |
| Set up site audits | System Admin |
| Create/delete custom fields | System Admin |
| Import properties | System Admin |

---

## Related (see other modules)

- **Indirect Services & Opportunities** (steps 2–3 of the indirect workflow) → Opportunities module.
- **Separate/Paperless invoice behavior at invoice time** → Invoicing module.
- **Contacts on a property** → Contacts module.
- **GEO perimeter system default, branches, custom-field creation** → Administration.

---

## Frequently Asked Questions

**Q: Can I delete a property?**
No. Properties cannot be deleted — mark them Inactive to remove them from active views.

**Q: What's the difference between Operation Notes and Property Notes?**
Operation Notes are visible to crew leaders in Aspire Mobile (field-facing). Property Notes are internal/office-only.

**Q: What are Snow Notes?**
Snow Ops Notes replace Operation Notes in Mobile when a work ticket is in the Snow division. If no Snow Notes exist, Operation Notes show instead.

**Q: When does the GEO Perimeter field matter?**
It sets the radius within which a crew member must be to clock in at the property via mobile. Set at the property level, it overrides the system-wide default in Application Configuration.

**Q: What permissions are needed to set Tax Jurisdiction or Billing Contact?**
The Edit Billing permission in your user role.

**Q: Before creating a new property, what should I do first?**
Search to confirm the property doesn't already exist — edit the existing record instead of creating a duplicate.

**Q: What are the only required fields to create a property?**
Property Name and Branch. Status, tax jurisdiction, payment terms, address, and industry are recommended but optional.

**Q: Can I import properties in bulk?**
Yes — Administration → Application → Imports → Property spreadsheet. Import contacts and employees FIRST, since account owner, ops manager, and contacts must already exist.

**Q: Why do I need an indirect property for each branch?**
Setting up a branch requires an Internal Property, so each branch needs its own indirect property to record overhead/indirect time.

**Q: What is a Site Audit?**
A scored, documented inspection of a property's condition (notes + photos on a universal scale) that you can send to clients and turn into Issues or Opportunities.

**Q: What's the difference between a Site Audit Type and Category?**
Type = the reason/name for the inspection (what the auditor picks at a property). Category = an individual scored consideration within the audit (cleanliness, safety, a room, etc.).

**Q: Why does a property show twice in Receivables?**
Its billing contact was changed without confirming "update open invoices" — the old contact keeps the old balance while the new contact holds new invoices. Confirm that prompt when changing a billing contact.

**Q: Where do I see all financial activity for a property?**
Click the Earned Revenue amount on the property record to open the Property P&L Report (requires View Revenue permission).
