# Aspire Platform – Reports Module

Module: Reports | Platform: Aspire Cloud  
Source: guide.youraspire.com/docs/reports

---

## Overview

The Reports module in Aspire gives you access to standard reports, pivot reports, and custom report layouts. Reports help you analyze business performance across CRM, Sales, Purchasing, Invoicing, and Production.

---

## Types of Reports in Aspire

| Type | Description |
|---|---|
| Standard Reports | Pre-built reports available directly from the Reports module (e.g., Contract Renewal, Sales Commission, EOM Report). |
| Pivot Reports | Flexible data tables you configure with filters, rows, columns, and data fields. Available for Work Tickets, Sales, Purchases, and Hours. |
| Saved Lists | Custom filtered views saved in each module (Activities, Properties, Work Tickets, etc.) |
| KPI & Insight Charts | Visual dashboards on the Home Screen for key metrics like Profit/Loss, Sales Pipeline, and Scorecards. |
| Custom Report Layouts | Printable report layouts (invoices, proposals, work tickets, etc.) customized using the Web Report Designer. |

---

## Recommended Reports to Set Up

These are the top reports Aspire recommends for managing your business. Use them as starting points for saved lists.

### CRM Reports

| # | Report Name | Module | Purpose |
|---|---|---|---|
| 1 | Open Issues | Activities | View all open issues |
| 2 | MTD Client Touches by User | Activities | Track all activity except issues for the month |
| 3 | MTD Client Complaints | Activities | Track complaints recorded this month |
| 5 | Property Clean Up Checklist | Properties | Find properties with missing info |
| 6 | Contact Clean Up Checklist | Contacts | Find contacts with missing info |

### Sales Reports

| # | Report Name | Module | Purpose |
|---|---|---|---|
| 9 | New Property Leads MTD | Properties | Properties created this month |
| 12 | Sales Silo | Opportunities | Sales by division for the year |
| 14 | Sold Opportunities MTD | Opportunities | Won opportunities this month |
| 17 | MTD Renewals Report | Reports | Contracts up for renewal |
| 18 | Sold GM YTD | Opportunities | Won opportunities gross margin |

### Purchasing Reports

| # | Report Name | Module | Purpose |
|---|---|---|---|
| 21 | Unpurchased Materials ±30 Days | Purchasing Assistant | Materials not yet purchased |
| 23 | New Purchase Receipts – Through Today | Purchasing | New receipts to process |
| 24 | Received Purchase Receipts | Purchasing | Receipts received but not approved |
| 25 | Approved Purchase Receipts – Last Month | Purchasing | Last month's approved receipts |

### Production Reports

| # | Report Name | Module | Purpose |
|---|---|---|---|
| 40 | Open Maintenance Tickets – Through Today | Work Tickets | Overdue maintenance tickets |
| 46 | Completed Ticket Analysis MTD | Work Tickets | Completed maintenance tickets this month |
| 49 | YTD Revenue Per Hour | Work Tickets Pivot | Revenue efficiency by division |
| 51 | Divisional Analysis | Work Tickets Pivot | GM comparison by division |
| 58 | EOM Revenue | EOM Report | End of month revenue by division |

---

## How to Build a Saved List

1. Navigate to the module (Activities, Properties, Work Tickets, etc.).
2. Use **Advanced Search Tools** to set filters, display fields, sort, and group.
3. Click the **three-dot menu** → **Save As** to save the list.
4. Set it as **My Default** to auto-load it when you open that module.

> Saved lists are module-specific — a list saved in Activities does not carry over to Properties.

---

## Pivot Reports

Pivot Reports give you flexible multi-dimensional analysis. Available pivot types:

- **Work Ticket Pivot** – analyze completed tickets by division, route, employee, month
- **Sales Pivot** – analyze opportunities by sales rep, division, status, month
- **Purchases Pivot** – analyze material allocations and purchase receipts
- **Hours Pivot** – analyze labor hours for payroll and efficiency

### Key Pivot Report Fields

| Field Type | Purpose |
|---|---|
| Data Display Fields | The metrics shown in the cells (e.g., Gross Margin, Hours, Cost) |
| Row Display Fields | What the rows represent (e.g., Division, Property, Employee) |
| Column Display Fields | What the columns represent (usually a time period like Month) |
| Filter Fields | Narrow results by date, division, status, etc. |

