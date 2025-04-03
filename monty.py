from math import remainder
import random
from time import sleep
from datetime import datetime

# Constants
doors_count = 3  # Number of doors in the game (minimum 3) (e.g., 3, 100, etc.)
TOTAL_SIMULATIONS = 1000000  # Number of times the game will be played
PROGRESS_BAR_SEGMENTS = 50  # Number of segments in the progress bar
PRINT_INTERVAL_SECONDS = 0.3  # Interval for updating progress bar


def simulate_monty_hall(switch: bool) -> bool:
    """
    Simulates one round of the Monty Hall game.

    Args:
        switch (bool): Whether the player switches their choice.

    Returns:
        bool: True if the player wins, False otherwise.
    """
    # Randomly place the car behind one door
    door_with_car = random.randint(0, doors_count - 1)

    # Player makes an initial choice
    player_choice = random.randint(0, doors_count - 1)

    # Monty opens all doors without the car. If the player's choice is correct, Monty opens every door except one random door.
    remaining_one_door = door_with_car if player_choice != door_with_car else 0
    if remaining_one_door == player_choice:
        remaining_one_door = 1

    # If the player switches, they choose the remaining unopened door
    if switch:
        player_choice = remaining_one_door

    # Return True if the player's final choice is the car door
    return player_choice == door_with_car


def display_progress(
    wins: int, losses: int, current_iteration: int, total_iterations: int
):
    """
    Displays a progress bar with current win/loss rates.

    Args:
        wins (int): Number of wins so far.
        losses (int): Number of losses so far.
        current_iteration (int): Current iteration number.
        total_iterations (int): Total number of simulations.
    """
    progress_percentage = current_iteration / total_iterations
    completed_segments = int(progress_percentage * PROGRESS_BAR_SEGMENTS)
    remaining_segments = PROGRESS_BAR_SEGMENTS - completed_segments
    progress_bar = "#" * completed_segments + "." * remaining_segments

    win_rate = (wins / current_iteration) * 100
    loss_rate = (losses / current_iteration) * 100

    print(
        f"Win Rate: {win_rate:.2f}%, Loss Rate: {loss_rate:.2f}%, Progress: [ {progress_bar} ] "
        f"{current_iteration}/{total_iterations} ({progress_percentage * 100:.2f}%)",
        end="\r",
    )


def main():
    """
    Main function to run the Monty Hall simulation.
    """
    wins = 0
    losses = 0
    last_print_time = datetime.now().timestamp()

    print("Starting Monty Hall Simulation...")

    for i in range(TOTAL_SIMULATIONS):
        if simulate_monty_hall(
            switch=True
        ):  # Change switch=True to False to test "stay" strategy
            wins += 1
        else:
            losses += 1

        # Update progress bar periodically
        current_time = datetime.now().timestamp()
        if current_time - last_print_time >= PRINT_INTERVAL_SECONDS:
            display_progress(wins, losses, i + 1, TOTAL_SIMULATIONS)
            last_print_time = current_time

    # Final stats and progress bar update
    display_progress(wins, losses, TOTAL_SIMULATIONS, TOTAL_SIMULATIONS)

    print(
        f"\nFinal Win Rate: {wins / TOTAL_SIMULATIONS * 100:.2f}%, "
        f"Final Loss Rate: {losses / TOTAL_SIMULATIONS * 100:.2f}%"
    )


if __name__ == "__main__":
    main()
