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
        line = line.lower()
        tasks.append(line)   
    inputFile.close()

    deleteTask = input("Which task would you like to delete?\n")
    deleteTask = deleteTask.lower()

    if deleteTask not in tasks:
        print("This task does not exist")
        return None
    
    if deleteTask in tasks:
        tasks.remove(deleteTask)
        outputFile = open(fileName, "w")
        for item in tasks:
            outputFile.write(item + "\n")

        outputFile.close()
        print(f"Successfully deleted {deleteTask}")
        return None
    

def main(fileName):
    operation = input("Would you like to 'Read', 'Add', or 'Delete' tasks?\n")
    operation = operation.lower()

    if operation != "read" and operation != 'add' and operation != 'delete':
        print("Input must be 'Read', 'Add', or 'Delete")
        return None

    if operation == 'read':
        readTasks(fileName)
        return None
    
    if operation == 'add':
        addTask(fileName)
        return None
    
    if operation == 'delete':
        deleteTask(fileName)
        return None
    

fileName = 'todo.txt'
main(fileName)
