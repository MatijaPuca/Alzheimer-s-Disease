class Navigation(object):
     pass

current_view = None

def set(view):
     global current_view
     current_view = view

def show():
     global current_view
     current_view.show()

def close():
     global current_view
     current_view.close()
     
def get():
     global current_view
     return current_view