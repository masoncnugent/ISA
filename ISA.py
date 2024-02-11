#-------------------------------------------
# USCC Headquarter's Instruction Set Architecture
#  System Design:
#   - Four function calculator
#   - Can only operate on numbers stored in registers
#   - Processor receives binary data as 32-bit strings
#   - Returns results to the terminal
#   - Can operate on 10-bit numbers (0 thru 1023)
#   - Results can be negative (5 - 10 = -5)
#  Instruction format:
#   - 32 bit's in length
#   - Binary data will come to the CPU as a string
#   - Registers (32 total on CPU, 0-indexed)
#      - 0 thru 21:  Available for number storage
#        - 0: Constant 0
#      - 22 thru 31: Available for history storage
# +=======+=======+=======+=======+=======+=======+=======+=======+
# | 0: 0  | 1:    | 2:    | 3:    | 4:    | 5:    | 6:    | 7:    |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# | 8:    | 9:    |10:    |11:    |12:    |13:    |14:    |15:    |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# |16:    |17:    |18:    |19:    |20:    |21:    |22: H0 |23: H1 |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# |24: H2 |25: H3 |26: H4 |27: H5 |28: H6 |29: H7 |30: H8 |31: H9 |
# +=======+=======+=======+=======+=======+=======+=======+=======+
#   - Bits 0-5 are OPCODEs
#     - use variable 'opcode' in program
#   - Bits 6-10 & 11-15 are source register locations
#     - use variables 'source_one' and 'source_two' in program
#   - Bits 16-25 are reserved for adding a new value to the registers
#     - use variable 'store' in program
#   - Bits 26-31 are functions
#     - use variable 'function_code' in program
# +--------+----------+-------------------------------------+
# | OPCODE | FUNCTION | Definition                          |
# | 000000 |  100000  | Add two numbers from registers      |
# | 000000 |  100010  | Subtract two numbers from registers |
# | 000000 |  011000  | Multiply two numbers from registers |
# | 000000 |  011010  | Divide two numbers from registers   |
# | 000001 |  000000  | Store value to next register        |
# | 100001 |  000000  | Return previous calculation         |
# +--------+----------+-------------------------------------+

