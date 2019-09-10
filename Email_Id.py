{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6 emails collected!\n"
     ]
    }
   ],
   "source": [
    "# Code to Extract the Email-Ids from a Text file\n",
    "\n",
    "import re\n",
    " \n",
    "fileToRead = 'C:\\\\Users\\\\1121710\\\\Downloads\\\\email.txt'\n",
    "fileToWrite = 'C:\\\\Users\\\\1121710\\\\Downloads\\\\emailExtracted.txt'\n",
    " \n",
    " \n",
    "delimiterInFile = [',', ';']\n",
    " \n",
    "def validateEmail(strEmail):\n",
    "    # .* Zero or more characters of any type. \n",
    "    if re.match(\"(.*)@(.*).(.*)\", strEmail):\n",
    "        return True\n",
    "    return False\n",
    " \n",
    "def writeFile(listData):\n",
    "    file = open(fileToWrite, 'w+')\n",
    "    strData = \"\"\n",
    "    for item in listData:\n",
    "        strData = strData+item+'\\n'\n",
    "    file.write(strData)\n",
    " \n",
    "listEmail = []\n",
    "file = open(fileToRead, 'r') \n",
    "listLine = file.readlines()\n",
    "for itemLine in listLine:\n",
    "    item =str(itemLine)\n",
    "    for delimeter in delimiterInFile:\n",
    "        item = item.replace(str(delimeter),' ')\n",
    "     \n",
    "    wordList = item.split()\n",
    "    for word in wordList:\n",
    "        if(validateEmail(word)):\n",
    "            listEmail.append(word)\n",
    " \n",
    "if listEmail:\n",
    "    uniqEmail = set(listEmail)\n",
    "    print(len(uniqEmail),\"emails collected!\")\n",
    "    writeFile(uniqEmail)\n",
    "else:\n",
    "    print(\"No email found.\")\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
