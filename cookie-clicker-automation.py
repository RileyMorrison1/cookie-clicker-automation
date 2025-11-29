from pynput import keyboard
import pyautogui
import threading
import time

#  * Basic Variables *
# These variables should be the only variables changed by a non technical user.

# Cookie Location
cookie_x = 877
cookie_y = 456

# Function Priorities
stock_market_priority = 1
golden_cookie_priority = 2
clicker_priority = 3
shopping_priority = 4
gardening_priority = 5

# Shopping
minutes_between_buys = 1

# Stock Market Variables
buy_under_price = 10

bank_level = 1

cereals_sell_price = 0
 
chocolate_sell_price = 0
 
butter_sell_price = 0

sugar_sell_price = 0

nuts_sell_price = 0

salt_sell_price = 0

vanilla_sell_price = 0

eggs_sell_price = 0

cinnamon_sell_price = 0 

cream_sell_price = 0

jam_sell_price = 0

white_chocolate_sell_price = 0

honey_sell_price = 0

cookies_sell_price = 0 

recipes_sell_price = 0

subsidiaries_sell_price = 0 

publicists_sell_price = 0

you_sell_price = 0

# Key Configuration
auto_clicker_start_key = 'q'
auto_clicker_stop_key = 'w'

auto_stock_start_key = 'a'
auto_stock_stop_key = 's'

auto_golden_cookie_start_key = 'z'
auto_golden_cookie_stop_key = 'x'

auto_shopping_start_key = 'r'
auto_shopping_stop_key = 't'

auto_gardening_start_key = 'f'
auto_gardening_stop_key = 'g'

# * END OF BASIC VARIABLES *

auto_click = False
clicking = False

auto_golden_cookie = False
golden_cookie_click = False

auto_stocks = False
stock_buy_sell = False

auto_shopping = False
auto_shopping_click = False

auto_gardening = False
auto_gardening_click = False

seconds_between_buys = minutes_between_buys * 60

# clicker method automatically clicks the cookie.
def auto_clicker():
	global auto_click
	global clicking
	global cookie_x, cookie_y

	while True:
		if clicking & auto_click:
			pyautogui.click(x=cookie_x, y=cookie_y, button='left')


# auto_stock_market method automatically buys and sells stock.
# Method not created yet.
def auto_stock_market():
	print("Auto Stock Market started")


# golden_cookie_search method searches for a golden cookie and if found clicks it.
# Method not created yet.
def golden_cookie_search():
	print("Searching for a golden cookie")


# auto_shopping method automatically buys buildings and perks.
# Currently does not work because of update.
def auto_shop():
        global clicking, auto_clicking, auto_shopping_click, seconds_between_buys
        auto_shopping_click = True
        
        while auto_shopping:
                clicking = False
                #Antim. Condenser
                pyautogui.click(x=1611, y=1028, button='left', clicks=10, interval=.1)

                # Time Machine
                pyautogui.click(x=1611, y=966, button='left', clicks=10, interval=.1)

                # Portal
                pyautogui.click(x=1611, y=901, button='left', clicks=10, interval=.1)

                # Alchemy Lab
                #pyautogui.click(x=1611, y=836, button='left', clicks=10, interval=.1)

                # Shipment
                #pyautogui.click(x=1611, y=772, button='left', clicks=10, interval=.1)

                # Wizard Tower
                #pyautogui.click(x=1611, y=711, button='left', clicks=10, interval=.1)

                # Temple
                #pyautogui.click(x=1611, y=645, button='left', clicks=10, interval=.1)

                # Bank
                #pyautogui.click(x=1611, y=580, button='left', clicks=10, interval=.1)

                # Factory
                #pyautogui.click(x=1611, y=517, button='left', clicks=10, interval=.1)

                # Mine
                #pyautogui.click(x=1611, y=449, button='left', clicks=10, interval=.1)

                # Farm
                #pyautogui.click(x=1611, y=393, button='left', clicks=10, interval=.1)

                # Grandma
                #pyautogui.click(x=1611, y=325, button='left', clicks=10, interval=.1)

                # Clicker
                #pyautogui.click(x=1611, y=263, button='left', clicks=10, interval=.1)

                # Perks
                pyautogui.click(x=1392, y=150, button='left', clicks=10, interval=.1)
                clicking = True
                time.sleep(seconds_between_buys)


