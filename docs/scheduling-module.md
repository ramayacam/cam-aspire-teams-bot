# Scheduling Module (Aspire)

System URL: https://cloud.youraspire.com/

*The operations hub where Division Managers and route managers schedule won services to Ops Managers and crews, then track time through to payroll. Covers the Schedule Board, routes (creating, managing, changing, deleting), route optimization, schedule changes and deletions, checklists, SMS notifications, and the full time-entry lifecycle (daily acceptance, weekly review, manual entry, Aspire Mobile, quick tickets). Structure based on the Aspire Academy Scheduling and Mobile & Time Entry chapters, enriched with operational depth from the reference documentation.*

> **Who this is for:** Division Managers and route managers who calendar services out to Ops Managers / crews, and the office staff who review the resulting time. The priority topics are how to **schedule work, and how to change or remove it** once scheduled.

---

## What is the Schedule Board?

The **schedule board** is the operations hub — a flexible digital whiteboard where work gets assigned to crews across days. Work tickets appear here to be scheduled once their opportunity is **won**.

- **Organized by manager:** a drop-down (top-left) selects the route manager; each manager has their own board with their routes/crews. Routes run down one side, days across the top.
- **Views:** weekly (default, Mon–Sun) or monthly (upper-right). The **Working Days** drop-down adjusts which days are visible.
- **Work-ticket list:** the **clipboard icon** (top-right) shows tickets waiting to be scheduled; expand it with the left caret to reveal more columns.
- **A scheduled tile** shows the occurrence number, property abbreviation, service abbreviation, and estimated hours; the day total shows scheduled estimated hours.
- **Route colors:** each route can display a distinct color for quick visual scanning.

**Search prefixes on the board:** `s` = service, `t` = ticket, `o` = opportunity number, `P` = property name. (e.g., `O` + a number shows all tickets for that opportunity.)

**Navigate:** Scheduling icon (blue side panel) → schedule board → choose the route manager.

---

## The Scheduling Workflow — From Won Ticket to Assigned Crew

This is the core flow a Division Manager follows to calendar services out to Ops Managers and crews:

1. **A service is won** → Aspire generates work tickets (Open status), which appear in the work-ticket list (clipboard icon).
2. **Set up routes** (once) → each route is a crew or individual that performs scheduled tickets, under a route manager (the Ops Manager). See "Routes" below.
3. **Schedule the ticket** → drag it from the work-ticket list onto the correct route and day, or use the **Scheduling Assistant** for sequenced/recurring visits.
4. **Order the visits** → use Route Scheduling (manual) or Route Optimization (automatic) so the crew's day is efficient.
5. **Crew performs the work** → they see it in Aspire Mobile, clock in/out, and record time/materials.
6. **Review the time** → Daily Time Acceptance (catch errors) → Weekly Time Review (approve + export to payroll).
7. **Make changes as needed** → reschedule, skip, insert blank days, or remove — see "Making Changes to the Schedule."

> The relationship to work-ticket status: a ticket is **Open** until scheduled, then **Scheduled** on the board, then **Complete** after the crew finishes and time is accepted. (Full status rules live in the Work Tickets module — here, "Scheduled" simply means the ticket is placed on the board, and a ticket stuck in Scheduled past its date signals a problem to investigate.)

---

## Routes — Creating & Managing

A **route** is an individual or crew set up to perform scheduled work tickets. A manager can have **multiple routes**, but **only one Crew Leader per route.**

### Sequenced vs. Time-Based routes

| Type | Behavior |
|------|----------|
| **Sequenced** | No start/end time; visits are scheduled in sequence based on the route's man-hours. You can set available working days. |
| **Time-Based** | Requires working hours; visits have specific start/end times; supports overnight visits. ⚠️ **Route Optimization is disabled** for time-based routes, and **absentee notifications require time-based scheduling.** |

**Time-based visual cues:** clock icon + time zone; gray banner = working hours with no visits; blue banner = scheduled visits; red background = conflict or outside working hours; link icon = multi-day visit. ⚠️ Time ranges per day **cannot overlap** — an overnight shift needs two ranges split at midnight.

