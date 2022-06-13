## Piotr Śliperski
## Zadanie do złudzenia przypomina mi szukanie cyklu hamiltona w grafie, zatem jest to problem NP - trudny
## i wykonałem go metodą brute-force, czyli proóbująć wszyskie opcje, dopóki nie natrafię na tą poprawną
## W rozwiazaniu uzywam rekurencyjnej funkcji sol, która dostaje miedzy innymi parametr come_from
## dzieki ktoremu mogę się dowiedzieć której bramy powinieniem użyć.



from zad7testy import runtests

def find_gate(G,vertex, miasto_z):
    for i in range(2):
        for j in range(len(G[vertex][i])):
            if(G[vertex][i][j] == miasto_z):
                return i
    return -1



global_answ = []
exit_gate=-1



def sol(G,vertex,answer,visited,come_from,n):
    global global_answ
    global exit_gate

    if(len(global_answ) == n):
        return
 
    if(come_from == -1):## przypadek początkowy
        for i in range(2):
            for j in range(len(G[vertex][i])):
                visited[G[vertex][i][j]] = True
                answer.append(G[vertex][i][j])
               # print(G[vertex][i][j])

                exit_gate= i
                sol(G,G[vertex][i][j],answer,visited,vertex,n)
                
                visited[G[vertex][i][j]] = False
                answer.pop() 
    
    
    else:
        gate = find_gate(G,vertex,come_from)



        gate_to_consider = (gate+1)%2


        #print("looped in recursion/? ", vertex)
        for i in range(len(G[vertex][gate_to_consider])):
        
            if(len(answer) == n and G[vertex][gate_to_consider][i] == 0):
                
                gate_at_start = find_gate(G,0,vertex)
                if(gate_at_start == exit_gate):
                    return
         
                global_answ = answer[:]
                return True

            if not visited[G[vertex][gate_to_consider][i]]:
            
                visited[G[vertex][gate_to_consider][i]] = True
                answer.append(G[vertex][gate_to_consider][i])

                sol(G,G[vertex][gate_to_consider][i],answer,visited,vertex,n)
    

                visited[G[vertex][gate_to_consider][i]] = False
                answer.pop()


    




def droga( G ):
    global global_answ
    global_answ = []
    ## liczba miast
    n = len(G)
    ## wjechano z bramy północnej, wjechano z bramy południowej
    visited = [False for i in range(n)]
    visited[0] = True

    answer = [0]

    path = [-1] * n
    path[0] = 0

    ## start
    sol(G,0,answer,visited,-1,n)

    #print(global_answ)

    
    if(len(global_answ) != n):
        global_answ = None




    # tu prosze wpisac wlasna implementacje
    return global_answ

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )