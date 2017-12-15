def main():
    # list to hold on to out items
    shopping_list = []

    def show_help():
        print("What should we ick up at the store?")
        print("""
        Enter 'DONE' to stop adding items.
        Enter 'HELP' for help.
        Enter 'SHOW' to see your current list.
        """)

    def show_list():
        print("Here is everything in the list")

        for item in shopping_list:
            print(item)

    def add_to_list(new_item):
        shopping_list.append(new_item)
        print("Adding {}. List now has {} items".format(new_item, len(shopping_list)))

    show_help()

    while True:
        new_item = raw_input("> ")

        if new_item == 'DONE':
            break
        elif new_item == 'HELP':
            show_help()
            continue
        elif new_item == 'SHOW':
            show_list()
            continue
        add_to_list(new_item)


    show_list()
main()
