# в консоли пишем: pip install PyPDF2
import PyPDF2

def change_page_order(input_pdf_path, output_pdf_path, page_order):
    # Открываем исходный PDF файл
    with open(input_pdf_path, "rb") as input_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()

        # Добавляем страницы в новом порядке
        for page_num in page_order:
            writer.add_page(reader.pages[page_num])

        # Сохраняем измененный PDF в новый файл
        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)


# Пример использования
# Берет файлы из директории с самим файлом pdf.py
input_pdf = "original.pdf"
output_pdf = "reordered.pdf"

# На это месте должен быть алгоритм
# Новый порядок страниц (например, если хотим поменять местами первую и вторую страницы)
new_order = [1, 0]

change_page_order(input_pdf, output_pdf, new_order)