# Your code below here:
class UltraSuperCalculator:
  def __init__(self, name):
    self.name = name
    self.number_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.history_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.numbers_index = 1
    self.history_index = 0
    self.temp_history_index = 0
    self.user_display = ""

    self.update_display("Hello, " + self.name + "!!!")



  def update_display(self, to_update):
    self.user_display = to_update
    print(self.user_display)



  def store_value_to_next_register(self, value_to_store):
    if self.numbers_index > 21:
      self.numbers_index = 1
    
    self.number_registers[self.numbers_index] = int(value_to_store, 2)
    self.update_display(str(int(value_to_store, 2)) + " was stored in register " + str(self.numbers_index))

    self.numbers_index += 1


  #assumes the value_to_store is in the binary type and the store
  def store_value_to_specific_register(self, value_to_store, register_store):
    number_register_index = int(register_store, 2)
    if 21 > number_register_index > 0:
      #this m
      self.number_registers[number_register_index] = int(value_to_store, 2)
      self.update_display(str(int(value_to_store, 2)) + " was stored in register " + str(number_register_index))

      
    else:
      self.update_display("The register address" + str(register_store) + " corresponds to an index of " + str(register_index) + ", which is not between 1 and 20 inclusive.")



  def load_value_from_register(self, register_address):
    index = int(register_address, 2)
    print("below this is the index that is loaded")
    print(index)
    #the int below this might not be needed
    int_value = self.number_registers[index]
    return int_value
  


  def store_to_history_registers(self, result_to_store):
    if self.history_index > 9:
      self.history_index = 0

    self.history_registers[self.history_index] = bin(result_to_store)

    self.history_index += 1

    self.temp_history_index = self.history_index



  def add(self, register_source, register_two):
    num1 = self.load_value_from_register(register_source)
    num2 = self.load_value_from_register(register_two)
    print("below this are num1 and num2")
    print(num1)
    print(num2)
    print("we are doing addition")
    calculated_value = num1 + num2
    return calculated_value

  def subtract(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    print("below this are num1 and num2")
    print(num1)
    print(num2)
    print("we are doing subtraction")
    calculated_value = num1 - num2
    return calculated_value

  def multiply(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    print("below this are num1 and num2")
    print(num1)
    print(num2)
    print("we are doing multiplication")
    calculated_value = num1 * num2
    return calculated_value

  def divide(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    print("below this are num1 and num2")
    print(num1)
    print(num2)
    print("we are doing division")
    if num2 != 0:
      calculated_value = int(num1 / num2)
      print(calculated_value)
    else:
      print(f"Division by 0 error: {num1}/{num2}.")
      calculated_value = 0
    
    return calculated_value
  
  def add_intermediate (self,)



  def get_last_calculation(self):
    if self.temp_history_index > 0:
      self.temp_history_index -= 1
    else:
      self.update_display("No further history to display, showing oldest calculation")
    print(self.history_registers)
    print(self.temp_history_index)
    last_value = "The previous calculation was: " + str(int(self.history_registers[self.temp_history_index], 2))

    self.update_display(last_value)



  def binary_reader(self, instruction):
    print("\nraw instruction is " + instruction)
    if len(instruction) != 32:
      self.update_display("Invalid Instruction Length: Instruction was " + str(len(instruction)) + " characters long")
      return
    else:

      #attempted re-write using the opcode to determine how to format the remaining 28 bits
      #adding, dividing, multiplying, and subtracting can use the same formatting

      opcode = instruction[0:6]
      if opcode == "000000":


      elif opcode == "000001":
        register_source = instruction[6:11]
        register_two = instruction[11:16]
        register_destination = instruction[16:21]
        unused_code = instruction[21:26]
        function_code = instruction[26:]

        if unused_code != "00000":
          self.update_display("Data entered into unused code region and subsequently ignored.")

        #ADD case
        result = None
        if function_code == "000001":
          result = self.add(register_source, register_two)
          self.store_value_to_specific_register(result, register_destination)






























      opcode = instruction[0:6]
      source_one = instruction[6:11]
      source_two = instruction[11:16]
      store = instruction[16:26]
      function_code = instruction[26:]
      print("the opcode is " + str(opcode))
      print("source_one is " + str(source_one))
      print("source_two is " + str(source_two))
      print("store is " + str(store))
      print("the function code is " + str(function_code))

      if opcode == "000001":
        self.store_value_to_next_register(store)
        return
      elif opcode == "100001":
        self.get_last_calculation()
        return
      elif opcode != "000000":
        print(opcode)
        self.update_display("Invalid OPCODE")
        return

      result = 0
      if function_code == "100000":
        result = self.add(source_one, source_two)
      elif function_code == "100010":
        result = self.subtract(source_one, source_two)
      elif function_code == "011000":
        result = self.multiply(source_one, source_two)
      elif function_code == "011010":
        result = self.divide(source_one, source_two)
      else:
        if opcode == "000001":
            self.store_value_to_next_register(store)
            return
        #test code for storing a value to a specified register, using source_two as that register
        elif opcode == "000010"

        else:
            self.update_display("Invalid function code")

      self.store_to_history_registers(result)
      self.update_display("The result of the operation is " + str(result))



masons_calculator = UltraSuperCalculator("Mason")



# Adds 5 and 10 to number registers
masons_calculator.binary_reader("00000100000000000000000101000000")
masons_calculator.binary_reader("00000100000000000000001010000000")
print(masons_calculator.number_registers)

# Adds/Subtracts/Multiplies/Divides 5 and 10 from registers
#masons_calculator.binary_reader("000000 00001 00010 0000000000 100000")
masons_calculator.binary_reader("00000000001000100000000000100000")
masons_calculator.binary_reader("00000000001000100000000000100010")
masons_calculator.binary_reader("00000000001000100000000000011000")
masons_calculator.binary_reader("00000000001000100000000000011010")

# Gets the last four calculations

masons_calculator.binary_reader("10000100000000000000000000000000")
masons_calculator.binary_reader("10000100000000000000000000000000")
masons_calculator.binary_reader("10000100000000000000000000000000")
masons_calculator.binary_reader("10000100000000000000000000000000")

#tests the exception handling of loading more history than exists
masons_calculator.binary_reader("10000100000000000000000000000000")
masons_calculator.binary_reader("10000100000000000000000000000000")