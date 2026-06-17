# Invoicing Module (Aspire)

System URL: https://cloud.youraspire.com/

---

## What is an Invoice?

An Invoice is a bill sent to customers for completed work. The Invoicing module is where you prepare, review, send, track, and receive payment for invoices.

---

## Invoicing Module Tabs

| Tab | Purpose |
|-----|---------|
| Invoicing Assistant | Lists all billable items ready to invoice; generates invoice batches |
| Invoice Batches | Holding area to review/edit invoices before sending |
| Invoices | Browse sent and draft invoices |
| Receivables | Manage open balances, aging, payments, statements (organized by property) |
| Payments | Review/record payments and credit memos; create deposits |
| Deposits | Review past deposits sent to accounting |
| Log Event | Log weather events (mostly snow) to attach to invoice batches |
| Electronic Payment Log | List of electronic payments processed via Fiserv |

---

## Invoice Types and When They Can Be Invoiced

### Contract Invoice Types (recurring services)

| Type | Description | When it appears in Invoicing Assistant |
|------|-------------|----------------------------------------|
| Fixed Payment | Recurring invoice on a set billing schedule | Independent of ticket completion. Same date each month per opportunity |
| Per Service | Invoice per completed service visit at agreed rate | When the work ticket is marked Complete |
| T&M (Time & Materials) | Hourly rates + materials from completed tickets | When ticket complete AND time/materials entered |

### Work Order Invoice Types (one-time / enhancements)

| Type | Description | When it appears |
|------|-------------|-----------------|
| Fixed Price on Completion | Single invoice for full WO amount | All tickets on the WO are Complete |
| T&M on Completion | Single invoice from time/materials across all tickets | All tickets Complete and Approved with all entries |
| Fixed Price Open Billing (FPOB) | Bill any amount at any time, max flexibility | Always available; no thresholds |
| Fixed Price on Payment Schedule | Pre-agreed payment schedule (% complete) | Per the schedule defined on the opportunity |

⚠️ Invoice type is set during estimating and cannot be changed without a change order.

---

## Invoicing Assistant

The first tab and main entry point. Each row is a billing **recommendation**, not an invoice yet.

### Quick filters
- Properties, Branches, Invoice Types
- Invoice Timing (first/middle/last of month — only affects Fixed Payment Contract)
- As of Date — controls which items display by point in time

### Status colors / values

| Status | Meaning | Clicking row goes to... |
|--------|---------|-------------------------|
| Ready to be invoiced | Ready to batch | FPOB → Invoice Open Billing screen; others → no action |
| Ready and overdue | Ready, past due | Same as above |
| Can be invoiced | FPOB only | Invoice Open Billing screen |
| More work must be done | FP on Payment Schedule WO not ready | Nowhere |
| Address required | Billing address missing | Opportunity Invoice screen |
| Terms required | Payment terms missing | Property |
| Tax Jurisdiction missing | Tax setup missing | Property |

### Generating invoices
1. Filter list, set As of Date.
2. Check rows in Ready/Overdue.
3. **Bulk Actions → Generate Invoice** → confirm date → Save.
4. One invoice generated per property (unless property has Separate Invoices checked).
5. FPOB rows have no checkbox — select the row to invoice individually.

⚠️ FPOB invoices don't show checkboxes; click the row to specify amount.

### Permissions
- `View Invoice` — access tabs in Invoicing module
- `Create Invoice` — generate invoices via Bulk Actions
- `Edit Invoice` — complete batches

---

## Invoice Batches Workflow

Batches are a holding area between creation and customer delivery.

### Creating a batch
- From Invoicing Assistant → select Ready rows → Bulk Actions → Generate Invoice → confirm date → Save.
- Batch shows in Invoice Batches tab as **Not Complete**.

### Reviewing & editing
- Open batch → click invoice → edit billing contact, notes, terms → Save.
- ⚠️ **Do NOT adjust prices manually** except for T&M. Use change orders for other types — manual changes affect EOM numbers.

### Removing invoices from a batch
- Check invoices → Bulk Actions → Delete Selected Invoices. Returns them to Invoicing Assistant.

### Deleting an entire batch
- Three-dot menu → Delete Batch. All invoices return to Invoicing Assistant.

### Printing
- Three-dot menu → Print All Invoices (Include or Exclude Paperless).
- Pending batch prints display a **DRAFT** watermark.

### Completing a batch & sending
1. Three-dot menu → Complete Batch → Confirm.
2. If property has Invoice Email contact, the Email Invoice screen opens.
3. Configure: Email message, Attach Layout, Include Proposal (single only), Add Attachment, recipient checkboxes.
4. Click Send. Non-paperless invoices open a print window.
5. After completion, Aspire archives a PDF copy of each WO invoice as a property attachment (`InvoiceMMDDYY`).

### Batch screen — Related Event
Used for snow/weather events; description appears on all invoices in the batch (only events within 30 days available).

### 4-4-5 accounting period note
Companies on 4-4-5 calendars get checkboxes + Bulk Actions → Update Accounting Period (only on non-completed batches).

---

## Invoices Tab

Stores sent and draft invoices. Useful display columns: **Invoice Batch Status** and **Email Status** (must be added to view).

### Email/Batch Status combinations

| Batch | Email | Meaning | Action |
|-------|-------|---------|--------|
| Draft | N/A | Batch in progress, no email contact | Set invoice email contact if email needed |
| Draft | Pending | Has email contact, batch not completed | Complete the batch |
| Sent | In Queue | Batch complete, email queued | Wait; if stuck >1 hr, check user email sync |
| Sent | Sent | Email delivered | If not received, check spam, IT, sync, kickbacks |

### Edit Invoice screen — key actions (3-dot menu)

| Action | Notes |
|--------|-------|
| Print Invoice | Choose layout + export type (PDF, Excel, HTML, PNG, MHT, RTF, Text) |
| Email Invoice | Opens Bulk Email Invoice screen |
| Publish Invoice in Customer Portal | Replaces last published invoice |
| Add Credit Memo | Only if invoice is Sent |
| Delete Invoice | Removes from batch |
| Void and Reset | Resets sent invoice to Draft (requires Modify Sent Invoices permission) |
| Process Electronic Payment | Requires Process Electronic Payments permission |
| Reverse and Rebill | FPOB only, in closed months. Voids original (1234.001), creates rebill (1234.002) |

### Tax Jurisdiction override allowed?

| Type | Allowed |
|------|---------|
| WO FPOB / FP on Payment Schedule / WO T&M per Service | ❌ No |
| WO Fixed Price on Completion / WO T&M on Completion | ✅ Yes |
| Contract Fixed Payment / Per Service / T&M | ✅ Yes |

### Add Invoice Line Item options
Bounced Check, Clean up A/R, Finance Charges, Late Fees, Miscellaneous, Offset A/R Credit (Refund Customer).

---

## Receivables Tab

Organized **by property** (not customer). Shows open balances and aging.

### Default lists
- **Open Balance** — all properties with outstanding balances.
- **Aging** — buckets: Current, 1–30, 31–60, 61–90, 91+.
- **Payments to Deposit** — payments not yet sent to accounting.

### Aging logic
Aging is based on customer's **payment terms + invoice date** (not date sent). Example: 15-day terms → invoice within 15 days = Current; 16–45 days = 1–30 bucket.

### Three-dot (per property) actions
| Action | What it does |
|--------|--------------|
| Add Payment | Opens Payment screen prefilled |
| Send Email | Email billing contact (no statement attached) |
| Collection Notes | Add/view collection notes |
| Print Statement | Single statement print modal (with optional Include Invoices for combined PDF, max 50 invoices) |

### Bulk Actions
- **Print Statement** — Standard format (all unpaid) or Balance Forward format (rolls forward + current month).
- **Email Statement** — Send PDF statements to billing contacts. Sender: `notifications@youraspire.com`.

### Statement formats
- **Standard** — all invoices with outstanding balance.
- **Balance Forward** — prior balances rolled forward, current-month invoices listed.

### Credits
If `On Account` shows a number in parentheses, the property has a credit. Unapplied credits continue to age until applied.

### Permission
`View Accounts Receivable` — also grants Payments and Deposits tabs.

---

## Payments Tab

Lists all payments and credit memos.