# on_press method checks what key is pressed and gives it functionality.
def on_press(key):
        global clicking, auto_click
        global auto_stocks, auto_golden_cookie, auto_shopping, auto_gardening
        golden_cookie_search_thread = threading.Thread(target=golden_cookie_search, daemon=True)
        auto_stock_market_thread = threading.Thread(target=auto_stock_market, daemon=True)
        auto_shopping_thread = threading.Thread(target=auto_shop, daemon=True)

        try:

                # If the 'q' key is pressed the auto clicker is started.
                if key.char == auto_clicker_start_key:
                        if auto_click:
                                print("Auto clicker is already running")
                                
                        else:
                                auto_click = True
                                clicking = True
                                print("Auto clicker started")

                # If the 'w' key is pressed the auto clicker is stopped.
                elif key.char == auto_clicker_stop_key:
                        if auto_click:
                                auto_click = False
                                clicking = False
                                print("Auto clicker stopped")

                        else:
                                print("Auto clicker is already inactive")

                # If the 'a' key is pressed the auto stock market is started.
                elif key.char == auto_stock_start_key:
                        if auto_stocks:
                                print("Auto stock market is already running")

                        else:
                                auto_stocks = True
                                print("Auto stock market started")

                # If the 's' key is pressed the auto stock market is stopped.
                elif key.char == auto_stock_stop_key:
                        if auto_stocks:
                                auto_stocks = False
                                print("Auto stock market stopped")

                        else:
                                print("Auto stock market is already inactive")

                # If the 'z' key is pressed the auto golden cookie is started.
                elif key.char == auto_golden_cookie_start_key:
                        if auto_golden_cookie:
                                print("Auto golden cookie is already running")

                        else:
                                auto_golden_cookie = True
                                print("Auto golden cookie started")

                # If the 'x' key is pressed the auto golden cookie is stopped.
                elif key.char == auto_golden_cookie_stop_key:
                        if auto_golden_cookie:
                                auto_golden_cookie = False
                                print("Auto golden cookie stopped")

                        else:
                                print("Auto golden cookie is already inactive")

                # If the 'r' key is pressed the auto shopping is started.
                elif key.char == auto_shopping_start_key:
                        if auto_shopping:
                                print("Auto shopping is already running")

                        else:
                                auto_shopping = True
                                auto_shopping_thread.start()
                                print("Auto shopping started")

                # If the 't' key is pressed the auto shopping is stopped.
                elif key.char == auto_shopping_stop_key:
                        if auto_shopping:
                                auto_shopping = False
                                print("Auto shopping stopped")

                        else:
                                print("Auto shopping is already inactive")

                elif key.char == auto_gardening_start_key:
                        if auto_gardening:
                                print("Auto gardening is already running")

                        else:
                                auto_gardening = True
                                print("Auto gardening started")

                elif key.char == auto_gardening_stop_key:
                        if auto_gardening:
                                auto_gardening = False
                                print("Auto gardening stopped")

                        else:
                                print("Auto gardening is already inactive")

	# Happens when the key pressed is not a standard letter, key like escape.
        except AttributeError:
                # If the escape key is pressed the program is terminated.
                if key == keyboard.Key.esc:
                        print("Terminating Program")
                        return False


# Presses into the Cookie Clicker window.
pyautogui.click(x=cookie_x, y=cookie_y, button='left')

# Creates threads.
clicker_thread = threading.Thread(target=auto_clicker, daemon=True)


# Starts threads.
clicker_thread.start()



# Listens for keyboard inputs.
with keyboard.Listener(on_press=on_press) as listener:
	listener.join()
