# Snake Game

![Contributors](https://img.shields.io/github/contributors/nascho/react-calculator?style=plastic) ![Forks](https://img.shields.io/github/forks/nascho/react-calculator) ![Stars](https://img.shields.io/github/stars/nascho/react-calculator) ![Issues](https://img.shields.io/github/issues/nascho/react-calculator)


## Description 

This repository is for being used for a Snake Game using Python and PyGame and is part of a small out of hours project while attending Generation UK&I's AWS Re/Start programme.

It is a fully functioning application, please feel free to use it.


__Techologies Used__ 

As part of the project the technologies we settled on were:

![Python](https://img.shields.io/badge/-Python-blue?style=flat-square&logo=python&logoColor=white) ![Pygame](https://img.shields.io/badge/-Pygame-green?style=flat-square&logo=python&logoColor=white)


## Installation & Running Project

Please click the link below to copy the pathway for cloning the project and paste into your terminal:

```sh
   git clone https://github.com/nascho/snake_game.git
```

For Windows, once cloned please install the PyGame package:

```sh
    pip install pygame
```

For MacOS, once cloned please install the PyGame package:

```sh
    pip3 install pygame
```

For Windows, in the terminal run the following command to start the game:

```sh
    python main.py
```

For MacOS, in the terminal run the following command to start the game:

```sh
    python3 main.py
```

When the program starts a window will appear for you to interact with the game.

## Game Rules

1. **Objective**: 
   - Control the snake to collect food that appears randomly on the game screen.
   - Each time the snake eats food, it grows longer.

2. **Snake Movement**: 
   - Use the arrow keys on your keyboard to control the direction of the snake:
     - `←` Move Left
     - `→` Move Right
     - `↑` Move Up
     - `↓` Move Down
   - The snake can move in any of the four directions at any time.

3. **Game Over Conditions**: 
   - The game ends if the snake runs into its own body.
   
4. **Food**:
   - The food appears at random locations on the screen. The snake grows longer each time it eats the food.

5. **Wrapping Around**:
   - The snake can pass through the screen edges and reappear on the opposite side of the screen.

## Future Development

In the future I would like to look at adding different levels and with each increase in level would also increase the speed of the snake.
<br>
In the meantime you can manually increase the speed by increasing the number in **_FRAME_RATE_** line 119.

