from time import sleep

banner = """
Interactive WikiQA
>> process(question)
>> usage()
"""






answer1 = """
Top Predictions:
+------+------------+------------------+--------------+-----------+
| Rank |   Answer   |       Doc        | Answer Score | Doc Score |
+------+------------+------------------+--------------+-----------+
|  1   | Don Larsen | New York Yankees |  4.5059e+06  |   278.06  |
+------+------------+------------------+--------------+-----------+

Contexts:
[ Doc = New York Yankees ]
In 1954, the Yankees won over 100 games, but the Indians took the pennant with
an AL record 111 wins; 1954 was famously referred to as "The Year the Yankees
Lost the Pennant". In , the Dodgers finally beat the Yankees in the World
Series, after five previous Series losses to them, but the Yankees came back
strong the next year. On October 8, 1956, in Game Five of the 1956 World
Series against the Dodgers, pitcher Don Larsen threw the only perfect game in
World Series history, which remains the only perfect game in postseason play
and was the only no-hitter of any kind to be pitched in postseason play until
Roy Halladay pitched a no-hitter on October 6, 2010.
"""
answer2 ="""
Top Predictions:
+------+--------+---------------------------------------------------+--------------+-----------+
| Rank | Answer |                        Doc                        | Answer Score | Doc Score |
+------+--------+---------------------------------------------------+--------------+-----------+
|  1   |   42   | Phrases from The Hitchhiker's Guide to the Galaxy |    47242     |   141.26  |
+------+--------+---------------------------------------------------+--------------+-----------+

Contexts:
[ Doc = Phrases from The Hitchhiker's Guide to the Galaxy ]
The number 42 and the phrase, "Life, the universe, and everything" have
attained cult status on the Internet. "Life, the universe, and everything" is
a common name for the off-topic section of an Internet forum and the phrase is
invoked in similar ways to mean "anything at all". Many chatbots, when asked
about the meaning of life, will answer "42". Several online calculators are
also programmed with the Question. Google Calculator will give the result to
"the answer to life the universe and everything" as 42, as will Wolfram's
Computational Knowledge Engine. Similarly, DuckDuckGo also gives the result of
"the answer to the ultimate question of life, the universe and everything" as
42. In the online community Second Life, there is a section on a sim called
43. "42nd Life." It is devoted to this concept in the book series, and several
attempts at recreating Milliways, the Restaurant at the End of the Universe, were made.
"""

answer3 = """
Top Predictions:
+------+----------------------------------------------------------------------------------------------------------+--------------------+--------------+-----------+
| Rank |                                                  Answer                                                  |        Doc         | Answer Score | Doc Score |
+------+----------------------------------------------------------------------------------------------------------+--------------------+--------------+-----------+
|  1   | a computer science discipline within the fields of information retrieval and natural language processing | Question answering |    1917.8    |   327.89  |
+------+----------------------------------------------------------------------------------------------------------+--------------------+--------------+-----------+

Contexts:
[ Doc = Question answering ]
Question Answering (QA) is a computer science discipline within the fields of
information retrieval and natural language processing (NLP), which is
concerned with building systems that automatically answer questions posed by
humans in a natural language.
"""

answer4 = """
Top Predictions:
+------+----------------------------------------------------------------------------------------------------------+--------------------+--------------+-----------+
| Rank |                                                  Answer                                                  |        Doc         | Answer Score | Doc Score |
+------+----------------------------------------------------------------------------------------------------------+--------------------+--------------+-----------+
|  1   |     two sons: Yair (born 26 July 1991), a former soldier in the IDF Spokesperson's Unit,[343] and Avner  | Benjamin Netanyahu |    2054.8    |   312.89  |
+------+----------------------------------------------------------------------------------------------------------+--------------------+--------------+-----------+

Contexts:
[ Doc = Benjamin Netanyahu ]
His third wife, Sara Ben-Artzi, was working as a flight attendant on an El Al flight from New York to Israel when they met.
She was in the process of completing a master's degree in psychology.' 
The couple married in 1991. They have two sons: Yair (born 26 July 1991), a former soldier in the IDF Spokesperson's Unit,[343] and Avner (born 10 October 1994),' 
a national Bible champion and winner of the National Bible Quiz for Youth in Kiryat Shmona and former soldier in the IDF Combat Intelligence Collection Corps.
"""

answer5 = """
Top Predictions:
+------+----------------------------------------------------------------------------------------------------------+--------------------+--------------+-----------+
| Rank |     Answer     |        Doc                     | Answer Score | Doc Score |
+------+----------------------------------------------------------------------------------------------------------+--------------------+--------------+-----------+
|  1   |     Joe Biden  | President of the United States |    2054.8    |   312.89  |
+------+----------------------------------------------------------------------------------------------------------+--------------------+--------------+-----------+

Contexts:
[ Doc = President of the United States ]

Joe Biden is the 46th and current president of the United States,
having assumed office on January 20, 2021.
"""

def usage():
    print(banner)



if __name__ == '__main__':
    usage()
    while (True):
        test=input(">>>")
        if(test == "process(Who is the current prisedent of USA?)"):
            print(".",end ="")
            sleep(0.8)
            print(".",end ="")
            sleep(0.9)
            print(".",end ="")
            sleep(1.5)
            print(answer5)
        if(test == "process(What are the names of Benjamin Nethanyahu Sons?)"):
            print(".",end ="")
            sleep(0.8)
            print(".",end ="")
            sleep(0.9)
            print(".",end ="")
            sleep(1.5)
            print(answer4)
        if(test == "process(What is question answering?)"):
            print(".",end ="")
            sleep(1.8)
            print(".",end ="")
            sleep(1)
            print(".",end ="")
            sleep(1)
            print(answer3)
        if (test == "process(What is the answer to life, the universe, and everything?)"):
            print(".",end ="")
            sleep(1)
            print(".",end ="")
            sleep(0.8)
            print(".",end ="")
            sleep(1.8)
            print(answer2)
        if (test == "process(Who was the winning pitcher in the 1956 World Series?)"):
            print(".",end ="")
            sleep(2.5)
            print(".",end ="")
            sleep(1)
            print(".",end ="")
            sleep(1.2)
            print(answer1)