### Creating a route
Scheduling module → three-dot → **Manage Routes** → **New Route** →
1. Name (consistent convention — crew leader or property name).
2. Confirm **branch**; set **route manager** and **crew leader**; optional division.
3. **Man-hours/day** (largest possible for one member); **route size** (number of people incl. crew leader).
4. **Display order** (increments of 10); **color**.
5. Add **crew members** (needed so absentee notifications can cover all members).
6. Optional **property / service / service-type restrictions**.
7. Scheduling type: **Add to Schedule** → pick working days (sequenced) or days + times (time-based) → **Save**.

**Permissions:** Edit Routes + Full Access to Schedule Board (manage/edit routes and crew/properties); View Routes (activate/deactivate a route); the **Time-Based Scheduling** checkbox on the branch record enables the sequenced-vs-time-based choice.

### Recurring Schedule for Time-Based Routes (303C / 304C)
For time-based routes, you can set a **recurring schedule** so visits repeat automatically (e.g., every Monday and Thursday at set times) instead of scheduling each visit by hand. Set it after the route is created; recurring visits then populate the board on the defined cadence. (Recurring scheduling is what enables **Skip This Week's Visit** — see below.)

### Managing / editing a route
Scheduling → three-dot → **Manage Routes** → select the route → edit crew members, properties, working days/times, color, or man-hours → Save. Use **View Routes** permission to **activate/deactivate** a route without deleting it.

---

## Route Scheduling & Optimization

Two features control the **order** crews visit properties on a given day.

| Feature | What it does |
|---|---|
| **Route Scheduling** | **Manually** sequence visits — you specify the visit order of each property on a route for a day. |
| **Route Optimization** | **Automatically** sequences visits in the most efficient order based on distance and drive time — reduces fuel, wear, and can free time for more tickets. |

The route-scheduling **map** shows property icons color-coded by route; the number on each icon is the visit order. Each icon shows the work ticket number, opportunity number, scheduled service, and visit hours. A **green check mark** at the bottom of a route means it's optimized — **manually reordering removes the check mark.**

### Use Route Scheduling (manual order)
1. Schedule board → **three-dot menu** (top-right) → **Route Scheduling**.
2. Confirm route manager and date.
3. Click **Set Route Order** → select the route → Save.
4. Click property icons in the order visits should occur (the number on the arrows becomes the sequence); use the **reset icon** to start over.
5. **Save** and confirm; the map refreshes.

### Use Route Optimization (automatic order)
- **One route, one day:** click the blank space on that day/route → **Optimize Route**.
- **One route, entire week:** right-click the route name → **Optimize Route**.
- **All routes under a manager, one day:** right-click the day header → **Optimize Routes**.
- **All routes/days for a manager, a week:** three-dot menu → **Optimize Route** button.

⚠️ If you don't see the Optimize option, Route Optimization must be enabled for your Aspire system (and remember it's disabled on time-based routes).

---

## Making Changes to the Schedule (reschedule, skip, remove)

This is a core Division-Manager task. Here's how to change or remove scheduled work without disrupting the whole board.

### Reschedule a visit (change day/crew)
**Drag and drop** the visit tile to a different day or route on the schedule board. This updates the scheduled date and, if moved to another route, reassigns the crew. (If SMS visit reminders are configured and the reminder already sent, a change triggers a Reschedule Notification — see SMS below.)

### Remove a visit from the schedule (back to Open)
To take a ticket off the board without cancelling the work: drag it back to the work-ticket list, or right-click the tile and remove it. The ticket returns to **Open** status and can be rescheduled later. (To **cancel** the work entirely — not just unschedule it — use the Work Tickets module; cancellation rules depend on invoice type.)

### Skip This Week's Visit
For **weekly or bi-weekly** recurring visits only, and only after the recurring schedule is set:
1. Right-click the visit tile on the schedule board.
2. Select **Skip This Week's Visit**.

⚠️ **Skipping pushes ALL occurrences forward one week.** Any work ticket pushed **past the contract end date** is set to **Open** status — make sure it's completed before the contract ends. Use for last-minute customer requests or bad weather.

### Insert Blank Days (push a route forward)
To handle a crew illness, equipment failure, or supply delay without wrecking the schedule:
1. Right-click a day on the route → **Insert Blank Days**.
2. Specify: how many days of visits to move, how many days forward, and whether shifted visits may land on the weekend.
3. **Look ahead** for conflicts with recurring services and confirm the route isn't over-scheduled; drag-and-drop tiles to fix conflicts.

⚠️ After skipping or inserting blank days, always look ahead so you don't over-schedule a crew or leave a contract's tickets unscheduled.

