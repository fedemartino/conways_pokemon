namespace ConwaysPokemon.Gens
{
    public class Generation1 : IGeneration
    {
        public String[] Types { get; set; }
        public (int,int,int)[] Colors {get; set;}
        public Double[][] Effectiveness {get; set;}
        public Generation1()
        {
            this.Types = new String[] { "NOR","FIR","WAT","ELE","GRA","ICE","FIG","POI","GRO","FLY","PSY","BUG","ROC","GHO","DRA" };
            this.Effectiveness = new Double[][] {
                new Double[] {1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1},
                new Double[] {1,0.5,0.5,1,2,2,1,1,1,1,1,2,0.5,1,0.5},
                new Double[] {1,2,0.5,1,0.5,1,1,1,2,1,1,1,2,1,0.5},
                new Double[] {1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5},
                new Double[] {1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5},
                new Double[] {1,1,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2},
                new Double[] {2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1},
                new Double[] {1,1,1,1,2,1,1,0.5,0.5,1,1,2,0.5,0.5,1},
                new Double[] {1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1},
                new Double[] {1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1},
                new Double[] {1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1},
                new Double[] {1,0.5,1,1,2,1,0.5,2,1,0.5,2,1,1,0.5,1},
                new Double[] {1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1},
                new Double[] {0,1,1,1,1,1,1,1,1,1,0,1,1,2,1},
                new Double[] {1,1,1,1,1,1,1,1,1,1,1,1,1,1,2}
            };
            this.Colors = new (int,int,int)[]{
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
                (120, 105, 236)
            };
        }
    }
}