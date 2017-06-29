""" Spork engine.

A Rogue-like game engine written in Python 3.

"""

import tdl


class GameObject(object):  # TODO: Add tests
    """A generic object: player, npc, items, stairs, etc.

    All objects are represented by a character on screen.

    """
    def __init__(self, x_coordinate, y_coordinate, char, color):  # TODO: Add tests
        self.x = x_coordinate
        self.y = y_coordinate
        self.char = char
        self.color = color

    def move(self, distance_x, distance_y):  # TODO: Add tests
        """Move object by the given distance, unless new position is blocked.

        """
        if not game_map[self.x + distance_x][self.y + distance_y].blocked:
            self.x += distance_x
            self.y += distance_y

    def draw(self):  # TODO: Add tests
        """Draw the character that represents the object at position.

        """
        console.draw_char(self.x, self.y, self.char, self.color)

    def clear(self):  # TODO: Add tests
        """Remove the character representing the object.

        """
        console.draw_char(self.x, self.y, ' ', self.color, bg=None)


class Tile(object):  # TODO: Add tests
    """Map tiles and their properties.

    """
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked

        # By default, if a tile is blocked, it also blocks sight:
        if block_sight is None:
            block_sight = blocked
        self.block_sight = block_sight


def make_map():  # TODO: Add tests
    """Create the game map.

    """
    global game_map

    # Populate the map with unblocked tiles.
    game_map = [[Tile(False) for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

    # For testing purposes:
    game_map[30][22].blocked = True
    game_map[30][22].block_sight = True
    game_map[50][22].blocked = True
    game_map[50][22].block_sight = True


def render_all():  # TODO: Add tests
    """Draws all game objects and the game map to screen.

    """
    # Draw all game objects.
    for obj in objects:
        obj.draw()

    # Draw the map.
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            wall = game_map[x][y].block_sight
            if wall:
                console.draw_char(x, y, None, fg=None, bg=color_dark_wall)
            else:
                console.draw_char(x, y, None, fg=None, bg=color_dark_ground)

    root.blit(console, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)


def handle_keys(realtime):  # TODO: Add tests
    """Handle user input.

    Alt+Enter toggles full-screen mode.
    Escape exits the game.
    Arrow keys move the player character.

    """
    global player_x, player_y

    if realtime:
        keypress = False
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                keypress = True
        if not keypress:
            return
    else:
        user_input = tdl.event.key_wait()

    if user_input.key == 'ENTER' and user_input.alt:
        tdl.set_fullscreen(not tdl.get_fullscreen())

    elif user_input.key == 'ESCAPE':
        return True

    if user_input.key == 'UP':
        player.move(0, -1)

    elif user_input.key == 'DOWN':
        player.move(0, 1)

    elif user_input.key == 'LEFT':
        player.move(-1, 0)

    elif user_input.key == 'RIGHT':
        player.move(1, 0)

# Game initialization.

# Window size.
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

# Map size and attributes.
MAP_WIDTH = 80
MAP_HEIGHT = 45
color_dark_wall = (0, 0, 100)
color_dark_ground = (50, 50, 150)

# Real-time or turn based.
REALTIME = False
LIMIT_FPS = 20

tdl.set_font('arial10x10.png', greyscale=True, altLayout=True)
root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Spork", fullscreen=False)
tdl.setFPS(LIMIT_FPS)
console = tdl.Console(SCREEN_WIDTH, SCREEN_HEIGHT)

# Create player and npc objects, and add them to a list of objects.
player = GameObject(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, '@', (255, 255, 255))
npc = GameObject(SCREEN_WIDTH//2 - 5, SCREEN_HEIGHT//2, '@', (255, 255, 0))
objects = [npc, player]

# Generate the game map.
make_map()

# Main loop
while not tdl.event.is_window_closed():
    render_all()
    tdl.flush()

    # Remove all objects from old location before they move.
    for obj in objects:
        obj.clear()

    exit_game = handle_keys(realtime=True)
    if exit_game:
        break
