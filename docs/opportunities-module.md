# Opportunities & Estimating Module (Aspire)

System URL: https://cloud.youraspire.com/

*Covers the full estimating workflow: fundamentals (services, items, pricing), creating opportunities (contracts and work orders), building estimates, and managing them through their lifecycle (change orders, renewals, contract changes, cancellation). Structure based on the Aspire Academy Estimating chapter, enriched with operational depth from the reference documentation.*

---

## What is the Opportunities Module?

The module where you track potential and actual work your company performs for customers. Each opportunity represents an individual contract or agreement, and is the **chance to bid future work.**

**Key facts:**
- Aspire is **property-centric** — every opportunity is created **from a property**, never directly from the module.
- Each new project = a new opportunity.
- **Every estimate starts as an opportunity.**
- You can also create **Indirect Opportunities** to track employee time not tied to customers (vacation, meetings, training — see Indirect Opportunities below).
- When an opportunity is marked **Won**, each service on the estimate becomes a **work ticket**.

---

## Estimating Fundamentals

Before building estimates, these Administration-level building blocks must exist. (Setting them up requires administrator access.)

### Divisions
Divisions track **revenue and expenses** (a common one is **Maintenance**). An **Overhead Division** records employee hours for **indirect services** (meetings, training) that aren't costed to a customer job.

### Service Types
**Service Types** group Services and tie them to a **Division** — they are the link between service and division, and they break down the **pricing markups** on services within opportunities. Recommended setup: start with **one Service Type per division.**

### Services
A **Service** is the work performed by your company. It must be created in the **Service Catalog in Administration** before it can be added to an estimate.
- **Division prefixes** in service names help route revenue to the correct division.
- **Service Abbreviation** is the field displayed on the **Schedule Board and in Aspire Mobile** for crew leaders.
- Services **cannot be deleted** once created.

**Indirect Services:** require a Service Name and should each have a **Service Schedule** so they can be monitored monthly. They live in the Service Catalog and require administrator access.

### Items and the Item Catalog
Items usable on estimates must be created in the **Item Catalog in Administration**. Aspire has **six item types: Labor, Material, Equipment, Sub, Other, and Kit.**
- Good labor item names are specific (Labor - Janitorial, Labor - Floor Care, Labor - Power Washing).
- **Allocate from Mobile** checkbox lets items be added as costs to tickets in Aspire Mobile.
- The **EPA Number** is for chemical-usage reporting — it does **not** auto-calculate quantities.

**Catalog Item Import Spreadsheet** (bulk create/update items — requires System Admin): Administration → Application → Imports → Import Type = Catalog Item → Download Example / Upload. Spreadsheet columns map directly to the Item Detail screen. **Duplicate handling:** if an item name **exactly matches** an existing item, Aspire **updates** it rather than creating a duplicate — so use precise, consistent naming. Required columns: A–D, G–J, N–P, T. Don't remove/reorder columns, no blank rows, no line breaks in cells.

Key import columns: Item Name (A), Item Type (B), Category (C), Item Alternate Name (D), Purchase Unit Cost (G), Purchase Unit Type (H), Allocation Unit Type (I), Allocation conversion factor (J), Inventory (N), Available to Bid (O), Allocate From Mobile (P), Branches (T — separate multiple with `|`).

### Takeoffs and Kits
- A **Kit** is a **bundled set of related items** designed for specific services; its main benefit is **speeding up estimate creation.**
- A **Takeoff** is a **measurement or count** used for estimating with Kits.
- You **do** need to know your crews' **production rates** when creating Kits.

---

## Pricing in Aspire (MORS)

How Aspire turns cost into the customer's price.

### Pricing terms
| Term | Definition |
|---|---|
| **Cost** | What your company pays for labor, materials, equipment, subs, and other resources. |
| **Price** | What the customer pays. |
| **Revenue** | Total earned from sales before subtracting costs. |
| **Gross Profit** | Revenue − Cost. |
| **Gross Margin** | (Gross Profit ÷ Revenue) × 100. |

