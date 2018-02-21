memory = [ ] # put code here
while (len(memory) < 100):
   memory.append(0)

accumulator = 0
counter = 0
while True:
   opcode = memory[counter] // 100
   operand = memory[counter] % 100
   if opcode == 10:
      memory[operand] = (int)(input("Enter number: "))
   elif opcode == 11:
      print(memory[operand])
   elif opcode == 20:
      accumulator = memory[operand]
   elif opcode == 21:
      memory[operand] = accumulator
   elif opcode == 30:
      accumulator += memory[operand]
   elif opcode == 31:   
      accumulator -= memory[operand]
   elif opcode == 32:
      accumulator //= memory[operand]
   elif opcode == 33:
      accumulator *= memory[operand]
   elif opcode == 40:
      counter = operand
   elif opcode == 41 and accumulator < 0:
      counter = operand - 1
   elif opcode == 42 and accumulator == 0:
      counter = operand - 1
   elif opcode == 43:
      break
   elif opcode == 50:
      print("PC: " + str(counter))
      print("Accumulator: " + str(accumulator))
      print("Memory:")
      for x in range(0,9):
         line = ""
         for y in range(0,9):
            line += str(memory[10*x+y]).zfill(4) + "  "
         print(line)
   elif opcode == 51:
      print("to do: break")
   elif opcode == 52:
      print("to do: continue")
   counter += 1
