import sys
from ensurepip import __main__


def _format_and_split(line, separator=','):
    return line.strip().split(separator)

def _emit(elements, separator=','):
    elements_as_string = map(str, elements)
    output_string = separator.join(elements_as_string)
    print output_string

def mapper():
    for line in sys.stdin:
        user_id=""
        product_id=""
        location=""
        line_elements=_format_and_split(line)
        if len(line_elements)==5:
            user_id=line_elements[2]
            product_id=line_elements[1]
        else:
            user_id=[0]
            location=line_elements[3]
        #print('%s\t%s\t%s'%(user_id,product_id,location))
        _emit([user_id,product_id,location])
if __name__=='__main__':
    mapper()