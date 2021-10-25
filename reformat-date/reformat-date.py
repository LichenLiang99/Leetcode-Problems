class Solution:
    def reformatDate(self, date: str) -> str:
        day,month,year = date.split()
        months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        return '{}-{:02}-{:0>2}'.format(year, months.index(month) + 1, day[:-2])