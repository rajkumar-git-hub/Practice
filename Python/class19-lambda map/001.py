p_prices=[98,198,298,398]

new_p_prices=list(map(lambda x : x+1 ,  p_prices))

print(new_p_prices)

# method-2
print(list(map(lambda x : x+1 , [98,198,298,398])))

