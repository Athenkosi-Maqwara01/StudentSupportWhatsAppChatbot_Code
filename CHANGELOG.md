# 📜 CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

- Ongoing testing and minor refactoring.

---

### ✨ Added

- Implemented **Simple Factory** pattern to create `PaymentTransaction` and `SupportTicket` instances dynamically.
- Implemented **Factory Method** for flexible creation of `SupportTicket` based on priority and category.
- Implemented **Abstract Factory** for grouped creation of different chatbot components (`NLPEngine`, `WhatsAppIntegration`).
- Implemented **Builder** pattern for structured construction of complex `SupportTicket` and `PaymentTransaction` objects.
- Implemented **Prototype** pattern for cloning `DistressAlert` and `SupportTicket` instances.
- Implemented **Singleton** pattern for `AcademicDatabase` connection class.

### 🧪 Tests

- Added **unit tests** for:
  - Simple Factory creation
  - Factory Method specialisation
  - Abstract Factory component sets
  - Builder correct object construction
  - Prototype deep cloning verification
  - Singleton instance uniqueness enforcement

### 🛠 Improvements

- Enhanced `WhatsAppIntegration` to include better exception handling and retry logic.
- Updated `Administrator` class — created issues for method implementation.

---

## [Planned for Next Release]

- Full implementation of `Administrator` class methods.
- Exception logging and handling improvements across all classes.
- Extend NLP processing logic for better intent and entity extraction.
- Database syncing improvements for `AcademicDatabase`.

---

## [Repository Management]

- Moved completed tasks (e.g., "Implement Singleton") to **Done** column in GitHub Project Board.
- Created issues for discovered improvements and bugs.
- Linked commits to issues following `Fix #issue_number` commit convention.

---

# 📌 Versioning

This project adheres to **Semantic Versioning** (`MAJOR.MINOR.PATCH`).

