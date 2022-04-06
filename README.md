# PyNoughtAndCrosses

Implementation of the famous **Tic-Tac-Toe** game in python.

## Table of Content 

## Overview

## Detailed Description

### Tic-Tac-Toe rules

The rules are explain on wikipedia, you can check [here](https://en.wikipedia.org/wiki/Tic-tac-toe)

### Code Structure
I do this projet with an **oriented-object language** so I will use this structure in my project.

#### The board
The board will be represented by an object `Board`.

*Attributes*

| Attribute Name | Role                | Type   |
|----------------|---------------------|--------|
| `content`      | Content of the grid | `list` |

*Methods*

| Method Name   | Role                                                                                     | Args                    |
|---------------|------------------------------------------------------------------------------------------|-------------------------|
| `add_symbol`  | Add a symbol on the board                                                                | NO ARGS                 |
| `__str__`     | When we call the function `print`                                                        | NO ARGS                 |
| `line(n)`     | Return a `tuple` of the line number n                                                    | `n` : index of the line |
| `column(n)`   | Return a `tuple` of the column number n                                                  | `n` : index of the line |
| `diagonal(n)` | Return a `tuple` of the diagonal number n (there are 2, the first start from the (0, 0)) | `n` : index of the line |

### The Game

A game will be represented by the object `Game`

*Attributes*

| Attribute Name | Role               | Type                   |
|----------------|--------------------|------------------------|
| `board`        | to stock the board | `Board`                |
| `player`       | player who plays   | `str` : `"X"` or `"O"` |

*Methods*

| Method Name    | Role                                                      | Args                    |
|----------------|-----------------------------------------------------------|-------------------------|
| `run`          | To run the game (the main method it calls others methods) | NO ARGS                 |
| `__ask_player` | demands the cell which the player wants to put his symbol | NO ARGS                 |
| `__is_won`     | tests if the game is won                                  | `n` : index of the line |



