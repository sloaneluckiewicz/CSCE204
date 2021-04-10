from product import Product 

shopping_list = (
    Product("Veja Sneakers", "Venturi Suede Kaki Sable Oxford-Grey Sneakers", 175),
    Product("Ragnar Lothbrok and the History of the Vikings", "Paperback Book", 17.58),
    Product("Venus Flytrap", "Plant with Black Pot", 18.99)
)

print("Your shopping list: ")
total_cost = 0
for product in shopping_list:
    product.display()
    total_cost += product.get_total_price()

print(f"Total cost : $ {round(total_cost, 2)}")


