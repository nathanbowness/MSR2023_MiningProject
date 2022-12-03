django-excel-response3
=====================
 
This is an overhaul of https://pypi.python.org/pypi/django-excel-response which was originally http://djangosnippets.org/snippets/1151/

+ added class detection for values, and will use the value str(class_value)
+ added support for floats, dollar strings, and comma separated number strings that were broken in other forks
+ refactored the code to resemble an actual class, as opposed to one giant init function
+ removed the performance killing import every time you write a sheet, xlwt is required. If you don't like it use a CSV writer
+ refactored the CSV writing portion of the code to actually use python's csv class
+ added width auto adjustment

Usage
=====


    from excel_response3 import ExcelResponse

    def excelview(request):
        objs = SomeModel.objects.all()
        return ExcelResponse(objs)


or

    from excel_response3 import ExcelResponse

    def excelview(request):
        data = [
            ['Column 1', 'Column 2'],
            [1,2],
            [23,67]
        ]
        return ExcelResponse(data, 'my_data')

Constructor Kwargs
======
+ headers - an array containing column headers
+ output_name - maintaining this kwarg, but tries first to 
use the 2nd arg passed when defining the class
+ force_csv - forcibly respond with csv, defaults to False
+ encoding - defaults to 'utf8'
+ sheet_name - defaults to 'Sheet 1'
+ blanks_for_none - replace None values with '', defaults to True
+ auto_adjust_width - adjust width of each column automatically, defaults to True
