Aquí tienes una explicación detallada de los diferentes tipos de módulos en Taskyto, sus propósitos, características distintivas y cómo se interconectan:

1. Módulo de Menú
Propósito Principal: El módulo de menú es el punto de entrada principal para la interacción del usuario. Permite al usuario elegir entre diferentes opciones de conversación.

Características Distintivas:

Presentación: Proporciona una descripción clara de lo que el módulo hace.
Elementos: Contiene una lista de elementos que pueden ser respuestas directas, referencias a otros módulos (como módulos de preguntas y respuestas o recopilación de datos), o secuencias de módulos.
Fallback: Permite definir un mensaje de respaldo que se utiliza cuando el chatbot no entiende la entrada del usuario.
2. Módulo de Acción
Propósito Principal: Ejecuta acciones específicas basadas en la entrada del usuario. Se utiliza para realizar cálculos, enviar datos a un servicio externo, etc.

Características Distintivas:

Dependencia de Datos: Asume que los datos necesarios han sido recopilados previamente por un módulo de recopilación de datos.
Código Ejecutable: Puede incluir código Python que se ejecuta cuando se activa el módulo.
No se Referencia Directamente: No puede ser referenciado directamente en un menú, solo en secuencias.
3. Módulo de Recopilación de Datos
Propósito Principal: Solicita información específica del usuario que es necesaria para completar una acción o responder a una pregunta.

Características Distintivas:

Definición de Datos: Permite definir los datos que se recopilarán, incluyendo tipos y ejemplos.
On-Success: Define qué hacer una vez que se ha recopilado la información, como ejecutar un módulo de acción.
Interacción Directa: Se utiliza para interactuar directamente con el usuario y obtener información.
4. Módulo de Preguntas y Respuestas
Propósito Principal: Proporciona respuestas a preguntas comunes que los usuarios pueden tener.

Características Distintivas:

Preguntas Directas: Las preguntas se definen explícitamente, y el módulo utiliza un LLM para emparejar la entrada del usuario con las preguntas definidas.
Respuesta Automática: Puede devolver respuestas sin necesidad de un módulo de acción.
Flexibilidad: No requiere múltiples frases de entrenamiento para reconocer intenciones, lo que simplifica la configuración.
5. Módulo de Secuencia
Propósito Principal: Orquesta flujos de conversación complejos al encadenar varios módulos.

Características Distintivas:

Memoria Completa: Debe incluir la opción memory: full para mejorar la gestión del contexto.
Referencias a Módulos: Puede incluir referencias a múltiples módulos, incluyendo módulos de acción, siempre que estén precedidos por módulos de recopilación de datos.
Flujos Complejos: Permite crear flujos de conversación más elaborados y estructurados.
Interconexiones y Dependencias
Dependencia de Módulos de Acción y Recopilación de Datos: Un módulo de acción siempre debe ser precedido por un módulo de recopilación de datos. Esto asegura que la acción tenga acceso a la información necesaria para ejecutarse correctamente.
Uso de Módulos de Secuencia: Los módulos de secuencia permiten combinar múltiples módulos, facilitando la creación de flujos de conversación complejos. Esto es especialmente útil cuando se necesita recopilar datos y luego realizar acciones basadas en esos datos.
Funcionalidades Específicas: El uso de LLMs en módulos de preguntas y respuestas permite un emparejamiento más natural de las preguntas del usuario, mientras que el fallback en los menús asegura que el chatbot pueda manejar entradas no reconocidas de manera efectiva.
Conclusión
Al diseñar tu chatbot, considera el propósito de cada módulo y cómo se interconectan. Utiliza módulos de recopilación de datos para obtener información del usuario, módulos de acción para procesar esa información y módulos de menú y secuencia para guiar la conversación. Esto asegurará una estructura lógica y eficiente en tu chatbot.

Si necesitas ayuda para implementar alguno de estos módulos en tu proyecto, no dudes en pedírmelo.