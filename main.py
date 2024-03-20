from pikepdf import Pdf

startfrom = int(input('Введите номер страницы, где расположен первый билет: '))

with Pdf.open('order.pdf') as pdf:

    for n, page in enumerate(pdf.pages, start=1):
        if n >= startfrom:
            sep_page = Pdf.new()
            sep_page.pages.append(page)
            sep_page.save(f'Билет {n - (startfrom - 1):02d}.pdf')
