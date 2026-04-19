import random
from turtle import Turtle
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

class Truck(Turtle):
    def __init__(self, x, y, speed, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.speed_value = speed

    def move(self):
        self.goto(self.xcor()- self.speed_value,
                  self.ycor())

        if self.xcor() < -340 :
            self.goto(random.randint(320,500),
                      self.ycor())
            self.color(random.choice(truck_palette))
            self.speed_value = random.uniform(0.2, 0.4)