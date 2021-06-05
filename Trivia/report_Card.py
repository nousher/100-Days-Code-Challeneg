from fpdf import FPDF
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def CreateReportCard(Username, score):
    Document=FPDF(orientation='L', unit='mm', format='A3')
    Document.add_page()
    Document.image('Congratulation.Jpeg',0,0,410,180,'JPEG')
    Document.set_font("Helvetica", "BUI",size=45)
    Document.set_text_color(192,75,71)
#txt message will displayed on pdf page  at the center.
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=10, align="L")
    Document.cell(210, 10, txt="", ln=20, align="L")
    Document.cell(400, 10, txt=f"Congratulations, {Username} have passed this Trivia.", ln=12, align="C")
    Document.cell(400, 10, txt="\n", ln=12, align="C")
    Document.cell(400, 10, txt=f"You have successfully earned {score} out of 10.", ln=12, align="C")
    Document.output("pdf_file_name.pdf")
    open("pdf_file_name.pdf")
    #creating page format A4 Or A3 Or ...
    print("pdf has been created successfully....")