# AI-Powered WhatsApp Chatbot for Enhancing Student Support

## Overview
This project implements a modular and scalable system to enhance student support services via WhatsApp integration. It combines AI (NLP engine) and structured academic data services with robust ticketing, payment, and alert mechanisms.

## Structure
The system is built around core components:
- **Academic Support** (CourseMaterial, AcademicDatabase)
- **Student Services** (SupportTicket, PaymentTransaction)
- **Communication** (WhatsAppIntegration, NLPEngine)
- **Alerts and Monitoring** (DistressAlert)
- **Administration** (Administrator)

Design patterns were used heavily to ensure flexibility, maintainability, and scalability.

---

## Design Choices
| Decision Area         | Choice |
|:----------------------|:-------|
| **Encapsulation**      | All classes use private fields (`__var`) and controlled access via getters/setters or properties. |
| **Resilience**         | Retrying mechanisms (e.g., WhatsApp sending retries) and SLA violation checks. |
| **Domain-driven**      | Core objects (e.g., SupportTicket, DistressAlert) closely match real-world concepts for clarity. |
| **Extensibility**      | Modular classes prepared for extension (e.g., adding more payment methods, integrating new NLP models). |
| **Testing-first**      | Unit tests written to validate object creation and behaviour under different scenarios. |
| **Error Handling**     | Basic error catching simulated in methods where needed (e.g., `send_message` retries on failure). |
| **Logging and Monitoring** | Basic logging through print statements and internal logs. |

---

## Creational Patterns Implemented

| Pattern               | Why It Was Used |
|:----------------------|:----------------|
| **Singleton**          | Ensures a single point of access for the `AcademicDatabase` (e.g., data consistency). |
| **Simple Factory**     | Centralised creation of common domain objects like `SupportTicket` or `PaymentTransaction`. |
| **Factory Method**     | Specialised object creation based on type (e.g., distress alerts for different severity levels). |
| **Abstract Factory**   | Family of related objects — for instance, different kinds of communication handlers could be introduced later. |
| **Builder**            | Flexible construction of complex objects (e.g., assembling a full `SupportTicket` with optional fields). |
| **Prototype**          | Enables fast cloning of complex objects like `CourseMaterial` for versioning or rollback purposes. |

---

## Testing Strategy
- Unit tests created for all creational patterns.
- Focused on validating:
  - Correct object creation
  - Pattern behaviour under typical and edge cases
  - State after operations (e.g., publishing a CourseMaterial or reconciling a PaymentTransaction)

---


## Future Improvements
- Integrate real WhatsApp API (currently simulated).
- Implement real NLP models.
- Expand support ticket categories and escalation paths.
- UI dashboard for administrators.
- Database backend instead of in-memory simulation.

---
