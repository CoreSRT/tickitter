from pikepdf import Pdf
import os
from icecream import ic


def find_pdf():
	file_name = ''
	pdf_count = 0
	for file in os.listdir():
		if os.path.isfile(file) and file.endswith(".pdf"):
			file_name = file
			pdf_count += 1
		if pdf_count == 1:
			return file_name
		else:
			print(f'Внимание! В директории должен быть только один файл pdf!')
			break
	return None


def main():
	savedir: str = os.getcwd()
	ic(os.listdir())
	filename: str = ''
	if find_pdf():
		filename: str = find_pdf()
	ic(filename)

	startfrom: int = int(input('Введите номер страницы, где расположен первый билет: '))

	with Pdf.open(filename) as pdf:

		if not os.path.exists('output'):
			os.makedirs('output')
		os.chdir('output')
		ic(os.getcwd())
		for n, page in enumerate(pdf.pages, start=1):
			if n >= startfrom:
				sep_page: Pdf = Pdf.new()
				sep_page.pages.append(page)
				# sep_page.save(f'Билет {n - (startfrom - 1)}.pdf')
				ic(f'Я создаль {n - (startfrom - 1)}.pdf')
	os.chdir(savedir)
	ic(os.getcwd())


if __name__ == '__main__':
	main()
