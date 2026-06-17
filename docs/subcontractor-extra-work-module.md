# Subcontractor Extra Work — Module

*Last updated: June 2026 | Source: Maddie Wheeler (Aspire Admin) — Office Hours June 4, 2026 + CAM Subcontractor Extra Work Assignment SOP*

---

## Overview

This module covers the end-to-end process for extra work assignments that involve subcontractors — from the initial client approval through to the client invoice being sent. It spans multiple teams (Operations, OST, CSC, Accounting) and multiple Aspire modules (Opportunities, Work Tickets, Invoicing). Because the workflow touches so many areas, sequence matters enormously. Steps performed out of order routinely cause billing errors, unsent invoices, or overpaid subcontractors.

**Teams involved:**
- **Operations Manager** — requests extra work, schedules and completes the work ticket
- **CSC (Client Success Center)** — receives the extra work request form, notifies OST
- **OST (Operations Support Team)** — manages subcontractor bidding, assignment, and purchase receipt (PR) creation; led by RJ (Operations Support Manager)
- **Accounting / Process Smart** — processes weekly invoicing batches for extra work

> ⚠️ **Process Smart** is CAM's outsourced process automation vendor. They handle the weekly extra work invoicing batch run — they are "as close as we can get to automation" of that step, but it still requires human oversight and is not fully automatic.

---

## 1. Extra Work Workflow — Full Sequence

### Step 1: Client Approval & Extra Work Request

- The client approves an extra work order.
- The Operations Manager submits a **CSC Form** (via Monday.com) to initiate the request internally.
- The CSC Form must include: scope of work, property, and urgency level.

> ⚠️ **Even if the client has provided their own estimated amount, the request must still go through the CSC Form process** for internal evaluation, bidding, and assignment. Client estimates do not bypass the internal workflow.

> 📋 **Known gap:** The specific required fields on the CSC Form have not yet been captured in this document. Follow up with Maddie Wheeler to obtain the form template or the notification email that lists all required fields.

---

### Step 2: CSC Notifies OST

- Upon receiving the CSC Form, CSC notifies OST of the approved extra work opportunity via **Monday.com**.
- OST reviews the request for completeness and scope clarity before proceeding.

---

### Step 3: Subcontractor Bidding & Selection

- OST (led by RJ) emails bid requests to **2–3 qualified subcontractors** in the relevant division.
- Each bid request includes: scope of work, property/location, timeline expectations, and any special instructions.

**Bid deadlines:**
- Non-urgent work: **48 hours**
- Urgent work: **24 hours**
- Critical/emergency work (board-ups, broken water lines, emergency hauling): **phone call for immediate quotes**

**Selection criteria (best overall value — not always lowest price):**
- Scope alignment
- Past performance
- Availability
- Cost

- OST formally assigns the job to the selected subcontractor **via email**.

---

### Step 4: Extra Work Opportunity Created in Aspire

- OST creates the **extra work opportunity** in Aspire. This includes:
  - Estimate
  - Contract setup
  - Work ticket
- The Operations Manager is notified that the opportunity has been accepted and is ready to schedule.

> 📋 **Known gap:** The exact notification method/flow from OST to the Operations Manager was recently changed. The current state has not been fully confirmed. Verify with RJ or OST before relying on this step for training.

---

### Step 5: Purchase Receipt (PR) Created

- OST creates a **Purchase Receipt (PR)** on the work ticket in Aspire.
- The PR is given to the subcontractor. The subcontractor **must include both the PR number and the work ticket number** on their invoice when they submit it to CAM for payment.

> ⚠️ **Missing PR or work ticket number on a sub invoice will cause processing delays.** Subcontractors who fail to include these may experience payment delays or denials.

---

### Step 6: Ticket Scheduled by Operations Manager

- The Operations Manager places the work ticket on the **schedule board** in Aspire.
- The ticket moves to **Scheduled** status.

---

### Step 7: Subcontractor Completes the Work

Subcontractors are required to:
- Complete all work according to the approved scope
- Finish within the confirmed timeline
- Follow CAM quality and safety standards
- Immediately notify OST of any delays, scope changes, or site issues
- **Submit clear completion photos** upon finishing — no photos = no payment

**Subcontractors may not:**
- Perform work outside the approved scope without a written change order from OST
- Communicate directly with the client about pricing, scope, or additional work

---

### Step 8: Operations Manager Completes the Work Ticket

