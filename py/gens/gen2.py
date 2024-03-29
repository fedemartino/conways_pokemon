class GenData:
    types = ['NOR','FIR','WAT','ELE','GRA','ICE','FIG','POI','GRO','FLY','PSY','BUG','ROC','GHO','DRA','DAR','STE']
    types_colors = [
        (170, 170, 153),
        (235, 73, 40),
        (87, 154, 253),
        (255, 237, 63),
        (137, 203, 89),
        (130, 204, 254),
        (174, 87, 69),
        (160, 88, 152),
        (214, 187, 89),
        (142, 154, 253),
        (236, 90, 153),
        (172, 186, 44),
        (183, 170, 104),
        (104, 103, 186),
        (120, 105, 236),
        (140, 111, 97),
        (183, 183, 197)
    ]

    effectiveness = [
        [1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1,1,0.5],
        [1,0.5,0.5,1,2,2,1,1,1,1,1,2,0.5,1,0.5,1,2],
        [1,2,0.5,1,0.5,1,1,1,2,1,1,1,2,1,0.5,1,1],
        [1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5,1,1],
        [1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5,1,0.5],
        [1,0.5,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2,1,0.5],
        [2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1,2,2],
        [1,1,1,1,2,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,0],
        [1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1,1,2],
        [1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1,1,0.5],
        [1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1,0,0.5],
        [1,0.5,1,1,2,1,0.5,0.5,1,0.5,2,1,1,0.5,1,2,0.5],
        [1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1,1,0.5],
        [0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,0.5,0.5],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0.5],
        [1,1,1,1,1,1,0.5,1,1,1,2,1,1,2,1,0.5,0.5],
        [1,0.5,0.5,0.5,1,2,1,1,1,1,1,1,2,1,1,1,0.5]
    ]
    @classmethod
    def get_types(cls):
        return cls.types
    
    @classmethod
    def get_colors(cls):
        return cls.types_colors
    
    @classmethod
    def get_effectiveness(cls):
        return cls.effectiveness

    