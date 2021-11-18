import argparse
def passs(val):   
    up = 0
    lo = 0
    schar = 0
    digi = 0
   
    if len(val)>7:
       
       
        for ele in val:
            if (ele.islower()):
                lo+=1
            if (ele.isupper()):
                up+=1
            if (ele.isdigit()):
                digi+=1
            if (ele == '@' or ele == '$' or ele == '!'):
                schar+=1
       
    else:
        assert len(val)>7, 'Password parameter can accept only val greater than 7'
       
       
    if (up>=1 and lo>=1 and digi>=1 and schar>=1):
        print("Valid password")
    else:
        print("Invalid password")
           
parser = argparse.ArgumentParser(description = 'Enter the valid password')
parser.add_argument('-p', '--password', type=str, metavar="", help='Type valid password')
args = parser.parse_args()

passs(args.password)

