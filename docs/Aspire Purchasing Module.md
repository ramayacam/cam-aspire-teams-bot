# Aspire Platform – Purchasing Module

Module: Purchasing | Platform: Aspire Cloud  
Source: guide.youraspire.com/docs/purchasing-module-screen-reference

---

## Overview

The Purchasing module in Aspire tracks material and service purchases from vendors. It links vendor invoices (purchase receipts) to work tickets and opportunities, enabling accurate job costing and accounts payable processing.

**Two ways to create purchase receipts:**

| Method | When to use |
|---|---|
| **Purchasing Assistant** | Guided purchasing — Aspire recommends items based on opportunity estimates. Best for materials tied to specific jobs. |
| **Purchase Receipts screen** | Direct creation — for subcontractor expenses, one-off purchases, or managing existing receipts. |

---

## Purchase Receipt Lifecycle (Statuses)

A purchase receipt moves through four statuses:

| Status | Meaning |
|---|---|
| **New** | Receipt created. Quantities and estimated prices can still be edited. |
| **Received** | Materials or services have been received. Received Date is required to advance. |
| **Approved** | Vendor invoice has been received, amounts verified, ready to pay. Invoice Date and Invoice # required to advance. |
| **Complete** | PR has been transmitted to the accounting system (only applies to companies with accounting integration). |

> **Key rule:** You cannot approve a PR without first receiving it. You cannot receive without a Received Date. You cannot approve without an Invoice Date and Invoice #.

---

## Creating a Purchase Receipt

### From the Purchasing Assistant (recommended for material purchases)

1. Go to **Purchasing** → **Purchasing Assistant**
2. Filter by Purchase Date, Service, Category, or Vendor as needed
3. Check the boxes next to the items you want to purchase
4. Click **Bulk Actions** → **Create Purchase...**
5. Select the **Branch** and **Vendor**
6. Click **Save** — Aspire creates the receipt and allocates quantities to their work tickets

### From the Purchase Receipts Screen (direct creation)

1. Go to **Purchasing** → **Purchase Receipts** → **New** dropdown → **Add Purchase Receipt**
2. Fill in required fields: **Branch**, **Vendor**, **Inventory Location**
3. Add line items (from the item catalog or as one-time items)
4. Optionally assign to a **single Work Ticket** (for job-specific purchases)
5. Set **Ship To** address
6. Add **Notes** if needed
7. Click **Save**

### From a Work Ticket (for subcontractor purchase receipts)

1. Open the **Work Ticket**
2. Go to the **Costs** section
3. Click **New Purchase Receipt** (or access via the three-dot menu)
4. Fill in the Vendor and items
5. Save — the PR is automatically linked to that work ticket

> ⚠️ **For CAM's subcontractor workflow:** OST creates the PR on the work ticket and provides the PR number + work ticket number to the subcontractor. The subcontractor **must include both numbers** on their invoice to CAM. Missing either number causes payment delays.

---

## Key Fields on a Purchase Receipt

| Field | Required | Description |
|---|---|---|
| Branch | ✅ | Branch for which the purchase is being made |
| Vendor | ✅ | Vendor supplying the materials/services |
| Inventory Location | ✅ | Required if purchasing to inventory or job inventory |
| Work Ticket | Optional | Links the entire PR to one work ticket. All line items allocated to that ticket. |
| Received Date | Required to Receive | Date materials/services were received |
| Invoice Date | Required to Approve | Date on the vendor's invoice |
| Invoice # | Required to Approve | Vendor's invoice number |
| Receipt Status | Auto | New → Received → Approved → Complete |
| Job Inventory checkbox | Optional | Holds items in job inventory until installed (improves EOM accuracy) |

---

## Processing a Purchase Receipt

### Receiving a PR

When materials arrive or work is confirmed as complete:

1. Open the PR
2. Click **More** → **Receive** (if all items received) or **Receive Partial** (if some items are back-ordered)
3. Enter or confirm the **Received Date**
4. Aspire changes status to **Received**

