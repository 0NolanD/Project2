class Logic:
    def __init__(self, ui) -> None:
        '''
        Initializes variables and sets up button connections
        '''
        self.ui = ui
        self.ui.Screens.setCurrentIndex(0)
        self.ui.BurgerButton.clicked.connect(lambda: self.ui.Screens.setCurrentIndex(1))
        self.ui.FriesButton.clicked.connect(lambda: self.ui.Screens.setCurrentIndex(2))
        self.ui.DrinksButton.clicked.connect(lambda: self.ui.Screens.setCurrentIndex(3))
        self.ui.CheckoutButton.clicked.connect(lambda: self.ui.Screens.setCurrentIndex(4))
        self.done = False
        self.subtotal = 0
        self.tax_rate = 0.055
        self.fry_amount = 0
        self.burger_amount = 0
        self.drink_amount = 0
        self.ui.CheeseInput.hide()
        self.ui.NumOfSlices.hide()
        self.ui.CheeseButton.clicked.connect(self.toggle_cheese_input)
        self.ui.AllButton.clicked.connect(self.select_all_toppings)
        self.ui.NoButton.clicked.connect(self.deselect_all_toppings)
        self.ui.FryConfirm.clicked.connect(self.add_fries)
        self.ui.DrinkConfirm.clicked.connect(self.add_drink)
        self.ui.BurgerConfirm.clicked.connect(self.add_burger)
        self.ui.Tip15Button.clicked.connect(lambda: self.calculate_total(0.15))
        self.ui.Tip20Button.clicked.connect(lambda: self.calculate_total(0.20))
        self.ui.Tip25Button.clicked.connect(lambda: self.calculate_total(0.25))
        self.ui.CustomTipButton.clicked.connect(self.toggle_custom_tip_input)
        self.ui.CheckoutConfirm.clicked.connect(self.calculate_total_with_custom_tip)
        self.ui.CheckoutClear.clicked.connect(self.clear_variables)
        self.ui.PercentagePrompt.hide()
        self.ui.TipInput.hide()
        self.burger_stack = []
        self.fry_stack = []
        self.drink_stack = []

    def clear_variables(self) -> None:
        '''
        Resets all variables
        '''
        self.ui.CheckoutDisplay.clear()
        self.ui.TipInput.clear()
        self.subtotal = 0
        self.ui.Tip15Button.setChecked(False)
        self.ui.Tip20Button.setChecked(False)
        self.ui.Tip25Button.setChecked(False)
        self.ui.CustomTipButton.setChecked(False)
        self.ui.PercentagePrompt.hide()
        self.ui.TipInput.hide()
        self.ui.CheckoutError.clear()
        self.done = False
        self.fry_amount = 0
        self.burger_amount = 0
        self.drink_amount = 0
        self.burger_stack = []
        self.fry_stack = []
        self.drink_stack = []
        self.ui.PattyInput.setText("1")
        self.ui.CheeseInput.setText("1")
        self.ui.CheeseButton.setChecked(False)
        self.ui.CheeseInput.clear()
        self.ui.NumOfSlices.hide()
        self.ui.CheeseInput.hide()
        self.ui.MustardBox.setChecked(False)
        self.ui.KetchupBox.setChecked(False)
        self.ui.OnionBox.setChecked(False)
        self.ui.PickleBox.setChecked(False)
        self.ui.LettuceBox.setChecked(False)
        self.ui.TomatoBox.setChecked(False)
        self.ui.BurgerError.clear()
        self.ui.SmallFryButton.setChecked(False)
        self.ui.MediumFryButton.setChecked(False)
        self.ui.LargeFryButton.setChecked(False)
        self.ui.FryError.clear()
        self.ui.SmallDrinkButton.setChecked(False)
        self.ui.MediumDrinkButton.setChecked(False)
        self.ui.LargeDrinkButton.setChecked(False)
        self.ui.DrinkInput.setCurrentIndex(0)
        self.ui.DietCheck.setChecked(False)
        self.ui.DrinkError.clear()

    def toggle_cheese_input(self) -> None:
        '''
        Shows the cheese input box when the button is checked
        '''
        if self.ui.CheeseButton.isChecked():
            self.ui.CheeseInput.show()  # shows when the cheese button is true
            self.ui.NumOfSlices.show()
        else:
            self.ui.CheeseInput.hide()
            self.ui.NumOfSlices.hide()

    def add_fries(self) -> None:
        '''
        Adds fries to the checkout
        '''
        if self.done:  # doesn't allow new items when a total is shown in checkout
            self.ui.FryError.setText("Clear total to add")
            return

        size = ""
        price = 0
        if self.ui.SmallFryButton.isChecked():
            size = "Small"
            price = 2.00
        elif self.ui.MediumFryButton.isChecked():
            size = "Medium"
            price = 3.00
        elif self.ui.LargeFryButton.isChecked():
            size = "Large"
            price = 4.00
        else:
            self.ui.FryError.setText("Please select a size")
            return

        self.subtotal += price

        self.fry_stack.append({'size': size, 'price': price})

        self.ui.CheckoutDisplay.append(f"{size} Fries - ${price:.2f}")  # adds fries to checkout and clears variable
        self.ui.SmallFryButton.setChecked(False)
        self.ui.MediumFryButton.setChecked(False)
        self.ui.LargeFryButton.setChecked(False)
        self.ui.FryError.clear()
        self.fry_amount += 1
        self.check_for_combo()

    def add_drink(self) -> None:
        '''
        Adds drinks to the checkout
        '''
        if self.done:
            self.ui.FryError.setText("Clear total to add")
            return
        size = ""
        price = 0
        option = self.ui.DrinkInput.currentText()

        if self.ui.SmallDrinkButton.isChecked():
            size = "Small"
            price = 1.50
        elif self.ui.MediumDrinkButton.isChecked():
            size = "Medium"
            price = 2.00
        elif self.ui.LargeDrinkButton.isChecked():
            size = "Large"
            price = 2.50
        else:
            self.ui.DrinkError.setText("Please select a size")
            return

        if option == 'Select A Drink':
            self.ui.DrinkError.setText("Please select a drink")
            return

        if self.ui.DietCheck.isChecked() and option != 'Water':  # correctly specifies if the drink is diet
            self.ui.CheckoutDisplay.append(f"{size} Diet {option} - ${price:.2f}")
        else:
            self.ui.CheckoutDisplay.append(f"{size} {option} - ${price:.2f}")

        self.drink_stack.append({'size': size, 'price': price, 'option': option})

        self.subtotal += price
        self.ui.SmallDrinkButton.setChecked(False)
        self.ui.MediumDrinkButton.setChecked(False)
        self.ui.LargeDrinkButton.setChecked(False)
        self.ui.DrinkInput.setCurrentIndex(0)
        self.ui.DietCheck.setChecked(False)
        self.ui.DrinkError.clear()
        self.drink_amount += 1
        self.check_for_combo()

    def add_burger(self) -> None:
        '''
        Adds burgers to the checkout
        '''
        if self.done:
            self.ui.FryError.setText("Clear total to add")
            return
        slices_int = 1
        price = 0
        patties = 0
        patties_str = self.ui.PattyInput.text().strip()
        has_cheese = False
        has_mustard = self.ui.MustardBox.isChecked()
        has_ketchup = self.ui.KetchupBox.isChecked()
        has_onion = self.ui.OnionBox.isChecked()
        has_pickle = self.ui.PickleBox.isChecked()
        has_lettuce = self.ui.LettuceBox.isChecked()
        has_tomato = self.ui.TomatoBox.isChecked()

        try:
            patties = int(patties_str)  # ensures patties isn't below 1 or above 4
            if patties < 1 or patties > 4:
                raise ValueError
        except ValueError:
            self.ui.BurgerError.setText("Patty amount must be 1-4")
            return

        price = 0
        if patties == 1:
            patties_str = 'Single'
            price += 2.50
        elif patties == 2:
            patties_str = 'Double'
            price += 3.00
        elif patties == 3:
            patties_str = 'Triple'
            price += 3.50
        elif patties == 4:
            patties_str = 'Quadruple'
            price += 4.00

        if self.ui.CheeseButton.isChecked():
            slices = 1
            has_cheese = True
            slices = self.ui.CheeseInput.text().strip()

            try:
                slices_int = int(slices)
                if slices_int < 1 or slices_int > 4:
                    raise ValueError
            except ValueError:
                self.ui.BurgerError.setText("Max cheese slices is 4")
                return

            price += slices_int * 0.25  # Raises price based on number of slices

        if has_cheese:  # shows 'cheeseburger' if it has cheese, 'burger' if not
            burger_item = f'{patties_str} Cheeseburger - ${price:.2f}'
        else:
            burger_item = f'{patties_str} Burger - ${price:.2f}'
        self.ui.CheckoutDisplay.append(burger_item)

        if has_cheese:  # lists all toppings
            self.ui.CheckoutDisplay.append(f"   {slices_int} Cheese")
        if has_mustard:
            self.ui.CheckoutDisplay.append("   Mustard")
        if has_ketchup:
            self.ui.CheckoutDisplay.append("   Ketchup")
        if has_onion:
            self.ui.CheckoutDisplay.append("   Onion")
        if has_pickle:
            self.ui.CheckoutDisplay.append("   Pickle")
        if has_lettuce:
            self.ui.CheckoutDisplay.append("   Lettuce")
        if has_tomato:
            self.ui.CheckoutDisplay.append("   Tomato")

        self.subtotal += price

        self.burger_stack.append({'patties': patties_str, 'price': price, 'has_cheese': has_cheese, 'slices': slices_int})

        self.ui.PattyInput.setText("1")
        self.ui.CheeseInput.setText("1")
        self.ui.CheeseButton.setChecked(False)
        self.ui.CheeseInput.clear()
        self.ui.NumOfSlices.hide()
        self.ui.CheeseInput.hide()
        self.ui.MustardBox.setChecked(False)
        self.ui.KetchupBox.setChecked(False)
        self.ui.OnionBox.setChecked(False)
        self.ui.PickleBox.setChecked(False)
        self.ui.LettuceBox.setChecked(False)
        self.ui.TomatoBox.setChecked(False)
        self.ui.BurgerError.clear()
        self.burger_amount += 1
        self.check_for_combo()


    def select_all_toppings(self) -> None:
        '''
        Sets all burger toppings to True
        '''
        self.ui.MustardBox.setChecked(True)
        self.ui.KetchupBox.setChecked(True)
        self.ui.OnionBox.setChecked(True)
        self.ui.PickleBox.setChecked(True)
        self.ui.LettuceBox.setChecked(True)
        self.ui.TomatoBox.setChecked(True)

    def deselect_all_toppings(self) -> None:
        '''
        Sets all burger toppings to False
        '''
        self.ui.MustardBox.setChecked(False)
        self.ui.KetchupBox.setChecked(False)
        self.ui.OnionBox.setChecked(False)
        self.ui.PickleBox.setChecked(False)
        self.ui.LettuceBox.setChecked(False)
        self.ui.TomatoBox.setChecked(False)

    def calculate_total(self, tip_percentage: float) -> None:
        '''
        Calculates a total for the order
        '''
        if tip_percentage == 0:  # sets the tip to 0 if no tip is added
            tip = 0
        else:
            tip = self.subtotal * tip_percentage

        total = self.subtotal + tip + (self.tax_rate * self.subtotal)
        self.display_total(tip, total)

    def display_total(self, tip: float, total: float) -> None:
        '''
        Displays an order total in the checkout screen
        '''
        self.ui.CheckoutDisplay.append(f"Subtotal: ${self.subtotal:.2f}")
        self.ui.CheckoutDisplay.append(f"Tax: ${self.subtotal * self.tax_rate:.2f}")
        self.ui.CheckoutDisplay.append(f"Tip: ${tip:.2f}")
        self.ui.CheckoutDisplay.append(f"Total: ${total:.2f}")
        self.done = True

    def toggle_custom_tip_input(self) -> None:
        '''
        Shows the tip input box when the custom tip box is checked
        '''
        if self.ui.CustomTipButton.isChecked():
            self.ui.PercentagePrompt.show()
            self.ui.TipInput.show()
        else:
            self.ui.PercentagePrompt.hide()
            self.ui.TipInput.hide()

    def calculate_total_with_custom_tip(self) -> None:
        '''
        Calculates a total when there is a custom tip
        '''
        custom_tip_str = self.ui.TipInput.text().strip()

        try:
            if custom_tip_str == '':  # sets tip to 0 if nothing is typed into the custom tip box
                custom_tip = 0
            else:
                custom_tip = float(custom_tip_str)  # ensures there can't be a negative tip
                if custom_tip < 0:
                    raise ValueError
        except ValueError:
            self.ui.CheckoutError.setText("Invalid tip amount")
            return

        custom_tip /= 100  # divides tip by 100 to ensure totals are correctly calculated
        tip = self.subtotal * custom_tip

        total = self.subtotal + tip + (self.tax_rate * self.subtotal)

        self.display_total(tip, total)

    def check_for_combo(self) -> None:
        '''
        Checks if there's a match for a combo
        '''
        if len(self.burger_stack) > 0 and len(self.fry_stack) > 0 and len(self.drink_stack) > 0:
            self.combine_items()  # combines items into a combo if there is a match for each item
        else:
            pass

    def combine_items(self) -> None:
        '''
        Assigns combos when there is an available match and applies a discount
        '''
        if len(self.burger_stack) >= 1 and len(self.fry_stack) >= 1 and len(self.drink_stack) >= 1:
            burger_price = self.burger_stack[0]['price']  # finds the items at the bottom of the stacks
            fry_price = self.fry_stack[0]['price']
            drink_price = self.drink_stack[0]['price']

            total_price = burger_price + fry_price + drink_price

            combo_discount = total_price * 0.20  # applies a 20% discount
            combo_price = total_price - combo_discount

            self.ui.CheckoutDisplay.append(f"Combo Added - ${combo_price:.2f}")

            self.subtotal -= total_price - combo_price  # removes the previous prices for the items before the match

            del self.burger_stack[0]  # removes the matched items from the bottom of the stack
            del self.fry_stack[0]
            del self.drink_stack[0]
        else:
            pass