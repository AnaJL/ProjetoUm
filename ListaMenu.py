from Node import No
from Cdados import Dadu
import time

class Lista:
    def __init__(self, head = None):  #Construtor
        self._head = head
        self._size = 0

    def mostrar(self, index):  #Mostra de acordo com o index
        p = self._head
        if p == None:
            print(' Lista Vazia ')
        elif index > self.length()-1:
            print(' Indice invalido')
        elif index < self.length():
            for i in range(index):
                if p.get_proximo() != None:
                    p = p.get_proximo()
            print(p.get_dado().get_filmeeano())



    def mostrarano(self, index):  #Mostra de acordo com o index
        p = self._head
        a = self
        for i in range(index):
            if p.get_proximo() != None:
                p = p.get_proximo()
        return p.get_dado().get_ano()
    def isEmpty(self): #Vazia
        if self.length() == 0:
            return True
        else: return False
    def insert(self, index, elem): #Inserir
            if self._head == None:
                no = No(elem)
                no.set_proximo(None)
                self._head = no
            if index > self.length():
                print ( ' indice invalido ')
            if index == 0:
                no = No(elem)
                no.set_proximo(self._head)
                self._head = no
            else:
                no = No(elem)
                q = self._head
                for i in range(index -1):
                    if q.get_proximo() != None:
                        q = q.get_proximo()
                no.set_proximo(q.get_proximo())
                q.set_proximo(no)
    def remove(self,index): #Remover um item no indice
        p = self._head
        if self.length() == 0:
            print(' A lista ja está vazia ')
        elif index == 0:
            p = self._head
            if p != None:
                self._head = self._head.get_proximo()
        elif index > self.length():
            print ( ' indice invalido ')
        elif p != None:
            q = self._head.get_proximo()
            for i in range(index - 1):
                q = q.get_proximo()
                p = p.get_proximo()
            if q != None:
                p.set_proximo(q.get_proximo())
                q.set_proximo(p)
                
    def ordenar(self):
        ordem = False
        while not ordem:
            ordem = True
            p = self._head
            q = p.get_proximo()
            while q.get_proximo() != None:
                if p.get_dado().get_ano() > q.get_dado().get_ano():
                    ordem = False
                    aux = p.get_dado()
                    p.set_dado(q.get_dado())
                    q.set_dado(aux)
                p = q
                q = q.get_proximo()
    def length(self):
        p =self._head
        count = 0
        if p != None:
            while p.get_proximo() != None :
                p =p.get_proximo()
                count+=1
        return count
    def printar_all(self):
        p = self._head
        i = 0
        if p == None:
            print(' Lista Vazia')
        elif p != None:
            while(p.get_proximo() != None):
                print(f' pos: {i} -> {p.get_dado().get_filmeeano()}')
                i +=1
                p = p.get_proximo()

