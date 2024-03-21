from pikepdf import Pdf
import os
from icecream import ic
from time import sleep


def find_pdf():
	file_name = ''
	pdf_count = 0
	for file in os.listdir():
		if os.path.isfile(file) and file.endswith(".pdf"):
			file_name = file
			pdf_count += 1
	return pdf_count, file_name


def main():
	savedir: str = os.getcwd()
	ic(os.listdir())

	# Нужно исключительно для хранения кортежа из функции find_pdf(), для того, чтобы не запускать функцию каждый раз
	find_pdf_tuple = find_pdf()

	if find_pdf_tuple[0] != 1:
		print(
				f'{"-" * 20}\n'
				f'Внимание! В директории находится больше одного pdf-файла!\n'
				f'Пожалуйста, проверьте, чтобы в директории находился только один pdf-файл,\n'
				f'закройте программу и повторите попытку\n'
				f'{"-" * 20}\n'
		)
		sleep(100)
		quit()
	filename: str = find_pdf_tuple[1]
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
