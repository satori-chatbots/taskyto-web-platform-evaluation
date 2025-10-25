Aquí tienes una explicación detallada de los tipos de módulos en Taskyto, sus propósitos, características y cómo se interconectan:

1. Módulo de Menú
Propósito: Actúa como el punto de entrada principal para la interacción del usuario. Permite definir un conjunto de opciones de conversación que el usuario puede elegir.
Características:
Contiene elementos que pueden ser respuestas directas, referencias a otros módulos (como módulos de preguntas y respuestas o recopilación de datos), o secuencias de módulos.
Puede incluir un mensaje de fallback que se utiliza cuando el chatbot no entiende la entrada del usuario.
Interconexión: Los módulos de menú pueden llamar a otros módulos, pero no pueden referenciar módulos de acción directamente.
2. Módulo de Acción
Propósito: Ejecuta acciones específicas basadas en la entrada del usuario. Esto puede incluir cálculos, interacciones con bases de datos, o cualquier lógica de negocio necesaria.
Características:
Se basa en datos que deben ser recopilados previamente por un módulo de recopilación de datos.
Puede devolver un resultado que se utiliza en la respuesta al usuario.
Interconexión: Siempre debe ser precedido por un módulo de recopilación de datos en una secuencia. No puede ser referenciado directamente desde un menú.
3. Módulo de Recopilación de Datos
Propósito: Solicita información específica del usuario que es necesaria para completar una acción o responder a una pregunta.
Características:
Define los datos que se deben recopilar, especificando tipos y si son obligatorios o no.
Puede ejecutar acciones después de recopilar los datos.
Interconexión: Los módulos de acción dependen de los módulos de recopilación de datos para obtener la información necesaria antes de ejecutar cualquier lógica.
4. Módulo de Preguntas y Respuestas
Propósito: Permite al chatbot responder a preguntas específicas de los usuarios sin necesidad de entrenamiento extenso de intenciones.
Características:
Define preguntas y respuestas de manera directa.
Puede incluir lógica de ejecución que permite realizar cálculos o acciones antes de responder.
Interconexión: Puede ser referenciado desde un menú, pero no puede ser parte de una secuencia que incluya módulos de acción.
5. Módulo de Secuencia
Propósito: Permite encadenar varios pasos de conversación, facilitando flujos más complejos.
Características:
Cada paso en la secuencia puede ser un módulo de recopilación de datos, un módulo de acción o un módulo de preguntas y respuestas.
Se debe especificar memory: full para mejorar la gestión del contexto.
Interconexión: Permite la inclusión de módulos de acción, siempre que estén precedidos por módulos de recopilación de datos.
Comparativa y Uso
Menú: Utilizado para iniciar la conversación y ofrecer opciones al usuario. Ideal para la navegación inicial.
Recopilación de Datos: Usado cuando se necesita información del usuario antes de proceder. Fundamental en la fase de recolección de datos.
Acción: Utilizado para ejecutar lógica o cálculos. Debe ser usado después de un módulo de recopilación de datos.
Preguntas y Respuestas: Ideal para proporcionar información estática o responder preguntas frecuentes sin necesidad de lógica adicional.
Secuencia: Utilizado para flujos complejos donde se requiere una serie de pasos interconectados.
Funciones Adicionales
Fallback en Menús: Proporciona una respuesta alternativa cuando el usuario no entiende la opción seleccionada.
Uso de LLMs en Q&A: Permite respuestas más naturales y contextuales, mejorando la interacción del usuario.
Esta estructura y lógica optimizan el diseño del chatbot, asegurando que cada módulo cumpla su función específica y se interconecte de manera efectiva para proporcionar una experiencia de usuario fluida.