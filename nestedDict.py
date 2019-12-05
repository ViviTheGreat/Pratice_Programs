allGuests = {'Alice': {'apples': 5, 'pretzels': 12},'Bob': {'ham sandwiches': 3, 'apples': 2},'Carol': {'cups': 3, 'apple pies': 1}}
#items1 = allGuests.values()
#print items
getItemCount = {}   
for a,b in allGuests.items():
        for x,y in b.items():
            getItemCount.setdefault(x,0)
            getItemCount[x] = getItemCount[x] + y


print getItemCount