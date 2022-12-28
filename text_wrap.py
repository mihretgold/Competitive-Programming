import textwrap

def wrap(string, max_width):
    list_string = []
    length = len(string)
   
    for index in range (0,length,max_width):
        list_string.append(string[index:index + max_width])
        answer = '\n'.join(list_string)
        # using fill from text wrap library
        # answer = textwrap.fill(string, max_width)  
    return answer
 
if __name__ == '__main__':
