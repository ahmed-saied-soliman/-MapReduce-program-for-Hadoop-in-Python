import sys

def _format_and_split(line, separator=','):
    return line.strip().split(separator)

def _emit(elements, separator=','):
    elements_as_string = map(str, elements)
    output_string = separator.join(elements_as_string)
    print output_string

def reducer():
    last_user_id=None
    current_location="_"
    for line in sys.stdin:
        line_elements=_format_and_split(line)
        user_id,product_id,location=line_elements
        if not last_user_id or last_user_id!=user_id:
            last_user_id=user_id
            current_location=location
        elif user_id==last_user_id:
            location=current_location
            #print('%s\t%s'%(product_id,location))
            _emit([product_id,location])
if __name__=='__main__':
    reducer()
