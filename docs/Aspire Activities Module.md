# Aspire Platform – Activities Module

> **Module:** Activities | **Platform:** Aspire Cloud
> **Source:** guide.youraspire.com/docs/activities-1

---

## Overview

The **Activities module** in Aspire is where your team manages all action-oriented records: appointments, emails, tasks, issues, and milestones. Every activity is tied to a person responsible for it and can be linked to a property, opportunity, or work ticket.

You can access Activities from:
- The **Activities module** (main navigation)
- The **To Do List** on the Home screen
- The **Quick Menu** on the Aspire Toolbar

---

## Activity Types

| Type | What it's for |
|------|--------------|
| **Appointment** | Meetings or events. Syncs with Google or Outlook calendar. |
| **Task** | Actions someone needs to complete. Can have a due date. |
| **Issue** | Customer complaints, property damage, or service concerns. Cannot be deleted. |
| **Email** | Emails sent or received. Can sync with Google or Microsoft Exchange. |
| **SMS** | Text messages sent via Marketing Pro integration. Shows delivery status. |
| **Milestone** | Key target dates for opportunities or work tickets. Only created from Work Ticket or Opportunity screens. |

> **Important:** Milestones can only be created from the Activity Search List on a Work Ticket or Opportunity screen — not from the Home screen or Property screen.

---

## Navigating the Activities Module

### Search
- Use the **search bar** for quick keyword lookups (approximate match).
- Use **Advanced Search Tools** to filter, group, sort, and configure your results.
- You can drag and drop column headers to reorder fields.
- Click a field name to change sort order.

### Saving Search Lists
- Go to the **three-dots menu → Save As** to save a custom search list.
- Set a **My Default** list to auto-load your preferred view.
- **Reset Advanced Search** to return to system defaults.

### Export Options
- **Export to Excel (Current View):** Only selected columns.
- **Export to Excel (All Fields):** All available fields.

### Activity Visibility (Branch Access)
Users only see activities linked to branches they have access to. Branch is determined in this order:
1. Branch of the associated invoice
2. Branch of the opportunity service for the work ticket
3. Branch of the opportunity
4. Branch of the property
5. Branch of the user who created the activity

### Default and Additional Search Fields

**Default Fields:** Activity Type, Assigned To, Notes, Priority, Property Name, Regarding, Start Date, Status, Subject

**Additional Fields:** Branch, Category, Completed Date, Completed By, Contact, Created By, Created Date, Days Since Activity Created, Due Date, End Date, Include Client, Invoice Number, Issue #, Location, Reminder

---

## Tasks

### What is a Task?
A task is an action someone in the organization needs to complete. Tasks can have a due date, priority, and notes.

### Where to Create a Task
- **Aspire Toolbar → Add icon → New Task**
- **Work Ticket screen → Activities section → New Task**
- **Activities module → New Activity → New Task**

### Task Fields

| Field | Description |
|-------|-------------|
| **Assigned To** | One or more contacts responsible for the task. Assigned contacts see the task in their Activities list. |
| **Regarding** | Link the task to a Property, Opportunity, or Work Ticket. |
| **Priority** | High, Normal, or Low. |
| **Subject** | Title of the task. Supports expandable tokens if a Regarding value is selected. |
| **Due Date** | Target completion date. Changing the Start Date auto-updates the Due Date to the next day. |
| **Category** | Classifies the task (e.g., Phone Call, To Do). Configured in Administration. |
| **Notes** | Rich-text field for descriptions or progress tracking. Supports tokens. |
| **Attachments** | Upload documents or images related to the task. |

### Task Actions
- **Save** – Saves the task.
- **Complete** – Marks the task as done.
- **Cancel** – Closes without saving.
- **Create a Copy** – Clones the task to use as a template.

---

## Issues

### What is an Issue?
An issue tracks customer complaints, property damage, service requests, or concerns. Issues **cannot be deleted** and are visible in Aspire Mobile when a crew leader opens a property's work ticket.

### Where Issues Appear
- Home Screen
- Customer's activity folder
- Property record
- Work Ticket (visible in Mobile)

### Where to Create an Issue
- **Aspire Toolbar → Quick Menu → New Issue**
- **Activities module → New Activity → New Issue**
- **Work Ticket screen → Activities section → New Issue**
- **Properties screen → Activities section → New Issue**
- **Opportunity screen → Activities section → New Issue**

### Issue Fields

