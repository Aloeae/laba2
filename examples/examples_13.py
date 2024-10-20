def book_list(books, func):
  for book in books:
    print(func(book))
    
books = ['System Design','Python и DevOps','Git. Практическое руководство']

book_list(books, lambda book: book.upper() + ' - прочитано')



==================== RESTART: C:/Users/tvoym/Downloads/ex.py ===================
SYSTEM DESIGN - прочитано
PYTHON И DEVOPS - прочитано
GIT. ПРАКТИЧЕСКОЕ РУКОВОДСТВО - прочитано
