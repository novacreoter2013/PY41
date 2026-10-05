import tkinter as tk
from tkinter import messagebox, ttk


class StationeryOrderManagement:

    def __init__(self, root):
        self.root = root
        self.root.title("Stationery Order Management App")

        self.stationery_items = {
            "NOTEBOOK": 3,
            "PENCIL PACK": 2,
            "PEN SET": 4,
            "ERASER": 1,
            "GEOMETRY BOX": 6,
            "COLOUR PENCILS": 5,
        }

        self.exchange_rate = 82

        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(
            frame,
            text="Stationery Order Management",
            font=("Arial", 20, "bold"),
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.item_labels = {}
        self.item_quantities = {}

        for index, (item, price) in enumerate(
            self.stationery_items.items(), start=1
        ):
            item_label = ttk.Label(
                frame, text=f"{item} (${price}):", font=("Arial", 12)
            )

            item_label.grid(row=index, column=0, padx=10, pady=5)

            self.item_labels[item] = item_label

            quantity_entry = ttk.Entry(frame, width=5)

            quantity_entry.grid(row=index, column=1, padx=10, pady=5)

            self.item_quantities[item] = quantity_entry

        self.currency_var = tk.StringVar()

        ttk.Label(frame, text="Currency:", font=("Arial", 12)).grid(
            row=len(self.stationery_items) + 1, column=0, padx=10, pady=5
        )

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "INR"),
        )

        currency_dropdown.grid(
            row=len(self.stationery_items) + 1, column=1, padx=10, pady=5
        )

        currency_dropdown.current(0)

        self.currency_var.trace_add("write", self.update_item_prices)

        order_button = ttk.Button(
            frame, text="Place Order", command=self.place_order
        )

        order_button.grid(
            row=len(self.stationery_items) + 2,
            columnspan=3,
            padx=10,
            pady=10,
        )

    def setup_background(self, root):
        background_width = 800
        background_height = 600

        canvas = tk.Canvas(
            root, width=background_width, height=background_height
        )

        canvas.pack()

        original_image = tk.PhotoImage(file="image1.png")

        background_image = original_image.subsample(
            original_image.width() // background_width,
            original_image.height() // background_height,
        )

        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

        canvas.image = background_image

    def update_item_prices(self, *args):
        currency = self.currency_var.get()

        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, label in self.item_labels.items():
            price = self.stationery_items[item] * rate

            label.config(text=f"{item} ({symbol}{price}):")

    def place_order(self):
        total_cost = 0
        order_summary = "Stationery Order Summary:\n"

        currency = self.currency_var.get()

        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, entry in self.item_quantities.items():
            quantity = entry.get()

            if quantity.isdigit():
                quantity = int(quantity)

                price = self.stationery_items[item] * rate
                cost = quantity * price
                total_cost += cost

                if quantity > 0:
                    order_summary += (
                        f"{item}: {quantity} x "
                        f"{symbol}{price} = {symbol}{cost}\n"
                    )

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"

            messagebox.showinfo("Order Placed", order_summary)

        else:
            messagebox.showerror(
                "Error", "Please order at least one stationery item."
            )


if __name__ == "__main__":
    root = tk.Tk()

    app = StationeryOrderManagement(root)

    root.geometry("800x600")

    root.mainloop()