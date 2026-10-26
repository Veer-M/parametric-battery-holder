# Parametric battery holder

This generates a rectangular holder with a grid of cylindrical cell openings. Change the series and parallel counts to export a different STEP model or STL.

## Run it

Use Python 3.11 or newer. Run these commands from this repository's folder.

```sh
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
# source .venv/bin/activate
python -m pip install -r requirements.txt
```

```sh
python battery_holder.py
python battery_holder.py --series 3 --parallel 2 --output holder.stl
```

## How it works and current limits

All dimensions are in millimeters. Defaults produce an eight-hole 42 x 81 x 65.5 mm holder, with 18.5 mm openings on a 19.5 mm pitch and 2 mm outer margins. The holes pass all the way through, matching the supplied sketch; this is a cell spacer, not a closed enclosure. Counts describe geometry, not electrical wiring. Material choice, fit, insulation, heat, and cell retention need separate physical design and testing.

## Tests

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Tests check the solid dimensions and volume, then export and reload a STEP file. Physical cell fit has not been tested.
