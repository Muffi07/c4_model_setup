import jinja2
import os

root_dir_path = os.getcwd()

title = 'Hi this is my title'
output_file = './html_files/html_test_reports/myfile.html'

# lets write the substitution to a file
# items = []
# for i in range(1, 11):
#     i = str(i)
#
#     dict == {}
#     # you just don't have to quote the keys
#     an_item = dict(test_case_name="Test name - " + i, date="2012-06-" + i, id=i, position="status", status="Passed")
#     items.append(an_item)

# ... your code here ...
status_pre = True
status_data = True
status_ser = True
status_build = True

status_server = status_data & status_ser

table_headings = ("Test Category", "Presentation", "Data Analysis", "Services", "Build Automation")
table_data_client = ("Client(SWT Bot)", status_pre, status_pre, status_pre, "")
table_data_ser = ("Server(Integration tests)", "", status_server, status_server, "")
table_data_smoke = ("Smoke tests(manual)", "", status_build, status_build, status_build)

table_data = (table_data_client, table_data_ser, table_data_smoke)

print(table_data)

subs = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./html_files/template')
).get_template('table_test_report.html').render(headings=table_headings, data=table_data)
with open(output_file, 'w') as f: f.write(subs)

script_path = os.path.dirname(os.path.abspath(__file__))
rendered_file_path = os.path.join(script_path, output_file)

print(rendered_file_path)
