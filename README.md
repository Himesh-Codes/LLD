# LLD (JAVA)

## References

https://github.com/ashishps1/awesome-low-level-design?tab=readme-ov-file

How to answer a LLD question? (https://blog.algomaster.io/p/how-to-answer-a-lld-interview-problem)

- Step 1: Clarify Requirements

  The first step in a LLD interview is to understand the requirements and use-cases.

  Start by asking questions to understand what's required:

        - Core features

        - Specific features we should prioritize?

        - Primary users of this system?

        - Actions can users take?

        - Specific constraints or limitations?

        - Need to handle concurrency?

        - Need to handle errors, edge cases, exceptions, and unexpected input?

- Step 2: Identify Entities

  Break down the problem and identify the core entities or objects.

  Core entities are the key objects or concepts around which your system is built.

  These entities will become the classes in your object-oriented design. Think of them as the nouns in the problem description.
  For eg: Stack Overflow, different entities we can have are:

        - User: Represent a person who interact with system.
        - Question: Question posted by user.
        - Answer
        - Comment: Comment on a question or answer.
        - Tag: The tag that can be applied to a question.
        - Vote: The vote on a question.

- Step 3: Class Design
  Design the classes, enums and interfaces that will represent the entities in your system.

  - 3.1 Define classes and relationships

    Translate entities into classes and class attributes.

    `You can draw a UML class diagram to illustrate the relationships between classes.`

    If your design consists of multiple classes, figure out how would they would relate with each other.

  - 3.2 Define interfaces and core methods
    Define interfaces and core methods in each of the classes.

    These methods encapsulate the actions or behaviors that each class is responsible for.

    Here are the interface/core method for Stack Overflow classes:

        - Commentable: Defines the contract for objects that can receive comments (eg. Question, Answer)
            - addComment(comment): Adds a comment to this object.
            - getComments(): Retrieves all comments for this object.

        - Votable: Defines the contract for objects that can be voted on.
            - vote(): Registers a vote on this object.

            - getVoteCount(): Retrieves the total vote count for this object.

    Core methods:

            - User Class:
                - Setter/Getters for variables
                - askQuestion(title, content, tags): Creates a new question asked by this user.
                - answerQuestion(question, content)
                - addComment(commentable, comment)
                - updateReputation(value)

            - Question Class:
                - Setter/Getters for variables
                - addAnswer(answer)
                - addComment(comment)
                - vote(user, value)
                - addTag(user, value)

            - Answer Class:
                - Setter/Getters for variables
                - addComment(comment)
                - vote(user, value)
                - markAsAccepted()

  - 3.3 Define a central class
    We don’t want to manipulate classes in our design directly from outside, that’s why we need a central class that provides a unified interface for interacting with the system.

    This simplifies the API and makes it easier to use and understand the system as a whole.
    For example Stack Overflow design, we can create a class called StackOverflow;
    Here are some of it’s key responsibilities:

        1. User management (Call user class and methods from central class)
        2. Question and Answer management. (Call question/answer class and methods from central class)
        3. Voting and commenting operations, (Call vote/commenting class and methods from central class)
        4. Searching and data retrieval. (Uses a common class for these operation in in-memory is used)
        5. Maintaining data consistency across system (We can use the single entry point using central class)

    We can have following core methods in the StackOverflow class:
    (https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/stack-overflow.md)

        - createUser(username, email)
        - askQuestion(user, title, content, tags)
        - answerQuestion(user, question, content)
        - addComment(user, commentable, content)
        - voteQuestion(user, question, value)
        - voteAnswer(user, answer, value)
        - acceptAnswer(answer)
        - searchQuestions(query)
        - getQuestionsByUser(user)

- Step 4: Implementation

  - 4.1 Follow good coding practices
    We should try your best to follow good coding principles like:

    - meaningful names for classes, methods, and variables.
    - simplicity and readability.
    - composition over inheritance to promote flexibility and avoid tight coupling.
    - Avoid duplicating code or logic.
    - Use interfaces to define contracts and enable loose coupling between components
    - Only implement what is required.
    - Strive for modularity and separation of concerns to make the codebase maintainable and scalable.
    - Apply design principles and design patterns wherever necessary.
    - Make your code scalable, performs well with large data sets.

  - 4.2 Implement necessary methods
    Check with the interviewer to understand which methods are important for the interview.

  - 4.3 Address concurrency
    Check with the interviewer if you need to handle concurrency in the design.

    Here are few strategies to address concurrency:

    - Use synchronization mechanisms to ensure that only one thread can access a shared resource at a time.
    - Use atomic operations that are guaranteed to be executed as a single, indivisible unit.
    - Use immutable objects wherever possible to eliminate the risk of concurrent modifications.
    - Use thread-safe data structures that handle synchronization internally.

    For Stack Overflow example;

    - Voting System: Implement atomic operations for vote counts to prevent race conditions.
    - Comment System: Use a thread-safe data structure for storing and retrieving comments.
    - User Reputation: Use synchronization when updating user reputation to ensure consistency.

- Step 5: Exception Handling
  The problem may require you to handle errors, edge cases, exceptions, and unexpected input.

  For the Stack Overflow example,

  - What if a user tries to vote on their own question/answer?
  - What is a user tries to vote multiple times on the same content?
  - What if a user posts a question with empty title or content?
  - Can the user reputation go negative?

Final Note: Feel free to skip some of these due to limited time in interviews.
It’s always a good idea to check with the interviewer on what all is expected from the design.

- https://github.com/ashishps1/awesome-low-level-design

## References

- SOLID (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion (High level module not depend on low level module)) Principle Concept: https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898
- SOLID Code Explainations : https://blog.algomaster.io/p/solid-principles-explained-with-code
- DRY (Don't Repeat Yourself - Avoid duplication of logic/code): Steps:- Identify Repetitive Code, Extract Common Functionality, Use Inheritance and Composition, Leverage Libraries and Frameworks, Refactor Regularly(it's an ongoing process) https://blog.algomaster.io/p/082450d8-0e7b-4447-a8dc-b7308e45f048
- YAGNI (You are'nt gonna need it: Implement only whatever need now not on forseen items): https://blog.algomaster.io/p/8c3c7da7-885b-4a9c-a6e4-70ee02de4772
- KISS (Keep it simple stupid: Avoid over engineering, leverage on whatever exist, inbuit library, etc..): https://blog.algomaster.io/p/21b57678-b351-4ed4-b390-3b6308af2f7d

## Common Design Patterns

![design cheat sheet 1](./Design%20Patterns/images/Design%20cheat%20sheet%201.png)

![design cheat sheet 2](./Design%20Patterns/images/design%20cheat%20sheet%202.png)

### Creational Patterns

#### Singleton (https://blog.algomaster.io/p/singleton-design-pattern): Class to have only one object created,achieved by making the constructor private to avoid other classes creates it's object and providing a static method for external objects to access it.

Let’s understand how this Pattern will created:
4.1. Static Member: This static member ensures that memory is allocated only once, preserving the single instance of the Singleton class.
4.2. Private Constructor: The Singleton pattern or pattern singleton incorporates a private constructor. This ensures that the class has control over its instantiation process.
4.3. Static Factory Method: When someone requests an instance, this method either creates a new instance (if none exists) or returns the existing instance to the caller.

Singleton is useful in scenarios like:
Managing Shared Resources (database connections, thread pools, caches, configuration settings)
Coordinating System-Wide Actions (logging, print spoolers, file managers)
Managing State (user session, application state)

Note: Consider alternative approaches like dependency injection when possible to promote loose coupling and testability.

[Code](./Design%20Patterns/singleton.java)

#### Factory (https://refactoring.guru/design-patterns/factory-method): The subclasses can create an object of one class with help of a factory class, Factory Method Pattern says that just define an interface or abstract class for creating an object but let the subclasses decide which class to instantiate, with providing the type.

https://www.javatpoint.com/factory-method-design-pattern

Let’s understand how this Pattern will created:

1. Creator Interface (Factory Interface): The creator typically contains a method that serves as a factory for creating objects. It may also contain other methods that work with the created objects.
2. Concrete Creators (Concrete Factories): Concrete Creator classes are subclasses of the Creator that implement the factory method to create specific types of objects.
3. Product Interface: This is the interface or abstract class for the objects that the factory method creates. The Product defines the common interface for all objects that the factory method can create.
4. Concrete Products: Concrete Product classes are the actual objects that the factory method creates. Each Concrete Product class implements the Product interface or extends the Product abstract class.

Factory Design Pattern Useful scenarios:

- By the way factory if the factory have multiple products and creation of product involves multiple
  other object creation we can use Factory Design Pattern avoiding the decoupling on object creations.
- Document Creation Software: In applications like Microsoft Word or Google Docs, you can create different types of documents
- Payment Processing Systems: In e-commerce platforms, you might need to handle various payment methods (credit card, PayPal, cryptocurrency)
- Vehicle Manufacturing: In an automobile factory, different types of vehicles (cars, trucks, motorcycles) need to be produced.
- Database Connections: In an application that needs to connect to different databases (MySQL, PostgreSQL, SQLite)
- Report Generation: In a business application, different types of reports (financial reports, sales reports, inventory reports) need to be generate
- Logging Frameworks: In software that requires logging, different logging mechanisms (console logging, file logging, database logging) can be used.

Usage of Factory Design Pattern:
When a class doesn't know what sub-classes will be required to create
When a class wants that its sub-classes specify the objects to be created.
When the parent classes choose the creation of objects to its sub-classes.

#### Abstract Factory (https://refactoring.guru/design-patterns/abstract-factory): Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes. It is a way of organizing how you create groups of things that are related to each other. It provides a set of rules or instructions that let you create different types of things without knowing exactly what those things are.

https://www.geeksforgeeks.org/abstract-factory-pattern/

Let’s understand how this Pattern will created:

- Abstract Factory Interface (CarFactory): Defines methods for creating cars and their specifications. Abstract Factory serves as a high-level blueprint that defines a set of rules for creating families of related objects. It declares a series of methods, each responsible for creating a particular type of object and ensures that concrete factories adhere to a common interface,
- Concrete Factories (NorthAmericaCarFactory and EuropeCarFactory): Implement the abstract factory interface to create cars and specifications specific to North America, Europe. It contain the logic for creating specific instances of objects within a family.
- Abstract Products (Car and CarSpecification interfaces): Define interfaces for cars and specifications to ensure a common structure. It acts as an abstract or interface type that all concrete products within a family must adhere to and provides a unified way for concrete products to be used interchangeably.
- Concrete Products (Sedan, Hatchback, NorthAmericaSpecification, EuropeSpecification): Implement the interfaces to create specific instances of cars and specifications. They are the actual instances of objects created by concrete factories.
- Client: Client enjoys the flexibility of seamlessly switching between families of objects by changing the concrete factory instance.

When to use Abstract Factory Pattern:

- Multiple families of related products
- Flexibility and extensibility: If you need to allow for variations or extensions in the products or their families
- Encapsulation of creation logic
- Consistency across product families: If you want to enforce consistency among the products created by different factories.

Abstract Factory Pattern Useful scenarios:

- Document Generation Systems: A system that generates different types of documents (PDF, HTML, Word) based on user requirements.
- Mutiple Country Spec Vehicle Manufacturing: An automobile company producing different types of vehicles (cars, trucks, motorcycles) with different components (engines, tires, seats), have multiple variations for each vehicle with country wise (Europe, NorthAmerica, India etc..).
- Database Connection Libraries: A system that needs to support different types of databases (MySQL, PostgreSQL, SQLite).

#### Builder (https://refactoring.guru/design-patterns/builder): Builder is a creational design pattern that lets you construct complex objects step by step, where the construction process can vary based on the type of product being built. The pattern allows you to produce different types and representations of an object using the same construction code.

https://www.geeksforgeeks.org/builder-design-pattern/

Let’s understand how this Pattern will created:

- Product (Computer): The Product is the complex object that the Builder pattern is responsible for constructing.
- Builder: The Builder is an interface or an abstract class that declares the construction steps for building a complex object.
- ConcreteBuilder: ConcreteBuilder classes implement the Builder interface, providing specific implementations for building each part of the product.
- Director: The Director is responsible for managing the construction process of the complex object.
  It collaborates with a Builder, but it doesn’t know the specific details about how each part of the object is constructed.
- Client: The Client is the code that initiates the construction of the complex object.

Builder Pattern Useful scenarios:

- By the name suggest we have Product, we can give multiple specification models, let's say Buidling as example, Contompary, Tropical, Tropical Comtompary are options of product, if a builder is dedicated for multiple styles of proudct spcefication and custruct product. We can have a Director which is calling respective builder and get the product build, gives an option to add other builders (other styles).
- Building a House: A house can have many optional features (garage, swimming pool, garden, multiple floors).
- Creating a Meal: A meal can have multiple parts (main course, side dish, drink, dessert).
- Constructing a Computer: A computer has various components (CPU, RAM, storage, GPU, power supply).
- Constructing a Vacation Package: A vacation package includes flight, hotel, car rental, and activities.

When to use Builder Pattern:

- Complex Object Construction: When you have an object with many optional components or configurations
- Step-by-Step Construction
- Avoiding constructors with multiple parameters
- Immutable Objects: When you want to create immutable objects, and the Builder pattern allows you to construct the object gradually before making it immutable.
- Configurable Object Creation
- Common Interface for Multiple Representations: When you want to provide a common interface for constructing different representations of an object.

#### Prototype pattern (https://refactoring.guru/design-patterns/prototype): Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their classes. The Prototype pattern delegates the cloning process to the actual objects that are being cloned. The pattern declares a common interface for all objects that support cloning. This interface lets you clone an object without coupling your code to the class of that object.

Let’s understand how Prototype Design Pattern will created:

- Prototype Interface (Shape): We define an interface called Shape that acts as the prototype.It declares two methods: clone() for making a copy of itself and draw() for drawing the shape.
- Concrete Prototype (Circle): We implement the Shape interface with a concrete class Circle. The Circle class has a private field color and a constructor to set the color when creating a circle. It implements the clone() method to create a copy of itself (a new Circle with the same color).
- Client (ShapeClient): We create a client class, ShapeClient, which will use the prototype to create new shapes. The client has a field shapePrototype representing the prototype it will use. The constructor takes a Shape prototype, and there’s a method createShape() that creates a new shape using the prototype’s clone() method.

`It is basically create an object of any Prototype and use that object reference to call client which have implementation to call clone method of given Prototype concrete class, which will return a new clone of Prototype. `

Useful scenarios:

- Web Application Templates: You can create a prototype of a generic page template and then clone and customize it for different content types. This avoids duplicating code and allows for consistent behavior across different pages.
- Document Management Systems: A prototype of a generic document structure can be created, and then specific documents are cloned and customized based on this prototype. This reduces the need to create each document from scratch.
- Game Development: A prototype of a game character (e.g., a generic enemy type) can be created, and then specific characters are cloned and customized with different stats, abilities, and appearances.
- User Interface Design
- Configuration Management: A prototype configuration can be created for the most common settings, and then specific configurations are cloned and modified accordingly.
- Financial Software Systems: A prototype of a financial instrument can be created, and then specific instruments are cloned and customized with different parameters like interest rates, maturities, and credit ratings.
- E-commerce Product Customization: A prototype product can be created, and then different product variants are cloned and customized based on customer selections.
- Healthcare Systems: A prototype of a medical form or patient record can be created, and then clones are customized based on specific patient needs or medical conditions.
- Content Generation for Marketing
- Automation in Manufacturing: A prototype of a product design can be created, and then customized versions are cloned for different production lines.

When to use this Pattern:
https://www.geeksforgeeks.org/prototype-design-pattern/

- Creating Objects is Costly: If object creation involves significant resources, such as database or network calls, and you have a similar object available, cloning can be more efficient.
- Variations of Objects: Instead of creating multiple classes for each variation, you can create prototypes and clone them with modifications.
- Dynamic Configuration: You can prototype a base configuration and clone it, adjusting the properties as needed.
- Reducing Initialization Overhead: Creating a clone can be faster than creating an object from scratch, especially when the initialization process is resource-intensive.

### Structural Patterns

#### Adapter (https://refactoring.guru/design-patterns/adapter): Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.

Let’s understand how this Pattern will created:

- Target Interface (Printer) : The interface that the client code expects.
- Adaptee (LegacyPrinter): The existing class with an incompatible interface.
- Adapter (PrinterAdapter): The class that adapts the LegacyPrinter to the Printer interface.
- Client Code: The code that interacts with the Printer interface.

Useful scenarios:

- Integrating Legacy Systems with Modern Applications: Create an adapter that wraps the legacy system’s API and converts its methods into the new system’s expected format.
- Working with Third-Party Libraries: Create an adapter that sits between your application and the third-party library, translating calls from your application to the library and vice versa.
- Cross-Platform Mobile Applications: Implement platform-specific adapters that translate a common interface into the appropriate API calls for each platform.
- Database Access Layer: Create an adapter that provides a consistent interface for database operations, regardless of the underlying database system.
- API Gateway in Microservices Architecture: An API Gateway can act as an adapter, translating client requests into the appropriate service-specific API calls.
- Middleware Integration: Create an adapter that converts your application’s data format into the format required by the middleware or ESB.
- Message Queue Systems: Create an adapter that standardizes the message queue operations, allowing your application to interact with different systems through a unified interface.
- Payment Gateway Integration: An adapter can be created for each payment gateway, providing a consistent payment processing interface across the platform.
- Data Conversion Utilities: Your application needs to work with different data formats (e.g., JSON, XML, CSV) but expects data in a consistent format.
- Internationalization and Localization: Create an adapter that provides a uniform interface for localization, hiding the differences between various localization libraries.

When to use this Pattern:

- Integration of Existing Code: When you have existing code or components with interfaces that are incompatible with the interfaces expected by new code or systems.
- Reuse of Existing Functionality: When you want to reuse classes or components that provide valuable functionality but don’t conform to the desired interface. The Adapter pattern enables you to reuse existing code by creating an adapter that makes it compatible.
- Interoperability: The Adapter pattern acts as a bridge, allowing systems with incompatible interfaces to collaborate effectively and operate toghether.
- Client-Server Communication: Adapters help in translating requests and responses between client and server, ensuring smooth communication despite interface differences.
- Third-Party Library Integration: Adapters make it possible to use external components by providing a compatible interface for the rest of the application.

#### Facade (https://refactoring.guru/design-patterns/facade): Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes. Imagine a building, the facade is the outer wall that people see, but behind it is a complex network of wires, pipes, and other systems that make the building function. The facade pattern is like that outer wall. It hides the complexity of the underlying system and provides a simple interface that clients can use to interact with the system.

https://www.geeksforgeeks.org/facade-design-pattern-introduction/

Let’s understand how Prototype Design Pattern will created:

Facade (Compiler) : Facade knows which subsystem classes are responsible for a request. It delegate client requests to appropriate subsystem objects.

- Subsystem classes (Scanner, Parser, ProgramNode, etc.) : It implement subsystem functionality. It handle work assigned by the Facade object. It have no knowledge of the facade; that is, they keep no references to it.

- Facade Method Design Pattern collaborate in different way
  Client communicate with the subsystem by sending requests to Facade, which forwards them to the appropriate subsystem objects.
  The Facade may have to do work of its own to translate it inheritance to subsystem interface.
  Clients that use the Facade don’t have to access its subsystem objects directly.

Useful scenarios:

- Enterprise Resource Planning (ERP) Systems : A facade can be created to provide a simplified interface for common operations that require interaction with multiple modules, such as generating a financial report that pulls data from finance, inventory, and sales.
- E-commerce Platforms : A facade can be created to manage the entire order processing workflow, providing a single method to place an order, which then handles payment, inventory check, order creation, and shipping arrangements.
- Home Automation Systems : A facade can provide a unified interface for common scenarios like "turn on all lights" or "set home to vacation mode," which would internally call the appropriate methods for each device.
- Microservices Architecture : A facade can provide a unified API that aggregates calls to multiple microservices, simplifying the interaction for the client.
- Customer Relationship Management (CRM) Systems : A facade can simplify the management of customer data by providing a unified interface for tasks like getCustomerOverview() or updateCustomerRecord(), which might involve interaction with multiple CRM modules.
- Video Game Development : A facade can provide a simplified interface for common game operations like startGame(), loadLevel(), or playSoundEffect(), which internally manage the interactions with the various subsystems.
- Banking Systems : A facade can provide a simplified interface for customer-facing operations like transferFunds() or applyForLoan(), coordinating the necessary backend interactions.
- Hotel Management Systems : Facade can provide a simplified interface for hotel staff, such as checkInGuest() or processPayment(), which would internally coordinate with the necessary subsystems.
- Healthcare Management Systems : A facade can provide a unified interface for healthcare providers, such as registerPatient() or scheduleAppointment(), coordinating the necessary operations across subsystems.

When to use this Pattern:

- A Facade provide a simple default view of the subsystem that is good enough for most clients. Only clients needing more customizability will need to look beyond the facade.
- There are many dependencies between clients and the implementation classes of an abstraction.
- A Facade to decouple the subsystem from clients and other subsystems, thereby promoting subsystem independence and portability.
- Facade define an entry point to each subsystem level. If subsystem are dependent, then you can simplify the dependencies between them by making them communicate with each other solely through their facades.

#### Decorator (https://refactoring.guru/design-patterns/decorator): Decorator is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors, dynamically without altering their structure.

Let’s understand how Prototype Design Pattern will created:
https://www.geeksforgeeks.org/decorator-design-pattern-in-java-with-example/

- Component Interface (Pizza): An interface or abstract class that defines the core functionality. This is the base type for both concrete components and decorators.
- Concrete Component (PlainPizza): A class that implements the Component interface and provides the basic behavior.
- Abstract Decorator (PizzaDecorator): An abstract class that implements the Component interface and has a reference to a Component object. This class defines the interface for the decorators and includes a reference to a Component instance.
- Concrete Decorators (CheeseDecorator, PepperoniDecorator, MushroomDecorator, OliveDecorator): Classes that extend the Decorator class and add additional behavior to the Component.
- Client Code (PizzaShop): Implements the whole unit in single place as an entry point to client.

Useful scenarios:

- Text Processing Applications: Use decorators to wrap text objects with different formatting styles. Each decorator adds a specific formatting behavior.
- Logging in Software Applications : Use decorators to dynamically add different logging behaviors to a base logger.
- E-commerce Platforms – Product Pricing : Use decorators to wrap product pricing objects and apply different price modifications.
- Data Encryption and Compression : Use decorators to wrap data objects and apply encryption, compression, or other data processing steps.
- Web Application Middleware : Use decorators to wrap HTTP request and response objects to add middleware functionalities.
- Payment Processing Systems : Use the Decorator pattern to wrap the payment processing object with additional processing behaviors like fraud detection or currency conversion.
- Email Systems : Use decorators to wrap the email object with additional features like encryption or compression, allowing these features to be applied dynamically.

When to use this Pattern:

- Dynamic Behavior Addition: You need to dynamically add or modify the behavior of an object at runtime. Adding various toppings to a pizza in a pizza shop application, where toppings can be added or removed based on user preferences.
- Avoiding Subclass Explosion: You have a large number of combinations of functionalities that would otherwise lead to a combinatorial explosion of subclasses.
- Enhancing or Extending Functionality: You want to extend the functionality of a class without modifying its existing code. Adding logging, caching, or encryption features to a method call without altering the core logic of the method.
- Maintaining Open/Closed Principle: You want your classes to be open for extension but closed for modification.
- Reusable and Composable Functionality: You need to create reusable and composable functionality that can be applied to different objects.

#### Composite (https://refactoring.guru/design-patterns/composite): Composite is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects. The Composite Design Pattern was created to address specific challenges related to the representation and manipulation of hierarchical structures in a uniform way.

For example, imagine that you have two types of objects: Products and Boxes. A Box can contain several Products as well as a number of smaller Boxes. These little Boxes can also hold some Products or even smaller Boxes, and so on.
Say you decide to create an ordering system that uses these classes. Orders could contain simple products without any wrapping, as well as boxes stuffed with products...and other boxes. How would you determine the total price of such an order?
The Composite pattern suggests that you work with Products and Boxes through a common interface which declares a method for calculating the total price.

How would this method work? For a product, it’d simply return the product’s price. For a box, it’d go over each item the box contains, ask its price and then return a total for this box.

Let’s understand how Prototype Design Pattern will created:

https://www.geeksforgeeks.org/composite-design-pattern-in-java/

1. Task (Component): The component declares the interface for objects in the composition and for accessing and managing its child components. This is like a blueprint that tells us what both individual items (leaves) and groups of items (composites) should be able to do.
   Represents the common interface for both simple tasks and task lists.
   Defines methods such as getTitle(), setTitle(), and display().
2. SimpleTask (Leaf): Leaf defines behavior for primitive objects in the composition. This is the basic building block of the composition, representing individual objects that don’t have any child components.
   Represents an individual task with a title.
   Implements the Task interface.

3. TaskList (Composite): Composite stores child components and implements child-related operations in the component interface. This is a class that has child components, which can be either leaf elements or other composites.
   Represents a collection of tasks, which can include both simple tasks and other task lists.
   Implements the Task interface but also has a list of tasks (List<Task>).
   Defines methods to add, remove, and display tasks.

4. TaskManagementApp (Client): The client manipulates the objects in the composition through the component interface. The client uses the component class interface to interact with objects in the composition structure.
   Represents the application that uses the Composite Design Pattern to manage tasks.
   It creates a mix of simple tasks and task lists, showcasing how the Composite pattern allows treating both individual tasks and task collections uniformly.

Useful scenarios:

- File System Management: Both File and Directory implement a common interface (e.g., FileSystemComponent). A Directory can contain both File and other Directory objects, allowing you to perform operations like "delete," "copy," or "move" uniformly across both files and directories.
- Graphic Drawing Applications : Simple shapes like Line, Rectangle, and Circle implement a common interface or abstract class (e.g., Graphic). A CompositeGraphic can contain multiple Graphic objects, allowing you to treat simple shapes and groups of shapes uniformly.
- Company Organizational Structures : Both Employee and Manager implement a common interface (e.g., CompanyComponent). A Manager can contain other CompanyComponent objects, allowing you to treat individual employees and departments uniformly.
- Menu Systems: Both MenuItem and SubMenu implement a common interface (e.g., MenuComponent). A SubMenu can contain other MenuComponent objects, allowing you to handle operations like "display" or "select" uniformly.
- Product Configurators : Both Component and CompositeComponent implement a common interface (e.g., ProductComponent). A CompositeComponent can contain other ProductComponent objects, allowing you to handle the configuration process uniformly.
- E-commerce Cart Systems : Both CartItem and ItemBundle implement a common interface (e.g., CartComponent). An ItemBundle can contain multiple CartComponent objects, allowing you to calculate the total price or apply discounts uniformly.

When to use this Pattern:

- Uniform Interface:
  The Composite Pattern provides a uniform interface for both individual objects and compositions.
  This uniformity simplifies client code, making it more intuitive and reducing the need for conditional statements to differentiate between different types of objects.
- Hierarchical Structures:
  The primary focus of the Composite Pattern is to deal with hierarchical structures where objects can be composed of other objects.
- Flexibility and Scalability:
  The Composite Pattern allows for dynamic composition of objects, enabling the creation of complex structures.
- Common Operations:
  By defining common operations at the component level, the Composite Pattern reduces code duplication and promotes a consistent approach to handling both leaf and composite objects.
- Client Simplification:
  The Composite Pattern simplifies client code by providing a unified way to interact with individual and composite objects.

### Behavioral Patterns

#### Strategy Pattern (https://refactoring.guru/design-patterns/strategy): The Strategy Design Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable, allowing clients to switch algorithms dynamically without altering the code structure.

Imagine you’re planning a trip to a new city, and you have several options for getting there: by car, by train, or by plane. Each mode of transportation offers its own set of advantages and disadvantages, depending on factors such as cost, travel time, and convenience.

Context: You, as the traveler, represent the context in this analogy. You have a specific goal (reaching the new city) and need to choose the best transportation strategy to achieve it.
Strategies: The different modes of transportation (car, train, plane) represent the strategies in this analogy. Each strategy (mode of transportation) offers a different approach to reaching your destination.

Let’s understand how Strategy Design Pattern will created:

https://www.geeksforgeeks.org/strategy-pattern-set-1/

1. Context(SortingContext): The Context is a class or object that holds a reference to a strategy object and delegates the task to it. It acts as the interface between the client and the strategy, providing a unified way to execute the task without knowing the details of how it’s done.

2. Strategy Interface(SortingStrategy): The Strategy Interface is an interface or abstract class that defines a set of methods that all concrete strategies must implement.

3. Concrete Strategies: Concrete Strategies are the various implementations of the Strategy Interface. Each concrete strategy provides a specific algorithm or behavior for performing the task defined by the Strategy Interface.

4. Client Component: The Client is responsible for selecting and configuring the appropriate strategy and providing it to the Context.

##### Communication between the Components

- Client to Context
- Context to Strategy
- Strategy to Context: Return data to Context after executing specific strategy.
- Strategy Interface as Contract: The Strategy Interface serves as a contract that defines a set of methods that all concrete strategies must implement.
- Decoupled Communication: Context does not need to know the specific details of how each strategy implements the task. Strategies can be swapped or replaced without impacting the client

Useful scenarios:

- Payment Processing in E-Commerce Systems: Different payment methods can be encapsulated as separate strategy classes implementing a common PaymentStrategy interface.
- Sorting Algorithms: Each sorting algorithm is implemented as a strategy class that implements a common SortStrategy interface. The application can choose the appropriate sorting strategy at runtime.
- Authentication Mechanisms: Each authentication method is implemented as a strategy class that implements a common AuthenticationStrategy interface. The application can select the appropriate strategy at runtime based on the context.
- Tax Calculation in Finance Systems: Each tax calculation method is implemented as a strategy class that implements a common TaxStrategy interface. A global e-commerce platform calculates taxes differently for users in the EU, the US, and Asia.
- File Parsing and Processing: Each file parsing method is implemented as a strategy class that implements a common FileParserStrategy interface. A data import tool might need to handle CSV, JSON, and XML files differently.
- Document Generation Systems: Each document generation method is implemented as a strategy class that implements a common DocumentStrategy interface. A report generation tool might allow users to export reports in PDF, Word, or HTML formats.
- Notification Sending in Communication Systems: Each notification sending method is implemented as a strategy class that implements a common NotificationStrategy interface. An alert system might send critical alerts via SMS, regular updates via email, and app notifications for non-urgent messages.
- Data Caching Mechanisms: Each caching method is implemented as a strategy class that implements a common CachingStrategy interface.
- Input Validation in Form Handling: Each validation method is implemented as a strategy class that implements a common ValidationStrategy interface. When a user submits a form, the application might validate the input client-side for immediate feedback and server-side for security

When to use this Pattern:

- Multiple Algorithms: When you have multiple algorithms that can be used interchangeably based on different contexts.
- Encapsulating Algorithms: When you want to encapsulate the implementation details of algorithms separately from the context that uses them.
- Runtime Selection: When you need to dynamically select and switch between different algorithms at runtime based on user preferences.
- Reducing Conditional Statements: When you have a class with multiple conditional statements that choose between different behaviors, using the Strategy pattern helps in eliminating the need for conditional statements.
- Testing and Extensibility: When you want to facilitate easier unit testing by enabling the substitution of algorithms with mock objects or stubs.

#### Iterator Pattern (https://refactoring.guru/design-patterns/iterator): Collections are one of the most used data types in programming. Nonetheless, a collection is just a container for a group of objects. Most collections store their elements in simple lists. However, some of them are based on stacks, trees, graphs and other complex data structures. The main idea of the Iterator pattern is to extract the traversal behavior of a collection into a separate object called an iterator.

Let’s understand how Iterator Design Pattern will created:

1. Iterator Interface: Defines the methods for accessing and traversing the collection. It typically includes methods like hasNext(), next(), and optionally remove().
2. Aggregate Interface: Defines the method for creating an iterator. It typically includes a method like createIterator() that returns an Iterator object for the collection.
3. Concrete Iterator: Implements the Iterator interface and provides the actual iteration logic.
4. Concrete Aggregate: Implements the Aggregate interface and provides the method to create an iterator for the collection.

Useful scenarios:

- Social Media Feed: Each feed source (friends, pages, groups) can be represented as a collection, with an iterator to traverse the posts in a specific orderEach feed source (friends, pages, groups) can be represented as a collection, with an iterator to traverse the posts in a specific order.
- Product Catalog in E-Commerce Platforms: The catalog and its categories can be treated as collections, and an iterator can be used to traverse through products or subcategories in a consistent manner.
- File System Navigation: The files and directories can be represented as a collection, with an iterator used to traverse the directory tree.
- Tree Traversal in Hierarchical Data: A tree structure can be traversed using an iterator, with specific traversal strategies like pre-order, in-order, or post-order, DFS, BFS etc..
- Document Parsing: The document elements can be treated as a collection, with an iterator used to traverse through these elements in sequence.
- Web Crawlers: The web pages can be treated as a collection of URLs, with an iterator used to traverse through the links on each page.
- Inventory Management Systems: The inventory items, categories, and warehouses can be treated as collections, with an iterator used to traverse and manage the items.
- Workflow Engines: The tasks or steps in the workflow are treated as collections, with an iterator used to traverse and execute each step in order.

When to use this Pattern:

- Need for sequential access: Use the Iterator pattern when you need to access elements of a collection sequentially without exposing its underlying representation
- Decoupling iteration logic
- Support for multiple iterators: Use the Iterator pattern when you need to support multiple iterators over the same collection.
- Simplifying client code: Use the Iterator pattern to simplify client code that iterates over a collection.

#### Observer Pattern (Pub-Sub) (https://refactoring.guru/design-patterns/observer): Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing. The object that has some interesting state is often called subject, but since it’s also going to notify other objects about the changes to its state, we’ll call it publisher. All other objects that want to track changes to the publisher’s state are called subscribers.

Let’s understand how Observer Design Pattern will created:
https://www.geeksforgeeks.org/observer-pattern-set-1-introduction/

1. Subject : The subject maintains a list of observers (subscribers or listeners). It Provides methods to register and unregister observers dynamically. The “Subject" interface outlines the operations a subject (like “WeatherStation") should support. "addObserver" and “removeObserver" are for managing the list of observers. "notifyObservers" is for informing observers about changes.

2. Observer : The “Observer" interface defines a contract for objects that want to be notified about changes in the subject (“WeatherStation" in this case). It includes a method “update" that concrete observers must implement to receive and handle updates.

