def weight_on_planets():
   user_input = input("What do you weigh on earth? ")
   weight = int(user_input)

   print("\n"
         "On Mars you would weigh %.2f pounds.\n" 
         "On Jupiter you would weigh %.2f pounds.\n" 
         % (weight * 0.38, weight * 2.34))
   
if __name__ == '__main__':
   weight_on_planets()