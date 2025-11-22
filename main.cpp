import pyautogui

def shopping():
	print("Shopping Mode Activation")

	# Time Machine
	pyautogui.click(x=1611, y=966, button='left', clicks=10, interval=.1)

	# Portal
	pyautogui.click(x=1611, y=901, button='left', clicks=10, interval=.1)

	# Alchemy Lab
	pyautogui.click(x=1611, y=836, button='left', clicks=10, interval=.1)

	# Shipment
	pyautogui.click(x=1611, y=772, button='left', clicks=10, interval=.1)

	# Wizard Tower
	pyautogui.click(x=1611, y=711, button='left', clicks=10, interval=.1)

	# Temple
	pyautogui.click(x=1611, y=645, button='left', clicks=10, interval=.1)

	# Bank
	pyautogui.click(x=1611, y=580, button='left', clicks=10, interval=.1)

	# Factory
	pyautogui.click(x=1611, y=517, button='left', clicks=10, interval=.1)

	# Mine
	pyautogui.click(x=1611, y=449, button='left', clicks=10, interval=.1)

	# Farm
	pyautogui.click(x=1611, y=393, button='left', clicks=10, interval=.1)

	# Grandma
	pyautogui.click(x=1611, y=325, button='left', clicks=10, interval=.1)
	
	# Clicker
	pyautogui.click(x=1611, y=263, button='left', clicks=10, interval=.1)

	# Perks
	pyautogui.click(x=1392, y=150, button='left', clicks=10, interval=.1)

print(pyautogui.position())

pyautogui.click(x=877, y=456, button='left')
running = True

shopping()
while(running):
	pyautogui.click(x=877, y=456, button='left', clicks=1000, interval=.1)
	shopping()
