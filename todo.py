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
    inputFile = open(fileName, "a")
    newTask = input("What task would you like to create?\n")

    try:
        inputFile.write(newTask + "\n")
        print(f"Successfully created task: {newTask}")
        inputFile.close()
        return None
    except:
        print("Error writing task")
        inputFile.close()
        return None
    
def deleteTask(fileName):
    inputFile = open(fileName, "r")
    tasks = []
    for line in inputFile.readlines():
        line = line.strip()
        tasks.append(line)   
    inputFile.close()

    taskToDelete = input("Which task would you like to delete?\n")

    if taskToDelete not in tasks:
        print("This task does not exist")
        tryAgain = input("Would you like to try again? (Y)\n").lower()

        if tryAgain == "y" or tryAgain == "yes":
            deleteTask(fileName)
        else:
            return None
    
    if taskToDelete in tasks:
        tasks.remove(taskToDelete)
        outputFile = open(fileName, "w")
        for item in tasks:
            outputFile.write(item + "\n")

        outputFile.close()
        print(f"Successfully deleted task: {taskToDelete}")
        return None
    

def main(fileName):
    operation = input("Would you like to 'Read (r)', 'Add (a)', or 'Delete (d)' tasks?\n").lower()

    if operation == 'read' or operation == 'r':
        readTasks(fileName)
        return None
    
    if operation == 'add' or operation == 'a':
        addTask(fileName)
        return None
    
    if operation == 'delete' or operation == 'd':
        deleteTask(fileName)
        return None

    print("Input must be 'Read (r)', 'Add (a)', or 'Delete (d)")
    return None

fileName = 'todo.txt'
main(fileName)
