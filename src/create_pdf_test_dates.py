"""Create a PDF with random dates on it."""

from datetime import datetime
from random import randint

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("docs/example.pdf", pagesize=letter)


def add_random_dates_to_page(page_num):
    c.drawString(30, 750, f"Page {page_num}")
    for i in range(10):
        random_x = randint(50, 500)
        random_y = randint(50, 700)
        random_date = datetime(randint(2000, 2022), randint(1, 12),
                               randint(1, 28))
        c.drawString(random_x, random_y, random_date.strftime("%Y-%m-%d"))


# Example usage: add_random_dates_to_page(1)
add_random_dates_to_page(1)
c.showPage()
add_random_dates_to_page(2)
c.save()
