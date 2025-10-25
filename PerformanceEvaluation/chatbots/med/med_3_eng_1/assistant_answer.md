Here’s a detailed explanation of the types of modules in Taskyto, including their purposes, characteristics, interconnections, and guidance on when to use each type.

1. Menu Module
Purpose: The menu module serves as the entry point for user interactions. It presents users with a set of options to choose from, guiding them through the conversation flow.
Characteristics:
Contains a presentation field that describes the module's purpose.
Can include a fallback response to handle unrecognized inputs.
Items can be of type answer, module, or sequence.
Interconnections: Menu modules can reference other modules (like data gathering or question answering) but cannot reference action modules directly.
2. Action Module
Purpose: Action modules execute specific actions based on user input or gathered data. They are typically used to perform computations or trigger external processes.
Characteristics:
Does not have a description field.
Assumes that data has been previously gathered by data gathering modules.
Can return a result that can be referenced in the response text.
Interconnections: Action modules must be preceded by at least one data gathering module when used in a sequence. They can only be referenced in sequence modules.
3. Data Gathering Module
Purpose: This module is used to collect information from the user. It prompts the user for specific data needed for further processing.
Characteristics:
Contains a data field that defines the expected inputs.
Can have a description field explaining what data is being collected.
The on-success section defines what happens after data is successfully gathered.
Interconnections: Data gathering modules are often followed by action modules to process the collected data. They can also be referenced in menu modules.
4. Question Answering Module
Purpose: This module is designed to provide answers to specific questions that users may ask. It utilizes LLMs to interpret user queries and respond appropriately.
Characteristics:
Contains a list of predefined questions and their corresponding answers.
Can include an execute field to run Python code, allowing for dynamic responses.
The on-success section can reference the result of the executed code.
Interconnections: This module can be referenced in menu modules and can utilize LLMs to enhance user interaction.
5. Sequence Module
Purpose: Sequence modules define a series of steps that the conversation will follow. They allow for complex flows by chaining multiple modules together.
Characteristics:
Must include memory: full to ensure the context is maintained throughout the sequence.
Can reference multiple modules, including data gathering and action modules.
Interconnections: Sequence modules can include action modules, but only if they are preceded by data gathering modules. They help in structuring complex interactions.
Comparison and Usage Guidance
Menu Modules: Use these as the starting point for user interactions. They help in guiding users through available options.
Data Gathering Modules: Use these when you need to collect specific information from users before proceeding with actions.
Action Modules: Use these to perform computations or trigger actions based on the data collected. They should follow data gathering modules.
Question Answering Modules: Use these to provide predefined answers to common questions, enhancing user experience with LLM capabilities.
Sequence Modules: Use these to create complex flows that require multiple steps, ensuring that the context is preserved throughout the interaction.
By understanding the roles and interconnections of these modules, you can optimize the structure and logic of your Taskyto chatbot, ensuring a smooth and efficient user experience.

If you need any specific YAML content or further assistance in developing your chatbot, feel free to ask!