Here’s a concise overview of the Taskyto module types:

1. **Menu Module**: Defines a set of conversation alternatives. It can capture user responses, manage complex conversation flows, or reference other modules. It may also include a fallback response for unrecognized inputs.

2. **Action Module**: Executes a specific action based on input data. It can run Python code and produce a response for the user, which can be displayed verbatim or rephrased using an LLM.

3. **Data Gathering Module**: Requests specific data from the user and may execute an action based on that data.

4. **Question Answering Module**: Contains a set of predefined questions and answers. It uses an LLM to match user queries to the appropriate questions without needing multiple training phrases.

5. **Sequence Module**: Defines a chain of conversation steps, each specified in another module. It is used to create a flow of interactions.

If you need further details or examples of any specific module type, feel free to ask!