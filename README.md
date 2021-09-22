# REST API Musica
## Agregar nuevo artista

**URL** : `/api/artistas/`

**Metodo** : `POST`

Proveer nombre del Artista que sera creado.

```json
{
    "nombre": "[unicode 70 chars max]"
}
```

**Ejemplo** 

```json
{
    "nombre": "Ruben Blades"
}
```

### Response

```json
{
    "id": 1,
    "nombre": "Ruben Blades"
}
```
## Listar artistas

**URL** : `/api/artistas/`

**Metodo** : `GET`

Devuelve un arreglo con todos los artistas que se encuentran registrados.


### Respuesta

```json
[
    {
        "id": 1,
        "nombre": "Hector Lavoe"
    },
    {
        "id": 2,
        "nombre": "Ruben Blades"
    },
    {
        "id": 3,
        "nombre": "Willie Colon"
    },
    {
        "id": 4,
        "nombre": "Willie Rosario"
    },
    {
        "id": 5,
        "nombre": "Frankie Ruiz"
    }
]
```
