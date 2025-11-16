# TaskFlow - Complete URL Reference

## 🌐 ALL AVAILABLE ENDPOINTS

### PUBLIC PAGES (No Login Required)

#### Homepage & Basic Pages
```
GET  /                    → Homepage (hero + 6 features)
     Display Name: Home
     Template: todowork.html
     Features: Feature showcase, CTA banner

GET  /about/              → About page
     Display Name: About
     Template: about.html
     Features: Profile, skills, contact

GET  /features/           → Features showcase
     Display Name: Features
     Template: features.html
     Features: All features, suggestions (if logged in)
```

---

### AUTHENTICATION ROUTES (Public)

#### User Registration
```
GET  /signup/             → Show signup form
POST /signup/             → Process registration
     Form: CustomUserCreationForm
     Fields: first_name, last_name, email, username, password
     Validates: Email uniqueness, password strength
     On Success: Login user, redirect to /
     Template: signup.html

GET  /login/              → Show login form
POST /login/              → Process login
     Form: CustomAuthenticationForm
     Fields: username (or email), password
     On Success: Create session, redirect to /
     Template: login.html

GET  /logout/             → Logout user
     Action: Destroy session
     Redirect: Home page (/)
     Message: "You have been logged out successfully"
```

---

### USER ROUTES (Login Required)

#### Task Management
```
GET  /todos/              → List user's tasks
     Template: todos_list.html
     Features: Filter by status, see priority badges
     Accessible: Logged-in users only

POST /todos/create/       → Show create task form
GET  /todos/create/       → Create task page
     Template: create_todo.html
     Form: TodoForm
     Fields: title, description, priority, status, due_date
     On Success: Create task, redirect to /todos/

GET  /todos/<id>/edit/    → Edit task form
POST /todos/<id>/edit/    → Update task
     Template: edit_todo.html
     Form: TodoForm
     Validates: User ownership
     On Success: Update task, redirect to /todos/

GET  /todos/<id>/delete/  → Delete confirmation
POST /todos/<id>/delete/  → Delete task
     Template: delete_todo.html
     Validates: User ownership
     On Success: Delete task, redirect to /todos/
     Message: "Task deleted successfully!"
```

#### Feature Management (Users)
```
GET  /features/suggest/   → Suggest feature form
POST /features/suggest/   → Create suggestion
     Template: suggest_feature.html
     Form: SuggestedFeatureForm
     Fields: title, description
     Validates: User not duplicate suggester
     On Success: Create suggestion, redirect to /features/
     Message: "Thank you! Your feature suggestion has been received"
```

---

### ADMIN ROUTES (Staff Login Required)

#### Django Admin Panel
```
GET  /admin/              → Django admin panel
POST /admin/              → Admin login/actions
     Username: admin
     Password: Rohan@9845
     Features: Full database management
```

#### Feature Management (Admin)
```
GET  /features/add/       → Add feature form
POST /features/add/       → Create feature
     Template: createfeatures.html
     Form: FeatureForm
     Fields: title, description, icon_svg, order, is_active
     Validates: Staff only
     On Success: Create feature, redirect to /features/
     Message: "Feature added successfully!"
```

---

## 📊 DETAILED ROUTE INFORMATION

### Homepage (/)
```
Method: GET
Authentication: None
Template: todowork.html
Context:
  - features: All active features from database
Data Displayed:
  - Hero section with product name & tagline
  - 6 feature cards with icons & descriptions
  - Stats section
  - Call-to-action banner
Navbar Shows:
  - Login & Sign Up (if not authenticated)
  - Username, Tasks, Logout (if authenticated)
```

### About Page (/about/)
```
Method: GET
Authentication: None
Template: about.html
Context: None (static content)
Data Displayed:
  - Profile section
  - Social media links
  - Skills grid
  - Contact information
Navbar Shows:
  - Same as homepage
```

### Features Page (/features/)
```
Method: GET
Authentication: None (but enhanced for logged-in users)
Template: features.html
Context:
  - features: All active features
  - suggested_features: Approved suggestions (if logged in)
Data Displayed:
  - All feature cards
  - Approved suggestions (if logged in)
  - "Suggest a Feature" button (if logged in)
Navbar Shows:
  - Same as homepage
```

---

