from fpdf import FPDF


# parametre page orientation : Portrait = P (par defaut), Landscape = L
# Les formats peuvent être modifiés 'A4' (par defaut), 'A3', 'A5'
class PDF(FPDF):

	def titles(self):
		self.set_xy(0.0,30.0) # indique la position initiale x,y de l'élément
		self.set_font('Arial', 'B', 16)
		self.set_text_color(255,255,255) # text_color
		self.set_fill_color(60, 171, 176) # brackground color
		self.set_line_width(0.7) # border width
		self.cell(10)
		self.cell(w=190.0, h=10.0, align='C', txt="CONTRAT DE FORMATION", border=False, ln=True, fill=True)
		self.ln()

	
	def sub_titles(self, texte):
		
		self.set_font('Arial', 'B', 12)
		self.set_text_color(0,0,0)
		self.set_fill_color(222,222,222) #gris
		self.cell(w = 190.0, h=7.0, align='L', txt=texte, ln=True, fill=True)
		#self.ln()


	def paraf(self, paraf):
		
		self.set_x(10)
		self.set_font('Times', '', 10)
		self.set_text_color(0,0,0) # noir
		self.multi_cell(190, 5, paraf)

	def img(self):
		self.image('pdf_generator/logo_keyz.png', x=100, y=5,w=20)
		self.ln()
	
		


