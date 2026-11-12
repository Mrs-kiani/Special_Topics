import random
import tkinter as tk
from tkinter import ttk


class NumberGuessingGame:
    MAX_ATTEMPTS = 10
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    def __init__(self, root):
        self.root = root
        self.root.title("بازی حدس عدد")
        self.root.geometry("520x620")
        self.root.minsize(460, 560)
        self.root.configure(bg="#101827")

        self.secret_number = 0
        self.attempts = 0
        self.game_over = False

        self.setup_styles()
        self.build_ui()
        self.new_game()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Game.Horizontal.TProgressbar",
            troughcolor="#263449",
            background="#38bdf8",
            bordercolor="#263449",
            lightcolor="#38bdf8",
            darkcolor="#38bdf8",
            thickness=12,
        )

    def build_ui(self):
        container = tk.Frame(self.root, bg="#101827", padx=28, pady=24)
        container.pack(fill="both", expand=True)

        tk.Label(
            container, text="🎯", font=("Segoe UI Emoji", 38),
            bg="#101827", fg="#ffffff"
        ).pack(pady=(0, 4))

        tk.Label(
            container, text="بازی حدس عدد",
            font=("Tahoma", 23, "bold"), bg="#101827", fg="#f8fafc"
        ).pack()

        tk.Label(
            container, text="عدد مخفی را در ۱۰ فرصت پیدا کن!",
            font=("Tahoma", 10), bg="#101827", fg="#94a3b8"
        ).pack(pady=(7, 20))

        card = tk.Frame(
            container, bg="#1b293b", padx=24, pady=22,
            highlightthickness=1, highlightbackground="#304158"
        )
        card.pack(fill="both", expand=True)

        tk.Label(
            card, text="یک عدد بین ۱ تا ۱۰۰ حدس بزن",
            font=("Tahoma", 12, "bold"), bg="#1b293b", fg="#e2e8f0"
        ).pack(pady=(0, 14))

        self.guess_var = tk.StringVar()
        self.guess_entry = tk.Entry(
            card, textvariable=self.guess_var, justify="center",
            font=("Tahoma", 20, "bold"), bg="#f8fafc", fg="#0f172a",
            relief="flat", bd=0, insertbackground="#0f172a"
        )
        self.guess_entry.pack(fill="x", ipady=12, pady=(0, 12))
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())

        self.guess_button = tk.Button(
            card, text="ثبت حدس", command=self.check_guess,
            font=("Tahoma", 11, "bold"), bg="#0284c7", fg="white",
            activebackground="#0369a1", activeforeground="white",
            relief="flat", cursor="hand2", pady=11
        )
        self.guess_button.pack(fill="x")

        self.feedback = tk.Label(
            card, text="منتظر اولین حدس تو هستم!",
            font=("Tahoma", 12, "bold"), bg="#1b293b", fg="#cbd5e1",
            wraplength=380
        )
        self.feedback.pack(pady=(22, 16))

        stats = tk.Frame(card, bg="#1b293b")
        stats.pack(fill="x", pady=(0, 8))

        self.attempt_label = tk.Label(
            stats, text="تلاش: ۰ از ۱۰",
            font=("Tahoma", 10, "bold"), bg="#1b293b", fg="#e2e8f0"
        )
        self.attempt_label.pack(side="right")

        self.remaining_label = tk.Label(
            stats, text="فرصت باقی‌مانده: ۱۰",
            font=("Tahoma", 10), bg="#1b293b", fg="#94a3b8"
        )
        self.remaining_label.pack(side="left")

        self.progress = ttk.Progressbar(
            card, maximum=self.MAX_ATTEMPTS, style="Game.Horizontal.TProgressbar"
        )
        self.progress.pack(fill="x", pady=(0, 18))

        self.new_game_button = tk.Button(
            card, text="↻  بازی جدید", command=self.new_game,
            font=("Tahoma", 10, "bold"), bg="#334155", fg="#f8fafc",
            activebackground="#475569", activeforeground="white",
            relief="flat", cursor="hand2", pady=10
        )
        self.new_game_button.pack(fill="x")

        tk.Label(
            container, text="ساخته‌شده با Python و Tkinter",
            font=("Tahoma", 8), bg="#101827", fg="#64748b"
        ).pack(pady=(16, 0))

    def check_guess(self):
        if self.game_over:
            return

        raw_value = self.guess_var.get().strip()
        try:
            guess = int(raw_value)
        except ValueError:
            self.feedback.config(
                text="لطفاً یک عدد صحیح وارد کن.", fg="#fbbf24"
            )
            self.guess_entry.focus_set()
            return

        if not self.MIN_NUMBER <= guess <= self.MAX_NUMBER:
            self.feedback.config(
                text="عدد باید بین ۱ تا ۱۰۰ باشد.", fg="#fbbf24"
            )
            self.guess_entry.focus_set()
            return

        self.attempts += 1
        remaining = self.MAX_ATTEMPTS - self.attempts
        self.attempt_label.config(text=f"تلاش: {self.to_persian(self.attempts)} از ۱۰")
        self.remaining_label.config(
            text=f"فرصت باقی‌مانده: {self.to_persian(remaining)}"
        )
        self.progress["value"] = self.attempts

        if guess == self.secret_number:
            self.feedback.config(
                text=f"🎉 آفرین! درست حدس زدی. عدد {self.to_persian(self.secret_number)} بود.",
                fg="#4ade80"
            )
            self.finish_game()
        elif self.attempts >= self.MAX_ATTEMPTS:
            self.feedback.config(
                text=f"😕 فرصت‌ها تمام شد! عدد درست {self.to_persian(self.secret_number)} بود.",
                fg="#fb7185"
            )
            self.finish_game()
        elif guess < self.secret_number:
            self.feedback.config(text="⬆️ عدد بزرگ‌تر است؛ بالاتر حدس بزن!", fg="#38bdf8")
        else:
            self.feedback.config(text="⬇️ عدد کوچک‌تر است؛ پایین‌تر حدس بزن!", fg="#fbbf24")

        self.guess_var.set("")
        if not self.game_over:
            self.guess_entry.focus_set()

    def finish_game(self):
        self.game_over = True
        self.guess_button.config(state="disabled", bg="#475569")
        self.guess_entry.config(state="disabled")

    def new_game(self):
        self.secret_number = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)
        self.attempts = 0
        self.game_over = False

        self.guess_var.set("")
        self.guess_entry.config(state="normal")
        self.guess_button.config(state="normal", bg="#0284c7")
        self.feedback.config(text="منتظر اولین حدس تو هستم!", fg="#cbd5e1")
        self.attempt_label.config(text="تلاش: ۰ از ۱۰")
        self.remaining_label.config(text="فرصت باقی‌مانده: ۱۰")
        self.progress["value"] = 0
        self.guess_entry.focus_set()

    @staticmethod
    def to_persian(value):
        return str(value).translate(str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹"))


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
