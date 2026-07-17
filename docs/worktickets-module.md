# Work Tickets Module (Aspire)

System URL: https://cloud.youraspire.com/

*Covers the full life of a work ticket: what it is, its status lifecycle, how to make changes to a ticket (with individual, per-ticket actions as the priority), when to complete vs. cancel, how to find and monitor tickets, and Dynamic Forecasting. Structure based on the Aspire Academy Scheduling chapter (course 306), enriched with operational depth from the reference documentation.*

> **CAM internal practice:** Make changes to work tickets **individually, one ticket at a time** — open the specific ticket and act on it. Bulk Actions exist and are documented here for reference, but CAM prefers individual changes because they are deliberate and verifiable. Treat Bulk Actions as the exception, not the default.

---

## What is a Work Ticket?

A **work ticket** represents an individual work order: a job or task your company was hired to perform.

**Automatic creation:** work tickets are generated automatically when:
- You **win an opportunity** (each service on the approved estimate generates its own ticket).
- "As Needed" services are created manually during the season (they don't auto-generate a ticket until requested).

When first created, a ticket is in **Open** status and is not yet on the schedule board.

---

## Work Ticket Lifecycle & Statuses

```
Open → Scheduled → (Pending Approval) → Complete
  │                                          
  └──────────────► Cancelled                 
```

| Status | What it means | When it happens |
|--------|--------------|---------------|
| **Open** | First status a ticket receives. Generated when an opportunity is won, based on the approved estimate. Not yet on the schedule board. | When opportunity is won |
| **Scheduled** | The ticket has been placed on the schedule board. | Team schedules it |
| **Pending Approval** | Crew completed the work, but (in systems configured to require it) the ticket needs approval before completion. Some services require approval; others go straight to Complete. | After completion, for services requiring approval |
| **Complete** | Work finished and approved; ready for invoicing. | Crew/office marks it complete |
| **Cancelled** | Won't be performed. | Manually cancelled |

**Why status matters:** a ticket left in an early status means work not done or money not billed. A ticket stuck in **Scheduled** is potential lost revenue — find what's blocking it (future visit? backordered materials?) and act.

**Whether a ticket routes through Pending Approval** depends on **per-service system configuration.** When completing a ticket, if the Property Account Owner marks it complete, services requiring approval are automatically approved — unless "Automatic Ticket Approval" is disabled in Administration → Configuration.

**Scheduled start date** is driven by the opportunity start/end date, or for contracts by the **service schedule** of the service type on the ticket (Aspire uses service schedules to spread work across the life of the contract).

---

## Making Changes to a Work Ticket — Individual Actions (PRIORITY)

**This is the preferred way to change a ticket at CAM: open the individual ticket and act on it directly.** Each action below is described for a single ticket.

**How to open a single work ticket:** Work Ticket icon on the blue side menu → use the search bar or filters (Status / Service / Ticket Date) to find the ticket → click it to open the Work Ticket screen. From there, use the ticket's **three-dot menu** for the actions below.

### Complete a work ticket

**Conditions that must be met to complete a ticket:**
- The ticket must be in **Open** or **Scheduled** status.
- There must be **no unapproved time or materials** on the ticket.
- The **accounting month must be open** (tickets cannot be completed in a closed month).

**Steps (individual):**
1. Open the work ticket.
2. Three-dot menu → **Complete**.
3. If the service requires approval and you have the right permission, it may complete-and-approve in one step; otherwise it moves to **Pending Approval**.

> You complete a ticket when the service was performed — **or** when the service was NOT performed but you still need to bill it (e.g., a Fixed Payment contract where weather stopped service that month but the client is still billed). ⚠️ *[VERIFY the exact individual-complete click path in your Aspire instance — the concept and conditions are confirmed; the per-ticket menu wording may differ slightly.]*

### Approve a work ticket (in Pending Approval)

**Conditions:** ticket is in **Pending Approval**; **no unapproved time/materials**; open month.

1. Open the work ticket.
2. Three-dot menu → **Approve**.
3. Status moves to **Complete**, ready for invoicing.

### Uncomplete a work ticket (reopen)

Returns a completed ticket to **Scheduled** (or **Open** if it has no visits).
1. Open the ticket → three-dot menu → **Uncomplete**.
2. Use this to correct a ticket completed by mistake, or to add/fix time or materials.

### Cancel a work ticket

⚠️ **Cancelling is only allowed for certain invoice types — see "Complete vs. Cancel" below.** Cancelling removes the ticket from the schedule board.

**Conditions:** ticket in **Open** or **Scheduled**; no unapproved time/materials; the invoice type must allow cancellation (Per Service / T&M, or a Fixed Payment ticket whose opportunity was already cancelled).

**Steps (individual):**
1. Open the work ticket.
2. Three-dot menu → **Cancel**.
3. (For Fixed Payment, after the opportunity was cancelled) update the **Payment Schedule** if needed.
4. Select a **Cancel Reason** → **Save**.

> The Cancel option only appears if the ticket is in Open or Scheduled. Requires the **Cancel Work Ticket** permission.

### Uncancel a work ticket (restore)

1. Open the cancelled ticket → three-dot menu → **Uncancel**.
2. The cancel reason is removed and the ticket returns to its prior status.

### Change the anticipated start date

For tickets in **Open** status, to change when a ticket is scheduled to start:
1. Open the ticket → three-dot menu → **Anticipated Start Date**.
2. Set the new date → Save.

### Partial Occurrence (reduce % of work completed)

For **Per Service** invoice-type tickets that are incomplete:
1. Open the ticket → three-dot menu → **Partial Occurrence**.
2. Reduce the percentage of work completed as needed.

### Trigger Auto Expense Creation

For **Fixed Payment** services with configured subcontractor auto-expenses: open the ticket → three-dot menu → **Trigger Auto Expense Creation** → generates the purchase receipts for subcontractors.

---

## Complete vs. Cancel — Which and When

The invoice type determines whether a ticket can be cancelled at all.

### When to COMPLETE
- The service was performed, **or**
- The service was NOT performed but you still need to charge (e.g., **Fixed Payment** — mark Complete to maintain revenue even if weather stopped the visit).

### When to CANCEL
Only when:
- The ticket's invoice type is **Per Service** or **T&M** (you won't bill for the service), **or**
- The associated **Fixed Payment** opportunity was cancelled and the service won't be provided.

