class Tasks: # class of tasks that we plan on daily basis which can have priority, timeline, comments. And we can have operations for the task such as in progress, completed, deffered, blocked.
    '''
    Some tips
    1] We need to use decorators while creation class method and static method like @classmethod and @staticmethod respectively
    2] self is nothing but an istance of class so it can only access instance variables and instance methods.
    3] cls is a reference of class which we need to use when we want to access class vaiables and class methods.
    4]

    '''
    # class variable/attribute
    project_name = "Python OOP"
    # constructor
    def __init__(self):
        self.priority= "normal"
        self.timeline = 0
        self.comments =""
        self.status ="Un assigned"

    # Create task method
    def create_task(self,task_title_param,owner_param, priority_param):
        self.task_title = task_title_param
        self.owner =  owner_param
        self.priority = priority_param

    # Instance method
    def in_progress(self, owner_param, timeline_param, status_param="In progress"):
        self.owner = owner_param
        self.timeline = timeline_param
        self.status = status_param

    def task_completed(self, comments_param, status_param="Completed"):
        self.comments = comments_param
        self.status = status_param

    # class method
    @classmethod
    def update_project_name(cls, name_param):
        cls.project_name = name_param

    # static method
    @staticmethod       # basically this method doesn't have to be relevant to our class or overall work it can be a random thing that we need to handle at this point of time which doesn't deal with instance or class varianles or methods.
    def pending_report(no_of_tasks, no_of_tasks_done):
        pending_tasks = no_of_tasks - no_of_tasks_done
        print("Pending tasks:",pending_tasks)
    
    def view_task_details(self):
        print("""
Project name : {0}\nTasks Name : {1}\nTask Owner : {2}\nPritority : {3}\nStatus : {4}\nTimeLine : {5}
\nComments : {6}
""".format(self.project_name,self.task_title,self.owner,self.priority,self.status,self.timeline,self.comments))

# Run instance methods
task1 = Tasks()
task1.create_task("Complete OOP python implementation","Ghana","High")
task1.view_task_details()
task1.in_progress("TheBadCoder",3)

# Call class method and check its impact on object
Tasks.update_project_name("Coding Practice")
task1.view_task_details()

# Call static method
Tasks.pending_report(1,0)


'''
OUTPUT:
-------------
Project name : Python OOP
Tasks Name : Complete OOP python implementation
Task Owner : Ghana
Pritority : High
Status : Un assigned
TimeLine : 0

Comments :


Project name : Coding Practice
Tasks Name : Complete OOP python implementation
Task Owner : TheBadCoder
Pritority : High
Status : In progress
TimeLine : 3

Comments :

Pending tasks: 1
'''