### New dropdown
- New Payment → Payment screen
- New Credit Memo → Credit Memo screen

### Bulk Actions
- Create Deposit → Deposit screen with selected payments.

### Electronic Payment Status
| Status | Meaning |
|--------|---------|
| Success | Payment completed |
| Pending | Processor still working (typically a few minutes) |
| Error | Failed; check Sync Error column |
| N/A | Not electronic (cash/check/credit memo) |

Pending and Error rows are color-coded. Selecting Pending/Error opens the **Electronic Payment screen** (with Payment + Transaction History tabs); other rows open the Payment screen.

### Payment Screen — Key fields
- **Company / Contact / Property or Opportunity (Regarding)** — payment context (Property/Opp read-only after save).
- **Payment Date / Method / Reference No / Branch**
- **Payment Methods** — Check, Credit Card, Cash, EFT, or saved electronic methods (only saved methods process via Fiserv).
- **Invoices section** — checkbox to apply payment + Payment column for amount; Fee column auto-populates for electronic.
- **Credits section** — apply existing credit memos / unapplied credits.
- **Notes** — payment-level note. (Hidden when electronic method selected.)

### Filters available on Payment screen
Prefix (multi-select), Invoice # (multi-select), Description (string), Invoice Date (date), Invoice Amount (number), Open Balance (number).

⚠️ Changing filters clears existing allocations.

---

## Applying Payments

### To an invoice
1. Receivables → 3-dot icon next to property → Add Payment.
2. Verify Company/Regarding/Contact, set Branch, Method, Reference, Payment Date.
3. Check invoice rows; verify Payment Summary.
4. Optionally apply existing Credits.
5. Save.

### Without an invoice (prepayment / advance)
- Option A: **Quick Menu → New Payment** → search contact/company → set Regarding to Property → Method, Reference, Payment Date, Total → Collection Notes → Save.
- Option B: Invoicing → Payments tab → New → Add Payment → same fields.
- Result: credit recorded on property/opportunity in Regarding field.

### Overpayment / Underpayment
- **Overpay** — record full amount; remaining balance saved as credit on account.
- **Underpay** — adjust payment row to actual paid amount; invoice keeps remaining open balance.

### Notes vs Collection Notes
- **Payment Notes** — internal, only on payment record.
- **Collection Notes** — display on property and AR Aging reports.

---

## Credit Memos

Recorded credits applied against future invoices. Used for billing errors, returns, discounts.

### Creation paths
Quick Menu → New Credit Memo / Payments tab → New / Invoice screen → 3-dot → Add Credit Memo / Payments Search List → click credit memo line.

### Two modes
| Setting | Behavior |
|---------|----------|
| **Credit as Expense** ✅ | Credits to expense payment category (Admin > Lists > Payment Categories). Appears as expense on EOM, separate from divisional revenue |
| **Credit as Expense** ❌ | Credits to division (Maintenance, Enhancement, etc.). Appears as revenue on EOM |

### Required fields
Billing Contact*, Credit Date*, Branch*, Billing State/Zip*, Property/Opportunity*, Division/Expense*.

### Tax fields
- Sale Amount (excludes tax) — keep separate for accurate EOM.
- Taxable Amount — portion subject to tax (may differ from sale amount).
- Tax Amount — auto-calculated from jurisdiction; manual override limited to ±5% of calculated value.

### Applying a CM to an invoice
1. Quick Menu → New Payment → select contact → Apply.
2. (Optional) Regarding to filter invoices.
3. Method = Check, Date, Reference Number.
4. Check the invoice; **Payment field auto-sets to 0** (because CM amount applies, not a payment).
5. In Credits section, check the CM; full amount auto-applies — adjust if partial.
6. Verify Payment Summary minus credit, Save.

### Crediting Sales Tax Only
1. Find invoice → 3-dot → Add Credit Memo.
2. Sale Amount = $0.00.
3. Taxable Amount = full taxable amount of original invoice (not always = sale amount).
4. Tax Amount calculates automatically.
5. Apply → fill Property/Opportunity → Save.

---

## Deposits

Group payments and send to your accounting software (recognizes revenue).