3. ConcreteSubject(WeatherStation): "WeatherStation" is the concrete subject implementing the “Subject" interface. It maintains a list of observers (“observers") and provides methods to manage this list. "notifyObservers" iterates through the observers and calls their “update" method, passing the current weather.

4. ConcreteObserver(PhoneDisplay): "PhoneDisplay" is a concrete observer implementing the “Observer" interface. It has a private field weather to store the latest weather. The “update" method sets the new weather and calls the “display" method.

5. ConcreteObserver(TVDisplay)

6. Usage: In “WeatherApp", a “WeatherStation" is created. Two observers (“PhoneDisplay" and “TVDisplay") are registered with the weather station using “addObserver".

Useful scenarios:

When to use this Pattern:

#### Command Pattern (https://refactoring.guru/design-patterns/command): Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

The Command Pattern encapsulates a request as an object, allowing for the separation of sender and receiver.
Commands can be parameterized, meaning you can create different commands with different parameters without changing the invoker(responsible for initiating command execution).
It decouples the sender (client or invoker) from the receiver (object performing the operation), providing flexibility and extensibility.
The pattern supports undoable(action or a series of actions that can be reversed or undone in a system) operations by storing the state or reverse commands.

Let’s understand how Command Design Pattern will created:
https://www.geeksforgeeks.org/command-pattern/

