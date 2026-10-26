# Parametric battery holder

This program makes a 3D battery holder with a grid of round cell openings. You can change the number of rows and columns, then save the model as a STEP file for CAD or an STL file for printing.

## How the model is made

The program uses build123d, a Python library for creating CAD models. It draws an outer rectangle, places circles inside it, and subtracts those circles from the rectangle. It then extrudes the remaining shape, which means giving the flat shape a height.

The default model has four rows and two columns. The openings are 18.5 mm wide, their centers are 19.5 mm apart, and the outside wall margin is 2 mm. The holder is 65.5 mm tall. Together, these settings make an eight-hole model that is 42 mm wide and 81 mm deep.

The `series` setting controls the rows and `parallel` controls the columns. These names only control the shape. The program does not design electrical connections between the cells.

## What kind of holder this makes

The holes go all the way through. The result is a spacer that keeps cells apart, rather than a closed box with a bottom or lid. Cell fit, insulation, material choice, heat, and how the cells stay in place still need physical design and testing.

## Try it

Use Python 3.11 or newer. Open a terminal in this project's folder and create a virtual environment. This keeps its packages separate from your other Python projects.

```sh
python -m venv .venv
```

On Windows, activate it with this command.

```sh
.venv\Scripts\activate
```

On macOS or Linux, use this command instead.

```sh
source .venv/bin/activate
```

Then install the packages the project needs.

```sh
python -m pip install -r requirements.txt
```

```sh
python battery_holder.py
python battery_holder.py --series 3 --parallel 2 --output holder.stl
```

The default output is `battery_holder.step`. You can change `--diameter`, `--height`, `--pitch`, and `--wall` to adjust the dimensions. Pitch is the distance between the centers of neighboring holes. It must be greater than the hole diameter.

## Tests

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

The tests check the dimensions and volume of the solid. They also save a STEP file and load it again to check the export. Fit with real cells has not been tested.
