import libtcodpy as libtcod

#Handles user input

def handle_keys(key):

	#Handles changing snake direction
	if key.vk == libtcod.KEY_UP:
		return {'move': 4}
	elif key.vk == libtcod.KEY_DOWN:
		return {'move': 2}
	elif key.vk == libtcod.KEY_LEFT:
		return {'move': 3}
	elif key.vk == libtcod.KEY_RIGHT:
		return {'move': 1}
	
	
	#Handles other input
	if key.vk == libtcod.KEY_SPACE:
		return {'restart': True}
		
	elif key.vk == libtcod.KEY_ENTER and key.lalt:
		return {'fullscreen': True}
		
	elif key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}
		
	return {}