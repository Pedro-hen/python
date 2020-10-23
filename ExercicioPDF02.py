from fpdf import FPDF
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()


cars = [[]]

while True:
    nome = str(input('Digite um carro: '))
    cars[0].append(nome)
    if nome == '':
        pdf.set_font('Arial', '', 16)
        for modelo in cars[0]:
            nome = modelo
            #pdf.cell(60, 20, '{}'.format((nome),0, 1))
            pdf.cell(0, 10, '{}'.format(nome), 0, 1, 'C')
        break

pdf.output('carros.pdf', 'F')

