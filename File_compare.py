import difflib as dl
from colorama import Fore


"""
Open the PRE and POST config back up files
"""

def pre_post_comp(pre_checks,post_checks):
    with open(pre_checks, 'r') as f1:
        list1 = f1.readlines()
    with open(post_checks, 'r') as f2:
        list2 = f2.readlines()

    for diff in dl.context_diff(list2,list1):

        if diff.startswith('+ '):
            print(Fore.GREEN,diff)

        if diff.startswith('- '):
            print(Fore.RED,diff)



if __name__=='__main__':
    pre_post_comp('192.168.64.10_POST.txt','192.168.64.10_PRE.txt')


