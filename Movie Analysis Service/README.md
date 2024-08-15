# Movie Analysis Service

## Project structure

- /src : Contains source code
- abstract: Service API abstract class
- model: Entity models definition like a JPA (java).
- service: Service layer, handles the business logic.
- config: Enums and types definitions.
- movieAnalytics.py: Central API to serve API endpoints exposed to downstream clients.
- test.py: Test cases

Refinement of SOLID Principles:
Single Responsibility: Each class has one responsibility.
Open/Closed: Classes are open for extension but closed for modification.
Liskov Substitution: Subclasses or implementations can replace base classes without affecting the system's behavior.
Interface Segregation: Clients should not be forced to depend on interfaces they do not use.
Dependency Inversion: High-level modules should not depend on low-level modules. Both should depend on abstractions.