1. Command Interface: The Command interface declares a method, often named execute(). This method is meant to encapsulate a specific operation.
2. Concrete Command Classes: Concrete command classes implement the Command interface. Each class encapsulates a specific operation related to devices. Each concrete command class provides a specific implementation of the execute() method, defining how a particular device operation (turning on, turning off, adjusting volume, changing channel) is executed.
3. Receiver Classes (Devices): The Device interface declares methods related to device functionality, such as turnOn() and turnOff(). This interface sets a contract for device classes.
4. Invoker Class (Remote Control): The invoker class holds a reference to a Command object and triggers its execution through the execute() method. The invoker doesn’t know the specific details of the command or the devices. It simply calls the execute() method on the current command.

Useful scenarios:

When to use this Pattern:

#### State Pattern (https://refactoring.guru/design-patterns/state): State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class. The State pattern suggests that you create new classes for all possible states of an object and extract all state-specific behaviors into these classes. Instead of implementing all behaviors on its own, the original object, called context, stores a reference to one of the state objects that represents its current state

Let’s understand how State Design Pattern will created:

https://www.geeksforgeeks.org/state-design-pattern/

Eg: User interactions with the vending machine trigger state transitions. For example, when a user inserts money, the vending machine transitions from the “ReadyState” to the “PaymentPendingState.” Similarly, when a product is selected, the vending machine transitions to the “ProductSelectedState.” If a product is out of stock, the vending machine transitions to the “OutOfStockState.”

