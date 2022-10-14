class Resume:

    def __init__(my, name, age):
        my.name = name
        my.age = age

    def show(my):
        len_name = len(my.name)

        print(" -" + "-"*len_name + "- ")
        print("| " +    my.name   + " |")
        print(" -" + "-"*len_name + "- ")