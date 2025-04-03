
Happy simulating!

## Overview

The **Monty Hall problem** is a famous brain teaser based on a probability puzzle that originated from a game show scenario. In this problem, a contestant is presented with three doors. Behind one door is a prize (usually a car), and behind the other two are goats. The contestant picks one door, then the host (Monty Hall) opens one of the remaining doors, revealing a goat. The contestant is then given the choice to either stick with their original choice or switch to the other unopened door. The puzzle is to determine whether it's better to stick with the original choice or switch.

This simulation allows you to explore the Monty Hall problem by running multiple simulations and tracking the win rates of both strategies: **switching** doors versus **staying** with the original choice.

## How the Monty Hall Problem Works

1. **Initial Setup**: The contestant picks a door (let's say Door 1).
2. **Monty Opens a Door**: Monty, who knows which door has the prize, opens a door with a goat behind it (say Door 3).
3. **Decision**: The contestant is given the choice to switch to the remaining unopened door (Door 2) or stay with the original choice (Door 1).
4. **Outcome**: The contestant wins if the door they chose (either the original or the switched door) has the car behind it.

### The Key Insight:
It has been shown that the contestant has a **better chance of winning if they switch** doors. When the contestant switches, their chances of winning rise to **2/3**, whereas if they stay, their chances of winning remain at **1/3**. This counter-intuitive result is the core of the Monty Hall problem and the reason it's such a popular and perplexing puzzle.

## Why the Probability is Not 50/50:

At first glance, one might think that after the contestant makes their initial choice, Monty’s actions could make the game appear to be like a 50/50 situation as though the remaining two doors are equally likely to contain the car. However, this is not the case. The reason lies in **Monty's knowledge and behavior**.

### Monty Knows Where the Car Is:

In the Monty Hall problem, Monty is not a random actor. He **knows** where the car is located, and this knowledge significantly impacts the probability distribution of the remaining doors.

1. **The initial choice (before Monty opens any doors)**:
   When the contestant initially picks a door, there is a **1/3 chance** that they have selected the car (the winning door), and a **2/3 chance** that they have selected a goat (the losing door).

2. **Monty’s Action**:
   Monty then opens a door that **does not** have the car behind it. Crucially, he will **never** open the door that has the car. This is key to the puzzle. Monty’s action of revealing a goat behind one of the unchosen doors provides additional information to the contestant. Because Monty always reveals a goat, the probability distribution is affected.

   - If the contestant initially chose the **car door** (1/3 chance), Monty can open either of the remaining doors (both have goats), and the contestant's chances of winning if they switch are 0%. The contestant will lose if they switch.
   
   - If the contestant initially chose a **goat door** (2/3 chance), Monty is forced to open the other door that also has a goat. The only remaining door must have the car, so if the contestant switches, they will win.

## About the Program

This Python program simulates the Monty Hall game multiple times to demonstrate how switching versus staying affects the win rates. The user can choose whether to simulate the game with the **switch** strategy or the **stay** strategy. The program runs a large number of simulations (default: 1,000,000) and provides a real-time progress bar that shows the win/loss rates as the simulations progress.

### Features:
- Simulates multiple rounds of the Monty Hall game.
- Calculates the win rate for both the **switch** strategy and the **stay** strategy.
- Displays a progress bar that updates every 0.3 seconds with the current win/loss statistics.
- Allows you to adjust the number of simulations and the update interval for the progress bar.

### Key Constants:
- **`doors_count`**: The number of doors in the game (default: 3). This can be changed to simulate a different version of the problem with more doors.
- **`TOTAL_SIMULATIONS`**: The total number of game simulations to run (default: 1,000,000).
- **`PROGRESS_BAR_SEGMENTS`**: The number of segments in the progress bar (default: 50).
- **`PRINT_INTERVAL_SECONDS`**: The interval in seconds for updating the progress bar in the console (default: 0.3 seconds).

## How to Use the Program

1. **Run the Script**:
   - Simply execute the Python script. It will start by running the Monty Hall game and will display the progress in the console.
   
        for windows: 
            ```
            py monty_hall_simulation
            ```

        for linux or mac: 
            ```
            python3 monty_hall_simulation
            ```

2. **Simulate with the Stay Strategy**:
   - Change the line in the code that calls the `simulate_monty_hall()` function from `switch=True` to `switch=False` to simulate the scenario where the player does **not** switch doors.

3. **View the Results**:
   - After the program completes all simulations, it will display the final win rate for both strategies (switch vs. stay).

4. **Customize the Simulation**:
   - You can adjust the number of doors, the number of simulations, the progress bar segments, and the update interval for more detailed or faster simulations.

## Code Explanation

#### The `simulate_monty_hall(switch: bool)` Function
This function simulates one round of the Monty Hall game. It randomly places a car behind one of the doors, lets the player choose a door, and then simulates Monty's actions (opening doors). Depending on whether the player switches or stays, the function returns `True` (win) or `False` (loss).

#### The `display_progress(wins, losses, current_iteration, total_iterations)` Function
This function updates and displays the progress bar in the console. It shows the current win/loss rate and how many simulations have been completed so far, with a dynamic progress bar.

#### The `main()` Function
The main function runs the simulation for the specified number of iterations. It keeps track of the wins and losses, updates the progress bar at regular intervals, and displays the final win rate once all simulations are complete.

## Example Output

```
Starting Monty Hall Simulation...
Win Rate: 66.67%, Loss Rate: 33.33%, Progress: [ #######################........................ ] 500000/1000000 (50.00%)
Final Win Rate: 66.67%, Final Loss Rate: 33.33%
```

## How the Monty Hall Simulation Works

- In the simulation, **switching** doors leads to a win rate of approximately **66.67%**, while **staying** results in a win rate of around **33.33%**.
- The program runs a large number of simulations to show how these probabilities play out in practice.

## Conclusion

This simulation helps visualize the Monty Hall problem and provides insights into the probabilities at play. It highlights how seemingly counter-intuitive strategies (like switching doors) can result in better outcomes. By running multiple simulations, you can verify the probabilities and better understand the problem.

## Requirements

- Python 3.x
- Standard Python libraries: `random`, `time`, `datetime`

## License

This project is open-source. Feel free to use and modify it as you see fit!

---

Happy simulating!