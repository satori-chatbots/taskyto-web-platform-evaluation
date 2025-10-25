Aquí tienes una explicación detallada de los tipos de módulos en Taskyto, sus propósitos, características y cómo se interconectan. Esto te ayudará a optimizar la estructura y lógica de tu chatbot.

1. Módulo de Menú
Propósito: Actúa como el punto de entrada principal para la interacción del usuario. Permite definir opciones de conversación que el usuario puede elegir.
Características:
Contiene una presentación que describe el módulo y cómo interactuar con él.
Puede incluir un mensaje de fallback que se utiliza cuando el chatbot no entiende la entrada del usuario.
Los elementos del menú pueden referirse a otros módulos (como módulos de preguntas y respuestas o de recopilación de datos) o a secuencias de módulos.
2. Módulo de Acción
Propósito: Ejecuta acciones específicas basadas en la entrada del usuario. Esto puede incluir cálculos, interacciones con bases de datos, o cualquier lógica de negocio que necesite ser ejecutada.
Características:
No tiene una descripción como tal.
Asume que los datos necesarios han sido recopilados previamente por un módulo de recopilación de datos.
Puede ser referenciado dentro de un módulo de secuencia, pero debe ser precedido por un módulo de recopilación de datos.
3. Módulo de Recopilación de Datos
Propósito: Solicita información específica del usuario que es necesaria para ejecutar acciones o responder preguntas.
Características:
Define los datos que se deben recopilar, especificando el tipo de cada dato (por ejemplo, string, integer, enum).
Puede incluir una descripción que explique qué datos se necesitan y por qué.
Al finalizar la recopilación de datos, puede ejecutar una acción y proporcionar una respuesta al usuario.
4. Módulo de Preguntas y Respuestas
Propósito: Permite al chatbot responder a preguntas específicas que los usuarios pueden hacer.
Características:
Define un conjunto de preguntas y sus respuestas correspondientes.
Utiliza un modelo de lenguaje (LLM) para identificar la pregunta del usuario y proporcionar la respuesta adecuada.
Puede incluir un bloque de ejecución para realizar acciones adicionales basadas en la pregunta.
5. Módulo de Secuencia
Propósito: Permite encadenar varios módulos en un flujo de conversación más complejo.
Características:
Se define dentro de un módulo de menú y puede incluir múltiples módulos de recopilación de datos y acción.
Debe tener la opción memory: full para mejorar la gestión del contexto de la conversación.
Facilita la creación de flujos de conversación que requieren múltiples pasos y decisiones.
Interconexiones y Dependencias
Dependencia de Módulos de Acción y Recopilación de Datos: Un módulo de acción siempre debe ser precedido por un módulo de recopilación de datos. Esto asegura que la acción tenga acceso a la información necesaria para ejecutarse correctamente.
Uso de LLMs en Módulos de Preguntas y Respuestas: Los módulos de preguntas y respuestas utilizan LLMs para interpretar las preguntas del usuario y proporcionar respuestas precisas, lo que mejora la experiencia del usuario al interactuar con el chatbot.
Comparativa para el Diseño
Fase de Inicio: Utiliza un módulo de menú para establecer el contexto y las opciones disponibles para el usuario.
Fase de Recopilación de Información: Implementa módulos de recopilación de datos para obtener la información necesaria antes de ejecutar acciones.
Fase de Ejecución: Usa módulos de acción para procesar la información recopilada y realizar cálculos o interacciones.
Fase de Respuesta: Implementa módulos de preguntas y respuestas para manejar consultas específicas de los usuarios.
Fase de Flujo Complejo: Utiliza módulos de secuencia para crear flujos de conversación que requieren múltiples pasos y decisiones.
Esta estructura te permitirá diseñar un chatbot eficiente y lógico, optimizando la interacción con los usuarios y asegurando que todas las partes del flujo de conversación estén bien conectadas.

Si necesitas ayuda para implementar alguno de estos módulos en tu proyecto de Taskyto, no dudes en decírmelo.