1. Context(VendingMachineContext): The context is responsible for maintaining the current state of the vending machine and delegating state-specific behavior to the appropriate state object. The Context provides an interface for clients to interact with and typically delegates state-specific behavior to the current state object.

2. State Interface (VendingMachineState): This interface defines the contract that all concrete state classes must implement. It typically contains a method or methods representing the behavior associated with each state of the vending machine.

3. Concrete States (Specific Vending Machine States): Concrete state classes represent specific states of the vending machine, such as “ReadyState,” “ProductSelectedState,” and “OutOfStockState.” Each concrete state class implements the behavior associated with its respective state, like allowing product selection, processing payment, or displaying an out-of-stock message.

4. Client: Interacts with the Context that contains the state references.

Useful scenarios:

- ATM Machine: The ATM machine can have states like NoCard, HasCard, Authenticated, and DispensingCash. Each state has its behavior, and the machine transitions between states as the user interacts with it.

- Traffic Light System: The traffic light can have states like GreenLight, YellowLight, and RedLight, with each state defining the behavior of the light. The light transitions from one state to another based on a timer or external input.

- Document Workflow Management: The document can have states like Draft, InReview, Approved, and Rejected. Each state defines the actions that can be taken (e.g., editing is only allowed in the Draft state).

- Order Processing System: The order can have states like NewOrder, PaidOrder, ShippedOrder, DeliveredOrder, and CanceledOrder. Each state defines the actions that can be taken (e.g., an order can only be shipped if it has been paid).

