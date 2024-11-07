# AUC Calculator

A simple GUI-based Python application to calculate the Area Under Curve (AUC) for up to 26 [𝑥, 𝑦] coordinates. Built with Tkinter for the GUI and NumPy for numerical integration.


## Features
- **GUI**: Enter up to 26 coordinate points [𝑥, 𝑦] for AUC calculation.
- **Data Sorting**: Ensures the x values are sorted from lowest to highest.
- **Error Handling**: Displays error messages for invalid input or insufficient data.

## Preview
![Screenshot of AUC Calculator](https://i.imgur.com/Ve2yALd.png)

## Requirements
- Python 3.7+
- NumPy: Used for AUC calculations via numerical integration.

## Installation
- Clone the Repository
```
git clone https://github.com/martinbezecny/AUC-Calculator
cd AUC-Calculator
```
- Install Dependencies
```
pip install numpy
```
- Run the Application
```
python main.py
```

## Usage
- **Input Coordinates**: Enter your [𝑥, 𝑦] coordinate values in the text fields labeled "Point 1" to "Point 26".
- **Calculate AUC**: Click the 'Calculate' button to calculate the AUC.
> Leave unused fields empty. Use decimal points (e.g., 1.5), not commas (e.g., 1,5).

## Compiling to a Windows Executable
If you’re on Linux or another OS but want to create a Windows executable:

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes! Contributions are welcomed.



© 2024 Martin Bezecný
