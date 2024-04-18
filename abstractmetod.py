# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def docPrinter(self):
#         print(f"сформирован отчет {self.title} с содержанием {self.content}")
#


from abc import ABC, abstractmethod

class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass


class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)


class HtmlFormatted(Formatted):
    def format(self, report):

        print(f"<h1>{report.title}</h1>") # h1 - заголовок
        print(f"<p>{report.content}</p>") # p - параграф


class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)



report = Report("заголовок", "это текст отчета, его тут много",  HtmlFormatted())
reporttextformatted = Report("заголовок", "это текст отчета, его тут много",  TextFormatted())
report.docPrinter()
reporttextformatted.docPrinter()