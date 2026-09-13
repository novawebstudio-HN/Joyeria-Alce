#!/usr/bin/env python3
"""Convierte las fotos originales (JPG) a WebP, las renombra y las organiza
en carpetas por tipo de producto y genero. Ademas genera data/catalogo.json,
que es lo que consume la pagina.

    python3 tools/build_catalogo.py --origen "<carpeta zip 1>" "<carpeta zip 2>"

Con --solo-datos vuelve a escribir data/catalogo.json a partir de las imagenes
ya convertidas, sin volver a comprimir nada (util al corregir la clasificacion).
"""
import argparse
import colorsys
import json
import pathlib
import sys

from PIL import Image, ImageOps

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from clasificacion import cargar, cargar_materiales  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "catalogo"
DATA = RAIZ / "data"

# Lado mayor y calidad de cada variante.
FULL_MAX, FULL_Q = 1400, 86
THUMB_MAX, THUMB_Q = 640, 80

ETIQUETAS = {
    "anillos": "Anillos",
    "aretes": "Aretes",
    "collares": "Collares",
    "esclavas": "Esclavas",
    "juegos": "Juegos",
    "pulseras": "Pulseras",
    "tobilleras": "Tobilleras",
}
GENEROS = {"mujer": "Mujer", "hombre": "Hombre", "ninos": "Niños"}
MATERIALES = {"plata": "Plata 925", "oro": "Oro 10K"}
ORDEN_TIPOS = ["anillos", "aretes", "collares", "pulseras", "esclavas", "tobilleras", "juegos"]

# Foto que representa a cada coleccion en el inicio. Si un tipo no aparece aqui
# se usa su primera pieza.
PORTADAS = {
    "esclavas": "esclavas-hombre-007",
    "tobilleras": "tobilleras-mujer-007",
    "juegos": "juegos-mujer-002",
}
ORDEN_MATERIALES = ["plata", "oro"]


def guardar_webp(imagen, destino, lado_max, calidad):
    copia = imagen.copy()
    copia.thumbnail((lado_max, lado_max), Image.LANCZOS)
    destino.parent.mkdir(parents=True, exist_ok=True)
    copia.save(destino, "WEBP", quality=calidad, method=6)
    return copia.size


def firma_fondo(ruta):
    """Color medio del borde de la foto.

    Las piezas fotografiadas en la misma sesion comparten fondo (tarjeta, marmol,
    satin, plantas), asi que ordenar por este color deja juntas las series.
    """
    im = Image.open(ruta).convert("RGB").resize((64, 64))
    px = im.load()
    marco = [px[x, y] for x in range(64) for y in range(64)
             if x < 6 or y < 6 or x > 57 or y > 57]
    n = len(marco)
    rgb = [sum(p[i] for p in marco) / n / 255 for i in range(3)]
    return colorsys.rgb_to_hsv(*rgb)


def portada(tipo, piezas):
    elegida = PORTADAS.get(tipo)
    if elegida and any(p["id"] == elegida for p in piezas):
        return elegida
    del_tipo = [p for p in piezas if p["tipo"] == tipo]
    return del_tipo[0]["id"] if del_tipo else None


def clave_orden(pieza):
    tono, sat, val = pieza["_firma"]
    return (
        ORDEN_TIPOS.index(pieza["tipo"]),
        ORDEN_MATERIALES.index(pieza["material"]),
        round(sat * 10),
        -round(val * 12),
        round(tono * 24),
        pieza["id"],
    )


def convertir(origenes, mapa):
    originales = []
    for carpeta in origenes:
        originales += sorted(pathlib.Path(carpeta).glob("*.JPG"))
    if len(originales) != len(mapa):
        sys.exit(f"Se esperaban {len(mapa)} imagenes y se encontraron {len(originales)}")

    contadores = {}
    rutas = []
    for indice, origen in enumerate(originales):
        tipo, genero = mapa[indice]
        contadores[(tipo, genero)] = contadores.get((tipo, genero), 0) + 1
        nombre = f"{tipo}-{genero}-{contadores[(tipo, genero)]:03d}.webp"
        imagen = ImageOps.exif_transpose(Image.open(origen)).convert("RGB")
        carpeta = DESTINO / tipo / genero
        guardar_webp(imagen, carpeta / nombre, FULL_MAX, FULL_Q)
        guardar_webp(imagen, carpeta / "thumbs" / nombre, THUMB_MAX, THUMB_Q)
        rutas.append(carpeta / nombre)
    return rutas


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--origen", nargs="+", help="Carpetas con los JPG originales")
    parser.add_argument("--solo-datos", action="store_true",
                        help="Regenera data/catalogo.json sin volver a convertir imagenes")
    args = parser.parse_args()

    mapa = cargar()
    if args.solo_datos:
        rutas = sorted(p for p in DESTINO.rglob("*.webp") if p.parent.name != "thumbs")
    elif args.origen:
        rutas = convertir(args.origen, mapa)
    else:
        parser.error("indica --origen o --solo-datos")

    plata = cargar_materiales()
    piezas = []
    for ruta in rutas:
        tipo, genero = ruta.parent.parent.name, ruta.parent.name
        pid = ruta.stem
        with Image.open(ruta) as im:
            ancho, alto = im.size
        piezas.append({
            "id": pid,
            "tipo": tipo,
            "genero": genero,
            "material": "plata" if pid in plata else "oro",
            "full": f"catalogo/{tipo}/{genero}/{ruta.name}",
            "thumb": f"catalogo/{tipo}/{genero}/thumbs/{ruta.name}",
            "w": ancho,
            "h": alto,
            "_firma": firma_fondo(ruta.parent / "thumbs" / ruta.name),
        })

    piezas.sort(key=clave_orden)
    for pieza in piezas:
        del pieza["_firma"]

    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "catalogo.json").write_text(json.dumps({
        "tipos": [{"slug": t, "nombre": ETIQUETAS[t], "portada": portada(t, piezas)}
                  for t in ORDEN_TIPOS],
        "generos": [{"slug": g, "nombre": n} for g, n in GENEROS.items()],
        "materiales": [{"slug": m, "nombre": MATERIALES[m]} for m in ORDEN_MATERIALES],
        "piezas": piezas,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"{len(piezas)} piezas")
    for tipo in ORDEN_TIPOS:
        del_tipo = [p for p in piezas if p["tipo"] == tipo]
        detalle = ", ".join(
            f"{MATERIALES[m]} {sum(1 for p in del_tipo if p['material'] == m)}"
            for m in ORDEN_MATERIALES if any(p["material"] == m for p in del_tipo))
        print(f"  {ETIQUETAS[tipo]:11} {len(del_tipo):3}  ({detalle})")


if __name__ == "__main__":
    main()
