import view


def start():
    op = view.get_funchion()
    if op == 1:
        view.new_user()
        if op == 2:
          view.print_tab()
          if op == 3:
            view.print_name_lastname()