### Create a deposit
1. Invoicing → Payments → list dropdown → **Payments to Deposit** (groups by payment type, only undeposited).
2. Select checkboxes → Bulk Actions → Create Deposit.
3. Review Deposit Date / Status (defaults New) / Payments.
4. Trash icon next to a payment removes it (returns to Payments tab).
5. Save (return later) or **Send to Accounting** (3-dot menu) when ready.

### Notes
- Credit memos are NOT included in deposits — handle via journal entry at month-end.
- Cannot delete a sent deposit.
- Cannot Reset to New in a closed month.
- Group by payment type for cleaner records.

### Reset / Delete
- Sent deposit → 3-dot → **Reset to New** (only in open month) → modify → Send to Accounting.
- Unsent → 3-dot → Delete Deposit (payments return to Payments tab).

---

## Electronic Payments (Fiserv Integration)

### Setup
1. Sign up via Fiserv partnership page or AspireCare ticket. Enroll for Credit Card, ACH, or both.
2. Wait for AspireCare to enable integration.
3. Update user roles in Administration > User Management with permissions:
   - `Process Electronic Payments`
   - `Void Electronic Payments`
   - `Refund Electronic Payments`
   - `Expiring Electronic Payment Method Alerts`
   - `Rejected Electronic Payment Alerts`
4. Log out and back in.

After enabling: Customer Portal payment options activate; Electronic Payments tab appears in Configuration; Payment Methods tab appears on non-Employee/Sub contacts.

### Adding a payment method on a contact
1. Open contact (must NOT be type Employee or Sub).
2. Payment Methods → New.
3. Choose Credit or ACH/echeck.
   - Credit: Card #, CVV, Expiration. Only last 4 digits stored after save.
   - ACH: Routing\AccountNumber (backslash required: `123456789\987654321`).
4. Default Payment Method checkbox (at least one required).
5. Use Default Billing Information toggle.
6. Save.

### Adding during payment creation
- Same form + **Remember Card** checkbox. Uncheck for one-time (e.g., gift cards).

### Processing electronic payments

Entry points: Quick Menu, Payments tab, Process Electronic Payments screen, Invoice screen Bulk Actions, Customer Portal.

⚠️ Don't select generic "Credit Card" method — that doesn't process via Fiserv. Use a saved card.

### Bulk processing (Process Electronic Payments screen)
1. Quick Menu → Process Electronic Payments.
2. Filter by Payment Term (e.g., "Autopay") — useful for autopay-style workflow.
3. Check invoices, adjust amounts (partial payments allowed).
4. Bulk Actions → Process.

### Autopay workflow setup
- Create payment term named "Autopay" in Admin > Application > Lists > Payment Terms.
- Apply to properties.
- Process via Process Electronic Payments + Payment Term filter.

(Aspire has no fully automatic recurring billing — this workflow is the closest.)

### Statuses (Electronic Payment Status)
- Pending (≤5 min typical)
- Successful
- Error (add Sync Error column for details)

### Logs and receipts
- **Electronic Payment Log tab** — full transactional log including voided/expired records, error messages.
- Resend receipt: Log → select payment → Transaction History → 3-dot → Send/Resend Email Receipt.

### Void vs Refund

| Action | When | Result |
|--------|------|--------|
| Void | Before payment posts (~5 min window in Aspire) | Stops the transaction |
| Refund | After payment posts | Returns money to original card |

⚠️ Once payment is sent on a deposit to accounting, refund option is **locked** in Aspire — must use Fiserv directly.

⚠️ Fiserv void window in Aspire: until 8:30 PM CST same day (or following day if created after 8:30 PM).

⚠️ Fiserv does NOT allow partial voids/refunds.

⚠️ Fiserv does NOT notify Aspire of failed/uncollected ACH — check Fiserv portal or your bank.

### Refund Scenarios

