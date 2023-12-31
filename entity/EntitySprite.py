from arcade import Sprite


#   ______           _     _   _              _____                  _   _
#  |  ____|         | |   (_) | |            / ____|                (_) | |
#  | |__     _ __   | |_   _  | |_   _   _  | (___    _ __    _ __   _  | |_    ___
#  |  __|   | '_ \  | __| | | | __| | | | |  \___ \  | '_ \  | '__| | | | __|  / _ \
#  | |____  | | | | | |_  | | | |_  | |_| |  ____) | | |_) | | |    | | | |_  |  __/
#  |______| |_| |_|  \__| |_|  \__|  \__, | |_____/  | .__/  |_|    |_|  \__|  \___|
#                                     __/ |          | |
#                                    |___/           |_|


# Wrapper for arcade.Sprite that enables us to access the entity from the sprite.
class EntitySprite(Sprite):

	def __init__(self, entity, sprite_data, hit_box_algorithm):
		super().__init__(filename=sprite_data.file, scale=sprite_data.scale, center_x=entity.iso_position.x + sprite_data.x_offset, center_y=entity.iso_position.y + sprite_data.y_offset, hit_box_algorithm=hit_box_algorithm)
		self.sprite_data = sprite_data
		self.entity = entity
		self.hit_box_algorithm = hit_box_algorithm

	def __getstate__(self):
		return self.sprite_data, self.entity, self.hit_box_algorithm, self.entity.iso_position

	def __setstate__(self, data):
		self.sprite_data, self.entity, self.hit_box_algorithm, self.entity.iso_position = data
		super().__init__(filename=self.sprite_data.file, scale=self.sprite_data.scale, center_x=self.entity.iso_position.x + self.sprite_data.x_offset, center_y=self.entity.iso_position.y + self.sprite_data.y_offset, hit_box_algorithm=self.hit_box_algorithm)

	def update(self):
		self.center_x = self.entity.iso_position.x + self.sprite_data.x_offset
		self.center_y = self.entity.iso_position.y + self.sprite_data.y_offset
