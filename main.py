from pikepdf import Pdf
import os
from icecream import ic


filename = input('Введите название файла: ')
ic(filename)

savedir = os.getcwd()
if not filename.endswith('.pdf'):
    filename += '.pdf'
ic(filename)
startfrom = int(input('Введите номер страницы, где расположен первый билет: '))

with Pdf.open('order.pdf') as pdf:

    if not os.path.exists('output'):
        os.makedirs('output')
    os.chdir('output')
    ic(os.getcwd())
    for n, page in enumerate(pdf.pages, start=1):
        if n >= startfrom:
            sep_page = Pdf.new()
            sep_page.pages.append(page)
            # sep_page.save(f'Билет {n - (startfrom - 1)}.pdf')
            ic(f'Я создаль {n - (startfrom - 1)}.pdf')
os.chdir(savedir)