### Delete / deactivate a route
To stop using a route: Scheduling → three-dot → Manage Routes → select route → **deactivate** (keeps history) or delete if empty. Reassign or reschedule its visits first so no tickets are stranded.

---

## Scheduling Assistant

An alternative to drag-and-drop, useful for sequenced or recurring/time-based visits. Open it from the **Scheduling Assistant** icon on the board: select the ticket(s), choose the route and the recurring pattern or specific days, and Aspire places the visits according to the service schedule and route man-hours. Best for placing a full contract's recurring visits at once rather than dragging each occurrence.

---

## As-Needed Services & Work Tickets

Services marked **as-needed** (Per Service invoice type) don't auto-schedule — they wait in the work-ticket list under "as needed" until requested. Drag one onto the board only when the service is actually requested; it invoices only after completion. Use **Bulk Actions → Swap As Needed Service** (e.g., for snow) to change the service on an as-needed ticket. (See Work Tickets module for full ticket-action detail.)

---

## Service Visit Checklists

**Service Visit Checklists** break a service into actionable tasks crews must complete before a work ticket can be completed — for accountability and quality tracking.

- **Enable at BOTH system and branch levels** (branch-level is required even with a single branch).
- **Mandatory items:** an item marked mandatory in the Service Catalog is mandatory on **all** opportunities using that service; to make it optional per job, mark mandatory on individual opportunities instead.
- A checklist-related checkbox/indicator also appears on the **work ticket screen** itself, distinct from where checklists are configured.

**Permissions:** View Visit Checklists (view the report); Make Visit Checklist Items Mandatory in the Service Catalog.

**Enable:** Administration → Configuration → **Application** → check **Enable Visit Checklist** → Save; then Administration → **Organization** → **Branches** → branch → check **Enable Visit Checklist** → Save.
**Create items:** Administration → **Estimating** → **Visit Checklist Items** → New → name by task → choose branches + divisions → Save.
**Attach to a service:** Administration → Estimating → **Service Catalog** → service → **Visit Checklist** section → add items → mark **Mandatory** as needed → Save.

---

## SMS Notifications

Two types: **Visit Reminders** (to customers) and **Absentee Notifications** (internal). Configuration, permissions, and opt-in/opt-out live in the Administration chapter; this covers how they behave in use.

### Visit Reminders
- Sent the **day before** the visit at the template time. Cannot be duplicated — copy the template and change Delivery Time Details for multiple reminders.
- **Not triggered** if the visit is scheduled after the reminder time (e.g., reminder set 1 PM Tuesday; visit scheduled after 1 PM Monday → no reminder).
- **Cancellation Notification** (visit deleted): sent within 15 min; fixed format; not sent if the visit was canceled/rescheduled before the reminder triggered.
- **Reschedule Notification** (date/time changed): sent within 15 min, only if the original reminder already sent. A sequence-only change (same date/time) doesn't trigger it; a future reschedule sends both a Reschedule Notification and a new Visit Reminder.

### Absentee Notifications
- Internal alert when a team member hasn't clocked in after the scheduled start. ⚠️ **Only compatible with Time-Based Routes.**
- **Recipients / Additional Recipients:** who gets the alert. **Grace Period:** acceptable minutes past the Visit Start Time before sending (5–240 min).
- **Trigger Type** defaults to Job Not Started in Mobile; **Delivery Time** defaults to Immediately.
- **Property Tags** filter which properties trigger it; cleaners must be on the same time-based route. Overnight visits trigger a single notification (no next-day repeat). One message per template; separate messages per differing Grace Period.

---

## Consumables (scheduling side)

Consumables deliveries are scheduled on a dedicated **Consumables Route**. Field crews request supplies via **Open Issues → Consumables Request** in mobile (requires a Consumables Request issue category in Administration). Completed consumable tickets go to **Pending Approval** before Invoicing. Full setup (Service/Item Catalog, T&M pricing hierarchy, contract vs. work-order handling) is in the **Opportunities module → Consumables**.

---

## Time Entry — The Three Parts

Time entry connects three steps: the **Aspire Mobile app** (real-time capture), **Daily Time Acceptance** (catch errors early), and **Weekly Time Review** (final payroll check).

