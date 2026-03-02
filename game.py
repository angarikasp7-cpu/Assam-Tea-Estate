class GameState:
    def __init__(self):
        self.current_year = 2024
        self.current_month = 1
        self.player_name = ""
        self.estate = None
        self.finances = None
        self.workers = None
        self.running = True
    
    def advance_month(self):
        self.current_month += 1
        if self.current_month > 12:
            self.current_month = 1
            self.current_year += 1
    
    def get_date_string(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return f"{months[self.current_month - 1]} {self.current_year}"

class TeaEstateGame:
    def __init__(self):
        self.state = GameState()
    
    def initialize_estate(self):
        from estate import Estate
        from finances import Finances
        from workers import WorkerManager
        self.state.estate = Estate(name=f"{self.state.player_name}'s Tea Estate")
        self.state.finances = Finances()
        self.state.workers = WorkerManager()

if __name__ == "__main__":
    print("Use gui_game.py to start the game with GUI")