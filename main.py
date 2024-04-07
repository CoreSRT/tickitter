from pikepdf import Pdf
import os
from icecream import ic  # библиотека для отладки
from time import sleep
from warns.warns import warnings

ic.disable()  # отключение модуля icecream, пока отладка не требуется


def find_pdf() -> tuple:
	file_name: str = ''
	pdf_count: int = 0
	for file in os.listdir():
		if os.path.isfile(file) and file.endswith(".pdf"):
			file_name = file
			pdf_count += 1
	return pdf_count, file_name


def main() -> None:
	savedir: str = os.getcwd()  # Сохраняем изначальную директорию

	# Нужно для хранения кортежа из функции find_pdf(), для того, чтобы не запускать функцию каждый раз
	find_pdf_tuple: tuple = find_pdf()

	if find_pdf_tuple[0] > 1:
		print(
				warnings.get('manyfiles')
		)
		sleep(100)
		quit()
	elif find_pdf_tuple[0] == 0:
		print(
				warnings.get('nofile')
		)
		sleep(100)
		quit()
	filename: str = find_pdf_tuple[1]
	# Данная часть кода выглядит довольно громоздкой, однако она выполняет необходимый функционал.
	# Возможно, в будущем ее можно улучшить или вынести в отдельную функцию

	startfrom: int = int(input('Введите номер страницы, где расположен первый билет: '))

	with Pdf.open(filename) as pdf:

		if not os.path.exists('Билеты'):
			os.makedirs('Билеты')
		os.chdir('Билеты')
		ic(os.getcwd())
		for n, page in enumerate(pdf.pages, start=1):
			if n >= startfrom:
				sep_page: Pdf = Pdf.new()
				sep_page.pages.append(page)
				sep_page.save(f'Билет {n - (startfrom - 1)}.pdf')
		# ic(f'Я создаль {n - (startfrom - 1)}.pdf')
	os.chdir(savedir)  # Возвращаемся в исходную директорию


if __name__ == '__main__':
	main()
