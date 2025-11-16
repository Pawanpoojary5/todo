# TaskFlow - User & Admin Workflow Guide

## 👤 REGULAR USER WORKFLOW

### 1️⃣ Create Your Account

**Step 1:** Go to http://127.0.0.1:8000/
**Step 2:** Click **"Sign Up"** button (top right)
**Step 3:** Fill the form:
```
First Name: (optional) John
Last Name:  (optional) Doe
Email:      john@example.com
Username:   johndoe
Password:   StrongPassword123!
Confirm:    StrongPassword123!
```
**Step 4:** Click **"Create Account"**
**Result:** ✅ Account created & automatically logged in

---

### 2️⃣ Create Your First Task

**Step 1:** Click **"Tasks"** button in navbar (shows after login)
**Step 2:** Click **"➕ New Task"** button
**Step 3:** Fill the form:
```
Task Title:    Complete project documentation (required)
Description:   Write user guides and API docs (optional)
Priority:      High (or Low/Medium/Urgent)
Status:        In Progress
Due Date:      2025-11-30 17:00 (optional)
```
**Step 4:** Click **"Create Task"**
**Result:** ✅ Task appears in your task list

---

### 3️⃣ Manage Your Tasks

#### View All Tasks
- Click **"Tasks"** in navbar
- See all your tasks with:
  - Task title and description
  - Priority badge (color-coded)
  - Status badge (color-coded)
  - Due date
  - Edit & Delete buttons

#### Filter Tasks by Status
- Click filter buttons at top of task list:
  - **All Tasks** - Show everything
  - **Pending** - Not started
  - **In Progress** - Currently working on
  - **Completed** - Finished tasks
  - **On Hold** - Paused tasks

#### Edit a Task
1. Click **"Edit"** button on any task
2. Update fields as needed
3. Click **"Create Task"** button (saves changes)

#### Delete a Task
1. Click **"Delete"** button on any task
2. Confirm deletion on next page
3. Task removed from list

---

### 4️⃣ View Features & Suggest Ideas

#### Browse Features
- Click **"Features"** in navbar
- See 6 built-in features:
  - ⚡ Lightning Fast
  - 🎯 Smart Prioritization
  - 📱 Fully Responsive
  - 🔒 Secure & Private
  - 🌙 Dark Mode
  - ✨ Beautiful Design

#### Suggest a New Feature
1. Click **"Features"** in navbar
2. If logged in, see **"Suggest a Feature"** button
3. Fill form with:
   ```
   Feature Title: Advanced Calendar View
   Description:   Add calendar interface to view tasks by date
   ```
4. Submit
5. Result: ✅ Suggestion sent to admin for review

---

### 5️⃣ Account Management

#### View Your Profile
- Click your username in navbar
- Shows your information

#### Logout
1. Click **"Logout"** button in navbar
2. You're logged out
3. Redirected to home page

#### Login Again
1. Click **"Login"** button (appears after logout)
2. Enter username/email and password
3. Click **"Sign In"**
4. ✅ Logged in again

---

## 👨‍💼 ADMIN WORKFLOW

### 1️⃣ Access Admin Panel

**URL:** http://127.0.0.1:8000/admin/

**Login:**
```
Username: admin
Password: Rohan@9845
```

---

### 2️⃣ Manage Features

#### View All Features
1. Click **"Features"** in left sidebar
2. See table with all features:
   - Title
   - Status (Active/Inactive)
   - Created date
   - Orders

#### Add New Feature
1. Click **"Add Feature"** button (top right)
2. Fill form:
   ```
   Feature Title:    Offline Mode
   Description:      Use the app without internet connection
   Icon (emoji):     📡
   Order:            6
   Active:           ✓ Checked
   ```
3. Click **"Save"**
4. ✅ Feature appears on /features/ page

#### Edit Feature
1. Click on feature name in list
2. Update any field
3. Click **"Save"**

#### Deactivate Feature
1. Click on feature
2. Uncheck **"Active"** checkbox
3. Click **"Save"**
4. Feature hidden from users (but not deleted)

#### Sort Features by Order
- Features display in numerical order (0, 1, 2, etc.)
- Lower numbers appear first
- Adjust "Order" field to rearrange

---

### 3️⃣ Review User Suggestions

#### View Suggested Features
1. Click **"Suggested Features"** in left sidebar
2. See all user suggestions:
   - Title
   - Who suggested it
   - Vote count
   - Approval status
   - Date created

#### Approve Suggestion
1. Click on suggestion title
2. Check **"Approved"** checkbox
3. Click **"Save"**
4. ✅ Suggestion becomes visible to users

#### Promote Popular Ideas
- Suggestions sorted by vote count (most popular first)
- Look at high-vote suggestions for implementation priority

---

### 4️⃣ Monitor All User Tasks

#### View All User Tasks
1. Click **"Todos"** in left sidebar
2. See all tasks from all users:
   - Task title
   - Who created it
   - Priority (badge)
   - Status (badge)
   - Due date
   - Created date

#### Filter Tasks
- By Status: Click "Status" filter
- By Priority: Click "Priority" filter
- By User: Click "User" filter
- By Date: Click "Created At" filter

#### Search Tasks
- Use **search box** at top
- Search by:
  - Task title
  - Description
  - Username

#### View Task Details
1. Click on task title
2. See all details:
   - User who owns it
   - Full description
   - Priority level
   - Current status
   - Due date
   - When created
   - When last updated
   - When completed (if done)

#### Edit User Task (if needed)
1. Click on task title
2. Update any field
3. Click **"Save"**

#### Delete User Task (if needed)
1. Click on task title
2. Scroll to bottom
3. Click **"Delete"** button
4. Confirm deletion

---

### 5️⃣ Manage Users

#### View All Users
1. Click **"Users"** in left sidebar
2. See all registered users:
   - Username
   - Email
   - First/Last name
   - Staff status
   - Superuser status
   - Last login
   - Date joined

#### Create New User
1. Click **"Add User"** button
2. Enter username and password
3. Click **"Save and continue editing"**
4. Add email and other info
5. Click **"Save"**

#### Change User Password
1. Click on username
2. Click **"This form has read-only fields. No changes can be made here. To change it, go to this form."** link
3. Click **"Change Password"** link
4. Enter new password twice
5. Click **"Change Password"**

#### Make User Admin
1. Click on user
2. Check **"Staff status"** to make them staff
3. Check **"Superuser status"** to make them admin
4. Click **"Save"**

#### Delete User
1. Click on username
2. Scroll to bottom
3. Click **"Delete"**
4. Confirm on next page

---

### 6️⃣ Dashboard Overview

#### Quick Stats
- Total users registered
- Total tasks created
- Total feature suggestions
- Active/inactive features

#### Recent Activity (if implemented)
- New users this week
- Tasks completed this week
- New feature suggestions

---

## 🔍 TASK PRIORITY & STATUS GUIDE

### Priority Levels
```
🔵 Low      - Can be done anytime, low impact
🟡 Medium   - Should be done soon, moderate impact
🔴 High     - Important, do before others
⚫ Urgent   - Critical, do immediately
```

### Task Status
```
⚪ Pending      - Not started yet
🔵 In Progress  - Currently working on it
✅ Completed    - Done and finished
⏸️ On Hold      - Paused, will resume later
```

---

## 📊 DATA VISIBILITY RULES

### Users Can See:
- ✅ Their own tasks only
- ✅ All public features
- ✅ Other users' suggested features (if approved)
- ✅ Their own profile
- ✅ Public about page

### Users CANNOT See:
- ❌ Other users' tasks
- ❌ Other users' profiles
- ❌ Unapproved suggestions
- ❌ Admin panel

### Admins Can See:
- ✅ All users' tasks
- ✅ All users' profiles
- ✅ All features
- ✅ All suggestions (approved & pending)
- ✅ Complete user database
- ✅ Admin panel with full control

---

## 🔐 SECURITY BEST PRACTICES

### For Users:
1. **Use Strong Passwords**
   - Mix uppercase, lowercase, numbers, symbols
   - At least 8 characters
   - Don't use personal information

2. **Keep Email Private**
   - Your email isn't shown to other users
   - Only used for authentication

3. **Don't Share Passwords**
   - Each person needs their own account
   - No password sharing

4. **Logout When Done**
   - Click logout on shared computers
   - Closes your session

### For Admins:
1. **Change Default Password**
   - Don't use Rohan@9845 in production
   - Set a strong admin password

2. **Create Staff Accounts**
   - Don't share admin credentials
   - Create individual admin accounts

3. **Monitor Activity**
   - Regularly review user activities
   - Check suggested features
   - Manage spam or inappropriate suggestions

---

## 🚀 COMMON TASKS QUICK REFERENCE

| Task | Steps |
|------|-------|
| **Sign Up** | Click Sign Up → Fill form → Create Account |
| **Login** | Click Login → Enter credentials → Sign In |
| **Create Task** | Click Tasks → New Task → Fill → Create |
| **Edit Task** | Tasks → Click Edit → Update → Save |
| **Delete Task** | Tasks → Click Delete → Confirm |
| **Filter Tasks** | Tasks → Click status filter → View results |
| **Logout** | Click Logout in navbar |
| **Suggest Feature** | Features → Suggest → Fill → Submit |
| **Access Admin** | /admin/ → Login → Manage features/users/tasks |
| **Approve Suggestion** | Admin → Suggested Features → Check Approved → Save |
| **Add New Feature** | Admin → Features → Add Feature → Fill → Save |

---

## ⚠️ TROUBLESHOOTING

### "Incorrect password or username"
- **Check:** Username spelling (case-sensitive for email)
- **Check:** Caps Lock is off
- **Solution:** Click "Forgot Password" (if implemented)

### "This email is already registered"
- **Reason:** Email used for another account
- **Solution:** Use different email or login with existing account

### "Email already exists"
- **Reason:** During signup, email taken
- **Solution:** Use another email or login instead

### "Task not appearing in list"
- **Check:** Logged in to correct account
- **Check:** Filter is set to "All Tasks"
- **Solution:** Refresh page with Ctrl+F5

### "Can't delete task"
- **Reason:** Database error or permissions
- **Solution:** Try again or contact admin

### "Features not showing"
- **Check:** Admin hasn't deactivated them
- **Check:** /features/ page loads
- **Solution:** Refresh page or clear browser cache

### "Admin panel won't load"
- **Reason:** Not logged in as admin
- **Solution:** Logout and login with admin credentials

### "Feature suggestion not showing up"
- **Reason:** Admin hasn't approved it yet
- **Solution:** Wait for admin review

---

## 📱 MOBILE ACCESS

### All Pages Work on Mobile:
- ✅ Home page - Responsive design
- ✅ Login/Signup - Optimized forms
- ✅ Task list - Stacked layout
- ✅ Create task - Full-screen form
- ✅ Features - Responsive grid
- ✅ About page - Mobile friendly

### Admin Panel:
- ⚠️ Limited on mobile (better on desktop)
- Use desktop browser for full admin features

---

## 🎯 KEY FEATURES SUMMARY

| Feature | User Access | Admin Access |
|---------|-------------|--------------|
| Create Account | ✅ | ✅ |
| Create Task | ✅ Own only | ✅ All |
| View Features | ✅ | ✅ |
| Suggest Features | ✅ | ✅ |
| Manage Features | ❌ | ✅ |
| Approve Suggestions | ❌ | ✅ |
| View All Tasks | ❌ | ✅ |
| Manage Users | ❌ | ✅ |
| Admin Panel | ❌ | ✅ |

---

## 💡 TIPS & TRICKS

### For Users:
1. **Set Due Dates** - Tasks with due dates help track deadlines
2. **Use Priorities** - Mark urgent tasks high priority
3. **Update Status** - Keep status updated for accurate tracking
4. **Describe Tasks** - Add descriptions for context later
5. **Filter Often** - Use filters to focus on what matters now

### For Admins:
1. **Order Features** - Arrange by importance/popularity
2. **Review Suggestions** - Check suggested features weekly
3. **Monitor Tasks** - Track user engagement via task creation
4. **Create Staff** - Distribute admin duties to trusted staff
5. **Regular Backup** - Back up database regularly

---

**You're all set! Start using TaskFlow today! 🚀**
