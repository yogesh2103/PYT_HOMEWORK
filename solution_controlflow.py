{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "44b01602",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The number is even\n"
     ]
    }
   ],
   "source": [
    "#Exercise 1\n",
    "#Write a program that prints whether a number is even or odd.\n",
    "#We can use the modulus operator (%) to check the remainder.\n",
    "\n",
    "a = 10\n",
    "a = a%2\n",
    "\n",
    "if a==0:\n",
    "    print('The number is even')\n",
    "else:\n",
    "    print('The number is odd')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "060b1da1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Exercise 2\n",
    "\n",
    "x = 8\n",
    "y = 0\n",
    "a = \"Hello!\"\n",
    "b = \"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "32ae5d7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check if x and b are both True. If they are, print \"Both of these are true.\"\n",
    "if x==True and b==True:\n",
    "    print('Both of these are true.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "109d5c2e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "One of these is false.\n"
     ]
    }
   ],
   "source": [
    "# Check if y or a is False. If one is, print \"One of these is false.\"\n",
    "if y==False or a==False:\n",
    "    print('One of these is false.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "75cad9fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "One is false.\n"
     ]
    }
   ],
   "source": [
    "# Check if either x or y is False. If one is, print out \"One is false.\"\n",
    "if x==False or y==False:\n",
    "    print('One is false.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0881b72d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x is greater than y.\n"
     ]
    }
   ],
   "source": [
    "# Then, only if either x or y is False, check if x is greater than y. If it is, print out \"x is greater than y.\"\n",
    "if x==False or y==False:\n",
    "    if x>y:\n",
    "        print ('x is greater than y.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8c96418",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
