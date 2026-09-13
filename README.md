# Joyería Alce — catálogo web

Catálogo estático de Joyería Alce: sin nombres ni precios de producto, solo las
fotos organizadas por tipo de pieza y línea (mujer, hombre, niños). Funciona en
móvil y escritorio y no necesita servidor: son archivos HTML, CSS, JS e imágenes.

## Estructura

```
index.html                 Página única
assets/css/estilos.css     Estilos (base blanca, dorado del logo como acento)
assets/js/app.js           Filtros, rejilla y visor de imágenes
assets/img/                Logo y favicons
data/catalogo.json         Índice de las 360 piezas (lo genera el script)
catalogo/<tipo>/<línea>/   Imágenes en WebP + subcarpeta thumbs/ para la rejilla
tools/build_catalogo.py    Script que convierte, renombra y organiza las fotos
tools/clasificacion.py     Clasificación de cada foto original
```

Tipos: `anillos`, `aretes`, `collares`, `pulseras`, `esclavas`, `tobilleras`,
`juegos`. Líneas: `mujer`, `hombre`, `ninos`.

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

## Agregar o cambiar fotos

1. Copia los JPG nuevos a una carpeta.
2. Añade su clasificación en `tools/clasificacion.py` (`índice tipo/línea`).
3. Ejecuta:

```bash
pip install Pillow
python3 tools/build_catalogo.py --origen "carpeta-1" "carpeta-2"
```

El script regenera las carpetas de `catalogo/` y `data/catalogo.json`.

## Publicar en GitHub Pages

En **Settings → Pages** hay dos opciones equivalentes:

- **Deploy from a branch**: rama `main`, carpeta `/ (root)`.
- **GitHub Actions**: usa el flujo incluido en `.github/workflows/pages.yml`,
  que publica en cada push a `main`.

La página queda en `https://<usuario>.github.io/Joyeria-Alce/`.
