namespace ConwaysPokemon.Desktop;

partial class BoardPainter
{
    /// <summary>
    ///  Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;
    

    /// <summary>
    ///  Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    ///  Required method for Designer support - do not modify
    ///  the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
            this.boardPictureBox = new System.Windows.Forms.PictureBox();
            this.btnPlayPause = new System.Windows.Forms.Button();
            this.btnReset = new System.Windows.Forms.Button();
            this.trackBarSpeed = new System.Windows.Forms.TrackBar();
            ((System.ComponentModel.ISupportInitialize)(this.boardPictureBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBarSpeed)).BeginInit();
            this.SuspendLayout();
            // 
            // boardPictureBox
            // 
            this.boardPictureBox.Location = new System.Drawing.Point(12, 12);
            this.boardPictureBox.Margin = new System.Windows.Forms.Padding(50, 50, 3, 3);
            this.boardPictureBox.Name = "boardPictureBox";
            this.boardPictureBox.Size = new System.Drawing.Size(950, 950);
            this.boardPictureBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.boardPictureBox.TabIndex = 0;
            this.boardPictureBox.TabStop = false;
            // 
            // btnPlayPause
            // 
            this.btnPlayPause.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnPlayPause.Location = new System.Drawing.Point(12, 1123);
            this.btnPlayPause.Name = "btnPlayPause";
            this.btnPlayPause.Size = new System.Drawing.Size(188, 58);
            this.btnPlayPause.TabIndex = 1;
            this.btnPlayPause.Text = "Play";
            this.btnPlayPause.UseVisualStyleBackColor = true;
            this.btnPlayPause.Click += new System.EventHandler(this.btnPlayPause_Click);
            // 
            // btnReset
            // 
            this.btnReset.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnReset.Location = new System.Drawing.Point(206, 1123);
            this.btnReset.Margin = new System.Windows.Forms.Padding(60, 3, 3, 3);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(188, 58);
            this.btnReset.TabIndex = 2;
            this.btnReset.Text = "Reset";
            this.btnReset.UseVisualStyleBackColor = true;
            this.btnReset.Click += new System.EventHandler(this.btnReset_Click);
            // 
            // trackBarSpeed
            // 
            this.trackBarSpeed.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.trackBarSpeed.Location = new System.Drawing.Point(12, 999);
            this.trackBarSpeed.Name = "trackBarSpeed";
            this.trackBarSpeed.Size = new System.Drawing.Size(950, 114);
            this.trackBarSpeed.TabIndex = 4;
            this.trackBarSpeed.Value = 20;
            this.trackBarSpeed.Maximum = 20;
            this.trackBarSpeed.
            this.trackBarSpeed.Scroll += new System.EventHandler(this.trackBarSpeed_Scroll);
            // 
            // BoardPainter
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(17F, 41F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1200, 1196);
            this.Controls.Add(this.trackBarSpeed);
            this.Controls.Add(this.btnReset);
            this.Controls.Add(this.btnPlayPause);
            this.Controls.Add(this.boardPictureBox);
            this.Name = "BoardPainter";
            this.Text = "Conway\'s Pokemon";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.BoardPainter_FormClosing);
            this.Load += new System.EventHandler(this.BoardPainter_Load);
            ((System.ComponentModel.ISupportInitialize)(this.boardPictureBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBarSpeed)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

    }

    #endregion
    private PictureBox boardPictureBox;
    private Button btnPlayPause;
    private Button btnReset;
    private TrackBar trackBarSpeed;
}
