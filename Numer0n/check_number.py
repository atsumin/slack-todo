def check(guess,answer):
    for i in range(0,n+1):
        for j in range(0,n+1):
            if guess[i]==answer[j]:
                if i ==j:
                    eat_counter=eat_counter+1
                else:
                    bite_counter=bite_counter+1

    print("eat_counter="+eat_counter, "bite_counter="+bite_counter)