**Worked example:** Cost $60, Price $100 → Gross Profit $40, Gross Margin 40%.

### MORS and the pricing hierarchy
- **MORS = Multiple Overhead Recovery System.**
- **Markups exist to recover overhead** expenses not tied to a specific job (e.g., staff training).
- Basic formula: **Cost + Markup = Price.**
- **Pricing hierarchy, most specific to least specific: Service Type → Division → Branch.** Aspire applies the **most specific markup available.**
- **Five item types** factor into a service's total price: **Labor, Material, Equipment, Sub, Other.**

### The Pricing Markup Calculator
Determines the markup % needed to hit a target gross margin. Input the **Cost** and **target Gross Margin %**; it outputs the required **Markup %** and resulting **Price**.

⚠️ **Common error — markup % ≠ gross margin %.** A 50% markup does **not** produce a 50% gross margin. Margin is a percentage of **Price**; markup is a percentage of **Cost**. Use the calculator, not mental math.

**Formulas:**
- Total Cost + Total Markup Dollars = Total Price
- Total Markup Dollars ÷ Total Cost = Markup %
- Total Markup Dollars ÷ Total Price = Gross Margin %

---

## Workflow: 7-Step Process

```
1. Create Opportunity (New)
   ↓
2. Build Estimate (Bidding)
   ↓
3. Mark Complete (Pending Approval if workflow exists)
   ↓
4. Approve (Approved)
   ↓
5. Send Proposal (Delivered)
   ↓
6. Win/Lose (Won → creates Work Tickets | Lost)
   ↓
7. Complete Job (In Process → Complete)
```

### Status Table

| Status | What it means |
|--------|--------------|
| **New** | Opportunity created for a property |
| **Bidding** | Estimate under construction |
| **Pending Approval** | Estimate complete, awaiting internal review (optional) |
| **Approved** | Estimate approved, ready to send |
| **Delivered** | Proposal sent to customer |
| **Won** | Customer accepted, work tickets created |
| **Lost** | Customer rejected |
| **In Process** | Work in progress |
| **Complete** | All work tickets completed |
| **Cancelled** | Work cancelled after being won |

---

## Opportunity Types

### Contracts
**For:** Recurring work at regular intervals, renewable year to year.
**Examples:** Lawn maintenance, janitorial, snow removal, irrigation service.

**Invoice types:**
- **Fixed Payment** — fixed periodic payment (e.g., $500/month for 12 months). Invoiced per the payment schedule set at estimate.
- **Per Service** — bill when a service is completed (e.g., as-needed/emergency work). Invoiced from the work-ticket completion date.
- **T&M (Time & Materials)** — bill actual time and materials; for work spanning seasons or with undefined extras. Invoiced only when all tickets are completed and approved.

### Work Orders
**For:** One-time, non-recurring jobs (small to multi-million-dollar, multi-month).
**Examples:** Installations, construction, vacancy prep, emergency response.

**Invoice types:**
- **Fixed Price on Completion** — one invoice for the total once the last ticket is complete.
- **Fixed Price on Payment Schedule** — installments as work progresses (deposit + milestone payments).
- **T&M on Completion** — actual time/materials, billed when all tickets are complete and approved.
- **Fixed Price Open Billing (FPOB)** — bill any amount at any time; most flexible; great for construction (supports retainage).

> The invoice type sets the entire billing structure — choosing the right opportunity type and invoice type up front is a key decision.

---

## Selection Guide: Which Invoice Type to Use?

### For CONTRACTS

**Fixed Payment** — regular services on a fixed schedule; customer wants the same payment monthly (e.g., annual mowing/janitorial). Invoiced per the payment schedule you configure.

**Per Service** — billing per individual event; emergency or last-minute services (e.g., snow removal, urgent repair). Invoiced on work-ticket completion date.

**T&M** — work spanning seasons, needing extra materials/labor, or with undefined expenses (e.g., fall cleanup of unknown hours). Invoiced only when ALL tickets are completed and approved.

