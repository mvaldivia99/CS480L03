
class MyParser():
        
    # input validation
    def callback(self, a):
        if a.isdigit():
            return True
        elif a == "*" or a == "+" or a == "-" or a == "/":
            return True
        elif a == "":
            return True
        else:
            return False
