import tkinter as tk


class Mortgage_calc:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("250x350")
        self.window.title("Mortgage Calculator")
        # house label and entry
        self.house_cost_label = tk.Label(text="House Price:")
        self.house_cost_entry = tk.Entry()
        # down payment label and entry
        self.d_pay_label = tk.Label(text="Down Payment (%):")
        self.d_pay_entry = tk.Entry()
        # interest label and entry
        self.interest_label = tk.Label(text="Annual Interest (%):")
        self.interest_entry = tk.Entry()
        # term label and entry
        self.term_label = tk.Label(text="Payment Years:")
        self.term_entry = tk.Entry()
        # make button
        self.button = tk.Button(text="Submit", command=self._button_submit)
        # output label and entry
        self.output_label = tk.Label(text="Monthly Payment:")
        self.output_Entry = tk.Entry()

    def run_calc(self):
        #  draw house cost label and input
        self.house_cost_label.pack()
        self.house_cost_entry.pack()

        # draw down payment label and input
        self.d_pay_label.pack()
        self.d_pay_entry.pack()

        # draw annual interest label and input
        self.interest_label.pack()
        self.interest_entry.pack()

        # draw loan term label and input
        self.term_label.pack()
        self.term_entry.pack()

        # draw create submit button
        self.button.pack(pady=(10, 10))

        # draw output label
        self.output_label.pack()
        self.output_Entry.pack()

        self.window.mainloop()

    def _button_submit(self):
        house_cost_pl = float(self.house_cost_entry.get())
        d_pay_pl = float(self.d_pay_entry.get())
        interest_pl = float(self.interest_entry.get())
        term_pl = float(self.term_entry.get())

        self._mortgage_calc(house_cost_pl, d_pay_pl, interest_pl, term_pl)

    def _mortgage_calc(self, cost, d_pay_percent, interest, term):
        monthly_irate = (interest/100)/12
        d_pay = cost * (d_pay_percent/100)
        months = term*12
        total = cost - d_pay
        monthly_pay_pl = (monthly_irate*total)/(1-(1 + monthly_irate)**-months)
        self.output_Entry.delete(0, tk.END)
        self.output_Entry.insert(0, f'$ {round(monthly_pay_pl, 2)}')


if __name__ == "__main__":
    calc = Mortgage_calc()
    calc.run_calc()