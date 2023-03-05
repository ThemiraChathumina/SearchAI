import random

class DependencyGenerator:

    def __init__(self, size):
        self.size = size
        self.tasks = [i for i in range(1,size+1)]
        self.dependencies = []

        random.shuffle(self.tasks)

    def generate_random_dependencies(self):
        self.dependencies = []
        for i in range(self.size-1):
            for j in range(i+1, self.size):
                if random.randint(0,1):
                    self.dependencies.append((self.tasks[i], self.tasks[j]))

    def print_dependencies(self, filename):
        formatted_dependencies = ["task {}-->task {}\n".format(i, j) for (i, j) in self.dependencies]
        with open(filename, "w") as f:
            f.writelines(formatted_dependencies)
        with open("valid"+filename, "w") as f:
            f.write(",".join(["task {}".format(i) for i in self.tasks]))


if __name__ == "__main__":
    dg = DependencyGenerator(20)
    dg.generate_random_dependencies()
    dg.print_dependencies("input1.txt")