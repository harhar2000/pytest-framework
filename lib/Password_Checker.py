class Password_Checker:
    def check(self, password):
        if len(password) >= 8:
            return True
        else:
            raise Exception("Invalid password, must be 8+ characters.")

# if length of password greater/equal to 8 return True
# else raise exception and print ("Invalid password, must be 8+ characters")