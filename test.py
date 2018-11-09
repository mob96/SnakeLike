import libtcodpy as libtcod
from input_handler import handle_keys
from entity import Entity
from renderer import render_all, clear_all

def main():
	screen_width = 20
	screen_height = 20
	
	libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
	libtcod.console_init_root(screen_width, screen_height, 'TEST RL', False)
	
	con = libtcod.console_new(screen_width, screen_height)
	key = libtcod.Key()
	mouse = libtcod.Mouse()
	
	player = Entity(5, 5, '@', libtcod.red)
	oracle = Entity(2, 2, '0', libtcod.blue)
	
	entities = [player, oracle]
	
	while not libtcod.console_is_window_closed():
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
		
		render_all(con, entities, screen_width, screen_height)
		libtcod.console_flush()
		clear_all(con, entities)
		
		
		input = handle_keys(key)
		
		move = input.get('move')
		exit = input.get('exit')
		fullscreen = input.get('fullscreen')
		
		if move:
			x, y = move
			player.move(x, y);
		
		if exit:
			return True
			
		if fullscreen:
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
			

if __name__ == '__main__':
	main();