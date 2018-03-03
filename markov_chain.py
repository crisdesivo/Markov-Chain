import numpy as np

class Markov_Chain:
    def __init__(self, number_of_states, starting_state, weights=None):
        self.number_of_states=number_of_states
        if weights==None:
            weights=np.random.rand(number_of_states, number_of_states)
        self.weights=weights/weights.sum(axis=1)[:,None]
        self.starting_state=max(number_of_states -1 , starting_state)
        self.current_state=starting_state
    
    def move_once(self):
        next_state=np.random.choice(range(self.number_of_states), p=self.weights[self.current_state, :])
        self.current_state=next_state
        
    def move(self, moves=1):
        for _ in range(moves):
            previous_state = self.current_state
            self.move_once()
            print("Moved from ", previous_state, " to ", self.current_state)
        
    def count_state(self, number_of_moves):
        counter=[0]*self.number_of_states
        for _ in range(number_of_moves):
            self.move_once()
            counter[self.current_state]+=1
        return counter
            
    def force_move(self, i, j):
        j_vector= [0]*self.number_of_states
        j_vector[j]=1
        j_vector=np.array(j_vector)
        self.weights[i, :]= j_vector
    
    def set_probability(self, i, new_probabilities):
        self.weights[i, :]= new_probabilities/np.sum(new_probabilities)