#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        best_score = 0
        best_player = ""
        for key in a_dictionary:
            if best_score < a_dictionary[key]:
                best_score = a_dictionary[key]
                best_player = key
        return best_player
    else:
        return (None)
