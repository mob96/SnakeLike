import libtcodpy as libtcod

#Handles rendering entities to the console

def render_all(con, entities, screen_width, screen_height):
	for e in entities:
		render_entity(con, e)
	
	libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

def render_entity(con, entity):
	libtcod.console_set_default_foreground(con, entity.colour)
	libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)
	
def clear_all(con, entities):
	for e in entities:
		clear_entity(con, e)

def clear_entity(con, entity):
	libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)

