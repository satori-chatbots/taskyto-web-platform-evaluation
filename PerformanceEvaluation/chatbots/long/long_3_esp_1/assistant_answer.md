Aquí tienes una explicación detallada de los diferentes tipos de módulos en Taskyto, sus propósitos, características distintivas y cómo se interconectan:

1. Módulo de Menú
Propósito Principal: Actúa como el punto de entrada para la interacción del usuario. Permite al usuario elegir entre diferentes opciones de conversación.
Características Distintivas:
Contiene una presentación que describe el módulo y las opciones disponibles.
Puede incluir un mensaje de fallback que se utiliza cuando el chatbot no entiende la entrada del usuario.
Los elementos del menú pueden referirse a otros módulos (menú, preguntas y respuestas, o recopilación de datos) o a secuencias de módulos.
2. Módulo de Acción
Propósito Principal: Ejecuta acciones específicas basadas en la entrada del usuario. Esto puede incluir cálculos, interacciones con bases de datos, o cualquier lógica de negocio.
Características Distintivas:
No tiene una descripción como tal.
Se basa en datos que han sido recopilados previamente por módulos de recopilación de datos.
Puede devolver un resultado que se utiliza en la respuesta al usuario.
3. Módulo de Recopilación de Datos
Propósito Principal: Solicita información específica al usuario que es necesaria para completar una acción o responder a una pregunta.
Características Distintivas:
Define los datos que se deben recopilar, especificando tipos y si son obligatorios.
Puede ejecutar acciones después de recopilar datos, lo que permite una interacción más dinámica.
La respuesta se puede personalizar utilizando los datos recopilados.
4. Módulo de Preguntas y Respuestas
Propósito Principal: Permite al chatbot responder a preguntas específicas de los usuarios sin necesidad de reformular las preguntas en múltiples formas.
Características Distintivas:
Define un conjunto de preguntas y respuestas.
Utiliza un LLM para identificar la pregunta formulada por el usuario y proporcionar la respuesta correspondiente.
Puede incluir un bloque de ejecución para realizar acciones adicionales si es necesario.
5. Módulo de Secuencia
Propósito Principal: Orquesta flujos de conversación complejos al encadenar múltiples módulos.
Características Distintivas:
Se define dentro de un módulo de menú y permite la ejecución de varios módulos en un orden específico.
Debe incluir la opción memory: full para mejorar la gestión del contexto.
Puede incluir módulos de acción, siempre que estén precedidos por módulos de recopilación de datos.
Interconexiones y Dependencias
Dependencia de Módulos de Acción y Recopilación de Datos: Los módulos de acción requieren que los datos sean recopilados previamente por módulos de recopilación de datos. Esto asegura que la acción tenga la información necesaria para ejecutarse correctamente.
Rol de los Módulos de Secuencia: Los módulos de secuencia permiten encadenar la lógica de conversación, facilitando flujos más complejos que pueden incluir múltiples pasos de recopilación de datos y acciones. Esto es útil para interacciones que requieren varios inputs del usuario antes de llegar a una conclusión o respuesta final.
Funcionalidades Específicas
Fallback en Menús: Proporciona una respuesta alternativa cuando el chatbot no entiende la entrada del usuario, mejorando la experiencia del usuario.
Uso de LLMs: En los módulos de preguntas y respuestas, los LLMs permiten un emparejamiento más natural y efectivo de las preguntas formuladas por el usuario, mejorando la precisión de las respuestas.
Conclusión
Al diseñar tu chatbot, considera el propósito de cada módulo y cómo se interconectan. Utiliza módulos de recopilación de datos para obtener la información necesaria, módulos de acción para ejecutar lógica y módulos de menú para guiar al usuario a través de la conversación. Los módulos de secuencia son ideales para flujos complejos que requieren múltiples pasos.

Si necesitas ayuda adicional para implementar alguno de estos módulos en tu chatbot, no dudes en preguntar.