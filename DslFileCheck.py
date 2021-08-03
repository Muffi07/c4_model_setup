import os


class DslFileCheck:
    file_name = ''
    file_data = ''
    file_data_list = []
    name_prod_dict = {}
    name_prod_dict_end = {}
    current_dir = os.path.abspath(os.getcwd())
    ext_report_xml_dir = current_dir + '\\external_report_xmls'
    ext_report_file = os.listdir(ext_report_xml_dir)
    fail_test = {}
    cont_relation_dict = {}
    cont_list_complete = []  # Required to search for Containers in relation dictionary.
    depl_env_dict = {}

    # Returns DSL file data as a String.
    def load_file(self, file_name):
        # file_path = 'dsl_files/' + file_name
        self.file_name = file_name
        if self.file_name != '':
            with open(self.file_name, 'r') as dsl_file:
                data = dsl_file.read()
                if data != '':
                    print('The DSL file has been read.')
                    print('Length of file is', len(str(data)))
                    # print('File content is - ', '\n', data)
                    self.file_data = data
                    return data
                else:
                    assert False, "No data in the DSL file"

    def dsl_file_product_chk(self):
        name_prod_dict = {}
        file_data = self.file_data
        file_data_list = file_data.split('\n')
        for i in range(len(file_data_list)):
            file_data_list[i] = file_data_list[i].strip()

        file_data_list = list(filter(None, file_data_list))
        print("After filter Length of file data list - ", len(file_data_list))
        self.file_data_list = file_data_list
        for i in range(len(file_data_list) - 2):
            if "softwareSystem" in file_data_list[i] and "=" in file_data_list[i] and "{" in file_data_list[i]:
                # print("Product name is - ", file_data_list[i])
                # print("Product name is - " + file_data_list[i][indx_1 + 1: indx_2])
                # indx_1 = file_data_list[i].index('=')
                # indx_2 = self.file_data_list[i][indx_1:].index('=')

                indx_1 = file_data_list[i].index('"')
                indx_2 = file_data_list[i].index('"', indx_1 + 1)
                name_prod_dict[file_data_list[i][indx_1 + 1:indx_2]] = i

                # name_prod.append(file_data_list[i][:indx_1].strip())

        print(name_prod_dict)
        self.name_prod_dict = name_prod_dict
        return name_prod_dict

    def dsl_file_container_chk(self):
        name_cont_dict = {}
        cont_dict = {}
        name_cont_map_dict = {}
        # cont_prod_list = []

        for product in self.name_prod_dict:
            # name_cont_dict = {}
            cont_list = []
            cont_index_list = []
            j = 0
            for i in range(int(self.name_prod_dict[product]), len(self.file_data_list) - 1):
                if "container" in self.file_data_list[i] and "=" in self.file_data_list[i]:
                    indx_1 = self.file_data_list[i].index('"')
                    indx_2 = self.file_data_list[i].index('"', indx_1 + 1)
                    cont_list.append(self.file_data_list[i][indx_1 + 1:indx_2])
                    # cont_index_list.append(i)
                    container_value = self.file_data_list[i].split('=')[0].strip()
                    self.cont_list_complete.append(container_value)
                    name_cont_dict[self.file_data_list[i][indx_1 + 1:indx_2]] = product
                    cont_dict[container_value] = product
                    name_cont_map_dict[self.file_data_list[i][indx_1 + 1:indx_2]] = container_value
                    # print(name_cont_dict)
                    # print(cont_dict)
                    if j != 0:
                        container_value_chk = self.file_data_list[j].split('=')[0].strip()
                        for k in range(j, i):
                            if "url" in self.file_data_list[k] and ".txt" in self.file_data_list[k]:
                                path_result_file = self.file_data_list[k].split()[-1]
                                print(path_result_file)
                                self.dsl_file_report_chk(path_result_file, container_value_chk)
                    j = i
                if (product.lower() in self.file_data_list[i + 1] or product.upper() in self.file_data_list[
                    i + 1] or product in self.file_data_list[i + 1]) \
                        and '"Is-part of"' in self.file_data_list[i + 1]:
                    if j != 0:
                        print("THIS IS REAL IMP +++++++++++++", self.file_data_list[j])
                        container_value_chk = self.file_data_list[j].split('=')[0].strip()
                        for k in range(j, i):
                            if "url" in self.file_data_list[k] and ".txt" in self.file_data_list[k]:
                                path_result_file = self.file_data_list[k].split()[-1]
                                print(path_result_file)
                                self.dsl_file_report_chk(path_result_file, container_value_chk)
                    prod_end_index = i
                    self.name_prod_dict_end[product] = prod_end_index
                    print("It broke here - ", i)
                    break

            # cont_prod_list.append(cont_list)
        print("Combined containers list - ", self.cont_list_complete)
        print("Container mapping - ", name_cont_map_dict)
        return name_cont_dict, cont_dict, name_cont_map_dict, self.fail_test

    def dsl_file_report_chk(self, report_file_name, container_value):
        if report_file_name in self.ext_report_file:
            report_file_name_path = self.ext_report_xml_dir + '\\' + report_file_name
            with open(report_file_name_path, 'r') as result_file:
                result_data = result_file.read()
                if result_data != '':
                    result_data_list = result_data.split('\n')
                    for result in result_data_list:
                        if "Failures:" in result:
                            indx_01 = result.index("Fail")
                            indx_02 = result.index(",", indx_01)
                            fail_test = result[indx_01:indx_02].split()[-1]
                            if int(fail_test) > 0:
                                print("Container name inside if +++++ ", container_value)
                                self.fail_test[container_value] = result_data
                                print("Fail test case for - ", report_file_name, " are -", fail_test)
                            break

    def dsl_file_cont_relation(self):
        container_status_dict = {key: None for key in self.cont_list_complete}
        for product in self.name_prod_dict:
            # name_cont_dict = {}
            # cont_list = []
            # cont_index_list = []
            j = 0
            for i in range(int(self.name_prod_dict[product]), self.name_prod_dict_end[product]):
                if "Relationship" in self.file_data_list[i] and "containers" in self.file_data_list[i]:
                    # self.dsl_cont_relation_dict(i)
                    for j in range(i + 1, self.name_prod_dict_end[product]):
                        if "->" in self.file_data_list[j]:
                            cont01 = self.file_data_list[j].split()[0]
                            cont02 = self.file_data_list[j].split()[2]
                            print("cont01 ---- ", cont01)
                            print("cont02 ---- ", cont02)
                            if cont01 in self.cont_list_complete and cont02 in self.cont_list_complete:
                                self.cont_relation_dict[cont01] = cont02
                        else:
                            break
            for item in container_status_dict:
                if item in self.fail_test:
                    container_status_dict[item] = False
                else:
                    container_status_dict[item] = True

            for i in range(len(self.cont_relation_dict)):
                for item in container_status_dict:
                    if item in self.cont_relation_dict.keys() and not container_status_dict[self.cont_relation_dict[item]]:
                        container_status_dict[item] = container_status_dict[self.cont_relation_dict[item]]

        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Containers status after Relation - ", container_status_dict)
        # self.container_status_dict = container_status_dict
        print("Relation dictionary - ", self.cont_relation_dict)
        return container_status_dict

    def dsl_file_depl_env(self):
        depl_env_dict = {}
        file_data = self.file_data
        file_data_list = file_data.split('\n')
        for i in range(len(file_data_list)):
            file_data_list[i] = file_data_list[i].strip()

        file_data_list = list(filter(None, file_data_list))
        print("After filter Length of file data list - ", len(file_data_list))
        self.file_data_list = file_data_list
        for i in range(len(file_data_list)):
            if "deploymentEnvironment" in file_data_list[i]:
                # print("Product name is - ", file_data_list[i])
                # print("Product name is - " + file_data_list[i][indx_1 + 1: indx_2])
                # indx_1 = file_data_list[i].index('=')
                # indx_2 = self.file_data_list[i][indx_1:].index('=')

                indx_1 = file_data_list[i].index('"')
                indx_2 = file_data_list[i].index('"', indx_1 + 1)
                depl_env_dict[file_data_list[i][indx_1 + 1:indx_2]] = i

                # name_prod.append(file_data_list[i][:indx_1].strip())

        print(depl_env_dict)
        self.depl_env_dict = depl_env_dict

        for env in self.depl_env_dict:
            # name_cont_dict = {}
            cont_list = []
            cont_index_list = []
            j = 0
            env_dependancy = []
            for i in range(int(self.depl_env_dict[env]) + 1, len(self.file_data_list) - 1):

                if "containerInstance" in self.file_data_list[i]:
                    env_cont = self.file_data_list[i].split()[1]
                    print("containerInstance - ", env_cont)
                    env_dependancy.append(env_cont)
                if "deploymentEnvironment" in self.file_data_list[i]:
                    break
            self.depl_env_dict[env] = env_dependancy

        print("After Changes ====================== ", depl_env_dict)
        return self.depl_env_dict
