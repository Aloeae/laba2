books = ['System Design','Python и DevOps','Git. Практическое руководство']

def book_list(books, func):
  for book in books:
    print(func(book))
    
def book_print(book):
  return book.upper() + ' - прочитано'
  
book_list(books, book_print)


==================== RESTART: C:/Users/tvoym/Downloads/ex.py ===================
SYSTEM DESIGN - прочитано
PYTHON И DEVOPS - прочитано
GIT. ПРАКТИЧЕСКОЕ РУКОВОДСТВО - прочитано