| Field | Description |
|-------|-------------|
| **Assigned To** | Multiple contacts can be assigned. They receive email updates when the issue changes. |
| **Regarding** | Links the issue to a Property, Opportunity, or Work Ticket. |
| **Priority** | High, Normal, or Low. |
| **Subject** | Title of the issue. Supports expandable tokens. |
| **Due Date** | Expected resolution date. |
| **Category** | Type of issue (e.g., Complaint, Service Request, Property Damage). |
| **Include Client** | Sends email to the property's primary contact on every update. |
| **Notes** | Rich-text notes. Each saved note is added to the note log. |
| **Public Checkbox** | If checked, the note is included in emails sent to non-employees (clients). |

### Issue Actions
- **Save** – Saves and sends notification emails to assigned contacts.
- **Complete** – Marks the issue as resolved.
- **Print** – Prints the issue.
- **Create a Copy** – Clone the issue as a template from the Quick Menu.

### Who Gets Email Notifications on Issues?
When an issue is created or updated, Aspire automatically emails:
- Property Account Owner (not if they made the update)
- Property Operations Manager (not if they made the update)
- All contacts in the **Assigned To** field (not if they're the updater)
- Property Primary Contact (only if **Include Client** is enabled)
- Current Branch Manager (when created/updated in Aspire Mobile)

> **Tip:** You can configure issues to send from the Branch Name instead of Company Name. Go to **Admin → Application → Issues** and enable "Issue Email from Branch Name."

### Completing an Issue
Click **Complete** in the upper right corner. The Complete Date will appear. All notes will be emailed to the client unless the **Public** checkbox is unchecked for a specific comment.

### Creating a Work Ticket from an Issue
If an issue needs follow-up work, click the **Create New Opportunity** hyperlink on the Issue screen. A Regarding value (Property, Opportunity, or Work Ticket) must be set for this to work.

---

## Appointments

### What is an Appointment?
An appointment represents a meeting or event. It appears on the Aspire Calendar and on the calendars of all attendees. It can sync with Google or Outlook.

### Where to Create an Appointment
- **Calendar module → double-click a blank space**
- **Aspire Toolbar → Quick Menu → New Appointment**
- **Activities module → New Activity → New Appointment**
- **Work Ticket screen → Activities section → New Appointment**

### How to Create an Appointment

1. **Check "Private Appointment"** if you want to hide details from non-attendees.
2. **Add Attendees** – Search and select contacts. You are added by default. Employee attendees will see the appointment on their Calendar, Activities module, and Contact record.
3. **Set Regarding** – Link to a Property, Opportunity, or Work Ticket. Selecting one auto-fills the Location field with the associated address.
4. **Set Start Date and End Date.**
5. **Enter Location** (auto-filled if Regarding is selected).
6. **Enter Subject** – This appears as the title on the Calendar. Supports tokens.
7. **Add a Note** – Supports rich text, attachments, and tokens.
8. **Click Save.**

### Quick Access Icons on the Appointment Screen

| Icon | Action |
|------|--------|
| Property (building) | Opens the Property record in a new tab |
| Map pin | Opens the address in a map view |
| Trophy | Opens the Opportunity record in a new tab |
| Clipboard | Opens the Work Ticket record in a new tab |

> **Note:** You can link multiple Regarding types to one appointment (e.g., a Property and a Work Ticket). Work Tickets up to 12 months old are available.

---

## Emails

### What is an Email Activity?
The Email screen lets you compose and send emails from within Aspire, or view emails previously sent. Aspire can sync with Google or Microsoft Exchange to import received emails automatically.

### Where to Access Emails
- **Aspire Toolbar → New Email**
- **Invoice screen → Email tab**
- **Receivables Search List → New Email icon**
- **Work Ticket screen → Activities → New Email**
- **Activities module → New Activity → New Email**
- **Properties screen → Activities → New Email**
- **Opportunity screen → Activities → New Email**

### Email Fields

| Field | Description |
|-------|-------------|
| **To** | One or more contacts. Options for invoices: Property Billing Contact, Email Invoice Contact, or Primary Contact. |
| **CC** | Additional contacts to copy. |
| **Regarding** | Links the email to a Property, Opportunity, or Work Ticket. |
| **Subject** | Email subject line. Supports expandable tokens. |
| **Attachments** | Shows count of attached files. Click to view or rename them. |
| **+ Upload Files** | Upload a new file to attach. |
| **Search Existing Attachments** | Find files already stored in Aspire (from Properties, Opportunities, Work Tickets, Issues, or other emails). |
| **Message** | Rich-text body of the email. Supports tokens. |

### Email Actions
- **Send** – Saves and sends the email.
- **Cancel** – Exits without saving.

### Unknown Email Address
If an imported email contains an address not matched to any Aspire contact, an icon appears next to the To/CC field. Clicking it lets you assign the email address to an existing contact or mark it to be ignored in the future.

---

## Milestones

### What is a Milestone?
A milestone represents a key target date for an opportunity or work ticket. Unlike tasks, a milestone has only one date: the date by which associated tasks should be complete.

### Where to Create a Milestone
- **Work Ticket screen → Activities section → New Milestone**
- **Opportunity screen → Activities section → New Milestone**
- **Activity Search List** (only when accessed from the Opportunity or Work Ticket screen)

### Milestone Fields

| Field | Description |
|-------|-------------|
| **Assigned To** | Contacts responsible for or interested in the milestone. |
| **Regarding** | Links to a Property, Opportunity, or Work Ticket. |
| **Priority** | High, Normal, or Low. |
| **Subject** | Title of the milestone. Supports tokens. |
| **Date** | The target milestone date. |
| **Notes** | Rich-text field for descriptions or progress notes. Supports tokens. |

### Milestone Actions
- **Save** – Saves the milestone.
- **Cancel** – Closes without saving.

---

## Attachments

### Select Attachment Screen
The **Select Attachment screen** lets you attach existing files stored in Aspire to emails or other communications. Access it by clicking the **magnifying glass icon** in the Attachments section of any detail screen.

Attachments can be related to: **Properties, Opportunities, Work Tickets, Issues, and Emails.**

### How to Select Attachments
- Use **checkboxes** to select one or more attachments.
- Use **Bulk Actions → Attach Selected** to add multiple files at once.
- Use the **search bar** for quick lookups, or **Advanced Search Tools** to filter and sort.

### Attachment Fields

| Field | Description |
|-------|-------------|
| **Attachment Name** | File name of the saved attachment. |
| **Opportunity Name** | Opportunity linked to the attachment. |
| **Attachment Type** | File format (document, image, etc.). |
| **Regarding** | Module the attachment is linked to (Property, Work Ticket, Opportunity). Pre-filtered by relevance. |
| **Regarding Name** | Specific record name associated with the attachment. |
| **Property Name** | Property linked to the attachment. |
| **Show Crew** | Whether the attachment is visible to crew leaders in the Mobile app. |
| **Attach to Invoice** | Whether the attachment is included in invoice communications. |

### Managing Attachment Search Lists
- **Save As** – Save your current search configuration for reuse.
- **My Default** – Set a default attachment list that auto-loads.
- **Reset Advanced Search** – Return to the system default view.
- **Show All Attachments** – Display all attachments, removing pre-filters.

---

## Frequently Asked Questions

**Q: Can I delete an Issue?**
No. Issues cannot be deleted in Aspire. You can complete them once resolved.

**Q: Who receives emails when I create or update an issue?**
The Property Account Owner, Property Operations Manager, contacts in the Assigned To field, and (if enabled) the Property Primary Contact. The person who made the update is excluded.

**Q: Can I create a Milestone from the Home screen?**
No. Milestones can only be created from the Work Ticket screen or Opportunity screen.

**Q: What happens when I assign someone to a Task or Issue?**
The activity appears in the Activities list on that contact's record. They will also receive email updates when the issue is changed (for Issues).

**Q: Can I link an appointment to multiple records at once?**
Yes. You can select multiple Regarding types — for example, a Property and a Work Ticket — for a single appointment.

**Q: How do I attach existing files from Aspire to an email instead of uploading new ones?**
Use the **Search Existing Attachments** icon on the Email screen. This opens the Select Attachment screen where you can browse and attach files already stored in Aspire.

**Q: Can I send an issue email from my Branch name instead of the Company name?**
Yes. Go to **Admin → Application → Issues** and enable the "Issue Email from Branch Name" checkbox.

**Q: What are expandable tokens?**
Tokens are placeholders in Subject or Notes fields that Aspire automatically replaces with real values (like property name or work ticket number) when the record is saved. They are only available when a Regarding value is selected.

**Q: Can I save my search filters in the Activities module?**
Yes. Configure your search, then go to the three-dots menu and select **Save As**. You can also set a **My Default** search that auto-loads when you open the module.

**Q: If I change a Task's Start Date, does the Due Date change automatically?**
Yes. Changing the Start Date automatically sets the Due Date to the following day. However, if you later change the Start Date to an earlier date, the Due Date remains unchanged.