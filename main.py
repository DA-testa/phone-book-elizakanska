# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]
            
def write_res(rez):
    print('\n'.join(rez))
    
def process_q(queries):
    rez = []
    contacts = {}
    for cur_q in queries:
        if cur_q.type == 'add':
            contacts[cur_q.number] = cur_q.name
        elif cur_q.type == 'del':
            if cur_q.number in contacts:
                del contacts[cur_q.number]
        else:
            response = contacts.get(cur_q.number, 'not found')
            rez.append(response)
    return rez

def read_q():
    n = int(input())
    queries = []
    for i in range(n):
        queries.append(Query(input().split()))
    return queries

if __name__ == '__main__':
    write_res(process_q(read_q()))
