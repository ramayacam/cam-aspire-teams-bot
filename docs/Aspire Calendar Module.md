# Aspire Platform – Calendar Module

> **Module:** Calendar | **Platform:** Aspire Cloud
> **Source:** guide.youraspire.com/docs/calendar-1

---

## Overview

The **Calendar module** in Aspire lets you keep track of your Tasks and Appointments in one place. You can sync it with your Microsoft Outlook or Gmail calendar so everything stays up to date across platforms.

By default, you only see Tasks and Appointments assigned to you. With the right permissions, you can also view calendar entries for other users in your organization.

> **Sync window:** When Aspire syncs with an external calendar, it looks back **10 days** and forward **60 days** to identify appointments to update.

---

## Calendar Screen Elements

| Screen Element | Description |
|----------------|-------------|
| **Contacts** | Search for and select employee contacts to view their calendars. Other users' private appointments still appear but only show "Private" — no details are visible. |
| **View Selector** | Switch between **Day**, **Week**, **Month**, or **Agenda** views. Agenda view shows one week of tasks and appointments starting from today. |
| **Calendar Refresh Icon** | If synced with Outlook or Gmail, the calendar auto-syncs once per hour. Click this icon to trigger an immediate sync. Syncing may take a couple of minutes. |
| **Date Selector** | Use the arrows to move backward or forward in the current view. Click the date drop-down to jump to a specific date. |

---

## Creating and Editing Appointments

### How to Create an Appointment from the Calendar
**Double-click on any empty space** in the Calendar to open a new Appointment screen.

### How to Edit an Appointment
**Double-click on an existing appointment** in the Calendar to open and edit it.

For full details on all appointment fields, see the section below.

---

## Appointment Screen – Full Reference

### Where to Open the Appointment Screen
- **Calendar module** → double-click an empty space (create) or double-click an existing appointment (edit)
- **Aspire Toolbar → Quick Menu → New Appointment**
- **Activities module → New Activity → New Appointment**
- **Work Ticket screen → Activities section → New Appointment**

### Step-by-Step: Creating a New Appointment

1. **Private Appointment** – Check this box if you want to hide the appointment details from users who are not attendees.
2. **Attendees** – Search and select contacts who will attend. You are added by default. Remove yourself if scheduling for someone else. Employee attendees will see the appointment on their Calendar, in their Activities module, and on their Contact record.
3. **Regarding** – Link the appointment to a Property, Opportunity, or Work Ticket. Selecting one automatically fills in the **Location** field with the associated address. You can select multiple Regarding types (e.g., a Property and a Work Ticket). Work Tickets up to 12 months old are available.
4. **Start Date / End Date** – Type or select when the appointment starts and ends.
5. **Location** – Auto-filled when a Regarding record is selected. Can also be typed manually.
6. **Subject** – The title that appears on the Calendar. Supports expandable tokens (click the magnifying glass icon to insert one).
7. **Notes** – Rich-text field. Supports formatting, attachments, and tokens. Available tokens change based on the Regarding selection.
8. **Save** – The appointment appears on your Calendar and the Calendars of any employee attendees.

### Quick Access Icons on the Appointment Screen

| Icon | Action |
|------|--------|
| 🏢 Building (Property) | Opens the linked Property record in a new tab |
| 📍 Map pin | Opens the associated address in a map view |
| 🏆 Trophy (Opportunity) | Opens the linked Opportunity record in a new tab |
| 📋 Clipboard (Work Ticket) | Opens the linked Work Ticket record in a new tab |

### Key Behaviors
- Selecting a Property, Opportunity, or Work Ticket in the **Regarding** field **automatically sets the Location** to the associated address.
- **Expandable tokens** in Subject and Notes are replaced with real values (like property name or work ticket number) when you save. They only work when a Regarding value is selected.
- If you add an **employee contact** as an attendee, the appointment appears on their personal Calendar, Activities list, and Contact record.
- **Private appointments** still show as a block on other users' calendars but display no details.

---

## Syncing Your Calendar (and Email) with Aspire

### Supported Providers
- **Microsoft 365**
- **Microsoft Exchange**
- **Google / Gmail**

> Any other email provider must rely on the SMTP option via SPF and DNS validation.

### What Syncs
- **Calendar:** Appointments created in Aspire can sync to Outlook/Gmail, and appointments created in Outlook/Gmail can appear in Aspire.
- **Email:** Emails sent from Aspire can go through your Exchange, Gmail, or Microsoft 365 account and appear in your Sent folder. You can also pull selected emails into Aspire.

### Important Things to Know Before Syncing
- Recurring appointments must be scheduled in Microsoft Exchange, Microsoft 365, or Gmail — they can display in Aspire if synced, but cannot be created there.
- Calendar events created **outside of Aspire** are **read-only** in Aspire.
- Mail-enabled groups (distribution lists, shared mailboxes) are **not supported** for email sync.
- Only sync **one Aspire user per Microsoft 365 account** to avoid throttling from Microsoft.
- The sync token lasts **90 days** and refreshes each time you log in.

### How to Set Up Email and Calendar Sync

1. Select your **profile icon** in the lower-left corner → **User Settings**.
2. In the **Sync** section, check **Sync Email** and/or **Sync Calendar**.
3. *(Optional)* Check **Sync Aspire Folder** (see below).
4. Choose your **Calendar Privacy** setting (Public or Private).
5. Select your **Provider** and follow the steps for that provider:

**Microsoft 365:**
- Click Save → log in with your Microsoft credentials when prompted.
- If you see "Admin approval required," your company's Microsoft admin must approve the Aspire app in the Microsoft Azure / Entra ID portal.
- If MFA is enabled, complete the authentication step.

**Exchange:**
- Enter your Exchange **Email Address**, **Username**, and **Password**.
- Click Save.

**Google:**
- Enter your work **Email Address**.
- Click Save → a Google login prompt appears. Sign in and complete MFA if required.
- Note: It can take up to **24 hours** for the Aspire labels to appear in Gmail.

### Using the "Sync Aspire Folder" Option
When enabled, Aspire creates two folders (labels in Gmail) in your email account: **Aspire** and **Processed**.

- Move any email from your inbox into the **Aspire** folder.
- On the next hourly sync, the email moves to the **Processed** folder and appears in the Activities tab for the matching contact in Aspire.
- **Note:** The Regarding field is not filled in automatically. You'll need to manually link the email to a Property, Opportunity, or Work Ticket in Aspire.

### Calendar Privacy Settings

| Setting | Who Can See Your Events |
|---------|------------------------|
| **Public** | All users in your company |
| **Private** | Only users you share your calendar with. Others see a time block with no details. |

---

## How to Resync Your Calendar or Email

If synced emails show as "Undeliverable" or are going to the wrong place, resync your account:

1. Go to **Profile icon → User Settings**.
2. **Uncheck** Sync Email and Sync Calendar → click **Save**.
3. Go back to **User Settings**.
4. **Re-check** Sync Email and Sync Calendar.
5. Select your Provider and follow the setup steps again.
6. Click **Save**.

If the issue persists, contact **AspireCare**.

---

## Frequently Asked Questions

**Q: Can I view other users' calendars?**
Yes, but only with the appropriate permissions. Other users' private appointments will appear as "Private" with no details visible.

**Q: How often does the calendar sync with Outlook or Gmail?**
Automatically once per hour. You can trigger an immediate sync by clicking the **Calendar Refresh icon**.

**Q: How far back and forward does the calendar sync go?**
Aspire looks back **10 days** and forward **60 days** when syncing with an external calendar.

**Q: Can I create recurring appointments in Aspire?**
No. Recurring appointments must be created in Microsoft Exchange, Microsoft 365, or Gmail. They can display in Aspire once synced, but are read-only.

**Q: What happens if I change my email password after syncing?**
Your sync will break. You'll need to resync by unchecking and re-checking the Sync Email and Sync Calendar options in User Settings.

**Q: How do I sync a specific email from my inbox into Aspire?**
Enable the **Sync Aspire Folder** option. Then drag the email into the "Aspire" folder in your email client. It will appear in Aspire after the next sync.

**Q: Does the Regarding field fill in automatically when I sync an email via the Aspire Folder?**
No. You'll need to open the email activity in Aspire and manually link it to a Property, Opportunity, or Work Ticket.

**Q: Can I add multiple Regarding records to one appointment?**
Yes. For example, you can link both a Property and a Work Ticket to a single appointment.

**Q: What does "Private Appointment" do?**
It hides the appointment's details from all users who are not listed as attendees. The time block still appears on their calendar, but shows no information.

**Q: How long does the Microsoft 365 or Google sync token last?**
**90 days.** It refreshes automatically each time you log in. If it expires or your password changes, you'll need to resync.