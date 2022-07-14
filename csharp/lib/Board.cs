using ConwaysPokemon.Gens;
namespace ConwaysPokemon;

public class Board
{
    public int Width { get; set; }
    public int Height { get; set; }
    public Int32[,] Cells { get; set; }
    public IGeneration Generation { get; set; }

    public Board(int width, int height, IGeneration gen)
    {
        Random r = new Random();
        Width = width;
        Height = height;
        Cells = new Int32[width, height];
        for (int i = 0; i < width; i++)
        {
            for (int j = 0; j < height; j++)
            {
                Cells[i, j] = r.Next(0, gen.Types.Length);
            }
        }
        Generation = gen;
    }
    public void NextState()
    {
        Random r = new Random();
        for (int x = 0; x < Width; x++)
        {
            for (int y = 0; y < Height; y++)
            {
                int defender = Cells[x, y];
                List<int> winners = new List<int>();
                for (int i = -1; i < 2; i++)
                {
                    for (int j = -1; j < 2; j++)
                    {
                        if ((i == 0 && j == 0) || (x + i < 0 || x + i >= Width || y + j < 0 || y + j >= Height))
                        {
                            continue;
                        }
                        else
                        {
                            int attacker = Cells[x + i, y + j];
                            if (Generation.Effectiveness[attacker][defender] == 2)
                            {
                                winners.Add(attacker);
                            }
                        }
                    }
                }
                if (winners.Count > 0)
                {
                    Cells[x, y] = winners[r.Next(0, winners.Count)];
                }
            }
        }
    }
}