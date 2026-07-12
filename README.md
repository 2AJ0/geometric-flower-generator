# Geometric Flower Generator

A beautiful, interactive desktop application that generates mesmerizing, spirograph-like geometric flowers and pursuit curves using Python's `turtle` and `tkinter` libraries.

![Geometric Flower Generator](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Pursuit_curve.svg/300px-Pursuit_curve.svg.png) <!-- Example image placeholder -->

*Created by AntiGravity*

## Features

- **Polished Unified GUI**: All controls and graphics are embedded in a single, easy-to-use window.
- **Dynamic Pursuit Curve Math**: Automatically scales the polygons so they perfectly nest inside each other, creating stunning floral illusions.
- **Manual Overrides**: Toggle automatic scaling off to experiment with your own size multipliers (e.g., `0.92`).
- **Color Wheel Integration**: Select your own custom color palettes using your system's native color picker. The app loops through your chosen colors for each nested shape.
- **Instant Rendering**: Highly optimized drawing logic allows for instant regeneration of complex, hundreds-of-shapes flowers.

## Installation

1. Ensure you have Python 3 installed.
2. Clone this repository or download `geometric_flowers.py`.
3. `turtle` and `tkinter` are built into the standard Python library, so no extra dependencies are needed!

## How to Run

Open your terminal or command prompt and run:

```bash
python3 geometric_flowers.py
```

## Example Inputs

Try out these combinations in the Control Panel to get started:

### 1. The Classic Heptagon Rose
- **Number of Sides**: 7
- **Number of Shapes**: 45
- **Rotation Angle**: 8
- **Auto Scale**: Checked
- **Colors**: Gold, DarkOrange (Add multiple colors)

### 2. Triangle Star-Flower
- **Number of Sides**: 3
- **Number of Shapes**: 60
- **Rotation Angle**: 12
- **Auto Scale**: Checked
- **Colors**: Cyan, Magenta, Yellow

### 3. Disconnected Spiral Illusion
- **Number of Sides**: 6
- **Number of Shapes**: 40
- **Rotation Angle**: 15
- **Auto Scale**: Unchecked
- **Size Multiplier**: 0.90
- **Colors**: Red, Blue, White

## Usage Notes

- Click **Generate Flower** to draw.
- You can change parameters and hit **Generate Flower** again at any time to instantly clear the canvas and see your new design!
- If the rotation angle is too large for the pursuit curve math (e.g., trying to rotate a square by 90 degrees), the app will warn you and use a safe fallback size multiplier.