### For WORK ORDERS

**Fixed Price on Completion** — one invoice for the total when done; simple project at an agreed price (e.g., $5,000 patio). Invoiced once the last ticket is complete.

**Fixed Price on Payment Schedule** — large projects with milestone payments (e.g., $50k project → 10% deposit, payment at 50%, final at 100%). Invoiced when the configured % completion is reached.

**T&M on Completion** — Work Order work of unknown scope. Invoiced only when all tickets completed and approved.

**Fixed Price Open Billing (FPOB)** — construction; maximum flexibility; bill part or all at any time. Uses a **Schedule of Values (SOV)** to break down the budget. Invoiced any time, no restrictions.

---

## Creating an Opportunity: Step by Step

### Prerequisites
- Customer must have a **Contact** record and a **Property** record.

### Steps
1. **Properties module** → search and select the property.
2. Scroll to **Opportunities** section → **New Opportunity**.
3. Templates window → choose **New Contract** or **New Work Order**. (Folders here are opportunity templates, organized by division.)
4. **Opportunity Name** — brief and searchable (e.g., "Lawn Maintenance 2027").
5. **Invoice Type** — choose the appropriate one (sets billing structure).
6. **Sales Rep** — defaults to the property account owner; revenue reflects on that employee's **sales scorecard**.
7. **Division** — drives sales-by-division reports.
8. **Status** — starts at New; advances through the pipeline.
9. **Start Date / End Date:**
   - **Contracts:** maximum 12 months between start/end.
   - **Work Orders:** end date auto-populates 30 days after start.
10. **Contract-specific:** Renewal Date (when to revisit renewal); Master Job (auto-filled when renewing an existing opportunity).
11. Bottom fields (optional): **Proposal Description 1** (scope of work), **Proposal Description 2** (terms & conditions), **Opportunity Invoice Notes** (pulled into invoice layouts), **Estimator Notes** (internal only).
12. **Save** — opportunity is created in "New" status, ready to estimate.

**Required permission:** Add Opportunity.

---

## Creating an Estimate

### Key concepts
| Term | Definition |
|---------|-----------|
| **Service Group** | Header that groups related services on the proposal (e.g., "Trees", "Shrubs"). |
| **Service** | Specific work proposed (e.g., "Tree Installation"). |
| **Items** | Components: Labor, Materials, Equipment. |
| **Occurrence (OCC)** | Number of times a service repeats (Contracts). Drives ticket count. |
| **Quantity (Labor)** | Budgeted time per visit; combines with markups for the final labor price. |
| **Proposal** | Completed estimate sent to the customer. |

**Occurrence examples:** twice-weekly for a year = 104; quarterly = 4; daily = 365; weekday-only = 260.

### Basic steps
1. Open opportunity → three-dot menu → **Create Estimate**.
2. Add a **Service Group** header (organizes the proposal); rename "Default Group" as needed.
3. **Add Service** — search and select from the catalog.
4. **Add Items** — Labor, Materials, Equipment to the service.
5. **Quantity** — enter the amount of each item (labor quantity = budgeted hours per visit).
6. **OCC (Contracts)** — enter the number of occurrences.
7. Repeat for all services → return to the Opportunity tab.

### Per-opportunity edits (don't affect the catalog)
- **Service display name** (customer-facing, on proposal) and **service abbreviation** (scheduler-facing) can be edited per-opportunity.
- Editing a **service description** on an opportunity also doesn't affect the catalog.

### Complete the estimate
1. **Complete** (three-dot → Estimate Complete) → for Fixed Payment / FP on Payment Schedule this opens the Payment Schedule window.
2. Configure the payment schedule if applicable.
3. Status changes to **Approved** (or **Pending Approval** if a workflow exists).

### Send the proposal
**Print:** Print Proposal → choose Report Layout → Export Type (PDF recommended) → Print.
**Email:** Email Proposal → To auto-includes primary contact → add emails → (optional) Electronic Signature → choose Layout/Template → Send.