print("IFPB - Instituto Federal da Paraiba ")
print("-=-"*20)
lis = Lista()
r = input(""" 
\033[1;34m ________________________________\033[m
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▀█▀ ▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▒█░ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█▄▄█ ▄█▄ ▒█▄▄▄█ ░▒█░░ ▒█░▒█  \033[m\033[1;34m|\033[m     
\033[1;34m|________________________________|\033[m
\033[1;34m|\033[m  \033[1;36m0)\033[m \033[1;31msair do Menu\033[m               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m1)\033[m adicionar                  \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m2)\033[m remover                    \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m3)\033[m Mostrar se está vazia      \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m4)\033[m Mostrar tamanho da Lista   \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m5)\033[m Mostrar tudo               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m6)\033[m Mostrar por indice         \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m7)\033[m Deixar a lista ordenada    \033[1;34m|\033[m 
\033[1;34m|________________________________|\033[m 
\033[1;31m🔴\033[m Digite sua opção: 
""")
while (r != '0') :
    if r == "1":
        a = input("Qual FILME você quer adicionar: ")

        b = int(input("Qual ANO você quer adicionar: "))
        i = int(input("Qual a posição que deseja adicionar ?")) 
        lis.insert(i, Dadu(a,b))
        print("...")
        time.sleep(1)
        r = input(""" 
\033[1;34m ________________________________\033[m
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▀█▀ ▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▒█░ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█▄▄█ ▄█▄ ▒█▄▄▄█ ░▒█░░ ▒█░▒█  \033[m\033[1;34m|\033[m     
\033[1;34m|________________________________|\033[m
\033[1;34m|\033[m  \033[1;36m0)\033[m \033[1;31msair do Menu\033[m               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m1)\033[m adicionar                  \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m2)\033[m remover                    \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m3)\033[m Mostrar se está vazia      \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m4)\033[m Mostrar tamanho da Lista   \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m5)\033[m Mostrar tudo               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m6)\033[m Mostrar por indice         \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m7)\033[m Deixar a lista ordenada    \033[1;34m|\033[m 
\033[1;34m|________________________________|\033[m 
\033[1;31m🔴\033[m Digite sua opção: 
""")
    elif r == "2":
        print("...")
        time.sleep(1)
        i = int(input("De qual indice deseja remover?"))
        lis.remove(i)
        print("...")
        time.sleep(1)
        r = input(""" 
\033[1;34m ________________________________\033[m
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▀█▀ ▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▒█░ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█▄▄█ ▄█▄ ▒█▄▄▄█ ░▒█░░ ▒█░▒█  \033[m\033[1;34m|\033[m     
\033[1;34m|________________________________|\033[m
\033[1;34m|\033[m  \033[1;36m0)\033[m \033[1;31msair do Menu\033[m               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m1)\033[m adicionar                  \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m2)\033[m remover                    \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m3)\033[m Mostrar se está vazia      \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m4)\033[m Mostrar tamanho da Lista   \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m5)\033[m Mostrar tudo               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m6)\033[m Mostrar por indice         \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m7)\033[m Deixar a lista ordenada    \033[1;34m|\033[m 
\033[1;34m|________________________________|\033[m 
\033[1;31m🔴\033[m Digite sua opção: 
""")
    elif r =="3":
        print(lis.isEmpty())
        r = input(""" 
\033[1;34m ________________________________\033[m
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▀█▀ ▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▒█░ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█▄▄█ ▄█▄ ▒█▄▄▄█ ░▒█░░ ▒█░▒█  \033[m\033[1;34m|\033[m     
\033[1;34m|________________________________|\033[m
\033[1;34m|\033[m  \033[1;36m0)\033[m \033[1;31msair do Menu\033[m               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m1)\033[m adicionar                  \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m2)\033[m remover                    \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m3)\033[m Mostrar se está vazia      \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m4)\033[m Mostrar tamanho da Lista   \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m5)\033[m Mostrar tudo               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m6)\033[m Mostrar por indice         \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m7)\033[m Deixar a lista ordenada    \033[1;34m|\033[m 
\033[1;34m|________________________________|\033[m 
\033[1;31m🔴\033[m Digite sua opção: 
""")
    elif r == "4":
        print("O tamanho da lista é: ",lis.length())
        r = input(""" 
\033[1;34m ________________________________\033[m
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▀█▀ ▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▒█░ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█▄▄█ ▄█▄ ▒█▄▄▄█ ░▒█░░ ▒█░▒█  \033[m\033[1;34m|\033[m     
\033[1;34m|________________________________|\033[m
\033[1;34m|\033[m  \033[1;36m0)\033[m \033[1;31msair do Menu\033[m               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m1)\033[m adicionar                  \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m2)\033[m remover                    \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m3)\033[m Mostrar se está vazia      \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m4)\033[m Mostrar tamanho da Lista   \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m5)\033[m Mostrar tudo               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m6)\033[m Mostrar por indice         \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m7)\033[m Deixar a lista ordenada    \033[1;34m|\033[m 
\033[1;34m|________________________________|\033[m 
\033[1;31m🔴\033[m Digite sua opção: 
""")
    elif r == "5":
        lis.printar_all()
        r = input(""" 
\033[1;34m ________________________________\033[m
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▀█▀ ▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▒█░ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█▄▄█ ▄█▄ ▒█▄▄▄█ ░▒█░░ ▒█░▒█  \033[m\033[1;34m|\033[m     
\033[1;34m|________________________________|\033[m
\033[1;34m|\033[m  \033[1;36m0)\033[m \033[1;31msair do Menu\033[m               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m1)\033[m adicionar                  \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m2)\033[m remover                    \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m3)\033[m Mostrar se está vazia      \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m4)\033[m Mostrar tamanho da Lista   \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m5)\033[m Mostrar tudo               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m6)\033[m Mostrar por indice         \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m7)\033[m Deixar a lista ordenada    \033[1;34m|\033[m 
\033[1;34m|________________________________|\033[m 
\033[1;31m🔴\033[m Digite sua opção: 
""")
    elif r == "6":
        i = int(input('Qual indice do elemento que deseja ver ?'))
        lis.mostrar(i)
        r = input(""" 
\033[1;34m ________________________________\033[m
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▀█▀ ▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▒█░ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█▄▄█ ▄█▄ ▒█▄▄▄█ ░▒█░░ ▒█░▒█  \033[m\033[1;34m|\033[m     
\033[1;34m|________________________________|\033[m
\033[1;34m|\033[m  \033[1;36m0)\033[m \033[1;31msair do Menu\033[m               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m1)\033[m adicionar                  \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m2)\033[m remover                    \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m3)\033[m Mostrar se está vazia      \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m4)\033[m Mostrar tamanho da Lista   \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m5)\033[m Mostrar tudo               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m6)\033[m Mostrar por indice         \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m7)\033[m Deixar a lista ordenada    \033[1;34m|\033[m 
\033[1;34m|________________________________|\033[m 
\033[1;31m🔴\033[m Digite sua opção: 
""")
    elif r == "7":
        lis.ordenar()
        print("...")
        time.sleep(1)
        print('A lista foi ordenada com sucesso !')
        r = input(""" 
\033[1;34m ________________________________\033[m
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▀█▀ ▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▒█░ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█▄▄█ ▄█▄ ▒█▄▄▄█ ░▒█░░ ▒█░▒█  \033[m\033[1;34m|\033[m     
\033[1;34m|________________________________|\033[m
\033[1;34m|\033[m  \033[1;36m0)\033[m \033[1;31msair do Menu\033[m               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m1)\033[m adicionar                  \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m2)\033[m remover                    \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m3)\033[m Mostrar se está vazia      \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m4)\033[m Mostrar tamanho da Lista   \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m5)\033[m Mostrar tudo               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m6)\033[m Mostrar por indice         \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m7)\033[m Deixar a lista ordenada    \033[1;34m|\033[m 
\033[1;34m|________________________________|\033[m 
\033[1;31m🔴\033[m Digite sua opção: 
""")
    else:
        print('Opção invalida')
        r = input(""" 
\033[1;34m ________________________________\033[m
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▀█▀ ▒█▀▀▀█ ▀▀█▀▀ ░█▀▀█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█░░░ ▒█░ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄█ \033[m \033[1;34m|\033[m    
\033[1;34m|\033[m  \033[1;36m▒█▄▄█ ▄█▄ ▒█▄▄▄█ ░▒█░░ ▒█░▒█  \033[m\033[1;34m|\033[m     
\033[1;34m|________________________________|\033[m
\033[1;34m|\033[m  \033[1;36m0)\033[m \033[1;31msair do Menu\033[m               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m1)\033[m adicionar                  \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m2)\033[m remover                    \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m3)\033[m Mostrar se está vazia      \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m4)\033[m Mostrar tamanho da Lista   \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m5)\033[m Mostrar tudo               \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m6)\033[m Mostrar por indice         \033[1;34m|\033[m 
\033[1;34m|\033[m  \033[1;36m7)\033[m Deixar a lista ordenada    \033[1;34m|\033[m 
\033[1;34m|________________________________|\033[m 
\033[1;31m🔴\033[m Digite sua opção: 
""")