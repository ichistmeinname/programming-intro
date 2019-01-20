# In der Vorlesung wurde das folgende Python-Programm zur Berechnung des *größten gemeinsamen Teilers (ggT)* mit dem *Euklidischen Algorithmus* vorgestellt, welches wir in dieser Aufgabe auf sein Verhalten für negative Zahlen untersuchen wollen:  

# ~~~{.Python}
# a = -6                            #1
# b = -9                            #2

# while a != 0 and b != 0:          #3
#   if a < b:                       #4
#     b = b - a                     #5
#   else:                           #6
#     a = a - b                     #7

# if a == 0:                        #8
#   if b == 0 :                     #9
#     print("ggT nicht definiert")  #10
#   else:                           #11
#     print(b)                      #12

# else:                             #13
#   print(a)                        #14
# ~~~

# **(a)** Simulieren Sie den Ablauf des Programms in einer Programmablauftabelle, soweit es Sinn macht.

# **(b)** Korrigieren Sie das Programm, so dass es gemäß der ggT-Definition der Vorlesung (erweitert auf positive und negative ganze Zahlen) das richtige Ergebnis liefert. Geben Sie das korrigierte Programm ab und vergessen Sie nicht, Ihre Änderungen zu erklären.

# **Hinweis:** Programmzeilen, die nur Erklärungen bzw. Kommentare von Ihnen enthalten, können Sie mit dem Zeichen `#` einleiten. Python ignoriert dann den Rest der Zeile anstatt zu versuchen, sie als Python-Code zu interpretieren.
