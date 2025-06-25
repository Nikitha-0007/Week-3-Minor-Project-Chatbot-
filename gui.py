import tkinter as tk
from main import handle_input
from database import export_history, setup_db

def run_gui():
    setup_db()
    root = tk.Tk()
    root.title("🤖 Virtual Assistant")
    root.geometry("400x500")
    root.configure(bg="lightblue")

    history_text = tk.Text(root, height=20, width=48)
    history_text.pack(pady=10)

    input_field = tk.Entry(root, width=40)
    input_field.pack(pady=5)

    def on_submit():
        user_input = input_field.get()
        response = handle_input(user_input)
        history_text.insert(tk.END, f"You: {user_input}\nAssistant: {response}\n\n")
        input_field.delete(0, tk.END)

    submit_btn = tk.Button(root, text="Submit", command=on_submit)
    submit_btn.pack(pady=5)

    def export():
        export_history()
        history_text.insert(tk.END, "✅ History exported to history.csv\n\n")

    export_btn = tk.Button(root, text="Export History", command=export)
    export_btn.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
