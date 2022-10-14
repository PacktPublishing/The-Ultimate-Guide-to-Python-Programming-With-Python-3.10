def log(*values, decor="-", **kwargs):
    
    kwargs.setdefault("padding", 2)
    kwargs.setdefault("end", "\n")

    for value in values:

        value = str(value)
        len_val = len(value)

        prefix = (  
            decor * kwargs['padding'] + 
            decor * len_val + 
            decor * kwargs['padding']
        )

        output = (
            decor * (kwargs['padding'] - 1) +
            " " + value + " " +
            decor * (kwargs['padding'] - 1)
        )

        print(prefix)
        print(output)
        print(prefix, end=kwargs['end'])