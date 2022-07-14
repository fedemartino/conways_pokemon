using ConwaysPokemon.Gens;

namespace ConwaysPokemon.Desktop;

public partial class BoardPainter : Form
{
    Board b;
    bool playing = false;
    Thread playThread;
    public BoardPainter()
    {
        InitializeComponent();
        b = new Board(150, 150, new Generation1());
        DrawBoard();
    }
    private void Play()
    {
        while(playing)
        {
            DrawBoard();
            b.NextState();
            Thread.Sleep(sleepTime);
        }
    }
    private void DrawBoard()
    {
        Bitmap boardImage = new Bitmap(b.Height, b.Width);
        int x, y;

        // Loop through the images pixels to reset color.
        for(x=0; x<boardImage.Width; x++)
        {
            for(y=0; y<boardImage.Height; y++)
            {
                (int,int,int) cellColor = b.Generation.Colors[b.Cells[x, y]];
                Color newColor = Color.FromArgb(cellColor.Item1, cellColor.Item2, cellColor.Item3);
                boardImage.SetPixel(x, y, newColor);
            }
        }
        // Set the PictureBox to display the image.
        this.boardPictureBox.Image = boardImage;
    }

    private void btnPlayPause_Click(object sender, EventArgs e)
    {
        if (playing)
        {
            playing = false;
            btnPlayPause.Text = "Play";
        }
        else
        {
            playing = true;
            btnPlayPause.Text = "Pause";
            playThread = new Thread(Play);
            playThread.Start();
        }
    }
    int sleepTime = 0;
    private void btnReset_Click(object sender, EventArgs e)
    {
        this.b = new Board(150, 150, new Generation1());
        DrawBoard();
    }

    private void BoardPainter_Load(object sender, EventArgs e)
    {

    }

    private void BoardPainter_FormClosing(object sender, FormClosingEventArgs e)
    {
        playing = false;
    }

    private void trackBarSpeed_Scroll(object sender, EventArgs e)
    {
        double speed = (-0.1 * trackBarSpeed.Value + 2)*1000;
        sleepTime = Convert.ToInt32(speed);
    }
}
