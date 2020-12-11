import queue

from apps.user.models import Type_id, Goods


class ClassTree:
    def __init__(self):
        self.graph = None
        self.classId = {}
        self.updateflag = 0

    def GetTree(self) -> None:
        self.graph = {}
        edges = Type_id.objects.all()
        for item in edges:
            self.classId[item.class_name] = item.class_id
            if item.father_id == 0:
                continue
            if item.father_id not in self.graph:
                self.graph[item.father_id] = list()
            self.graph[item.father_id].append(item.class_id)

    def GetLeafNode(self, className: str) -> list:
        leafnode = []
        if self.graph is None:
            self.GetTree()
        u = self.classId[className]
        q = queue.Queue()
        q.put(u)
        while q.empty() == False:
            s = q.get()
            if s not in self.graph:
                leafnode.append(s)
                continue
            for v in self.graph[s]:
                q.put(v)
        return leafnode

    def search(self, className: str) -> list:
        leftnode = self.GetLeafNode(className)
        goodlist = Goods.objects.filter(class_id__in=leftnode)
        return goodlist
    def getTypeNameById(self,classId:int):
        if self.graph == None:
            self.GetTree()
        type = Type_id.objects.get(class_id=classId);
        if type != None:
            return type.class_name
        return None
    def str2typeid(self, goodstype: str) -> int:
        if self.graph == None:
            self.GetTree()
        if goodstype not in self.classId:
            return -1
        return self.classId[goodstype]


classtree = ClassTree()