### Win or Lose
- **Won** — mark as won (Aspire creates individual work tickets for each service).
- **Sign and Won** — opens a window for customer signature.
- **Reset** — returns to Bidding for adjustments.
- **Lost** — mark as lost.

---

## Contract Set Up (detailed)

You can use **multiple invoice types on one contract opportunity**, as long as the **opportunity-page invoice type is Fixed Payment.**

**Steps:**
1. Properties → property → New Opportunity → New Contract; name it; set invoice type, division, start/end, renewal date.
2. Three-dot → **Create Estimate.**
3. Add a **service group header**; add services with occurrences and labor (quantity = budgeted hours per visit).
4. Edit display name / service description per-opportunity as needed.
5. For **optional work** (e.g., hot-water carpet extraction): set the service to **Per Service** invoice type and mark it **as-needed** → no open ticket is created on win; crews see it in mobile but it isn't auto-scheduled or billed unless performed (avoids contract changes for optional work).
6. Add **Operations Notes** to services for crew visibility in mobile.
7. Three-dot → **Estimate Complete** → set the **payment schedule** → Save (status → Approved) → preview via Print Proposal → **Won.**

⚠️ On a contract you **cannot reuse the same service** — create separate services (e.g., day shift vs. night shift) with distinct abbreviations for clear scheduling. As-needed per-service items appear in the work-ticket list under "as needed" and are dragged onto the board only when requested; they invoice only after completion.

---

## Work Order Set Up (detailed)

**Steps:**
1. Properties → property → New Opportunity → New Work Order; name it; confirm sales rep; choose division and ops manager; optional due/proposal-due date; start date; end date (defaults 30 days out).
2. Select invoice type; fill proposal descriptions, invoice notes, estimator notes.
3. Three-dot → **Create Estimate.** Add service group headers; add services, labor, materials.
4. To split into separate tickets: click the added service → check **Separate Work Ticket**; change display name (include building area) and abbreviation for scheduler clarity.
5. Preview via Print Proposal → **Estimate Complete** (print/email) → **Won** → Confirm. New **Job Dashboard** and **Work Tickets** tabs appear (one ticket per separate service).

**Note:** On a work order you **can reuse the same service** more than once; the **Separate Work Ticket** checkbox makes each its own ticket (e.g., two crews on hard surfaces at once). Labor quantity = budgeted time; combines with markups for final labor price.

---

## Indirect Opportunities (Overhead)

To have indirect services available in **Aspire Mobile / Time Entry**, an **indirect opportunity must exist — one per branch.** Purpose: track employee hours that **won't be directly costed to a job** (meetings, training, PTO).

**Workflow order:** (1) Create Indirect Properties → (2) Review/Create Indirect Services → (3) Create Indirect Opportunities.

**Steps:**
1. Properties → open the **indirect property** → New Opportunity → New Contract.
2. Name it **Indirect Services**; Invoice Type = **Fixed Payment**; Division = **Overhead/Indirect**; start/end dates (recommended 12 months); Sales Rep (required).
3. Status → **Create Estimate.** Under the Default Group, add each active indirect service, then add the labor item for each.
4. For each item set **OCC = 12** and **QTY hours = 0**; override to **$0.00** if a price calculates.
5. Estimate auto-saves → return to opportunity → **Estimate Complete** → **Won.**
6. **Repeat for the indirect property under each branch.**

⚠️ **Renewal is critical:** indirect opportunities have a fixed end date. If it expires unrenewed, **indirect work tickets disappear and employees can't record overhead time.** Best practice: 12-month duration + an annual renewal reminder.

---

## Opportunity Templates

An **opportunity template** is a "saved recipe" capturing proposal structure (name, invoice type, division, descriptions/attachments), services (with occurrences/quantities), and job-costing info (labor rates, material costs). Purpose: quickly generate consistent, accurate estimates.

**Permissions:** **Edit All Opportunities** to create templates freely; **Edit My Opportunities** can create only for opportunities where they're the sales rep.

