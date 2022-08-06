Cadastro=[]

while True:
    
    Ca=input("Insira o nome completo do aluno, ou para encerrar a coleta de nomes, digite P: ")
    if (Ca == 'P') or (Ca == 'p'):
        print("Processo encerrado")
        break
    else:
        Cadastro.append(Ca)
        

#Pesquisa
while True:
    NC=input("Gostaria de Fazer alguma pesquisa? Responda com Sim ou Não: ")
    if (NC== 'Sim') or (NC== 'sim') or (NC== 'S') or (NC=='s'):
        try:
            Ca=input("Insira o nome completo do aluno: ")
            print("O {} está localizado no índice {}".format(Ca,Cadastro.index(Ca)))
        except:
            print("Nome não encontrado")
    elif (NC== 'Não') or (NC== 'não') or (NC== 'N') or (NC=='n') or (NC=="nao") or (NC=="Nao"):
        break
    else:
        print("Resposta inválida")
        
