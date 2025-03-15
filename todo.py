def readTasks(fileName):
    inputFile = open(fileName, "r")
    todoList = "####################\n"
    for line in inputFile.readlines():
        todoList += line
    todoList += "####################"

    print(todoList)
    inputFile.close()
    return None

def addTask(fileName):
    inputFile = open(fileName, "r")
    taskLength = len(inputFile.readlines())
    inputFile.close()

    inputFile = open(fileName, "a")
    newTask = input("What task would you like to create? (Separate by \";\" to create multiple tasks at once)\n")

    newTasks = newTask.split(";")

    try:
        for item in newTasks:
            taskLength += 1
            inputFile.write(f"{taskLength}: {item}\n")
            print(f"Successfully created task: {item}")           
        inputFile.close()
        return None
    except:
        print("Error writing task")
        inputFile.close()
        return None
    
def deleteTask(fileName):
    inputFile = open(fileName, "r")
    taskMap = {}
    
    for line in inputFile.readlines():
        line.strip()
        taskMap[line[:line.find(":")]] = line[line.find(":") + 2:].strip()
    inputFile.close()

    taskToDelete = input("Which task would you like to delete? Enter the Task number\n")

    if taskToDelete not in taskMap.keys():
        print("This task does not exist")
        tryAgain = input("Would you like to try again? (Y)\n").lower()

        if tryAgain == "y" or tryAgain == "yes":
            deleteTask(fileName)
        else:
            return None

    if taskToDelete in taskMap.keys():
        try:
            deleted = taskMap[taskToDelete]
            taskMap.pop(taskToDelete)
            newTaskMap = {}
            
            iterator = 1
            for value in taskMap.values():
                newTaskMap[iterator] = value
                iterator += 1

            outputFile = open(fileName, "w")
            for key, value in newTaskMap.items():
                outputFile.write(f"{key}: {value}\n")
            
            outputFile.close()
            print(f"Successfully deleted task: {deleted}")
            
        except:
            print("There was an error deleting your task")
            return None

    
def deleteAllTasks(fileName):
    disclaimer = input("WARNING: This operation will delete all tasks on your task list. Would you like to proceed? (Y)\n").lower()
    if disclaimer == "yes" or disclaimer == "y":
        outputFile = open(fileName, "w")
        outputFile.close()
        print("All tasks deleted successfully")
        return None      
    
    print("Operation aborted")
    return None

def main(fileName):
    operation = input("Would you like to 'Read (r)', 'Add (a)', 'Delete (d)', or 'Delete All (da)' tasks?\n").lower()

    if operation == 'read' or operation == 'r':
        readTasks(fileName)
        return None
    
    if operation == 'add' or operation == 'a':
        addTask(fileName)
        return None
    
    if operation == 'delete' or operation == 'd':
        deleteTask(fileName)
        return None
    
    if operation == 'delete all' or operation == 'da':
        deleteAllTasks(fileName)
        return None

    print("Input must be 'Read (r)', 'Add (a)', 'Delete (d), or Delete All (da)")
    return None

fileName = 'todo.txt'
main(fileName)