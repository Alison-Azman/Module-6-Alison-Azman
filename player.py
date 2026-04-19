import random
from turtle import Turtle, Screen
from player import Player
from truck import Truck
from scorboard import Scoreboard
import random

# --- HOT PINKS & FUSCHIAS (The "Power" Colors) ---
truck_palette = [ '#ff00ff', '#ff1aff', '#ff33ff', '#ff4dff', '#ff66ff', '#ff80ff', # High-energy Magentas
    '#ff00cc', '#ff0099', '#ff0066', '#ff1493', # Deep Pinks & DeepPink

    # --- COTTON CANDY & BUBBLEGUM PINKS ---
    '#ff66b2', '#ff80bf', '#ff99cc', '#ffb3d9', '#ffcce6', '#ffe6f2', # Soft & Sugary

    # --- PEACHY PINKS & CORALS ---
    '#ff4d4d', '#ff6666', '#ff8080', '#ff9999', # Warm "Strawberry" tones
    '#ff7f50', '#ff8c69', '#ffa07a', '#ffb3a1', # Coral & Salmon

    # --- BRIGHT PEACH & SUNSET ORANGE ---
    '#ffcc99', '#ffd9b3', '#ffe6cc', '#fff2e6', # Creamy Oranges

    # --- ELECTRIC & LEMON YELLOWS ---
    '#ffff00', '#ffff33', '#ffff66', '#ffff99', # Neon Yellows
    '#fffacd', '#fff5b3', '#fff099', '#ffeb80', # Lemon Chiffon tones

    # --- MINT & SOFT AQUAS ---
    '#e0ffff', '#b2ffff', '#80ffff', '#4dffff', # Icy Cyans
    '#98fb98', '#afffaf', '#c6ffc6', '#ddffdd', # Sweet Mints

    # --- PERIWINKLE & LAVENDER ---
    '#e6e6ff', '#ccccff', '#b2b2ff', '#9999ff', # Soft Purples
    '#d8b2ff', '#cc99ff', '#bf80ff', '#b266ff', # Sugary Lilac

    # --- VIVID VIOLETS & ORCHIDS ---
    '#a64dff', '#9933ff', '#8c1aff', '#8000ff', # Intense Purple pop
    '#da70d6', '#ee82ee', '#ff82ff', '#ffb3ff'  # Orchids & Bright Violet
]


screen = Screen()
screen.setup(width=700, height= 600)
screen.bgcolor("#09814a")
screen.title("Turtle Crossing")
screen.tracer(0)


player = Player()
scorboard = Scoreboard()

truck_lanes =[-200, -100, 0, 100, 200]
trucks =[]

for lane in truck_lanes:
    truck = Truck(
        x = random.randint(-300, 300),
        y = lane,
        speed = random.uniform(0.3, 0.7),
        color = random.choice(truck_palette)

    )
    trucks.append(truck)

screen.listen()

screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")
screen.onkey(player.move_left,"Left")
screen.onkey(player.move_right,"Right")


game_is_on = True
while game_is_on:
    screen.update()

    for truck in trucks:
        truck.move()

screen.exitonclick()