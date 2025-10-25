Here is an overview of the Taskyto module types:

Menu Module: This module defines a set of conversation alternatives (exclusive choices). It can capture user responses, manage complex conversation flows, or reference other modules. It may also include a fallback response for unrecognized user input.

Action Module: This module executes an action based on input data. Actions are defined in Python and can produce a response for the user. The response can be displayed verbatim or rephrased using an LLM.

Data Gathering Module: This module requests data from the user and may execute an action based on the gathered data.

Question Answering Module: This module defines a set of questions and their corresponding answers. It uses an LLM to identify which question corresponds to the user's input without needing multiple training phrases.

Sequence Module: This module defines a chain of conversation steps, each defined in another module. It allows for more complex conversation flows.

If you have any specific questions about these module types or need assistance with creating a Taskyto chatbot, feel free to ask!