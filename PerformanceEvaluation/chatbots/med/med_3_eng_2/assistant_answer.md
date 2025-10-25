1. Menu Module
Purpose: The menu module serves as the entry point for user interactions. It presents users with a set of options to choose from, guiding them through the conversation flow.
Characteristics:
Contains a presentation field that describes the module's purpose.
Can include a fallback message to handle unrecognized inputs.
Items can be of type answer, module, or sequence.
Interconnections: Menu modules can reference other modules (like data gathering or question answering) but cannot reference action modules directly.
2. Action Module
Purpose: Action modules execute specific actions based on user input or previously gathered data. They are typically used to perform calculations or trigger external processes.
Characteristics:
Does not have a description field.
Requires a data field that references previously gathered data from data gathering modules.
Executes code (Python) and returns a result.
Interconnections: Must be preceded by at least one data gathering module within a sequence module. They rely on data gathered from previous interactions.
3. Data Gathering Module
Purpose: This module is designed to collect information from the user. It prompts users for specific data needed for subsequent actions or responses.
Characteristics:
Contains a data field that defines the required inputs.
Can include a description field explaining what data is being collected.
Has an on-success section that defines what happens after data is successfully gathered.
Interconnections: Data gathering modules are often followed by action modules to process the collected data.
4. Question Answering Module
Purpose: This module is used to provide answers to frequently asked questions. It allows the chatbot to respond to user inquiries without needing extensive training phrases.
Characteristics:
Contains a list of predefined questions and their corresponding answers.
Can include an on-success section to execute code if needed.
Uses LLMs to identify user questions and provide relevant answers.
Interconnections: Can be referenced in menu modules but does not directly interact with action modules.
5. Sequence Module
Purpose: Sequence modules define a series of steps in a conversation flow, allowing for complex interactions.
Characteristics:
Must include the memory: full option to enhance context retention.
Can reference multiple modules, including data gathering and action modules.
Interconnections: They can chain together various modules, allowing for a structured flow of conversation that can include data gathering followed by actions.
Comparison and Usage
Menu Modules: Use when you want to present options to the user. Ideal for starting points in the conversation.
Data Gathering Modules: Use when you need to collect specific information from the user before proceeding.
Action Modules: Use when you need to perform an action based on previously gathered data. They should always follow data gathering modules.
Question Answering Modules: Use for providing quick responses to common questions without needing extensive user input.
Sequence Modules: Use to create complex flows that require multiple steps, combining data gathering and actions.
Example of Module Interconnections
A user starts with a Menu Module that offers options. If they choose to order a pizza, the chatbot transitions to a Data Gathering Module to collect pizza preferences. After gathering the data, it moves to an Action Module to calculate the price or confirm the order. If the user has questions, the Question Answering Module can be referenced from the menu.
This structure optimizes the chatbot's logic and enhances user experience by clearly defining the flow of conversation and the purpose of each module.

If you need any specific YAML content or further assistance in developing your Taskyto chatbot, feel free to ask!