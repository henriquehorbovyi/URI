n1,n2,n3,n4   = input().split(" ")
n1    = float(n1)
n2    = float(n2)
n3    = float(n3)
n4    = float(n4)

ave   = ((n1*2)+(n2*3)+(n3*4)+(n4*1)) / 10
message = None

if(ave >= 7.0):
    print("Media: %0.1f" %ave)
    print("Aluno aprovado.")
elif(ave < 5.0):
    print("Media: %0.1f" %ave)
    print("Aluno reprovado.")
elif(ave >= 5.0 and ave < 7.0):
    print("Media: %0.1f" %ave)
    print("Aluno em exame.")
    exam = float(input())
    print("Nota do exame: %0.1f" %exam)
    ave  = (ave + exam) / 2
    if(ave >= 5.0):
        print("Aluno aprovado.")
    elif(ave < 5.0):
        print("Aluno reprovado.")
    print("Media final: %0.1f" %ave)