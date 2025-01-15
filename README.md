# coin-flip
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

A simple Python 3 script that prompts the user for a number and then simulates flipping a coin that many times. After all the flips are complete, it displays the result (Heads or Tails) along with a progress bar and the winning percentage.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)


## Features

- **User Input Validation**: Continually prompts until a valid (positive integer) input is provided.
- **Random Coin Flips**: Uses Python's `random` module to simulate fair coin flips.
- **Results Display**: Displays the final winning side (Heads or Tails) and the winning percentage as a graphical percentage bar.


## Prerequisites

- **Python 3.6+** (Recommended)
- A terminal or command prompt to run the script.


## Installation

1. Clone or download this repository.
   ```bash
     git clone https://github.com/your-username/coin-flip-script.git
   ```
2. Navigate into the project directory.
   ```bash
    cd coin-flip-script
   ```


## Usage

1. Run the script:
   ```bash
     python coin_flip.py
   ```
2. When prompted, enter a positive integer representing how many times you want to flip the coin.


3. The script will simulate that many flips and display:
  - A percentage bar indicating the winning side’s share of the flips.
  - The name of the winning side (Heads or Tails) and its percentage.


## Example

Below is an example session:
   ```bash
    Enter a number: 5
    
    ██████████████████████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 50%
    Heads Won By: 50% Out Of 100%
    
    --HEADS--
   ```
*(Your actual results may vary because of the randomness.)*


## License

This project is open-source and available under the MIT License.

[Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)

