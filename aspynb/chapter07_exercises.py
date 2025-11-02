def cells():
    '''
    # 7/ Exercises solutions
    '''

    '''
    '''

    # setup SymPy
    from sympy import *
    init_printing()

    '''
    '''

    '''
    ### E7.3
    
    A group of farmers has formed a cooperative that specializes in three crops:
    arugula, broccoli, and carrots.
    They need to produce 100 tons of arugula,
    200 tons of broccoli,
    and 300 tons of carrots for sale.
    The farmers also need some additional production to feed themselves
    and the work-for-food tourists that come to help them scale up production during the harvest season.
    To feed the workers needed to grow 100 kg of arugula,
    they need to produce an extra 10 kg of broccoli and 10 kg of carrots.
    To produce 100 kg of broccoli,
    it takes 1 kg of arugula and 15 kilograms of carrots.
    To produce 100 kg of carrots,
    it takes 1 kg of arugula
    and 20 kilograms of broccoli.
    How much of each vegetable should the farmers produce?
    '''

    '''
    '''

    # The external demand is
    d = Matrix(
        [100,   # arugula
         200,   # broccoli
         300])  # carrots (in tons)

    '''
    '''

    # The internal demands of production are describe by
    A = Matrix([
    [    0,  0.01,  0.01],
    [  0.1,     0,  0.20],
    [  0.1,  0.15,     0]])

    '''
    '''

    # The required production rates for both internal and external demands:
    x = (eye(3)-A).inv()*d
    x

    '''
    '''


    '''
    '''


    '''
    '''


    '''
    '''

