# SYSTEMMEDIA Typeface Concept

Eine futuristische Display-Schrift im Stil der gelieferten SYSTEMMEDIA-Vorlage.

## Dateien

- `index.html` - interaktive Vorschau mit Mehrzeilen-Eingabe und Export
- `systemmedia-typeface.js` - vektorbasierte Glyphen A-Z, 0-9 und einfache Zeichen
- `layer-font-demo.html` - Demo fuer echte Layer-Fonts
- `build_layer_fonts.py` - Generator fuer TTF/WOFF/WOFF2 Layer-Fonts
- `dist/fonts/` - fertige Font-Dateien
- `dist/systemmedia-layer-fonts.css` - CSS fuer Web-Einbindung

## Nutzung

Oeffne `index.html` im Browser. Der Text im Eingabefeld wird als SYSTEMMEDIA-Stil gerendert:

- schwarzer Aussenstrich
- weisser Innenkanal
- cyanfarbene Akzentlinie
- abgerundete, technische Buchstabenformen
- Zeilenumbrueche
- Ausrichtung links, zentriert oder rechts
- Export als SVG, PNG-Bild und PDF

Die Glyphen sind als SVG-Pfade aufgebaut und lassen sich in `systemmedia-typeface.js` weiter verfeinern.

## Layer-Fonts

Das Font-Paket besteht aus drei Fonts mit identischen Metriken:

- `SYSTEMMEDIA-Outer` - schwarze Aussenform
- `SYSTEMMEDIA-Channel` - weisser Innenkanal
- `SYSTEMMEDIA-Accent` - cyanfarbene Akzentlinie

Die Fonts liegen als `.ttf`, `.woff` und `.woff2` in `dist/fonts/`.

Zusatzlich sind zwei direkt auswaehlbare Fonts enthalten:

- `SYSTEMMEDIA-ThreeLine` - ein einfarbiger 3-Linien-Font
- `SYSTEMMEDIA-Color` - ein mehrfarbiger Color-Font mit COLR/CPAL Tabellen

Hinweis: `SYSTEMMEDIA-Color` wird nicht von allen Programmen farbig angezeigt. Browser und moderne Designprogramme koennen COLR/CPAL oft darstellen; andere Programme zeigen nur die Fallback-Kontur.

Oeffne `layer-font-demo.html`, um die echte Font-Version mit allen drei Ebenen zu testen.

Fuer Websites kann `dist/systemmedia-layer-fonts.css` eingebunden werden. Der Text wird dreimal uebereinander gesetzt:

```html
<span class="systemmedia-layer-text">
  <span class="outer">SYSTEMMEDIA</span>
  <span class="channel">SYSTEMMEDIA</span>
  <span class="accent">SYSTEMMEDIA</span>
</span>
```

<!-- SYSTEMMEDIA_LEGAL_START -->
## Rechtliche Hinweise

- Impressum: https://systemmedia.de/impressum/
- Datenschutz / DSGVO-Hinweise: https://systemmedia.de/datenschutz/
- Nutzungsbedingungen und Haftungsausschluss: https://systemmedia.de/nutzungsbedingungen/

Dieses Repository enthält, sofern nicht ausdrücklich anders gekennzeichnet, Test-, Entwicklungs-, Demonstrations- oder Evaluierungsinhalte. Nutzung auf eigene Verantwortung.

Soweit eine `LICENSE`-Datei vorhanden ist, gelten die dort genannten Lizenzbedingungen für die eingeräumten Nutzungsrechte. Ergänzend gelten die Status-, Gewährleistungs- und Haftungshinweise in `LEGAL.md`.
<!-- SYSTEMMEDIA_LEGAL_END -->
