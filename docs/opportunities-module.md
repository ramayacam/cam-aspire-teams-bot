# Opportunities Module

**System URL:** https://cloud.youraspire.com/

---

## What is the Opportunities Module?

The module where you track potential and actual work your company performs for customers. Each opportunity represents an individual contract or agreement.

**Key features:**
- System centered on **Properties** (customer locations)
- All opportunities are created from a property
- Each new project = new opportunity
- You can also create **Indirect Opportunities** to track employee time not related to customers (vacation, meetings, etc.)

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

### 1. Contracts
**For:** Recurring work at regular intervals

**Examples:** Lawn maintenance, snow removal, irrigation service

**Available Invoice Types:**
- **Fixed Payment:** Fixed monthly/periodic payment (e.g., $500/month for 12 months)
- **Per Service:** Bill when service is completed (e.g., snow removal per event)
- **T&M (Time & Materials):** Bill for actual time and materials when finished

### 2. Work Orders
**For:** One-time, non-recurring jobs

**Examples:** Tree installation, irrigation installation, construction

**Available Invoice Types:**
- **Fixed Price on Completion:** One invoice for total when everything is done
- **Fixed Price on Payment Schedule:** Customer pays in installments as work progresses
- **T&M on Completion:** Bill actual time/materials at completion
- **Fixed Price Open Billing:** Bill any amount at any time (most flexible)

---

## Selection Guide: Which Invoice Type to Use?

### For CONTRACTS

#### Fixed Payment
**When to use:**
- Regular services on fixed schedule
- Customer wants same payment each month
- Example: Annual lawn mowing contract

**How to invoice:** Invoicing Assistant invoices based on payment schedule you configure

#### Per Service
**When to use:**
- Billing based on individual event
- Emergency or last-minute services
- Example: Snow removal, urgent repair

**How to invoice:** Invoicing Assistant invoices based on work ticket completion date

#### T&M (Time & Materials)
**When to use:**
- Work spanning seasons
- Requires extra materials/labor
- Undefined expenses
- Example: Fall cleanup where you don't know how many hours it'll take

**How to invoice:** Only when ALL work tickets are completed and approved

### For WORK ORDERS

#### Fixed Price on Completion
**When to use:**
- One invoice for total when done
- Simple project with agreed price
- Example: Patio installation, total price $5,000

**How to invoice:** Once the last work ticket is complete

#### Fixed Price on Payment Schedule
**When to use:**
- Large projects with milestone payments
- Customer pays deposit + payments based on % completed
- Example: $50,000 project → 10% deposit, payment at 50%, final payment at 100%

**How to invoice:** When configured % completion is reached

#### T&M on Completion
**When to use:**
- Same as T&M for contracts
- Work Order work where you don't know full scope

**How to invoice:** Only when all tickets are completed and approved

#### Fixed Price Open Billing
**When to use:**
- Construction projects
- Maximum billing flexibility
- Can bill part or all at any time
- Uses **Schedule of Values (SOV)** to break down

**How to invoice:** At any time, no restrictions

---

## Creating an Opportunity: Step by Step

### Prerequisites
- Customer must have a **Contact** record
- Customer must have a **Property** record

### Steps

1. **Properties module** → Search and select the property
2. Scroll to **Opportunities** section → **New Opportunity**
3. Templates window → Choose type: **New Contract** or **New Work Order**
4. **Opportunity Name:** Descriptive name (e.g., "Lawn Maintenance 2027")
5. **Invoice Type:** Choose appropriate one
6. **Sales Rep:** Choose responsible person (default: property account owner)
7. **Division:** Choose division (e.g., Maintenance, Snow, Construction)
8. **Start Date / End Date:** Define period
   - **Contracts:** Maximum 12 months between start/end
   - **Work Orders:** End date auto-populates 30 days after start
9. (Optional) **Renewal Date** (contracts only)
10. (Optional) Fill: Proposal Description 1, Proposal Description 2, Opportunity Invoice Notes, Estimator Notes
11. **Save**

**Result:** Opportunity created with "New" status, ready to create estimate

---

## Creating an Estimate

### Key Concepts

| Term | Definition |
|---------|-----------|
| **Service Group** | Groups related services (e.g., "Trees", "Shrubs") |
| **Service** | Specific work proposed (e.g., "Tree Installation") |
| **Items** | Components: Labor, Materials, Equipment |
| **Occurrence (OCC)** | Number of times a service repeats (Contracts only) |
| **Proposal** | Completed estimate sent to customer |

### Basic Steps

1. Open opportunity → **Create Estimate**
2. **Service Group:** Rename "Default Group" (e.g., "Tree Installation")
3. **Add Service:** Search and select service from catalog
4. **Add Items:** Add Labor, Materials, Equipment to service
5. **Quantity:** Enter needed amount of each item
6. **OCC (Contracts):** Enter number of occurrences
7. Repeat for all services
8. Return to **Opportunity tab**