| Scenario | Solution |
|----------|----------|
| Payment applied to wrong invoice (open month, deposited) | Reset deposit to New, delete deposit, edit payment allocation |
| Payment applied to wrong invoice (open month, not deposited) | Edit payment allocation directly |
| Payment to wrong invoice (closed month) | Misc Invoice (Clean Up A/R) on wrong client + CM (as Expense, Clean Up A/R) on correct client |
| Returned/Bounced/Declined | Misc Invoice with item "Bounced Check"; record refund account in accounting |
| Customer paid + requests refund (Aspire methods) | Send payment to accounting; cut check from accounting "Refund Customer" account; if no invoice, create Misc Invoice or CM |
| Customer credit balance + wants refund | Misc Invoice using "Offset A/R Credit (Customer Refund)"; apply credit; cut check in accounting |
| Fiserv: customer paid + needs refund | Refund directly in Fiserv; record entry in accounting |
| Fiserv: void before processing (Aspire) | Aspire → Payments → Void payment |
| Fiserv: void after sent to accounting | Void in Fiserv (not Aspire); create Misc Invoice "Clean Up A/R"; reprocess payment |

### Card Payment Compliance (PCI / Fiserv)
- Verify cardholder identity; collect CVV always.
- Process only legitimate goods/services tied to your approved business model.
- Refund only to original card; never to cash/ACH/different card.
- Never store card data in notebooks/spreadsheets/emails/screenshots.
- Use chip (EMV) → contactless → swipe (last resort) → manual key (avoid).
- Don't split transactions, run test charges, or process cards from owner/relatives.
- Use Fiserv-approved terminals/gateways; maintain PCI DSS.

### Aspire stores: only the last 4 digits of cards. Fiserv handles all transactions and is PCI compliant.

### Alerts (require permissions)
- Rejected Electronic Payments
- Expiring Payment Methods

---

## Fixed Price Open Billing (FPOB) — Special Invoice Type

Most flexible: bill any amount at any time.

### Schedule of Values (SOV)
Required on the estimate. Default config (Admin > Configuration > Application: "Default Schedule of Values to % vs. Dollars").

### Billing by dollar amount instead of %
1. Edit Schedule of Values on the estimate (during bidding or after).
2. **Switch the Quantity and Unit Price values** for lines you want to bill by dollar amount.
3. Lines with Quantity = 1 still behave as percentage-based.
4. When invoicing: enter quantity equal to dollar amount in **Amount This Invoice** (e.g., 6,000 to bill $6,000).
5. Percentage lines: enter decimal (.25 for 25%).

### Reverse and Rebill (FPOB only, closed months)
- Edit Invoice → 3-dot → Reverse and Rebill.
- Edit Amount This Invoice in Invoice Schedule of Values screen.
- Voids original (e.g., 1234.001) and creates rebill (1234.002) in current period.
- Requires `Reverse and Rebill FPOB Invoice in Closed Months` permission.
- Excludes T&M services.

---

## Retainage (FPOB only)

Retainage = % withheld (typically 5–10%) released at project end or at milestones.

### Setup
On the work order with FPOB → Invoice Type → receipt icon → Invoicing Info → enter Retainage % → optional Retainage Maturity Date → Save.

### Workflow
- Invoicing Assistant → opportunity → New → enter amount → Aspire shows withheld retainage automatically.
- Pay Application layout: Page 2 shows accumulated retainage on Line 5; current due on Line 9.
- Invoicing for retainage: select the **New** on the retainage line → enter date and amount (defaults to 100%) → Save.

### EOM treatment
- EOM Revenue tab includes a separate **Retainage** line (debit = withheld; credit = invoiced).
- In Revenue Journal Entry: separate Retainage from Accounts Receivable → Retainage Receivable account on balance sheet.

---

## Prepayments / Deferred Revenue

Best practice: do NOT accept prepayments before opportunity is created in Aspire.

### Two options to track in accounting
1. **With sales tax** — record prepayment, apply to invoice as a payment in Aspire.
2. **Without sales tax** — record prepayment, apply via Credit Memo in Aspire.
   - Create payment category "Job Deposits" pointing to Deferred Revenue account.

### Aspire-side options
- **Invoice full opportunity in first month** — apply prepayment + CM for any discount. Pro: eliminates A/R; Con: revenue recognized before earned, over/under report skewed.
- **Invoice monthly** — apply prepayment to property, allocate to monthly invoices. AR Aging shows credit balance until depleted.

### Recording the prepayment
Quick Menu → New Payment → set Regarding = Property (no opportunity yet) → Method, Reference, Contact, Branch, Date → Notes → Save.

