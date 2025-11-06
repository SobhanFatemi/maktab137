class UndoRedoManager:
    def __init__(self) :
        self._do = []
        self._undo = []


    def __enter__(self):
        return self
    

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("action" , self._do)


    def do(self, action):
        self._do.append(action)
        self._undo.clear()
        print(f"{action}")


    def undo(self):
        if not self._do:
            print("nothing to in  to undo")
            return 
        action = self._do.pop()
        self._undo.append(action)
        print(f"undo, {action}")


    def redo(self):
        if not self._undo:
                return 
        action = self._undo.pop()
        self._do.append(action)
        print(f"do, {action}")


#usage

if __name__ == "__main__":
    with UndoRedoManager() as mgr:
        mgr.do("type hello")
        mgr.do("delete 'o'")
        mgr.undo()
        mgr.redo()
