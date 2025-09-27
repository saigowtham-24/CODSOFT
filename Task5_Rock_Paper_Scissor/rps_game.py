import random

class RPSGame:
    def __init__(self):
        self.user_score=0
        self.computer_score=0
        self.choices=['rock', 'paper', 'scissors']
        self.color_enabled=self.check_colorama()

    def check_colorama(self):
        try:
            from colorama import Fore, Style
            self.Fore=Fore
            self.Style=Style
            return True
        except ImportError:
            return False

    def get_colored(self,text,color):
        if not self.color_enabled:
            return text
        return f"{color}{text}{self.Style.RESET_ALL}"

    def get_user_choice(self):
        while True:
            choice=input("Choose rock, paper, or scissors: ").strip().lower()
            if choice in self.choices:
                return choice
            print("Invalid choice. Please try again.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self,user,computer):
        winning_moves={'rock':'scissors','scissors':'paper','paper':'rock'}
        if user==computer:
            return "tie"
        elif winning_moves[user]==computer:
            return "user"
        else:
            return "computer"

    def play_round(self):
        print("\n🪨 📄 ✂️ Rock-Paper-Scissors Game")
        user=self.get_user_choice()
        computer=self.get_computer_choice()

        print(f"\nYou chose: {self.get_colored(user,self.Fore.YELLOW)}")
        print(f"Computer chose: {self.get_colored(computer,self.Fore.CYAN)}")

        result=self.determine_winner(user,computer)
        if result=="tie":
            print(self.get_colored("It's a tie!",self.Fore.MAGENTA))
        elif result=="user":
            print(self.get_colored("🎉 You win!",self.Fore.GREEN))
            self.user_score+=1
        else:
            print(self.get_colored("💻 Computer wins!",self.Fore.RED))
            self.computer_score+=1

        print(f"\nScore → You: {self.user_score} | Computer: {self.computer_score}")

    def run(self):
        while True:
            self.play_round()
            again=input("\nPlay another round? (y/n): ").strip().lower()
            if again!='y':
                print("\n🏁 Game Over. Final Score:")
                print(f"You: {self.user_score} | Computer: {self.computer_score}")
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    RPSGame().run()
