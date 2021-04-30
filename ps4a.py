# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(e):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(e)==1:
       return e[-1]
    else:
      empty_list=[]
      word=e[0] 
      e=e[1:]
      get_last_letter= get_permutations(e)
      for item in get_last_letter:
         for i in range(0,len(item)+1):
             h=item[:i] + word + item[i:]
             empty_list.append(h)
      return list(set(empty_list))

    

if __name__ == '__main__':
   #EXAMPLE 1
   example_input = 'aeiou'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
   #Example 2
   example_input='aab'
   print('Input:',example_input)
   print('expected output: ',['baa','aba','aab'])
   print('actual_result:',get_permutations(example_input))
   #Example 3
   example_input='ab'
   print('input: ', example_input)
   print('expected output:',['ab','ba'])
   print('actual_result: ',get_permutations(example_input))

  
