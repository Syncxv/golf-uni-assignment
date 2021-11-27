from random import randrange
class Game:
    def init(self):
        self.distance = 230
        self.shots = 0
        self.running = True
        self.club = False
        self.choice = False

    def set_username(self):
        self.username = input('welcome to niggaboy golf. Enter your username: ')
        return self.username
    
    def main_menu(self):
        print(f'welcome to niggaboy golf {self.username}\n')
        print("(I)nstructions\n(P)lay golf\n(Q)uit")
        self.choice = input("Choice: ").lower()
        self.handle_choice()

    def handle_choice(self):
        if self.choice == "i":
            print("This is a simple golf game in which each hole is 230m game away with par 5.You are able to choose from 3 clubs, the Driver, Iron or Putter. The Driverwill hit around 100m, the Iron around 30m and the Putter around 10m. Theputter is best used very close to the hole.")
        elif self.choice == "q":
            print(f"Farewell and thanks for playing {self.username}")
            self.running = False
        elif self.choice == "p":
            self.play()

    def play(self):
        while self.distance:
            self.set_club()
            self.swing()
        if self.shots > 5:
            print(f"Clunk... After {self.shots} hits, the ball is in the hole!\n Disappointing. You are 5 over par.")
        elif self.shots < 5:
            print(f"Clunk... After {self.shots} hits, the ball is in the hole!\n Congratulations, you are {self.shots - 1} under par.")
        elif self.shots == 5:
            print(f"Clunk... After {self.shots} hits, the ball is in the hole! And that’s par.")
    def swing(self):
        if not self.club in ['d', 'p', 'i']:
            self.shots += 1
            print(f"Invalid club selection = air swing :( Your shot went 0m. You are {self.distance} from the hole, after {self.shots} shot/s")
        else:
            if self.club == "d":
                average_distace = 100
                self.swing_club(average_distace)
            elif self.club == "i":
                average_distace = 30
                self.swing_club(average_distace)
            elif self.club == "p":
                average_distace = 10
                self.swing_club(average_distace)
    def swing_club(self, average_distace):
        shot_distance = randrange(average_distace * 0.80, average_distace * 1.20)
        self.distance = abs(self.distance - shot_distance)
        self.shots += 1
        print(f"Your shot went {shot_distance}m.\n You are {self.distance}m from the hole, after {self.shots} shot/s.")
    def set_club(self):
        print("Club selection: press D for driver Avg 100m, I for Iron Avg 30m, P for Putter Avg 10m\n")
        self.club = input("choose a club: ").lower()

    def start(self):
        self.init()
        while self.running:
            self.set_username()
            self.main_menu()

            

game = Game()
game.start()