from tkinter import *
from tkinter import ttk

root = Tk()

# for this example the "hidden" column is not hidden
tree = ttk.Treeview(root, columns='datakey')
tree.pack()

# the data (of a newsfeed reader aka newsaggregator)

theData = {
    "childs": [
        {
            "childs": [
                {
                    "childs": [
                        {
                            "htmlUrl": "http://www.news.org",
                            "text": "Newspaper",
                            "title": "Newspaper",
                            "type": "rss",
                            "xmlUrl": "http://www.news.org"
                        }
                    ],
                    "group": "News"
                },
                {
                    "htmlUrl": "https://www.theCinema.org",
                    "text": "Cinema",
                    "title": "Cinema",
                    "type": "atom",
                    "xmlUrl": "http://www.theCinema.org/newsfeed"
                }
            ],
            "group": "Group A"
        },
        {
            "htmlUrl": "http://www.top.org",
            "test": "Top Feed",
            "title": "Top Feed",
            "type": "rss",
            "xmlUrl": "http://www.top.org/feed"
        }
    ]
}


# populate the data into the tree


def _do_refresh_tree_level(data, parent_iid):
    nextParent_iid = parent_iid

    for key in data:
        if key == 'childs':  # CHILDS
            # first create the group
            if 'group' in data.keys():
                nextParent_iid = tree.insert(parent=parent_iid,
                                             index=END,
                                             text=data['group'])
            # each child in the group
            idxCurChild = -1
            for child in data['childs']:
                idxCurChild += 1
                _do_refresh_tree_level(child, nextParent_iid)
        elif key == 'group':  # GROUPS
            pass  # handled in CHILDS section
        else:  # FEED
            iid = tree.insert(parent_iid, index=END, text=data['title'])
            break


_do_refresh_tree_level(theData, '')

root.mainloop()

myData = [
    {
        "group": "A",
        "children": [
            {
                "name": "Tick"
            },
            {
                "group": "B",
                "children": [
                    {
                        "name": "Anna"
                    }
                ]
            }
        ]
    },
    {
        "name": "Bob"
    }
]
