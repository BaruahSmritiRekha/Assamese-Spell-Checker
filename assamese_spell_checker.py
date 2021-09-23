# -*- coding: utf-8 -*
"""Libaries"""

import re
import codecs
from tkinter import *
"""List"""

words = []
with codecs.open('Assamese.txt', mode='r',encoding='utf-8') as f:
 for line in f:
    words.append(line.split(' ')[0])

"""Dict"""

w_rank = {}
for i, word in enumerate(words):
    w_rank[word] = i
 
WORDS = w_rank
len(words)

def words(text): return re.findall(r'\w+', text.lower())
 #findall:Return all non-overlapping matches of pattern in string, as a list of strings

def P(word):
    """
    Probability of `word`
    use inverse of rank as proxy, returns 0 if the word isn't in the dictionary
    : word: The word we want the probability for
    :rtype: object
    """
    return  WORDS.get(word, 0)


def known(words):
    """
    The subset of `words` that appear in the dictionary of WORDS
    : words:   List - list of words
    :return:    List - Words that exist in the dictionary
    """
    return set(w for w in words if w in WORDS)

def edits1(word):
    """
    All edits that are one edit away from `word`
    : word(str): input
    :return: set of words that are 1 edit distance way
    """
    letters = 'ঁ  অ	আ	ই	ঈ	উ	ঊ	এ	ঐ	ও	ঔ	ঋ ঌ ক	খ	গ	ঘ	ঙ	চ	ছ	জ	ঝ	ঞ ট	ঠ	ড	ঢ	ণ	ত	থ	দ	ধ	ন প	ফ	ব	ভ	ম	য	ৰ ল	ৱ শ	ষ স	হ	ক্ষ	জ্ঞ	ড়	ঢ়	য়	ৎ   ্	 ং	 ঃ	ৈ : া : ী  ি  ূ  ো  ে  ু  ঃ ক্ক ঙ্ক ল্ক স্ক স্ফ ঙ্খ স্খ ঙ্গ ঙ্ঘ দ্ঘ শ্চ চ্ছ ঞ্ছ ঞ্জ জ্ঞ ল্ট ণ্ঠ ষ্ঠ ণ্ড ষ্ণ ক্ষ প্ত স্ত ক্ত গ্ন ম্ন শ্ন স্ন হ্ন ত্থ ন্থ ষ্থ ন্দ ব্দ ম্প ল্প ষপ স্প ম্ফ স্ফ দ্ব ম্ব হ্বদ্ভ ম্ভ ক্ম দ্ম হ্ম স্ব দ্ধ '
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    """
    All edits that are two edit away from `word`
    : word(str): input
    :return: set of words that are 2 edit distance way
    """
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def candidates(word):
    """
    Generate possible spelling corrections for word
    : word:    Input word
    :return:        All probable candidate words in 1 or 2 edit distance away
    """
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def correction(word):
    """
    Most probable spelling correction for word
    :word:    Incorrect word
    :return:    The most probable candidate
    """
    return max(candidates(word), key=P)

# a=input('Enter Input:')
#
# print(correction(a))

def myClick():
    # get a content from entry box
    a = E1.get()
    b=correction(a)

   # value in the text entry box.
    E2.insert(1,b)


def clearAll():
    # whole content of text entry area is deleted
    E1.delete(0, END)
    E2.delete(0, END)



root = Tk()
root.geometry('600x600')
root.title('Assamese spell Checker')
root.configure(bg='#00ffbf')



ti = Label(root, text="Assamese Spell Checker",font=24)
ti.pack(pady=30)

L1 = Label(root, text="Enter Word",font=24)
L1.pack(pady=10)
E1 = Entry(root,width=50,font=('Helvertica',24))
E1.pack(padx=30,pady=0)


Button1=Button(root,text="Check ",font=20,bg='#03943d',fg='White',command=myClick)
Button1.pack(pady=50)
Button1.config(relief=RAISED, bd=10)


L2 = Label(root, text="Correct Word",font=24)
L2.pack(pady=20)
E2 = Entry(root,width=50,font=('Helvertica',24))
E2.pack(padx=30,pady=0)

Button2=Button(root,text="Clear",font=20,bg='Red',fg='White',command=clearAll)
Button2.pack(pady=50)
Button2.config(relief=RAISED, bd=10)

root.mainloop()




