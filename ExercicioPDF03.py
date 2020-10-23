from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()


carros = [['HB20 1.0 Comfort Plus','Hyundai','2014','R$ 33590,00'],
          ['2008 Allure 1.6 16v','Peugeot','2018','R$ 71990,00'],
          ['Argo Drive 1.0 Firefly','Fiat','2018','R$ 44999,00'],
          ['Corolla Sedan SEG 1.8 16v','Toyota','2010','R$ 44900,00'],
          ['KA 1.0 SE','Ford','2017','R$ 34900,00'],
          ['Fox 1.0 VHT','Volkswagen','2013','R$ 26990,00']]

pdf.set_font('Arial', 'B', 16)

pdf.set_draw_color(51, 51, 255)
pdf.set_fill_color(51, 51, 255)
pdf.set_text_color(204, 255, 255)
pdf.cell(0, 20, 'Loja - Carro de qualidade',1,1,'C', 1)


pdf.set_draw_color(255, 204, 51)
pdf.set_fill_color(255, 204, 51)
pdf.set_text_color(0, 0, 0)
sub = '{:<26} {:<16} {:<5} {:<9}'.format('Carro', 'Marca', 'Ano','Valor')
pdf.set_font('courier', 'B', 15)
pdf.cell(0, 20, sub, 1, 1,'R', 1)

pdf.set_font('courier', '', 12)

i = 0
for carro in carros:
    car = carro[0]
    marca = carro[1]
    ano = carro[2]
    valor = carro[3]

    if i == 1:

        pdf.set_text_color(51, 51, 255)
        i = 0
    else:
        pdf.set_text_color(0, 0, 0)
        i = 1
    pdf.cell(0, 10, '{:<33} {:<20} {:7} {:1}'.format(car,
                                                   marca,
                                                   ano,
                                                   valor),0,1)

pdf.image('medalha.png', 13,13,15,15)
pdf.image('medalha.png', 182,13,15,15)
pdf.image('carro.png', 75,115,50,50)
pdf.output('exe_loja_carros.pdf', 'F')