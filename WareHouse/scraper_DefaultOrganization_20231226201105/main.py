'''
This is the main file of the web scraper application.
'''
import tkinter as tk
from scraper import Scraper
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Web Scraper")
        self.geometry("400x300")
        self.scraper = Scraper()
        self.url_entry = tk.Entry(self)
        self.url_entry.pack()
        self.scrape_button = tk.Button(self, text="Scrape", command=self.scrape_website)
        self.scrape_button.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
    def scrape_website(self):
        url = self.url_entry.get()
        result = self.scraper.scrape_website(url)
        self.result_label.config(text=result)
if __name__ == "__main__":
    app = Application()
    app.mainloop()