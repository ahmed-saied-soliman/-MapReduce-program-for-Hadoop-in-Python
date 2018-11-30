import sys


def _format_and_split(line, separator=','):
    return line.strip().split(separator)

def _emit(elements, separator=','):
    elements_as_string = map(str, elements)
    output_string = separator.join(elements_as_string)
    print output_string

def reducer():
    last_product_id=None
    current_location=""
    count_location=0
    for line in sys.stdin:
        line_elements=_format_and_split(line)
        product_id,location=line_elements
        if not last_product_id:
            last_product_id=product_id
            current_location=location
            count_location=1
        if product_id==last_product_id:
            if location!=current_location:
                count_location=count_location+1
                current_location=location
        else :
            #print ('%s\t%s'%(last_product_id,count_location))
            last_product_id=product_id
            count_location=location
            count_location=1
    _emit([product_id,count_location])
    #print ('%s\t%s'%(product_id,count_location))
if __name__=='__main__':
    reducer()

