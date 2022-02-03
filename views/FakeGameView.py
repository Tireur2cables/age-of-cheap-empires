# Imports
import arcade
import random

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = .25
COIN_COUNT = 50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Age Of Cheap Empire"

class FakeGameView(arcade.View):
	""" Our custom Window Class"""

	def __init__(self, ressources_list, nbIA, isPlayer):
		""" Initializer """
		# Call the parent class initializer
		super().__init__()

		self.ressources_list = ressources_list
		self.nbIA = nbIA

		# Variables that will hold sprite lists
		self.player_list = None
		self.coin_list = None

		# Set up the player info
		self.player_sprite = None
		self.score = 0

	def setup(self) :
		for b in self.ressources_list :
			print("ressource 1 :", b.child.text)
		print("nb ia :", self.nbIA)

	def on_show(self):
		""" Set up the game and initialize the variables. """
		arcade.set_background_color(arcade.color.AMAZON)

		# Don't show the mouse cursor
		self.window.set_mouse_visible(False)

		# Sprite lists
		self.player_list = arcade.SpriteList()
		self.coin_list = arcade.SpriteList()

		# Score
		self.score = 0

		# Set up the player
		# Character image from kenney.nl
		self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
		self.player_sprite.center_x = 50
		self.player_sprite.center_y = 50
		self.player_list.append(self.player_sprite)

		# Create the coins
		for i in range(COIN_COUNT):

			# Create the coin instance
			# Coin image from kenney.nl
			coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

			# Position the coin
			coin.center_x = random.randrange(SCREEN_WIDTH)
			coin.center_y = random.randrange(SCREEN_HEIGHT)

			# Add the coin to the lists
			self.coin_list.append(coin)

	def on_draw(self):
		""" Draw everything """
		arcade.start_render()
		self.coin_list.draw()
		self.player_list.draw()

		# Put the text on the screen.
		output = f"Score: {self.score}"
		arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

	def on_mouse_motion(self, x, y, dx, dy):
		""" Handle Mouse Motion """

		# Move the center of the player sprite to match the mouse x, y
		self.player_sprite.center_x = x
		self.player_sprite.center_y = y

	def on_update(self, delta_time):
		""" Movement and game logic """

		# Call update on all sprites (The sprites don't do much in this
		# example though.)
		self.coin_list.update()

		# Generate a list of all sprites that collided with the player.
		coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

		# Loop through each colliding sprite, remove it, and add to the score.
		for coin in coins_hit_list:
			coin.remove_from_sprite_lists()
			self.score += 1