**Quick (Work Order) Ticket Template:** a simple one-service work-order template that lets office staff create a work order on the fly from the time-entry screen (accounts for crew quick-ticket time).

⚠️ **Templates cannot be deleted.** To retire one: remove all branches (hides it from folders) and add "Do Not Use" to the name. Template folders are organized by **division**.

### Estimate-from-template update options
| Option | Effect |
|---|---|
| **Update Takeoffs** | Applies property takeoff values to items; items/kits without takeoffs = zero. Only check to find property takeoffs for the first time. |
| **Update Costs** | Recalculates prices from current Item Catalog values. |
| **Update Prices** | Uses most current system markups (service overrides preserved). Important to check on new estimates. |
| **Update Kits** | Updates items/production rates from current system kits. Unchecking keeps pricing the same. |

**Create a template** — Opportunities → open an opportunity → three-dot → **Save as Template** → assign branches → Save.
**Manage a template** — profile icon → Administration → Estimating tab → Opportunity Templates → edit → Save. (Templates are *managed*, not *created*, in Administration.)
**Use a template** — Properties → property → New Opportunity → open the division folder → select template → three-dot → Create Estimate → set update checkboxes → Save → adjust quantities/occurrences.

### Copy an opportunity (vs. template)
Open the opportunity → three-dot → **Copy** → optionally choose a different property → set update checkboxes → Save. Good for **rebidding previously lost jobs** or **correcting an opportunity without a change order** (especially if work has already started).

---

## Consumables

**Consumables** = billable supply goods (toilet paper, liners, hand soaps) provided to clients. Use them in Aspire if you invoice customers for consumables or job-cost a consumables service with material items.

**Inventory vs. purchased-as-needed:** if purchased into inventory and distributed, add to the Item Catalog as inventory items; if purchased on demand, manage as **one-time items** during purchasing.

### Service Catalog setup
- Create multiple service types/services if consumables report to different divisions (e.g., "In Contract" / "Out of Contract").
- For multiple tax jurisdictions, leave the taxable field empty and rely on **Service Tax Overrides** (three-dot on the Service screen).
- Check **Requires Approval** so consumable tickets move to **Pending Approval** for review before the Invoicing Assistant.

### Item Catalog setup
- Category = **Consumable Supplies.** Leave Material Item ID, EPA, Takeoff blank.
- Purchase Unit/Cost = how you buy it (e.g., Case); Allocation Unit = how you provide it (e.g., roll); Allocation = conversion (12 rolls/case → 12).
- Check **Inventory Item** only if kept in storage. **Allocate from Mobile should NOT be checked.**

### T&M Pricing Hierarchy (for as-needed consumables)
1. **Item in catalog AND price contractually guaranteed:** override a set unit price in the estimate; Aspire charges that price × allocated qty. *(Recommended for set pricing.)*
2. **No override, item in catalog:** Aspire uses catalog **Purchase Unit Cost** × T&M markup × allocated qty.
3. **No catalog cost, one-time item on a Purchase Receipt:** Aspire uses **actual PR cost** × estimated T&M markup × allocated qty.

**Contract vs. Work Order:** Contract if invoiced monthly/consistently or pricing is guaranteed (override prices). Work Order if invoiced inconsistently by demand or pricing isn't guaranteed. As-needed → T&M service on a Contract, or T&M on Completion on a Work Order.

---

## Best Practices: Multi-Year Contracts

**Aspire's recommendation: DO NOT create contracts longer than 12 months.** Instead, create 12-month contracts and renew each year.

**Why:** (1) Renewal lets you update takeoffs, service names, **prices**, and checklists with current costs. (2) A multi-year contract generates ALL work tickets at once, which must be scheduled in exact sequence — mid-year revisions become extremely difficult.

**If you MUST create multi-year:** System Admin creates Opportunity Tags ("Multi-Year Contract", "Year 1/2/3"). Start Date = first day of first service month; End Date = last day of last service month; ⚠️ maximum 12 months between start/end; add the multi-year tags.