### Tips
- Add **Opportunity Tags** like "2024 Contract Prepaid Customer" to batch separately.
- Use property notes to track deferred revenue balances.
- If client cancels, follow Refund Payments process.

---

## Aging & Statements

### Sending statements
- Receivables → check properties → Bulk Actions → Email Statement or Print Statement.
- Statements are per property, not per customer.
- Email available only when email sync is enabled.
- Sender: `notifications@youraspire.com`.

### Bulk Email Statement options
- To: Property Billing Contact / Email Invoice Contact / Primary Contact (multi-select).
- CC: contacts (all selected statements go to all CC'd).
- Include Invoice(s) checkbox: combines statement + invoices into single PDF (uses layout from most recently emailed invoice; max 50 invoices).
- Insert email tokens for dynamic data.

### Print Statement (bulk)
- Export Type: PDF, Excel, HTML, PNG, MHT, RTF, Text. (Without Choose Report Export Type permission, PDF only.)
- Include Invoice(s) is **NOT** available on the bulk Print modal.
- Standard or Balance Forward format depending on system config.

---

## Miscellaneous Invoices

Created from Quick Menu → New Misc Invoice or Invoicing module → New.

Common item types:
- Bounced Check
- Clean up A/R
- Finance Charges
- Late Fees
- Miscellaneous
- Offset A/R Credit (Refund Customer)

Used for: AR cleanup, bounced check tracking, refunds against credit balances, finance/late fees.

---

## Weather Events (Snow Season)

Allows weather event description to appear on all invoices in a batch.

### Setup
1. Admin → Application → Lists → Event Type → New (e.g., "Snow").
2. Invoicing → Log Event → New: Name, Branch (required), Event Type, Location, Start/End Date+Time, Zip Codes, Description, Attachments.
3. Zip Code field requires Branch + Start + End filled in first.
4. Pulls zip codes from properties with work tickets that have time/materials in the date range.

### Tying to a batch
- On Batch screen → **Related Event** dropdown (only events within 30 days available).
- Layout request needed for events to print on invoices (not default).

### Reporting
Weather Events Report (Reports module → Standard Reports → Production) — group by property/zip; review tickets and invoices.

---

## Add Work Ticket Images to Invoices

### Template setup (Web Report Designer)
Two placeholders (use only ONE per template):
- `InvoiceOpportunityServiceWorkTicketAndVisitNoteAttachments` — grouped with services (Group Header section).
- `InvoiceWorkTicketAndVisitNoteAttachments` — all images in one column (Footer section).

### Restrictions
- ❌ NOT supported on Fixed Price on Payment Schedule and FPOB invoice types.
- For Fixed Payment Contract: requires "Link Completed Tickets to Invoice" checked when completing the estimate.

### Workflow
1. On a visit/ticket → check **Image available on invoice** for desired notes.
2. On the invoice → Manage next to "Images Included on Invoice" → Add Images → check images → Save.
3. Marking images on a ticket does NOT auto-add to invoices — must select per invoice.

### Permissions
`System Admin` (for templates), `Full Access to Schedule Board`, `View Invoices`.

---

## Troubleshooting

### Customers not receiving invoices
1. **Invoices tab** → add display columns: Invoice Batch Status + Email Status.
2. Check status combinations table (above) to identify the stage.
3. **Branch/Region settings** (User Settings → Administration → Organization) — verify Invoicing Email From + email sync.
4. **Configuration screen** — used when no Branch/Region set, OR when batch spans multiple branches (Configuration takes priority for multi-branch batches).
5. **Contact record** — email must be unique and active (no duplicates, no leading/trailing spaces).
6. **User screen** — Aspire supports Microsoft 365 + Google Suite (others use SMTP via SPF/DNS). Auth tokens valid 90 days; refresh by logging in.
7. **Property** — verify Email Invoice + Primary/Billing checkboxes on contact.

### Lost / unmatched payments
1. Reports → Standard Reports → A/R Aging → Payment Source section. Note contact + amount.
2. Quick Menu → New Payment → search contact → Apply → match invoice + payment → Save.
3. **Deactivated contact** — Contacts module → remove Active filter → reactivate (Active radio button) →