### Comparison table

| Invoice Type | Complete | Cancel |
|-------------|-----------|----------|
| **Fixed Payment** | ✅ Yes | ❌ No (only if you cancel the opportunity first) |
| **Per Service** | ✅ Yes | ✅ Yes |
| **T&M** | ✅ Yes | ✅ Yes |
| **Fixed Price on Payment Schedule** | ✅ Yes | ❌ No (only if you cancel the opportunity first) |
| **T&M on Completion** | ✅ Yes | ✅ Yes |
| **Fixed Price on Completion** | ✅ Yes | ❌ No |
| **Fixed Price Open Billing** | ✅ Yes | ❌ No (only if you cancel the opportunity first) |

### How to cancel by scenario (individual)

**Fixed Payment (after cancelling the opportunity):** open ticket → three-dot → Cancel → update Payment Schedule if needed → select Cancel Reason → Save.

**Per Service or T&M:** open ticket → three-dot → Cancel → select Cancel Reason → Save.

---

## Why Can't I Change This Ticket? (Troubleshooting)

If an action (complete, cancel, approve, modify) is blocked, check these in order:

1. **Closed month** — tickets can only be completed or approved if the accounting month is **not closed** in Aspire. This is the most common blocker.
2. **Unapproved time or materials** — complete, approve, and cancel all require no unapproved time/materials on the ticket. Approve or resolve those first.
3. **Wrong status** — Cancel only appears in Open/Scheduled. Anticipated Start Date changes apply to Open tickets.
4. **Invoice type doesn't allow cancel** — Fixed Price on Completion, FP on Payment Schedule, and FPOB tickets cannot be cancelled directly (adjust the contract/opportunity instead).
5. **Missing permission** — see Permissions below (e.g., Cancel Work Ticket, Approve Work Ticket).

