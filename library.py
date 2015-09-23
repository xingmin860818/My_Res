#!/usr/bin/env python
#-*-coding:utf-8-*-
class Library(object):
        def __init__(self):
                self.book_list = {}
                self.lend_books = {}
        def add_book(self,b_id,b_name):
                self.book_list[b_id] = b_name
        def del_book(self,b_id):
                self.book_list.pop(b_id)
        def search_book(self,student):
                exist_book = {}
                for bookid in self.book_list:
                        if isinstance(student,str):
                                if student == self.book_list[bookid]:
                                        return 'BOOK_ID: %d\tBOOK_NAME: %s' % (bookid,student)
                                else:
                                        return 'Sorry,we cannot find the book you need'
                        elif isinstance(student,object):
                                for bookname in student.search_book():
                                        if bookname == self.book_list[bookid]:
                                                exist_book[bookid] = bookname
                return exist_book
        def lend_book(self,student):
                for bookid in self.book_list:
                        for msg in student.borrow_book():
                                if msg == bookid or msg == self.book_list[bookid]:
                                        self.lend_books[bookid] = [student.s_id,student.name,self.book_list[bookid]]
                for ids in self.lend_books:
                        self.book_list.pop(ids)
                return self.lend_books,self.book_list

class Student(object):
        def __init__(self,s_id,name):
                self.s_id = s_id
                self.name = name
                self.list_book = []
                self.borrow_list = []
        def add_search(self,book_name):
                self.list_book.append(book_name)
        def search_book(self):
                return self.list_book
        def add_borrow(self,msg):
                self.borrow_list.append(msg)
        def borrow_book(self):
                return self.borrow_list



lib1 = Library()
lib1.add_book(1001,'Python')
lib1.add_book(1002,'Mysql')
lib1.add_book(1003,'Redis')

tom = Student(76351,'Tom')
tom.add_search('Python')
tom.add_search('Redis')
tom.add_search('UFO')
print '_'*60
print 'We just found these book from our library:\n'
print lib1.search_book(tom)
tom.add_borrow('Redis')
tom.add_borrow(1001)
print lib1.lend_book(tom)

                                                  
