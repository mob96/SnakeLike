import libtcodpy as libtcod
from input_handler import handle_keys
from entity import Entity
from renderer import render_all, clear_all
from snake import Snake
from apple import Apple

#Handles set up and the main game loop

def main():
	#Initialise some game variables/objects and the libtcod console
	screen_width = 16
	screen_height = 16
	fps_limit = 60
	
	libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
	libtcod.console_init_root(screen_width, screen_height, 'Snake', False)
	libtcod.sys_set_fps(fps_limit)
	
	con = libtcod.console_new(screen_width, screen_height)
	key = libtcod.Key()
	mouse = libtcod.Mouse()
	apple = Apple('A', libtcod.Color(200, 20, 20), screen_width, screen_height)
	snake = Snake(int(screen_width/2), int(screen_height/2), 'S', libtcod.Color(20, 200, 20), 1, fps_limit, apple, screen_width, screen_height)
	
	#Main game loop
	while not libtcod.console_is_window_closed():
		#Updates game entities if snake is not dead
		if snake.alive == True:
			snake.update()
			entities = snake.entities.copy()
			entities.append(apple.apple)
		
		#Handles rendering
		render_all(con, entities, screen_width, screen_height)
		libtcod.console_flush()
		clear_all(con, entities)
		
		#Handles keyboard input
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
		input = handle_keys(key)
		move = input.get('move')
		restart = input.get('restart')
		exit = input.get('exit')
		fullscreen = input.get('fullscreen')
		
		if move:
			snake.set_next_dir(move)
		
		if restart:
			snake = Snake(int(screen_width/2), int(screen_height/2), 'S', libtcod.Color(20, 200, 20), 1, fps_limit, apple, screen_width, screen_height)
		
		if exit:
			return True
			
		if fullscreen:
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
			
if __name__ == '__main__':
	main();