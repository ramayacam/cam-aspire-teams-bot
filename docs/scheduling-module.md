# Scheduling Module — Aspire Knowledge Base

System URL: https://cloud.youraspire.com/

## 1. Module Overview

The Scheduling module is where work tickets generated from opportunities/services are placed on calendars, assigned to crews, executed in the field, and have their labor/material time recorded.

Core screens:
| Screen | Purpose |
|---|---|
| Schedule Board | Drag-and-drop calendar to schedule visits by route or property |
| Route Scheduling | Map-based optimization of stops |
| Scheduling Assistant | Auto-generate visits from sequence/recurring rules |
| Time Entry (Daily Acceptance) | Approve crew clock-ins/outs daily |
| Weekly Time Review | Final approval of hours into payroll |
| Aspire Mobile | Crew app for clock-in, time, materials, forms |

---

## 2. Required Permissions

| Permission | Allows |
|---|---|
| Schedule Board – View/Edit | Open & modify schedule |
| Route Scheduling | Use map-based route screen |
| Time Entry – Accept | Approve daily time |
| Weekly Time Review – Approve | Final-approve weekly hours |
| Branch Admin | Configure branch-level mobile/timekeeping settings |
| Subcontractor Portal Admin | Manage legacy subcontractor portal users |

---

## 3. Key Terminology

- **Work Ticket** — A scheduled occurrence of a service on a property.
- **Visit** — A single appearance of a work ticket on the schedule (a ticket can have many visits).
- **Route** — A reusable group of properties + services worked by one crew on a recurring day.
- **Sequenced Schedule** — Visits ordered by sequence # (no clock time).
- **Time-Based Schedule** — Visits with start/end times on the calendar.
- **As-Needed Service** — Service with no pre-built ticket; created on demand.
- **Quick Ticket** — Same-day mobile-created ticket for unplanned work.

---

## 4. Schedule Board

### 4.1 Views
- **Route View** — Rows = crews/routes, columns = days.
- **Property View** — Rows = properties, columns = days. Useful for client-centric scheduling.

### 4.2 Visit Tile Icons
| Icon | Meaning |
|---|---|
| 🟢 | Completed |
| 🟡 | In progress |
| ⚪ | Scheduled (not started) |
| 🔴 | Rejected / time error |
| 📍 | GEO mismatch flagged |
| 📋 | Has checklist |
| 💬 | Has notes |
| 🌧️ | Weather event affected |

### 4.3 Search Prefixes (S.T.O.P.)
| Prefix | Searches |
|---|---|
| `s:` | Service name |
| `t:` | Work ticket # |
| `o:` | Opportunity name |
| `p:` | Property name |
| `c:` | Contact |
| `cr:` | Crew |

### 4.4 Three-Dot / Right-Click Menus
- **Week tile** → Move week, copy week, clear week.
- **Day tile** → Move day, mark day off (weather/holiday).
- **Visit tile** → Edit, reschedule, mark complete, add note, view ticket, delete visit.

### 4.5 Bulk Move Work Tickets
1. Multi-select visits (Ctrl/Shift-click).
2. Right-click → **Bulk Move**.
3. Choose target date/crew → confirm.
   - Sequenced visits keep their relative sequence.
   - Time-based visits preserve relative offsets.

⚠️ Bulk move respects route-level constraints (active dates, crew capacity).

---

## 5. Routes

### 5.1 Creating a Route
Schedule Board → **+ Route** → enter:
- Route name, branch, crew, start/end date, active days.
- Add **Properties** → add **Services** under each property.
- Choose **Sequenced** OR **Time-Based**.

### 5.2 Sequencing & Recurring Schedules
- Sequence # determines order on the day.
- Recurring patterns: weekly, bi-weekly, monthly (Nth weekday), custom.
- Use **Setup Sequence Numbers** screen to renumber in bulk.

### 5.3 Time-Based Scheduling
- Each visit gets explicit start/end time.
- Drag tile edges on Schedule Board to resize.
- Used when crews have appointments or fixed windows.

### 5.4 Bulk Rescheduling (Sequenced & Time-Based)
Schedule Board → **Bulk Reschedule**:
- Select date range and route.
- Shift forward/back N days, skip weekends, or move to specific date.
- Preview impacted visits before confirming.

### 5.5 Activate / Deactivate Routes
- Deactivate stops new visit generation but keeps history.
- Reactivate restores recurring generation from current date.

---

## 6. Scheduling Assistant

Auto-generates visits from recurring/sequenced rules.

Workflow:
1. Open **Scheduling Assistant**.
2. Filter by branch, route, date range.
3. Review proposed visits.
4. **Generate** to push to Schedule Board.

📌 Run weekly to keep the board populated 4–8 weeks out.

---

## 7. Route Scheduling (Map View)

- Map-based screen for optimizing stop order.
- Drag pins to reorder, see drive time between stops.
- Apply optimized sequence back to the route with one click.
- Useful for new routes or when properties are added/removed.

---

## 8. As-Needed Services & Work Tickets

- Service flagged "As Needed" on the opportunity → no auto-tickets.
- Create ticket on demand from the property or schedule board.
- **Change As-Needed Service With No Work Tickets** — Edit service config (price/units) directly on opportunity since no tickets exist yet.

---

## 9. Service Visit Checklists

- Configured per service template.
- Crew completes items in Aspire Mobile.
- Required items block ticket completion until checked.
- Checklist completion stored on the ticket for audit.

---

## 10. Work Ticket Statuses


| Status | Meaning |
|---|---|
| Scheduled | On board, not started |
| In Progress | Crew clocked in |
| Complete | Crew clocked out, ready for review |
| Rejected | Time review sent back |
| Invoiced | Billed to customer |

---

## 11. Time Entry — Daily Acceptance

### 11.1 Workflow
1. Crew clocks time in mobile.
2. Office opens **Time Entry** screen.
3. Review per-crew, per-day entries.
4. Resolve errors → **Accept**.
5. Accepted hours feed Weekly Time Review.

### 11.2 Common Time Entry Errors
| Error | Cause | Fix |
|---|---|---|
| Missing clock-out | Crew forgot to clock out | Add manual clock-out |
| Overlapping time | Two tickets share minutes | Adjust split |
| Outside GEO perimeter | Clocked outside property radius | Verify location, override |
| No ticket assigned | Time on no work ticket | Assign or convert to non-billable |
| Pay code missing | Required pay code blank | Select pay code |
| Future time | Entry timestamp in the future | Correct timestamp |

### 11.3 Drive Time
- Tracked between properties when enabled.
- Auto-calculated from clock-out at site A → clock-in at site B.
- Can be billable or non-billable per branch settings.

### 11.4 GEO Perimeter
- Branch-level radius around property GPS.
- Crews clocking in outside radius are flagged.
- Override permission required to accept.

---

## 12. Weekly Time Review

### 12.1 Status Flow


### 12.2 Screen
- Group by employee, crew, or branch.
- Shows regular, OT, premium, drive, non-billable totals.
- Edit hours inline; audit log captures every change.

### 12.3 Bulk Actions
- Select multiple employees → **Approve All**, **Reject All**, **Reset to Pending**.

### 12.4 Audits
- Every edit logs user, timestamp, before/after.
- Available in Weekly Time Review history pane.

---

## 13. Aspire Mobile

### 13.1 Device Setup
1. Install Aspire Mobile from Google Play / App Store.
2. Tenant ID + login.
3. Device must be authorized by an admin (one-time).
4. Sync schedule on first login.

### 13.2 Offline Mode
- Cached schedule and forms work offline.
- Time, materials, photos queued locally.
- Auto-syncs when connection restored.

### 13.3 Spanish Mode
- Toggle in user profile.
- Translates UI labels (data remains as entered).

### 13.4 Quick Tickets
- Mobile-created same-day tickets for unplanned work.
- Crew picks property + service template → ticket auto-created.
- Requires "Allow Quick Tickets" branch setting + service template flagged.

### 13.5 Pay Code Overrides
Estimator-set per-service pay codes can be overridden in mobile when the crew member is paid differently for certain work.

| Pay Code Type | Effect |
|---|---|
| Premium Dollars | Adds flat $/hr on top of base |
| Premium % | Adds % on top of base |
| Fixed Rate | Replaces base rate entirely |

**Choose Pay Code screen scenarios:**
- Multiple pay codes available → crew selects on clock-in.
- Default pay code set → auto-applied unless changed.
- Locked pay code → no override allowed (admin-controlled).

📌 Pay code overrides flow into Weekly Time Review and respect approval workflow.

### 13.6 Tracking Time with Multiple Pay Codes
- Crew can switch pay codes mid-shift (e.g., regular → snow premium).
- Each segment recorded separately with its own pay code.
- Visible as split rows in Time Entry.

### 13.7 Custom Forms in Aspire Mobile
4 form trigger types:
| Trigger | Fires |
|---|---|
| Clock In | Start of shift |
| Clock Out | End of shift |
| Start Ticket | When ticket begins |
| Complete Ticket | When ticket marked done |

**Setup:** Admin → Application Configuration → Custom Forms → assign to service templates or branches.

**Field types:** text, number, date, dropdown, checkbox, signature, photo, GPS.

**Review locations:** Form responses appear on the work ticket, in property history, and exportable via reports.

⚠️ Required fields block clock-in/out or ticket completion until answered.

---

## 14. 6.21.0 Timekeeping Updates

### 14.1 Branch-Level Settings
- Per-branch: GEO radius, drive time billable/non-billable, allow quick tickets, require checklists, pay code defaults.
- Replaces older tenant-wide settings for multi-branch flexibility.

### 14.2 Time Correction Requests (Mobile)
- Crew submits correction from mobile (e.g., forgot clock-out).
- Routed to supervisor approval queue.
- Approved corrections post to Time Entry automatically.

### 14.3 Auto Time Acceptance
- Branch setting: auto-accept time entries with no errors after N hours.
- Errors still require manual review.
- 📌 Reduces office workload for clean crews.

---

## 15. Branch-to-Branch Subcontract Work

When a property in Branch A is serviced by a crew from Branch B.

| Option | When to Use | Pros | Cons |
|---|---|---|---|
| 1. Branch B as subcontractor on Branch A's ticket | Simple cross-branch labor | Single ticket; clean P&L allocation | Requires subcontractor setup |
| 2. Transfer property to Branch B | Permanent move | Simplest long-term | Loses Branch A history |
| 3. Mirror opportunities in both branches | Joint accountability | Both branches see revenue | Double maintenance |
| 4. Internal labor transfer (journal) | Occasional | No structural changes | Manual accounting work |

📌 Most common: Option 1 (subcontract) for ad-hoc, Option 2 for permanent moves.

---

## 16. Legacy Subcontractor Portal (System Admins)

### 16.1 Admin Setup
1. Enable Subcontractor Portal in Application Configuration.
2. Create subcontractor as a **Contact** with type = Subcontractor.
3. Create portal **User** linked to that contact.
4. Send activation email; subcontractor sets password.

### 16.2 Device Authorization
- Subcontractor's device must be approved by admin on first login.

### 16.3 Time & Material Entry
- Subcontractor logs into portal → sees assigned tickets.
- Enters time, materials, notes.
- Submits → enters Aspire's Time Entry queue.

### 16.4 Partial Occurrence
- If subcontractor completes only part of a visit, mark partial → remainder stays scheduled.

### 16.5 Closed Month Handling
- Time entered against a closed accounting month is flagged.
- Admin must reopen month or re-date entry to current period.

### 16.6 Crew Mobile Visibility
- Subcontractor time also visible in Crew Mobile under the assigned ticket for transparency.

⚠️ Legacy portal is being phased out in favor of Aspire Mobile for subcontractors. Use only if mobile is not feasible.

---

## 17. Lists to Create for the Scheduling Module

Recommended saved list filters:

| List | Filter Recipe |
|---|---|
| Maintenance Recurring (Active) | Service Type = Maintenance, Recurring = Yes, Status = Active |
| Maintenance Non-Recurring | Service Type = Maintenance, Recurring = No |
| Multiple Occurrences This Week | Visit Count > 1, Date = This Week |
| Enhancement Open | Service Type = Enhancement, Ticket Status ≠ Complete |
| Construction WIP | Service Type = Construction, Status In Progress |
| Unscheduled Active Tickets | Scheduled Date is Empty, Ticket Status = Active |
| Past-Due Visits | Scheduled Date < Today, Status ≠ Complete |
| GEO Mismatch Last 7 Days | Time Entry has GEO error, Date = Last 7 days |

📌 Save these as Tile Lists for quick scheduling-team dashboards.

---

## 18. How-To: Search the Schedule Board with Prefixes

Use the **S.T.O.P.** prefixes (section 4.3) in the board search bar.
- `t:12345` → jump straight to ticket #12345.
- `p:Smith` → all visits at properties matching "Smith".
- `cr:North` → all visits for crews containing "North".

---

## 19. Tips and Best Practices

### ✅ Do
- ✅ Run Scheduling Assistant weekly to keep 4–8 weeks visible.
- ✅ Use Route View for crew-centric ops, Property View for client-centric calls.
- ✅ Enable GEO perimeter and Auto Time Acceptance to reduce office review time.
- ✅ Set required custom forms for high-risk services (chemical apps, snow).
- ✅ Use Bulk Reschedule for weather days — never edit visits one-by-one.
- ✅ Train crews on Quick Tickets for unplanned work to avoid lost revenue.
- ✅ Configure pay code defaults at branch level when crews routinely earn premiums.
- ✅ Approve Weekly Time Review by Monday morning to keep payroll on schedule.

### ❌ Don't
- ❌ Don't delete visits to "reschedule" — use right-click → Reschedule (preserves history).
- ❌ Don't bypass GEO errors without verifying location — defeats the purpose.
- ❌ Don't override pay codes without supervisor sign-off if locked at admin.
- ❌ Don't enter subcontractor time in a closed accounting month — reopen or re-date.
- ❌ Don't transfer properties cross-branch just for one-off work — use subcontract option.
- ❌ Don't leave As-Needed services with stale opportunity pricing — review quarterly.

---

## 20. Quick Reference — Daily Scheduling Checklist

1. Open Schedule Board → check today's coverage.
2. Resolve any 🔴 / 📍 visits from yesterday in Time Entry.
3. Accept clean daily time entries.
4. Run Scheduling Assistant if 4-week horizon is thin.
5. Review weather forecast → bulk reschedule if needed.
6. Monday: approve last week's Weekly Time Review.

---

## 21. Source URLs

Primary module: https://guide.youraspire.com/docs/scheduling-1

Sub-categories:
- Using the Scheduling Module: https://guide.youraspire.com/docs/using-the-scheduling-module
- Time Acceptance and Review: https://guide.youraspire.com/docs/time-acceptance-and-review
- Mobile and Time Entry: https://guide.youraspire.com/docs/mobile-and-time-entry
- Legacy Scheduling Documentation: https://guide.youraspire.com/docs/legacy-scheduling-documentation
- Lists to Create: https://guide.youraspire.com/docs/lists-to-create-for-the-scheduling-module

Key articles:
- Schedule Board Screen: https://guide.youraspire.com/docs/schedule-board-screen
- Scheduling Assistant: https://guide.youraspire.com/docs/using-the-scheduling-assistant
- Route Scheduling: https://guide.youraspire.com/docs/route-scheduling-screen-1
- Sequence Numbers & Recurring: https://guide.youraspire.com/docs/setting-up-sequence-numbers-and-recurring-schedules
- Creating & Managing Routes: https://guide.youraspire.com/docs/creating-and-managing-routes
- Search Prefixes: https://guide.youraspire.com/docs/how-to-use-prefixes-to-search-for-schedule-board-work-tickets
- As-Needed Services: https://guide.youraspire.com/docs/using-as-needed-services-and-work-tickets
- Time-Based Scheduling: https://guide.youraspire.com/docs/time-based-scheduling
- Time Entry Errors: https://guide.youraspire.com/docs/understanding-time-entry-errors-in-aspire
- Bulk Reschedule: https://guide.youraspire.com/docs/bulk-rescheduling-sequenced-and-time-based-visits
- Bulk Move: https://guide.youraspire.com/docs/bulk-moving-work-tickets-on-the-schedule-board
- Property View: https://guide.youraspire.com/docs/property-view-schedule-board-1
- Service Visit Checklists: https://guide.youraspire.com/docs/service-visit-checklists
- Change As-Needed Service: https://guide.youraspire.com/docs/change-as-needed-service-with-no-work-tickets
- Time Entry Acceptance Workflow: https://guide.youraspire.com/docs/time-entry-acceptance-workflow-and-checklist
- Approving Weekly Time Review: https://guide.youraspire.com/docs/approving-weekly-time-review-hours
- Weekly Time Review Screen: https://guide.youraspire.com/docs/weekly-time-review-screen
- Drive Time: https://guide.youraspire.com/docs/drive-time
- Time Entry Screen Reference: https://guide.youraspire.com/docs/time-entry-screen-reference
- Aspire Mobile Setup: https://guide.youraspire.com/docs/setting-up-aspire-mobile-on-mobile-devices
- Quick Tickets: https://guide.youraspire.com/docs/enabling-and-using-quick-tickets-in-aspire
- Multiple Pay Codes: https://guide.youraspire.com/docs/tracking-time-with-multiple-pay-codes-in-crew-mobile
- Custom Forms in Mobile: https://guide.youraspire.com/docs/using-custom-forms-in-aspire-mobile
- 6.21.0 Timekeeping Updates: https://guide.youraspire.com/docs/6210-timekeeping-updates
- Branch-to-Branch Subcontract: https://guide.youraspire.com/docs/how-to-manage-branch-to-branch-subcontract-work
- Legacy Subcontractor Portal: https://guide.youraspire.com/docs/using-the-legacy-subcontractor-portal-for-system-admins