### Complete the Estimate

1. **Complete** button → For Fixed Payment/FP on Payment Schedule opens Payment Schedule window
2. Configure payment schedule if applicable
3. Status changes to **Approved** (or **Pending Approval** if workflow exists)

### Send Proposal

**Option 1: Print**
1. **Print Proposal**
2. Choose Report Layout
3. Choose Export Type (PDF recommended)
4. **Print**

**Option 2: Email**
1. **Email Proposal**
2. To field: Auto-includes primary contact
3. Add additional emails
4. (Optional) Enable Electronic Signature
5. Choose Proposal Layout and Template
6. **Send**

### Win or Lose

**Options:**
- **Won:** Mark as won immediately
- **Sign and Won:** Opens window for customer signature
- **Reset:** Returns to Bidding for adjustments
- **Lost:** Mark as lost

**⚠️ When winning:** Aspire creates individual work tickets for each service

---

## Best Practices: Multi-Year Contracts

### Aspire's Recommendation
**DO NOT create contracts longer than 12 months.** Instead:
- Create 12-month contracts
- Renew each year

### Why?

**1. Manage price increases**
During renewal you can:
- Update takeoffs
- Update service names
- **Update prices** with current cost changes
- Update visit checklists

**2. Process contract changes**
- If you create multi-year contract, Aspire generates ALL work tickets
- Tickets must be scheduled in exact sequence
- Mid-year revisions become extremely difficult

### If You MUST Create Multi-Year

**Prior setup:** System Admin must create Opportunity Tags:
- Tag "Multi-Year Contract"
- Tags "Year 1", "Year 2", "Year 3", etc.

**When creating estimate:**
- Start Date: First day of first service month
- End Date: Last day of last service month
- ⚠️ **Maximum 12 months** between start/end
- Add multi-year tags in Tag field

---

## Growing Community Contracts (Developing HOAs)

### Problem
HOA hires maintenance for community properties + residences. Number of units changes month to month, so billed amount varies.

### Option 1: Per Service + Contract Changes (Recommended)

**Setup:**
1. Create opportunity with **Fixed Payment**
2. Add production services with **$0.00 price**
3. Create special "Growing Community" service for billing:
   - Invoice Type: **Per Service**
   - 12 occurrences (1 per month)
   - Override per occurrence price with total monthly amount
4. Complete contract changes monthly before completing "Growing Community" ticket

**Advantage:** Separate tracking of production vs. billing

### Option 2: T&M Service

**Setup:**
1. Create opportunity with desired invoice type
2. Add normal services
3. Create "Growing Community" service with invoice type **T&M**
4. Create "Growing Community" item in catalog
5. Override item extended price to reflect monthly per-unit amount
6. Labor Rate: $0.00, Markups: 0%

**Advantage:** Doesn't require monthly contract changes

---

## Job Dashboard (Work Orders Only)

**Permission:** Job Dashboard + View Reports

### What Does It Show?

3 main sections:

#### 1. Profitability Information

| Metric | Description |
|---------|-------------|
| **Original Contract** | Original contract amount |
| **Change Orders** | Approved change orders amount |
| **Current Contract** | Original + Change Orders |
| **Estimated Cost** | Original estimated cost |
| **Estimated GM %** | Gross margin based on estimate |
| **Projected Cost to Complete** | Projected cost (adjustable via Construction WIP Adjustments) |
| **Cost to Date** | Costs received to date |
| **Billed to Date** | Total invoices to customer |
| **Earned Revenue** | Revenue earned based on work ticket % complete |

#### 2. Cash Position

| Element | What it means |
|----------|--------------|
| **Cash In** | Billed to Date - Open A/R |
| **Cash Out** | Labor Expense + A/P Direct Cost - Open A/P |
| **Cash Flow** | Cash In - Cash Out |

#### 3. Cost Breakdown

Costs by category:
- Labor
- Overtime
- Material
- Equipment
- Sub
- Other Costs

**Note:** Only Material Breakdown is clickable for additional details

---

## Discounts on Opportunities

### Option 1: Credit Memo (Best Practice)

**For:** Contracts or Work Orders

**Steps:**
1. Mention discount in service description and invoice notes
2. Generate invoice but DON'T send it
3. Create credit memo for customer for discount amount
4. Create payment in Aspire applying the credit
5. Review invoice showing applied credit → Send

**Advantage:** Records revenue and discount separately in accounting

### Option 2: Manual Override

**For:** Contracts or Work Orders

**Steps:**
1. Mention discount in Proposal Description
2. Calculate discounted amount
3. Override price in estimate