### Three types of time
- **Clock Time** — the employee's total paid time for the day (clock-in to clock-out, minus configured break).
- **Direct Time** — time serving customers on property, applied to work tickets.
- **Indirect Time** — time on indirect tickets (equipment maintenance, shop time, training) not chargeable to a direct ticket.
- **Difference / Drive Time** — time between tickets; on save, Aspire distributes it **proportionally** across the day's tickets (more hours on a ticket = more drive time). Exaggerated drive time signals time wasn't applied to a ticket.

---

## Daily Time Acceptance

The production/route manager reviews each crew's time **daily** to catch errors (unallocated materials, wrong clock-outs) before payroll.

**Icons:** mobile-device icon = time captured but not accepted; **green clock** = reviewed and accepted.

**Procedure:** Schedule board → click the blank space on the route/day → **Time Entry**. Review in order:
1. **Clock Time** — add crew members via Add New if needed; check clock-in/out and the auto-deducted lunch.
2. **Direct Job Time** — every ticket has time; verify lunch reported against the right ticket; confirm completed check marks.
3. **Indirect Time** — shop/meeting/training.
4. Review the **Difference** (drive time).
5. **Save** — the icon turns to a green clock.

---

## Weekly Time Review

The final check of all hours (including OT); each employee's time must be **approved** before export to payroll.

- Aspire shows 7 days starting from the payroll first-day set in Configuration. ⚠️ **Don't filter by branch** (you may miss cross-branch hours); filter by pay schedule to review hourly vs. salaried separately.
- **Time-entry statuses (cannot skip):** **Unaccepted** (entered, not accepted in Daily — go back and save) → **Pending** (accepted, ready for approval — the desired state) → **Approved** → **Exported** (sent to payroll).
- **Audits** (hover a time value): Open Time Entry, Time Entry Audit (log of changes), Clock Time Audit.
- **Common errors:** missing pay rate, missing pay schedule (fix on the employee contact → Payroll), and **OT Pay Code Exception** (a day used a non-default pay code; you can still export, or manually update to the OT code).

**Procedure:** Schedule board → **Weekly Time Review** tab → set the week → confirm all employees present → resolve errors → check total/OT columns (use audits for red flags) → check employees → **Bulk Actions → Approve** → **Bulk Actions → Export**. (Unapprove via Bulk Actions to correct, then reapprove.)

---

## Manual Time Entry

For a forgotten lunch, no mobile app, correcting mobile mistakes, or adjusting direct/indirect ticket time.

- The Time Entry screen uses **military time** — you can type `7A` / `4P` and Aspire converts. Lunch entered as a decimal (e.g., 0.50).
- Multiple clock rows (Clock 1, Clock 2) capture crew members with different hours.
- Saving moves completed tickets to Complete/Pending Approval and the day's time to **Pending** for weekly review; Difference distributes as drive time.

**Procedure:** Schedule board → right-click the route/day → **Open Time Entry** → **+** next to Clock Time → **Add Crew Member** → enter clock times (start/end/lunch), click each employee's cell (turns green); add clock rows for differing hours → **Direct Job Time:** enter onsite start/stop per ticket, click crew cells, check Completed; add materials via three-dot → **Add Material** → item + quantity → **Indirect Job Time:** shop/meeting/training → review Difference → **Save**.

---

## Aspire Mobile

The mobile app is the crew's real-time tool: view scheduled tickets, clock crew in/out, report lunch, start/stop job time, apply equipment/materials, view/respond to issues, add documents/photos, and request equipment service.

- **Lead Cleaners / Crew Leaders:** manage the crew's clock, start/stop time per ticket, allocate materials, complete tickets, handle issues.
- **Crew Members:** clock in/out and record their own time against assigned tickets.
- **Visit Notes** are internal; **Opportunity/Invoice Notes** (on quick tickets) are customer-facing.

---

## Quick Tickets

A **quick ticket** lets a crew leader log time/materials in mobile for jobs that pop up (e.g., irrigation repair) without building a full opportunity/estimate. A **quick ticket template** is a one-service work-order template that lets office staff create a work order on the fly from the Time Entry screen.

- Routes need the **Show New Ticket** button enabled (Manage Routes) to create quick tickets in mobile.
- On conversion, fields populate from the field entry; **Opportunity Invoice Notes** (entered by the crew leader) appear on the customer-facing invoice (no original proposal existed). **Visit Notes** stay internal.

