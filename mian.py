import tkinter as tk
from tkinter import ttk , messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root 
        self.root.title("Restaurant Order Management System")


        self.menu_items = {
            "Fries Meal": 5.99,
            "Burger Meal": 8.99,
            "Pizza Meal": 12.99,
            "Lunch Meal": 10.99,
            "Cheeseburger Meal": 9.99,
            "Drinks" : 5
        }

        self.exchange_rates = 82
        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx = 0.5 , rely = 0.5 , anchor = tk.CENTER)

        ttk.label(frame,text = "Restaurant Order Management System", font = ("Helvetica", 16, "bold")).grid(row = 0 , columnspan = 3 , padx = 10 , paddy = 10)

        self.menu_labels = {}

        self.menue_quantity = {}

        for i , (item , price) in enumerate(self.menu_items.items() , start = 1):
            label = ttk.Label(frame , text = f"{item}  (${price}):" , font = ("Arial", 12))

            label.grid(row=i , column = 0 , padx = 10 , pady = 5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame , width = 5)
            quantity_entry.grid(row = i , column = 1 , padx = 10 , pady = 5)
            self.menue_quantity[item] = quantity_entry

        self.currency_var = tk.StringVar()
        ttk.Label(frame , text = "Currency :" , font = ("Arial", 12)).grid(row = len(self.menu_items) + 1 , column = 0 , padx = 10 , pady = 5)

        currency_dropdown = ttk.Combobox(frame , textvariable = self.currency_var , state = "readonly" , width = 10 , values = ("USD" , "INR"))

        currency_dropdown.current(0)
        self.currency_var.trace("w" , self.update_prices)

        order_button = ttk.Button(frame , text = "Place Order" , command = self.place_order)

        order_button.grid(row = len(self.menu_items) + 2 , columnspan = 3 , pady = 10)



    def setup_background(self , root):
        bg_width  , bg_height = 8009 , 600
        canvas = tk.Canvas(root , width = bg_width , height = bg_height)
        canvas.pack()

        orginal_image = tk.PhotoImage(file = "background.png")
        background_image = orginal_image.subsample(orginal_image.width() // bg_width , orginal_image.height() // bg_height)

        canvas.create_image(0, 0 , anchor = tk.NW , image = background_image)

        def update_menu_prices(self , *args):
            currency = self.currency_var.get()
            symbol = "₹" if currency == "INR" else "$"
            rate = self.exchange_rates if currency == "INR" else 1

            for item , price in self.menu_items.items():
                price = self.menue_items[item] * rate
                label.config(text = f"{item} ({symbol}{price}):")

    def place_order(self):
        total_cost = 0
        order_summary = "ORDER SUMMARY:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rates if currency == "INR" else 1

        for item , entry in self.menue_quantity.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = price * quantity
                total_cost += cost

                if quantity > 0: 
                    order_summary += (f" {item}: {quantity} x {symbol}{price} = {symbol}{cost}\n")


            if total_cost > 0:
                order_summary += f"\nTotal Cost : {symbol}{total_cost}"
                messagebox.showinfo("Order PLaced" , order_summary)

            else:
                messagebox.showerror("Error" , "Please Order at least one item.")


if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()

                    


