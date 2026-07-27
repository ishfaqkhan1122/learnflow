#Welcome to the email slicer 
def main():
    print("----------<<Email Slicer>>-----------")
    print("="*40)
    
    email=input("Please enter the email:").strip().lower()
    
    (username,domain)=email.split("@")
    (domain,extention)=domain.split(".")
    
    print("User Name: ",username)
    print("Domain: ",domain)
    print("Extention: ",extention)
    print("="*40)
while True:    
 main()   
    