# Work Tickets Module (Invoices)

**System URL:** https://cloud.youraspire.com/

---

## What is a Work Ticket?

A **Work Ticket** represents an individual work order: a job or task that your company was hired to perform.

**Automatic creation:** Work tickets are generated automatically when:
- You win an opportunity
- Each service in the estimate generates its own tickets
- "As Needed" services are created manually during the season

---

## Work Ticket Lifecycle

```
Open → Scheduled → Complete
  ↓                    ↓
Cancelled    Pending Approval (only if service requires approval)
```

### Status Explained

| Status | What it means | When it happens |
|--------|--------------|---------------|
| **Open** | Ticket created, not scheduled | When opportunity is won |
| **Scheduled** | Assigned to Schedule Board | Team schedules it |
| **Pending Approval** | Awaiting approval | Services requiring approval after completion |
| **Complete** | Work finished | Crew marks it complete |
| **Cancelled** | Won't be performed | Manually cancelled |

**Important note:** When completing a ticket, if the Property Account Owner marks it complete, services requiring approval are automatically approved (unless you disable "Automatic Ticket Approval" in Administration > Configuration).

---

## Work Ticket Actions

### Work Tickets Screen

**Location:** Work Tickets Module  
**Function:** List of all work tickets in your system

**Additional quick filters:**
- By Status
- By Service
- By Vendor
- By Time

### Bulk Actions

Select multiple tickets → **Bulk Actions** → choose action:

| Action | What it does | Requirement |
|--------|----------|-----------|
| **Complete** | Completes selected tickets | Status Open/Scheduled, no unapproved time/materials |
| **Uncomplete** | Returns tickets to Scheduled (or Open if no visits) | - |
| **Approve** | Approves tickets in Pending Approval | No unapproved time/materials |
| **Cancel** | Cancels selected tickets | No unapproved time/materials; does NOT work for Fixed Price on Payment Schedule, Fixed Price on Completion, Fixed Price Open Billing |
| **Anticipated Start Date** | Changes scheduled date | Tickets in Open |
| **Email** | Sends email to contacts | - |
| **Print** | Generates PDF | - |
| **Uncancel** | Restores cancelled tickets | - |
| **Delete As Needed Tickets** | Deletes As Needed tickets | - |
| **Swap As Needed Service** | Changes As Needed service | Useful for snow |
| **Partial Occurrence** | Reduces % of work completed | Invoice type Per Service, incomplete tickets |
| **Trigger Auto Expense Creation** | Generates purchase receipts for subcontractors | Fixed Payment services, with configured auto-expenses |

**⚠️ Important restriction:** Tickets can only be completed or approved if the month is NOT closed in Aspire.

---

## Complete vs. Cancel Tickets

### When to COMPLETE a ticket?

- The service was performed
- The service was NOT performed but you still need to charge (e.g., Fixed Payment)
  - Example: Fixed Payment lawn maintenance contract. Extreme weather event prevents service that month. Client doesn't cancel the contract, so you still bill. You must mark the ticket as **Complete** to maintain revenue.

### When to CANCEL a ticket?

You can only cancel if:
- You have a ticket with invoice type **Per Service** or **T&M**
- The opportunity associated with **Fixed Payment** was cancelled

**Reasons to cancel:**
1. You won't bill the client for the service (Per Service, T&M, As Needed)
2. The associated contract was cancelled and service won't be provided

**⚠️ Cancelling tickets automatically removes them from the Schedule Board.**

### Comparison Table: Complete or Cancel?

| Invoice Type | Complete | Cancel |
|-------------|-----------|----------|
| **Fixed Payment** | ✅ Yes | ❌ No (only if you cancel the opportunity first) |
| **Per Service** | ✅ Yes | ✅ Yes |
| **T&M** | ✅ Yes | ✅ Yes |
| **Fixed Price on Payment Schedule** | ✅ Yes | ❌ No (only if you cancel the opportunity first) |
| **T&M on Completion** | ✅ Yes | ✅ Yes |
| **Fixed Price on Completion** | ✅ Yes | ❌ No |
| **Fixed Price Open Billing** | ✅ Yes | ❌ No (only if you cancel the opportunity first) |

---

## How to Cancel Tickets

### For Fixed Payment (after cancelling the opportunity)

1. Go to **Work Tickets module**
2. Select the ticket to cancel
3. Three-dot menu → **Cancel**
4. Update **Payment Schedule** if needed
5. Select a **Cancel Reason**
6. **Save**

### For Per Service or T&M

1. Go to **Work Tickets module**
2. Select the ticket to cancel
3. Three-dot menu → **Cancel**
4. Select a **Cancel Reason**
5. **Save**

**Notes:**
- Cancel option only appears if ticket is in **Open** or **Scheduled**
- When you **Uncancel**, the cancel reason is removed
- You need permission: **Cancel Work Ticket**

---

## Dynamic Forecasting Tab

**Required permission:** View Dynamic Forecast or Edit Dynamic Forecasting

### What is it?

Tool to manage and analyze forecast data at the ticket level. Shows:
- Projected revenue
- Labor hours
- Material costs

### Structure

3 sub-tabs:
- **Revenue:** Forecasts entered as **% of estimate** in dollars
- **Hours:** Forecasts entered in **hours**
- **Materials:** Forecasts entered as **% of estimate** in dollars

### How It Works

**Default columns:**

| Section | Content |
|---------|-----------|
| **Left** | Opportunity #, Work Ticket #, Service name |
| **Center** | 12 months of data (past/present/future) |
| **Right** | Totals: Estimated, Earned, Remaining |

**Editing rules:**
- Past months: **Locked** (actual values)
- Current month: Shows actuals + editable forecasts
- Future months: All editable

**⚠️ Warning:** If you enter an amount exceeding the estimate, a warning icon appears showing the difference.

### Practical Example

**Ticket with:**
- Price: $10,000
- Hours: 100
- Material spend: $3,000

**Forecast:**

| Month | Revenue | Hours | Materials |
|-----|---------|-------|-----------|
| January | 25% = $2,500 | 25 hrs | $1,500 |
| February | 25% = $2,500 | 50 hrs | $1,500 |
| March | 50% = $5,000 | 25 hrs | $0 |

---

## Multi-Year Contracts

When you win a multi-year contract opportunity:
- Aspire creates **all work tickets** if you provided an end date
- For contracts without end date (open-ended): creates up to **2 years** of tickets
  - You'll need to add an end date and renew when less than 1 year remains

---

## Tips and Best Practices

✅ **Complete tickets even if service wasn't performed** if you need the revenue (Fixed Payment)

✅ **Cancel tickets before closing the month** if service is postponed (Per Service/T&M)

✅ **Use Dynamic Forecasting** to project revenue, hours, and materials month by month

✅ **Review Pending Approval regularly** to approve completed services

❌ **Don't cancel Fixed Price on Completion tickets** - adjust the contract instead

❌ **Don't try to complete/approve tickets in closed months** - the system will reject it

---

## Required Permissions

| Action | Required Permission |
|--------|-------------------|
| Complete tickets | **Complete Work Ticket** |
| Cancel tickets | **Cancel Work Ticket** |
| Approve tickets | **Approve Work Ticket** or **System Admin** |
| View Dynamic Forecasting | **View Dynamic Forecast** |
| Edit Dynamic Forecasting | **Edit Dynamic Forecasting** |

---

**Source:** https://guide.youraspire.com/docs/understanding-scheduling-in-aspire