---

## Web Report Designer

The Web Report Designer is a tool for customizing the printable report layouts used throughout Aspire (invoices, proposals, work tickets, etc.).

**Required Permission:** Administration → User Management → User Roles → check **"Report Designer Access"**

**Access:** Administration → Application → Web Report Designer

### Customizable Report Types (16 total)

| Report Type | Location |
|---|---|
| Invoice | Invoicing |
| Opportunity Proposal | Opportunity Details or Estimate Details |
| Work Ticket | Work Tickets |
| Equipment Inspection | Reports Module |
| Invoice Statement | Invoicing → Receivables |
| Opportunity Estimate Sheet | Opportunity → Estimate |
| Daily Plan | Schedule Board |
| Receipt | Purchasing → Purchase Receipts |
| Employee Weekly Time Card | Weekly Time Review |
| Client Budget | Property |
| Quality Audit | Property |
| Payment | Invoicing → Payments |
| Deposit | Invoicing → Deposit |
| Daily Timesheet | Schedule Board |
| Inventory Allocation Report | Purchasing → Inventory |
| Opportunity Work Ticket Items | Reports → Work Ticket Item Sourcing |

### Key Concepts

**Report Bands** define sections of the report layout:

| Band | Purpose |
|---|---|
| ReportHeader | Appears once at the start (cover page, logo) |
| PageHeader | Appears at the top of every page (column headers, page numbers) |
| GroupHeader | Appears at the start of each data group. Controls grouping logic. |
| DetailBand | Displays one record at a time from the data source |
| GroupFooter | Appears at the end of each group (subtotals) |
| ReportFooter | Appears once at the end (totals, signatures) |
| PageFooter | Appears at the bottom of every page |

- **Calculated Fields** — create custom expressions using data fields, math operators, and functions.
- **Formatting Rules** — apply conditional formatting (show/hide, color changes) based on True/False conditions.
- **Data Members** — the datasets pulled from Aspire. Each report type has its own set of available fields.

### Saving Reports

| Method | When to use |
|---|---|
| Save (same version) | Minor changes — Unpublish, edit, then Publish. Previous state is lost. |
| Save As (new version) | Major changes — creates a new version you can revert to if needed. |
| Save As (copy) | Duplicating a report layout as a starting point for a new one. |

> Use Administration → Set Up Report Layout Defaults to control which version is used for each report type.

---

## KPI and Insight Charts

KPI charts appear on the **Home Screen** and provide visual performance dashboards.

### Available KPI Types

- **Sales Scorecard KPI** – tracks proposed and closed revenue goals per sales rep
- **Profit and Loss KPI** – tracks revenue vs. expenses
- **Sales Pipeline Insight** – shows opportunity pipeline by stage
- **Client Management KPI** – tracks client-related metrics

### Creating a KPI

1. On the Home Screen, go to the **KPI and Insights** section.
2. Click the **three-dot menu** → **New**.
3. Select the KPI or Insight Type.
4. Set the Date Range, relevant filters, and who to share it with.
5. Click **Save**.

---

## Frequently Asked Questions

**Q: What's the difference between a saved list and a report?**  
A saved list is a filtered, sortable view within a module. A report (in the Reports module) is a printable or pivot-based output designed for deeper analysis.

**Q: Can I export saved lists to Excel?**  
Yes. From any list, go to the three-dot menu and choose **Export to Excel (Current View)** or **Export to Excel (All Fields)**.

**Q: How do I find recommended reports to build?**  
See the Recommended Reports and Lists to Create in Aspire article (also known as Aspire's Top 60) for filters, display fields, and groupings for 60+ useful reports.

**Q: What permission is needed for the Web Report Designer?**  
You need **Report Designer Access** added to your user role in Administration.

**Q: Can I undo changes in the Web Report Designer?**  
Yes. Use the Undo/Redo buttons on the Toolbar. Be careful when deleting Calculated Fields or Formatting Rules — a confirmation dialog is not shown.

**Q: How do I make a copy of a report layout?**  
Open the report in Web Report Designer → Menu → Save As → enter a new name and select branches.