⚠️ **Bot-relevant guardrail:** on a quick-ticket work order (T&M invoice type by default), if the **price field in Time Entry is set to any amount greater than $0, the invoice type automatically changes from T&M to Fixed Price on Completion**, overriding the original service price. **Leave the price at $0 to preserve T&M billing.**

**Enable:** Scheduling → three-dot → Manage Routes → route → check **Show New Ticket Button** → Save.
**Convert (office):** Time Entry screen → quick ticket entry → three-dot → **Create New Ticket** → choose quick work-order template → review property/branch/division/name/price ($0)/invoice notes → Save.
**Create in mobile (crew leader):** tickets icon → **+** → select property → **Create Quick Ticket** → add Opportunity/Invoice Notes → **Start Work** → add Visit Notes/images (internal) → **+** → **Material** → item + quantity → **Stop Work** → confirm **Complete**.

---

## Timekeeping Behavior (Branch-Level Settings)

Modern timekeeping settings are **per-branch** for multi-branch flexibility:
- Per-branch: **GEO radius**, drive time billable/non-billable, allow quick tickets, require checklists, pay code defaults.
- **Time Correction Requests (mobile):** a crew member submits a correction (e.g., forgot clock-out) from mobile → routed to a supervisor approval queue → approved corrections post to Time Entry automatically.
- **Auto Time Acceptance:** a branch setting can auto-accept error-free time entries after N hours; entries with errors still require manual review (reduces office workload for clean crews).

---

## Time Reporting Settings (Administration → Configuration → Time Reporting)

Configuration for how clock and time behavior work. Navigate: Dashboard → Settings → Administration → Configuration → **Time Reporting** tab → save with the save icon.

| Setting | What it does |
|---|---|
| **Break Time** | Standard time auto-deducted from each crew member's daily clock time. Enter in **decimal** (0.25 = 15 min, 0.50 = 30 min, 1.00 = 1 hr). |
| **Early Clock-In Warning** | For states with minimum lunch requirements. If a user clocks out then back in before this many minutes, they're warned they aren't required back yet. Enter **0** to disable. |
| **First Day of the Week** | Sets the first day of the payroll week. |
| **OT Calculation** | **Standard** = OT only on hours under the employee's standard pay code. **Override Pay Code** = Aspire accounts for all time; with an override pay code it compares regular-pay-with-OT vs. override hours and uses the larger. |
| **Default Geo Perimeter** | Perimeter (from property center outward) crews must be within to clock into a ticket via mobile. **Red push pin** = clocked in/out outside the perimeter; **green push pin** = inside. |
| **Equipment Reading Clock-Out Prompt** | Prompts crew for equipment meter readings (per job, end of day, or a specific weekday). Blank = disabled. |
| **Round Clock In/Out to Nearest 15 Minutes** | Rounds clock times to nearest 15 min. Does **not** affect job time entries. |
| **Default Clock Time on Employee Time Card Report** | Time card clock-in/out determined only by the earliest clock-in and latest clock-out for the day; work ticket start/stop not considered. |

**Sub-Portal Settings** enable subcontractor contacts (with user accounts) to access the subcontractor portal for their own time/material entry.

---

## Branch-to-Branch Subcontract Work

When a property in Branch A is serviced by a crew from Branch B:

| Option | When to use | Pros | Cons |
|---|---|---|---|
| 1. Branch B as subcontractor on Branch A's ticket | Simple cross-branch labor | Single ticket; clean P&L allocation | Requires subcontractor setup |
| 2. Transfer property to Branch B | Permanent move | Simplest long-term | Loses Branch A history |
| 3. Mirror opportunities in both branches | Joint accountability | Both branches see revenue | Double maintenance |
| 4. Internal labor transfer (journal) | Occasional | No structural changes | Manual accounting work |

Most common: Option 1 (subcontract) for ad-hoc, Option 2 for permanent moves. (For the subcontractor billing/PR workflow, see `subcontractor-extra-work-module.md`.)

---

## Required Permissions

| Action | Permission |
|--------|-----------|
| Manage/edit routes, crew, properties | Edit Routes + Full Access to Schedule Board |
| Activate/deactivate a route | View Routes |
| Choose sequenced vs. time-based | Time-Based Scheduling checkbox on the branch |
| View visit checklists report | View Visit Checklists |
| Make checklist items mandatory | Make Visit Checklist Items Mandatory in the Service Catalog |
| Approve/export payroll time | (Weekly Time Review access / Bulk Actions) |

