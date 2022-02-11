import random
#Set grid size, total size N*N
N=5
#Set number empty spaces
E=10
#Set proportion black
b=0.3
#Set preference parameter
r=0.5

round=100

initial_color=[[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        rand=random.random()
        if rand<E/N/N:
            initial_color[i][j]="E"
        elif rand<E/N/N+b:
            initial_color[i][j]="B"
        else:
            initial_color[i][j]="W"

color=initial_color

color_code=[[0]*(N+2) for i in range(N+2)]
for i in range(N):
    for j in range(N):
        if color[i][j]=="W":
            color_code[i+1][j+1]=1
        if color[i][j]=="B":
            color_code[i+1][j+1]=-1

white_percent=[[0]*(N) for i in range(N)]
for i in range(N):
    for j in range(N):
        number_of_white=0
        number_of_people=0
        for m in range(-1,2):
            for n in range(-1,2):#n=-1 0 1
                if m!=0 or n!=0:
                    if color_code[i+m+1][j+n+1]==1:
                        number_of_white+=1 
                    number_of_people+=abs(color_code[i+m+1][j+n+1])
        if number_of_people==0:
            white_percent[i][j]=1
        else:
            white_percent[i][j]=number_of_white/number_of_people

#utility=[[0]*(N) for i in range(N)]
#for i in range(N):
#    for j in range(N):
#        if color[i][j]=="W" and white_percent[i][j]>=r:
#            utility[i][j]=1
#        elif color[i][j]=="B" and (1-white_percent[i][j])>=r:
#            utility[i][j]=1
#        elif color[i][j]=="E":
#            utility[i][j]="E"
#        else:
#            utility[i][j]=0
#people_need_to_move=[[1,2],[2,3],[5,9]]
white_need_to_move=[]
black_need_to_move=[]
empty_white_position=[]
empty_black_position=[]
total_utility=N*N
for i in range(N):
    for j in range(N):
        if color[i][j]=="W" and white_percent[i][j]<r:
            white_need_to_move.append([i,j])
            total_utility-=1
        elif color[i][j]=="B" and (1-white_percent[i][j])<r:
            black_need_to_move.append([i,j])
            total_utility-=1
        elif color[i][j]=="E":
            total_utility-=1
            if white_percent[i][j]>=r:
                empty_white_position.append([i,j])
            elif (1-white_percent[i][j])>=r:
                empty_black_position.append([i,j])
        

#white_open=[[0]*(N) for i in range(N)]
#for i in range(N):
#    for j in range(N):
#        if color=="E" and white_percent>=r:
#            white_open[i][j]=1
#        elif color=="E" and white_percent<r:
#            white_open[i][j]=0
#        else:
#            white_open[i][j]="E"
#empty_position=[[1,2],[2,3],[5,9]]



#black_open=[[0]*(N) for i in range(N)]
#for i in range(N):
#    for j in range(N):
#        if color=="E" and (1-white_percent)>=r:
#            black_open[i][j]=1
#        elif color=="E" and (1-white_percent)<r:
#            black_open[i][j]=0
#        else:
#            black_open[i][j]="E"
print(color)
print(white_percent)

print(empty_white_position)
print(empty_black_position)
print(total_utility)
#if_person=False
#personal_utility=0
#while if_person and personal_utility<r:
#    x_rand=random.randrange(N)
#    y_rand=random.randrange(N)
#    if initial_color[x_rand][y_rand]=="E":


#if people_need_to_move==[]:
#       if empty_black_position==[] and empty_white_position==[]:
#           break
position_code=random.choice(black_need_to_move)
if color[position_code[0],position_code[1]]=="W":
    rand_target_index=random.randrange(len(empty_white_position))