---

## Growing Community Contracts (Developing HOAs)

**Problem:** an HOA's unit count changes month to month, so the billed amount varies.

**Option 1 — Per Service + Contract Changes (Recommended):**
1. Create the opportunity with **Fixed Payment.**
2. Add production services at **$0.00 price.**
3. Create a special "Growing Community" service: Invoice Type = **Per Service**, 12 occurrences (1/month), override per-occurrence price with the total monthly amount.
4. Complete contract changes monthly before completing the "Growing Community" ticket.

**Option 2 — T&M Service:**
1. Create the opportunity with the desired invoice type; add normal services.
2. Create a "Growing Community" service with invoice type **T&M**; create a "Growing Community" item.
3. Override the item's extended price to the monthly per-unit amount; Labor Rate $0.00, Markups 0%.

---

## Job Dashboard (Work Orders Only)

**Permission:** Job Dashboard + View Reports.

### Profitability Information
| Metric | Description |
|---------|-------------|
| Original Contract | Original contract amount |
| Change Orders | Approved change orders amount |
| Current Contract | Original + Change Orders |
| Estimated Cost | Original estimated cost |
| Estimated GM % | Gross margin based on estimate |
| Projected Cost to Complete | Adjustable via Construction WIP Adjustments |
| Cost to Date | Costs received to date |
| Billed to Date | Total invoices to customer |
| Earned Revenue | Revenue earned based on ticket % complete |

### Cash Position
Cash In = Billed to Date − Open A/R · Cash Out = Labor Expense + A/P Direct Cost − Open A/P · Cash Flow = Cash In − Cash Out.

### Cost Breakdown
By category: Labor, Overtime, Material, Equipment, Sub, Other. Only Material Breakdown is clickable for detail.

---

## Discounts on Opportunities

**Option 1 — Credit Memo (best practice, Contracts or Work Orders):** mention the discount in the service description/invoice notes → generate invoice but don't send → create a credit memo for the discount → apply the credit → review and send. Records revenue and discount separately.

**Option 2 — Manual Override (Contracts or Work Orders):** mention the discount in the Proposal Description → calculate the discounted amount → override the price in the estimate. Doesn't record revenue and discount separately.

**Option 3 — Discount as Service Line (Work Orders ONLY):** create a discount item in the catalog → duplicate the service → rename one "Discount" → add the discount item → ⚠️ ensure **Separate Work Ticket is NOT selected.**

---

## Sub Auto Expenses

Automatically generates expense items in the Purchasing Assistant when subcontractors complete work (useful for subcontracted services/equipment).

| Fee Type | Description |
|----------|-------------|
| Flat Fee | Fixed amount per ticket (e.g., $100 per plow) |
| Hourly | Hourly rate × reported hours |
| Catalog Item | Cost per unit (e.g., $200 per ton of salt) |

**In Estimate:** Service Detail screen → Add Subcontractor Auto Expense → select Company (vendor), Fee Type, Amount.
**In Company Screen:** Properties → Company → Auto Expense section → Auto Expense Wizard for bulk creation.

---

## Bulk Actions in Opportunities

From the Opportunities search screen: Change Sales Rep, Change Operations Manager, Change Anticipated Close Date, Change Probability, Won, Lost, Email (bulk proposals), Add/Remove Tags, Renew (contracts 12 months or less).

---

## Estimating: Advanced Concepts

### Payment Schedule (Fixed Payment)
Defines when and how much to bill each month.
**Fields:** Invoice on (First/Middle/Last of month); Link Completed Tickets to Invoice; month checkboxes; Invoice Amount (editable per month); **Spread Evenly** (distributes balance equally); **Spread and Round** (rounds to nearest dollar).
⚠️ Schedule $ must equal Contract $ to save.

### Schedule of Values (SOV) — FPOB only
Breakdown of the project budget into itemized lines. Editable while Bidding; after winning, only NOT-invoiced lines are editable. Total difference must = zero to save. **Master SOV** consolidates SOV from the work order + all won change orders.

