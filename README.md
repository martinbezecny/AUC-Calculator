# AUC Calculator

A simple GUI-based Python application to calculate the Area Under Curve (AUC) for up to 26 [𝑥, 𝑦] coordinates. Built with Tkinter for the GUI and NumPy for numerical integration.


## Features
- **GUI**: Enter up to 26 coordinate points [𝑥, 𝑦] for AUC calculation.
- **Data Sorting**: Ensures the x values are sorted from lowest to highest.
- **Error Handling**: Displays error messages for invalid input or insufficient data.

## Preview
![Screenshot of AUC Calculator](https://i.imgur.com/FgICjt2.png)

## Requirements
- Python 3.7+
- NumPy: Used for AUC calculations via numerical integration.
- CustomTkinter: Used for GUI.

## Installation
### Download executable for Windows
Download the .EXE file and run: TODO
___
### Clone git repository
- Clone the Repository
```
git clone https://github.com/martinbezecny/AUC-Calculator
cd AUC-Calculator
```
- Install Dependencies
```
pip install -r requirements.txt
```
- Run the Application
```
python main.py
```

## Usage
- **Input Coordinates**: Enter your [𝑥, 𝑦] coordinate values in the text fields labeled "Point 1" to "Point 26".
- **Calculate AUC**: Click the 'Calculate' button to calculate the AUC.
> Leave unused fields empty. Use decimal points (e.g., 1.5), not commas (e.g., 1,5).

## Task list
- [x] Update layout to fit lower DPI screens
- [x] Create a new executable for Win

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes! Contributions are welcomed.



© 2024 Martin Bezecný
