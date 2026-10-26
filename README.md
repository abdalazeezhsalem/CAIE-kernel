# Django Blog Application - Data Models & Migrations

A Django-based blog application extended with core database models for managing users, categories, and post comments.

---

## Overview

This module extends the existing Django Blog platform by introducing the foundational ORM models required for user management, post classification, and reader interaction, adhering to clean architectural conventions and constraints.

---

## Implemented Models

### 1. User Model (`User`)
Represents the blog users and authors.
* **`username`**: Unique string identifier
* **`email`**: Unique user email address 
* **`first_name`**: Optional user first name 
* **`last_name`**: Optional user last name 
* **`created_at`**: Timestamp auto-generated at model creation
* **String Representation**: Returns the `username`.

### 2. Category Model (`Category`)
Organizes blog posts into distinct topics.
* **`name`**: Unique category name 
* **`description`**: Detailed overview of the category
* **`created_at`**: Creation timestamp 
* **String Representation**: Returns the category `name`.

### 3. Comment Model (`Comment`)
* **`content`**: Full body text of the comment 
* **`created_at`**: Timestamp logged on initial creation 
* **`updated_at`**: Timestamp automatically refreshed on every update 
* **String Representation**: Returns a concise snippet of the comment content.

> **Note:** models are currently decoupled without direct relational fields (`ForeignKey` / `ManyToManyField`).

---

Technical Stack
Framework: Django 5.x

Language: Python 3.11+

Database: PostgreSQL 

Version Control: Git & GitHub

   
