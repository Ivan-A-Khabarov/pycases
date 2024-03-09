from pyflowchart import Flowchart

code = """
a = 5
b = 7
c = a + b
print(c)
"""

fc = Flowchart.from_code(code)
fc.flowchart(open_browser=True)