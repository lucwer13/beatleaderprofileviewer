import requests

class getBLdata:

        def getName(id):
                base_url = "https://api.beatleader.xyz"
                request = requests.get(f"{base_url}/player/{id}")
                if request.status_code == 200:
                        data = request.json()
                        name = f"{data['name']}"
                        return f"Name: {name}"
                else:
                        return f"error {request.status_code}"
        
        def getRank(id):
                base_url = "https://api.beatleader.xyz"
                request = requests.get(f"{base_url}/player/{id}")
                if request.status_code == 200:
                        data = request.json()
                        rank = f"{data['rank']}"
                        return f"Rank: {rank}"
                else:
                                return f"error {request.status_code}"
        
        def getPP(id):
                base_url = "https://api.beatleader.xyz"
                request = requests.get(f"{base_url}/player/{id}")
                if request.status_code == 200:
                        data = request.json()
                        pp = f"{data['pp']}"
                        floatingpp = float(pp)
                        roundedpp = round(floatingpp,2)
                        return f"{roundedpp}pp"
                else:
                                return f"error {request.status_code}"
        
        def getAvgRank(id):
                base_url = "https://api.beatleader.xyz"
                request = requests.get(f"{base_url}/player/{id}")
                if request.status_code == 200:
                        data = request.json()
                        avgacc = f"{data['scoreStats']['averageRankedAccuracy']}"
                        firstnumavgacc = avgacc[2:4]
                        inter = int(firstnumavgacc)
                        decimelsacgacc = avgacc[4:6]
                        return f"Avg. ranked acc: {inter}.{decimelsacgacc}%"
                        
                else:
                                return f"error {request.status_code}"