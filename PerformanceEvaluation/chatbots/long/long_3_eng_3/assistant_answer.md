In Taskyto, there are five main types of modules, each serving a distinct purpose in the chatbot's architecture. Understanding these modules and their interconnections is crucial for designing an efficient and logical chatbot structure. Below is a detailed explanation of each module type, including their characteristics, functionalities, and how they interconnect.

1. Menu Module
Purpose: The menu module serves as the entry point for user interactions. It presents users with a set of options to choose from, guiding them through the conversation flow.

Distinctive Characteristics:

Presentation: It includes a clear description of the module's purpose and expected user interactions.
Fallback: A fallback message can be specified to handle unexpected user inputs, ensuring a smoother user experience.
Items: It can contain various items, such as answers, references to other modules, or sequences.
Interconnection: Menu modules can reference other modules (like data gathering or question answering) or initiate sequences, making them versatile in directing the conversation.

2. Action Module
Purpose: Action modules execute specific actions based on user inputs or gathered data. They are typically used to perform backend operations, such as calculations or data processing.

Distinctive Characteristics:

Data Dependency: Action modules assume that the necessary data has been gathered by preceding data gathering modules.
Execution: They can execute Python code, which can either be embedded or referenced from an external script.
Interconnection: Action modules are often placed within sequence modules, following data gathering modules to ensure they have the required data to operate effectively.

3. Data Gathering Module
Purpose: Data gathering modules are designed to collect information from users. They prompt users for specific data inputs necessary for the chatbot's operations.

Distinctive Characteristics:

Data Definition: They define the data fields to be collected, specifying types (e.g., string, integer, enum) and whether the fields are required.
On-Success Handling: Upon successful data collection, they can execute actions or provide responses based on the gathered data.
Interconnection: Data gathering modules are essential precursors to action modules, as action modules rely on the data they collect. They can also be referenced in menu modules to guide users through the data collection process.

4. Question Answering Module
Purpose: This module is designed to handle specific questions from users and provide predefined answers.

Distinctive Characteristics:

Question Matching: It uses LLMs (Large Language Models) to match user questions with predefined questions, allowing for flexible user input.
On-Success Execution: Similar to data gathering modules, it can execute actions based on the matched question.
Interconnection: Question answering modules can be referenced in menu modules, allowing users to access information without needing to navigate through multiple steps.

5. Sequence Module
Purpose: Sequence modules orchestrate a series of steps in a conversation, allowing for complex flows that involve multiple modules.

Distinctive Characteristics:

Memory Management: They require the "memory: full" option to ensure that the context is preserved throughout the sequence.
References: They can reference multiple modules, including data gathering and action modules, to create a cohesive flow.
Interconnection: Sequence modules are crucial for managing the flow of conversation, especially when multiple data points need to be collected before executing an action. They can link various modules together, ensuring a logical progression in user interactions.

Summary of Interconnections
Action modules depend on data gathering modules to provide the necessary data for execution.
Menu modules can reference question answering and data gathering modules, guiding users through the conversation.
Sequence modules orchestrate complex flows by linking multiple modules, ensuring that the chatbot can handle intricate user interactions effectively.
By understanding these module types and their interconnections, you can design a Taskyto chatbot that is both logical and efficient, ensuring a smooth user experience throughout the conversation.

If you need assistance in implementing any of these modules or have specific requirements for your chatbot, feel free to ask!