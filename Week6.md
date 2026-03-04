
# MetroBlue Web Application – QA Testing Plan

### Project Overview

This repository documents the **functional QA testing plan** for the **MetroBlue Web Application**. The goal of this testing phase is to verify system stability, ensure role-based access control works correctly, and validate that all core modules behave as expected under normal and edge-case scenarios.

Testing follows a **black-box testing approach**, focusing on user-facing functionality without inspecting the internal codebase.

The testing process includes validation of authentication flows, role permissions, task management, financial modules, data integrity, and system responsiveness across browsers and devices.

**Application Under Test:**
MetroBlue Web Application
Staging Environment:
[https://metroblue.infodomain.com.ng/](https://metroblue.infodomain.com.ng/)

---

# Testing Team

### Team Lead

**Musrat**

Responsibilities:

* Coordinate the overall QA testing process
* Ensure bugs are documented in the approved format
* Review and consolidate testing reports
* Validate final findings before submission

### Team Members

**Thomas**

**Gabino**

Responsibilities:

* Execute assigned test scenarios
* Document bugs and provide screenshots or recordings
* Verify module functionality based on the testing checklist

---

# Testing Scope

The QA process covers the following major areas of the application:

* Authentication and account management
* Role-based access control
* Task management system
* Payment records module
* Expense tracking module
* User administration
* Form validation and input handling
* UI responsiveness and cross-browser compatibility
* Data integrity and persistence
* Reports, training records, projects, procurements, and sales pipelines

---

# Testing Methodology

Testing follows a **Functional QA (Black-Box) methodology**, where testers interact with the application as real users and verify:

* Correct functionality of system features
* Proper validation and error handling
* Correct role-based permissions
* Data persistence and accuracy
* UI responsiveness across browsers and devices

The following browsers are used during testing:

* Google Chrome
* Mozilla Firefox
* Microsoft Edge
* Safari

---

# Core Testing Modules

### Authentication & Account Flows

* Login validation for all six user roles
* Failed login scenarios
* Admin two-factor authentication
* Logout session validation
* Password reset workflow

### Role-Based Access Control

* UI visibility per role
* Restricted page access attempts
* Action permissions validation

### Task Management

* Task creation and editing
* Task checklists and attachments
* Task duplication
* Activity logs
* Task workflow transitions
* Task filtering and search

### Payments Module

* Payment record creation and editing
* CSV import and export
* Data validation checks
* Role-based restrictions

### Expenses Module

* Expense record creation and editing
* CSV import/export
* Data validation and boundary testing
* Role-based restrictions

### User Management

* User list and pagination
* User creation for each role
* User editing and role reassignment
* User activation and deactivation

### Forms & Input Validation

* Required field validation
* Maximum length validation
* Special character handling
* Date field validation
* Numeric field boundary testing
* Rich text editor validation

### UI & Responsiveness

* Cross-browser testing
* Mobile responsiveness
* Loading states
* Empty data states
* Error handling during network interruption
* Navigation and routing validation

### Data Integrity

* Record persistence validation
* Concurrent editing behavior
* Pagination accuracy
* Sorting and filtering verification
* Delete operations verification

### Reports, Training, Projects & Sales

* Intern and staff report generation
* CRUD operations for training records
* CRUD operations for projects
* Procurement record management
* Sales and leads pipeline validation

---

# Bug Reporting Standard

All identified issues must follow the standard bug reporting format below.

| Field              | Description                        |
| ------------------ | ---------------------------------- |
| Title              | Short summary of the bug           |
| Role Tested        | User role used during testing      |
| Steps to Reproduce | Steps required to trigger the bug  |
| Expected Result    | Correct expected system behavior   |
| Actual Result      | Observed system behavior           |
| Screenshot / Video | Evidence of the issue              |
| Severity           | Blocker / Major / Minor / Cosmetic |
| Browser / Device   | Environment where bug occurred     |
