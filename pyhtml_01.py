import jinja2
import os
from main import DslMain
from DslFileCheck import DslFileCheck


class DSLDashboard:
    root_dir_path = os.getcwd()
    output_file = './html_files/html_test_reports/myfile.html'
    headings_product_table = ["Products", "Status"]
    product_table_data = []

    def product_status(self, products_dict, containers_dict, failed_containers_dict):
        # headings_product_table = ["Products", "Status"]
        product_table_data = []
        for product in products_dict:
            product_table_data_temp = [product]
            status = True
            for container in containers_dict:
                if containers_dict[container] == product:
                    this_container = container
                    if this_container in failed_containers_dict.keys():
                        status = False
                        break
            if status:
                product_table_data_temp.append(True)
            else:
                product_table_data_temp.append(False)

            product_table_data.append(product_table_data_temp)

        self.product_table_data = product_table_data

        print("This is the list for Product table ---------- ")
        print(product_table_data)


    def each_product_status(self, products_dict, containers_dict, failed_containers_dict, cont_relation_dict):
        # headings_product_table = ["Products", "Status"]
        headings_container_table = ["Tests"]
        for product in products_dict:
            headings_container_table = ["Tests"]
            test = [['Client(SWT Bot)'], ['Server(Integration tests)'], ['Demo build for Jenkins Client']]
            table_data_client = ["Client(SWT Bot)"]
            table_data_ser = ["Server(Integration tests"]
            table_data_smoke = ["Smoke tests(manual)"]
            status = True
            for container in containers_dict:
                if containers_dict[container] == product:
                    this_container = container
                    headings_container_table.append(this_container)

            for i in range(len(test)):
                for j in range(1, len(headings_container_table)):
                    if headings_container_table[j] in failed_containers_dict.keys():
                        test[i].append(False)
                        print("START from here -------------------")
                        # for item in cont_relation_dict:






    def html_dashboard(self):
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

        # print(table_data)

        subs = jinja2.Environment(
            loader=jinja2.FileSystemLoader('./html_files/template')
        ).get_template('table_test_report.html').render(h_headings_product_table=self.headings_product_table,
                                                        h_product_table_data=self.product_table_data)
        with open(self.output_file, 'w') as f: f.write(subs)

        script_path = os.path.dirname(os.path.abspath(__file__))
        rendered_file_path = os.path.join(script_path, self.output_file)

        print(rendered_file_path)


if __name__ == "__main__":
    Dsl_obj = DslMain('./dsl_files')
    file_path = Dsl_obj.get_file()

    dslChk = DslFileCheck()

    file_data = dslChk.load_file(file_path)
    prod_dict = dslChk.dsl_file_product_chk()
    name_cont_dict, cont_dict, name_cont_map_dict, failed_cont_dict = dslChk.dsl_file_container_chk()
    print(cont_dict)
    print("----------------------------------------")
    print(failed_cont_dict.keys())
    cont_relation_dict = dslChk.dsl_file_cont_relation()
    html_obj = DSLDashboard()
    html_obj.product_status(prod_dict, cont_dict, failed_cont_dict)
    html_obj.html_dashboard()
