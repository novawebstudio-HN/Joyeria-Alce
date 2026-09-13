# Joyería Alce — catálogo web

Catálogo estático de Joyería Alce: sin nombres ni precios de producto, solo las
fotos organizadas por colección, material y línea. Funciona en móvil y
escritorio y no necesita servidor: son archivos HTML, CSS, JS e imágenes.

## Cómo se navega

- **Inicio**: una tarjeta por colección (Anillos, Aretes, Collares, Pulseras,
  Esclavas, Tobilleras, Juegos) con su portada y su número de piezas, más
  accesos directos por material y por línea.
- **Colección**: solo las piezas de esa colección, con dos selectores —
  **Material** (Oro 10K / Plata 925) y **Línea** (Mujer / Hombre / Niños)—.
  Cada selector muestra únicamente lo que existe en esa colección, cuenta ya con
  el otro filtro aplicado y desaparece si no hay nada que elegir.
- El filtro queda en la dirección (`#/aretes?m=plata&l=mujer`), así que se puede
  compartir o guardar una vista concreta.

Dentro de cada colección las piezas van agrupadas por material y, dentro de
cada material, por sesión de fotos: el orden usa el color de fondo de cada
imagen, de modo que las fotos de la misma serie quedan juntas.

## Estructura

```
index.html                 Página única
assets/css/estilos.css     Estilos (base blanca, dorado del logo como acento)
assets/js/app.js           Vistas, filtros, rejilla y visor de imágenes
assets/img/                Logo y favicons
data/catalogo.json         Índice de las 360 piezas (lo genera el script)
catalogo/<tipo>/<línea>/   Imágenes en WebP + subcarpeta thumbs/ para la rejilla
tools/build_catalogo.py    Script que convierte, renombra y organiza las fotos
tools/clasificacion.py     Tipo, línea y material de cada foto
```

Tipos: `anillos`, `aretes`, `collares`, `pulseras`, `esclavas`, `tobilleras`,
`juegos`. Líneas: `mujer`, `hombre`, `ninos`. Materiales: `oro` (10K) y
`plata` (925).

## Las imágenes

Las fotos originales venían en dos ZIP con nombres tipo
`0103caad-3c9e-42b1-95f9-ffe40483b282.JPG`. El script las convierte a WebP en
dos tamaños y las renombra a `<tipo>-<línea>-<número>.webp`:

| Variante | Lado mayor | Calidad | Peso medio | Uso |
|---|---|---|---|---|
| `catalogo/.../thumbs/` | 640 px | 80 | ~24 KB | rejilla (carga diferida) |
| `catalogo/.../` | 1400 px | 86 | ~102 KB | visor ampliado |

Al abrir la página solo se descargan las miniaturas visibles, así que carga
rápido incluso con datos móviles.

El material sale de lo que dice la propia foto (`Oro 10K`, `plata italy 925`,
`PLATA FINA`). Si alguna pieza quedó mal clasificada, se corrige en
`tools/clasificacion.py` y se vuelve a generar el índice.

## Agregar o cambiar fotos

1. Copia los JPG nuevos a una carpeta.
2. Añade su clasificación en `tools/clasificacion.py`: el tipo y la línea en
   `CLASIFICACION` (`índice tipo/línea`) y, si es de plata, su identificador en
   `PLATA`.
3. Ejecuta:

```bash
pip install Pillow
python3 tools/build_catalogo.py --origen "carpeta-1" "carpeta-2"
```

El script regenera las carpetas de `catalogo/` y `data/catalogo.json`. Si solo
cambiaste la clasificación y no hay fotos nuevas, basta con
`python3 tools/build_catalogo.py --solo-datos`, que reescribe el índice sin
volver a comprimir las imágenes.

Las portadas de cada colección se eligen en `PORTADAS`, dentro de
`tools/build_catalogo.py`.

## Publicar en GitHub Pages

El flujo `.github/workflows/pages.yml` publica en cada push a `main` y, como
usa `configure-pages` con `enablement: true`, activa GitHub Pages por sí solo
la primera vez que corre.

Si la organización no permite que Actions active Pages, hazlo a mano en
**Settings → Pages** con cualquiera de estas dos opciones:

- **GitHub Actions** como origen (deja que el flujo publique).
- **Deploy from a branch**: rama `main`, carpeta `/ (root)`.

La página queda en `https://novawebstudio-hn.github.io/Joyeria-Alce/`.