> For partial receipts: Aspire creates a linked PR for the back-ordered items (e.g., PR #1027 → back-order PR #1027-1).

### Approving a PR

When you have the vendor's invoice and agree with the charges:

1. Open the Received PR
2. Verify or update **Unit Prices** to match the vendor invoice
3. Add any **Extra Costs** (tax, freight, other)
4. Enter **Invoice Date** and **Invoice #**
5. Click **More** → **Approve**
6. Aspire changes status to **Approved** — ready for accounting sync

### Un-receiving or Un-approving

- **Unreceive:** Available on Received PRs. Reverts to New status so quantities can be modified.
- **Unapprove:** Available on Approved PRs. Reverts to Received status so prices or extra costs can be corrected.

---

## Purchasing Assistant

The Purchasing Assistant identifies items from your estimates that need to be ordered. It does **not** auto-remove items once a PR is created — you must manually remove them or filter for items with Quantity to Order > 0.

### Recommended default filter
Set **Quantity to Order — Does Not Equal — 0** as your default view to avoid re-ordering already-purchased items.

### Bulk Actions in Purchasing Assistant

| Action | Description |
|---|---|
| Create Purchase... | Create a new PR for selected items. Select branch and vendor. |
| Allocate from Inventory... | Allocate items from existing inventory to work tickets (no new PR created). |
| Remove from List | Remove items you won't be purchasing through Aspire (e.g., owner-supplied materials). |
| Update Vendor | Reassign the vendor for selected items. |
| Substitute Item | Replace an item with another from the same branch and category. |

---

## Subcontractor Purchase Receipts (CAM-Specific)

For extra work assigned to subcontractors, OST creates the PR on the work ticket before the work begins.

**What the subcontractor must include on their invoice to CAM:**

| Required | Why |
|---|---|
| PR Number | Matches their invoice to the approved work in Aspire |
| Work Ticket Number | Links the invoice to the specific job |
| Approved scope and amount | Prevents billing for unauthorized work |
| Completion photos | No photos = no payment |

**Variance handling (sub invoice > PR amount):**  
OST must explicitly approve or deny any variance before payment is processed. Document the reason for every approval or denial.

> See also: `subcontractor-extra-work-module.md` for the full CAM SOP on subcontractor extra work assignment.

---

## Reviewing Purchase Receipts (Weekly Best Practice)

Review the PR list weekly:

1. **New status, older than 15 days** — follow up on whether materials have been received
2. **Received status, awaiting vendor invoice** — follow up for timely approval
3. **Approved totals** — verify they match what was sent to the accounting system for the month
4. **Accounting system** — confirm bills are present and reconciled

> The benchmark metric: any PR in New or Received status created more than 15 days ago is a flag. Keep this list as small as possible for accurate job costing and on-time vendor payment.

---

## Printing and Emailing a Purchase Receipt

- **Print:** More → **Print Receipt** → select layout and export format (PDF, Excel, etc.)
- **Email:** More → **Email Receipt** → fill in To, CC, Subject, attach layout, add message → Send

> Purchase receipts are commonly emailed to vendors to seek bids or place orders.

---

## Purchase Credits

To record a credit from a vendor, go to Purchase Receipts → **New** → **Add Purchase Credit**. Credits follow the same workflow as receipts.

---

## Frequently Asked Questions

**Q: What's the difference between the Purchasing Assistant and the Purchase Receipts screen?**  
The Purchasing Assistant guides you through purchasing items already estimated on won opportunities. The Purchase Receipts screen is for direct or manual creation of any purchase, including subcontractor expenses and one-off items not tied to estimates.

**Q: Can a purchase receipt cover multiple work tickets?**  
Yes. Use the Purchase Allocations screen to split line items across multiple work tickets. If you assign a single Work Ticket to the PR header, all items are allocated to that ticket and you cannot split them further without removing the ticket assignment.

**Q: What happens if the subcontractor invoices for more than the PR amount?**  
This is a variance. OST must review and either approve (with documented reason) or deny the variance before payment proceeds.

**Q: Can I delete a purchase receipt?**  
Only if it is in **New** status. Once received or approved, it cannot be deleted — use Unreceive or Unapprove to correct it.

**Q: What does "Complete" status mean?**  
The PR has been successfully transmitted to the accounting system (QuickBooks, Sage, etc.). Only applies to companies with accounting integration enabled.

**Q: Why isn't a vendor showing in the Vendor dropdown?**  
Use the **Vendor Resync** button on the Purchase Receipt screen to pull in new vendors from the accounting system.

**Q: What is Job Inventory?**  
Job Inventory allows materials to be received but not costed to the job until they are installed. This improves the accuracy of earned revenue calculations at month end. The inventory location assigned on the PR is used if any remaining materials are returned to inventory when the work ticket closes.
