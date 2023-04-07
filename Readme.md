# Backend developer - Prueba técnica
## Reto: Biblioteca
### Objetivo: Crear un API web que permita administrar una pequeña biblioteca. El servicio
Tiene un repositorio interno y además se alimenta de 2 APIs públicas.

En la biblioteca cada libro tiene:
- Id
- Título
- Subtítulo
- Autor(es)
- Categoría(s)
- Fecha publicación
- 1 Editor
- Descripción
- Imagen (Opcional)

### Alcance:
1. Diseñar la base de datos de acuerdo a los atributos del libro. Puede utilizar cualquier
motor. Ej: postgres, mongo, dynamodb, etc
2. Crear un servicio para buscar un libro por cualquiera de sus atributos. Si no hay
registros en la base de datos interna, el servicio debe hacer la búsqueda en el API
de libros de google y entregar los resultados.
a. En la respuesta del APi se debe indicar la fuente, Ej: db interna, google
3. Registrar un libro. Si la fuente en la respuesta del punto 2 no es la DB interna, se
debe poder crear un libro con el resultado de esa búsqueda. Solo se debe enviar un
identificador y la fuente.
4. Integrar otra API de consulta de libros.
5. Eliminar un libro.
### Requisitos técnicos:
1. Desarrollar con python 3.X
2. Se puede utilizar cualquier framework.
3. Crear un repositorio en github/gitlab/bitbucket/otro e ir subiendo los commits.
### Bonus:
1. Hacer el WS graphql en lugar de REST.
2. Utilizar asincronía para las operaciones a la DB y el consumo de la API de google
3. Hacer de manera concurrente los requests a ambos API.
4. Proteger los endpoints con algún mecanismo de seguridad.
5. Desplegar el endpoint en un server y entregar las URLs para validación.