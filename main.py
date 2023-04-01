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
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_q in queries:
        if cur_q.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_q.number:
                    contact.name = cur_q.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_q)
        elif cur_q.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_q.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_q.number:
                    response = contact.name
                    break
            rez.append(response)
    return rez

def read_q():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

if __name__ == '__main__':
    write_res(process_q(read_q()))

