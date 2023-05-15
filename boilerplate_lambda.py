from constants.operations import OPERATIONS

def handler(event, context):
    '''Provide an event that contains the following keys:

      - operation: one of the operations in the operations dict below
      - payload: a JSON object containing parameters to pass to the 
                 operation being performed
    '''
    
    # define the functions used to perform the CRUD operations
    operation = event['operation']
    
    if operation in OPERATIONS:
        return OPERATIONS[operation](event.get('payload'))
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))