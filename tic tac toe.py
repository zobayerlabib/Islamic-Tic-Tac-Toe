import tkinter as tk  # Import tkinter for GUI
from tkinter import messagebox  # Import messagebox for dialogs
import random  # Import random module to generate random number
from collections import deque # Import deque from collections module to implement BFS algorithm
# Create class
class IslamicTicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Islamic Tic-Tac-Toe")  # Title for the window
        self.master.geometry("400x300")  # Set the initial size for the window
        self.master.configure(bg="#f0f0f0")  # Window background color
        # Initialize current player
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        # Create buttons for the Tic-Tac-Toe game
        self.buttons = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text="", command=lambda i=i, j=j: self.on_button_click(i, j),
                                               font=("Arial", 20), width=5, height=2)
                self.buttons[i][j].grid(row=i + 1, column=j + 1, padx=5, pady=5)
        # Set question
        self.mcqs = [
            ("What is the obligatory pilgrimage to Mecca called?", ["Hajj", "Umrah", "Eid", "Ziyarat"], "Hajj"),
            ("What is the Islamic declaration of faith?", ["Shahada", "Salah", "Zakat", "Sawm"], "Shahada"),
            ("What is the first month of the Islamic calendar?", ["Muharram", "Ramadan", "Shawwal", "Dhu al-Hijjah"], "Muharram"),
            ("Who is the final prophet in Islam?", ["Prophet Muhammad (pbuh)", "Prophet Moses (pbuh)", "Prophet Jesus (pbuh)", "Prophet Abraham (pbuh)"], "Prophet Muhammad (pbuh)"),
            ("What is the term for obligatory Islamic charitable giving?", ["Zakat", "Sadaqah", "Khums", "Fitrah"], "Zakat"),
            ("How many times a day do Muslims perform the Salah (prayer)?", ["Five", "Three", "Seven", "Ten"], "Five"),
            ("What is the month of fasting in Islam?", ["Ramadan", "Shawwal", "Dhu al-Hijjah", "Muharram"], "Ramadan"),
            ("Which city is considered the holiest in Islam?", ["Mecca", "Medina", "Jerusalem", "Karachi"], "Mecca"),
            ("What is the Night of Decree in Islam known as?", ["Laylat al-Qadr", "Laylat al-Miraj", "Laylat al-Bara'ah", "Laylat al-Isra"], "Laylat al-Qadr"),
            ("What is the term for Islamic jurisprudence?", ["Fiqh", "Hadith", "Tafsir", "Usul al-Fiqh"], "Fiqh"),
            ("Who is known as the 'Seal of the Prophets' in Islam?", ["Muhammad (pbuh)", "Jesus (pbuh)", "Moses (pbuh)", "Abraham (pbuh)"], "Muhammad (pbuh)")
        ]
        self.shuffle_options()
        self.current_mcq_index = 0
        self.show_welcome_page() # Show the welcome page

    def shuffle_options(self):
        for mcq in self.mcqs: # Shuffle the options of each mcq
            random.shuffle(mcq[1])

    def show_welcome_page(self):
        self.name = tk.StringVar() # For displaying the welcome page
        self.welcome_frame = tk.Frame(self.master, bg="#f0f0f0") # set details about frame
        self.welcome_frame.grid(row=0, column=0, padx=50, pady=20)

        self.welcome_label = tk.Label(self.welcome_frame, text="Welcome to Islamic Tic-Tac-Toe!", font=("Arial", 16),
                                      bg="#f0f0f0")
        self.welcome_label.pack()

        self.name_label = tk.Label(self.welcome_frame, text="Enter your name:", font=("Arial", 12), bg="#f0f0f0")
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(self.welcome_frame, textvariable=self.name, font=("Arial", 12))
        self.name_entry.pack()

        self.start_button = tk.Button(self.welcome_frame, text="Start Game", command=self.show_instructions,
                                      font=("Arial", 12), bg="#4CAF50", fg="white")
        self.start_button.pack(pady=10)
    # Method for the instructions page
    def show_instructions(self): 
        self.player_name = self.name.get()
        if not self.player_name:
            messagebox.showerror("Error", "Please enter your name!")
            return

        self.welcome_frame.destroy()

        self.instruction_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.instruction_frame.grid(row=0, column=0, padx=50, pady=20)

        self.instruction_label = tk.Label(self.instruction_frame, text="Instructions:", font=("Arial", 12),
                                          bg="#f0f0f0")
        self.instruction_label.pack()
       # set instruction
        instructions = [
            "1. Answer the questions correctly to play your move.",
            "2. AI player will make moves automatically.",
            "3. If you answer incorrectly, the correct answer will be displayed.",
            "4. The game will continue until someone wins or the game ends in a draw."
        ]
        for instruction in instructions:
            tk.Label(self.instruction_frame, text=instruction, font=("Arial", 10), bg="#f0f0f0").pack(anchor="w")

        self.start_game_button = tk.Button(self.instruction_frame, text="Start Game", command=self.start_game,
                                           font=("Arial", 12), bg="#4CAF50", fg="white")
        self.start_game_button.pack(pady=10)

    def start_game(self):
        self.instruction_frame.destroy()
        self.display_mcq()
    #Method For display meq
    def display_mcq(self):
        if self.current_mcq_index < len(self.mcqs):
            mcq, options, answer = self.mcqs[self.current_mcq_index]
            self.current_mcq_index += 1

            self.mcq_frame = tk.Frame(self.master, bg="#f0f0f0")
            self.mcq_frame.grid(row=0, column=0, padx=50, pady=20)

            self.mcq_label = tk.Label(self.mcq_frame, text=mcq, font=("Arial", 12), bg="#f0f0f0")
            self.mcq_label.pack()

            self.selected_option = tk.StringVar()
            for i, option in enumerate(options):
                tk.Radiobutton(self.mcq_frame, text=option, variable=self.selected_option, value=option,
                               font=("Arial", 10), bg="#f0f0f0").pack(anchor="w")

            self.submit_mcq_button = tk.Button(self.mcq_frame, text="Submit", command=self.check_answer,
                                               font=("Arial", 12), bg="#4CAF50", fg="white")
            self.submit_mcq_button.pack(pady=10)
        else:
            self.mcq_frame.destroy()
            if self.current_player == "X":
                self.enable_board()
            else:
                self.ai_move()
    # to judge the answer
    def check_answer(self):
        user_answer = self.selected_option.get()
        mcq, options, answer = self.mcqs[self.current_mcq_index - 1]

        if user_answer == answer:
            messagebox.showinfo("Correct", "Well done! You answered correctly.")
            if self.current_player == "X":
                self.on_player_move()
            else:
                self.ai_move()
            self.mcq_frame.destroy()
        else:
            messagebox.showinfo("Incorrect", f"Sorry, that's incorrect. The correct answer is: {answer}.")
    
    def on_button_click(self, i, j):
        if self.board[i][j] == "":
            if self.current_player == "X":
                self.current_move = (i, j)
                if hasattr(self, "mcq_frame"):  # Checking if the mcq frame exists
                    self.mcq_frame.destroy()  # to remove the current question frame
                self.display_mcq()  # Display a new question
    # for the user moves
    def on_player_move(self):
        i, j = self.current_move
        self.board[i][j] = self.current_player
        self.buttons[i][j].config(text=self.current_player)
       # check if it is win draw or lost
        if self.check_winner(i, j):
            messagebox.showinfo("Winner", f"Congratulations, {self.player_name}! You win!")
            self.reset_board()
        elif self.check_draw():
            messagebox.showinfo("Draw", "The game ends in a draw.")
            self.reset_board()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            if self.current_player == "O":
                self.ai_move()
   # Method for ai move, that uses breadth-first search and minimax algorithom
    def ai_move(self):
        best_move = self.find_best_move_bfs()
        if best_move:
            i, j = best_move
            self.current_move = (i, j)
            self.on_player_move()
    # to find the best move for ai
    def find_best_move_bfs(self):
        queue = deque() # Initialize a queue for bfs
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    queue.append((i, j))

        best_score = float('-inf')
        best_move = None
       # Performing the  breadth-first search
        while queue:
            i, j = queue.popleft()
            self.board[i][j] = "O"
            score = self.minimax_bfs(self.board, False, "O")
            self.board[i][j] = ""

            if score > best_score:
                best_score = score
                best_move = (i, j)

        return best_move
    # method for minimax bfs
    def minimax_bfs(self, board, is_maximizing, current_player):
        if self.check_winner(0, 0):
            return 1 if current_player == "O" else -1
        elif self.check_draw():
            return 0
    # Recursive minimax function
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        score = self.minimax_bfs(board, False, current_player)
                        board[i][j] = ""
                        best_score = max(best_score, score)
            return best_score
        else: # If time for the opponent turn
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "X"
                        score = self.minimax_bfs(board, True, current_player)
                        board[i][j] = ""  #backtracking
                        best_score = min(best_score, score)  # Update the best score
            return best_score
 # Check if the current player won horizontally, vertically or diagonally
    def check_winner(self, row, col):
        if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.current_player:
            return True
        if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_player:
            return True
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player) or \
           (self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player):
            return True
        return False
#check if it is draw
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True
  #reset the game board to initial
    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
  #enable game board for player input
    def enable_board(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.buttons[i][j].config(state="normal")
                else:
                    self.buttons[i][j].config(state="disabled")
  #method for quit game
    def quit_game(self):
        if messagebox.askokcancel("Quit", "Do you want to quit the game?"):
            self.master.destroy()
# The main program entry point
if __name__ == "__main__":
    root = tk.Tk()  # Create Tkinter root window
    game = IslamicTicTacToe(root) #game object instandiate
    root.protocol("WM_DELETE_WINDOW", game.quit_game) # to close the window
    root.mainloop() #tkinter event loop start