---

## Daily Scheduling Checklist (Best Practices)

✅ Review the Open work-ticket lists daily and schedule tickets near their start date.
✅ Investigate any ticket stuck in Scheduled past its date (future visit? backordered materials?).
✅ Do Daily Time Acceptance every day — catch errors before payroll.
✅ After skipping visits or inserting blank days, look ahead for conflicts and over-scheduling.
✅ Keep only one Crew Leader per route; add all crew members so absentee notifications cover everyone.
✅ Prefer individual visit changes (drag-and-drop, skip, reschedule) over sweeping bulk changes.
❌ Don't filter Weekly Time Review by branch (you may miss cross-branch hours).
❌ Don't set a quick-ticket price above $0 unless you intend to switch it from T&M to Fixed Price.

---

## Related (see other modules)

- **Full work-ticket actions** (complete, cancel, approve, statuses in depth) → Work Tickets module.
- **Consumables setup** (catalog, pricing) → Opportunities module.
- **SMS setup, geo-perimeter config, user roles, branches** → Administration.
- **Subcontractor billing / PR workflow** → subcontractor-extra-work module.

---

## Common Questions (from Aspire Academy)

**Q: How do I schedule a work ticket?**
Open the schedule board (Scheduling icon → choose the route manager), open the work-ticket list (clipboard icon), and drag the ticket onto the correct route and day — or use the Scheduling Assistant for recurring/time-based visits.

**Q: What's the difference between sequenced and time-based routes?**
Sequenced routes have no set times — visits run in sequence based on the route's man-hours. Time-based routes require specific start/end times per visit (and support overnight work), but route optimization is disabled and absentee notifications require them.

**Q: How many Crew Leaders can a route have?**
Only one Crew Leader per route. A manager can have multiple routes, though.

**Q: How do I change the order crews visit properties?**
Use Route Scheduling (three-dot → Route Scheduling → Set Route Order → click icons in order) for manual ordering, or Route Optimization to let Aspire order them automatically by drive time.

**Q: How do I skip a visit for a week?**
Right-click the visit tile → Skip This Week's Visit (only for weekly/bi-weekly recurring visits). It pushes all occurrences forward one week — any ticket pushed past the contract end date goes back to Open, so complete it before the contract ends.

**Q: A crew is out sick — how do I push their schedule without breaking everything?**
Right-click a day on the route → Insert Blank Days → specify how many days of visits to move and how far forward. Then look ahead for conflicts and confirm the route isn't over-scheduled.

**Q: How do I reschedule or reassign a visit?**
Drag the visit tile to a different day or route on the schedule board. Moving it to another route reassigns the crew.

**Q: How do I take a ticket off the schedule without cancelling the work?**
Drag it back to the work-ticket list (or right-click → remove). The ticket returns to Open and can be rescheduled. To cancel the work entirely, use the Work Tickets module (cancellation depends on invoice type).

**Q: How is drive time calculated?**
It's the Difference between tickets; on save, Aspire distributes it proportionally across the day's tickets. Exaggerated drive time usually means time wasn't applied to a ticket.

**Q: What should I review first in Daily Time Acceptance?**
Clock Time first, then Direct Job Time, then Indirect Time, then the Difference (drive time). Save when correct — the icon turns to a green clock.

**Q: What do the time-entry statuses mean?**
Unaccepted (entered but not accepted in Daily) → Pending (accepted, ready for approval — the goal) → Approved → Exported (sent to payroll). You can't skip stages.

**Q: Why shouldn't I filter Weekly Time Review by branch?**
You may miss an employee's cross-branch hours. Filter by pay schedule instead if you need to separate hourly vs. salaried.

**Q: How do quick tickets work, and what's the price warning?**
A crew leader logs time/materials in mobile for an unplanned job without a full estimate. Keep the Time Entry price at $0 — setting it above $0 automatically switches the ticket from T&M to Fixed Price on Completion.

**Q: When do visit reminders send?**
The day before the visit at the template time — unless the visit was scheduled after the reminder time, in which case it isn't sent.

**Q: What are absentee notifications and what do they require?**
Internal alerts when a team member hasn't clocked in after the scheduled start. They only work on time-based routes, and the Grace Period sets how long to wait before sending.
