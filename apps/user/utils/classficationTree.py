import queue

from apps.user.models import Type_id, Goods


class classTree:
    def __init__(self):
        self.graph = None
        self.classId = {}
        self.updateflag = 0

    def gettree(self) -> None:
        edges = Type_id.objects.all()
        for item in edges:
            self.classId[item.class_name] = item.class_id
            if self.graph[item.father_id] is None:
                continue
            if self.graph[item.father_id] is None:
                self.graph[item.father_id] = list()
            self.graph[item.father_id].append(item.class_id)

    def getleafnode(self, className: str) -> list:
        leafnode = []
        if self.graph is None:
            self.getTree()
        u = self.classId[className]
        q = queue.Queue()
        q.put(u)
        while len(queue) != 0:
            s = q.get()
            if len(self.graph[s]) == 0:
                leafnode.append(s)
            for v in self.graph[s]:
                q.put(v)
        return leafnode

    def search(self, classNmae: str) -> list:
        leftnode = self.getleafNode(classNmae)
        goodlist = Goods.objects.filter(class_id__in=leftnode)
        return goodlist


searchUtils = classTree()
