class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.currentPage = 0
        self.totalPages = len(self.items) // self.pageSize + 1

    def getVisibleItems(self):
        first = self.currentPage * self.pageSize
        return self.items[first:first + self.pageSize]

    def nextPage(self):
        self.currentPage += 1
        self.currentPage = 0 if self.currentPage >= self.totalPages else self.currentPage  # last then first again
        return self

    def prevPage(self):
        self.currentPage -= 1
        self.currentPage = (self.currentPage + self.totalPages) % self.totalPages  # first page then last again
        return self

    def firstPage(self):
        self.currentPage = 0
        return self

    def lastPage(self):
        self.currentPage = self.totalPages - 1
        return self

    def goToPage(self, pageNum):
        if pageNum < 1:
            pageNum = 1
        elif pageNum > self.totalPages:
            pageNum = self.totalPages
        self.currentPage = pageNum - 1
        return self


alphabetlist = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(items=alphabetlist, pageSize=7)