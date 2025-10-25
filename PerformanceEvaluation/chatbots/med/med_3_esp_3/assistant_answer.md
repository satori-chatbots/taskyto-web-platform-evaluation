Aquí tienes una explicación detallada de los tipos de módulos en Taskyto, incluyendo su propósito, características, interconexiones y recomendaciones sobre cuándo utilizarlos en el diseño de un chatbot.

1. Módulo de Menú
Propósito: Actúa como el punto de entrada principal para la interacción del usuario. Permite al usuario elegir entre diferentes opciones de conversación.
Características:
Contiene una presentación que describe el módulo y las opciones disponibles.
Puede incluir un mensaje de fallback para manejar entradas no reconocidas.
Los elementos del menú pueden referirse a otros módulos (menú, recopilación de datos, preguntas y respuestas) o a secuencias de módulos.
2. Módulo de Acción
Propósito: Ejecuta acciones específicas basadas en la entrada del usuario. Se utiliza para realizar cálculos, enviar datos a un sistema externo, etc.
Características:
No tiene una descripción como tal.
Asume que los datos necesarios han sido recopilados previamente por un módulo de recopilación de datos.
Puede devolver un resultado que se puede utilizar en la respuesta al usuario.
3. Módulo de Recopilación de Datos
Propósito: Solicita información específica del usuario que es necesaria para completar una acción o responder a una pregunta.
Características:
Define los datos que se deben recopilar, especificando tipos y si son obligatorios.
Puede ejecutar acciones después de recopilar los datos.
La información recopilada se puede utilizar en módulos de acción posteriores.
4. Módulo de Preguntas y Respuestas
Propósito: Permite al chatbot responder a preguntas específicas de los usuarios sin necesidad de múltiples frases de entrenamiento.
Características:
Define preguntas y respuestas fijas.
Puede incluir un bloque de ejecución para procesar la respuesta antes de enviarla al usuario.
Utiliza LLMs para identificar la pregunta formulada por el usuario y proporcionar la respuesta correspondiente.
5. Módulo de Secuencia
Propósito: Permite encadenar varios módulos en un flujo de conversación más complejo.
Características:
Debe incluir la opción memory: full para mejorar el contexto de la conversación.
Puede incluir módulos de acción, pero estos deben ser precedidos por módulos de recopilación de datos.
Facilita la creación de flujos de conversación que requieren múltiples pasos.
Interconexiones y Dependencias
Módulos de Acción y Recopilación de Datos: Un módulo de acción siempre debe ser precedido por un módulo de recopilación de datos. Esto asegura que los datos necesarios estén disponibles antes de ejecutar cualquier acción.
Módulos de Secuencia: Permiten combinar varios módulos, incluyendo módulos de recopilación de datos y acción, para crear flujos de conversación más complejos. Esto es útil para interacciones que requieren múltiples pasos, como realizar un pedido.
Uso de Fallback y LLMs
Fallback en Menús: Proporciona una respuesta alternativa cuando el chatbot no entiende la entrada del usuario, mejorando la experiencia del usuario.
Uso de LLMs en Preguntas y Respuestas: Permite que el chatbot entienda y responda a preguntas formuladas de manera natural, sin necesidad de múltiples ejemplos de entrenamiento.
Comparativa y Recomendaciones
Fase de Diseño:
Menú: Utiliza para definir las opciones principales de interacción.
Recopilación de Datos: Usa cuando necesites información específica del usuario antes de proceder.
Acción: Implementa para ejecutar lógica o cálculos basados en los datos recopilados.
Preguntas y Respuestas: Ideal para proporcionar información estática y responder preguntas frecuentes.
Secuencia: Emplea para flujos de conversación que requieren múltiples pasos y decisiones.
Esta estructura y lógica optimizan la interacción del chatbot, asegurando que cada módulo cumpla su función específica y se interconecte de manera efectiva.

Si necesitas ejemplos específicos de módulos o más detalles sobre cómo implementarlos, no dudes en preguntar.