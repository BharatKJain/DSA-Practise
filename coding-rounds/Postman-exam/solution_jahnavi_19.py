def fetchCost(cartridges_num,perksCost_num):
    return cartridges_num*perksCost_num
def fetchGreater(a,b):
    if a>b:
        return b
    else:
        return a

if __name__ == "__main__":
    cartridges=int(input())
    dollars=int(input())
    recycleRewards=int(input())
    perksCost=int(input())
    maxCostAllowed=fetchCost(cartridges,perksCost)
    maxPerks=-1
    if maxCostAllowed<=dollars:
        maxPerks=cartridges
    else:
        print(dollars+((cartridges//2)*recycleRewards) > (dollars+((cartridges//2)*recycleRewards)
        for cartridge_count in range(cartridges,0,-1):
            currentWallet=((cartridges-cartridge_count)*recycleRewards)+dollars
            currentPerks=fetchGreater(currentWallet//perksCost,cartridge_count)
            if currentPerks<maxPerks and maxPerks!=-1:
                break
            if currentPerks>maxPerks or maxPerks==-1:
                maxPerks=currentPerks
    print(maxPerks)