class UVSim:
    r0pc = 0
    r1acc = 0
    halted = False
    mem = [0] * 100

    def input_program(self):
        continue_input = True
        index = 0
        while index < 100:
            print("{i:02d}: ".format(i=index), end='')
            entered = int(input())
            if entered == -99999:
                index = 100
            else:
                self.mem[index] = entered
                index += 1

    def run(self):
        while not self.halted:
            self.step()

    def step(self):
        instruction = self.mem[self.r0pc]
        if instruction < 0:
            raise ValueError("INVALID INSTRUCTION AT MEMORY LOCATION {i:02d}".format(self.r0pc))
        opcode = instruction // 100
        operand = instruction % 100
        if opcode == 10:
            self.read(operand)
        elif opcode == 11:
            self.write(operand)
        elif opcode == 20:
            self.load(operand)
        elif opcode == 21:
            self.store(operand)
        elif opcode == 30:
            self.add(operand)
        elif opcode == 31:
            self.subtract(operand)
        elif opcode == 32:
            self.divide(operand)
        elif opcode == 33:
            self.multiply(operand)
        elif opcode == 40:
            self.branch(operand)
        elif opcode == 41:
            self.branchneg(operand)
        elif opcode == 42:
            self.branchzero(operand)
        elif opcode == 43:
            self.halt()
        else:
            raise ValueError("INVALID INSTRUCTION AT MEMORY LOCATION {i:02d}".format(self.r0pc))

    def read(self, loc):
        self.mem[loc] = int(input("INPUT: "))
        self.r0pc += 1

    def write(self, loc):
        print("OUTPUT: {}".format(self.mem[loc]))
        self.r0pc += 1

    def load(self, loc):
        self.r1acc = self.mem[loc]
        self.r0pc += 1

    def store(self, loc):
        self.mem[loc] = self.r1acc
        self.r0pc += 1

    def add(self, loc):
        self.r1acc = self.r1acc + self.mem[loc]
        self.r0pc += 1

    def subtract(self, loc):
        self.r1acc = self.r1acc - self.mem[loc]
        self.r0pc += 1

    def divide(self, loc):
        self.r1acc = self.r1acc // self.mem[loc]
        self.r0pc += 1

    def multiply(self, loc):
        self.r1acc = self.r1acc * self.mem[loc]
        self.r0pc += 1

    def branch(self, loc):
        self.r0pc = loc

    def branchneg(self, memloc):
        if self.r1acc < 0:
            self.r0pc = memloc
        else:
            self.r0pc += 1

    def branchzero(self, memloc):
        if self.r1acc == 0:
            self.r0pc = memloc
        else:
            self.r0pc += 1

    def halt(self):
        self.halted = True

    def memdump(self):
        print("R0 - Program Counter: {j:+05d}".format(j=self.r0pc))
        print("R1 - Accumulator: {j:+05d}".format(j=self.r1acc))
        print("  ", end='')
        for col in range(0,10):
            print("|   {c:02d}  ".format(c=col), end='')
        print('')
        for index, memloc in enumerate(self.mem):
            if index % 10 == 0:
                print("{i:02d}".format(i=index//10 * 10), end='')
            print("| {j:+05d} ".format(i=index, j=memloc), end='')
            if index % 10 == 9:
                print('')
                
c = UVSim()

c.input_program()
c.run()
c.memdump()

input("Press enter to exit...")