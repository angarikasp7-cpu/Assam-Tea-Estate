class Estate:
    def __init__(self, name, area, tea_type):
        self.name = name  # Name of the estate
        self.area = area  # Area in acres
        self.tea_type = tea_type  # Type of tea grown
        self.production = 0  # Initial production

    def grow_tea(self, amount):
        """
        Simulate growing tea.
        :param amount: Amount of tea harvested
        """
        self.production += amount
        print(f'Grew {amount} kg of tea in {self.name}. Total production: {self.production} kg.')

    def get_info(self):
        """
        Return information about the estate.
        """
        return f'Estate: {self.name}, Area: {self.area} acres, Tea Type: {self.tea_type}, Total Production: {self.production} kg.'