---

## Finding & Monitoring Work Tickets

Daily review of work ticket lists is the core habit that keeps work scheduled and billed. **Reviewing the Open, Scheduled, Pending Approval, and Complete lists daily makes end-of-month smoother.**

### Default system lists for Open work tickets

| List | What it shows | Priority |
|---|---|---|
| **Open Contract Thru Today** | Contract tickets promised to be done by today but not yet scheduled | Highest — review daily |
| **Open Work Order Thru Today** | Work order tickets that should already have been scheduled | High — review daily |
| **Open Contract Next 30 Days** | Upcoming contract tickets | Schedule near the start date |
| **Open Work Order Next 30 Days** | Upcoming work order tickets | Schedule near the start date |

### View tickets that need scheduling (Schedule Board)
1. Dashboard → **Scheduling** icon on the blue side menu (opens the schedule board).
2. Click the **clipboard icon** (upper-right of the schedule board) to display work tickets.
3. Click the **caret just below the X** to expand the list and reveal more columns.
4. Select one of the default Open lists to find tickets that need scheduling.

### Monitor Scheduled / Pending Approval / Complete (Work Ticket module)
1. **Work Ticket** icon on the blue side menu.
2. Filter with the drop-downs under the search bar: **Status**, **Service**, **Ticket Date**.
3. **Review scheduled work:** Status = Scheduled, Service = all, Date = Thru Today. Investigate any ticket still scheduled (future visits? backordered materials?).
4. **Review work ready to invoice:** List drop-down → **Pending Approval Thru Today**. Review once or twice daily — check material allocations and compare estimated vs. actual hours/costs.
5. **Review completed work:** List drop-down → **Default All Tickets**, filter to Complete, Ticket Date = This Month. Catches discrepancies and refines job costing.

> Each company sets its own scheduling cadence — some schedule all won tickets immediately, others 6–8 weeks out. Agree on a cadence as a team.

---

## Dynamic Forecasting

**Required permission:** View Dynamic Forecast or Edit Dynamic Forecasting.

A tool to manage and analyze forecast data at the ticket level: projected **revenue**, **labor hours**, and **material costs**.

**Three sub-tabs:** Revenue (entered as % of estimate in dollars), Hours (entered in hours), Materials (entered as % of estimate in dollars).

**Layout:** Left = Opportunity #, Work Ticket #, Service name. Center = 12 months of data. Right = totals (Estimated, Earned, Remaining).

**Editing rules:** past months locked (actuals); current month shows actuals + editable forecasts; future months fully editable. ⚠️ Entering an amount exceeding the estimate shows a warning icon with the difference.

**Example** — ticket priced $10,000, 100 hours, $3,000 materials:

| Month | Revenue | Hours | Materials |
|-----|---------|-------|-----------|
| January | 25% = $2,500 | 25 hrs | $1,500 |
| February | 25% = $2,500 | 50 hrs | $1,500 |
| March | 50% = $5,000 | 25 hrs | $0 |

---

## Multi-Year Contracts

When you win a multi-year contract opportunity:
- Aspire creates **all work tickets** if you provided an end date.
- For open-ended contracts (no end date): creates up to **2 years** of tickets; you'll need to add an end date and renew when less than 1 year remains.

---

## Bulk Actions (Reference Only — CAM Prefers Individual Actions)

> ⚠️ **CAM internal practice: avoid Bulk Actions for routine changes.** Bulk operations can complete, cancel, or approve the wrong tickets at scale. Use the **individual per-ticket actions above** as the default. This section exists for reference and for the rare case where a genuine bulk operation is justified and carefully reviewed.

Bulk Actions are accessed from the Work Tickets list: select multiple tickets → **Bulk Actions** → choose an action.

