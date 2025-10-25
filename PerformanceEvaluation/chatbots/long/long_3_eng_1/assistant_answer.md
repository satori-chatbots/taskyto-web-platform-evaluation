To help you understand the different types of modules in Taskyto, their purposes, distinctive characteristics, and how they interconnect, here’s a detailed breakdown:

1. Menu Module
Purpose: The menu module serves as the primary entry point for user interactions. It presents users with a set of options to choose from, guiding them through the conversation flow.
Distinctive Characteristics:
Fallback: It can include a fallback message that is triggered when the chatbot does not understand the user's input.
Items: It can contain various items, including answers, references to other modules (like data gathering or question answering), and sequences.
2. Action Module
Purpose: Action modules are designed to execute specific actions based on the input data received from the user.
Distinctive Characteristics:
They do not gather data themselves but rely on data gathered from previous data gathering modules.
They can execute Python code to perform operations and return results.
Action modules are typically referenced within sequence modules after data gathering modules.
3. Data Gathering Module
Purpose: This module is used to collect information from the user, which is essential for the chatbot to function correctly.
Distinctive Characteristics:
It defines the data fields that need to be collected, specifying types and whether they are required.
It can also execute actions upon successful data collection.
The data gathered can be referenced in subsequent action modules.
4. Question Answering Module
Purpose: This module is designed to handle specific questions from users and provide predefined answers.
Distinctive Characteristics:
It uses LLMs (Large Language Models) to match user questions with predefined questions, allowing for flexible user input.
It can execute Python code to modify the response based on the question asked.
The response can include the reserved keywords {result} and {question} for dynamic content.
5. Sequence Module
Purpose: Sequence modules orchestrate a series of steps in a conversation, allowing for complex flows that involve multiple modules.
Distinctive Characteristics:
They must include the memory: full option to enhance the chatbot's context retention.
They can reference multiple modules, including action modules, but only after data gathering modules have been executed.
They help in structuring the conversation logically, ensuring that the user experience is smooth and coherent.
Interconnections and Dependencies
Action and Data Gathering Modules: Action modules depend on data gathered from data gathering modules. An action module cannot function without prior data collection, ensuring that the necessary information is available for processing.
Sequence Modules: These modules play a crucial role in orchestrating the flow of conversation. They can include multiple data gathering and action modules, allowing for a structured approach to complex interactions. This ensures that the chatbot can handle various scenarios effectively.
Functionalities
Fallback in Menus: The fallback feature in menu modules ensures that users receive a response even when their input is not understood, enhancing user experience.
LLMs for Question Matching: The use of LLMs in question answering modules allows for a more natural interaction, as users can ask questions in their own words without needing to match predefined phrases.
This detailed comparison should help you decide which module to use in each phase of your chatbot design, ensuring a logical and efficient structure.

If you need any specific YAML content or further assistance in designing your chatbot, feel free to ask!