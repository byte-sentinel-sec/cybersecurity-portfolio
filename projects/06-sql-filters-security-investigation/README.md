# 6. Apply Filters to SQL Queries

**Skills:** MariaDB / SQL · `AND` · `OR` · `NOT` · `LIKE` · log analysis

## Overview
Investigated a potential security incident by filtering the organization's login logs and employee records.

## Queries

### 1. After-hours failed login attempts
```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00' AND success = FALSE;
```
Isolates failed logins after business hours (possible insider threat or brute-force).

### 2. Login attempts on specific dates (May 8–9, 2022)
```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';
```
Expands the window to the day before a confirmed anomaly to look for reconnaissance.

### 3. Login attempts outside of Mexico
```sql
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';
```
Mexico appears as both `MEX` and `MEXICO`, so the `%` wildcard catches both variants.

### 4. Marketing employees in the East building
```sql
SELECT *
FROM employees
WHERE department = 'Marketing' AND office LIKE 'East%';
```

### 5. Employees in Finance or Sales
```sql
SELECT *
FROM employees
WHERE department = 'Finance' OR department = 'Sales';
```

### 6. All employees not in IT
```sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```
Used to find staff who still needed a critical security patch.

## Takeaway
Precise filtering reduces noise in large datasets, helping surface unusual login timing and geography and segment assets for remediation.

📄 [Original report with screenshots](original-report.pdf)
