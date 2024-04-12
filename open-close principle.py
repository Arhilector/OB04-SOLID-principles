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
        print()


class HtmlFormatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(report.content)

class Report():
    def __init__(self, title, content, format):
        self.title = title
        self.content = content
        self.format = format


report = Report("заголовок", "это текст отчета, его тут много",  TextFormatted())
