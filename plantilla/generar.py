"""Uso: python3 generar.py ruta/a/datos.json  ->  crea web/index.html junto al json."""
import json, sys, pathlib
from jinja2 import Environment, FileSystemLoader
UI = {
 "cta":{"es":"Escribir por WhatsApp","en":"Message on WhatsApp","de":"Per WhatsApp schreiben","fr":"Écrire sur WhatsApp"},
 "see":{"es":"Ver la oferta","en":"See what we offer","de":"Angebot ansehen","fr":"Voir l'offre"},
 "visit":{"es":"Dónde estamos","en":"Find us","de":"So finden Sie uns","fr":"Nous trouver"},
 "map":{"es":"Abrir en Google Maps","en":"Open in Google Maps","de":"In Google Maps öffnen","fr":"Ouvrir dans Google Maps"},
 "reply":{"es":"Te respondemos el mismo día.","en":"We reply the same day.","de":"Wir antworten am selben Tag.","fr":"Nous répondons le jour même."},
 "demo":{"es":"Web de demostración creada por Atalaya Studio","en":"Demo site by Atalaya Studio","de":"Demo-Website von Atalaya Studio","fr":"Site de démonstration par Atalaya Studio"},
}
src = pathlib.Path(sys.argv[1]).resolve()
d = json.loads(src.read_text(encoding="utf-8"))
env = Environment(loader=FileSystemLoader(pathlib.Path(__file__).parent), autoescape=True)
html = env.get_template("plantilla.html").render(**d, ui=UI)
out = src.parent / "web"; out.mkdir(exist_ok=True)
(out / "index.html").write_text(html, encoding="utf-8")
print("creado:", out / "index.html")
