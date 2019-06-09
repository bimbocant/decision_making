#bimbocant
#script that calculates the best decision
#to make based on OWA family operators
import pandas as pd

#ask for the alternatives for the problem
alternatives_list=[]
num_alt=input("Please enter the number of alternatives to the problem: ")

# TODO: ask alternatives descriptions

for i in range(1,int(num_alt)+1):
    alternatives_list.append("A"+'{}'.format(i))

print(alternatives_list)

#ask for number of states of nature
states_list=[]
num_states=input("Please enter the number of states of nature to deal with: ")

# TODO: loop over number to enter the states fo nature descriptions

for i in range(1,int(num_states)+1):
    states_list.append("S"+'{}'.format(i))

print(states_list)


#ask for the value(benefit) for each alternative in each state
# TODO: do the same for utilities instead of benefit
values_list=[]
for alt in alternatives_list:
    #saves the value for each combination
    aux=[]
    for state in states_list:
        aux.append(float(input("Please enter benefit for "+alt+" in "+state+": ")))

    #appends the row
    values_list.append(aux)



#show matrix
print(pd.DataFrame(values_list,columns=states_list,index=alternatives_list))

#ask for the decision environment

#controls if an available environment has been selected
env_selected=False

env_list=['risk','uncertainty','risk and uncertainty']
while env_selected is False:
    print("""Please select an environment where to calculate the decision:""")
    c=1
    for envi in env_list:
        print('{}-'.format(c)+envi)
        c=c+1
    environment=input("Option> ")
    if environment not in ['1','2','3']:
        print("Option not available.\n")
    else:
        env_selected=True


#risk environment calculation
#Expected value
#asks for probabilistic information about the possible states of nature
probabilities=[]
for state in states_list:
    while True:
        try:
            prob=float(input("Please enter probability for {}: ".format(state)))
            if prob<=1 and prob>=0:
                probabilities.append(prob)
            else:
                raise ValueError
            break
        except ValueError as e:
            print('Value must be numeric and between one and zero')
        except Exception as e:
            print(e)


#calculate expected value for each alternative
expected_value_list=[]
for alt_index,alt in enumerate(alternatives_list):
    expected_value=0
    for state_index,state in enumerate(states_list):
        expected_value=expected_value+values_list[alt_index][state_index]*probabilities[state_index]
    expected_value_list.append(expected_value)

#select best alternative
# TODO: study cases where there are more repeated max values
print("Expected value for each alternative: ")
print(alternatives_list)
print(expected_value_list)
max_value=max(expected_value_list)
index_of_max=expected_value_list.index(max_value)
print("Best Alternative: {} {}".format(alternatives_list[index_of_max],max_value))

#uncertainty environment calculation
#TODO pesimistic criteria


#TODO optimistic criteria

#TODO hurwicz criteria

#TODO laplace criteria

#TODO Savaje criteria