**Disadvantage:** Doesn't record revenue and discount separately

### Option 3: Discount as Service Line

**For:** Work Orders ONLY

**Steps:**
1. Create discount item in catalog
2. Duplicate service in estimate
3. Rename services (one normal, other "Discount")
4. Add all items to normal service
5. Add discount item to "Discount" service
6. ⚠️ Ensure **Separate Work Ticket** is NOT selected

---

## Sub Auto Expenses

### What is it?
Automatically generates expense items in Purchasing Assistant when subcontractors complete work.

**Useful for:** Snow services, subcontracted equipment

### Fee Types

| Fee Type | Description |
|----------|-------------|
| **Flat Fee** | Fixed amount per ticket (e.g., $100 per plow) |
| **Hourly** | Hourly rate × Reported hours |
| **Catalog Item** | Cost per unit (e.g., $200 per ton of salt) |

### How to Configure

**In Estimate:**
1. Open Service Detail screen
2. "Add Subcontractor Auto Expense"
3. Select Company (vendor)
4. Select Fee Type
5. Enter Amount

**In Company Screen:**
1. Properties module → Company
2. Auto Expense section
3. Use Auto Expense Wizard for bulk creation

---

## Bulk Actions in Opportunities

From Opportunities search screen:

| Bulk Action | Function |
|-------------|---------|
| **Change Sales Rep** | Change designated sales rep |
| **Change Operations Manager** | Change ops manager |
| **Change Anticipated Close Date** | Update expected "Won" date |
| **Change Probability** | Update % probability of winning |
| **Won** | Mark multiple as won |
| **Lost** | Mark multiple as lost |
| **Email** | Send bulk proposals |
| **Add/Remove Tags** | Add/remove tags |
| **Renew** | Renew contracts (only for contracts 12 months or less) |

---

## Estimating: Advanced Concepts

### Payment Schedule (Fixed Payment)

**For:** Fixed Payment Contracts

**Function:** Defines when and how much to bill each month

**Fields:**
- **Invoice on:** First/Middle/Last of the Month
- **Link Completed Tickets to Invoice:** Ties invoice to completed tickets
- **Month checkboxes:** Include/exclude months
- **Invoice Amount:** Editable per month
- **Spread Evenly:** Distributes balance equally
- **Spread and Round:** Rounds to nearest dollar

**⚠️ Important:** Schedule $ must equal Contract $ to save

### Schedule of Values (SOV) - FPOB Only

**Function:** Breakdown of project budget into itemized lines

**When to use:** Work Orders with Fixed Price Open Billing

**Features:**
- Editable while in Bidding
- After winning: only NOT invoiced lines are editable
- Total difference must = zero to save

**Master SOV:** Consolidates SOV from work order + all won change orders

### General Conditions (Work Orders Only)

**Function:** Apply general conditions to work order estimates

**Common items:**
- Project Manager hours
- Safety equipment
- Site trailers
- Insurance costs

**How it works:**
1. Aspire calculates GC costs
2. Distributes costs proportionally among services based on estimated hours
3. Applies markups according to pricing model

### One Time Items

**Function:** Add items NOT in your catalog

**Example:** Customer wants outdoor TV in pergola (not something you normally do)

**Steps:**
1. In estimate → **New One Time Item**
2. (Optional) Pre-fill from similar item
3. Select Category, Unit Type, Item Type
4. Enter Item Cost
5. (Optional) Check "Add to Catalog"

---

## Change Orders (Work Orders Only)

### When to Use?

**For:** Adjust already approved Work Orders

**Types of changes:**
- Modify existing services
- Add new services
- Remove services
- Change quantities/prices

### Process

1. Opportunity (In Process status) → Three-dot menu → **Add Change Order**
2. Change Order table appears on opportunity screen
3. Click Change Order 1 to open Estimate Screen
4. Make changes:
   - **Change:** Modify existing service
   - **Copy:** Duplicate service
   - **Delete:** Remove service (will use negative quantities)
5. **Print or Email Proposal** to send
6. **Won** to approve

**⚠️ Once won, you CANNOT undo it.** You'll need another change order to correct.

### For FPOB: Schedule of Values

When winning change order, Aspire asks to confirm new Schedule of Values

---

## Contract Renewals

**Permission:** Annual Renewals

### Process

1. Opportunity (Contract, 12 months or less) → Three-dot menu → **Renew**
2. Aspire creates new opportunity linked via Master Job field
3. During renewal, you can:
   - Update takeoffs
   - Update service names
   - **Update prices** with current costs
   - Update checklists
   - Update routing/sequence

### Contract Renewal Report

**Location:** Reports → Standard Reports → Sales → Contract Renewals

**Cutoff filter:** Default 45 days before today

