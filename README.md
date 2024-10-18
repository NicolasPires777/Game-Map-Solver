# Game Map Solver 🎮🗺️

This project is a Python-based game simulation where a random sequence of numbers (1, 2, or 3) is generated to represent the "map" of a level. The objective is to create an algorithm that navigates through this map by **jumping**, **walking**, or **crouching**, and attempts to complete the level in the fewest possible tries.

## How it Works

- A random sequence is generated, where each number represents an obstacle or action:
  - **1**: Crouch
  - **2**: Walk
  - **3**: Jump
- The algorithm must navigate through the sequence and survive as long as possible by making the correct moves.
- If the algorithm "dies" (i.e., makes a wrong move), it saves the progress up to the furthest point reached and resumes from there in the next attempt.
- The goal is to complete the entire sequence (map) with the fewest attempts.

### Example Map

A generated sequence might look like this:  
1 3 2 2 1 3 2 2 3 3 1 2 1 2 3  

The algorithm must determine the correct moves to successfully navigate this map.

## Key Features

- **Random Map Generation**: Each time the game starts, a new sequence of numbers is generated to create a unique challenge.
- **Algorithm Efficiency**: The algorithm aims to minimize the number of attempts by saving progress and resuming from where it last "died."
- **Progress Tracking**: The furthest point reached in the sequence is saved, so that the algorithm remembers the path taken.




