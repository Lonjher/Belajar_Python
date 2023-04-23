import time
from tqdm import tqdm

print("Loading".center(70))
progress_bar = tqdm(total=100)
for i in range(100):
            time.sleep(0.1)
            progress_bar.update(1)
progress_bar.close()
time.sleep(1)
print("\n")
tittle = " Welcome to My World ".center(50,"=")
line = "="*50
line2 = "\n"+"="*70
icon = ("=>")
print(line)
print (tittle)
print(line)
ansr1 = " Thank You for your attention ".center(50,"=")
ansr2 = " I am sorry for you\'re not the one I hope ".center(50,"=")

name = input ("\nEnter Your Name: ")
print("\nTunggu Sebentar.......\n")
time.sleep(2)
hello = f" Hello {name} ".center(50,"=")
print(hello)

print("\n" + ansr1)
input(f"\n {icon} How are you? ")

question1 = input(f"\n {icon} Do you ready for the question? (yes/no): ")
if question1 == 'yes':
	    print(line2)
	    time.sleep(2)
	    
	    print(" All you know here is what always becomes my thought for long time ".center(70,"="))
	    print("="*70)
else:
	   print("\nYou have probably not been ready for this\n")
	   print(f" Thank You {name} ".center(50,"="))
	   exit()

input(f"\n {icon} How long have you been with me?:\n")
input(f"\n {icon} What do you feel?\n")
input(f"\n {icon} What do you think about me?\n")

question2 = input(f"\n {icon} Have I ever hurt you?: \n")
if question2 == 'yes':
	   print("I first wanna say sorry and I plead for the sake of ny destiny")
else:
	   print("Thank You")
	   
question3 = input("\n ? Do you want to continue for the question?: ")
if question3 == 'no':
	    print("\nThank You very much")
	    exit()
else:
	print("\nOk. Let's continue.....")
	time.sleep(2)
	
input(f"\n {icon} Have I ever accross your thought?")
input(f"\n {icon} Have you realized that I have a deep feeling for you?: ")
input("\n" "Enter!")
question = input (f"\n {icon} So, do you receive my love? (Yes/No) : ")
if question == 'No':
         print("\nI Hope you all the best")
else:
	     print("\nThank You")
