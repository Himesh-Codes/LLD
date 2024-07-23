# LLD (JAVA)

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

### Creational Patterns

- Singleton (https://blog.algomaster.io/p/singleton-design-pattern): Class to have only one object created,
  achieved by making the constructor private to avoid other classes creates it's object and providing a static method for external objects to access it.

  Singleton is useful in scenarios like:
  Managing Shared Resources (database connections, thread pools, caches, configuration settings)
  Coordinating System-Wide Actions (logging, print spoolers, file managers)
  Managing State (user session, application state)

  Note: Consider alternative approaches like dependency injection when possible to promote loose coupling and testability.

  [Code](./Design%20Patterns/singleton.java)

- Factory (https://refactoring.guru/design-patterns/factory-method): The subclasses can create an object of one class with help of a factory class, Factory Method Pattern says that just define an interface or abstract class for creating an object but let the subclasses decide which class to instantiate, with providing the type.
  https://www.javatpoint.com/factory-method-design-pattern

Usage of Factory Design Pattern:
When a class doesn't know what sub-classes will be required to create
When a class wants that its sub-classes specify the objects to be created.
When the parent classes choose the creation of objects to its sub-classes.