- Customer Support Ticket System: The ticket can have states like NewTicket, InProgressTicket, OnHoldTicket, ResolvedTicket, and ClosedTicket. Each state defines the actions that can be taken (e.g., a ticket can only be resolved if it is in progress).

- Subscription Service: The subscription can have states like ActiveState, SuspendedState, and CanceledState. Each state defines what actions are allowed (e.g., a user can only access premium features if the subscription is active).

- Project Management Software: The task can have states like ToDoState, InProgressState, BlockedState, and CompletedState. Each state defines the actions that can be taken (e.g., a task can only be marked as completed if it is in progress).

- Text Editor: The editor can have states like EditMode, ReadOnlyMode, and CommandMode. Each state defines how the editor handles user input and text manipulation.

When to use this Pattern:

#### Template Method Pattern (https://refactoring.guru/design-patterns/template-method): Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure. The Template Method pattern suggests that you break down an algorithm into a series of steps, turn these steps into methods, and put a series of calls to these methods inside a single template method.

Let’s understand how Template Design Pattern will created:
https://www.geeksforgeeks.org/template-method-design-pattern/

1. Abstract Class (BeverageMaker): This is the superclass that defines the template method. It provides a skeleton for the algorithm, where certain steps are defined but others are left abstract or defined as hooks that subclasses can override.

