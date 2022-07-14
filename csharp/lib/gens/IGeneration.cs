namespace ConwaysPokemon.Gens;

public interface IGeneration
{
    String[] Types { get; set; }
    (int,int,int)[] Colors {get; set;}
    Double[][] Effectiveness {get; set;}
}