- Once the work is performed, the Operations Manager **completes the work ticket** in Aspire.
- For **Fixed Price on Completion (FPOB)** jobs — the most common extra work type — completing the ticket is what **triggers the invoice to appear in Invoicing Assistant**.
- For **Fixed Payment** contracts, the invoice generates automatically on schedule regardless of ticket completion.

> ⚠️ **This is one of the most common failure points.** If the Operations Manager does not complete the ticket, the invoice never reaches the invoicing inbox and never gets sent to the client. Delayed or missing ticket completions were a significant contributor to the unsent invoice issues earlier in 2026.

---

### Step 9: Subcontractor Submits Invoice to CAM

- The subcontractor submits their invoice to CAM, including the PR number and work ticket number.
- OST processes the sub invoice against the PR using the **sub invoice reconciliation process** (see Section 3 below).

---

### Step 10: Client Invoice Sent

- Extra work invoices are sent to clients on a **weekly basis**, processed by **Process Smart**.
- This is a manual batch process, not fully automated.
- Invoices that appeared late in the Invoicing Assistant inbox (due to delayed ticket completion or late contract renewal) may be missed if the inbox is not actively monitored.

> ⚠️ **Active monitoring of the Invoicing Assistant inbox is required.** Do not assume everything that appears will be caught in the weekly batch — invoices that land between batch runs need to be caught on the next cycle.

---

## 2. Subcontractor Rules & Payment Enforcement

### To Get Paid
- Work must be completed per the approved scope
- Completion photos must be submitted and approved by OST
- Invoice must include the PR number and work ticket number

### Performance Consequences
- **No completion photos → No payment**
- **Late completion → Pay deduction** from total job cost
- **Repeated issues → Reduced future work opportunities** with CAM

### Change Orders
- Any work identified beyond the approved scope requires a **change of work order** submitted through OST before proceeding
- No additional work may be started without written OST approval
- Unauthorized additional work will not be paid

---

## 3. Sub Invoice Reconciliation Process

When a subcontractor submits their invoice to CAM, OST must reconcile it against what was estimated and approved in Aspire. This is a separate review step before payment is processed.

The reconciliation focuses on **variances** — cases where the sub's invoice amount is higher than the estimated/PR amount in Aspire. Each variance requires an explicit approval or denial with a documented reason.

Currently this process is managed via a **manually maintained Excel report** that is rebuilt each reconciliation cycle. Known problems with the current state:
- Previous approval/denial decisions and their reasons are not automatically carried forward when the report is rebuilt
- There is no single living document — multiple versions accumulate over time
- The data must be pulled manually from Aspire

**Desired future state (flagged by Maddie Wheeler, June 2026):** An API-connected report that auto-populates from Aspire data, retains and enriches prior decisions rather than replacing them, and surfaces a summary of approved payment history. This has been flagged as a potential automation opportunity for Roberto.

> 📋 **Known gap:** The specific columns and structure of the current Excel reconciliation report have not yet been captured. Review the June 4, 2026 Office Hours recording (screen share segment ~46:00–48:00) to document the column structure before drafting an automated version.

---

## 4. Common Errors & How to Fix Them

### Misapplied Payment (Wrong Property)

**What happens:** A payment is created and assigned to the wrong property (e.g., paid on LAGK 04 when it should have gone to LAGK 05). Once the payment is saved with a "regarding" property assignment, that field becomes **locked and grayed out** — it cannot simply be reassigned.

**Resolution sequence:**
1. Open the payment and unapply it from the incorrect invoice (deselect the invoice, save) — this creates an unapplied credit
2. Attempt to apply the credit directly to the correct invoice; if the "regarding" field is locked to the wrong property, this will not work
3. If locked: delete the payment and recreate it, entering the correct invoice number at creation time so the "regarding" field is assigned to the right property from the start
4. If the invoice amount also needs correction: use **Void and Reset** on the invoice, then edit the extended price
   - Note: editing invoice prices is an exception — not standard practice
5. When completing the invoice batch, remove the email contact so the client does not receive a duplicate notification
6. Refresh and confirm the payment is applied correctly

**Root cause to prevent:** The "regarding" (property assignment) field on a payment is locked once saved. Always confirm the correct property before saving a new payment.

---

### Premature or Bulk Ticket Completion

**What happens:** An Operations Manager completes all work tickets on a contract at once — or completes them daily instead of weekly — rather than completing them according to the actual service schedule. This floods the Invoicing Assistant with incorrect billing triggers and corrupts the contract's P&L data.

