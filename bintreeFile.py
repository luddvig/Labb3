class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Bintree:
    """Klass för binärt sökträd. Instansvariabel root. Metoder put, contains och write."""
    def __init__(self):
        self.__root = None      # Privat, vill inte manipulera  utanför klass.

    def put(self, newvalue):
        self.__root = putta(self.__root, newvalue)  # Kallar på hjälpfunktion putta, vill addera value.

    def __contains__(self, value):
        return finns(self.__root, value)  # Kallar på hjälpfunktion finns, söker value.

    def write(self):            # Kallar på hjälpfunktion
        skriv(self.__root)
        print("\n")


def putta(root, value): # Tar in rot för binärt träd samt värde att lägga till
    # Jämför värden från rot nedåt till korrekt plats hittas att placera value, rekursivt
    if root == None:
        return TreeNode(value)
    else:
        if root.value == value:
            return root
        elif root.value > value:
            root.left = putta(root.left, value)
        else:
            root.right = putta(root.right, value)
    return root


def finns(root, value):   # Tar in rot för binärt träd samt värde att söka efter
    # Binärsök i trädet efter value, rekursivt
    if root == None:
        return False
    else:
        if value == root.value:
            return True
        elif value < root.value:
            return finns(root.left, value)
        else:
            return finns(root.right, value)


def skriv(root):
    # Går igenom trädet och skriver up i inorder (LPR), rekursivt
    if root == None:
        return None
    else:
        skriv(root.left)
        print(root.value)
        skriv(root.right)

