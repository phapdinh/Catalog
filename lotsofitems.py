from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
restaurant1 = Category(name="Urban Burger")

session.add(restaurant1)
session.commit()


menuItem1 = Item(name="French Fries", description="with garlic and parmesan", category=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = Item(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",category=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = Item(name="Chocolate Cake", description="fresh baked and served with ice cream",category=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = Item(name="Sirloin Burger", description="Made with grade A beef",category=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = Item(name="Root Beer", description="16oz of refreshing goodness",category=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = Item(name="Iced Tea", description="with Lemon",category=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = Item(name="Grilled Cheese Sandwich", description="On texas toast with American Cheese",category=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = Item(name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",category=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Category(name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = Item(name="Chicken Stir Fry", description="with your choice of noodles vegetables and sauces",category=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = Item(name="Peking Duck", description=" a famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", category=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = Item(name="Spicy Tuna Roll", description="",category=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = Item(name="Nepali Momo ", description="",category=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = Item(name="Beef Noodle Soup", description="",category=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = Item(name="Ramen", description="", category=restaurant2)

session.add(menuItem6)
session.commit()


# Menu for Panda Garden
restaurant1 = Category(name="Panda Garden")

session.add(restaurant1)
session.commit()


menuItem1 = Item(name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     category=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = Item(name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     category=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = Item(name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",
                     category=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = Item(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     category=restaurant1)

session.add(menuItem4)
session.commit()


# Menu for Thyme for that
restaurant1 = Category(name="Thyme for That Vegetarian Cuisine ")

session.add(restaurant1)
session.commit()


menuItem1 = Item(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     category=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = Item(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     category=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = Item(name="Honey Boba Shaved Snow",description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", category=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = Item(name="Cauliflower Manchurian",
                     description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions", category=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = Item(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     category=restaurant1)

session.add(menuItem5)
session.commit()


# Menu for Tony's Bistro
restaurant1 = Category(name="Tony\'s Bistro ")

session.add(restaurant1)
session.commit()


menuItem1 = Item(name="Shellfish Tower", description="", category=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = Item(name="Chicken and Rice", description="",category=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = Item(name="Mom's Spaghetti", description="",category=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = Item(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="", category=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = Item(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     category=restaurant1)

session.add(menuItem5)
session.commit()


# Menu for Andala's
restaurant1 = Category(name="Andala\'s")

session.add(restaurant1)
session.commit()


menuItem1 = Item(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     category=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = Item(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     category=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = Item(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     category=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = Item(name="Nigiri SamplerMaguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     description="",category=restaurant1)

session.add(menuItem4)
session.commit()


# Menu for Auntie Ann's
restaurant1 = Category(name="Auntie Ann\'s Diner ")

session.add(restaurant1)
session.commit()

menuItem9 = Item(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                     category=restaurant1)

session.add(menuItem9)
session.commit()


menuItem1 = Item(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     category=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = Item(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     category=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = Item(name="Morels on toast (seasonal)",
                     description="Wild morel mushrooms fried in butter, served on herbed toast slices", category=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = Item(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     category=restaurant1)

session.add(menuItem4)
session.commit()


# Menu for Cocina Y Amor
restaurant1 = Category(name="Cocina Y Amor ")

session.add(restaurant1)
session.commit()


menuItem1 = Item(name="Super Burrito Al Pastor",
                     description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", category=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = Item(name="Cachapa", description="Golden brown, corn-based venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     category=restaurant1)

session.add(menuItem2)
session.commit()

print "added menu items!"