### General Conditions (Work Orders only)
Apply general conditions to work-order estimates (Project Manager hours, safety equipment, site trailers, insurance). Aspire calculates GC costs, distributes them proportionally among services by estimated hours, and applies markups per the pricing model.

### One Time Items
Add items NOT in your catalog (e.g., an outdoor TV in a pergola). In the estimate → **New One Time Item** → (optional) pre-fill from a similar item → select Category, Unit Type, Item Type → enter Item Cost → (optional) Add to Catalog.

---

## Change Orders (Work Orders Only)

**For:** adjusting already-approved Work Orders (modify/add/remove services, change quantities/prices).

**Process:**
1. Opportunity (In Process) → three-dot → **Add Change Order.**
2. Change Order table appears → click Change Order 1 to open the Estimate Screen.
3. Make changes: **Change** (modify), **Copy** (duplicate), **Delete** (removes via negative quantities).
4. **Print or Email Proposal** to send → **Won** to approve.

⚠️ Once won, you **cannot undo** it — you'll need another change order to correct. For FPOB, winning a change order asks you to confirm a new Schedule of Values.

---

## Contract Renewals

**Permission:** Annual Renewals.

1. Opportunity (Contract, 12 months or less) → three-dot → **Renew.**
2. Aspire creates a new opportunity linked via the **Master Job** field.
3. During renewal you can update takeoffs, service names, **prices** (current costs), checklists, and routing/sequence.

**Contract Renewal Report:** Reports → Standard Reports → Sales → Contract Renewals. Default cutoff = 45 days before today. Shows contracts with a past start date, and no end date / renewal date not before cutoff / end date not before cutoff.

---

## Changes to Active Contracts (Contract Changes)

⚠️ Avoid changing the number of occurrences — instead, cancel the original contract and create a new one.

**Process:**
1. Opportunity (In Process, no pending revisions) → **Change.**
2. Set **New Revision Start Date** (after current start, before end) → status → **Changes Pending.**
3. Make changes (Add/Remove/Edit services) → **Win Contract Change.**

**What Aspire does when winning:** Removed services → cancels Open/Scheduled tickets without time/materials, service marked Inactive. Added services → new tickets with a new version number. Updated services → moves Open/Scheduled tickets to the new version. Increased occurrences → adds tickets from the last existing ticket. Reduced occurrences → cancels Open/Scheduled tickets from the end.

---

## Mid-Year Contract Cancellation

1. Determine the cancellation date (last service date).
2. Invoice the customer for services before that date.
3. Cancel contract: three-dot → Cancel.
4. Validate: status → Cancelled.
5. Complete or cancel tickets scheduled before the cancellation date.
6. Handle any credit balance (credit memo if refund).
7. Review adjustments in the End of Month Report.

⚠️ Aspire does NOT automatically cancel tickets before the date — you must do it manually.

---

## Gantt Charts (Work Orders Only)

Visual project management for Construction/Design-Build. Shows the opportunity timeline, individual work tickets, appointments, tasks, issues, and milestones.

| Color | Represents |
|-------|----------------|
| Yellow Lines | Planned Start/End dates |
| Light Grey | Work Order Start/End Dates |
| Dark Grey | Work Order WIP + Estimated Hours |
| Light Green | Work Ticket Estimated Start/End |
| Dark Green | Work Ticket WIP + Estimated Hours |
| Blue + Yellow | Appointments/Tasks |
| Yellow Diamond | Due Dates (Milestones/Issues) |

---

## Electronic Signatures

**Setup (Admin):** Profile → Administration → Configuration → Electronic Signature tab → enable, set email subject/body tokens, confirmation message.

**Send with e-signature:** Email Proposal → check **Enable Electronic Signature** → customer receives a link → opens it, enters email + job number → signs (mouse/finger/stylus) → Sales Rep receives confirmation → marks opportunity **Won.**

⚠️ If you Reset to Bidding, the electronic signature is removed — the customer must sign again.