**Correct practice:** For in-house recurring contracts, one work ticket should exist per scheduled service period (typically weekly). All hours for that period are logged on that single ticket. The ticket is completed only when that service period's work is actually done — not in advance, and not one ticket per visit.

**Example:** A property visited 5x/week for 3 hours per visit = one weekly ticket with 15 hours. Not five tickets with 3 hours each.

**Scheduling best practice (from Maddie Wheeler):** Biweekly scheduling (26 occurrences/year) is preferred over "2 times per month" (24 occurrences/year). Biweekly is simpler to set up in Aspire, more predictable, and avoids edge cases with variable month lengths. Advocate for biweekly framing with clients wherever possible.

**How to fix premature completions:**
1. Work tickets cannot be uncompleted in bulk — each ticket must be uncompleted individually
2. Build a master list of all incorrectly completed tickets
3. Assign the uncompleting work to James Martin (Aspire expert) for efficiency
4. Once tickets are uncompleted, make the necessary contract corrections or addendums
5. Consider temporarily restricting the user's ticket completion permissions in Aspire (role: Production Supervisor + Time Entry) until training is completed

---

### Invoice Not Reaching the Client

**Common causes (in order of frequency):**
1. Operations Manager did not complete the work ticket (required for FPOB and Per Service invoice types)
2. Contract was renewed late — the invoice appeared in Invoicing Assistant but was not noticed before the weekly batch ran
3. Contract was not renewed at all — no invoice was ever generated
4. Contract renewed at wrong price (missing CPI increase) — invoice sent but for wrong amount
5. Duplicate contract created during renewal — payment applied to wrong contract

**Prevention:** Actively monitor the Invoicing Assistant inbox between weekly batch runs. Contracts renewed mid-cycle or late require manual attention to ensure their invoices are caught and sent.

---

## 5. Contract Renewal Context

Several of the billing issues in early 2026 originated in the January contract renewal cycle. Key facts for context:

- CAM's contracts renew January 1st annually (~1,300 contracts)
- The person responsible for renewals left in December 2025, creating a knowledge gap at the worst possible time
- Process Smart handled renewals in bulk, but exceptions and special cases were not properly separated out — resulting in duplicate contracts, wrong prices, and some contracts not renewed
- Contracts that were not properly terminated and restarted on January 1st may expire mid-year (April, May, etc.); SAC pulls monthly reports to catch and renew these on a rolling basis

> 📋 **Known gap:** The identity and role of "SAC" (referenced by Maddie as pulling the monthly expiring contracts report) has not been confirmed. Verify before next documentation update.

**Going forward:** CAM now begins reviewing contracts for the next renewal cycle approximately two months before January 1st — sending CPI letters, flagging special cases for separate handling, and identifying contracts that need to be canceled and restarted vs. simply renewed.

---

## 6. Aspire Behaviors to Know

These are non-obvious system behaviors that affect this workflow:

| Behavior | Detail |
|---|---|
| Payment "regarding" field locks on save | Once a payment is saved with a property assignment, it cannot be reassigned. Must delete and recreate to fix. |
| FPOB invoices require ticket completion | Fixed Price on Completion invoices only appear in Invoicing Assistant after the work ticket is completed by the ops manager. |
| Fixed Payment invoices are automatic | Fixed Payment contract invoices generate on schedule regardless of ticket completion — no ops action required. |
| Ticket completion cannot be bulk-undone | Uncompleting incorrectly completed tickets must be done one at a time. |
| In-house ↔ Sub switches require contract cancellation | Aspire does not handle frequency/ticket count changes on an existing contract well. Standard practice is to cancel the contract (with reason "sub to in-house" or "in-house to sub") and create a new one. This is a technical cancellation, not a client cancellation. |
| Invoice batch email can be overridden | When completing an invoice batch for a corrected invoice you don't want to resend, remove the email contact from the batch before completing it. |

---

## 7. Key Principle (from Maddie Wheeler)

> *"All the actions you take have downstream consequences. The system is entirely connected — from the first contact created all the way to when we bill the customer. Any choices or changes you make in the system can have profound consequences later."*

This is the single most important thing to understand before working in Aspire. Precision and attention to detail at every step are not optional — errors made early in the workflow (at contract setup, at ticket creation, at payment entry) compound into billing problems, data integrity issues, and hours of remediation work downstream.

---

*For questions about this workflow, contact Maddie Wheeler (Aspire Admin) or RJ (Operations Support Manager). For Aspire system questions, see also: `worktickets-module.md`, `invoices-module.md`, `opportunities-module.md`.*
