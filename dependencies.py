class Tracker:

    def __init__(self):
        self.map = {}

    def add_direct(self, target, dependencies):
        self.map[target] = dependencies

    def dependencies_for(self, target):
        final_deps = self.map.get(target, []) 
        for dep in final_deps:
            final_deps.extend(self.dependencies_for(dep))            
        return sorted(set(final_deps))

