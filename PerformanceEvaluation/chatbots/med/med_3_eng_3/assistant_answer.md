Here is a detailed explanation of the types of modules in Taskyto, including their purposes, characteristics, interconnections, and guidance on when to use each one in the design phase of your chatbot.

1. Menu Module
Purpose: The menu module serves as the primary entry point for user interactions. It presents users with a set of options to choose from, guiding them through the conversation flow.
Characteristics:
Contains items that can be answers, references to other modules, or sequences.
Can include a fallback response, which is triggered when the chatbot does not understand the user's input.
Supports memory management with the memory: full option to enhance context retention.
Use Case: Use a menu module as the top-level module to organize the conversation and provide clear options for users.
2. Action Module
Purpose: The action module executes specific actions based on user input and previously gathered data.
Characteristics:
Does not have a description field.
Assumes that data has been gathered from preceding data gathering modules.
Can return results that can be referenced in the response text.
Interconnection: Action modules must be preceded by data gathering modules to ensure they have the necessary data to operate.
Use Case: Use action modules when you need to perform operations or calculations based on user input.
3. Data Gathering Module
Purpose: This module is designed to collect specific information from users, such as names, dates, or preferences.
Characteristics:
Contains a data section where keywords are defined, specifying the type of data to be collected.
Can include a description field to explain what data is being gathered and why.
Supports on-success actions to respond to users after data collection.
Interconnection: Data gathering modules are essential for collecting input before executing action modules.
Use Case: Use data gathering modules when you need to prompt users for information that will be used later in the conversation.
4. Question Answering Module
Purpose: This module allows the chatbot to respond to specific questions from users without needing extensive training phrases.
Characteristics:
Contains a list of predefined questions and their corresponding answers.
Can utilize LLMs (Large Language Models) to identify user questions and provide relevant answers.
Supports an on-success section for executing code and returning results.
Interconnection: The execute field can be used to run Python code, allowing for dynamic responses based on user queries.
Use Case: Use question answering modules when you want to provide quick, factual responses to common inquiries.
5. Sequence Module
Purpose: The sequence module defines a series of steps in a conversation, allowing for complex flows.
Characteristics:
Must include memory: full to enhance context retention across the sequence.
Can reference multiple modules, including data gathering and action modules.
Interconnection: Sequence modules can link various modules together, creating a coherent flow of conversation.
Use Case: Use sequence modules when you need to guide users through a multi-step process, such as placing an order or completing a form.
Comparison and Recommendations
Menu Modules are best for starting points and guiding users through options.
Data Gathering Modules are essential for collecting user input before any actions can be taken.
Action Modules should follow data gathering modules to perform operations based on the collected data.
Question Answering Modules are ideal for providing quick responses to common questions without extensive training.
Sequence Modules are useful for creating complex flows that require multiple steps and interactions.
By understanding these modules and their interconnections, you can optimize the structure and logic of your Taskyto chatbot, ensuring a smooth and effective user experience.