### Signup (/signup/)
```
Method: GET → Display form
Method: POST → Process registration

GET Response:
  - Template: signup.html
  - Form: CustomUserCreationForm
  - Fields:
    * First Name (optional)
    * Last Name (optional)
    * Email (required, must be unique)
    * Username (required, must be unique)
    * Password (required, 8+ chars, strong)
    * Confirm Password (required, must match)

POST Processing:
  - Validate form data
  - Check email uniqueness
  - Hash password
  - Create user in database
  - Automatically log user in
  - Redirect to homepage (/)
  - Show success message

Error Responses:
  - Duplicate email → "This email is already registered"
  - Duplicate username → "Username already taken"
  - Weak password → Show password requirements
  - Passwords don't match → "Passwords do not match"
  - Invalid data → Show field-specific errors
```

### Login (/login/)
```
Method: GET → Display form
Method: POST → Process login

GET Response:
  - Template: login.html
  - Form: CustomAuthenticationForm
  - Fields:
    * Username or Email (required)
    * Password (required)

POST Processing:
  - Validate credentials
  - Create session
  - Redirect to homepage (/)
  - Show success message

Error Responses:
  - Invalid credentials → "Invalid username or password"
  - Invalid form → Show field errors
  - Account locked → "Too many failed attempts" (if implemented)
```

### Logout (/logout/)
```
Method: GET

Processing:
  - Destroy session
  - Clear authentication cookie
  - Redirect to homepage (/)
  - Show message: "You have been logged out successfully"
```

---

### Task List (/todos/)
```
Method: GET
Authentication: Required (login_required)
Template: todos_list.html

Context:
  - todos: User's tasks ordered by -created_at

Data Displayed:
  - User's tasks only
  - Priority badge with color
  - Status badge with color
  - Due date (if set)
  - Edit & Delete buttons
  - Filter buttons (All, Pending, In Progress, Completed, On Hold)

Features:
  - Filter by status
  - Edit task
  - Delete task
  - Create new task button
  - Empty state with helpful message

Redirect: If not authenticated → /login/?next=/todos/
```

### Create Task (/todos/create/)
```
Method: GET → Show form
Method: POST → Create task

GET Response:
  - Template: create_todo.html
  - Form: TodoForm
  - Fields:
    * Title (required, 1-200 chars)
    * Description (optional)
    * Priority (required: Low, Medium, High, Urgent)
    * Status (required: Pending, In Progress, Completed, On Hold)
    * Due Date (optional, datetime)

POST Processing:
  - Validate form
  - Create Todo instance
  - Set user to current user
  - Save to database
  - Redirect to /todos/
  - Show message: "Task created successfully!"

Error Responses:
  - Missing required fields → Show field-specific errors
  - Invalid priority/status → Show valid options
```

### Edit Task (/todos/<id>/edit/)
```
Method: GET → Show form
Method: POST → Update task

GET Response:
  - Template: edit_todo.html
  - Form: TodoForm (pre-filled with current data)
  - Validates: User ownership

POST Processing:
  - Validate form
  - Update Todo instance
  - Verify user ownership
  - Save to database
  - Redirect to /todos/
  - Show message: "Task updated successfully!"

Error Responses:
  - Task not found → 404 Not Found
  - Not owner → 403 Forbidden
  - Invalid data → Show field errors

URL Parameter:
  - <id>: Primary key of todo to edit
```

### Delete Task (/todos/<id>/delete/)
```
Method: GET → Show confirmation
Method: POST → Delete task

GET Response:
  - Template: delete_todo.html
  - Shows task details
  - Confirmation button

POST Processing:
  - Verify user ownership
  - Delete Todo from database
  - Redirect to /todos/
  - Show message: "Task deleted successfully!"

Error Responses:
  - Task not found → 404 Not Found
  - Not owner → 403 Forbidden

URL Parameter:
  - <id>: Primary key of todo to delete
```

---

### Suggest Feature (/features/suggest/)
```
Method: GET → Show form
Method: POST → Create suggestion

GET Response:
  - Template: suggest_feature.html
  - Form: SuggestedFeatureForm
  - Fields:
    * Title (required, 1-200 chars)
    * Description (required, 5+ chars)

POST Processing:
  - Validate form
  - Create SuggestedFeature instance
  - Set user to current user
  - Set votes to 1 (suggester's vote)
  - Save to database
  - Redirect to /features/
  - Show message: "Thank you! Your feature suggestion has been received"

Authentication:
  - Required (login_required)
  - Redirect: If not logged in → /login/?next=/features/suggest/

Error Responses:
  - Missing fields → Show field errors
  - Invalid characters → Sanitize input
```

---

