from tkinter import *
from tkinter import ttk

tkinter = Tk()

class View_EditableList(object):
    def __init__(self, root, root_row):
        """ List with buttons to edit its contents.
        :param root: parent widget
        :param roow_row: row in 'root'. The section takes 2 rows.
        """

        self.list = tkinter.Listbox(root, selectmode=tkinter.EXTENDED)
        self.list.grid(row=root_row, sticky=(W, E))
        root.rowconfigure(root_row, weight=1)

        self.frame = ttk.Frame(root)
        self.frame.grid(row=root_row + 1, sticky=(W, E))

        self.add = ttk.Button(self.frame, text="+", width=5)
        self.add.grid(row=0, column=1)
        self.edit = ttk.Button(self.frame, text="*", width=5)
        self.edit.grid(row=0, column=2)
        self.del_ = ttk.Button(self.frame, text="-", width=5)
        self.del_.grid(row=0, column=3)
        self.up = ttk.Button(self.frame, text=u"↑", width=5)
        self.up.grid(row=0, column=4)
        self.down = ttk.Button(self.frame, text=u"↓", width=5)
        self.down.grid(row=0, column=5)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(6, weight=1)


class Presenter_EditableList(object):
    def __init__(self, view, root):
        """

        :param view: View_EditableList
        :param root: root widget to be used as parent for modal windows
        """
        self.root = root
        self.view = view
        view.add.configure(command=self.add)
        view.edit.configure(command=self.edit)
        view.del_.configure(command=self.del_)
        view.up.configure(command=self.up)
        view.down.configure(command=self.down)

    def add(self):
        # View_AskText is a simple dialog that asks for a text value.
        #  see https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app/49028688#49028688
        #  for implementation
        w = gui_view.View_AskText(self.root)
        self.root.wait_window(w.top)
        if w.value:
            self.view.list.insert(self.view.list.size(), w.value)

    def edit(self):
        l = self.view.list
        try:
            [index] = l.curselection()
        except ValueError:
            return
        w = gui_view.View_AskText(self.root, l.get(index))
        self.root.wait_window(w.top)
        if w.value:
            l.delete(index)
            l.insert(index, w.value)

    def del_(self):
        l = self.view.list
        try:
            [index] = l.curselection()
        except ValueError:
            return
        l.delete(index)
        l.select_set(max(index, l.size() - 1))

    def up(self):
        l = self.view.list
        try:
            [index] = l.curselection()
        except ValueError:
            return
        if index > 0:
            v = l.get(index)
            l.delete(index)
            l.insert(index - 1, v)
            l.select_set(index - 1)

    def down(self):
        l = self.view.list
        try:
            [index] = l.curselection()
        except ValueError:
            return
        if index < l.size() - 1:
            v = l.get(index)
            l.delete(index)
            l.insert(index + 1, v)
            l.select_set(index + 1)

    def getlist(self):
        return [self.view.list.get(i) for i in range(self.view.list.size())]

    def setlist(self, list_):
        self.view.list.delete(0, tkinter.END)
        for i, v in enumerate(list_):
            self.view.list.insert(i, v)
