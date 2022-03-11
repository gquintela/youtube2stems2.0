from threading import Thread
import os


class Concurrent_mananger:
    def __init__(self):
        pass

    def concurrent_run(self, original_list_to_process, run_method):
        a_list_of_lists_to_proccess = self.distribute_by_cores(original_list_to_process)
        self.proccess_list_of_lists(run_method, a_list_of_lists_to_proccess)

    def distribute_by_cores(self, a_list_to_process):
        """creates (#cores) lists (min between cores and total videos)"""
        effective_cores_qty = min(os.cpu_count(), len(a_list_to_process))
        a_list_of_lists_to_proccess = [[] for x in range(effective_cores_qty)]
        index_list = 0
        for element in a_list_to_process:
            a_list_of_lists_to_proccess[index_list].append(element)
            index_list += 1
            if index_list >= effective_cores_qty:
                index_list = 0
        return a_list_of_lists_to_proccess

    def proccess_list_of_lists(self, run_method, a_list_of_lists_to_proccess):
        for a_list in a_list_of_lists_to_proccess:
            if len(a_list) != 0:
                try:
                    t = Thread(target=self.serial_run, args=(a_list, run_method))
                    t.start()
                except:
                    print("Error in serial run")
                    exit(1)

    def serial_run(self, a_list, run_method):
        for element in a_list:
            run_method(element)