**Shows contracts that meet:**
- Start date in past
- No end date, OR renewal date not before cutoff, OR end date not before cutoff

---

## Changes to Active Contracts (Contract Changes)

**⚠️ Recommendation:** Avoid changing number of occurrences. Instead, cancel original contract and create new one.

### Process

1. Opportunity (In Process, no pending revisions) → **Change**
2. Set **New Revision Start Date** (must be after current start date, before end date)
3. Status changes to **Changes Pending**
4. Make changes:
   - **Add New Service:** + icon
   - **Remove Service:** Three-dot menu on service
   - **Edit Service:** Click on service
5. **Win Contract Change** when finished

### What Aspire Does When Winning

**Removed services:**
- Cancels Open/Scheduled tickets without time/materials
- Service is marked Inactive (grayed out)

**Added services:**
- Generates new tickets with new version number

**Updated services:**
- Moves Open/Scheduled tickets from selected occurrence to new version

**Increased occurrences:**
- Adds tickets, Anticipated Start Date = last existing ticket

**Reduced occurrences:**
- Cancels Open/Scheduled tickets from end until reaching new number

---

## Mid-Year Contract Cancellation

### Process (7 Steps)

1. **Determine cancellation date** (last service date)
2. **Invoice customer** for services before that date
3. **Cancel contract:** Three-dot menu → Cancel
4. **Validate:** Status should change to Cancelled
5. **Complete or cancel tickets** scheduled before cancellation date
6. **Handle credit balance** (credit memo if refund)
7. **Review adjustments** in End of Month Report

**⚠️ Important:** Aspire does NOT automatically cancel tickets before the date. You must do it manually.

---

## Gantt Charts (Work Orders Only)

**Function:** Visual project management for Construction/Design/Build

**Shows:**
- Opportunity timeline
- Individual work tickets
- Appointments, Tasks, Issues, Milestones

**Color Legend:**

| Color | What It Represents |
|-------|----------------|
| **Yellow Lines** | Planned Start/End dates |
| **Light Grey** | Work Order Start/End Dates |
| **Dark Grey** | Work Order WIP + Estimated Hours |
| **Light Green** | Work Ticket Estimated Start/End |
| **Dark Green** | Work Ticket WIP + Estimated Hours |
| **Blue + Yellow** | Appointments/Tasks |
| **Yellow Diamond** | Due Dates (Milestones/Issues) |

---

## Electronic Signatures

**Function:** Customers sign proposals digitally

### Setup (Admin)

**Profile Icon → Administration → Configuration → Electronic Signature tab**

**Key fields:**
- Enable Electronic Signatures
- Email Subject/Body (with tokens)
- Confirmation Message

### Send Proposal with E-Signature

1. Email Proposal → Check **Enable Electronic Signature**
2. Customer receives email with link
3. Customer opens link, enters email + job number
4. Proposal displays with "Sign Proposal" button
5. Customer signs (mouse, finger, stylus)
6. Sales Rep receives confirmation email
7. Sales Rep marks opportunity as **Won**

**Note:** If you Reset to Bidding, electronic signature is removed. Customer must sign again.

---

## Key Permissions

| Permission | What For |
|---------|----------|
| **View Opportunities / View My Opportunities** | View opportunities |
| **Edit Opportunities / Edit My Opportunities** | Edit opportunities, create estimates |
| **Add Opportunity** | Create opportunities from properties |
| **Win Contracts / Win Work Orders** | Mark as Won |
| **Lose Opportunities** | Mark as Lost |
| **Change Contract Opportunity** | Make contract revisions |
| **Change Opportunity** | Add change orders |
| **Allow Negative Item Quantity** | Negative quantities in change orders |
| **Annual Renewals** | Renew contracts |
| **Job Dashboard** | View Job Dashboard |
| **Import Estimate** | Import from CSV/XLSX |
| **Allow One-Time Items** | Add non-catalog items |
| **Modify SOV After Opportunity is Won** | Edit SOV after winning FPOB |

---

## Tips and Best Practices

✅ **Contracts: Maximum 12 months** between start/end date

✅ **Use tags** to organize opportunities (division, type, year)

✅ **Consistent naming convention:** "Service Type - Property Name - Year"

✅ **Payment schedules:** Ensure Schedule $ = Contract $

✅ **Change orders:** Document reason in Description

✅ **Multi-year contracts:** Create 12 months + renew annually

❌ **DON'T change occurrences** in contract changes - cancel and create new

❌ **DON'T mark Won** without confirming with customer first

❌ **DON'T edit SOV after invoicing** lines (system won't allow it)

❌ **DON'T use more than 12 months** for mid-month start contracts

---

**Source:** https://guide.youraspire.com/docs/opportunities-1
