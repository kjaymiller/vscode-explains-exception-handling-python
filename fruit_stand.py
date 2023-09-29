from rich.console import Console

console = Console()


inventory = {
    "apples": {
        "qty": 3,
        "price": 1.00,
    },
    "oranges": {
        "qty": 5,
        "price": 1.25,
    },
    "lemons": {
        "qty": 5,
        "price": 0.75,
    },
    "watermelons": {
        "qty": 5,
        "price": 3.00,
    },
}

def take_fruit(fruit: str, qty: int=1) -> float:
    """reduce the amount of fruit in the inventory"""
    # check_fruit(fruit)

    if inventory[fruit]["qty"] >= qty:
        inventory[fruit]["qty"] -= qty 
        console.print(f"Sold [blue]{qty}[/blue] [green]{fruit}[/green]")
        return inventory[fruit]["price"] * qty
    else:
        raise ValueError(f"Not enough {fruit}({inventory[fruit]['qty']})")