from fpdf import FPDF


class PDF:
    def __init__(self, name):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("helvetica", "B", 50)
        self.pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self.pdf.image("shirtificate.png", w=self.pdf.epw)
        self.pdf.set_font_size(30)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.text(x=62, y=140, txt=f"{name} took CS50")

    def save(self, name):
        self.pdf.output(name)


name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")