2. Template Method (makeBeverage()): This is the method within the abstract class that defines the overall algorithm structure by calling various steps in a specific order, eg; boilWater(), brew(), pourInCup(), addCondiments().

3. Abstract (or Hook) Methods: These are methods declared within the abstract class but not implemented. They serve as placeholders for steps in the algorithm that should be implemented by subclasses. eg; brew(), addCondiments().

4. Concrete Subclasses (TeaMaker/CoffeeMaker): These are the subclasses that extend the abstract class and provide concrete implementations for the abstract methods defined in the superclass. Each subclass can override certain steps of the algorithm to customize the behavior

5. Client: Interact with Concrete subclasses, person who wants to make a hot beverage, so you decide whether you want tea or coffee.

Useful scenarios:

- Online Payment Processing: A base class PaymentProcessor defines the common steps (e.g., validate payment, process payment, and send confirmation), with subclasses implementing specific gateway-related logic.

- Document Generation: A base class DocumentGenerator defines the common steps (e.g., prepare header, generate content, and prepare footer), with subclasses implementing the specifics for each document type.

- Game Development: A base class GameLevel defines the common steps, with subclasses implementing specific logic for different levels.

- Data Processing Pipelines: A base class DataProcessor defines the common steps, with subclasses implementing the specifics for each data type.

- User Authentication: A base class Authenticator defines the common authentication steps (e.g., gather credentials, validate credentials, and grant access), with subclasses implementing the specific logic for each method.

- File Parsing: A base class FileParser defines the common steps (e.g., open file, read content, and parse content), with subclasses implementing specific parsing logic for each file type.

- Software Build Processes: A base class BuildProcess defines the common build steps, with subclasses implementing specific logic for different types of projects. eg: JavaBuildProcess, PythonBuildProcess, and NodeJSBuildProcess classes.

- Restaurant Order Processing: A base class OrderProcessor defines the common steps (e.g., take order, process payment, and deliver order), with subclasses implementing the specific logic for each type of order.

- Notification Sending System: A base class NotificationSender defines the common steps (e.g., create message, send message, and log result), with subclasses implementing the specific sending logic for each channel.

- Report Generation: A base class ReportGenerator defines the common steps (e.g., gather data, format report, and generate output), with subclasses implementing the specific logic for each report type.

When to use this Pattern:
