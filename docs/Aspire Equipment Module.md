# Aspire Platform – Equipment Module

> **Module:** Equipment | **Platform:** Aspire Cloud
> **Source:** guide.youraspire.com/docs/equipment

---

## Overview

The **Equipment module** in Aspire lets you manage your company's equipment assets — from initial request and approval, through active service life, to disposal. It also supports GPS tracking, scheduling, meter reading logs, and service maintenance records.

> **Note for Growth clients:** If you're interested in the **Azuga GPS product** (which includes full Equipment Module access), contact AspireCare or your CSM. Additional costs apply.

---

## Equipment Module Structure

The Equipment module is organized into tabs:
- **Equipment List** – All equipment assets with filter, sort, and group capabilities.
- **Scheduling Tab** – View and schedule shared equipment against work ticket visits.
- **Logs Tab** – Reading logs, service logs, and scheduling logs per asset.

Click any equipment asset to open the **Equipment Details** screen.

---

## Equipment Statuses

Equipment moves through the following statuses over its lifecycle:

| Status | Description | Permission Required |
|--------|-------------|---------------------|
| **Requested** | Initial status when equipment is created | Request Equipment |
| **Approved** | Approved for purchase (no Purchase Date yet) | Approve Equipment |
| **Purchased** | Approved and Purchase Date entered | Purchase Equipment |
| **In Service** | Active, in-use equipment. Most fields become read-only. | Mark Equipment in Service |
| **Out of Service** | Temporarily unavailable. Not visible in Crew Mobile. | Mark Equipment Out of Service |
| **Disposed** | End of life. Disposal Date entered. | Dispose Equipment or Equipment Admin |

> **Note:** Equipment with a **Critical** score in an Equipment Inspection is automatically set to **Out of Service**.

---

## Equipment Details Screen Fields

| Field | Description |
|-------|-------------|
| **Description** | Required. Unique name for the equipment. |
| **Equipment Model** | Required. Must exist in the Equipment Models list. |
| **Purchase Price** | Purchase cost. Requires **Purchase Equipment** permission. |
| **Estimated Purchase Price** | Pre-approval estimated cost. Becomes read-only after purchase is approved. |
| **Warranty Days** | Warranty period in days. |
| **Starting Mileage/Hours** | Initial meter reading. |
| **Active** | Inactive equipment is hidden from lists and unavailable in Crew Mobile. |
| **Model Year** | Year of the equipment model. |
| **Asset Number** | Internal asset label number. |
| **Serial Number** | Manufacturer serial number. |
| **Engine Number** | Engine serial number. |
| **Aspire GPS Identifier** | IMEI number for GPS tracker. Must be unique per device. |
| **Available for Scheduling** | Marks equipment as schedulable on the Route Schedule Board. Requires **Schedule Equipment** permission. |
| **Branch** | Required. Branch currently in possession of the equipment. |
| **Property** | Property where the equipment is currently located. |
| **Division** | Division currently using the equipment. |
| **Route** | Route the equipment is assigned to. Crew leaders can log readings for it in Mobile. |

### Additional Information Fields

| Field | Description |
|-------|-------------|
| **Purchased Date** | Date the equipment was purchased. Required to move to Purchased status. |
| **In Service Date** | Date the equipment entered active service. Requires a Purchase Date first. |
| **Disposal Date / Price / Reason** | Set when disposing of equipment. Requires **Dispose Equipment** or **Equipment Admin** permission. |
| **Financing Bank** | Lending institution for financed equipment. |
| **Plate Number** | License plate for vehicles. |
| **Gross Vehicle Weight** | GVW for the equipment. |
| **Pay Schedule** | Payment months for financed equipment. |
| **Renewal Date** | License plate renewal date. |
| **Dealer** | Dealer from whom the equipment was purchased. |

---

## Equipment Logs

### Reading Logs
Records equipment meter readings. Columns include: Log Date, Reading Date, Meter Reading, Trouble Code, Created User, Branch, Division, Route.

### Service Logs
Records service events. Columns include: Service Tag, Service Date, Technician Name, Cost, Hours, Meter Reading, Branch, Division, Route.

> Only the most recent service entry for a given service can be edited. Previous entries are read-only.

### Scheduling Logs
Read-only view of equipment scheduling history linked to the Route Scheduling Board. Columns: Visit Date, Route, Ticket #, Description, Branch.

---

## Bulk Actions on Equipment

| Action | Description |
|--------|-------------|
| **Dispose** | Bulk dispose multiple In Service assets. Specify disposal date, price, and reason. |
| **Mark In Service** | Simultaneously mark multiple assets as In Service. Set a shared In Service Date. |
| **Set as Available to Schedule / Unavailable** | Enable or disable scheduling availability for multiple assets. |
| **GPS Set Up** | Bulk assign GPS Provider, Tracker Type, Primary Vehicle for Route, and GPS Identifier. |

> **Note:** You cannot mark equipment as Available for Scheduling if it is inactive, disposed, or already assigned to a route.

---

## Scheduling Equipment

When **Available for Scheduling** is checked on an asset:
- It appears on the **Scheduling tab** of the Equipment module.
- It can be assigned to work ticket visits via the Route Schedule Board.
- The Scheduling Log tracks all scheduled visits.

Required permissions: **Schedule Equipment** + **View Equipment** + **Read-Only or Full Access to the Schedule Board**.

---

## GPS Tracking

For companies with GPS integration (Azuga or Fleetsharp):
- Enter the **Aspire GPS Identifier (IMEI)** on each equipment record.
- The **GPS Provider** and **Tracker Type** fields show current disposition/location.
- GPS data updates when meter readings or service events are logged.

> ⚠️ Never assign the same GPS Identifier to two different equipment items — it causes unpredictable tracking behavior.

---

## Company-Owned Equipment: Costing Approach

There are two philosophies for handling owned equipment costs in Aspire:

### Option 1: Include in Service Markups (Recommended)
- Add the cost of owned equipment into **Labor Markup** on equipment-heavy Service Types.
- Equipment becomes part of your **Overhead** in the budget.
- No need to cost equipment down to the Work Ticket level.
- Simpler and avoids A/P reconciliation issues.

### Option 2: Track via Inventory
- Allocate equipment at a cost per day or hour from Inventory to Work Tickets.
- Requires zeroing out inventory at month-end and creating a journal entry.
- More granular but administratively intensive and potentially inaccurate.

> **Best practice:** Most companies use Option 1 (Markup approach) to keep accounting aligned between Aspire and their external accounting system.

---

## Frequently Asked Questions

**Q: What happens when equipment is marked Out of Service?**
It becomes unavailable throughout Aspire and Crew Mobile — including Equipment, Equipment Inspection, Meter Reading screens, and the Request Equipment Service section.

**Q: Can I mark equipment as Out of Service from the New Equipment screen?**
No. Equipment must be saved first and have a status before it can be set to Out of Service.

**Q: What triggers automatic Out of Service status?**
An Equipment Inspection with a **Critical** inspection category score automatically sets the equipment to Out of Service.

**Q: What permissions do I need to dispose of equipment?**
You need **Dispose Equipment** or **Equipment Admin** permission.

**Q: Can two pieces of equipment share the same GPS Identifier?**
No. Each GPS Identifier