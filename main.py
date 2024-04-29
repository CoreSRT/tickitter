from pikepdf import Pdf
import os
from warns.warns import project_warnings
from functools import cache
from typing import NoReturn


@cache
def find_pdf(amount=None) -> str | int:
	"""
	Функция для поиска и подсчета количества pdf файлов в директории. Кэширует результат, поскольку вызывается
	многократно
	Args:
		:param amount: Параметр, определяющий возвращаемое значение:
			None - при отсутствии аргумента, возвращается название файла
			Любой другой аргумент (для удобства используется 'amount') возвращает количество pdf файлов в директории
	:return(str | int): Название файла или количество pdf файлов в директории
	"""
	amount = amount or None
	pdf_name: str = ''
	pdf_count: int = 0
	for cur_file in os.listdir():
		if os.path.isfile(cur_file) and cur_file.endswith('.pdf'):
			pdf_name = cur_file
			pdf_count += 1
	return pdf_count if amount else pdf_name


def check_dir_files() -> NoReturn | str:
	"""
	Функция для отработки всех возможных ошибок, которые могут возникнуть при запуске программы
	:return: (str): Возвращает название файла в виде строки, либо выводит сообщение об ошибке и завершает программу
	"""
	if find_pdf('amount') > 1:
		print(project_warnings.get('manyfiles'))
		input()
		quit()
	elif find_pdf('amount') == 0:
		print(project_warnings.get('nofile'))
		input()
		quit()
	return find_pdf()


def get_start_page() -> int:
	"""
	Функция для получения номера страницы, с которой начинается разделение билетов.
	:return: (int): Номер страницы, с которой начинается разделение.
	"""
	while True:
		try:
			startpage: int = int(input('Введите номер страницы, с которой начинаются билеты: '))
			if startpage > 0:
				return startpage
			else:
				raise ValueError
		except ValueError:
			print(project_warnings.get('badnum'))


def main() -> None:
	"""
	Главная функция. Получает название файла и номер страницы, где расположен первый билет, разделяет последующие
	билеты на отдельные pdf файлы под своей нумерацией в соответствие с накладной и сохраняет их в директорию 'Билеты'
	:return:
	"""
	savedir: str = os.getcwd()  # Сохраняем изначальную директорию
	filename: str = check_dir_files()
	startfrom: int = get_start_page()

	with Pdf.open(filename) as pdf:
		if not os.path.exists('Билеты'):
			os.makedirs('Билеты')
		os.chdir('Билеты')
		for n, page in enumerate(pdf.pages, start=1):
			if n >= startfrom:
				sep_page: Pdf = Pdf.new()
				sep_page.pages.append(page)
				sep_page.save(f'Билет {n - (startfrom - 1)}.pdf')
	os.chdir(savedir)  # Возвращаемся в исходную директорию


if __name__ == '__main__':
	main()
