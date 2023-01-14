import time

class spencer_timer:

    def __init__(self):
        self.start_marks = []
        self.process_names = []

    """
    Begins tracking a process
    
    Parameters:
        process_name (string): name of the process being tracked
    Return:
        None
        
    """
    def begin_timer(self, process_name):
        self.process_names.append(process_name)
        self.start_marks.append(time.time())

    """
    Ends tracking a process and shows how long the process has been going on for

    Parameters:
        process_name (string): name of the process being tracked
    Return:
        A double representing the seconds that the given process has been going on for

    """
    def end_timer(self, process_name):
        index = self.process_names.index(process_name)
        self.process_names.pop(index)
        elapsed_time = time.time() - self.start_marks.pop(index)
        print("Process \"" + process_name + "\" has taken time " + str(elapsed_time) + " seconds")
        return elapsed_time

    def __print_status(self):
        print(self.process_names)
        print(self.start_marks)