---

## Key Permissions

| Permission | For |
|---------|----------|
| View / View My Opportunities | View opportunities |
| Edit / Edit My Opportunities | Edit, create estimates, create templates (My = only where sales rep) |
| Add Opportunity | Create opportunities from properties |
| Win Contracts / Win Work Orders | Mark as Won |
| Lose Opportunities | Mark as Lost |
| Change Contract Opportunity | Make contract revisions |
| Change Opportunity | Add change orders |
| Allow Negative Item Quantity | Negative quantities in change orders |
| Annual Renewals | Renew contracts |
| Job Dashboard | View Job Dashboard |
| Import Estimate | Import from CSV/XLSX |
| Allow One-Time Items | Add non-catalog items |
| Modify SOV After Opportunity is Won | Edit SOV after winning FPOB |

---

## Tips and Best Practices

✅ Contracts: maximum 12 months between start/end; renew annually.
✅ Use tags to organize opportunities (division, type, year).
✅ Consistent naming: "Service Type - Property Name - Year".
✅ Payment schedules: ensure Schedule $ = Contract $.
✅ Use templates for consistent estimates; copy an opportunity to rebid lost jobs.
✅ Renew indirect opportunities before they expire (or overhead time tracking breaks).
❌ DON'T change occurrences in contract changes — cancel and create new.
❌ DON'T reuse the same service on a contract — create separate services.
❌ DON'T mark Won without confirming with the customer first.
❌ DON'T edit SOV after invoicing lines (system won't allow it).
❌ DON'T confuse markup % with gross margin % — use the calculator.

---

## Common Questions (from Aspire Academy)

**Q: What is estimating in Aspire used for?**
To calculate the cost of materials, equipment, and labor required to complete a service, and turn that into the customer's price.

**Q: What's the difference between a Contract and a Work Order?**
Contract = recurring jobs completed over time, renewable year to year. Work Order = one-time jobs (any size).

**Q: What happens when I mark an opportunity Won?**
Each service on the estimate becomes a work ticket.

**Q: What does MORS stand for and what are markups for?**
Multiple Overhead Recovery System. Markups recover overhead expenses not tied to a specific job (like staff training). Basic formula: Cost + Markup = Price.

**Q: Is a 50% markup the same as a 50% gross margin?**
No. Markup is a % of Cost; margin is a % of Price. A 50% markup does not yield a 50% margin — use the Pricing Markup Calculator.

**Q: How does Aspire decide which markup to apply?**
Pricing hierarchy, most specific to least specific: Service Type → Division → Branch. Aspire applies the most specific markup available.

**Q: What is a Kit and what is a Takeoff?**
A Kit is a bundled set of related items that speeds up estimate creation. A Takeoff is a measurement or count used for estimating with Kits. You need to know crew production rates to build Kits.

**Q: Can I use more than one invoice type on a contract?**
Yes — as long as the opportunity-page invoice type is Fixed Payment, individual services can use Per Service or T&M.

**Q: How do I offer optional work without a contract change?**
Set the service to Per Service invoice type and mark it as-needed — no ticket is created on win; crews see it in mobile, and it only bills if performed.

**Q: Can I reuse the same service on an estimate?**
On a Work Order, yes — use the Separate Work Ticket checkbox so each becomes its own ticket. On a Contract, no — create separate services with distinct abbreviations.

**Q: Why did my indirect work tickets disappear?**
The indirect opportunity likely expired. Indirect opportunities have a fixed end date and must be renewed, or employees can't record overhead time.

**Q: When should I copy an opportunity instead of using a template?**
For rebidding previously lost jobs, or correcting an existing opportunity without a change order (especially if work has already started).

**Q: How do I stop people from using an outdated template?**
Templates can't be deleted — remove all branches and add "Do Not Use" to the name.

**Q: Which fields appear on invoices tied to an opportunity?**
Opportunity Invoice Notes. (Proposal Description 1 = scope, Description 2 = terms; Estimator Notes are internal only.)