### Add Feature (/features/add/)
```
Method: GET → Show form
Method: POST → Create feature

GET Response:
  - Template: createfeatures.html
  - Form: FeatureForm
  - Shows admin notice
  - Fields:
    * Title (required, 1-100 chars)
    * Description (required)
    * Icon (optional, emoji or icon name)
    * Order (required, number)
    * Active (checkbox)

POST Processing:
  - Verify staff/admin status
  - Validate form
  - Create Feature instance
  - Save to database
  - Redirect to /features/
  - Show message: "Feature added successfully!"

Authentication:
  - Requires: Staff status (is_staff)
  - Redirect: If not staff → Show error message

Error Responses:
  - Not staff → "You don't have permission to add features"
  - Invalid data → Show field errors
```

---

### Admin Panel (/admin/)
```
URL: http://127.0.0.1:8000/admin/

Main Page Features:
  - Manage Features
  - Manage Todos (all users)
  - Manage Suggested Features
  - Manage Users
  - Manage Groups
  - Manage Permissions

Authentication:
  - Requires: Superuser or staff with permissions
  - Default: admin / Rohan@9845

Feature Admin:
  - List display: Title, Status badge, Created at
  - Search: By title, description
  - Filter: By active status
  - Actions: Add, Edit, Delete
  - Sort: By order field

Todo Admin:
  - List display: Title, User, Priority badge, Status badge, Due date
  - Search: By title, description, username
  - Filter: By status, priority, user, date
  - Actions: Add, Edit, Delete

Suggested Feature Admin:
  - List display: Title, User, Votes, Approval badge
  - Search: By title, description, author
  - Filter: By approval status, votes, date
  - Actions: Add, Edit, Delete

User Admin:
  - List display: Username, Email, Name, Staff status
  - Search: By username, email
  - Filter: By staff status, superuser status, date joined
  - Actions: Add, Edit, Delete, Change password
```

---

## 🔍 URL PARAMETER REFERENCE

### Task ID (<id>)
```
Format: Integer (primary key)
Example: /todos/1/edit/
Valid Range: 1 to 2147483647
Error: If not found → 404 Not Found
```

---

## 📱 REDIRECT FLOW

### After Signup
```
/signup/ (POST) → Create user → /login/ → Redirect to /
```

### After Login
```
/login/ (POST) → Create session → / (homepage)
Or: /login/?next=/todos/ → /todos/
```

### After Task Creation
```
/todos/create/ (POST) → Create task → /todos/
```

### After Task Edit
```
/todos/<id>/edit/ (POST) → Update → /todos/
```

### After Task Delete
```
/todos/<id>/delete/ (POST) → Delete → /todos/
```

### After Feature Suggestion
```
/features/suggest/ (POST) → Create suggestion → /features/
```

### After Logout
```
/logout/ → Destroy session → /
```

---

## 🔐 AUTHENTICATION FLOW

```
1. User visits /signup/
   ↓
2. Fill form & submit (POST)
   ↓
3. Form validated
   ↓
4. User created in database
   ↓
5. Automatically logged in
   ↓
6. Session created
   ↓
7. Redirected to /
   ↓
8. Can now access /todos/, /features/suggest/, etc.
```

---

## 📊 RESPONSE STATUS CODES

| Code | Meaning | When |
|------|---------|------|
| 200 | OK | Page loads successfully |
| 301 | Moved | Permanent redirect |
| 302 | Found | Temporary redirect (after login) |
| 304 | Not Modified | Cached content |
| 400 | Bad Request | Invalid form data |
| 403 | Forbidden | Not authorized |
| 404 | Not Found | Page/resource doesn't exist |
| 405 | Not Allowed | Wrong HTTP method |
| 500 | Server Error | Django error |

---

## ✅ COMPLETE URL CHECKLIST

### Public URLs
- [x] / - Homepage
- [x] /about/ - About page
- [x] /features/ - Features page

### Auth URLs
- [x] /signup/ - Register
- [x] /login/ - Login
- [x] /logout/ - Logout

### User URLs
- [x] /todos/ - Task list
- [x] /todos/create/ - Create task
- [x] /todos/<id>/edit/ - Edit task
- [x] /todos/<id>/delete/ - Delete task
- [x] /features/suggest/ - Suggest feature

### Admin URLs
- [x] /admin/ - Admin panel
- [x] /features/add/ - Add feature

**Total: 13+ working URLs**

---

**Reference Version:** 1.0.0  
**Last Updated:** November 16, 2025  
**Status:** ✅ Complete & Tested
