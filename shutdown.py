import tkinter as tk
import random
import sys

plz_answer=input("\n \n \n \n would you like to shut down this code and if no plz click on the window that pops up before trying it also if it doesnt work and gives a wierd error that is red text in vscode just run it again it will work: \n \n \n ")
if plz_answer == 'yes':
    print("system terminated")
    exit()
elif plz_answer == 'no':                             # i used ai just for this massive chunk of code plz dont decline :)     
    class SuddenDeathGame:
        print("use arrow keys")
        def __init__(self, root):
            self.root = root
            self.root.title("Avoid the Red Square!")
            self.root.resizable(False, False)

            # Setup canvas
            self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
            self.canvas.pack()

            # Game variables
            self.player_x = 180
            self.enemy_x = random.randint(0, 360)
            self.enemy_y = 0
            self.enemy_speed = 7

            # Draw characters
            self.player = self.canvas.create_rectangle(self.player_x, 350, self.player_x + 40, 390, fill="green")
            self.enemy = self.canvas.create_rectangle(self.enemy_x, self.enemy_y, self.enemy_x + 40, self.enemy_y + 40, fill="red")

            # Bind controls
            self.root.bind("<Left>", self.move_left)
            self.root.bind("<Right>", self.move_right)

            # Start game loop
            self.update_game()

        def move_left(self, event):
            if self.player_x > 0:
                self.player_x -= 20
                self.canvas.moveto(self.player, self.player_x, 350)

        def move_right(self, event):
            if self.player_x < 360:
                self.player_x += 20
                self.canvas.moveto(self.player, self.player_x, 350)

        def update_game(self):
            # Move enemy down
            self.enemy_y += self.enemy_speed
            self.canvas.moveto(self.enemy, self.enemy_x, self.enemy_y)

            # Reset enemy if it goes off screen
            if self.enemy_y > 400:
                self.enemy_y = 0
                self.enemy_x = random.randint(0, 360)
                self.enemy_speed += 0.5  # Gradually increase difficulty

            # Check for collision
            if self.check_collision():
                print("You died!")
                sys.exit()  # Hard exit instantly closes the window and script

            # Repeat loop every 20 milliseconds
            self.root.after(20, self.update_game)

        def check_collision(self):
            # Quick bounding box collision check
            if (self.enemy_y + 40 >= 350 and self.enemy_y <= 390):
                if (self.enemy_x + 40 >= self.player_x and self.enemy_x <= self.player_x + 40):
                    return True
            return False

# Run the game
if __name__ == "__main__":
    window = tk.Tk()
    game = SuddenDeathGame(window)
    window.mainloop()
    print("system not terminated")
else:
    print("\n \n system error\n files exporting to terminal\n 172 viruses found please shut down your computer \n.......\n.......\n.......\n.......\n.......\n.......\n .......\n just kidding this is homework from -smit hehe")