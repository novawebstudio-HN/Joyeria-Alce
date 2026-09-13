#!/usr/bin/env python3
"""Convierte las fotos originales (JPG) a WebP, las renombra y las organiza
en carpetas por tipo de producto y genero. Ademas genera data/catalogo.json,
que es lo que consume la pagina.

Uso:
    python3 tools/build_catalogo.py --origen "<carpeta zip 1>" "<carpeta zip 2>"
"""
import argparse
import json
import pathlib
import sys

from PIL import Image, ImageOps

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from clasificacion import cargar  # noqa: E402

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
ORDEN_TIPOS = ["anillos", "aretes", "collares", "pulseras", "esclavas", "tobilleras", "juegos"]


def guardar_webp(imagen, destino, lado_max, calidad):
    copia = imagen.copy()
    copia.thumbnail((lado_max, lado_max), Image.LANCZOS)
    destino.parent.mkdir(parents=True, exist_ok=True)
    copia.save(destino, "WEBP", quality=calidad, method=6)
    return copia.size


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--origen", nargs="+", required=True,
                        help="Carpetas con los JPG originales, en el orden de la clasificacion")
    args = parser.parse_args()

    originales = []
    for carpeta in args.origen:
        originales += sorted(pathlib.Path(carpeta).glob("*.JPG"))

    mapa = cargar()
    if len(originales) != len(mapa):
        sys.exit(f"Se esperaban {len(mapa)} imagenes y se encontraron {len(originales)}")

    contadores = {}
    piezas = []
    for indice, origen in enumerate(originales):
        tipo, genero = mapa[indice]
        clave = (tipo, genero)
        contadores[clave] = contadores.get(clave, 0) + 1
        nombre = f"{tipo}-{genero}-{contadores[clave]:03d}.webp"

        imagen = ImageOps.exif_transpose(Image.open(origen)).convert("RGB")
        carpeta = DESTINO / tipo / genero
        ancho, alto = guardar_webp(imagen, carpeta / nombre, FULL_MAX, FULL_Q)
        guardar_webp(imagen, carpeta / "thumbs" / nombre, THUMB_MAX, THUMB_Q)

        piezas.append({
            "id": nombre[:-5],
            "tipo": tipo,
            "genero": genero,
            "full": f"catalogo/{tipo}/{genero}/{nombre}",
            "thumb": f"catalogo/{tipo}/{genero}/thumbs/{nombre}",
            "w": ancho,
            "h": alto,
        })

    piezas.sort(key=lambda p: (ORDEN_TIPOS.index(p["tipo"]), p["genero"], p["id"]))

    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "catalogo.json").write_text(json.dumps({
        "tipos": [{"slug": t, "nombre": ETIQUETAS[t]} for t in ORDEN_TIPOS],
        "generos": [{"slug": g, "nombre": n} for g, n in GENEROS.items()],
        "piezas": piezas,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"{len(piezas)} piezas procesadas")
    for clave in sorted(contadores):
        print(f"  {clave[0]}/{clave[1]}: {contadores[clave]}")


if __name__ == "__main__":
    main()