| Action | What it does | Requirement |
|--------|----------|-----------|
| Complete | Completes selected tickets | Open/Scheduled, no unapproved time/materials, open month |
| Uncomplete | Returns tickets to Scheduled (or Open if no visits) | - |
| Approve | Approves tickets in Pending Approval | No unapproved time/materials |
| Cancel | Cancels selected tickets | No unapproved time/materials; NOT for Fixed Price on Payment Schedule, Fixed Price on Completion, FPOB |
| Anticipated Start Date | Changes scheduled date | Tickets in Open |
| Email | Sends email to contacts | - |
| Print | Generates PDF | - |
| Uncancel | Restores cancelled tickets | - |
| Delete As Needed Tickets | Deletes As Needed tickets | - |
| Swap As Needed Service | Changes As Needed service | Useful for snow |
| Partial Occurrence | Reduces % of work completed | Per Service, incomplete tickets |
| Trigger Auto Expense Creation | Generates purchase receipts for subcontractors | Fixed Payment services with configured auto-expenses |

The conditions for each bulk action are the same as for the individual action. The month-closed and unapproved-time/materials rules always apply.

---

## Required Permissions

| Action | Required Permission |
|--------|-------------------|
| Complete tickets | Complete Work Ticket |
| Cancel tickets | Cancel Work Ticket |
| Approve tickets | Approve Work Ticket or System Admin |
| View Dynamic Forecasting | View Dynamic Forecast |
| Edit Dynamic Forecasting | Edit Dynamic Forecasting |

---

## Related (see other modules)

- **Scheduling a ticket, routes, the Schedule Board in depth** → Scheduling module.
- **Completing/handling tickets from Aspire Mobile, time entry, Quick Tickets** → Mobile & Time Entry (Scheduling module).
- **Invoicing a completed ticket** → Invoicing module.

---

## Common Questions (from Aspire Academy)

**Q: What is the first status a work ticket receives when created?**
Open — generated when an opportunity is won, based on the approved estimate. It's not yet on the schedule board.

**Q: How do I complete a work ticket, and what conditions must be met?**
Open the individual ticket → three-dot menu → Complete. Conditions: the ticket must be in Open or Scheduled status, have no unapproved time or materials, and the accounting month must be open. If the service requires approval, it moves to Pending Approval first.

**Q: How do I cancel a work ticket?**
Open the ticket → three-dot → Cancel → choose a Cancel Reason → Save. Cancelling is only allowed for Per Service or T&M tickets (or a Fixed Payment ticket whose opportunity was already cancelled). It requires the Cancel Work Ticket permission and removes the ticket from the schedule board.

**Q: Why can't I complete or cancel a ticket?**
Most often the month is closed, or there's unapproved time/materials on the ticket. Also check the status (Cancel only shows in Open/Scheduled), the invoice type (some can't be cancelled), and your permissions.

**Q: I completed a ticket by mistake — how do I undo it?**
Open the ticket → three-dot → Uncomplete. It returns to Scheduled (or Open if it has no visits).

**Q: Should I use Bulk Actions to complete tickets?**
At CAM, prefer individual per-ticket actions — open each ticket and complete it. Bulk Actions exist but are avoided for routine changes because they can affect the wrong tickets at scale.

**Q: A ticket is stuck in Scheduled — what should I do?**
Find out why and act. It usually means a future visit date or backordered materials. A ticket stuck in Scheduled is potential lost revenue.

**Q: What list should I review to find contract tickets that need scheduling ASAP?**
Open Contract Thru Today (review daily). It shows contract tickets promised by today but not yet scheduled.

**Q: How often should I review the Pending Approval Thru Today list?**
Daily (once or twice). It's how you catch work ready to invoice and check material allocations and estimated-vs-actual hours.

**Q: Do I have to bill a Fixed Payment service that didn't happen?**
If the client isn't cancelling the contract, mark the ticket Complete to maintain revenue — even though the visit didn't occur (e.g., weather).

**Q: What does reviewing completed work tickets help ensure?**
Accurate job costing — comparing estimated vs. actual and catching discrepancies before month-end.
